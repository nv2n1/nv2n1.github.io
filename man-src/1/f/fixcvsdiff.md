---
title: "fixcvsdiff(1)"
name: "fixcvsdiff"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fixcvsdiff/"
description: "fixcvsdiff – fix problematic diff files"
---

<h2 class="name">NAME</h2>
<p> fixcvsdiff &#8211; fix problematic diff files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fixcvsdiff</code> [-p] [-b] [<i>file</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>fixcvsdiff modifies diff files created from the <code>cvs diff</code> command, where files have been added or removed. CVS tends to create diff files that <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1) mis-interprets. The diff file must retain the lines beginning with &#8220;Index:&#8221; in order for the correction to work.</p>
<h2>OPTIONS</h2>
<p> <code>-b</code></p>
<dl>
<dt>
<dd> Keep a .bak backup file.</dl>
<p> <code>-p</code></p>
<dl>
<dt>
<dd> Print out the <code>cvs add</code> and <code>cvs remove</code> commands that must be made after applying the diff, but before running <code>cvs commit</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1), <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1), <code><a href="/docs/linux/man/1-cvs/">cvs</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<p> <code>Amir Karger</code> &lt;karger [at] post.harvard.edu&gt;</p>
<dl>
<dt>
<dd> Author of the original perl script and man page</dl>
<p> <code>John Levon</code> &lt;moz [at] compsoc.man.ac.uk&gt;</p>
<dl>
<dt>
<dd> Author of the original perl script and man page</dl>
<h2>Index</h2>
