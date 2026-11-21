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
<p> <code>speexenc</code> [<i>options</i>] <i>input_file output_file</i></p>
<p> Encodes input_file using Speex. It can read the WAV or raw files.</p>
<h3>input_file can be:</h3>
<dl>
<dt>filename.wav</dt>
<dd> wav file</dd>
<dt>filename.*</dt>
<dd> Raw PCM file (any extension other than .wav)</dd>
<dt>&#8211;</dt>
<dd> stdin</dd></dl>
<h3>output_file can be:</h3>
<dl>
<dt>filename.spx</dt>
<dd> Speex file</dd>
<dt>&#8211;</dt>
<dd> stdout</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;narrowband</code></dt>
<dd> Narrowband (8 kHz) input file</dd>
<dt><code>-w</code>, <code>&#8211;wideband</code></dt>
<dd> Wideband (16 kHz) input file</dd>
<dt> <code>-u</code>, <code>&#8211;ultra-wideband</code> &quot;Ultra-wideband&quot; (32 kHz) input file</dt>
<dt><code>&#8211;quality</code> n</dt>
<dd>
</dd><dd>Encoding quality (0-10), default 8</dd>
<dt><code>&#8211;bitrate</code> n</dt>
<dd> Encoding bit-rate (use bit-rate n or lower)</dd>
<dt><code>&#8211;vbr</code></dt>
<dd> Enable variable bit-rate (VBR)</dd>
<dt><code>&#8211;abr</code> rate</dt>
<dd> Enable average bit-rate (ABR) at rate bps</dd>
<dt><code>&#8211;vad</code></dt>
<dd> Enable voice activity detection (VAD)</dd>
<dt><code>&#8211;dtx</code></dt>
<dd> Enable file-based discontinuous transmission (DTX)</dd>
<dt><code>&#8211;comp</code> n</dt>
<dd> Set encoding complexity (0-10), default 3</dd>
<dt><code>&#8211;nframes</code> n</dt>
<dd> Number of frames per Ogg packet (1-10), default 1</dd>
<dt><code>&#8211;comment</code></dt>
<dd> Add the given string as an extra comment. This may be used multiple times</dd>
<dt><code>&#8211;author</code></dt>
<dd> Author of this track</dd>
<dt><code>&#8211;title</code></dt>
<dd> Title for this track</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> This help</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Version information</dd>
<dt><code>-V</code></dt>
<dd> Verbose mode (show bit-rate)</dd></dl>
<h3>Raw input options:</h3>
<dl>
<dt><code>&#8211;rate</code> n</dt>
<dd> Sampling rate for raw input</dd>
<dt><code>&#8211;stereo</code></dt>
<dd> Consider raw input as stereo</dd>
<dt><code>&#8211;le</code></dt>
<dd> Raw input is little-endian</dd>
<dt><code>&#8211;be</code></dt>
<dd> Raw input is big-endian</dd>
<dt><code>&#8211;8bit</code></dt>
<dd> Raw input is 8-bit unsigned</dd>
<dt><code>&#8211;16bit</code></dt>
<dd> Raw input is 16-bit signed</dd></dl>
<p> Default raw PCM input is 16-bit, little-endian, mono </p>
<p> More information is available from the Speex site: <a rel="nofollow" href="http://www.speex.org">http://www.speex.org</a> </p>
<p> Please report bugs to the mailing list `speex-dev [at] xiph.org&#8217;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002 Jean-Marc Valin </p>
