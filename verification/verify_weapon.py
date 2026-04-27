from playwright.sync_api import sync_playwright

def verify_weapon():
    """Verify weapon toggle behavior with new HUD labels and styling."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the game
        page.goto("http://localhost:8080/docs/index.html")
        page.wait_for_selector("canvas")

        # Start the game
        page.click("#startBtn")
        page.wait_for_timeout(500)

        # Verify UI elements are present
        weapon_toggle = page.locator("#weaponToggle")
        assert weapon_toggle.is_visible(), "Weapon toggle should be visible"

        weapon_display = page.locator("#weaponDisplay")

        # Initial state: NORMAL
        assert "NORMAL" in weapon_display.inner_text(), "Weapon should start as NORMAL"
        page.screenshot(path="verification/weapon_toggle_initial.png")

        # Toggle to FLAK via click
        weapon_toggle.click()
        page.wait_for_timeout(200)
        assert "FLAK" in weapon_display.inner_text(), "Weapon text should contain FLAK after toggle"

        # Verify flak-active class is applied
        flak_active = weapon_toggle.get_attribute("class")
        assert "flak-active" in flak_active, "Weapon toggle should have flak-active class when FLAK is selected"

        page.screenshot(path="verification/weapon_toggle_flak.png")

        # Toggle back to NORMAL via keyboard (Shift)
        page.keyboard.press("Shift")
        page.wait_for_timeout(200)
        assert "NORMAL" in weapon_display.inner_text(), "Weapon text should be NORMAL after Shift toggle"

        # Verify flak-active class is removed
        flak_active = weapon_toggle.get_attribute("class")
        assert "flak-active" not in flak_active, "Weapon toggle should not have flak-active class when NORMAL is selected"

        browser.close()
        print("All weapon toggle checks passed!")

if __name__ == "__main__":
    verify_weapon()
