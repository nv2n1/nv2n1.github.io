---
title: "cinnamon-settings-daemon(1)"
name: "cinnamon-settings-daemon"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cinnamon-settings-daemon/"
description: "cinnamon-settings-daemon – Cinnamon settings daemon"
---

<h2 class="name">NAME</h2>
<p> cinnamon-settings-daemon &#8211; Cinnamon settings daemon </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cinnamon-settings-daemon </code><code>[OPTION&#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>cinnamon-settings-daemon</code></p>
<dd>provides many session-wide services and functions that require a long-running process. Among the services implemented by cinnamon-settings-daemon are an XSettings manager, which provides theming, font and other settings to GTK+ applications, and a clipboard manager, which preserves clipboard contents when an application exits. Many user interface elements of <code>cinnamon</code> and <code>cinnamon-settings</code> rely on cinnamon-settings-daemon for their functionality. </p>
<p> The internal architecture of cinnamon-settings-daemon consists of a number of plugins, which provide functionality such as printer notifications, software update monitoring, background changing, etc. For debugging purposes, these plugins can be individually disabled by changing the gsettings key org.cinnamon.settings-daemon.plugins.<i>plugin-name</i>.active, where <i>plugin-name</i> is the name of the plugin. To see a list of all plugins, use the command <code> gsettings list-children org.cinnamon.settings-daemon.plugins </code> </p>
<p> cinnamon-settings-daemon takes the name org.cinnamon.SettingsDaemon on the session bus to ensure that only one instance is running. Some plugins export objects under this name to make their functionality available to other applications. The interfaces of these objects should generally be considered private and unstable. </p>
<p> cinnamon-settings-daemon is a required component of the Cinnamon desktop, i.e. it is listed in the RequiredComponents field of /usr/share/cinnamon-session/sessions/cinnamon.session. It is started in the initialization phase of the session, and <code>cinnamon-session</code> will restart it if it crashes.</p>
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
<p> /usr/share/cinnamon-session/sessions/cinnamon.session</p>
<dl>
<dt>
<dd> GNOME session definition file where cinnamon-settings-daemon is listed as a required component.</dl>
<p> /etc/xdg/autostart/cinnamon-settings-daemon.desktop</p>
<dl>
<dt>
<dd> Autostart file for cinnamon-settings-daemon, where its autostart phase is set.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cinnamon/">cinnamon</a></code>(1), <code><a href="/docs/linux/man/1-cinnamon-settings/">cinnamon-settings</a></code>(1), <code><a href="/docs/linux/man/1-cinnamon-session/">cinnamon-session</a></code>(1) </p>
<h2>Index</h2>
