---
title: "afopenfile(3)"
name: "afopenfile"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afopenfile/"
description: "afOpenFile – open an audio file and create a file handle structure used for subsequent calls to the Audio File Library"
---

<p>afOpenFile &#8211; open an audio file and create a file handle structure used for subsequent calls to the Audio File Library </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>AFfilehandle afOpenFile(const char *path, const char *mode,
 AFfilesetup setup);</pre>
<h2>Parameters</h2>
<p><i>path</i> is the path to the file to be opened. </p>
<p> <i>mode</i> specifies a mode for opening the file: &quot;r&quot; for reading or &quot;w&quot; for writing. </p>
<p> <i>setup</i> is an AFfilesetup created by <code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3). This value is ignored for files opened for reading except when the file format is AF_FILE_RAWDATA.</p>
<h2>Return Value</h2>
<p>Upon success, afOpenFile returns a valid AFfilehandle which can be used in subsequent calls to the Audio File Library. Upon failure, afOpenFile returns NULL and generates an error. </p>
<p> <code><a href="/docs/linux/man/3-afclosefile/">afCloseFile</a></code>(3) is used to close the file when it is no longer needed.</p>
<h2>Errors</h2>
<p>afOpenFile can produce the following errors: </p>
<p> AF_BAD_OPEN</p>
<dl COMPACT>
<dd>A call to open failed.</dl>
<p> AF_BAD_READ</p>
<dl COMPACT>
<dd>A call to read failed</dl>
<p> AF_BAD_WRITE</p>
<dl COMPACT>
<dd>A call to write failed.</dl>
<p> AF_BAD_LSEEK</p>
<dl COMPACT>
<dd>A call to lseek failed.</dl>
<p> AF_BAD_MALLOC</p>
<dl COMPACT>
<dd>Memory allocation failed.</dl>
<p> AF_BAD_FILEFMT</p>
<dl COMPACT>
<dd>setup specifies a file format which is unsupported for mode.</dl>
<p> AF_BAD_SAMPFMT</p>
<dl COMPACT>
<dd>The file&#8217;s sample format is not supported.</dl>
<p> AF_BAD_WIDTH</p>
<dl COMPACT>
<dd>The file&#8217;s sample width is not supported.</dl>
<p> AF_BAD_RATE</p>
<dl COMPACT>
<dd>The file&#8217;s sample rate is not supported.</dl>
<p> AF_BAD_CHANNELS</p>
<dl COMPACT>
<dd>The number of channels in the file is not supported.</dl>
<p> AF_BAD_FILESETUP</p>
<dl COMPACT>
<dd>setup specifies an invalid or unsupported configuration.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-afclosefile/">afCloseFile</a></code>(3), <code><a href="/docs/linux/man/3-afnewfilesetup/">afNewFileSetup</a></code>(3), <code><a href="/docs/linux/man/3-afinitfileformat/">afInitFileFormat</a></code>(3), <code><a href="/docs/linux/man/3-afinitsampleformat/">afInitSampleFormat</a></code>(3), <code><a href="/docs/linux/man/3-afreadframes/">afReadFrames</a></code>(3), <code><a href="/docs/linux/man/3-afwriteframes/">afWriteFrames</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
