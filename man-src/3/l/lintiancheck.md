---
title: "lintiancheck(3)"
name: "lintiancheck"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancheck/"
description: "Lintian::Check — Common facilities for Lintian checks"
---

<p>Lintian::Check &#8212; Common facilities for Lintian checks </p>
<h2>Synopsis</h2>
<pre> use Moo;
 use namespace::clean;
 with('Lintian::Check');</pre>
<h2>Description</h2>
<p>A class for collecting Lintian tags as they are issued</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>processable</p>
<dd>Get processable underlying this check.</p>
<dt>group</p>
<dd>Get group that the processable is in.</p>
<dt>run</p>
<dd>Run the check.</p>
<dt>package</p>
<dd>Get package name from processable.</p>
<dt>type</p>
<dd>Get type of processable.</p>
<dt>info</p>
<dd>Get the info data structure from processable.</p>
<dt>build_path</p>
<dd>Get the build path.</p>
<dt>tag</p>
<dd>Tag the processable associated with this check</dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
