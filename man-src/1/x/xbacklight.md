---

title: "xbacklight(1)"
name: "xbacklight"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xbacklight/"
description: "xbacklight – adjust backlight brightness using RandR extension"
---

<h2>NAME</h2>
<p> xbacklight &#8211; adjust backlight brightness using RandR extension</p>
<p> <code>xbacklight</code> [-help] [-display <i>display</i>] [-get] [-set percent] [-inc percent] [-dec percent]</p>
<p> <i>Xbacklight</i> is used to adjust the backlight brightness where supported. It finds all outputs on the X server supporting backlight brightness control and changes them all in the same way.</p>
<dl>
<dt>-get</dt>
<dd> Print out the current backlight brightness of each output with such a control. The brightness is represented as a percentage of the maximum brightness supported.</dd>
<dt>-set <i>percent</i></dt>
<dd> Sets each backlight brightness to the specified level.</dd>
<dt>-inc <i>percent</i></dt>
<dd> Increases brightness by the specified amount.</dd>
<dt>-dec <i>percent</i></dt>
<dd> Decreases brightness by the specified amount.</dd>
<dt>-help</dt>
<dd> Print out a summary of the usage and exit.</dd>
<dt>-time <i>milliseconds</i></dt>
<dd> Length of time to spend fading the backlight between old and new value. Default is 200.</dd>
<dt>-steps <i>number</i></dt>
<dd> Number of steps to take while fading. Default is 20.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-xrandr/">Xrandr</a>(3)</p>
<h2>AUTHORS</h2>
<p> Keith Packard, Open Source Technology Center, Intel Corporation. </p>
