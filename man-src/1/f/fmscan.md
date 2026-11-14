---
title: "fmscan(1)"
name: "fmscan"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fmscan/"
description: "fmscan – scan FM band for radio stations"
---

<h2>NAME</h2>
<p> fmscan &#8211; scan FM band for radio stations</p>
<h2>SYNOPSIS</h2>
<p> <code>fm</code> [ <code>-h</code> ] [ <code>-d</code> <i>device</i> ] [ <code>-t</code> <i>tuner</i> ] [ <code>-s</code> <i>freq</i> ] [ <code>-e</code> <i>freq</i> ] [ <i>-i</i> <i>freq</i> ] [ <i>-q</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>fmscan</code> is a program to scan a frequency band for radio stations, using the video4linux interface introduced in 2.1.x series Linux kernels. It shows which ones have a accumulated signal strength of 50% or higher.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-h</code></p>
<dd> Print a usage message to standard output, and exit.</p>
<dt><code>-d </code><i>device</p>
<dd> Sets device</i> as the device to tune. The default is <code>/dev/radio0</code>.</p>
<dt><code>-t </code><i>tuner</p>
<dd> Sets tuner</i> as the tuner on the selected device to adjust. The default is tuner 0. Most radio devices have only a single tuner.</p>
<dt><code>-s </code><i>freq</p>
<dd> Starting frequency for scan, in MHz. Default: 87.9.</p>
<dt></i><code>-e </code><i>freq</p>
<dd> Ending frequency for scan, in MHz. Default: 107.9.</p>
<dt></i><code>-i </code><i>freq</p>
<dd> Increment between scanned channels, in MHz. Default: 0.2.</p>
<dt></i><code>-t </code><i>percent</p>
<dd> Signal strength threshold to consider a channel. Default: 50%.</p>
<dt></i><code>-q</code></p>
<dd> Quiet mode. Suppresses progress output.</dl>
<h2>BUGS</h2>
<p> This process can take a while, and results vary greatly depending on the radio card in use. If your card&#8217;s hardware cannot report signal strength, it will not produce useful results. </p>
<p> This program may not do much if your radio card&#8217;s driver doesn&#8217;t support fine tuning in 1/16000 MHz offsets. By default, V4L2 assumes 1/16 MHz tuning units, which introduces evil rounding errors on many frequencies. </p>
<p> Supports only tuner 0 on any given device.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>Additional documentation:</p>
<dd> <code>/usr/doc/fmtools/README</code></p>
<dt>The fmtools homepage:</p>
<dd> <code><a rel="nofollow" href="http://benpfaff.org/fmtools">http://benpfaff.org/fmtools</a></code></dl>
<h2>AUTHORS</h2>
<p> Russell Kroll &lt;rkroll [at] exploits.org&gt;, now maintained by Ben Pfaff &lt;blp [at] cs.stanford.edu.&gt;. This manpage written by Ben Pfaff. </p>
<h2>Index</h2>
