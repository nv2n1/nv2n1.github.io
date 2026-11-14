---
title: "spice-vdagentd(1)"
name: "spice-vdagentd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spice-vdagentd/"
description: "spice-vdagentd – Spice guest agent daemon"
---

<h2 class="name">NAME</h2>
<p> spice-vdagentd &#8211; Spice guest agent daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>spice-vdagent</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The spice guest agent for Linux consists of 2 parts, a system wide daemon <code>spice-vdagentd</code> and a X11 session agent <code>spice-vdagent</code> of which there is one per X11 session.<br />
 <code>spice-vdagentd</code> gets started through a Sys-V initscript or a systemd unit.</p>
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
<dd> Log debug messages (use twice for extra info)</p>
<dt><code>-f</code></p>
<dd> Treat uinput device as fake; no ioctls. This is useful in combination with Xspice.</p>
<dt><code>-o</code></p>
<dd> The daemon will exit after processing a single session.</p>
<dt><code>-s</code> <i>port</i></p>
<dd> Set virtio serial <i>port</i> (default: /dev/virtio-ports/com.redhat.spice.0)</p>
<dt><code>-u</code> <i>device</i></p>
<dd> Set uinput <i>device</i> (default: /dev/uinput)</p>
<dt><code>-x</code></p>
<dd> Don&#8217;t daemonize</p>
<dt><code>-X</code></p>
<dd> Disable session info usage, <code>spice-vdagentd</code> needs to know which <code>spice-vdagent</code> is in the currently active X11 session. <code>spice-vdagentd</code> uses console kit or systemd-logind (compile time option) for this; The <code>-X</code> option disables this, if no session info is available only one <code>spice-vdagent</code> is allowed</dl>
<h2>FILES</h2>
<p> The Sys-V initscript or systemd unit parses the following files:</p>
<dl>
<dt>/etc/default/spice-vdagentd</p>
<dd> Default cmdline options can be passed to <code>spice-vdagentd</code> by setting them in the <i>SPICE_VDAGENTD_EXTRA_ARGS</i> variable in this file</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-spice-vdagent/">spice-vdagent</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2010-2013 Red Hat, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
