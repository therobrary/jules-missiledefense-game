from playwright.sync_api import sync_playwright

def verify_game_flow():
    """Verify the complete game flow: start, HUD labels, pause, game-over, reboot."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the game
        page.goto("http://localhost:8080/docs/index.html")
        page.wait_for_selector("canvas")

        # --- Start Screen ---
        assert page.is_visible("#startScreen"), "Start screen should be visible"
        start_title = page.locator("#startScreen .overlay-card h1").inner_text().upper()
        assert "MISSILE DEFENSE" in start_title, f"Title should say 'MISSILE DEFENSE', got: {start_title}"
        assert "MISSLE" not in start_title, "Typo 'Missle' should not appear"

        start_btn = page.locator("#startBtn")
        assert start_btn.is_visible(), "Start button should be visible"
        assert "INITIATE" in start_btn.inner_text(), "Start button should say INITIATE"

        page.screenshot(path="verification/start_screen.png")
        print("Start screen screenshot taken.")

        # --- Start Game ---
        page.click("#startBtn")
        page.wait_for_timeout(1500)

        start_class = page.locator("#startScreen").get_attribute("class")
        assert "hidden" in start_class, f"Start screen should be hidden after start, got: {start_class}"

        # --- HUD Labels ---
        score_labels = page.locator("#hud .hud-label").all_inner_texts()
        assert "SCORE" in score_labels, f"HUD should contain SCORE, got: {score_labels}"
        assert "HI-SCORE" in score_labels, f"HUD should contain HI-SCORE, got: {score_labels}"
        assert "WAVE" in score_labels, f"HUD should contain WAVE, got: {score_labels}"
        assert "LIVES" in score_labels, f"HUD should contain LIVES, got: {score_labels}"
        assert "AMMO" in score_labels, f"HUD should contain AMMO, got: {score_labels}"
        assert "WEAPON" in score_labels, f"HUD should contain WEAPON, got: {score_labels}"

        weapon_display = page.locator("#weaponDisplay")
        assert "NORMAL" in weapon_display.inner_text(), "Weapon should start as NORMAL"

        page.screenshot(path="verification/gameplay.png")
        print("Gameplay screenshot taken.")

        # --- Pause (dispatch event directly due to user-select: none on *) ---
        page.evaluate('''() => {
            const event = new KeyboardEvent('keydown', {code: 'Space', key: ' ', bubbles: true});
            window.dispatchEvent(event);
        }''')
        page.wait_for_timeout(500)

        pause_class = page.locator("#pauseScreen").get_attribute("class")
        assert "hidden" not in pause_class, f"Pause overlay should be visible, got class: {pause_class}"

        paused_title = page.locator("#pauseScreen .overlay-card h1").inner_text().upper()
        assert "PAUSED" in paused_title, f"Pause overlay should say PAUSED, got: {paused_title}"

        page.screenshot(path="verification/paused_state.png")
        print("Paused state screenshot taken.")

        # Unpause
        page.evaluate('''() => {
            const event = new KeyboardEvent('keydown', {code: 'Space', key: ' ', bubbles: true});
            window.dispatchEvent(event);
        }''')
        page.wait_for_timeout(500)
        pause_class = page.locator("#pauseScreen").get_attribute("class")
        assert "hidden" in pause_class, f"Pause overlay should be hidden after unpause, got class: {pause_class}"

        # --- Weapon Toggle ---
        page.locator("#weaponToggle").click()
        page.wait_for_timeout(200)
        assert "FLAK" in weapon_display.inner_text(), "Weapon should be FLAK after toggle"

        page.locator("#weaponToggle").click()
        page.wait_for_timeout(200)
        assert "NORMAL" in weapon_display.inner_text(), "Weapon should be NORMAL after second toggle"

        page.screenshot(path="verification/weapon_toggle_initial.png")
        page.locator("#weaponToggle").click()
        page.wait_for_timeout(200)
        page.screenshot(path="verification/weapon_toggle_flak.png")
        print("Weapon toggle screenshots taken.")

        # --- End Game via ESC (dispatch event directly) ---
        page.evaluate('''() => {
            const event = new KeyboardEvent('keydown', {code: 'Escape', key: 'Escape', bubbles: true});
            window.dispatchEvent(event);
        }''')
        page.wait_for_timeout(500)

        go_class = page.locator("#gameOverScreen").get_attribute("class")
        assert "hidden" not in go_class, f"Game over screen should be visible, got class: {go_class}"

        fail_title = page.locator("#gameOverScreen .overlay-card h1").inner_text().upper()
        assert "MISSION FAILED" in fail_title, f"Game over should say MISSION FAILED, got: {fail_title}"

        reboot_btn = page.locator("#restartBtn")
        assert reboot_btn.is_visible(), "REBOOT button should be visible"
        assert "REBOOT" in reboot_btn.inner_text(), "Restart button should say REBOOT"

        # --- Reboot ---
        page.click("#restartBtn")
        page.wait_for_timeout(1000)
        go_class2 = page.locator("#gameOverScreen").get_attribute("class")
        assert "hidden" in go_class2, f"Game over screen should be hidden after reboot, got class: {go_class2}"

        browser.close()
        print("All game flow checks passed!")

if __name__ == "__main__":
    verify_game_flow()
