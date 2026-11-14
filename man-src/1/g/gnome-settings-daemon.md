---
title: "gnome-settings-daemon(1)"
name: "gnome-settings-daemon"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-settings-daemon/"
description: "gnome-settings-daemon – GNOME settings daemon"
---

<h2 class="name">NAME</h2>
<p> gnome-settings-daemon &#8211; GNOME settings daemon </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gnome-settings-daemon </code><code>[OPTION&#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>gnome-settings-daemon</code></p>
<dd>provides many session-wide services and functions that require a long-running process. Among the services implemented by gnome-settings-daemon are an XSettings manager, which provides theming, font and other settings to GTK+ applications, and a clipboard manager, which preserves clipboard contents when an application exits. Many user interface elements of <code>gnome-shell</code> and <code>gnome-control-center</code> rely on gnome-settings-daemon for their functionality. </p>
<p> The internal architecture of gnome-settings-daemon consists of a number of plugins, which provide functionality such as printer notifications, software update monitoring, background changing, etc. For debugging purposes, these plugins can be individually disabled by changing the gsettings key org.gnome.settings-daemon.plugins.<i>plugin-name</i>.active, where <i>plugin-name</i> is the name of the plugin. To see a list of all plugins, use the command <code> gsettings list-children org.gnome.settings-daemon.plugins </code> </p>
<p> gnome-settings-daemon takes the name org.gnome.SettingsDaemon on the session bus to ensure that only one instance is running. Some plugins export objects under this name to make their functionality available to other applications. The interfaces of these objects should generally be considered private and unstable. </p>
<p> gnome-settings-daemon is a required component of the GNOME desktop, i.e. it is listed in the RequiredComponents field of /usr/share/gnome-session/sessions/gnome.session. It is started in the initialization phase of the session, and <code>gnome-session</code> will restart it if it crashes.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints a short help text and exits.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Enables debugging code.</dl>
<p> <code>&#8211;timed-exit</code></p>
<dl>
<dt>
<dd> Exits after a timeout (30 seconds) for debugging.</dl>
<h2>FILES</h2>
<p> /usr/share/gnome-session/sessions/gnome.session</p>
<dl>
<dt>
<dd> GNOME session definition file where gnome-settings-daemon is listed as a required component.</dl>
<p> /etc/xdg/autostart/gnome-settings-daemon.desktop</p>
<dl>
<dt>
<dd> Autostart file for gnome-settings-daemon, where its autostart phase is set.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnome-shell/">gnome-shell</a></code>(1), <code><a href="/docs/linux/man/1-gnome-control-center/">gnome-control-center</a></code>(1), <code><a href="/docs/linux/man/1-gnome-session/">gnome-session</a></code>(1) </p>
<h2>Index</h2>
