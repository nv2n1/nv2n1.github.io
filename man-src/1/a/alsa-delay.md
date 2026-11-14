---
title: "alsa-delay(1)"
name: "alsa-delay"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alsa-delay/"
description: "alsadelay – a command to (re)initialize sound hardware"
---

<h2>NAME</h2>
<p> alsadelay &#8211; a command to (re)initialize sound hardware </p>
<h2>SYNOPSIS</h2>
<p> <code>alsa-delay</code> <i>[options]</i> <i>requested_delay_in_ms</i> [<i>output_card</i>[,<i>device</i>]] </p>
<h2>DESCRIPTION</h2>
<p> <code>alsa-delay</code> is a command-line utility to setup an audio delay. The snd-aloop ALSA driver is used to send all PCM streams back to the user space and the alsaloop utility is used to send this stream to a real hardware. </p>
<p> The parameter <i>output_card</i> is ALSA card index (number) or string card identifier. The parameter <i>device</i> is ALSA device number. </p>
<p> Use <i>aplay -l</i> to list available cards and devices. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;h,&#8211;help</i></p>
<dd> Print help.</p>
<dt><i>&#8211;q,&#8211;quiet</i></p>
<dd> Quiet mode.</p>
<dt><i>&#8211;y,&#8211;yes</i></p>
<dd> Do not ask any questions &#8211; answer is always yes.</p>
<dt><i>&#8211;c,&#8211;clean</i></p>
<dd> Clean temporary directory.</p>
<dt><i>&#8211;r,&#8211;remove</i></p>
<dd> Remove the alsa-delay config modifications (modprobe, pulse-audio).</p>
<dt><i>&#8211;tmpdir=&lt;DIR&gt;</i></p>
<dd> Set temporary directory. </p>
</dl>
<h2>OPTIONS (for alsaloop daemon)</h2>
<dl>
<dt><i>&#8211;pdevice=&lt;DEV&gt;</i></p>
<dd> Force playback device.</p>
<dt><i>&#8211;cdevice=&lt;DEV&gt;</i></p>
<dd> Force capture device.</p>
<dt><i>&#8211;pctl=&lt;DEV&gt;</i></p>
<dd> Force playback control device.</p>
<dt><i>&#8211;cctl=&lt;DEV&gt;</i></p>
<dd> Force capture control device.</p>
<dt><i>&#8211;one=&lt;ARG&gt;</i></p>
<dd> Pass this argument to last thread.</p>
<dt><i>&#8211;arg=&lt;ARG&gt;</i></p>
<dd> Pass this argument to all threads.</p>
<dt><i>&#8211;mix=&lt;ARG&gt;</i></p>
<dd> Redirect ALSA mixer controls to OSS mixer (default is Master).</p>
<dt><i>&#8211;pa</i></p>
<dd> Redirect pulse-audio to alsaloop. </p>
</dl>
<h2>NOTE</h2>
<p> For devices, the string %s is replaced with the card index and second string %s is replaced with the device index and third string %s is replaced the substream index (0-7). </p>
<p> Example: hw:%s,%s,%s (card, device, substream) </p>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-alsaloop/">alsaloop</a>(1) <a href="/docs/linux/man/1-amixer/">amixer</a>(1) <a href="/docs/linux/man/1-alsamixer/">alsamixer</a>(1) </p>
<p> </code></p>
<h2>Index</h2>
