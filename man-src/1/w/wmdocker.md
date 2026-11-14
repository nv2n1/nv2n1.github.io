---
title: "wmdocker(1)"
name: "wmdocker"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmdocker/"
description: "wmdocker – System tray for KDE3/GNOME2 docklet applications"
---

<h2 class="name">NAME</h2>
<p> wmdocker &#8211; System tray for KDE3/GNOME2 docklet applications </p>
<h2>SYNOPSIS</h2>
<p> <code>wmdocker</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>wmdocker</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. </p>
<p> <code>wmdocker</code> is a docking application (WindowMaker dock app) which acts as a system tray for KDE3 and GNOME2. It can be used to replace the panel in either environment, allowing you to have a system tray without running the KDE/GNOME panel. </p>
<p> Docker was written and designed to work with Openbox 2, but it should work fine in any window manager that supports WindowMaker dock apps. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h-help</code></p>
<dd> Show summary of options.</p>
<dt><code>-display DISPLAY</code></p>
<dd> The X display to connect to.</p>
<dt><code>-border N</code></p>
<dd> The width of the border to put around the system tray icons. Defaults to 1.</p>
<dt><code>-vertical</code></p>
<dd> Line up the icons vertically. Defaults to horizontally.</p>
<dt><code>-wmaker</code></p>
<dd> WindowMaker mode. This makes wmdocker a fixed size (64&#215;64) to appear nicely in in WindowMaker. Note: In this mode, you have a fixed number of icons that wmdocker can hold.</p>
<dt><code>-iconsize SIZE</code></p>
<dd> The size (width and height and height) to display icons as in the system tray. Defaults to 24.</p>
<dt><code>-color COLOR</code></p>
<dd> The background color to use for the tray. Defaults to whatever color the window manager specifies.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Ari Pollak &lt;ari [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
