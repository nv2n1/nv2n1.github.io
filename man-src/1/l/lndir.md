---
title: "lndir(1)"
name: "lndir"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lndir/"
description: "lndir – create a shadow directory of symbolic links to another directory tree"
---

<h2>NAME</h2>
<p> lndir &#8211; create a shadow directory of symbolic links to another directory tree</p>
<h2>SYNOPSIS</h2>
<p> <code>lndir</code> [ <code>-silent</code> ] [ <code>-ignorelinks</code> ] [ <code>-withrevinfo</code> ] <i>fromdir</i> [ <i>todir</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>lndir</i> program makes a shadow copy <i>todir </i> of a directory tree <i>fromdir, </i> except that the shadow is not populated with real files but instead with symbolic links pointing at the real files in the <i>fromdir</i> directory tree. This is usually useful for maintaining source code for different machine architectures. You create a shadow directory containing links to the real source, which you will have usually mounted from a remote machine. You can build in the shadow tree, and the object files will be in the shadow directory, while the source files in the shadow directory are just symlinks to the real files. </p>
<p> This scheme has the advantage that if you update the source, you need not propagate the change to the other architectures by hand, since all source in all shadow directories are symlinks to the real thing: just cd to the shadow directory and recompile away. </p>
<p> The <i>todir</i> argument is optional and defaults to the current directory. The <i>fromdir</i> argument may be relative (e.g., ../src) and is relative to <i>todir</i> (not the current directory). </p>
<p> Note that BitKeeper, CVS, CVS.adm, .git, .hg, RCS, SCCS, and .svn directories are shadowed only if the <code>-withrevinfo</code> flag is specified. Files with names ending in <i>~</i> are never shadowed. </p>
<p> If you add files, simply run <i>lndir</i> again. New files will be silently added. Old files will be checked that they have the correct link. </p>
<p> Deleting files is a more painful problem; the symlinks will just point into never never land. </p>
<p> If a file in <i>fromdir</i> is a symbolic link, <i>lndir</i> will make the same link in <i>todir</i> rather than making a link back to the (symbolic link) entry in <i>fromdir.</i> The <code>-ignorelinks</code> flag changes this behavior.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-silent</p>
<dd> Normally <i>lndir</i> outputs the name of each subdirectory as it descends into it. The <code>-silent</code> option suppresses these status messages.</p>
<dt>-ignorelinks</p>
<dd> Causes the program to not treat symbolic links in <i>fromdir</i> specially. The link created in <i>todir</i> will point back to the corresponding (symbolic link) file in <i>fromdir</i>. If the link is to a directory, this is almost certainly the wrong thing.</p>
<dt>
<dd> This option exists mostly to emulate the behavior the C version of <i>lndir</i> had in X11R6. Its use is not recommended.</p>
<dt>-withrevinfo</p>
<dd> Causes any source control manager subdirectories (those named BitKeeper, CVS, CVS.adm, .git, .hg, RCS, SCCS, or .svn) to be treated as any other directory, rather than ignored.</dl>
<h2>DIAGNOSTICS</h2>
<p> The program displays the name of each subdirectory it enters, followed by a colon. The <code>-silent</code> option suppresses these messages. </p>
<p> A warning message is displayed if the symbolic link cannot be created. The usual problem is that a regular file of the same name already exists. </p>
<p> If the link already exists but doesn&#8217;t point to the correct file, the program prints the link name and the location where it does point.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ln/">ln</a></code>(1). </p>
<h2>Index</h2>
