---
title: "whereis(1)"
name: "whereis"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whereis/"
description: "whereis – locate the binary, source, and manual page files for a command"
---

<h2 class="name">NAME</h2>
<p> whereis &#8211; locate the binary, source, and manual page files for a command </p>
<h2>SYNOPSIS</h2>
<p> <code>whereis</code> [options] [<code>-BMS</code> <i>directory</i>&#8230; <code>-f</code>] <i>name</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>whereis</code> locates the binary, source and manual files for the specified command names. The supplied names are first stripped of leading pathname components. Prefixes of <code>s.</code> resulting from use of source code control are also dealt with. <code>whereis</code> then attempts to locate the desired program in the standard Linux places, and in the places specified by <code>$PATH</code> and <code>$MANPATH</code>. </p>
<p> The search restrictions (options <code>-b</code>, <code>-m</code> and <code>-s</code>) are cumulative and apply to the subsequent <i>name</i> patterns on the command line. Any new search restriction resets the search mask. For example,</p>
<dl>
<dt>
<dd>
<p> <code>whereis -bm ls tr -m gcc</code>
</dl>
<p> searches for &quot;ls&quot; and &quot;tr&quot; binaries and man pages, and for &quot;gcc&quot; man pages only. </p>
<p> The options <code>-B</code>, <code>-M</code> and <code>-S</code> reset search paths for the subsequent <i>name</i> patterns. For example,</p>
<dl>
<dt>
<dd>
<p> <code>whereis -m ls -M /usr/share/man/man1 -f cal</code>
</dl>
<p> searches for &quot;<code>ls</code>&quot; man pages in all default paths, but for &quot;cal&quot; in the <i>/usr/share/man/man1</i> directory only.</p>
<h2>OPTIONS</h2>
<p> <code>-b</code></p>
<dl>
<dt>
<dd> Search for binaries.</dl>
<p> <code>-m</code></p>
<dl>
<dt>
<dd> Search for manuals.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Search for sources.</dl>
<p> <code>-u</code></p>
<dl>
<dt>
<dd> Only show the command names that have unusual entries. A command is said to be unusual if it does not have just one entry of each explicitly requested type. Thus &#8216;<code>whereis -m -u *</code>&#8216; asks for those files in the current directory which have no documentation file, or more than one.</dl>
<p> <code>-B</code> <i>list</i></p>
<dl>
<dt>
<dd> Limit the places where <code>whereis</code> searches for binaries, by a whitespace-separated list of directories.</dl>
<p> <code>-M</code> <i>list</i></p>
<dl>
<dt>
<dd> Limit the places where <code>whereis</code> searches for manuals and documentation in Info format, by a whitespace-separated list of directories.</dl>
<p> <code>-S</code> <i>list</i></p>
<dl>
<dt>
<dd> Limit the places where <code>whereis</code> searches for sources, by a whitespace-separated list of directories.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Terminates the directory list and signals the start of filenames. It <i>must</i> be used when any of the <code>-B</code>, <code>-M</code>, or <code>-S</code> options is used.</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> Output the list of effective lookup paths that <code>whereis</code> is using. When none of <code>-B</code>, <code>-M</code>, or <code>-S</code> is specified, the option will output the hard-coded paths that the command was able to find on the system.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<h2>FILE SEARCH PATHS</h2>
<p> By default <code>whereis</code> tries to find files from hard-coded paths, which are defined with glob patterns. The command attempts to use the contents of <code>$PATH</code> and <code>$MANPATH</code> environment variables as default search path. The easiest way to know what paths are in use is to add the <code>-l</code> listing option. Effects of the <code>-B</code>, <code>-M</code>, and <code>-S</code> are displayed with <code>-l</code>.</p>
<h2>ENVIRONMENT</h2>
<p> WHEREIS_DEBUG=all</p>
<dl>
<dt>
<dd> enables debug output.</dl>
<h2>EXAMPLES</h2>
<p> To find all files in <i>/usr/bin</i> which are not documented in <i>/usr/man/man1</i> or have no source in <i>/usr/src</i>: </p>
<p> <code>cd /usr/bin</code> <code>whereis -u -ms -M /usr/man/man1 -S /usr/src -f *</code></p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>whereis</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
