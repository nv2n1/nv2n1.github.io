---
title: "fdebugdump(1)"
name: "fdebugdump"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fdebugdump/"
description: "fdebugdump – dumps a hierarchy of the debug info dies"
---

<h2 class="name">NAME</h2>
<p> fdebugdump &#8211; dumps a hierarchy of the debug info dies </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fdebugrpm</code> {<i>executable</i>}</dl>
<h2>DESCRIPTION</h2>
<p> <code>fdebugdump</code></p>
<dd>runs the given program and dumps a hierarchical view of libraries loaded at attach time. Does not watch for loading of new modules, but that would be a good extension.</p>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
fdebugdump ls
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-frysk/">frysk</a>(7)</p>
<h2>BUGS</h2>
<p> Report bugs to m[blue]<code><a rel="nofollow" href="http://sourceware.org/frysk">http://sourceware.org/frysk</a></code>m[] </p>
<h2>Index</h2>
