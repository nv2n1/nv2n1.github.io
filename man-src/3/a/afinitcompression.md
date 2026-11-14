---
title: "afinitcompression(3)"
name: "afinitcompression"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afinitcompression/"
description: "afInitCompression – initialize compression for a track in an audio file setup"
---

<p>afInitCompression &#8211; initialize compression for a track in an audio file setup </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>void afInitCompression(AFfilesetup setup, int track, int compression);</pre>
<h2>Parameters</h2>
<p>setup is a valid file setup returned by <code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3). </p>
<p> track specifies a track within the audio file setup. track is always AF_DEFAULT_TRACK for all currently supported file formats. </p>
<p> compression is an identifier specifying the compression type (such as AF_COMPRESSION_G711_ULAW) to be used for audio data in the track.</p>
<h2>Description</h2>
<p>Given an AFfilesetup structure created with <code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3) and a track identified by track (AF_DEFAULT_TRACK for all currently supported file formats), afInitCompression initializes the track to the specified compression. </p>
<p> The following compression types are currently supported: </p>
<p> AF_COMPRESSION_NONE</p>
<dl COMPACT>
<dd>no compression</dl>
<p> AF_COMPRESSION_G711_ULAW</p>
<dl COMPACT>
<dd>CCITT G.711 mu-law encoding</dl>
<p> AF_COMPRESSION_G711_ALAW</p>
<dl COMPACT>
<dd>CCITT G.711 A-law encoding</dl>
<p> AF_COMPRESSION_IMA</p>
<dl COMPACT>
<dd>IMA ADPCM encoding</dl>
<p> AF_COMPRESSION_MS_ADPCM</p>
<dl COMPACT>
<dd>MS ADPCM encoding</dl>
<p> AF_COMPRESSION_FLAC</p>
<dl COMPACT>
<dd>FLAC</dl>
<p> AF_COMPRESSION_ALAC</p>
<dl COMPACT>
<dd>Apple Lossless Audio Codec</dl>
<h2>Errors</h2>
<p>afInitCompression can produce the following errors: </p>
<p> AF_BAD_FILESETUP</p>
<dl COMPACT>
<dd>setup represents an invalid file setup.</dl>
<p> AF_BAD_TRACKID</p>
<dl COMPACT>
<dd>track represents an invalid track identifier.</dl>
<p> AF_BAD_COMPTYPE</p>
<dl COMPACT>
<dd>compression represents an invalid compression type.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3), <code><a href="/docs/linux/man/3-afinitsampleformat/">afInitSampleFormat</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
