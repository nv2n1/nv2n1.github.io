---
title: "fastrm(1)"
name: "fastrm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fastrm/"
description: "fastrm – Quickly remove a list of files"
---

<h2 class="name">NAME</h2>
<p> fastrm &#8211; Quickly remove a list of files </p>
<h2>SYNOPSIS</h2>
<p> <code>fastrm</code> [<code>-de</code>] [<code>-c</code>|<code>-c</code><i>I</i>] [<code>-s</code>|<code>-s</code><i>M</i>] [<code>-u</code>|<code>-u</code><i>N</i>] <i>base-directory</i></p>
<h2>DESCRIPTION</h2>
<p> <code>fastrm</code> reads a list of either file names or storage <font SIZE="-1">API</font> tokens, one per line, from its standard input and removes them. Storage <font SIZE="-1">API</font> tokens are removed via the <i>SMcancel()</i> interface. <code>fastrm</code> does not delete files safely or with an eye to security, but rather cuts every corner it can to delete files as fast as it can. It should therefore never be run on publically writable directories, or in any other environment where a hostile party may control the directory structure in which it is working. </p>
<p> If a file name is not an absolute path name, it is considered to be relative to <i>base-directory</i> as given on the command line. The <i>base-directory</i> parameter must be a simple absolute pathname (it must not contain multiple consecutive slashes or references to the special directories <tt>&quot;.&quot;</tt> or <tt>&quot;..&quot;</tt>). </p>
<p> <code>fastrm</code> is designed to be faster than the typical <tt>&quot;| xargs rm&quot;</tt> pipeline when given a sorted list of file names as input. For example, <code>fastrm</code> will usually <i><a href="/docs/linux/man/2-chdir/">chdir</a></i>(2) into a directory before removing files from it, meaning that if its input is sorted, most names passed to <i><a href="/docs/linux/man/2-unlink/">unlink</a></i>(2) will be simple names. This can substantially reduce the operating system overhead from directory lookups. </p>
<p> <code>fastrm</code> assumes that its input is valid and that it is safe to call <i><a href="/docs/linux/man/2-unlink/">unlink</a></i>(2) on every file name it is given. As a safety measure, however, <code>fastrm</code> when running as root will check with <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) that a file name doesn&#8217;t specify a directory before removing it. (In some operating systems, root is allowed to unlink directories, even directories which aren&#8217;t empty, which can cause file system corruption.) </p>
<p> The input to <code>fastrm</code> should always be sorted &#8212; or even better be in the order file names are output by <i><a href="/docs/linux/man/1-find/">find</a></i>(1)&nbsp;<wbr>&#8212; if speed is an issue and the input isn&#8217;t solely storage <font SIZE="-1">API</font> tokens. (It deals fine with unsorted input, but is unlikely to be any faster in that case than a simple <tt>&quot;| xargs rm&quot;</tt> command.) Sorting may even slightly speed up the removal of storage <font SIZE="-1">API</font> tokens due to caching effects, since sorting will tend to keep all of the tokens from a particular storage method together. </p>
<p> Various additional optimizations for removing files can be turned on and/or tuned with options (see below). Which options will be most effective depends heavily on the underlying structure of the file system, the way in which directories are stored and searched, and similar, often underdocumented, operating system implementation details. The more sophisticated the underlying operating system and file system, the more likely that it will already perform the equivalent of these optimizations internally.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>[<i>I</i>]</p>
<dd> Controls when <code>fastrm</code> calls <i><a href="/docs/linux/man/2-chdir/">chdir</a></i>(2). If the number of files to be unlinked from a given directory is at least <i>I</i>, then <code>fastrm</code> will change to that directory before unlinking those files. Otherwise, it will use either the absolute path names or a path name relative to the current directory (whichever is likely more efficient). The <i>I</i> parameter is optional; if just <code>-c</code> is given, <code>-c1</code> is assumed, which will cause <code>fastrm</code> to always chdir before calling <i><a href="/docs/linux/man/2-unlink/">unlink</a></i>(2). The default is <code>-c3</code>. Use <code>-c0</code> to prevent <code>fastrm</code> from ever using <i><a href="/docs/linux/man/2-chdir/">chdir</a></i>(2).</p>
<dt><code>-d</code></p>
<dd> Don&#8217;t remove any files. Instead, print a list of the files that would be removed to standard output. Each line contains either the current directory of <code>fastrm</code> at the time it would do the unlink and the relative path name it would pass to <i><a href="/docs/linux/man/2-unlink/">unlink</a></i>(2) as two fields separated by whitespace and a <tt>&quot;/&quot;</tt>, the absolute path name (as a single field) that would be passed to <i><a href="/docs/linux/man/2-unlink/">unlink</a></i>(2), or the string <tt>&quot;Token&quot;</tt> and the storage <font SIZE="-1">API</font> token that would be removed.</p>
<dt><code>-e</code></p>
<dd> Treat an empty input file as an error. This is most useful when <code>fastrm</code> is last in a pipeline after a preceding <i><a href="/docs/linux/man/1-sort/">sort</a></i>(1) command, ensuring that <code>fastrm</code> will fail if the sort fails.</p>
<dt><code>-s</code>[<i>M</i>]</p>
<dd> When <code>-s</code> is given and the number of files to remove in a directory is greater than <i>M</i>, rather than remove files in the order given, <code>fastrm</code> will open the directory and read it, unlinking files in the order that they appear in the directory. On systems with a per-process directory cache or that use a linear search to find files in a directory, this should make directory lookups faster. The <i>M</i> parameter is optional; if just <code>-s</code> is given, <code>-s5</code> is assumed. </p>
<p> When this option is in effect, <code>fastrm</code> won&#8217;t attempt to remove files that it doesn&#8217;t see in the directory, possibly significantly speeding it up if most of the files to be removed have already been deleted. However, using this option requires <code>fastrm</code> to do more internal work and it also assumes that the order of directory listings is stable in the presence of calls to <i><a href="/docs/linux/man/2-unlink/">unlink</a></i>(2) between calls to <i><a href="/docs/linux/man/3-readdir/">readdir</a></i>(3). This may be a dangerous assumption with some sophisticated file systems (and in general this option is only useful with file systems that use unindexed linear searches to find files in directories or when most of the files to be removed have already been deleted). </p>
<p> This optimization is off by default.</p>
<dt><code>-u</code>[<i>N</i>]</p>
<dd> Specifying this option promises that there are no symbolic links in the directory tree from which files are being removed. This allows <code>fastrm</code> to make an additional optimization to its calls to <i><a href="/docs/linux/man/2-chdir/">chdir</a></i>(2), constructing a relative path using <tt>&quot;../..&quot;</tt> and the like to pass to <i><a href="/docs/linux/man/2-chdir/">chdir</a></i>(2) rather than always using absolute paths. Since this reduces the number of directory lookups needed with deeply nested directory structures (such as that typically created by traditional news spool storage), it can be a significant optimization, but it breaks horribly in the presence of symbolic links to directories. </p>
<p> When <code>-u</code> is given, <code>fastrm</code> will use at most <i>N</i> levels of <tt>&quot;..&quot;</tt> segments to construct paths. <i>N</i> is optional; if just <code>-u</code> is given, <code>-u1</code> is assumed. </p>
<p> This optimization is off by default.</dl>
<p> <code>fastrm</code> also accepts <code>-a</code> and <code>-r</code> options, which do nothing at all except allow you to say <tt>&quot;fastrm -usa&quot;</tt>, <tt>&quot;fastrm -usr&quot;</tt>, or <tt>&quot;fastrm -user&quot;</tt>. These happen to often be convenient sets of options to use.</p>
<h2>EXIT STATUS</h2>
<p> <code>fastrm</code> exits with a status of zero if there were no problems, and an exit status of 1 if something went wrong. Attempting to remove a file that does not exist is not considered a problem.</p>
<h2>EXAMPLES</h2>
<p> <code>fastrm</code> is typically invoked by <font SIZE="-1">INN</font> via <i><a href="/docs/linux/man/8-expirerm/">expirerm</a></i>(8) using a command like: </p>
<pre>
    fastrm -e &lt;patharticles in inn.conf&gt; &lt; expire.list
</pre>
<p> To enable all optimizations and see the affect on the order of removal caused by <code>-s</code>, use: </p>
<pre>
    fastrm -d -s -e -u &lt;patharticles&gt; &lt; expire.list
</pre>
<p> If your file system has indexed directory lookups, but you have a deeply nested directory structure, you may want to use a set of flags like: </p>
<pre>
    fastrm -e -u3 &lt;patharticles&gt; &lt; expire.list
</pre>
<p> to strongly prefer relative paths but not to use <i><a href="/docs/linux/man/2-readdir/">readdir</a></i>(2) to order the calls to <i><a href="/docs/linux/man/2-unlink/">unlink</a></i>(2). </p>
<p> You may want to edit <i><a href="/docs/linux/man/8-expirerm/">expirerm</a></i>(8) to change the flags passed to <code>fastrm</code>.</p>
<h2>WARNINGS</h2>
<p> <code>fastrm</code> cuts corners and does not worry about security, so it does not use <i><a href="/docs/linux/man/2-chdir/">chdir</a></i>(2) safely and could be tricked into removing files other than those that were intended if run on a specially constructed file tree or a file tree that is being modified while it is running. It should therefore never be used with world-writable directories or any other directory that might be controlled or modified by an attacker.</p>
<h2>NOTES</h2>
<p> <code>fastrm</code> defers opening the storage subsystem or attempting to parse any <font SIZE="-1">INN</font> configuration files until it encounters a token in the list of files to remove. It&#8217;s therefore possible to use <code>fastrm</code> outside of <font SIZE="-1">INN</font> as a general fast file removal program.</p>
<h2>HISTORY</h2>
<p> <code>fastrm</code> was originally written by &lt;kre [at] munnari.oz.au&gt;. This manual page was rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> fastrm.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-expirerm/">expirerm</a></i>(8). </p>
<h2>Index</h2>
