---
title: "afinitsampleformat(3)"
name: "afinitsampleformat"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afinitsampleformat/"
description: "afInitSampleFormat, afInitByteOrder, afInitChannels, afInitRate – initialize audio data format for a track in an audio file setup"
---

<p>afInitSampleFormat, afInitByteOrder, afInitChannels, afInitRate &#8211; initialize audio data format for a track in an audio file setup </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>void afInitSampleFormat(AFfilesetup setup, int track, int sampleFormat,
 int sampleWidth);
void afInitByteOrder(AFfilesetup setup, int track, int byteOrder);
void afInitChannels(AFfilesetup setup, int track, int channels);
void afInitRate(AFfilesetup setup, int track, double rate);</pre>
<h2>Parameters</h2>
<p>setup is a valid file setup returned by <code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3). </p>
<p> track specifies a track within the audio file setup. track is always AF_DEFAULT_TRACK for all currently supported file formats. </p>
<p> sampleFormat is a symbolic constant specifying the sample format for the audio data in the track. sampleFormat must be one of AF_SAMPFMT_TWOSCOMP, AF_SAMPFMT_UNSIGNED, AF_SAMPFMT_FLOAT, or AF_SAMPFMT_DOUBLE. </p>
<p> sampleWidth is a positive integer specifying the number of bits for each sample in the track. </p>
<p> byteOrder is a symbolic constant specifying the byte order of the track. byteOrder must be one of AF_BYTEORDER_BIGENDIAN or AF_BYTEORDER_LITTLEENDIAN. </p>
<p> channels is a positive integer specifying the number of channels in the track. </p>
<p> rate is a positive double-precision floating-point number specifying the sample rate of the track.</p>
<h2>Description</h2>
<p>afInitSampleFormat initializes the track to the specified sample format and sample width. </p>
<p> afInitByteOrder initializes the track to the specified byte order. </p>
<p> afInitChannels initializes the track to the specified number of channels. </p>
<p> afInitRate initializes the track to the specified sample rate.</p>
<h2>Errors</h2>
<p>afInitSampleFormat, afInitByteOrder, afInitChannels, and afInitRate can produce the following errors: </p>
<table>
<tr VALIGN=top>
<td>
<p> AF_BAD_FILESETUP </td>
<td>
<p> setup represents an invalid file setup.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> AF_BAD_TRACK </td>
<td>
<p> track represents an invalid track identifier.
</td>
</tr>
</table>
<p> afInitSampleFormat can also produce the following errors: </p>
<table>
<tr VALIGN=top>
<td>
<p> AF_BAD_SAMPFMT </td>
<td>
<p> sampleFormat does not represent a valid sample format.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> AF_BAD_WIDTH </td>
<td>
<p> sampleWidth is not a valid sample width.
</td>
</tr>
</table>
<p> afInitByteOrder can also produce the following error: </p>
<table>
<tr VALIGN=top>
<td>
<p> AF_BAD_BYTEORDER </td>
<td>
<p> byteOrder does not represent a valid byte order.
</td>
</tr>
</table>
<p> afInitChannels can also produce the following error: </p>
<table>
<tr VALIGN=top>
<td>
<p> AF_BAD_CHANNELS </td>
<td>
<p> channels specifies an invalid number of channels.
</td>
</tr>
</table>
<p> afInitRate can also produce the following error: </p>
<table>
<tr VALIGN=top>
<td>
<p> AF_BAD_RATE </td>
<td>
<p> rate specifies an invalid sample rate.
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3), <code><a href="/docs/linux/man/3-afinitfileformat/">afInitFileFormat</a></code>(3), <code><a href="/docs/linux/man/3-afinitcompression/">afInitCompression</a></code>(3), <code><a href="/docs/linux/man/3-afopenfile/">afOpenFile</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
