---
title: "speexdec(1)"
name: "speexdec"
section: "1"
letter: "s"
url: "/docs/linux/man/1-speexdec/"
description: "speexdec – The reference implementation speex decoder."
---

<h2>NAME</h2>
<p> speexdec &#8211; The reference implementation speex decoder.</p>
<h2>SYNOPSIS</h2>
<p> <code>speexdec</code> [<i>options</i>] <i>input_file.spx </i>[<i>output_file</i>]</p>
<h2>DESCRIPTION</h2>
<p> Decodes a Speex file and produce a WAV file or raw file</p>
<h3>input_file can be:</h3>
<dl>
<dt>filename.spx</p>
<dd> regular Speex file</p>
<dt>&#8211;</p>
<dd> stdin</dl>
<h3>output_file can be:</h3>
<dl>
<dt>filename.wav</p>
<dd> Wav file</p>
<dt>filename.*</p>
<dd> Raw PCM file (any extension other that .wav)</p>
<dt>&#8211;</p>
<dd> stdout</p>
<dt>(nothing)</p>
<dd> Will be played to soundcard</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;enh</code></p>
<dd> Enable perceptual enhancement (default)</p>
<dt><code>&#8211;no-enh</code></p>
<dd> Disable perceptual enhancement</p>
<dt><code>&#8211;force-nb</code></p>
<dd> Force decoding in narrowband</p>
<dt><code>&#8211;force-wb</code></p>
<dd> Force decoding in wideband</p>
<dt><code>&#8211;force-uwb</code></p>
<dd> Force decoding in ultra-wideband</p>
<dt><code>&#8211;mono</code></p>
<dd> Force decoding in mono</p>
<dt><code>&#8211;stereo</code></p>
<dd> Force decoding in stereo</p>
<dt><code>&#8211;rate</code> n</p>
<dd> Force decoding at sampling rate n Hz</p>
<dt><code>&#8211;packet-loss</code> n</p>
<dd> Simulate n % random packet loss</p>
<dt><code>-V</code></p>
<dd> Verbose mode (show bit-rate)</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> This help</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Version information</p>
<dt><code>&#8211;pf</code></p>
<dd> Deprecated, use <code>&#8211;enh</code> instead</p>
<dt><code>&#8211;no-pf</code></p>
<dd> Deprecated, use <code>&#8211;no-enh</code> instead</dl>
<p> More information is available from the Speex site: <a rel="nofollow" href="http://www.speex.org">http://www.speex.org</a> </p>
<p> Please report bugs to the mailing list `speex-dev [at] xiph.org&#8217;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002 Jean-Marc Valin </p>
<h2>Index</h2>
