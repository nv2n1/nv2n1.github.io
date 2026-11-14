---
title: "gnome-shell(1)"
name: "gnome-shell"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-shell/"
description: "gnome-shell – Graphical shell for the GNOME desktop"
---

<h2 class="name">NAME</h2>
<p> gnome-shell &#8211; Graphical shell for the GNOME desktop </p>
<h2>SYNOPSIS</h2>
<p> <code>gnome-shell</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> GNOME shell provides core user interface functions for the GNOME 3 desktop, like switching to windows and launching applications. GNOME shell takes advantage of the capabilities of modern graphics hardware and introduces innovative user interface concepts to provide a visually attractive and easy to use experience. </p>
<p> gnome-shell is a required component of the GNOME desktop, i.e. it is listed in the RequiredComponents field of /usr/share/gnome-session/sessions/gnome.session. It is started in the window manager phase of the session.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;wayland</code></p>
<dl>
<dt>
<dd> Run as a wayland compositor</dl>
<p> <code>&#8211;display-server</code></p>
<dl>
<dt>
<dd> Run as a full display server, rather than nested</dl>
<p> <code>&#8211;nested</code></p>
<dl>
<dt>
<dd> Run as a nested compositor</dl>
<p> <code>&#8211;no-x11</code></p>
<dl>
<dt>
<dd> Run wayland compositor without starting Xwayland</dl>
<p> <code>&#8211;x11</code></p>
<dl>
<dt>
<dd> Run with X11 backend</dl>
<p> <code>&#8211;wayland-display</code>=<i>DISPLAY</i></p>
<dl>
<dt>
<dd> Wayland display name to use</dl>
<p> <code>-d</code>, <code>&#8211;display</code>=<i>DISPLAY</i></p>
<dl>
<dt>
<dd> X display to use</dl>
<p> <code>-r</code>, <code>&#8211;replace</code></p>
<dl>
<dt>
<dd> Replace the running window manager</dl>
<p> <code>&#8211;sm-disable</code></p>
<dl>
<dt>
<dd> Disable connection to the session manager</dl>
<p> <code>&#8211;sm-client-id</code>=<i>ID</i></p>
<dl>
<dt>
<dd> Specify session management <i>ID</i></dl>
<p> <code>&#8211;sm-save-file</code>=<i>FILE</i></p>
<dl>
<dt>
<dd> Initialize session from <i>FILE</i></dl>
<p> <code>&#8211;sync</code></p>
<dl>
<dt>
<dd> Make X calls synchronous</dl>
<p> <code>&#8211;mode</code>=<i>MODE</i></p>
<dl>
<dt>
<dd> Use a specific mode, e.g. &quot;gdm&quot; for login screen</dl>
<p> <code>&#8211;list-modes</code></p>
<dl>
<dt>
<dd> List possible modes and exit</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version and exit</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help and exit</dl>
<h2>FILES</h2>
<p> /usr/share/gnome-session/sessions/gnome.session, /usr/share/applications/org.gnome.Shell.desktop.</p>
<h2>BUGS</h2>
<p> The bug tracker can be reached by visiting the website m[blue]<code><a rel="nofollow" href="https://gitlab.gnome.org/GNOME/gnome-shell/issues">https://gitlab.gnome.org/GNOME/gnome-shell/issues</a></code>m[]. Before sending a bug report, please verify that you have the latest version of gnome-shell. Many bugs (major and minor) are fixed at each release, and if yours is out of date, the problem may already have been solved.</p>
<h2>ADDITIONAL INFORMATION</h2>
<p> For further information, visit the website m[blue]<code><a rel="nofollow" href="https://wiki.gnome.org/Projects/GnomeShell">https://wiki.gnome.org/Projects/GnomeShell</a></code>m[]. </p>
<h2>Index</h2>
