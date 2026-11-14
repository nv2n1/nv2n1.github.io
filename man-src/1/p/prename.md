---
title: "prename(1)"
name: "prename"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prename/"
description: "rename – renames multiple files"
---

<h2 class="name">NAME</h2>
<p> rename &#8211; renames multiple files </p>
<h2>SYNOPSIS</h2>
<p> <code>rename</code> [&nbsp;<wbr><code>-v</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-n</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-f</code>&nbsp;<wbr>] <i>perlexpr</i> [&nbsp;<wbr><i>files</i>&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;rename&quot;</tt> renames the filenames supplied according to the rule specified as the first argument. The <i>perlexpr</i> argument is a Perl expression which is expected to modify the <tt>$_</tt> string in Perl for at least some of the filenames specified. If a given filename is not modified by the expression, it will not be renamed. If no filenames are given on the command line, filenames will be read via standard input. </p>
<p> For example, to rename all files matching <tt>&quot;*.bak&quot;</tt> to strip the extension, you might say </p>
<pre>
        rename 's/\.bak$//' *.bak
</pre>
<p> To translate uppercase names to lower, you&#8217;d use </p>
<pre>
        rename 'y/A-Z/a-z/' *
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose: print names of files successfully renamed.</p>
<dt><code>-n</code>, <code>&#8211;no-act</code></p>
<dd> No Action: show what files would have been renamed.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Force: overwrite existing files.</dl>
<h2>ENVIRONMENT</h2>
<p> No environment variables are used.</p>
<h2>AUTHOR</h2>
<p> Larry Wall</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mv/">mv</a></i>(1), <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1)</p>
<h2>DIAGNOSTICS</h2>
<p> If you give an invalid Perl expression you&#8217;ll get a syntax error.</p>
<h2>BUGS</h2>
<p> The original <tt>&quot;rename&quot;</tt> did not check for the existence of target filenames, so had to be used with care. I hope I&#8217;ve fixed that (Robin Barker). </p>
<h2>Index</h2>
