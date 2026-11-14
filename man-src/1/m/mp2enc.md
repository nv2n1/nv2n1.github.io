---
title: "mp2enc(1)"
name: "mp2enc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mp2enc/"
description: "mp2enc – Simple MPEG-1 layer-II audio encoder"
---

<h2 class="name">NAME</h2>
<p> mp2enc &#8211; Simple MPEG-1 layer-II audio encoder </p>
<h2>SYNOPSIS</h2>
<p> <code>mp2enc</code> [<code>-v</code> <i>num</i>] [<code>-b</code> <i>bitrate_kbps</i>] [<code>-r</code> <i>output_sampling_rate_hz</i>] [<code>-R</code> <i>rate,chans,bits</i>] [<code>-s</code> ] [<code>-m</code> ] [<code>-e</code> ] [<code>-V</code> ] [<code>-?</code>] <code>-o</code><i>&nbsp;<wbr>output_filename</i> </p>
<h2>DESCRIPTION</h2>
<p> Mp2enc is a simple MPEG-1 layer-I/II audio encoder. It is actually a very mildly warmed over version of the MPEG Software Simulation Group&#8217;s reference encoder. It accepts a WAV file or stream on stdin and ouputs an a layer-I/II elementary audio stream. It is included in the <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1) primarily for reasons of completeness and because it is able to perform sampling rate conversion. </p>
<p> Those seeking a faster (and probably higher quality) layer II encoder are recommended to use <code><a href="/docs/linux/man/1-toolame/">toolame</a></code>(1) which can be obtained from:</p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="http://www.planckenergy.com">http://www.planckenergy.com</a></i> </p>
</dl>
<h2>GENERAL FUNCTION LETTERS</h2>
<dl>
<dt><code>-o</code><i>&nbsp;<wbr>output_filename</i></p>
<dd> Specifies the name for the output file. </p>
<p> An integer format code (e.g. %d) in the name is replaced the number of the file generated (see <a href="/docs/linux/man/3-printf/">printf</a>(3)).</p>
<dt><code>-v</code><i>&nbsp;<wbr>num</i></p>
<dd> Set verbosity level to num. 0 = warnings and errors only, 1 = information as well, 2=really verbose. <code>-?</code> Display a synopsis of the command syntax. </p>
<dt><code>-R</code><i>&nbsp;<wbr>rate,chans,bits</i></p>
<dd> Indicate, that the input is raw PCM without header. You must specify 3 numbers: rate is the samplerate in Hz, chans is the number of channels (1 or 2) and bits is the number of bits per sample. 8 bits are unsigned, 16 bits are signed in machine native byte order. </p>
</dl>
<h2>FUNCTION LETTERS CONTROLLING OUTPUT STREAM STRUCTURE</h2>
<dl>
<dt><code>-b</code><i>&nbsp;<wbr>bitrate</i></p>
<dd>
<p> This sets the bit-rate of the output stream in kBit/sec. Typical values for layer II might be 224kbps for good-quality audio suitable for capturing Dolby pro-logic signals. A rate of 192kbps or 128kbps is reasonable for low quality audio (e.g. mono TV audio). Really high compression is, of course, better achieved using MPEG-1 layer III (&quot;MP3&quot;) audio encoding or AAC. A more appropriate value for layer I might be 384kbps. </p>
<dt><code>-r</code><i>&nbsp;<wbr>sampling_rate</i></p>
<dd> Sets the audio sampling rate of the reconstructed output signal in Hz. Legal values are 32000, 44100 and 48000Hz. mp2enc will automatically sample-rate convert the input signal if necessary. </p>
<dt><code>-l</code><i>&nbsp;<wbr>layer</i></p>
<dd> Sets the audio layer. Legal values are 1 and 2. The default is layer II. </p>
<dt><code>-s</code></p>
<dd> Force stereo output. A mono input signal is channel doubled before encoding to make it stereo. This is useful for players which simply can&#8217;t handle a non-stero signal.</p>
<dt><code>-m</code></p>
<dd> Force mono output. A stereo input signal is down-mixed before encoding. Useful if you&#8217;ve captured a mono signal in stereo and your player can handle mono MPEG-1 Layer 2 audio.</p>
<dt><code>-e</code></p>
<dd> Use CRC error protection.</p>
<dt><code>-V</code></p>
<dd> Force VCD compatible output. The primary effect of this is to make certain that the sampling rate is set to 44100 (-r 44100). The VCD2.0 specifications permit mono audio at 64, 96 and 192 kbits/sec and stereo at 128, 192, 224, and 384 kbits/sec. Using <code>-V</code> checks that the bitrate is valid for the number of channels. The defaults (unless -m or -b are used) are stereo at 224 kbits/sec.</p>
<dt><code>-o</code><i>&nbsp;<wbr>outputpathname</i></p>
<dd> The name of the output file to generate. If &#8216;-&#8216; is given as the pathname output is written to standard output.</dl>
<h2>BUGS</h2>
<p> Mono output does not work for layer I.</p>
<h2>AUTHOR</h2>
<p> This man page was written by Andrew Stevens.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-mp2enc/">mp2enc</a></code>(1), <code><a href="/docs/linux/man/1-lavrec/">lavrec</a></code>(1), <code><a href="/docs/linux/man/1-lavplay/">lavplay</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-lav2wav/">lav2wav</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1) </p>
<h2>Index</h2>
