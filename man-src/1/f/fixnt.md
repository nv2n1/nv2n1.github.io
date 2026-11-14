---
title: "fixnt(1)"
name: "fixnt"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fixnt/"
description: "fixnt – Filter for the Windows NT postscript printer driver."
---

<h2 class="name">NAME</h2>
<p> fixnt &#8211; Filter for the Windows NT postscript printer driver. </p>
<h2>SYNOPSIS</h2>
<p> <code>fixnt </code> &lt; <i>BADFILE.ps </i> &gt; <i>GOODFILE.ps</i></p>
<h2>DESCRIPTION</h2>
<p> The Windows NT postscript driver has a tendency to make broken postscript files, that are incompatible with psutils. <code>fixnt</code> is a filter that fixes these problems, allowing the use of <a href="/docs/linux/man/1-psnup/">psnup</a>(1). </p>
<p> The filter takes the broken postscript file on <code>stdin</code>, and outputs a fixed postscript file on <code>stdout</code>. It has no other form for invocation and takes no options on the command-line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>fixnt</code></p>
<dd> takes no options.</dl>
<h2>BUGS</h2>
<p> <code>fixnt</code> does not check for NTPSOct94. For a workaround, use a <a href="/docs/linux/man/1-sed/">sed</a>(1) command to replace &#8216;NTPSOct94&#8217; with &#8216;NTPSOct95&#8217;, like so:</p>
<dl>
<dt>
<dd> sed &#8216;s/NTPSOct94/NTPSOct95/g&#8217;</dl>
<p> This is particularly important for Windows NT 3.5 users.</p>
<h2>AUTHOR</h2>
<p> <code>fixnt</code> was written by Holger Bauer &lt;Holger.Bauer [at] topmail.de&gt;, Michael Rath &lt;rath [at] itsm.uni-stuttgart.de&gt;, and Akim Demaille &lt;demaille [at] inf.enst.fr&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the Authors, but avoid sending large postscript files. </p>
<p> Patches are always welcome; send to &lt;bauer [at] itsm.uni-stuttgart.de&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psnup/">psnup</a>(1), <a href="/docs/linux/man/1-sed/">sed</a>(1) </p>
<h2>Index</h2>
