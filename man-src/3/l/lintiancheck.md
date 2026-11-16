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
<dt>processable</dt>
<dd>Get processable underlying this check.</dd>
<dt>group</dt>
<dd>Get group that the processable is in.</dd>
<dt>run</dt>
<dd>Run the check.</dd>
<dt>package</dt>
<dd>Get package name from processable.</dd>
<dt>type</dt>
<dd>Get type of processable.</dd>
<dt>info</dt>
<dd>Get the info data structure from processable.</dd>
<dt>build_path</dt>
<dd>Get the build path.</dd>
<dt>tag</dt>
<dd>Tag the processable associated with this check</dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
