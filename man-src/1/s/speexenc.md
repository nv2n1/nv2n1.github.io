---
title: "speexenc(1)"
name: "speexenc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-speexenc/"
description: "speexenc – The reference implementation speex encoder."
---

<h2>NAME</h2>
<p> speexenc &#8211; The reference implementation speex encoder.</p>
<h2>SYNOPSIS</h2>
<p> <code>speexenc</code> [<i>options</i>] <i>input_file output_file</i></p>
<h2>DESCRIPTION</h2>
<p> Encodes input_file using Speex. It can read the WAV or raw files.</p>
<h3>input_file can be:</h3>
<dl>
<dt>filename.wav</p>
<dd> wav file</p>
<dt>filename.*</p>
<dd> Raw PCM file (any extension other than .wav)</p>
<dt>&#8211;</p>
<dd> stdin</dl>
<h3>output_file can be:</h3>
<dl>
<dt>filename.spx</p>
<dd> Speex file</p>
<dt>&#8211;</p>
<dd> stdout</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;narrowband</code></p>
<dd> Narrowband (8 kHz) input file</p>
<dt><code>-w</code>, <code>&#8211;wideband</code></p>
<dd> Wideband (16 kHz) input file</p>
<dt> <code>-u</code>, <code>&#8211;ultra-wideband</code> &quot;Ultra-wideband&quot; (32 kHz) input file</p>
<dt><code>&#8211;quality</code> n</p>
<dd>
<dd>Encoding quality (0-10), default 8</p>
<dt><code>&#8211;bitrate</code> n</p>
<dd> Encoding bit-rate (use bit-rate n or lower)</p>
<dt><code>&#8211;vbr</code></p>
<dd> Enable variable bit-rate (VBR)</p>
<dt><code>&#8211;abr</code> rate</p>
<dd> Enable average bit-rate (ABR) at rate bps</p>
<dt><code>&#8211;vad</code></p>
<dd> Enable voice activity detection (VAD)</p>
<dt><code>&#8211;dtx</code></p>
<dd> Enable file-based discontinuous transmission (DTX)</p>
<dt><code>&#8211;comp</code> n</p>
<dd> Set encoding complexity (0-10), default 3</p>
<dt><code>&#8211;nframes</code> n</p>
<dd> Number of frames per Ogg packet (1-10), default 1</p>
<dt><code>&#8211;comment</code></p>
<dd> Add the given string as an extra comment. This may be used multiple times</p>
<dt><code>&#8211;author</code></p>
<dd> Author of this track</p>
<dt><code>&#8211;title</code></p>
<dd> Title for this track</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> This help</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Version information</p>
<dt><code>-V</code></p>
<dd> Verbose mode (show bit-rate)</dl>
<h3>Raw input options:</h3>
<dl>
<dt><code>&#8211;rate</code> n</p>
<dd> Sampling rate for raw input</p>
<dt><code>&#8211;stereo</code></p>
<dd> Consider raw input as stereo</p>
<dt><code>&#8211;le</code></p>
<dd> Raw input is little-endian</p>
<dt><code>&#8211;be</code></p>
<dd> Raw input is big-endian</p>
<dt><code>&#8211;8bit</code></p>
<dd> Raw input is 8-bit unsigned</p>
<dt><code>&#8211;16bit</code></p>
<dd> Raw input is 16-bit signed</dl>
<p> Default raw PCM input is 16-bit, little-endian, mono </p>
<p> More information is available from the Speex site: <a rel="nofollow" href="http://www.speex.org">http://www.speex.org</a> </p>
<p> Please report bugs to the mailing list `speex-dev [at] xiph.org&#8217;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002 Jean-Marc Valin </p>
<h2>Index</h2>
