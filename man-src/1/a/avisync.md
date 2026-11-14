---
title: "avisync(1)"
name: "avisync"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avisync/"
description: "avisync – adjust audio synchronisation"
---

<h2>NAME</h2>
<p> avisync &#8211; adjust audio synchronisation</p>
<h2>SYNOPSIS</h2>
<p> <code>avisync</code> [ <code>-o</code> <i>file</i> <code>-i</code> <i>file</i> <code>-q</code> <code>-n</code> <i>num</i> <code>-b</code> <i>num</i> <code>-a</code> <i>track</i> <code>-f</code> <i>commentfile</i> ]</p>
<h2>COPYRIGHT</h2>
<p> <code>avisync</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>avisync</code> shift audio on frame basis.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> <i>name</i></p>
<dd> Specify the name of the output file.</p>
<dt><code>-i</code> <i>file</i></p>
<dd> Specify the name of the input file.</p>
<dt><code>-q</code></p>
<dd> be less verbose.</p>
<dt><code>-n</code> <i>count</i></p>
<dd> shift audio by <i>count</i> frames. If <i>count</i> is positive, audio starts with audio frame <i>count</i> at the beginning of the AVI-file. If <i>count</i> is negative, audio is prepended <i>count</i> padding frames.</p>
<dt><code>-a</code> <i>track</i></p>
<dd> Specify the number of the audio channel to shift.</p>
<dt><code>-b</code> <i>num</i></p>
<dd> Specify if avisync should write an VBR mp3 header into the AVI file. Default is 1 because it does not hurt. <i>num</i> is either 1 or 0.</p>
<dt><code>-f</code> <i>commentfile</i></p>
<dd> Read AVI tombstone data for header comments from <i>commentfile</i>. See /docs/avi_comments.txt for a sample.</dl>
<h2>EXAMPLES</h2>
<p> The command </p>
<p> <code>avisync -i my_file1.avi -o out.avi -n -10</code> </p>
<p> puts 10 audio frames at the beginning of the AVI-file. </p>
<p> E.g. if the audio is delayed about 200 ms (0.2 seconds) and you&#8217;re working with a 25 frames per second AVI-File, you need to shift the audio 200/40 = 5 frames since one frame is 40 ms long.</p>
<h2>AUTHORS</h2>
<p> <code>avisync</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aviindex/">aviindex</a></code>(1), <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
