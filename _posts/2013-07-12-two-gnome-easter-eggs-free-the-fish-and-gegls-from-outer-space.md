---
title: "GNOME\u2019s Hidden Easter Eggs: Free the Fish and Gegl from Outer Space"
date: 2013-07-12 16:32:16 +0000
layout: post
canonical: https://www.systutorials.com/two-gnome-easter-eggs-free-the-fish-and-gegls-from-outer-space/
---

GNOME has hidden a few playful easter eggs in its desktop environment over the years. Two of the most well-known are “Free the Fish” and “Wanda the Fish” — small animated features that surprise unsuspecting users.

## Free the Fish (GNOME 2)

In GNOME 2, pressing **Alt+F2** and running this command:

```wp-block-code
free the fish
```

releases a small fish (Wanda) that swims across your desktop. The fish bounces around the screen edges and eventually disappears. It’s a harmless bit of fun that the GNOME developers included as a hidden feature.

You could also trigger it by running:

```wp-block-code
gnome-panel --run-dialog
```

and typing “free the fish” in the dialog.

## Getting Rid of Wanda

If Wanda is still swimming around and you want her gone, the most reliable method is to restart the GNOME panel:

```wp-block-code
killall gnome-panel
```

The panel automatically restarts, and the fish disappears. If that doesn’t work, logging out and back in will also clear it.

Some users reported that Wanda would reappear after being “freed.” To permanently prevent this:

```wp-block-code
gconftool-2 --set /apps/gnome-panel/global/enable_wanda --type bool false
```

## Gegl from Outer Space (GNOME 2)

Another easter egg in GNOME 2 was triggered by pressing **Alt+F2** and typing:

```wp-block-code
gegls from outer space
```

This launched a simple game where small alien creatures (gegls) would appear on your desktop and you could click on them. The game referenced GEGL (Generic Graphics Library), the image processing framework used by GIMP.

The gegls game was a simple reflex-clicking challenge — aliens would appear at random positions on the screen and you’d try to click them before they disappeared. It kept score of how many you caught.

## Modern GNOME (3.x and Later)

Most of these easter eggs were removed in GNOME 3 during the desktop rewrite. The new GNOME Shell doesn’t include “Free the Fish” or “Gegl from Outer Space” as built-in features. The **Alt+F2** run dialog still exists, but typing these commands no longer triggers any hidden behavior.

However, GNOME 3 has its own lesser-known features:

- Type `lg` in Alt+F2 to open the Looking Glass debugger (for GNOME Shell extension development)
- Type `r` in Alt+F2 to restart the GNOME Shell (useful when debugging extensions without logging out)
- Type `rt` to restart the GNOME Shell with a clean state

## Why Easter Eggs Matter

Desktop easter eggs are a tradition in software development. They show that developers have a sense of humor and make the software feel more human. Famous examples include:

- **Google’s “do a barrel roll”** — search for it and the page rotates 360 degrees
- **Firefox’s “about:robots”** — displays a robot-themed page
- **Chrome’s dinosaur game** — press Space when offline to play
- **apt-get moo** — displays an ASCII cow in Debian/Ubuntu

These hidden features have become less common in modern software as companies focus on security and professional appearance. But they remain a beloved part of computing culture and open-source tradition.

## Other GNOME Hidden Features

While not technically easter eggs, GNOME has several hidden or hard-to-discover features worth knowing:

**Tweak Tool:** Install GNOME Tweaks to access settings that aren’t exposed in the default Settings panel:

```wp-block-code
sudo dnf install gnome-tweaks    # Fedora
sudo apt install gnome-tweaks    # Ubuntu/Debian
```

**Extension management:** Visit <a href="https://extensions.gnome.org" rel="nofollow noopener" target="_blank">extensions.gnome.org</a> to browse and install community extensions that add functionality to GNOME Shell.

**D-Bus inspector:** Use `d-feet` to explore the D-Bus interfaces that GNOME applications expose — useful for scripting desktop interactions.
