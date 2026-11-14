---
title: "nmtui(1)"
name: "nmtui"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nmtui/"
description: "nmtui – Text User Interface for controlling NetworkManager"
---

<h2 class="name">NAME</h2>
<p> nmtui &#8211; Text User Interface for controlling NetworkManager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nmtui-edit | nmtui edit </code> {<i>name</i>&nbsp;|&nbsp;<i>id</i>}</p>
<dt> <code>nmtui-connect | nmtui connect </code> {<i>name</i>&nbsp;|&nbsp;<i>uuid</i>&nbsp;|&nbsp;<i>device</i>&nbsp;|&nbsp;<i>SSID</i>}</p>
<dt> <code>nmtui-hostname | nmtui hostname </code></dl>
<h2>DESCRIPTION</h2>
<p> <code>nmtui</code></p>
<dd>is a curses-based TUI application for interacting with NetworkManager. When starting <code>nmtui</code>, the user is prompted to choose the activity to perform unless it was specified as the first argument. </p>
<p> The supported activities are: </p>
<p> <code>edit</code></p>
<dl>
<dt>
<dd> Show a connection editor that supports adding, modifying, viewing and deleting connections. It provides similar functionality as <code>nm-connection-editor</code>.</dl>
<p> <code>connect</code></p>
<dl>
<dt>
<dd> Show a list of available connections, with the option to activate or deactivate them. It provides similar functionality as <code>nm-applet</code>.</dl>
<p> <code>hostname</code></p>
<dl>
<dt>
<dd> Set the system hostname.</dl>
<p> Corresponding to above activities, <code>nmtui</code> also comes with binaries named <code>nmtui-edit</code>, <code>nmtui-connect</code>, and <code>nmtui-hostname</code> to skip the selection of the activities.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1), <code><a href="/docs/linux/man/1-nm-applet/">nm-applet</a></code>(1), <code><a href="/docs/linux/man/1-nm-connection-editor/">nm-connection-editor</a></code>(1), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8). </p>
<h2>Index</h2>
