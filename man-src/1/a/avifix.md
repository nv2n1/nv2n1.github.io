---
title: "avifix(1)"
name: "avifix"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avifix/"
description: "avifix – fix header of AVI-file"
---

<h2>NAME</h2>
<p> avifix &#8211; fix header of AVI-file</p>
<h2>SYNOPSIS</h2>
<p> <code>avifix</code> [ <code>-i</code> <i>name</i> [ <code>-F</code> <i>string</i> ] [ <code>-f</code> <i>val1</i><code>,</code><i>val2</i> ] [ <code>-N 0x</code> <i>NN</i> ] [ <code>-b</code> <i>bitrate</i> ] [ <code>-e</code> <i>rate</i><code>[,</code><i>bits</i><code>[,</code><i>channels</i><code>]]</code> ] [ <code>-a</code> <i>num</i> ] [ <code>-v</code> ] ]</p>
<h2>COPYRIGHT</h2>
<p> <code>avifix</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>avifix</code> fixes the header of an AVI-file with the supplied parameters.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> <i>name</i></p>
<dd> Specify the name of the AVI-file.</p>
<dt><code>-F</code> <i>string</i></p>
<dd> Specify the video codec as FourCC.<br />
 Possible values are <code>RGB</code>, <code>RIFF</code> and <code>TIFF</code>. ???</p>
<dt><code>-f</code><i> val1,val2</i></p>
<dd> Use this option to change the frame rate and scale information in the header of the AVI-file. Both values must not be &lt; 0.</p>
<dt><code>-N</code><i> 0xnn</i></p>
<dd> Use this option to change the audio format identifier in the header of the AVI-file. Here are some possible values: </p>
<p> 0x1 PCM uncompressed audio </p>
<p> 0x50 MPEG layer-2 aka MP2 </p>
<p> 0x55 MPEG layer-3 aka MP3 </p>
<p> 0x2000 AC3 audio</p>
<dt><code>-b</code><i> bitrate</i></p>
<dd> Use this option to change the encoder bitrate in the header of the AVI-file. <i>bitrate</i> has to be given in units of kbps.</p>
<dt><code>-e</code><i> rate[,bits[,channels]]</i></p>
<dd> Use this option to change the audio stream parameters of in the header of the AVI-file.</p>
<dt><code>-a</code><i> num</i></p>
<dd> Use this option to change the audio stream parameters of audio track number <i>num</i> in the header of the AVI-file.</p>
<dt><code>-v</code></p>
<dd> Print version information and exit.</dl>
<h2>EXAMPLES</h2>
<p> The command </p>
<p> <code>avifix -i my_file.avi -f 30,1</code> </p>
<p> changes the header of the file <i>my_file.avi</i> and sets the frame rate to 30 fps.</p>
<h2>AUTHORS</h2>
<p> <code>avifix</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
