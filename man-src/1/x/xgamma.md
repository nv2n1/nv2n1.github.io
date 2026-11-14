---
title: "xgamma(1)"
name: "xgamma"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xgamma/"
description: "xgamma – Alter a monitor’s gamma correction through the X server"
---

<h2 class="name">NAME</h2>
<p> xgamma &#8211; Alter a monitor&#8217;s gamma correction through the X server </p>
<h2>SYNOPSIS</h2>
<p> <code>xgamma</code> [-display <i>display</i>] [-screen <i>screen</i>] [-quiet] [-version] [-gamma f.f | [[-rgamma f.f] [-ggamma f.f] [-bgamma f.f]]]</p>
<h2>DESCRIPTION</h2>
<p> <code>xgamma</code> allows X users to query and alter the gamma correction of a monitor via the X video mode extension (XFree86-VidModeExtension). </p>
<p> Note that the <code>xgamma</code> utility is obsolete and deficient, <code>xrandr</code> should be used with drivers that support the <code>XRandr</code> extension. </p>
<p> If no value for the gamma correction is given via the <i>-gamma</i> or <i>-rgamma</i>/<i>-ggamma</i>/<i>-bgamma</i> options, <code>xgamma</code> prints the current gamma correction of the display.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This argument allows you to specify the server to connect to; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dl>
<dl>
<dt><code>-screen </code><i>screen</i></p>
<dd> When multiple displays are configured as a single logical display, this option allows you to select the screen you wish to change.</dl>
<dl>
<dt><code>-quiet</code></p>
<dd> Silence the normal output of <code>xgamma</code></dl>
<dl>
<dt><code>-help</code></p>
<dd> Print out the `Usage:&#8217; command syntax summary.</dl>
<dl>
<dt><code>-version</code></p>
<dd> Print out the program version and exit.</dl>
<dl>
<dt><code>-gamma f.f</code></p>
<dd> The gamma correction can either be defined as a single value, or separately for the red, green and blue components. This argument specifies the gamma correction as a single value.</dl>
<dl>
<dt><code>-rgamma f.f</code></p>
<dd> This argument specifies the red component of the gamma correction.</dl>
<dl>
<dt><code>-ggamma f.f</code></p>
<dd> This argument specifies the green component of the gamma correction.</dl>
<dl>
<dt><code>-bgamma f.f</code></p>
<dd> This argument specifies the blue component of the gamma correction.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> To get default host and display number.</dl>
<h2>BUGS</h2>
<p> This client changes the internal values of the gamma correction for the Xserver. Whether or not these values are respected depends on the video drivers. </p>
<p> The gamma values are passed to the Xserver with 3 decimal places of accuracy.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xvidtune/">xvidtune</a>(1), <a href="/docs/linux/man/1-xrandr/">xrandr</a>(1)</p>
<h2>AUTHORS</h2>
<p> Kaleb S. Keithley, X Consortium.<br />
 David Dawes, David Bateman </p>
<h2>Index</h2>
