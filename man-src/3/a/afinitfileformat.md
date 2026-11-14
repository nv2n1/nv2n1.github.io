---
title: "afinitfileformat(3)"
name: "afinitfileformat"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afinitfileformat/"
description: "afInitFileFormat – initialize file format of an audio file setup"
---

<p>afInitFileFormat &#8211; initialize file format of an audio file setup </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>void afInitFileFormat(AFfilesetup setup, int fileFormat);</pre>
<h2>Parameters</h2>
<p>setup is a valid file setup created by <code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3). </p>
<p> fileFormat is an integer constant specifying a file format.</p>
<h2>Description</h2>
<p>Given an AFfilesetup structure created with <code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3), afInitFileFormat initializes the file format to that specified by fileFormat. </p>
<p> The following file formats are currently supported: </p>
<p> AF_FILE_RAWDATA</p>
<dl COMPACT>
<dd>raw audio data</dl>
<p> AF_FILE_AIFF</p>
<dl COMPACT>
<dd>Audio Interchange File Format</dl>
<p> AF_FILE_AIFFC</p>
<dl COMPACT>
<dd>Audio Interchange File Format AIFF-C</dl>
<p> AF_FILE_NEXTSND</p>
<dl COMPACT>
<dd>NeXT .snd/Sun .au</dl>
<p> AF_FILE_WAVE</p>
<dl COMPACT>
<dd>Microsoft RIFF WAVE</dl>
<p> AF_FILE_BICSF</p>
<dl COMPACT>
<dd>Berkeley/IRCAM/CARL Sound File</dl>
<p> AF_FILE_AVR</p>
<dl COMPACT>
<dd>Audio Visual Research</dl>
<p> AF_FILE_IFF_8SVX</p>
<dl COMPACT>
<dd>Amiga IFF/8SVX</dl>
<p> AF_FILE_SAMPLEVISION</p>
<dl COMPACT>
<dd>Sample Vision</dl>
<p> AF_FILE_VOC</p>
<dl COMPACT>
<dd>Creative Voice File</dl>
<p> AF_FILE_NIST_SPHERE</p>
<dl COMPACT>
<dd>NIST SPHERE</dl>
<p> AF_FILE_CAF</p>
<dl COMPACT>
<dd>Core Audio Format</dl>
<h2>Errors</h2>
<p>afInitFileFormat can produce the following errors: </p>
<p> AF_BAD_FILESETUP</p>
<dl COMPACT>
<dd>setup represents an invalid file setup.</dl>
<p> AF_BAD_FILEFMT</p>
<dl COMPACT>
<dd>fileFormat represents an unknown file format.</dl>
<p> AF_BAD_NOT_IMPLEMENTED</p>
<dl COMPACT>
<dd>fileFormat represents a file format which is not currently implemented.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
