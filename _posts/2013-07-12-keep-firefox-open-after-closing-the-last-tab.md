---
title: "Prevent Firefox from Closing When Last Tab Closes"
date: 2013-07-12 16:54:48 +0000
modified: 2026-04-12 10:58:27 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /keep-firefox-open-after-closing-the-last-tab/
---

By default, Firefox closes the entire window when you close the last tab. This can be annoying if you’re used to keeping the browser window open. Here’s how to change this behavior and other useful tab management tips.

## Prevent Firefox from Closing: about:config

1.  Open a new tab and type `about:config` in the address bar
2.  Click “Accept the Risk and Continue”
3.  In the search box, type `browser.tabs.closeWindowWithLastTab`
4.  Double-click the entry to change it from `true` to `false`

Now when you close the last tab, Firefox opens a new blank tab instead of closing the entire window. The change takes effect immediately.

## Why Firefox Does This by Default

The behavior matches how most desktop applications work: closing the last document or item closes the application window. For casual users, this feels natural. Power users who manage many tabs throughout the day often prefer the window to stay open, which is why this preference exists.

## Alternative: user.js for Persistent Configuration

If you want this setting to persist across Firefox updates and profile resets, add it to a `user.js` file:

```wp-block-code
// In your Firefox profile directory
// Find it: about:support → Profile Directory → Open Directory
// Create or edit: user.js

user_pref("browser.tabs.closeWindowWithLastTab", false);
```

The `user.js` file is read on every Firefox startup and overrides any changes made through about:config. This is useful for managed environments or when you want to ensure your preferences survive profile resets.

## Other Essential Tab Preferences

While you’re in about:config, these related settings improve tab management:

**Move new tabs next to the current tab (instead of at the end):**

```wp-block-code
browser.tabs.insertRelatedAfterCurrent = true
```

**Warn when closing a window with multiple tabs:**

```wp-block-code
browser.tabs.warnOnClose = true
browser.tabs.warnOnCloseOtherTabs = true
```

**Enable tab previews on hover:**

```wp-block-code
browser.tabs.cardPreview.enabled = true
browser.tabs.cardPreview.delayMs = 500
```

**Control where new windows open:**

```wp-block-code
browser.link.open_newwindow.restriction = 0
```

## Keyboard Shortcuts for Tab Power Users

Master these shortcuts to manage tabs efficiently:

- `Ctrl+T` — New tab
- `Ctrl+W` — Close current tab
- `Ctrl+Shift+T` — Reopen last closed tab (works multiple times!)
- `Ctrl+Tab` — Switch to next tab
- `Ctrl+Shift+Tab` — Switch to previous tab
- `Ctrl+1` through `Ctrl+9` — Switch to specific tab by position (9 goes to last tab)
- `Ctrl+L` — Focus address bar
- `Alt+Enter` — Open address bar content in new tab
- `Middle-click` on a tab — Close it
- `Middle-click` on a link — Open in new tab
- `Ctrl+click` on a link — Open in new tab (foreground)
- `Ctrl+Shift+click` on a link — Open in new tab and switch to it

## Tab Management Extensions

Firefox extensions that enhance tab handling:

- **Tab Session Manager** — Save and restore tab sessions across restarts
- **OneTab** — Convert all open tabs into a shareable list to save memory
- **Tree Style Tab** — Display tabs in a vertical tree hierarchy in the sidebar
- **Sidebery** — Modern vertical tab bar with bookmarks and containers
- **Multi-account Containers** — Mozilla’s official extension for isolating tabs by context (work, personal, banking)

## Firefox Container Tabs

Containers are a built-in Firefox feature (enhanced by the extension) that let you separate browsing contexts:

- Each container has its own cookies, storage, and login state
- Log into the same site with different accounts in different containers
- Keep work browsing separate from personal
- Isolate banking and shopping from regular browsing

Right-click the New Tab button or use the Containers extension to open a tab in a specific container.

## Memory Management with Many Tabs

If you tend to accumulate tabs, Firefox has built-in memory management:

- **Tab unload** — Firefox automatically unloads tabs you haven’t viewed recently, freeing memory while keeping them visible
- **about:unloads** — Manually see which tabs are loaded and unload specific ones
- **about:performance** — See which tabs and extensions are using the most resources

For extreme tab hoarders (100+ tabs), consider using bookmarks instead. `Ctrl+D` bookmarks the current tab, and you can organize bookmarks into folders for later access.

## Quick Reference

- `about:config` → `browser.tabs.closeWindowWithLastTab` → `false` — Prevent close
- `Ctrl+Shift+T` — Undo close tab
- `Ctrl+W` — Close tab
- `about:performance` — Check tab resource usage
- `user.js` — Persist settings across restarts
