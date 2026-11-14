---
title: "afinitaeschanneldatato(3)"
name: "afinitaeschanneldatato"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afinitaeschanneldatato/"
description: "afInitAESChannelDataTo, afInitAESChannelData – initialize AES non-audio data in an audio file setup"
---

<p>afInitAESChannelDataTo, afInitAESChannelData &#8211; initialize AES non-audio data in an audio file setup </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>void afInitAESChannelDataTo(AFfilesetup setup, int track, int willHaveData);
void afInitAESChannelData(AFfilesetup setup, int track);</pre>
<h2>Parameters</h2>
<p>setup is a valid file setup returned by <code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3). </p>
<p> track specifies a track within the audio file setup. track is always AF_DEFAULT_TRACK for all currently supported file formats. </p>
<p> willHaveData is a boolean-valued integer indicating whether AES non-audio data will be present.</p>
<h2>Description</h2>
<p>Given an AFfilesetup structure created with <code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3) and a track identified by track (AF_DEFAULT_TRACK for all currently supported file formats), afInitAESChannelDataTo initializes the track to contain or not contain AES non-audio data. afInitAESChannelData behaves similarly but always initializes the track to contain AES non-audio data. </p>
<p> Currently only AIFF and AIFF-C file formats can store AES non-audio data; this data is ignored in all other file formats.</p>
<h2>Errors</h2>
<p>afInitAESChannelDataTo and afInitAESChannelData can produce the following errors: </p>
<p> AF_BAD_FILESETUP</p>
<dl COMPACT>
<dd>setup represents an invalid file setup.</dl>
<p> AF_BAD_TRACKID</p>
<dl COMPACT>
<dd>track represents an invalid track identifier.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
