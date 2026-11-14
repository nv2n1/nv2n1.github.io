---
title: "lintianpathfsinfo(3)"
name: "lintianpathfsinfo"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianpathfsinfo/"
---

Lintian::Path::FSInfo - File System information for Lintian::Path 

<h2>Synopsis</h2><pre> my $l_path; # A L::Path object
 my $fs_info; # A L::Path::FSInfo object
 if ($fs_info-&gt;has_anchored_root_dir) {
 # The &quot;root&quot; dir is anchored and paths starting with &quot;/&quot; can
 # trivially be resolved (as relative to the &quot;root&quot; dir).
 } else {
 # The &quot;root&quot; dir is undefined and paths starting with &quot;/&quot; *cannot*
 # be resolved.
 }</pre><h2>Class Methods</h2><dl COMPACT><dt>new(<font SIZE="-1">OPTS</font>)
<dd>Internal constructor (used by Lintian::Collect::Package)</dl><h2>Instance Methods</h2><dl COMPACT><dt>_underlying_fs_path(<font SIZE="-1">PATH</font>)
<dd>Given <font SIZE="-1">PATH,</font> a Lintian::Path, obtain the underlying file system path that it represents.
<dt>_file_info(<font SIZE="-1">PATH</font>)
<dd>Given <font SIZE="-1">PATH,</font> a Lintian::Path, obtain the output from <i><a HREF="/docs/linux/man/1-file/">file</a></i>(1) about the file, if it has been collected. Throws an error if it not available.
<dt>has_anchored_root_dir
<dd>Returns a truth value if the ``root'' directory is anchored and is defined by the path string ``/''. In such cases, paths starting with ``/'' are well-defined semantically and are relative to the root directory rather than the ``current'' directory. 

 On the other hand, if this returns a non-truth value, the ``root'' directory is <i>not</i> well-defined and no path starting with ``/'' can be resolved logically.</dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i><a HREF="/docs/linux/man/3-lintian--path/">Lintian::Path</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--collect/">Lintian::Collect</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--collect--binary/">Lintian::Collect::Binary</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--collect--source/">Lintian::Collect::Source</a></i>(3)
