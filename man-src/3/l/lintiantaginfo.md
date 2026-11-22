---
title: "lintiantaginfo(3)"
name: "lintiantaginfo"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiantaginfo/"
description: "Lintian::Tag::Info – Lintian interface to tag metadata"
---

<p>Lintian::Tag::Info &#8211; Lintian interface to tag metadata </p>
<h2>Synopsis</h2>
<pre> my $taginfo = Lintian::Tag::Info-&gt;new;</pre>
<h2>Description</h2>
<p>This module provides an interface to tag metadata as gleaned from the *.desc files describing the checks. It can be used to retrieve specific metadata elements or to format the tag description.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>tag</dt>
<dd>
</dd><dt>original_severity</dt>
<dd>
</dd><dt>effective_severity</dt>
<dd>
</dd><dt>check</dt>
<dd>
</dd><dt>check_type</dt>
<dd>
</dd><dt>experimental</dt>
<dd>
</dd><dt>info</dt>
<dd>
</dd><dt>references</dt>
<dd>
</dd><dt>aliases</dt>
<dd>
</dd><dt>load(PATH)</dt>
<dd>Loads a tag description from PATH.</dd>
<dt><code>code()</code></dt>
<dd>Returns the one-letter code for the tag. This will be a letter chosen from <tt>&quot;E&quot;</tt>, <tt>&quot;W&quot;</tt>, <tt>&quot;I&quot;</tt>, or <tt>&quot;P&quot;</tt>, based on the tag severity, and other attributes (such as whether experimental is set). This code will never be <tt>&quot;O&quot;</tt> or <tt>&quot;X&quot;</tt>; overrides and experimental tags are handled separately.</dd>
<dt>description([FORMAT [, INDENT]])</dt>
<dd>Returns the formatted description (the Info field) for a tag. FORMAT must be either <tt>&quot;text&quot;</tt> or <tt>&quot;html&quot;</tt> and defaults to <tt>&quot;text&quot;</tt> if no format is specified. If <tt>&quot;text&quot;</tt>, returns wrapped paragraphs formatted in plain text with a right margin matching the Text::Wrap default, preserving as verbatim paragraphs that begin with whitespace. If <tt>&quot;html&quot;</tt>, return paragraphs formatted in HTML. </dd>
<p> If INDENT is specified, the string INDENT is prepended to each line of the formatted output.</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
</p>