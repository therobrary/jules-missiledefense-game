# Deployment Guide: GitHub Pages

This guide outlines how to deploy the `Missile Defense` game to GitHub Pages. Since the entire game is contained in a single `index.html` file, the process is straightforward.

## Prerequisites
*   A GitHub account.
*   This repository containing `index.html`.

## Steps

1.  **Push Code to GitHub**
    *   Ensure `index.html` is in the root directory of your repository.
    *   Commit and push your changes to the `main` (or `master`) branch.

2.  **Enable GitHub Pages**
    *   Go to your repository page on GitHub.
    *   Click on **Settings** (top right tab).
    *   On the left sidebar, click on **Pages** (under the "Code and automation" section).

3.  **Configure Build Source**
    *   Under **Source**, select **Deploy from a branch**.
    *   Under **Branch**, select `main` (or your default branch) and `/ (root)`.
    *   Click **Save**.

4.  **Verify Deployment**
    *   GitHub will now build and deploy your site. This may take a minute.
    *   Refresh the Pages settings page. You should see a banner at the top saying:
        > "Your site is live at https://<username>.github.io/<repository-name>/"
    *   Click the link to play your game!

## Troubleshooting
*   **404 Error**: Ensure your file is named exactly `index.html`. GitHub Pages looks for this specific file by default.
*   **Changes not showing**: You might need to do a hard refresh (Ctrl+F5 or Cmd+Shift+R) in your browser to clear the cache.
