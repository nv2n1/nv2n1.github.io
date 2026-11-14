---
title: "fm(1)"
name: "fm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fm/"
description: "fm – control frequency, volume, mute/unmute of FM radio card"
---

<h2>NAME</h2>
<p> fm &#8211; control frequency, volume, mute/unmute of FM radio card</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fm</code> [ <code>-h</code> ] [ <code>-o</code> ] [ <code>-q</code> ] [ <code>-d</code> <i>device</i> ] [ <code>-t</code> <i>tuner</i> ] [ <code>-T</code> <code>none</code> | <code>forever</code> | <i>time</i> ] <code>on</code> | <code>off</code> | <code>+</code> | <code>&#8211;</code> | <code>freq</code> [ <i>volume</i> ]</dl>
<h2>DESCRIPTION</h2>
<p> <code>fm</code></p>
<dd>is a program to control the frequency, volume, and mute/unmute state of an FM radio card, using the video4linux interface introduced in 2.1.x series Linux kernels.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-h</code></p>
<dd> Print a usage message to standard output, and exit.</p>
<dt><code>-o</code></p>
<dd> Ignore frequency range limits of card. Use if you suspect that the card supports a wider frequency range than its driver believes.</p>
<dt><code>-q</code></p>
<dd> Quiet mode. Keeps information on station and volume from being printed on standard output.</p>
<dt><code>-d </code><i>device</p>
<dd> Sets device</i> as the device to tune. The default is <code>/dev/radio0</code>.</p>
<dt><code>-t </code><i>tuner</p>
<dd> Sets tuner</i> as the tuner on the selected device to adjust. The default is tuner 0. Most radio devices have only a single tuner.</p>
<dt><code>-T none </code>| <code>forever </code>| <i>time</p>
<dd> After tuning, sleep for the time specified or forever. Time is specified in seconds by default. A suffix of </i><code>m</code> indicates minutes, <code>h</code> indicates hours, or <code>d</code> indicates days.</p>
<dt>
<dd> The <code>-T</code> option is useful with radio card drivers that only maintain the tuner settings while the tuner&#8217;s file descriptor remains open. Try using this option if running <code>fm</code> ordinarily produces only a single &quot;pop&quot; from your speakers.</p>
<dt><code>freq</code></p>
<dd> Frequency to tune the radio to, in MHz. For instance, <code>88.9</code> specifies a frequency of 88.9 MHz. AM tuner values are also specified in MHz; for instance, 530 kHz would be specified as <code>.530</code>.</p>
<dt><code>on</code></p>
<dd> Turn the radio on (unmute).</p>
<dt><code>off</code></p>
<dd> Turn the radio off (mute).</p>
<dt><code>volume</code></p>
<dd> Specify the desired volume, in percent. Not all radio devices support volume control.</p>
<dt><code>+</code></p>
<dd> Increase the current volume.</p>
<dt><code>&#8211;</code></p>
<dd> Decrease the current volume.</dl>
<h2>CONFIGURATION</h2>
<p> <code>fm</code> reads <i>$HOME</i><code>/.fmrc</code>, if it exists, to obtain default settings. Each line may take one of the following forms:</p>
<dl>
<dt><code>VOL</code>&nbsp;<wbr>percent</p>
<dd> Specifies default volume (default: 12.5%).</p>
<dt><code>INCR</code>&nbsp;<wbr>percent</p>
<dd> Volume increment used for <code>+</code> and <code>&#8211;</code> options (default: 10%).</p>
<dt><code>TIME</code></p>
<dd> Default sleep time (default: <code>none</code>).</dl>
<p> All other lines are ignored.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>Additional documentation:</p>
<dd> <code>/usr/share/doc/fmtools/README</code></p>
<dt>The fmtools homepage:</p>
<dd> <code><a rel="nofollow" href="http://benpfaff.org/fmtools">http://benpfaff.org/fmtools</a></code></dl>
<h2>AUTHORS</h2>
<p> Russell Kroll &lt;rkroll [at] exploits.org&gt;, now maintained by Ben Pfaff &lt;blp [at] cs.stanford.edu&gt;. Sleep time feature contributed by Dave Ulrick &lt;d-ulrick [at] insightbb.com&gt;. This manpage written by Ben Pfaff. </p>
<h2>Index</h2>
