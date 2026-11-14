---
title: "mode2(1)"
name: "mode2"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mode2/"
description: "mode2, xmode2 – shows the pulse/space length of infrared signals"
---

<h2>NAME</h2>
<p> mode2, xmode2 &#8211; shows the pulse/space length of infrared signals</p>
<h2>SYNOPSIS</h2>
<p> <code>mode2</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> The main purpose of these programs is to check operation of your home-brew LIRC receiver hardware and to see the IR waveform of the remote controller without an expensive oscilloscope. Very useful for debugging. Of course this program won&#8217;t work with hardware that decodes the signals itself like e.g. TV cards or the Irman. </p>
<p> mode2 will simply print pulse&amp;space lengths to stdout. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> display usage summary</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> display version</p>
<dt><code>-d</code> <code>&#8211;device</code>=<i>device</i></p>
<dd> read from given device</p>
<dt><code>-H</code> <code>&#8211;driver</code>=<i>driver</i></p>
<dd> use given driver</p>
<dt><code>-m</code> <code>&#8211;mode</code></p>
<dd> enable alternative display mode</p>
<dt><code>-r</code> <code>&#8211;raw</code></p>
<dd> access device directly</dl>
<h2>DRIVER LOADING</h2>
<p> Drivers are loaded dynamically. The search path used for this is determined by (falling priority):</p>
<dl>
<dt>&#8211;</p>
<dd> The &#8211;plugindir option if available.</p>
<dt>&#8211;</p>
<dd> The &#8216;plugindir&#8217; entry in the [lircd] section of the lirc_options.conf file.</p>
<dt>&#8211;</p>
<dd> The environment variable LIRC_PLUGINDIR.</p>
<dt>&#8211;</p>
<dd> A hardcoded default (usually /usr/lib[64]/lirc/plugins). </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.cache/mode2.log</code></p>
<dd> Debug output. Setting the XDG_CACHE_HOME environment variable relocates this file to $XDG_CACHE_HOME/mode2.log </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mode2/">mode2</a>(1), <a href="/docs/linux/man/1-xmode2/">xmode2</a>(1) </p>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
<h2>Index</h2>
