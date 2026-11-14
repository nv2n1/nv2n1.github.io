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
<dt>tag</p>
<dd>
<dt>original_severity</p>
<dd>
<dt>effective_severity</p>
<dd>
<dt>check</p>
<dd>
<dt>check_type</p>
<dd>
<dt>experimental</p>
<dd>
<dt>info</p>
<dd>
<dt>references</p>
<dd>
<dt>aliases</p>
<dd>
<dt>load(<font SIZE="-1">PATH</font>)</p>
<dd>Loads a tag description from <font SIZE="-1">PATH.</font></p>
<dt><code>code()</code></p>
<dd>Returns the one-letter code for the tag. This will be a letter chosen from <tt>&quot;E&quot;</tt>, <tt>&quot;W&quot;</tt>, <tt>&quot;I&quot;</tt>, or <tt>&quot;P&quot;</tt>, based on the tag severity, and other attributes (such as whether experimental is set). This code will never be <tt>&quot;O&quot;</tt> or <tt>&quot;X&quot;</tt>; overrides and experimental tags are handled separately.</p>
<dt>description([<font SIZE="-1">FORMAT</font> [, <font SIZE="-1">INDENT</font>]])</p>
<dd>Returns the formatted description (the Info field) for a tag. <font SIZE="-1">FORMAT</font> must be either <tt>&quot;text&quot;</tt> or <tt>&quot;html&quot;</tt> and defaults to <tt>&quot;text&quot;</tt> if no format is specified. If <tt>&quot;text&quot;</tt>, returns wrapped paragraphs formatted in plain text with a right margin matching the Text::Wrap default, preserving as verbatim paragraphs that begin with whitespace. If <tt>&quot;html&quot;</tt>, return paragraphs formatted in <font SIZE="-1">HTML.</font> </p>
<p> If <font SIZE="-1">INDENT</font> is specified, the string <font SIZE="-1">INDENT</font> is prepended to each line of the formatted output.</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
