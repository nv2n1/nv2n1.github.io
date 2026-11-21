---

title: "cheatmake(1)"
name: "cheatmake"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cheatmake/"
description: "cheatmake – fool make into not rebuilding certain files"
---

<p> cheatmake &#8211; fool <code>make</code> into not rebuilding certain files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cheatmake</code> [<code>hidechange</code><i>file</i>] [<code>show</code>] [<code>why</code><i>file</i>]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>cheatmake</code></p>
<dd>is used to save time when recompiling. It can fool make into skipping files that haven&#8217;t changed in a meaningful way. This can be used for instance when you change a comment in a file but none of the actual code. </dd>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>OPTIONS</h2>
<p> <code>hidechange</code> <i>file</i></p>
<dl>
<dt>
</dt><dd> Hides the fact that file was changed by setting the timestamp into the past. Use with care!</dd></dl>
<p> <code>show</code></p>
<dl>
<dt>
</dt><dd> Lists what files <code>make</code> currently needs to rebuild</dd></dl>
<p> <code>why</code> <i>file</i></p>
<dl>
<dt>
</dt><dd> Explains why make must rebuild file</dd></dl>
<h2>ENVIRONMENT</h2>
<p> One of the following variables (but not both) should be set if the source directory is different from the build directory. If the build directory is simply a subdirectory of the source directory, the simpler variable <code>OBJ_SUBDIR</code> should be used. </p>
<p> <code>OBJ_SUBJDIR</code></p>
<dl>
<dt>
</dt><dd> Indicates that the build directory is in the given subdirectory of the source directory. For instance, if the source directory is kdesdk and the build directory is kdesdk/obj-i386-linux, then <code>OBJ_SUBDIR</code> should be set to <i>obj-i386-linux</i>.</dd></dl>
<p> <code>OBJ_REPLACEMENT</code></p>
<dl>
<dt>
</dt><dd> A <code>sed</code> expression that is used to transform the source directory into the build directory. For instance, if the source directory is kdesdk/obj-i386-linux, then <code>OBJ_REPLACEMENT</code> should be set to <i>s#kdesdk#kdesdk-obj#</i>.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-make/">make</a>(1)</p>
<h2>AUTHORS</h2>
<p> <code>cheatmake</code> was written by David Faure&lt;faure [at] kde.org&gt;. This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt; for the Debian GNU/Linux&#174; system (but may be used by others). </p>
