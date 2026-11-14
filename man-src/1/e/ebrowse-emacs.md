---
title: "ebrowse-emacs(1)"
name: "ebrowse-emacs"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ebrowse-emacs/"
description: "ebrowse – create a class hierarchy database"
---

<p>ebrowse &#8211; create a class hierarchy database </p>
<h2>Synopsis</h2>
<p><code>ebrowse</code> [<i>options</i>] [<i>FILES</i>&#8230;]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>ebrowse</code> command. Full documentation is available in the GNU Info format. </p>
<p> <code>ebrowse</code> is used to create the database used by the class browser in Emacs. </p>
<h2>Options</h2>
<p>The program follows the usual GNU command line syntax, with long options starting with two dashes (&quot;-&quot;).</p>
<dl>
<dt><code>-a, &#8211;append</code></p>
<dd>append output to existing file</p>
<dt><code>-f, &#8211;files=FILES</code></p>
<dd>read input file names from <i>FILE</i></p>
<dt><code>-I, &#8211;search-path=LIST</code></p>
<dd>set search path for input files</p>
<dt><code>-m, &#8211;min-regexp-length=N</code></p>
<dd>set minimum regexp length to <i>N</i></p>
<dt><code>-M, &#8211;max-regexp-length=N</code></p>
<dd>set maximum regexp length to <i>N</i></p>
<dt><code>-n, &#8211;no-nested-classes</code></p>
<dd>exclude nested classes</p>
<dt><code>-o, &#8211;output-file=FILE</code></p>
<dd>set output file name to <i>FILE</i></p>
<dt><code>-p, &#8211;position-info</code></p>
<dd>print info about position in file</p>
<dt><code>-s, &#8211;no-structs-or-unions</code></p>
<dd>don&#8217;t record structs or unions</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>be verbose</p>
<dt><code>-V, &#8211;very-verbose</code></p>
<dd>be very verbose</p>
<dt><code>-x, &#8211;no-regexps</code></p>
<dd>don&#8217;t record regular expressions</p>
<dt><code>&#8211;help</code></p>
<dd>display this help</p>
<dt><code>&#8211;version</code></p>
<dd>display version info</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1), <code><a href="/docs/linux/man/1-etags/">etags</a></code>(1), and the full documentation for <code>ebrowse</code> which is maintained as a Texinfo manual. If the <code>info</code> and <code>ebrowse</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info ebrowse</code></dl>
<p> should give you access to the complete manual.</p>
<h2>Author</h2>
<p><i>Ebrowse</i> was written by Gerd Moellmann.</p>
<h2>Copying</h2>
<p>Copyright 2008-2019 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this document provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this document under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this document into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Free Software Foundation.</p>
