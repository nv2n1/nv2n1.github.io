---
title: "tcxmlcheck(1)"
name: "tcxmlcheck"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcxmlcheck/"
description: "tcxmlcheck – Check information in smil input file"
---

<h2>NAME</h2>
<p> tcxmlcheck &#8211; Check information in smil input file</p>
<h2>SYNOPSIS</h2>
<p> <code>tcxmlcheck</code> [ <code>options</code> ] [ <code>&#8211;</code> ]</p>
<h2>COPYRIGHT</h2>
<p> <code>tcxmlcheck</code> is Copyright (C) by Malanchini Marzio</p>
<h2>DESCRIPTION</h2>
<p> <code>tcxmlcheck</code> Check a smil input file. Most of the options are used by transcode at run time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> <i>name</i></p>
<dd> Specify the name of the input video/audio smil file [stdin].</p>
<dt><code>-p</code> <i>name</i></p>
<dd> Specify the name of the ausiliary audio smil file [none]</p>
<dt><code>-B</code></p>
<dd> Binary output to stdout (used by transcode) [off] Force to print to stdout the vob structure of the smil file</p>
<dt><code>-S</code></p>
<dd> Write stdin into shared memory (used by transcode)[off]. This is used by transcode at run time to store the vob information that will be modified by calling <code>tcxmlcheck</code> with the -V or -A options.</p>
<dt><code>-V</code></p>
<dd> Check only video smil file [off]. This is used by transcode at run time: it read the smil file to override some information in the vob structure.</p>
<dt><code>-A</code></p>
<dd> Check only ausiliary audio smil file [off]. This is used by transcode at run time: it read the smil file to override some information in the vob structure.</p>
<dt><code>-v</code></p>
<dd> Print the version</dl>
<h2>EXAMPLES</h2>
<p> Command: </p>
<p> <code>tcxmlcheck -i filename.smil</code> </p>
<p> Return <code>0</code> if the input file is correct, <code>1</code> with an error message in the other cases. </p>
<p> <code>tcxmlcheck -i filename.smil -S -B -V</code> </p>
<p> Analyze the <code>filename.smil</code> and store the vob structure into share memory (used only by transcode at run time). </p>
<p> <code>tcxmlcheck -i filename.smil -B -V</code> </p>
<p> Retrive the content from the share memory related to <code>filename.smil</code> (used only by transcode at run time). </p>
<h2>AUTHORS</h2>
<p> <code>tcxmlcheck</code> was written by Marzio Malanchini<br />
 &lt;marzio_malanchini [at] vodafone.it&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
