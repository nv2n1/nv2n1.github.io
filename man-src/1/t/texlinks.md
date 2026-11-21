---
title: "texlinks(1)"
name: "texlinks"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texlinks/"
description: "texlinks – maintain symbolic links from format to engine"
---

<h2>NAME</h2>
<p> texlinks &#8211; maintain symbolic links from format to engine </p>
<h2>SYNOPSIS</h2>
<p> <code>texlinks</code> [ <i>OPTIONS</i>&#8230; ] <i>DIRECTORIES</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>texlinks</code> is used to create or recreate symbolic links from formats to engines according to the information in <i>fmtutil.cnf</i> or a file specified with <code>&#8211;cnffile</code>. </p>
<p> <i>DIRECTORIES</i> is an optional list of directories in which to operate. If no directories are specified the list of directories depends on the <code>&#8211;multiplatform</code> option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cnffile</code> <i>FILE</i> or <code>-f</code> <i>FILE</i></dt>
<dd> use file as configuration file (default: <i>fmtutil.cnf</i>)</dd>
<dt><code>&#8211;help</code> or <code>-h</code></dt>
<dd> show some help text</dd>
<dt><code>&#8211;multiplatform</code> or <code>-m</code></dt>
<dd> operate in all platform-specific directories (default: operate only in the directory for this platform)</dd>
<dt><code>&#8211;silent</code> or <code>-s</code></dt>
<dd> silently skip over existing scripts/binaries instead of printing a warning</dd>
<dt><code>&#8211;unlink</code> or <code>-u</code></dt>
<dd> Unlink previously created symlinks</dd>
<dt><code>&#8211;verbose</code> or <code>-v</code></dt>
<dd> +set verbose mode on (default: off)</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>fmtutil.cnf</i></dt>
<dd> default configuration file</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fmtutil/">fmtutil</a></code>(1), <code><a href="/docs/linux/man/5-fmtutil-cnf/">fmtutil.cnf</a></code>(5) </p>
<p> Web page: &lt;<a rel="nofollow" href="http://tug.org/teTeX/">http://tug.org/teTeX/</a>&gt; </p>
<h2>BUGS</h2>
<p> None known, but report any bugs found to &lt;tex-k [at] tug.org&gt; (mailing list). </p>
<h2>AUTHOR</h2>
<p> <code>texlinks</code> was written by Thomas Esser &lt;te [at] dbs.uni-hannover.de&gt; in 1999. <code>texlinks</code> has been released into the public domain. </p>
<p> This manual page was written by C.M. Connelly &lt;c@eskimo.com&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
