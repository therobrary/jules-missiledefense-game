
from playwright.sync_api import sync_playwright

def verify_game_load():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the game
        page.goto("http://localhost:8080/docs/index.html")

        # Wait for canvas to exist
        page.wait_for_selector("canvas")

        # Wait for Start Screen
        page.wait_for_selector("#startScreen")

        # Take screenshot of Start Screen
        page.screenshot(path="verification/start_screen.png")
        print("Start screen screenshot taken.")

        # Click Start
        page.click("#startBtn")

        # Wait a bit for game to start and things to draw
        page.wait_for_timeout(2000)

        # Trigger a shot to test sound (though we can't hear it in screenshot) and ammo update
        # Click near the top
        page.mouse.click(400, 100)

        # Wait for missile to fly a bit
        page.wait_for_timeout(500)

        # Take screenshot of Gameplay
        page.screenshot(path="verification/gameplay.png")
        print("Gameplay screenshot taken.")

        browser.close()

if __name__ == "__main__":
    verify_game_load()
