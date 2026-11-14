---
title: "ptargrep(1)"
name: "ptargrep"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ptargrep/"
description: "ptargrep – Apply pattern matching to the contents of files in a tar archive"
---

<h2 class="name">NAME</h2>
<p> ptargrep &#8211; Apply pattern matching to the contents of files in a tar archive </p>
<h2>SYNOPSIS</h2>
<pre><code>
ptargrep[options]&lt;pattern&gt;&lt;tar file&gt;... Options : --basename | -b ignore directory paths from archive-- ignore - case | -i do case -insensitive pattern matching-- list - only | -l list matching filenames rather than extracting matches-- verbose | -v write debugging message to STDERR-- help | -? detailed help message
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility allows you to apply pattern matching to <code>the contents</code> of files contained in a tar archive. You might use this to identify all files in an archive which contain lines matching the specified pattern and either print out the pathnames or extract the files. </p>
<p> The pattern will be used as a Perl regular expression (as opposed to a simple grep regex). </p>
<p> Multiple tar archive filenames can be specified &#8211; they will each be processed in turn.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;basename</code> (alias -b)</p>
<dd> When matching files are extracted, ignore the directory path from the archive and write to the current directory using the basename of the file from the archive. Beware: if two matching files in the archive have the same basename, the second file extracted will overwrite the first.</p>
<dt><code>&#8211;ignore-case</code> (alias -i)</p>
<dd> Make pattern matching case-insensitive.</p>
<dt><code>&#8211;list-only</code> (alias -l)</p>
<dd> Print the pathname of each matching file from the archive to <font SIZE="-1">STDOUT.</font> Without this option, the default behaviour is to extract each matching file.</p>
<dt><code>&#8211;verbose</code> (alias -v)</p>
<dd> Log debugging info to <font SIZE="-1">STDERR.</font></p>
<dt><code>&#8211;help</code> (alias -?)</p>
<dd> Display this documentation.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright 2010 Grant McLean &lt;grantm [at] cpan.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<h2>Index</h2>
