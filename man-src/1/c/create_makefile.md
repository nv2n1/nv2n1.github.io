---
title: "create_makefile(1)"
name: "create_makefile"
section: "1"
letter: "c"
url: "/docs/linux/man/1-create_makefile/"
description: "create_makefile – Creates Makefile.in and Makefile from a Makefile.am"
---

<h2 class="name">NAME</h2>
<p> create_makefile &#8211; Creates Makefile.in and Makefile from a Makefile.am </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>create_makefile</code> [<i>relativepath/Makefile</i>] [<i>relativepath</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>create_makefile</code></p>
<dd>creates the Makefile.in and Makefile in a subdirectory containing a Makefile.am. This script saves time compared to re-running configure completely </p>
<p> Note that you must supply the path to the desired MakefileMakefile.am (though the final /Makefile may be omitted). </p>
<p> This script may be run from the toplevel directory (the one containing configure) or from one of it&#8217;s subdirectories. </p>
<p> If the source directory is different from the build directory (see the environment variables below), it will be assumed that the Makefile.am and Makefile.in belong beneath the source directory and that the Makefile belongs beneath the build directory. </p>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>ENVIRONMENT</h2>
<p> One of the following variables (but not both) should be set if the source directory is different from the build directory. If the build directory is simply a subdirectory of the source directory, the simpler variable <code>OBJ_SUBDIR</code> should be used. </p>
<p> <code>OBJ_SUBJDIR</code></p>
<dl>
<dt>
<dd> Indicates that the build directory is in the given subdirectory of the source directory. For instance, if the source directory is kdesdk and the build directory is kdesdk/obj-i386-linux, then <code>OBJ_SUBDIR</code> should be set to <i>obj-i386-linux</i>.</dl>
<p> <code>OBJ_REPLACEMENT</code></p>
<dl>
<dt>
<dd> A <code>sed</code> expression that is used to transform the source directory into the build directory. For instance, if the source directory is ~/src/kdesdk and the build directory is ~/src/kdesdk-obj, then <code>OBJ_REPLACEMENT</code> should be set to <i>s#kdesdk#kdesdk-obj#</i>.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-create_makefiles/">create_makefiles</a>(1)</p>
<h2>AUTHORS</h2>
<p> create_makefile was written by David Faure&lt;faure [at] kde.org&gt; and others. This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
