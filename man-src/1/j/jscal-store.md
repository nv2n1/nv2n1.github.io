---
title: "jscal-store(1)"
name: "jscal-store"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jscal-store/"
description: "jscal-store – stores joystick calibration"
---

<h2>NAME</h2>
<p> jscal-store &#8211; stores joystick calibration</p>
<h2>SYNOPSIS</h2>
<p> <code>jscal-store</code> &lt;<i>device-name</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>jscal-store</code> stores the calibration and mapping information for the given joystick device. This information can later be restored using the <code>jscal-restore</code> command. </p>
<p> An appropriate rule can be set up with udev so that any stored calibration settings are restored when the relevant device is connected. Some distributions (at least Debian, Ubuntu and Slackware) provide joystick packages which install such rules automatically.</p>
<h2>FILES</h2>
<dl>
<dt>/var/lib/joystick/joystick.state</p>
<dd> File used to store the calibration settings.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jscal/">jscal</a></code>(1), <code><a href="/docs/linux/man/1-jscal-restore/">jscal-restore</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>jscal-store</code> was written by Stephen Kitt. </p>
<h2>Index</h2>
