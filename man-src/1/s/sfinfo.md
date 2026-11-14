---
title: "sfinfo(1)"
name: "sfinfo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfinfo/"
description: "sfinfo – display information about audio files"
---

<h2 class="name">NAME</h2>
<p> sfinfo &#8211; display information about audio files </p>
<h2>SYNOPSIS</h2>
<p> <code>sfinfo</code> [<i>options</i>] <i>audio files</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> sfinfo prints information about the specified audio files, including file format, sample rate, duration, and audio data format. </p>
<p> By default sfinfo displays information in a longer, multi-line format; specifying the &#8211;short or -s option produces a short, single-line summary. </p>
<p> Any files which are not recognized as valid audio files will be ignored unless the &#8211;reporterror or -r option is given. The file formats currently supported by sfinfo are AIFF, AIFF-C, NeXT/Sun .snd/.au, WAVE, Berkeley/IRCAM/CARL Sound File, AVR, Amiga IFF/8SVX, Sample Vision, Creative Voice File, NIST SPHERE, and Core Audio Format.</p>
<h2>OPTIONS</h2>
<p> &#8211;short, -s</p>
<dl>
<dt>
<dd> Print short single-line summary of each recognized audio file.</dl>
<p> &#8211;reporterror, -r</p>
<dl>
<dt>
<dd> Print an error message if any of the specified files are not recognized as valid audio files.</dl>
<p> &#8211;help, -h</p>
<dl>
<dt>
<dd> Print help message.</dl>
<p> &#8211;version, -v</p>
<dl>
<dt>
<dd> Print version information.</dl>
<h2>EXAMPLES</h2>
<p> Display summary of an audio file: </p>
<dl>
<dt>
<dd>
<pre>
% sfinfo drum.aiff
File Name      drum.aiff
File Format    Audio Interchange File Format (aiff)
Data Format    16-bit integer (2's complement, big endian)
Audio Data     1569972 bytes begins at offset 54 (36 hex)
               2 channels, 392493 frames
Sampling Rate  44100.00 Hz
Duration       8.900 seconds
</pre>
</dl>
<p> List all recognized audio files in the current directory using the short output format: </p>
<dl>
<dt>
<dd>
<pre>
% sfinfo -s *
    9.60s 44100.00 aiff  1ch 16b -- bass.aiff
    8.90s 44100.00 aiff  2ch 16b -- drum.aiff
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sfconvert/">sfconvert</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Michael Pruett &lt;michael [at] 68k.org&gt; </p>
<h2>Index</h2>
