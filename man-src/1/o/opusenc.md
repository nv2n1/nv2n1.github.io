---
title: "opusenc(1)"
name: "opusenc"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opusenc/"
description: "opusenc – encode audio into the Opus format"
---

<h2>SYNOPSIS</h2>
<p> <code>opusenc</code> [ <code>-h</code> ] [ <code>-V</code> ] [ <code>&#8211;bitrate</code> <i>kbit/sec</i> ] [ <code>&#8211;vbr</code> ] [ <code>&#8211;cvbr</code> ] [ <code>&#8211;hard-cbr</code> ] [ <code>&#8211;comp</code> <i>complexity</i> ] [ <code>&#8211;framesize</code> <i>2.5, 5, 10, 20, 40, 60</i> ] [ <code>&#8211;expect-loss</code> <i>pct</i> ] [ <code>&#8211;downmix-mono</code> ] [ <code>&#8211;downmix-stereo</code> ] [ <code>&#8211;max-delay</code> <i>ms</i> ] [ <code>&#8211;save-range</code> <i>file</i> ] [ <code>&#8211;set-ctl-int</code> <i>ctl=value</i> ] [ <code>&#8211;comment</code> <i>tag=value</i> ] [ <code>&#8211;artist</code> <i>author</i> ] [ <code>&#8211;title</code> <i>track title</i> ] [ <code>&#8211;raw</code> ] [ <code>&#8211;raw-bits</code> <i>bits/sample</i> ] [ <code>&#8211;raw-rate</code> <i>Hz</i> ] [ <code>&#8211;raw-chan</code> <i>N</i> ] [ <code>&#8211;raw-endianness</code> <i>flag</i> ] [ <code>&#8211;ignorelength</code> ] <i>input.wav</i> <i>output.opus</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>opusenc</code> reads audio data in either raw, Wave, or AIFF format and encodes it into an Opus stream. If the input file is &quot;-&quot; audio data is read from stdin. Likewise, if the output file is &quot;-&quot; opus data is written to stdout. </p>
<p> Unless quieted <code>opusenc</code> displays fancy statistics about the encoding progress. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</dt>
<dd> Show command help</dd>
<dt>-V, &#8211;version</dt>
<dd> Show the version number</dd>
<dt>&#8211;bitrate N.nnn</dt>
<dd> Encoding bitrate in kbit/sec (6-256 per channel)<br />
 Default for &gt;=44.1kHz input is 64kbps per mono stream, 96kbps per coupled pair.</dd>
<dt>&#8211;vbr</dt>
<dd> Use variable bitrate encoding (default)</dd>
<dt>&#8211;cvbr</dt>
<dd> Use constrained variable bitrate encoding</dd>
<dt>&#8211;hard-cbr</dt>
<dd> Use hard constant bitrate encoding</dd>
<dt>&#8211;comp N</dt>
<dd> Encoding computational complexity (0-10, default: 10). Zero gives the fastest encodes but lower quality, while 10 gives the highest quality but slower encoding.</dd>
<dt>&#8211;framesize N</dt>
<dd> Maximum frame size in milliseconds (2.5, 5, 10, 20, 40, 60, default: 20)<br />
 Smaller framesizes achieve lower latency but less quality at a given bitrate.<br />
 Sizes greater than 20ms are only interesting at fairly low bitrates.</dd>
<dt>&#8211;expect-loss N</dt>
<dd> Percentage packet loss to expect (default: 0)</dd>
<dt>&#8211;downmix-mono</dt>
<dd> Downmix to mono</dd>
<dt>&#8211;downmix-stereo</dt>
<dd> Downmix to stereo (if &gt;2 channels input)</dd>
<dt>&#8211;max-delay N</dt>
<dd> Maximum container delay in milliseconds (0-1000, default: 1000)</dd>
<dt>&#8211;save-range file</dt>
<dd> Saves check values for every frame to a file</dd>
<dt>&#8211;set-ctl-int x=y</dt>
<dd> Pass the encoder control x with value y (advanced) Preface with s: to direct the ctl to multistream s<br />
 This may be used multiple times</dd>
<dt>&#8211;comment tag=value</dt>
<dd> Add an extra comment. This may be used multiple times, and all instances will be added to each of the input files specified. The argument should be in the form &quot;tag=value&quot;. See the vorbis-comment specification for well known tag names: <a rel="nofollow" href="http://www.xiph.org/vorbis/doc/v-comment.html">http://www.xiph.org/vorbis/doc/v-comment.html</a></dd>
<dt>&#8211;artist artist</dt>
<dd> Set the artist comment field in the comments to <i>artist</i></dd>
<dt>&#8211;title title</dt>
<dd> Set the track title comment field to <i>title</i></dd>
<dt>&#8211;raw</dt>
<dd> Raw (headerless) PCM input</dd>
<dt>&#8211;raw-bits N</dt>
<dd> Set bits/sample for raw input (default: 16)</dd>
<dt>&#8211;raw-rate N</dt>
<dd> Set sampling rate for raw input (default: 48000)</dd>
<dt>&#8211;raw-chan N</dt>
<dd> Set number of channels for raw input (default: 2)</dd>
<dt>&#8211;raw-endianness [0/1]</dt>
<dd> Set the endianness for raw input: 1 for bigendian, 0 for little (defaults to 0)</dd>
<dt>&#8211;ignorelength</dt>
<dd> Always ignore the datalength in Wave headers. Opusenc automatically ignores the length when its implausible (very small or very large) but some STDIN usage may still need this option to avoid truncation. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> Simplest usage. Take input as input.wav and produce output as output.opus:</p>
<dl>
<dt>
</dt><dd> opusenc input.wav output.opus</dd></dl>
<p> Produce a very high quality encode with a target rate of 160kbps:</p>
<dl>
<dt>
</dt><dd> opusenc &#8211;bitrate 160 input.wav output.opus</dd></dl>
<p> Record and send a live stream to an Icecast HTTP streaming server using oggfwd:</p>
<dl>
<dt>
</dt><dd> arecord -c 2 -r 48000 -twav &#8211; | opusenc &#8211;bitrate 96 &#8211; &#8211; | oggfwd icecast.somewhere.org 8000 password /stream.opus</dd></dl>
<h2>NOTES</h2>
<p> While it is possible to use opusenc for low latency streaming (e.g. with &#8211;max-delay set to 0 and netcat instead of Icecast) it&#8217;s not really designed for this, and the Ogg container and TCP transport aren&#8217;t the best tools for that application. Shell pipelines themselves will often have high buffering. The ability to set framesizes as low as 2.5 ms in opusenc mostly exists to try out the quality of the format with low latency settings, but not really for actual low latency usage.<br />
 Interactive usage should use UDP/RTP directly. </p>
<h2>AUTHORS</h2>
<p> Gregory Maxwell &lt;greg [at] xiph.org&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-opusdec/">opusdec</a></code>(1), <code><a href="/docs/linux/man/1-opusinfo/">opusinfo</a></code>(1), <code>oggfwd</code>(1) </p>
