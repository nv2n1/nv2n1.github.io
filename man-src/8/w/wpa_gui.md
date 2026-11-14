---
title: "wpa_gui(8)"
name: "wpa_gui"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wpa_gui/"
description: "wpa_gui – WPA Graphical User Interface"
---

<p>wpa_gui &#8211; WPA Graphical User Interface</p>
<h2>Synopsis</h2>
<p><code>wpa_gui</code> [ <code>-p </code><i>path to ctrl sockets</i> ] [ <code>-i </code><i>ifname</i> ] [ <code>-m </code><i>seconds</i> ] [ <code>-t</code> ] [ <code>-q</code> ]</p>
<h2>Overview</h2>
<p>wpa_gui is a QT graphical frontend program for interacting with wpa_supplicant. It is used to query current status, change configuration and request interactive user input. </p>
<p> wpa_gui supports (almost) all of the interactive status and configuration features of the command line client, wpa_cli. Refer to the wpa_cli manpage for a comprehensive list of the interactive mode features.</p>
<h2>Command Arguments</h2>
<dl>
<dt><code>-p path</code></p>
<dd>Change the path where control sockets should be found.</p>
<dt><code>-i ifname</code></p>
<dd>Specify the interface that is being configured. By default, choose the first interface found with a control socket in the socket path.</p>
<dt><code>-m seconds</code></p>
<dd>Set the update interval in seconds for the signal strength meter. This value must be a positive integer, otherwise meter is not enabled (default behavior).</p>
<dt><code>-t</code></p>
<dd>Start program in the system tray only (if the window manager supports it). By default the main status window is shown.</p>
<dt><code>-q</code></p>
<dd>Run program in the quiet mode &#8211; do not display tray icon pop-up messages.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wpa_cli/">wpa_cli</a></code>(8) <code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a></code>(8)</p>
<h2>Legal</h2>
<p>wpa_supplicant is copyright (c) 2003-2016, Jouni Malinen &lt;j@w1.fi&gt; and contributors. All Rights Reserved. </p>
<p> This program is licensed under the BSD license (the one with advertisement clause removed).</p>
