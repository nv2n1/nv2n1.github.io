---
title: "rredtool(1)"
name: "rredtool"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rredtool/"
description: "rredtool – merge or apply a very restricted subset of ed patches"
---

<h2>NAME</h2>
<p> rredtool &#8211; merge or apply a very restricted subset of ed patches</p>
<h2>SYNOPSIS</h2>
<p> <code>rredtool &#8211;help</code> </p>
<p> <code>rredtool</code> [ <i>options</i> ] <code>&#8211;merge</code> <i>patches&#8230;</i> </p>
<p> <code>rredtool</code> [ <i>options</i> ] <code>&#8211;patch</code> <i>file-to-patch</i> <i>patches&#8230;</i> </p>
<p> <code>rredtool</code> <i>directory</i> <i>newfile</i> <i>oldfile</i> <i>mode</i></p>
<h2>DESCRIPTION</h2>
<p> rredtool is a tool to handle a subset of ed patches in a safe way. It is especially targeted at ed patches as used in Packages.diff and Sources.diff. Is also has a mode supposed to be called from reprepro as Index Hook to generate and update a <code>Packages.diff/Index</code> file.</p>
<h2>MODI</h2>
<p> One of the following has to be given, so that rredtool know that to do.</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the version of this tool (or rather the version of reprepro which it is coming with).</p>
<dt><code>&#8211;help</code></p>
<dd> Print a short overview of the modi.</p>
<dt><code>&#8211;patch</code></p>
<dd> The first argument of rredtool is the file to patch, the other arguments are ed patches to apply on this one.</p>
<dt><code>&#8211;merge</code></p>
<dd> The arguments are treated as ed patches, which are merged into a single one.</p>
<dt><code>&#8211;reprepro-hook</code> (or no other mode flag)</p>
<dd> Act as reprepro index hook to manage a <code>Packages.diff/index</code> file. That means it expects to get exactly 4 arguments and writes the names of files to place into filedescriptor 3. </p>
<p> If neither &#8211;patch nor &#8211;merge is given, this mode is used, so you can just put </p>
<p>&nbsp;<wbr><code>DebIndices: Packages Release . .gz&nbsp;<wbr>/usr/bin/rredtool</code> </p>
<p> into reprepro&#8217;s <code>conf/distributions</code> file to have a Packages.diff directory generated. (Note that you have to generate an uncompressed file (the single dot). You will need to have patch, gzip and gunzip available in your path.) </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> Print intermediate results or other details that might be interesting when trying to track down bugs in rredtool but not intresting otherwise.</p>
<dt><code>&#8211;max-patch-count=</code><i>count</i></p>
<dd> When generating a <i>Packages</i><code>.diff/Index</code> file, put at most <i>count</i> patches in it (not counting possible apt workaround patches).</p>
<dt><code>-o</code>|<code>&#8211;output</code></p>
<dd> Not yet implemented.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TMPDIR</code>, <code>TEMPDIR</code></p>
<dd> temporary files are created in $<i>TEMPDIR</i> if set, otherwise in $<i>TMPDIR</i> if set, otherwise in <code>/tmp/</code>.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs or wishlist requests the Debian BTS (e.g. by using <code>reportbug reperepro</code>) or directly to &lt;brlink [at] debian.org&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Bernhard R. Link<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
