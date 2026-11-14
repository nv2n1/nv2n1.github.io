---
title: "afgetdataoffset(3)"
name: "afgetdataoffset"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afgetdataoffset/"
description: "afGetFrameCount, afGetTrackBytes, afGetDataOffset – get the total sample frame count, length of audio track in bytes, offset of the audio track for a track in an audio file"
---

<p>afGetFrameCount, afGetTrackBytes, afGetDataOffset &#8211; get the total sample frame count, length of audio track in bytes, offset of the audio track for a track in an audio file </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>AFframecount afGetFrameCount (AFfilehandle file, int track);</pre>
<pre>AFfileoffset afGetTrackBytes (AFfilehandle file, int track);</pre>
<pre>AFfileoffset afGetDataOffset (AFfilehandle file, int track);</pre>
<h2>Parameters</h2>
<p><i>file</i> is an audio file handle created by a previous call to <code><a href="/docs/linux/man/3-afopenfile/">afOpenFile</a></code>(3). </p>
<p> <i>track</i> is an integer which specifies an audio track within <i>file</i>. All supported file formats contain exactly one audio track per file, so the constant AF_DEFAULT_TRACK should always be used.</p>
<h2>Description</h2>
<p>afGetFrameCount returns the total number of sample frames contained within the specified track of the specified file. </p>
<p> Each sample frame of audio consists of a fixed number of samples (equal to the number of audio channels in the track. For monaural data, a sample frame consists of one audio sample. For stereophonic data, a sample frame consists of a stereo pair. </p>
<p> afGetTrackBytes returns the total number of bytes of raw audio data (i.e., prior to decompression or conversion) in the track. </p>
<p> afGetDataOffset returns the offset in bytes of the start of the audio data contained within the specified track of the specified file.</p>
<h2>Return Value</h2>
<p>afGetFrameCount returns the total number of sample frames in <i>track</i>. </p>
<p> afGetTrackBytes returns the total number of bytes of audio data in <i>track</i>. </p>
<p> afGetDataOffset returns the offset in bytes to the beginning of the audio data in <i>track</i>. </p>
<p> Each of these routines returns -1 in case of error.</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
