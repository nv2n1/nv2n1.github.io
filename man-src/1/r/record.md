---
title: "record(1)"
name: "record"
section: "1"
letter: "r"
url: "/docs/linux/man/1-record/"
description: "record – records *.wav files"
---

<h2>NAME</h2>
<p> record &#8211; records *.wav files</p>
<h2>SYNOPSIS</h2>
<p> <code>record [ options ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>record</code> records *.wav files in CD quality (i.e. 44100 Hz, 16bit, stereo). It has a input level meter, which might be useful for sound trouble shooting (check if the mixer settings ok for recording from the TV card etc.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> display help text</p>
<dt><code>-o file</code></p>
<dd> basename for the output file(s), a number and the .wav extension are added by record. Default is &quot;record&quot;.</p>
<dt><code>-i dev</code></p>
<dd> mixer control. This should be the one where you can adjust the record level for your audio source. Default is &quot;line&quot;. &quot;mic&quot; and &quot;igain&quot; are good candidates too. Best way to figure is to start your favorite mixer tool and check out which one works &#8230;</p>
<dt><code>-m dev</code></p>
<dd> set mixer device. Default is &quot;/dev/mixer&quot;.</p>
<dt><code>-d dev</code></p>
<dd> set audio device. Default is &quot;/dev/dsp&quot;.</p>
<dt><code>-r rate</code></p>
<dd> set sample rate. Default is 44100.</p>
<dt><code>-p sec</code></p>
<dd> peak seconds (number of seconds which should be scanned for the volume maximum). This affects both peak level display and level triggered recording (see below). Default is 1.5 seconds.</dl>
<p> record can also be used non-interactive:</p>
<dl>
<dt><code>-c</code></p>
<dd> enable console (non-interactive) mode.</p>
<dt><code>-v</code></p>
<dd> be verbose (console mode only).</p>
<dt><code>-t mm:ss</code></p>
<dd> Limit the record time (console mode only). By default record records until stopped by a signal (by typing ^C for example).</p>
<dt><code>-s size</code></p>
<dd> Limit the file size (console mode only). record will continue with a new file once the limit is reached.</p>
<dt><code>-n num</code></p>
<dd> Limit the file count (console mode only). record will stop recording after num files.</p>
<dt><code>-l</code></p>
<dd> Enable level triggered recording (console mode only) with the default trigger level (1000).</p>
<dt><code>-L level</code></p>
<dd> Enable level triggered recording with the specified trigger level.</dl>
<p> If level triggered recording is active, record will start and stop recording depending on the signal strength. Recording will be started if the signal strength is above the trigger level (1000/32768 =&gt; around 3%). Recording will be stopped if the signal is below the trigger level for some time (1.5 seconds by default, the -p switch changes this).</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
<h2>Index</h2>
