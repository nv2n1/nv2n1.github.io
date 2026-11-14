---
title: "audio2tape(1)"
name: "audio2tape"
section: "1"
letter: "a"
url: "/docs/linux/man/1-audio2tape/"
description: "audio2tape – Sinclair ZX Spectrum audio to tape file converter"
---

<h2 class="name">NAME</h2>
<p> audio2tape &#8211; Sinclair ZX Spectrum audio to tape file converter </p>
<h2>SYNOPSIS</h2>
<p> <code>audio2tape</code> [-t <i>type</i>] [-s] [-r] [-k] [-z <i>level</i>] [-c <i>level</i>] <i>infile outfile</i></p>
<h2>DESCRIPTION</h2>
<p> audio2tape converts audio files to ZX Spectrum tape images.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-t <i>type</i></p>
<dd> causes <i>type</i> to be used as the level detection trigger. There are two triggers implemented; the <i>simple</i> trigger just uses a threshold value to convert to a one or zero on output, and the <i>schmitt</i> trigger implements a Schmitt trigger which outputs a less noisy signal, but requires a stronger signal to noise ratio than the simple trigger. The default trigger is &quot;simple&quot;.</p>
<dt>-s</p>
<dd> causes the display of a frequency graph showing the sound levels present in the audio file. This can be useful when selecting good crossover points.</p>
<dt>-r</p>
<dd> causes any ROM blocks that are recognised to use idealised timing figures rather than the exact ones found in the audio file.</p>
<dt>-k</p>
<dd> causes the tape file that is produced to keep any audio data from the original audio file that isn&#8217;t recognised. This will allow unsupported loading schemes, encryption tones etc. to be preserved in the file that is produced.</p>
<dt>-z <i>level</i></p>
<dd> causes <i>level</i> to be used as the zero point in the supplied audio file, it allows adjustment for a DC offset in the audio file. The default level is 127 from a range of 0-255.</p>
<dt>-c <i>level</i></p>
<dd> causes <i>level</i> to be used as the Schmitt trigger noise threshold, this reduces the sensitivity to noise in the provided file. The default level is 8 from a range of 0-127.</p>
<dt><i>infile</i></p>
<dd> specifies the audio file to be converted. This file can be in any of the tape formats supported by <i>libaudiofile</i>.</p>
<dt><i>outfile</i></p>
<dd> specifies the output tape file. The format will be determined by the file extension and can be in any of the formats <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3) supports for output.</dl>
<h2>BUGS</h2>
<p> None known.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fuse/">fuse</a></i>(1), <i><a href="/docs/linux/man/1-fuse-utils/">fuse-utils</a></i>(1), <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3), <i><a href="/docs/linux/man/1-listbasic/">listbasic</a></i>(1), <i><a href="/docs/linux/man/1-tapeconv/">tapeconv</a></i>(1), <i><a href="/docs/linux/man/1-tzxlist/">tzxlist</a></i>(1), <i><a href="/docs/linux/man/1-snap2tzx/">snap2tzx</a></i>(1), <i><a href="/docs/linux/man/1-tape2wav/">tape2wav</a></i>(1) </p>
<p> The comp.sys.sinclair Spectrum FAQ, at<br />
 <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/index.html">http://www.worldofspectrum.org/faq/index.html</a></i>.</p>
<h2>AUTHOR</h2>
<p> Fredrick Meunier (fredm [at] spamcop.net). </p>
<h2>Index</h2>
