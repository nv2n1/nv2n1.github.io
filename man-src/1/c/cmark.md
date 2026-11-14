---
title: "cmark(1)"
name: "cmark"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmark/"
description: "cmark – convert CommonMark formatted text to HTML"
---

<h2>NAME</h2>
<p> <code>cmark</code> &#8211; convert CommonMark formatted text to HTML</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cmark</code> [options]</p>
<dd>file*</dl>
<h2>DESCRIPTION</h2>
<p> <code>cmark</code> converts Markdown formatted plain text to either HTML, groff man, CommonMark XML, LaTeX, or CommonMark, using the conventions described in the CommonMark spec. It reads input from <i>stdin</i> or the specified files (concatenating their contents) and writes output to <i>stdout</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;to, -t </code>FORMAT</p>
<dd> Specify output format (html, man, xml, latex, commonmark).</p>
<dt><code>&#8211;width </code>WIDTH</p>
<dd> Specify a column width to which to wrap the output. For no wrapping, use the value 0 (the default). This option currently only affects the commonmark renderer.</p>
<dt><code>&#8211;sourcepos</code></p>
<dd> Include source position attribute.</p>
<dt><code>&#8211;hardbreaks</code></p>
<dd> Treat newlines as hard line breaks. If this option is specified, hard wrapping is disabled, regardless of the value given with &#8211;width.</p>
<dt><code>&#8211;normalize</code></p>
<dd> Consolidate adjacent text nodes.</p>
<dt><code>&#8211;validate-utf8</code></p>
<dd> Validate UTF-8, replacing illegal sequences with U+FFFD.</p>
<dt><code>&#8211;smart</code></p>
<dd> Use smart punctuation. Straight double and single quotes will be rendered as curly quotes, depending on their position. &#8212; will be rendered as an en-dash. &#8212; will be rendered as an em-dash. &#8230; will be rendered as ellipses.</p>
<dt><code>&#8211;safe</code></p>
<dd> Do not render raw HTML or potentially dangerous URLs. (Raw HTML is replaced by a placeholder comment; potentially dangerous URLs are replaced by empty strings.) Dangerous URLs are those that begin with `javascript:`, `vbscript:`, `file:`, or `data:` (except for `image/png`, `image/gif`, `image/jpeg`, or `image/webp` mime types).</p>
<dt><code>&#8211;help</code></p>
<dd> Print usage information.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version.</dl>
<h2>AUTHORS</h2>
<p> John MacFarlane, Vicent Marti, Kārlis Gaņģis, Nick Wellnhofer.</p>
<h2>SEE ALSO</h2>
<p> CommonMark spec: <a rel="nofollow" href="http://spec.commonmark.org.">http://spec.commonmark.org.</a> </p>
<h2>Index</h2>
