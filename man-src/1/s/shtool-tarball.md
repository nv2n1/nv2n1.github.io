---
title: "shtool-tarball(1)"
name: "shtool-tarball"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-tarball/"
description: "shtool tarball – GNU shtool command for rolling standardized tarballs"
---

<h2 class="name">NAME</h2>
<p> shtool tarball &#8211; GNU shtool command for rolling standardized tarballs </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool tarball</code> [<code>-t</code>|<code>&#8211;trace</code>] [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-o</code>|<code>&#8211;output</code> <i>tarball</i>] [<code>-c</code>|<code>&#8211;compress</code> <i>prog</i>] [<code>-d</code>|<code>&#8211;directory</code> <i>directory</i>] [<code>-u</code>|<code>&#8211;user</code> <i>user</i>] [<code>-g</code>|<code>&#8211;group</code> <i>group</i>] [<code>-e</code>|<code>&#8211;exclude</code> <i>pattern</i>] <i>path</i> [<i>path</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This command is for rolling input files under <i>path</i> into a distribution tarballs which can be extracted by <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1). </p>
<p> The four important aspects of good open source software tarballs are: (1) unpack into a single top-level directory, (2) top-level directory corresponds to the tarball filename, (3) tarball files should be sorted and (4) arbitrary names for file owner and group.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display some processing information.</p>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Enable the output of the essential shell commands which are executed.</p>
<dt><code>-o</code>, <code>&#8211;output</code> <i>tarball</i></p>
<dd> Output tarball to file <i>tarball</i>.</p>
<dt><code>-c</code>, <code>&#8211;compress</code> <i>prog</i></p>
<dd> Pipe resulting tarball through compression program <i>prog</i>.</p>
<dt><code>-d</code>, <code>&#8211;directory</code> <i>directory</i></p>
<dd> Sets the top-level directory into which the tarball unpacks. By default it is <i>tarball</i> without the trailing <tt>&quot;.tar.*&quot;</tt> extension.</p>
<dt><code>-u</code>, <code>&#8211;user</code> <i>user</i></p>
<dd> The user (owner) of files and directories in the tarball to <i>user</i>.</p>
<dt><code>-g</code>, <code>&#8211;group</code> <i>group</i></p>
<dd> The group of files and directories in the tarball to <i>group</i>.</p>
<dt><code>-e</code>, <code>&#8211;exclude</code> <i>pattern</i></p>
<dd> Exclude files and directories matching comma-separated list of regex <i>pattern</i> from the tarball. Directories are expanded before the filtering takes place. The default filter pattern is &quot;<tt>&quot;CVS,\.cvsignore,\.svn,\.[oa]\$&quot;</tt>&quot;.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   Makefile.in
 dist:
     ...
     V=`shtool version -d short ...`; \
     shtool tarball -o foobar-$$V.tar.gz -c 'gzip -9' \
                    -u bar -g gnu -e 'CVS,\.cvsignore' .
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>tarball</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1999 for <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1), <i><a href="/docs/linux/man/1-compress/">compress</a></i>(1). </p>
<h2>Index</h2>
