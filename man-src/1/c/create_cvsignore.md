---
title: "create_cvsignore(1)"
name: "create_cvsignore"
section: "1"
letter: "c"
url: "/docs/linux/man/1-create_cvsignore/"
description: "create_cvsignore – Create preliminary .cvsignore in the current directory"
---

<h2>NAME</h2>
<p> create_cvsignore &#8211; Create preliminary .cvsignore in the current directory</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>createcvsignore</code> </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>create_cvsignore</code> is used to create a preliminary <i>.cvsignore</i> in the current directory. It does this based on certain contents it finds in <i>Makefile.am</i> </p>
<dd>No lines will be removed from any existing <i>.cvsignore</i>. If there is not already a <i>.cvsignore</i> file, it will be added to the cvs repository. </p>
<p> Note that you must have a <i>Makefile.am</i> in the current directory for this tool to work. </p>
<p> This utility is part of the KDE Software Development Kit. </p>
<h2>AUTHOR</h2>
<p> Ben Burton. </p>
<h2>Index</h2>
