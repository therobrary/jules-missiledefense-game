# Missile Defense
A modern, sleek, grayscale arcade game inspired by the classic Missile Command. Built with HTML5 Canvas and JavaScript in a single file.

## How to Play
1.  **Objective**: Defend your 6 cities from incoming ballistic missiles.
2.  **Controls**:
    *   **Desktop**: Click anywhere on the screen to launch a counter-missile from your silo.
    *   **Mobile**: Tap on the screen to launch.
3.  **Mechanics**:
    *   **Ammo**: You have limited ammo per wave. Use it wisely.
    *   **Explosions**: Your missiles create expanding explosions. Any enemy missile touching the explosion is destroyed.
    *   **Chain Reactions**: Destroying multiple enemies with one explosion maximizes efficiency.
    *   **Waves**: Difficulty increases with each wave (faster enemies, more missiles).
    *   **Scoring**:
        *   Destroy Enemy: 25 pts
        *   Wave Bonus: 100 pts per surviving City + 5 pts per leftover Ammo.

## Visual Style
*   **Modern Sleek Grayscale**: High-contrast black and white aesthetic.
*   **Neon Glow**: All game entities emit a glow using Canvas shadow effects.
*   **Glassmorphism**: UI elements feature semi-transparent, blurred backgrounds.
*   **Effects**: Particle explosions, screen shake, and missile trails.

## Tech Stack
*   **HTML5 Canvas**: For high-performance 2D rendering.
*   **Vanilla JavaScript (ES6+)**: No external libraries or frameworks.
*   **CSS3**: For UI overlays and typography.
*   **LocalStorage**: Persists high scores locally.
