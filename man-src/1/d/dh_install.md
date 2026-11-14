---
title: "dh_install(1)"
name: "dh_install"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_install/"
description: "dh_install – install files into package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_install &#8211; install files into package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_install</code> [<code>-X</code><i>item</i>] [<code>&#8211;autodest</code>] [<code>&#8211;sourcedir=</code><i>dir</i>] [<i>debhelper options</i>] [<i>file|dir</i> &#8230; <i>destdir</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_install</code> is a debhelper program that handles installing files into package build directories. There are many <code>dh_install</code><i>*</i> commands that handle installing specific types of files such as documentation, examples, man pages, and so on, and they should be used when possible as they often have extra intelligence for those particular tasks. <code>dh_install</code>, then, is useful for installing everything else, for which no particular intelligence is needed. It is a replacement for the old <code>dh_movefiles</code> command. </p>
<p> This program may be used in one of two ways. If you just have a file or two that the upstream Makefile does not install for you, you can run <code>dh_install</code> on them to move them into place. On the other hand, maybe you have a large package that builds multiple binary packages. You can use the upstream <i>Makefile</i> to install it all into <i>debian/tmp</i>, and then use <code>dh_install</code> to copy directories and files from there into the proper package build directories. </p>
<p> From debhelper compatibility level 7 on, <code>dh_install</code> will fall back to looking in <i>debian/tmp</i> for files, if it does not find them in the current directory (or wherever you&#8217;ve told it to look using <code>&#8211;sourcedir</code>).</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.install</p>
<dd> List the files to install into each package and the directory they should be installed to. The format is a set of lines, where each line lists a file or files to install, and at the end of the line tells the directory it should be installed in. The name of the files (or directories) to install should be given relative to the current directory, while the installation directory is given relative to the package build directory. You may use wildcards in the names of the files to install. </p>
<p> Note that if you list exactly one filename or wildcard-pattern on a line by itself, with no explicit destination, then <code>dh_install</code> will automatically guess the destination to use, the same as if the &#8211;autodest option were used.</p>
<dt>debian/not-installed</p>
<dd> Used with the deprecated <code>&#8211;list-missing</code> and <code>&#8211;fail-missing</code> options. Please refer to <i><a href="/docs/linux/man/1-dh_missing/">dh_missing</a></i>(1) for the documentation of this file.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;list-missing</code></p>
<dd> <code>Deprecated</code>: Please use <code>dh_missing &#8211;list-missing</code> instead. If you use this option, <code>dh_install</code> will call <code>dh_missing</code> with that option after it has processed all the files. Please see <i><a href="/docs/linux/man/1-dh_missing/">dh_missing</a></i>(1) for the documentation of this option. </p>
<p> This option is removed in compat 12.</p>
<dt><code>&#8211;fail-missing</code></p>
<dd> <code>Deprecated</code>: Please use <code>dh_missing &#8211;fail-missing</code> instead. If you use this option, <code>dh_install</code> will call <code>dh_missing</code> with that option after it has processed all the files. Please see <i><a href="/docs/linux/man/1-dh_missing/">dh_missing</a></i>(1) for the documentation of this option. </p>
<p> This option is removed in compat 12.</p>
<dt><code>&#8211;sourcedir=</code><i>dir</i></p>
<dd> Look in the specified directory for files to be installed. </p>
<p> Note that this is not the same as the <code>&#8211;sourcedirectory</code> option used by the <code>dh_auto_</code><i>*</i> commands. You rarely need to use this option, since <code>dh_install</code> automatically looks for files in <i>debian/tmp</i> in debhelper compatibility level 7 and above.</p>
<dt><code>&#8211;autodest</code></p>
<dd> Guess as the destination directory to install things to. If this is specified, you should not list destination directories in <i>debian/package.install</i> files or on the command line. Instead, <code>dh_install</code> will guess as follows: </p>
<p> Strip off <i>debian/tmp</i> (or the sourcedir if one is given) from the front of the filename, if it is present, and install into the dirname of the filename. So if the filename is <i>debian/tmp/usr/bin</i>, then that directory will be copied to <i>debian/package/usr/</i>. If the filename is <i>debian/tmp/etc/passwd</i>, it will be copied to <i>debian/package/etc/</i>.</p>
<dt><i>file|dir</i> &#8230; <i>destdir</i></p>
<dd> Lists files (or directories) to install and where to install them to. The files will be installed into the first package <i>dh_install</i> acts on.</dl>
<h2>LIMITATIONS</h2>
<p> <code>dh_install</code> cannot rename files or directories, it can only install them with the names they already have into wherever you want in the package build tree. </p>
<p> However, renaming can be achieved by using <code>dh-exec</code> with compatibility level 9 or later. An example debian/<i>package</i>.install file using <code>dh-exec</code> could look like: </p>
<pre>
 #!/usr/bin/dh-exec
 debian/default.conf =&gt; /etc/my-package/start.conf
</pre>
<p> Please remember the following three things:</p>
<dl>
<dt>&bull;</p>
<dd> The package must be using compatibility level 9 or later (see <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7))</p>
<dt>&bull;</p>
<dd> The package will need a build-dependency on dh-exec.</p>
<dt>&bull;</p>
<dd> The install file must be marked as executable.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
