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
<dt>&quot;basedir&quot;</dt>
<dd>
</dd><dt>name</dt>
<dd>
</dd><dt>module</dt>
<dd>
</dd><dt>type</dt>
<dd>
</dd><dt>type_table</dt>
<dd>
</dd><dt>tag_table</dt>
<dd>
</dd><dt>load</dt>
<dd>
</dd><dt>$cs-&gt;is_check_type ($type)</dt>
<dd>Returns a truth value if this check can be applied to a <tt>$type</tt> package. </dd>
<p> Note if <tt>$cs</tt>-&gt;type return undef, this will return a truth value for all inputs.</p>
<dt>$cs-&gt;add_taginfo ($taginfo)</dt>
<dd>Associates a tag as issued by this check.</dd>
<dt>$cs-&gt;get_tag ($tagname)</dt>
<dd>Return the tag or undef (if the tag is not in this check).</dd>
<dt>$cs-&gt;tags</dt>
<dd>Returns the list of tag names in the check. The list nor its contents should be modified.</dd>
<dt>$cs-&gt;run_check ($proc, $group)</dt>
<dd></dd></dl>
<h2>Author</h2>
<p>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
