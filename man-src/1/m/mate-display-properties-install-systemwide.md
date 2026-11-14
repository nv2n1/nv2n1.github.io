---
title: "mate-display-properties-install-systemwide(1)"
name: "mate-display-properties-install-systemwide"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-display-properties-install-systemwide/"
description: "mate-display-properties-install-systemwide – customize MATE display behavor"
---

<h2 class="name">NAME</h2>
<p> mate-display-properties-install-systemwide &#8211; customize MATE display behavor </p>
<h2>SYNOPSIS</h2>
<p> <code>mate-display-properties-install-systemwide</code> <i>&lt;SOURCE_FILE&gt; &lt;DEST_NAME&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> This executable is part of the package &#8216;mate-control-center&#8217;: The MATE Control Center. </p>
<p> This command line tool installs a RANDR profile for multi-monitor setups into a systemwide location. The resulting profile will get used when the RANDR plug-in gets run in <code>mate-settings-daemon</code>.</p>
<dl>
<dt><i>&lt;SOURCE_FILE&gt;</i></p>
<dd> a full pathname, typically /home/username/.config/monitors.xml</p>
<dt><i>&lt;DEST_NAME&gt;</i></p>
<dd> relative name for the installed file. This will get put in the systemwide directory for RANDR configurations, so the result will typically be /etc/mate-settings-daemon/xrandr/DEST_NAME</dl>
<h2>AUTHORS</h2>
<p> This manual page was writtenby Mike Gabriel &lt;mike.gabriel [at] das-netzwerkteam.de&gt; for the Debian project (but may be used by others).</p>
<h2>SEE ALSO</h2>
<p> Latest version of the MATE Desktop User Guide for your platform. </p>
<p> <code><a href="/docs/linux/man/1-mate-control-center/">mate-control-center</a></code>(1), <code><a href="/docs/linux/man/1-mate-display-properties/">mate-display-properties</a></code>(1), <code><a href="/docs/linux/man/1-mate-settings-daemon/">mate-settings-daemon</a></code>(1), </p>
<h2>Index</h2>
