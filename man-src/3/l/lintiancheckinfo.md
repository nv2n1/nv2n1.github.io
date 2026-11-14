---
title: "lintiancheckinfo(3)"
name: "lintiancheckinfo"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancheckinfo/"
description: "Lintian::Check::Info – Check script meta data"
---

<p>Lintian::Check::Info &#8211; Check script meta data </p>
<h2>Synopsis</h2>
<pre> use Lintian::Check::Info;</pre>
<h2>Description</h2>
<p>This class represents Lintian checks.</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>&quot;basedir&quot;</p>
<dd>
<dt>name</p>
<dd>
<dt>module</p>
<dd>
<dt>type</p>
<dd>
<dt>type_table</p>
<dd>
<dt>tag_table</p>
<dd>
<dt>load</p>
<dd>
<dt>$cs-&gt;is_check_type ($type)</p>
<dd>Returns a truth value if this check can be applied to a <tt>$type</tt> package. </p>
<p> Note if <tt>$cs</tt>-&gt;type return undef, this will return a truth value for all inputs.</p>
<dt>$cs-&gt;add_taginfo ($taginfo)</p>
<dd>Associates a tag as issued by this check.</p>
<dt>$cs-&gt;get_tag ($tagname)</p>
<dd>Return the tag or undef (if the tag is not in this check).</p>
<dt>$cs-&gt;tags</p>
<dd>Returns the list of tag names in the check. The list nor its contents should be modified.</p>
<dt>$cs-&gt;run_check ($proc, $group)</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
