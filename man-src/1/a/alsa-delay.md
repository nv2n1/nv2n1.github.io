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
<dt><i>&#8211;h,&#8211;help</i></dt>
<dd> Print help.</dd>
<dt><i>&#8211;q,&#8211;quiet</i></dt>
<dd> Quiet mode.</dd>
<dt><i>&#8211;y,&#8211;yes</i></dt>
<dd> Do not ask any questions &#8211; answer is always yes.</dd>
<dt><i>&#8211;c,&#8211;clean</i></dt>
<dd> Clean temporary directory.</dd>
<dt><i>&#8211;r,&#8211;remove</i></dt>
<dd> Remove the alsa-delay config modifications (modprobe, pulse-audio).</dd>
<dt><i>&#8211;tmpdir=&lt;DIR&gt;</i></dt>
<dd> Set temporary directory. </dd>
</dl>
<h2>OPTIONS (for alsaloop daemon)</h2>
<dl>
<dt><i>&#8211;pdevice=&lt;DEV&gt;</i></dt>
<dd> Force playback device.</dd>
<dt><i>&#8211;cdevice=&lt;DEV&gt;</i></dt>
<dd> Force capture device.</dd>
<dt><i>&#8211;pctl=&lt;DEV&gt;</i></dt>
<dd> Force playback control device.</dd>
<dt><i>&#8211;cctl=&lt;DEV&gt;</i></dt>
<dd> Force capture control device.</dd>
<dt><i>&#8211;one=&lt;ARG&gt;</i></dt>
<dd> Pass this argument to last thread.</dd>
<dt><i>&#8211;arg=&lt;ARG&gt;</i></dt>
<dd> Pass this argument to all threads.</dd>
<dt><i>&#8211;mix=&lt;ARG&gt;</i></dt>
<dd> Redirect ALSA mixer controls to OSS mixer (default is Master).</dd>
<dt><i>&#8211;pa</i></dt>
<dd> Redirect pulse-audio to alsaloop. </dd>
</dl>
<h2>NOTE</h2>
<p> For devices, the string %s is replaced with the card index and second string %s is replaced with the device index and third string %s is replaced the substream index (0-7). </p>
<p> Example: hw:%s,%s,%s (card, device, substream) </p>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-alsaloop/">alsaloop</a>(1) <a href="/docs/linux/man/1-amixer/">amixer</a>(1) <a href="/docs/linux/man/1-alsamixer/">alsamixer</a>(1) </p>
<p> </code></p>
