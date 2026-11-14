---
title: "kayadoc2man(1)"
name: "kayadoc2man"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kayadoc2man/"
description: "kayadoc2man – Automatic man pages for Kaya modules"
---

<h2>NAME</h2>
<p> kayadoc2man &#8211; Automatic man pages for Kaya modules</p>
<h2>SYNOPSIS</h2>
<p> <code>kayadoc2man</code> <i>XMLFILE [DONEFILE] [LICENSEFILE]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>kayadoc2man</code> creates a man page for every function and data type from an .xml file generated with the -xmldocs option of <code><a href="/docs/linux/man/1-kayac/">kayac</a>(1)</code>. Pass it the path to the XML documentation file to parse, and optionally (to ease Makefile writing) the name of a file to create when processing is complete. The third option allows you to specify your own author and license information (if this is omitted, <code>kayadoc2man</code> will assume that it is generating documentation for the Kaya standard library). If you want to specify the third option but not the second, you can of course use <code>/dev/null</code> for the <i>DONEFILE</i> on most systems. </p>
<p> Prior to Kaya 0.3.0 this utility was called xml2man </p>
<h2>OBTAINING</h2>
<p> The latest release of Kaya can be obtained from &lt;<a rel="nofollow" href="http://kayalang.org/download">http://kayalang.org/download</a>&gt;. </p>
<p> Development versions can be obtained using <code><a href="/docs/linux/man/1-darcs/">darcs</a>(1)</code> from &lt;<a rel="nofollow" href="http://kayalang.org/darcs/">http://kayalang.org/darcs/</a>&gt; </p>
<h2>BUGS</h2>
<p> Please report bugs found to &lt;kaya [at] kayalang.org&gt; </p>
<h2>LICENSE</h2>
<p> <code>kayadoc2man</code> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License (version 2 or any later version) as published by the Free Software Foundation. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-man/">man</a>(1)</code> <code><a href="/docs/linux/man/1-kayac/">kayac</a>(1)</code> </p>
<h2>Index</h2>
