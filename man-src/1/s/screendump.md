---
title: "screendump(1)"
name: "screendump"
section: "1"
letter: "s"
url: "/docs/linux/man/1-screendump/"
description: "screendump – dump the contents of a virtual console to stdout"
---

<h2 class="name">NAME</h2>
<p> screendump &#8211; dump the contents of a virtual console to stdout</p>
<h2>SYNOPSIS</h2>
<p> <code>screendump </code> [ <i>N</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The <code>screendump</code> command dumps the contents of virtual console <code>N</code> , (or the current console if N is omitted) to standard out. </p>
<p> Just saying</p>
<dl>
<dt>
<dd> cat /dev/vcsN</dl>
<p> has a similar effect. </p>
<h2>NOTES</h2>
<p> For security reasons, <code>screendump</code> uses linux devices &quot;virtual console screen&quot; and &quot;virtual console screen with attributes&quot; to give access for screendump. </p>
<p> Ensure these files exist, using </p>
<dl>
<dt>
<dd> cd /dev for i in 0 1 2 3 &#8230;; do<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>mknod vcs$i c 7 $i</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>mknod vcsa$i c 7 `expr 128 + $i`</p>
<p> done</dl>
<p> (filling in the ellipses) and give the device files appropriate permissions, or run <code>screendump</code> as root. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-setterm/">setterm</a></code>(1) </p>
<h2>Index</h2>
