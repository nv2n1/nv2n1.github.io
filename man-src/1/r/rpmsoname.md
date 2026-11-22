---

title: "rpmsoname(1)"
name: "rpmsoname"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmsoname/"
description: "rpmsoname – list files that provide sonames in RPM package(s)"
---

<p> rpmsoname &#8211; list files that provide sonames in RPM package(s) </p>
<h2>SYNOPSIS</h2>
<p> <code>rpmsoname</code> [<code>-h</code>] [<i>options</i>] [<i></i><i>FILE</i><i></i>&#8230;] [<i></i><i>DIR</i><i></i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>rpmsoname</code> produces two-column output (typically one line per each soname). Column one contains file path; column two contains corresponding soname. When processing a directory, an additional column is prepended to the output, which is typically RPM file basename. </p>
<p> Note that the name <code>rpmsoname</code> is probably a misnomer: the script does not deal with ELF <tt>&quot;DT_SONAME&quot;</tt> entries. What it does is try to map soname-like entries from RPM <tt>&quot;PROVIDES&quot;</tt> list to regular files within the very same RPM package (using <tt>&quot;BASENAMES&quot;</tt>, <tt>&quot;FILENAMES&quot;</tt>, and <tt>&quot;FILELINKTOS&quot;</tt> lists from RPM header).</p>
<h2>OPTIONS</h2>
<p> Options and arguments manage a set of RPM packages to be processed; they are those of <i><a href="/docs/linux/man/1-rpmargs/">rpmargs</a></i>(1).</p>
<h2>AUTHOR</h2>
<p> Written by Alexey Tourbin &lt;at [at] altlinux.org&gt;.</p>
<h2>COPYING</h2>
<p> Copyright (c) 2006 Alexey Tourbin, ALT Linux Team. </p>
<p> This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rpmargs/">rpmargs</a></i>(1) </p>
