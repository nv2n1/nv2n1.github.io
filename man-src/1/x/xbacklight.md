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
<h2>SYNOPSIS</h2>
<p> <code>xbacklight</code> [-help] [-display <i>display</i>] [-get] [-set percent] [-inc percent] [-dec percent]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xbacklight</i> is used to adjust the backlight brightness where supported. It finds all outputs on the X server supporting backlight brightness control and changes them all in the same way.</p>
<dl>
<dt>-get</p>
<dd> Print out the current backlight brightness of each output with such a control. The brightness is represented as a percentage of the maximum brightness supported.</p>
<dt>-set <i>percent</i></p>
<dd> Sets each backlight brightness to the specified level.</p>
<dt>-inc <i>percent</i></p>
<dd> Increases brightness by the specified amount.</p>
<dt>-dec <i>percent</i></p>
<dd> Decreases brightness by the specified amount.</p>
<dt>-help</p>
<dd> Print out a summary of the usage and exit.</p>
<dt>-time <i>milliseconds</i></p>
<dd> Length of time to spend fading the backlight between old and new value. Default is 200.</p>
<dt>-steps <i>number</i></p>
<dd> Number of steps to take while fading. Default is 20.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-xrandr/">Xrandr</a>(3)</p>
<h2>AUTHORS</h2>
<p> Keith Packard, Open Source Technology Center, Intel Corporation. </p>
<h2>Index</h2>
