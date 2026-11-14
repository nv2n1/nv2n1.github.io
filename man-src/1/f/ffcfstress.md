---
title: "ffcfstress(1)"
name: "ffcfstress"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffcfstress/"
description: "ffcfstress – constant force stress test for force-feedback devices"
---

<h2>NAME</h2>
<p> ffcfstress &#8211; constant force stress test for force-feedback devices</p>
<h2>SYNOPSIS</h2>
<p> <code>ffcfstress</code> [<code>-d</code> &lt;<i>device</i>&gt;] [<code>-u</code> &lt;<i>update rate</i>&gt;] [<code>-f</code> &lt;<i>frequency</i>&gt;] [<code>-a</code> &lt;<i>amplitude</i>&gt;] [<code>-s</code> &lt;<i>strength</i>&gt;] [<code>-x</code> &lt;<i>axis</i>&gt;] [<code>-A</code>] [<code>-o</code>]</p>
<h2>DESCRIPTION</h2>
<p> ffcfstress stress tests constant non-enveloped forces on a force feedback device. It simulates a moving spring force by applying a frequently updated constant force effect. </p>
<p> <code>Beware, the stress test may damage your device!</code></p>
<h2>OPTIONS</h2>
<p> At least one option is required.</p>
<dl>
<dt><code>-d</code> &lt;<i>device</i>&gt;</p>
<dd> The device to test (by default <i>/dev/input/event0</i>).</p>
<dt><code>-u</code> &lt;<i>update rate</i>&gt;</p>
<dd> The update rate in Hz (25 by default).</p>
<dt><code>-f</code> &lt;<i>frequency</i>&gt;</p>
<dd> The spring center motion frequency in Hz (0.1 by default).</p>
<dt><code>-a</code> &lt;<i>amplitude</i>&gt;</p>
<dd> The spring center motion amplitude, between 0.0 and 1.0 (1.0 by default).</p>
<dt><code>-s</code> &lt;<i>strength</i>&gt;</p>
<dd> The spring strength factor (1.0 by default).</p>
<dt><code>-x</code> &lt;<i>axis</i>&gt;</p>
<dd> absolute axis to test (default: 0)<br />
 [0 = X, 1 = Y, 2 = Z, 3 = RX, 4 = RY, 5 = RZ, 6 = WHEEL]</p>
<dt><code>-A</code></p>
<dd> switch off auto-centering</p>
<dt><code>-o</code></p>
<dd> Dummy option, useful when all defaults should be used.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmvforce/">ffmvforce</a></code>(1), <code><a href="/docs/linux/man/1-fftest/">fftest</a></code>(1), <code><a href="/docs/linux/man/1-jstest/">jstest</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>ffcfstress</code> was written by Oliver Hamann. </p>
<p> This manual page was written by Stephen Kitt &lt;steve [at] sk2.org&gt;, for the Debian GNU/Linux system (but may be used by others). It was last modified for <code>ffcfstress</code> dated February 15, 2002. </p>
<h2>Index</h2>
