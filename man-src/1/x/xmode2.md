---
title: "xmode2(1)"
name: "xmode2"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmode2/"
description: "mode2, smode2, xmode2 – shows the pulse/space length of infrared signals"
---

<h2>NAME</h2>
<p> mode2, smode2, xmode2 &#8211; shows the pulse/space length of infrared signals</p>
<h2>SYNOPSIS</h2>
<p> <code>xmode2</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> The main purpose of these programs is to check operation of your home-brew LIRC receiver hardware and to see the IR waveform of the remote controller without an expensive oscilloscope. Very useful for debugging. Of course this program won&#8217;t work with hardware that decodes the signals itself like e.g. TV cards or the Irman. </p>
<p> xmode2 is based on smode2 by Sinkovics Zoltan. It is just a conversion from svga to X with some basic support for resizing. The only differences are that the &#8211;mode option enables an alternative display mode and that xmode2 can read and visualise mode2 output from stdin.</p>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> display usage summary</dd>
<dt><code>-v</code> <code>&#8211;version</code></dt>
<dd> display version</dd>
<dt><code>-d</code> <code>&#8211;device</code>=<i>device</i></dt>
<dd> read from given device</dd>
<dt> <code>-g</code> <code>&#8211;geometry</code>=<i>geometry</i> window geometry</dt>
<dt><code>-t</code> <code>&#8211;timediv</code>=<i>value</i></dt>
<dd>
</dd><dd>ms per unit</dd>
<dt><code>-m</code> <code>&#8211;mode</code></dt>
<dd> enable alternative display mode</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mode2/">mode2</a>(1), smode2(1), <a href="/docs/linux/man/1-xmode2/">xmode2</a>(1) </p>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
<h2>Index</h2>
