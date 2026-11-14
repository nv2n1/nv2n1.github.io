---
title: "sfconvert(1)"
name: "sfconvert"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfconvert/"
description: "sfconvert – convert audio files"
---

<h2 class="name">NAME</h2>
<p> sfconvert &#8211; convert audio files </p>
<h2>SYNOPSIS</h2>
<p> <code>sfconvert</code> <i>infile</i> <i>outfile</i> [<i>output options</i>]</p>
<h2>DESCRIPTION</h2>
<p> The sfconvert command converts an audio file to another file format or data format.</p>
<h2>OPTIONS</h2>
<p> The following keywords specify the format of the output sound file: </p>
<p> format <i>f</i></p>
<dl>
<dt>
<dd> Output file format. <i>f</i> must be one of the following: </p>
<table>
<tr VALIGN=top>
<td> aiff </td>
<td> Audio Interchange File Format
</td>
</tr>
<tr VALIGN=top>
<td> aifc </td>
<td> AIFF-C
</td>
</tr>
<tr VALIGN=top>
<td> next </td>
<td> NeXT/Sun .snd/.au Format
</td>
</tr>
<tr VALIGN=top>
<td> wave </td>
<td> MS RIFF WAVE
</td>
</tr>
<tr VALIGN=top>
<td> bicsf </td>
<td> Berkeley/IRCAM/CARL Sound File Format
</td>
</tr>
<tr VALIGN=top>
<td> smp </td>
<td> Sample Vision Format
</td>
</tr>
<tr VALIGN=top>
<td> voc </td>
<td> Creative Voice File Format
</td>
</tr>
<tr VALIGN=top>
<td> nist </td>
<td> NIST SPHERE Format
</td>
</tr>
<tr VALIGN=top>
<td> caf </td>
<td> Core Audio Format
</td>
</tr>
<tr VALIGN=top>
<td> flac </td>
<td> FLAC
</td>
</tr>
</table>
</dl>
<p> compression <i>c</i></p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td> ulaw </td>
<td> G.711 mu-law
</td>
</tr>
<tr VALIGN=top>
<td> alaw </td>
<td> G.711 A-law
</td>
</tr>
<tr VALIGN=top>
<td> ima </td>
<td> IMA ADPCM
</td>
</tr>
<tr VALIGN=top>
<td> msadpcm </td>
<td> Microsoft ADPCM
</td>
</tr>
<tr VALIGN=top>
<td> flac </td>
<td> FLAC
</td>
</tr>
<tr VALIGN=top>
<td> alac </td>
<td> Apple Lossless Audio Codec
</td>
</tr>
</table>
</dl>
<p> byteorder <i>e</i></p>
<dl>
<dt>
<dd> Output byte order. <i>e</i> may be either big or little.</dl>
<p> channels <i>n</i></p>
<dl>
<dt>
<dd> Number of output channels. <i>n</i> is 1 for mono, and 2 for stereo.</dl>
<p> integer <i>n</i> <i>s</i></p>
<dl>
<dt>
<dd> Convert to integer audio data. <i>n</i> indicates the output sample width in bits. <i>s</i> specifies the sample format and may be either 2scomp for 2&#8217;s complement signed data or unsigned for unsigned data.</dl>
<p> float <i>m</i></p>
<dl>
<dt>
<dd> Convert to floating-point audio data with a maximum amplitude of <i>m</i> (usually 1.0). The integer and float options are mutually exclusive.</dl>
<p> The following options take no additional arguments: </p>
<p> &#8211;help, -h</p>
<dl>
<dt>
<dd> Print help message.</dl>
<p> &#8211;version, -v</p>
<dl>
<dt>
<dd> Print version information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sfinfo/">sfinfo</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Michael Pruett &lt;michael [at] 68k.org&gt; </p>
<h2>Index</h2>
