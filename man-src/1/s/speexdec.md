---

title: "speexdec(1)"
name: "speexdec"
section: "1"
letter: "s"
url: "/docs/linux/man/1-speexdec/"
description: "speexdec – The reference implementation speex decoder."
---

<p> speexdec &#8211; The reference implementation speex decoder.</p>
<h2>SYNOPSIS</h2>
<p> <code>speexdec</code> [<i>options</i>] <i>input_file.spx </i>[<i>output_file</i>]</p>
<h2>DESCRIPTION</h2>
<p> Decodes a Speex file and produce a WAV file or raw file</p>
<h3>input_file can be:</h3>
<dl>
<dt>filename.spx</dt>
<dd> regular Speex file</dd>
<dt>&#8211;</dt>
<dd> stdin</dd></dl>
<h3>output_file can be:</h3>
<dl>
<dt>filename.wav</dt>
<dd> Wav file</dd>
<dt>filename.*</dt>
<dd> Raw PCM file (any extension other that .wav)</dd>
<dt>&#8211;</dt>
<dd> stdout</dd>
<dt>(nothing)</dt>
<dd> Will be played to soundcard</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;enh</code></dt>
<dd> Enable perceptual enhancement (default)</dd>
<dt><code>&#8211;no-enh</code></dt>
<dd> Disable perceptual enhancement</dd>
<dt><code>&#8211;force-nb</code></dt>
<dd> Force decoding in narrowband</dd>
<dt><code>&#8211;force-wb</code></dt>
<dd> Force decoding in wideband</dd>
<dt><code>&#8211;force-uwb</code></dt>
<dd> Force decoding in ultra-wideband</dd>
<dt><code>&#8211;mono</code></dt>
<dd> Force decoding in mono</dd>
<dt><code>&#8211;stereo</code></dt>
<dd> Force decoding in stereo</dd>
<dt><code>&#8211;rate</code> n</dt>
<dd> Force decoding at sampling rate n Hz</dd>
<dt><code>&#8211;packet-loss</code> n</dt>
<dd> Simulate n % random packet loss</dd>
<dt><code>-V</code></dt>
<dd> Verbose mode (show bit-rate)</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> This help</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Version information</dd>
<dt><code>&#8211;pf</code></dt>
<dd> Deprecated, use <code>&#8211;enh</code> instead</dd>
<dt><code>&#8211;no-pf</code></dt>
<dd> Deprecated, use <code>&#8211;no-enh</code> instead</dd></dl>
<p> More information is available from the Speex site: <a rel="nofollow" href="http://www.speex.org">http://www.speex.org</a> </p>
<p> Please report bugs to the mailing list `speex-dev [at] xiph.org&#8217;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002 Jean-Marc Valin </p>
