---
title: "rpmdev-diff(1)"
name: "rpmdev-diff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmdev-diff/"
description: "rpmdev-diff – manual page for rpmdev-diff version 1.4"
---

<h2>NAME</h2>
<p> rpmdev-diff &#8211; manual page for rpmdev-diff version 1.4</p>
<h2>SYNOPSIS</h2>
<p> <code>rpmdev-diff</code> [<i>OPTION</i>]&#8230; [<i>DIFF-OPTIONS</i>] <i>FROM-ARCHIVE TO-ARCHIVE</i></p>
<h2>DESCRIPTION</h2>
<p> rpmdev-diff diffs contents of two archives. </p>
<p> See <a href="/docs/linux/man/1-rpmdev-extract/">rpmdev-extract</a>(1) for information about supported archive types.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;contents</code></p>
<dd> Diff contents of files in archives. This is the default.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> Diff lists of files in archives.</p>
<dt><code>-L</code>, <code>&#8211;long-list</code></p>
<dd> Diff long lists (akin to &#8216;find <code>-ls</code>&#8216;) of files in archives.</p>
<dt><code>-m</code>, <code>&#8211;metadata</code></p>
<dd> Diff archive metadata (only implemented for rpms for now).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt>diff-options</p>
<dd> Options passed to <a href="/docs/linux/man/1-diff/">diff</a>(1). The first repeated argument of the above or the first argument starting with a &#8216;-&#8216; but not one of the above starts diff-options, the first one not starting with it ends them. Default: <code>-Nup</code> for contents (in addition to <code>-r</code> which will always be passed), <code>-U0</code> for others.</dl>
<p> More than one of <code>-c</code>, <code>-l</code>, <code>-L</code>, and <code>-m</code> may be specified.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2010 Ville Skyttä &lt;ville.skytta [at] iki.fi&gt; This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
