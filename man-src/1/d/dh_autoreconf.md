---
title: "dh_autoreconf(1)"
name: "dh_autoreconf"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_autoreconf/"
description: "dh_autoreconf – Call autoreconf -f -i and keep track of the changed files."
---

<h2 class="name">NAME</h2>
<p> dh_autoreconf &#8211; Call autoreconf -f -i and keep track of the changed files. </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_autoreconf</code> [<i>debhelper options</i>] [<code>-X</code><i>item</i>] [<code>&#8211;mode=</code><i>mode</i>] [<i>program</i>&nbsp;<code>&#8212;</code>&nbsp;<i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> dh_autoreconf is responsible for calling autoreconf and creating the files debian/autoreconf.before and debian/autoreconf.after which contain checksums of all files before/after the build. It is complemented by dh_autoreconf_clean which creates a list of all changed and added files and removes them. </p>
<p> Please note that dh_autoreconf can only be run once. Thus, if you need to run multiple commands, use a script or similar. An example is given in <i><a href="/docs/linux/man/7-dh-autoreconf/">dh-autoreconf</a></i>(7).</p>
<h2>FILES</h2>
<dl>
<dt>debian/autoreconf</p>
<dd> This file can contain a list of directories. If present, dh_autoreconf will only scan the given directories for changes. If no special command is given to dh_autoreconf, it will also forward the directory list to autoreconf which causes it to be run only on those sub directories.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-X</code><i>item</i> <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain &#8220;item&#8221; anywhere in their filename from being checked for changes. This means that those files won&#8217;t be deleted by <tt>&quot;dh_autoreconf_clean&quot;</tt> even if there are changes. You may use this option multiple times to build up a list of things to exclude. </p>
<p> Starting with version 3, the directories of common version control systems such as cvs, git, hg, svn, and bzr are excluded automatically.</p>
<dt><code>&#8211;mode=</code><i>mode</i></p>
<dd> Change the way in which modifications to files are detected. The default mode is <i>md5</i> for using <font SIZE="-1">MD5</font> checksums, but there is also <i>timesize</i> for using the time of the last modification and the file size.</p>
<dt><code>&#8211;as-needed</code></p>
<dd> Enable support for -Wl,&#8211;as-needed in all ltmain.sh files identical to the one of the libtool package. This only works in the <font SIZE="-1">MD5</font> mode (the default one). The changes are reverted in dh_autoreconf_clean. You should not prevent <font SIZE="-1">LIBTOOLIZE</font> from running with this, as it only works correctly with libtoolize running.</p>
<dt><code>-D</code><i>dir</i> <code>&#8211;sourcedirectory</code>=<i>dir</i></p>
<dd> Run everything in the source directory. Supported only in debhelper compat level 10 for backwards compatibility.</p>
<dt><i>program</i> <code>&#8212;</code> <i>params</i></p>
<dd> Run the program given by <i>program</i> with the arguments given by <i>params</i> instead of autoreconf -f -i. If you need to run multiple commands, put them in a script and pass the script instead (or add a target to debian/rules).</dl>
<h2>ENVIRONMENT</h2>
<p> For each tool executed by <i><a href="/docs/linux/man/1-autoreconf/">autoreconf</a></i>(1), one can export a variable with the uppercase name of the tool to the specific program which shall be run, including <code>true</code> to prevent the tool in question from being run. The following example shows the beginning of a debian/rules for a package where automake 1.11 shall be run instead of the default automake version and libtoolize shall not be run: </p>
<pre>
    #!/usr/bin/make -f
    export AUTOMAKE = automake-1.11
    export LIBTOOLIZE = true
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7), <i><a href="/docs/linux/man/1-dh_autoreconf_clean/">dh_autoreconf_clean</a></i>(1), <i><a href="/docs/linux/man/7-dh-autoreconf/">dh-autoreconf</a></i>(7)</p>
<h2>AUTHOR</h2>
<p> Julian Andres Klode &lt;jak [at] debian.org&gt; </p>
<h2>Index</h2>
