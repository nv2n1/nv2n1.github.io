---

title: "wmdocker(1)"
name: "wmdocker"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmdocker/"
description: "wmdocker – System tray for KDE3/GNOME2 docklet applications"
---

<p> <code>wmdocker</code> [<i>options</i>]</p>
<p> This manual page documents briefly the <code>wmdocker</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. </p>
<p> <code>wmdocker</code> is a docking application (WindowMaker dock app) which acts as a system tray for KDE3 and GNOME2. It can be used to replace the panel in either environment, allowing you to have a system tray without running the KDE/GNOME panel. </p>
<p> Docker was written and designed to work with Openbox 2, but it should work fine in any window manager that supports WindowMaker dock apps. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h-help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-display DISPLAY</code></dt>
<dd> The X display to connect to.</dd>
<dt><code>-border N</code></dt>
<dd> The width of the border to put around the system tray icons. Defaults to 1.</dd>
<dt><code>-vertical</code></dt>
<dd> Line up the icons vertically. Defaults to horizontally.</dd>
<dt><code>-wmaker</code></dt>
<dd> WindowMaker mode. This makes wmdocker a fixed size (64&#215;64) to appear nicely in in WindowMaker. Note: In this mode, you have a fixed number of icons that wmdocker can hold.</dd>
<dt><code>-iconsize SIZE</code></dt>
<dd> The size (width and height and height) to display icons as in the system tray. Defaults to 24.</dd>
<dt><code>-color COLOR</code></dt>
<dd> The background color to use for the tray. Defaults to whatever color the window manager specifies.</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Ari Pollak &lt;ari [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
