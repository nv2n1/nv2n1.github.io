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
<p> <code>record [ options ]</code></p>
<p> <code>record</code> records *.wav files in CD quality (i.e. 44100 Hz, 16bit, stereo). It has a input level meter, which might be useful for sound trouble shooting (check if the mixer settings ok for recording from the TV card etc.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> display help text</dd>
<dt><code>-o file</code></dt>
<dd> basename for the output file(s), a number and the .wav extension are added by record. Default is &quot;record&quot;.</dd>
<dt><code>-i dev</code></dt>
<dd> mixer control. This should be the one where you can adjust the record level for your audio source. Default is &quot;line&quot;. &quot;mic&quot; and &quot;igain&quot; are good candidates too. Best way to figure is to start your favorite mixer tool and check out which one works &#8230;</dd>
<dt><code>-m dev</code></dt>
<dd> set mixer device. Default is &quot;/dev/mixer&quot;.</dd>
<dt><code>-d dev</code></dt>
<dd> set audio device. Default is &quot;/dev/dsp&quot;.</dd>
<dt><code>-r rate</code></dt>
<dd> set sample rate. Default is 44100.</dd>
<dt><code>-p sec</code></dt>
<dd> peak seconds (number of seconds which should be scanned for the volume maximum). This affects both peak level display and level triggered recording (see below). Default is 1.5 seconds.</dd></dl>
<p> record can also be used non-interactive:</p>
<dl>
<dt><code>-c</code></dt>
<dd> enable console (non-interactive) mode.</dd>
<dt><code>-v</code></dt>
<dd> be verbose (console mode only).</dd>
<dt><code>-t mm:ss</code></dt>
<dd> Limit the record time (console mode only). By default record records until stopped by a signal (by typing ^C for example).</dd>
<dt><code>-s size</code></dt>
<dd> Limit the file size (console mode only). record will continue with a new file once the limit is reached.</dd>
<dt><code>-n num</code></dt>
<dd> Limit the file count (console mode only). record will stop recording after num files.</dd>
<dt><code>-l</code></dt>
<dd> Enable level triggered recording (console mode only) with the default trigger level (1000).</dd>
<dt><code>-L level</code></dt>
<dd> Enable level triggered recording with the specified trigger level.</dd></dl>
<p> If level triggered recording is active, record will start and stop recording depending on the signal strength. Recording will be started if the signal strength is above the trigger level (1000/32768 =&gt; around 3%). Recording will be stopped if the signal is below the trigger level for some time (1.5 seconds by default, the -p switch changes this).</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
