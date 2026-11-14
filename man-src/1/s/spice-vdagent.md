---
title: "spice-vdagent(1)"
name: "spice-vdagent"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spice-vdagent/"
description: "spice-vdagent – Spice guest agent X11 session agent"
---

<h2 class="name">NAME</h2>
<p> spice-vdagent &#8211; Spice guest agent X11 session agent </p>
<h2>SYNOPSIS</h2>
<p> <code>spice-vdagent</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The spice guest agent for Linux consists of 2 parts, a system wide daemon <code>spice-vdagentd</code> and a X11 session agent <code>spice-vdagent</code> of which there is one per X11 session.<br />
 <code>spice-vdagent</code> gets automatically started in desktop environments which honor /etc/xdg/autostart, and under gdm.</p>
<h2>FEATURES</h2>
<p> The spice guest agent adds the following features to spice Linux guests: </p>
<p> Client mouse mode (no need to grab mouse by client, no mouse lag) </p>
<p> Automatic adjustment of the X11 session&#8217;s number of virtual monitors, and their resolution, to the number of client windows and their resolution </p>
<p> Support of copy and paste (text and images) between the active X11 session and the client, this supports both the primary selection and the clipboard </p>
<p> Support for transferring files from the client to the agent</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Print a short description of all command line options</p>
<dt><code>-d</code></p>
<dd> Log debug messages</p>
<dt><code>-s</code> <i>port</i></p>
<dd> Set virtio serial <i>port</i> (default: /dev/virtio-ports/com.redhat.spice.0)</p>
<dt><code>-x</code></p>
<dd> Don&#8217;t daemonize</p>
<dt><code>-f</code> <i>dir|xdg-desktop|xdg-download</i></p>
<dd> Set directory where to save files send from the client, this can be either an arbitrary <i>dir</i> or one of the special values of <i>xdg-desktop</i> or <i>xdg-download</i> to select the default xdg Desktop resp. xdg Download directory. If no value is specified the default is <i>xdg-desktop</i> when running under a Desktop Environment which has icons on the desktop and <i>xdg-download</i> under other Desktop Environments</p>
<dt><code>-o</code> <i>0|1</i></p>
<dd> Disable/enable opening the file save directory with xdg-open (showing the directory in the file manager) when a file transfer from the client completes. If no value is specified the default is <i>0</i> when running under a Desktop Environment which has icons on the desktop and <i>1</i> under other Desktop Environments</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-spice-vdagentd/">spice-vdagentd</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2010-2013 Red Hat, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
