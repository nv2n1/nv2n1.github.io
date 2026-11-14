---
title: "fgconsole(1)"
name: "fgconsole"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fgconsole/"
description: "fgconsole – print the number of the active VT."
---

<h2 class="name">NAME</h2>
<p> fgconsole &#8211; print the number of the active VT.</p>
<h2>SYNOPSIS</h2>
<p> <code>fgconsole</code> [ <code>-h &#8211;help</code> | <code>-V &#8211;version</code> | <code>-n &#8211;next-available</code> ]</p>
<h2>DESCRIPTION</h2>
<p> If the active Virtual Terminal is <i>/dev/ttyN</i>, then prints <i>N</i> on standard output. </p>
<p> If the console is a serial console, then &quot;serial&quot; is printed instead.</p>
<dl>
<dt><i>-h &#8211;help</i></p>
<dd> Prints short usage message and exits.</p>
<dt><i>-V &#8211;version</i></p>
<dd> Prints version number and exits.</p>
<dt><i>&#8211;next-available</i></p>
<dd> Will show the next unallocated virtual terminal. Normally 6 virtual terminals are allocated, with number 7 used for X; this will return &quot;8&quot; in this case. </p>
</dl>
<h2>NOTES</h2>
<p> Under <i>devfs</i>, the consoles are in <i>/dev/vc/N</i>. <i>devfsd</i> may maintain symlinks for compatibility.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chvt/">chvt</a></code>(1). </p>
<h2>Index</h2>
