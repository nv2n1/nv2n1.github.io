---
title: "create_makefiles(1)"
name: "create_makefiles"
section: "1"
letter: "c"
url: "/docs/linux/man/1-create_makefiles/"
description: "create_makefiles – Recreates all Makefiles beneath a directory"
---

<h2>NAME</h2>
<p> create_makefiles &#8211; Recreates all Makefiles beneath a directory</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>create_makefiles</code> [<i>dir</i>] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>create_makefiles</code> recreates all <i>Makefile</i>s in <i>dir</i> and its (recursed) subdirectories from the corresponding <i>Makefile.am</i> templates. </p>
<dd>This script must be run from the toplevel directory (the one containing configure). This script saves time compared to re-running configure completely. </p>
<p> If the source directory is different from the build directory (see the environment variables below), it will be assumed that each <i>Makefile.am</i> and <i>Makefile.in</i> belongs beneath the source directory and that each <i>Makefile</i> belongs beneath the build directory. </p>
<p> This utility is part of the KDE Software Development Kit. </p>
<h2>ENVIRONMENT</h2>
<p> One of the following variables (but not both) should be set if the source directory is different from the build directory. If the build directory is simply a subdirectory of the source directory, the simpler variable <code>OBJ_SUBDIR</code> should be used. </p>
<dl>
<dt><code>OBJ_SUBJDIR</code></p>
<dd> Indicates that the build directory is in the given subdirectory of the source directory. For instance, if the source directory is <i>kdesdk</i> and the build directory is <i>kdesdk/obj-i386-linux</i>, then <code>OBJ_SUBDIR</code> should be set to <i>obj-i386-linux</i>. </p>
<dt><code>OBJ_REPLACEMENT</code></p>
<dd> A <code>sed</code> expression that is used to transform the source directory into the build directory. For instance, if the source directory is <i>kdesdk/obj-i386-linux</i>, then <code>OBJ_REPLACEMENT</code> should be set to <i>s#kdesdk#kdesdk-obj#</i>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-create_makefile/">create_makefile</a>(1) <a href="/docs/linux/man/2-make/">make</a>(2) </p>
<h2>AUTHORS</h2>
<p> <code>create_makefiles</code> was written by David Faure &lt;faure [at] kde.org&gt;. </p>
<p> This manual page was prepared by Ben Burton &lt;bab [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
