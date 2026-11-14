---
title: "jscal(1)"
name: "jscal"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jscal/"
description: "jscal – joystick calibration and remapping program"
---

<h2>NAME</h2>
<p> jscal &#8211; joystick calibration and remapping program</p>
<h2>SYNOPSIS</h2>
<p> <code>jscal</code> [<i>options</i>] &lt;<i>device-name</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>jscal</code> calibrates joysticks and maps joystick axes and buttons. Calibrating a joystick ensures the positions on the various axes are correctly interpreted. Mapping axes and buttons allows the meanings of the joystick&#8217;s axes and buttons to be redefined. </p>
<p> On Debian systems the calibration settings can be stored and later applied automatically using the <code>jscal-store</code> command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;calibrate</code></p>
<dd> Calibrate the joystick.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print out a summary of available options.</p>
<dt><code>-s</code>, <code>&#8211;set-correction</code> &lt;<i>nb_axes</i>,<i>type</i>,<i>precision</i>,<i>coefficients</i>,&#8230;&gt;</p>
<dd> Sets correction to specified values. For each axis, specify the correction type (0 for none, 1 for &quot;broken line&quot;), the precision, and if necessary the correction coefficients (&quot;broken line&quot; corrections take four coefficients).</p>
<dt><code>-u</code>, <code>&#8211;set-mappings</code> &lt;<i>nb_axes</i>,<i>axmap1</i>,<i>axmap2</i>,&#8230;,<i>nb_buttons</i>,<i>btnmap1</i>,<i>btnmap2</i>,&#8230;&gt;</p>
<dd> Sets axis and button mappings. <i>n_of_buttons</i> can be set to 0 to remap axes only.</p>
<dt><code>-t</code>, <code>&#8211;test-center</code></p>
<dd> Tests if the joystick is correctly calibrated. Returns 2 if the axes are not calibrated, 3 if buttons were pressed, 1 if there was any other error, and 0 on success.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Prints the version numbers of the running joystick driver and that which jscal was compiled for.</p>
<dt><code>-p</code>, <code>&#8211;print-correction</code></p>
<dd> Prints the current correction settings. The format of the output is a jscal command line.</p>
<dt><code>-q</code>, <code>&#8211;print-mappings</code></p>
<dd> Prints the current axis and button mappings. The format of the output is a jscal command line.</dl>
<h2>CALIBRATION</h2>
<p> Using the Linux input system, joysticks are expected to produce values between -32767 and 32767 for axes, with 0 meaning the joystick is centred. Thus, full-left should produce -32767 on the X axis, full-right 32767 on the X axis, full-forward -32767 on the Y axis, and so on. </p>
<p> Many joysticks and gamepads (especially older ones) are slightly mis-aligned; as a result they may not use the full range of values (for the extremes of the axes), or more annoyingly they may not give 0 when centred. Calibrating a joystick provides the kernel with information on a joystick&#8217;s real behaviour, which allows the kernel to correct various joysticks&#8217; deficiencies and produce consistent output as far as joystick-using software is concerned. </p>
<p> <code><a href="/docs/linux/man/1-jstest/">jstest</a></code>(1) is useful to determine whether a joystick is calibrated: when run, it should produce all 0s when the joystick is at rest, and each axis should be able to produce the values -32767 and 32767. Analog joysticks should produce values in between 0 and the extremes, but this is not necessary; digital directional pads work fine with only the three values.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffset/">ffset</a></code>(1), <code><a href="/docs/linux/man/1-jstest/">jstest</a></code>(1), <code><a href="/docs/linux/man/1-jscal-store/">jscal-store</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> <code>jscal</code> was written by Vojtech Pavlik and improved by many others; see the linuxconsole tools documentation for details. </p>
<p> This manual page was written by Stephen Kitt &lt;steve [at] sk2.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
