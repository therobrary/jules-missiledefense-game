
from playwright.sync_api import sync_playwright

def verify_game():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the game
        page.goto("http://localhost:8080/docs/index.html")

        # Start the game
        page.click("#startBtn")

        # Verify UI elements are present
        weapon_toggle = page.locator("#weaponToggle")
        assert weapon_toggle.is_visible(), "Weapon toggle should be visible"

        # Take screenshot of initial state
        page.screenshot(path="verification/weapon_toggle_initial.png")

        # Toggle weapon via click
        weapon_toggle.click()

        # Verify text changed to FLAK (3) and color changed
        weapon_display = page.locator("#weaponDisplay")
        assert "FLAK (3)" in weapon_display.inner_text(), "Weapon text should be FLAK (3)"

        # Take screenshot of toggled state
        page.screenshot(path="verification/weapon_toggle_flak.png")

        # Toggle weapon via keyboard (Shift)
        page.keyboard.press("Shift")

        # Verify text changed back to NORMAL
        assert "NORMAL" in weapon_display.inner_text(), "Weapon text should be NORMAL"

        browser.close()

if __name__ == "__main__":
    verify_game()
