---
title: "opusdec(1)"
name: "opusdec"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opusdec/"
description: "opusdec – decode audio from Opus format to WAV (or simple audio output)"
---

<h2 class="name">NAME</h2>
<p> opusdec &#8211; decode audio from Opus format to WAV (or simple audio output)</p>
<h2>SYNOPSIS</h2>
<p> <code>opusdec</code> [ <code>-hV</code> ] [ <code>&#8211;rate Hz</code> ] [ <code>&#8211;gain dB</code> ] [ <code>&#8211;no-dither</code> ] [ <code>&#8211;force-wav</code> ] [ <code>&#8211;packet-loss pct</code> ] [ <code>&#8211;save-range file</code> ] <code>input.opus</code> [ <code>output.wav</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>opusdec</code> decodes Opus files into PCM Wave (uncompressed) files. </p>
<p> If the input file is specified as <code>&#8211;</code> , then <code>opusdec</code> will read from stdin. Likewise, an output filename of <code>&#8211;</code> will cause output to be to stdout. </p>
<p> If no output is specified <code>opusdec</code> will attempt to play the audio in realtime if it supports audio playback on your system. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd> Print help message</p>
<dt>-V, &#8211;version</p>
<dd> Display version information</p>
<dt>&#8211;quiet</p>
<dd> Suppresses program output</p>
<dt>&#8211;rate</p>
<dd>
 Force decoding at sampling rate n Hz</p>
<dt>&#8211;gain</p>
<dd>
 Adjust the output volume n dB, negative values make the signal quieter.</p>
<dt>&#8211;no-dither</p>
<dd> Do not dither 16-bit output</p>
<dt>&#8211;force-wav</p>
<dd> Force including a wav header on output (e.g. for non-wav extensions and stdout)</p>
<dt>&#8211;packet-loss</p>
<dd> Simulate n % random Opus packet loss</p>
<dt>&#8211;save-range</p>
<dd> Saves check values for every frame to a file </p>
</dl>
<h2>EXAMPLES</h2>
<p> Decode a file <code>input.opus</code> to <code>output.wav</code></p>
<dl>
<dt>
<dd> opusdec input.opus output.wav</dl>
<p> Play a file <code>input.opus</code> and force output at 48000 regardless of the original sampling rate<br />
 <i>(48kHz output may be faster, due to avoiding resampling and some sound hardware produces higher quality output when run at 48kHz)</i></p>
<dl>
<dt>
<dd> opusdec &#8211;rate 48000 input.opus</dl>
<p> Re-encode a high bitrate Opus file to a lower rate</p>
<dl>
<dt>
<dd> opusdec &#8211;force-wav input.opus &#8211; | opusenc &#8211;bitrate 64 &#8211; output.opus</dl>
<p> Play an http stream <code><a rel="nofollow" href="http://icecast.somwhere.org:8000/stream.opus">http://icecast.somwhere.org:8000/stream.opus</a></code> with the help of curl on a system with pulseaudio<br />
 <i>(press ctrl-c to quit)</i></p>
<dl>
<dt>
<dd> curl <a rel="nofollow" href="http://icecast.somwhere.org:8000/stream.opus">http://icecast.somwhere.org:8000/stream.opus</a> | padsp opusdec &#8211;</dl>
<h2>AUTHORS</h2>
<p> Jean-Marc Valin &lt;jmvalin [at] jmvalin.ca&gt;<br />
 Gregory Maxwell &lt;greg [at] xiph.org&gt; </p>
<h2>BUGS</h2>
<p> Opusdec does not currently reject all invalid files which it should reject. It also doesn&#8217;t provide very helpful output for the corrupted files it does reject. Use <code><a href="/docs/linux/man/1-opusinfo/">opusinfo</a></code>(1) for somewhat better diagnostics. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-opusenc/">opusenc</a></code>(1), <code><a href="/docs/linux/man/1-opusinfo/">opusinfo</a></code>(1) </p>
<h2>Index</h2>
