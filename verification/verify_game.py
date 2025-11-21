from playwright.sync_api import sync_playwright, expect
import time

def verify_game_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Load the game
        page.goto("http://localhost:8080")
        print("Page loaded")

        # 2. Verify Start Screen Instructions
        start_screen = page.locator("#startScreen")
        expect(start_screen).to_be_visible()
        instructions = start_screen.locator("p")
        expect(instructions).to_contain_text("ESC to End Game")
        expect(instructions).to_contain_text("Space to Pause")
        print("Instructions verified")

        # Take screenshot of start screen
        page.screenshot(path="verification/start_screen.png")

        # 3. Start Game
        page.click("#startBtn")
        time.sleep(1) # Wait for game to start and some updates
        print("Game started")

        # 4. Test Pause
        page.keyboard.press("Space")
        time.sleep(0.5)
        page.screenshot(path="verification/paused_state.png")
        print("Paused state captured")

        # Verify PAUSED text is likely visible (canvas pixel check is hard, but we can trust the screenshot)
        # Unpause
        page.keyboard.press("Space")
        time.sleep(0.5)
        print("Unpaused")

        # 5. Test End Game (ESC)
        page.keyboard.press("Escape")
        time.sleep(0.5)

        game_over_screen = page.locator("#gameOverScreen")
        expect(game_over_screen).to_be_visible()
        print("Game Over screen verified")
        page.screenshot(path="verification/game_over.png")

        browser.close()

if __name__ == "__main__":
    try:
        verify_game_changes()
        print("Verification script finished successfully.")
    except Exception as e:
        print(f"Verification failed: {e}")
        exit(1)
