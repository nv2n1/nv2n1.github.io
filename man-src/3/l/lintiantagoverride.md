---
title: "lintiantagoverride(3)"
name: "lintiantagoverride"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiantagoverride/"
---

Lintian::Tag::Override -- Representation of a Lintian Override 

<h2>Synopsis</h2><pre> use Lintian::Tag::Override;
 
 my $data = {
 'comments' =&gt; ['some', 'multi-line', 'comments']
 };
 my $override = Lintian::Tag::Override-&gt;new('unused-override', $data);
 my $comments = $override-&gt;comments;
 if ($override-&gt;overrides(&quot;some extra&quot;) ) {
 # do something
 }</pre><h2>Description</h2>Represents a Lintian Override.
<h2>Methods</h2><dl COMPACT><dt>Lintian::Tag::Override-&gt;new($tag, $data)
<dd>Creates a new override for <tt>$tag</tt>. <tt>$data</tt> should be a hashref with the following fields.
<dl COMPACT><dd><dl COMPACT><dt>arch
<dd>Architectures this override applies too (not really used).
<dt>comments
<dd>A list of comments (each item is a separate line)
<dt>extra
<dd>The extra part of the override. If it contains a ``*'' is will considered a pattern.</dl></dl><dl COMPACT><dd></dl><dt>$override-&gt;tag
<dd>Returns the name of the tag.
<dt>$override-&gt;arch
<dd>Returns the architecture this tag applies to.
<dt>$override-&gt;comments
<dd>Returns a list of lines that makes up the comments for this override. 

 Do not modify the contents of this list.
<dt>$override-&gt;extra
<dd>Returns the extra of this tag (or the empty string, if there is no extra).
<dt>$override-&gt;is_pattern
<dd>Returns a truth value if the extra is a pattern.
<dt>$override-&gt;overrides($extra)
<dd>Returns a truth value if this override applies to this extra.</dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1) 

 Lintian::Tags
