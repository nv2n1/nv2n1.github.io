---
title: "jscal-restore(1)"
name: "jscal-restore"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jscal-restore/"
description: "jscal-restore – restores joystick calibration"
---

<h2>NAME</h2>
<p> jscal-restore &#8211; restores joystick calibration</p>
<h2>SYNOPSIS</h2>
<p> <code>jscal-restore</code> &lt;<i>device-name</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>jscal-restore</code> restores the calibration and mapping information for the given joystick device, previously stored by the <code>jscal-store</code> command. </p>
<p> An appropriate rule can be set up with udev so that any stored calibration settings are restored when the relevant device is connected. Some distributions (at least Debian, Ubuntu and Slackware) provide joystick packages which install such rules automatically.</p>
<h2>FILES</h2>
<dl>
<dt>/var/lib/joystick/joystick.state</p>
<dd> File used to store the calibration settings.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jscal/">jscal</a></code>(1), <code><a href="/docs/linux/man/1-jscal-store/">jscal-store</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>jscal-restore</code> was written by Stephen Kitt. </p>
<h2>Index</h2>
