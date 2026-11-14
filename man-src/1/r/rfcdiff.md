---
title: "rfcdiff(1)"
name: "rfcdiff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rfcdiff/"
description: "rfcdiff [options] file1 file2"
---

<p>rfcdiff [options] file1 file2 </p>
<p> rfcdiff takes two RFCs or Internet-Drafts in text form as input, and produces output which indicates the differences found in one of various forms, controlled by the options listed below. In all cases, page headers and page footers are stripped before looking for changes.</p>
<dl>
<dt><code>&#8211;html</code></p>
<dd> Produce side-by-side .html diff (default)</p>
<dt><code>&#8211;chbars</code></p>
<dd> Produce changebar marked .txt output</p>
<dt><code>&#8211;diff</code></p>
<dd> Produce a regular diff output</p>
<dt><code>&#8211;wdiff</code></p>
<dd> Produce paged wdiff output</p>
<dt><code>&#8211;hwdiff</code></p>
<dd> Produce html-wrapped coloured wdiff output</p>
<dt><code>&#8211;oldcolour</code> COLOURNAME</p>
<dd> Colour for new file in hwdiff (default is &quot;green&quot;)</p>
<dt><code>&#8211;oldcolor</code> COLORNAME</p>
<dd> Color for old file in hwdiff (default is &quot;red&quot;)</p>
<dt><code>&#8211;newcolour</code> COLOURNAME</p>
<dd> Colour for new file in hwdiff (default is &quot;green&quot;)</p>
<dt><code>&#8211;newcolor</code> COLORNAME</p>
<dd> Color for new file in hwdiff (default is &quot;green&quot;)</p>
<dt><code>&#8211;larger</code></p>
<dd> Make difference text in hwdiff slightly larger</p>
<dt><code>&#8211;browse</code></p>
<dd> Show html output in browser</p>
<dt><code>&#8211;keep</code></p>
<dd> Don&#8217;t delete temporary workfiles</p>
<dt><code>&#8211;version</code></p>
<dd> Show version</p>
<dt><code>&#8211;help</code></p>
<dd> Show this help</dl>
<p> <code>&#8211;info</code> &quot;Synopsis|Usage|Copyright|Description|Log&quot; Show various info</p>
<dl>
<dt><code>&#8211;width</code> N</p>
<dd> Set a maximum width of N characters for the display of each half of the old/new html diff</p>
<dt><code>&#8211;linenum</code></p>
<dd> Show linenumbers for each line, not only at the start of each change section</p>
<dt><code>&#8211;body</code></p>
<dd> Strip document preamble (title, boilerplate and table of contents) and postamble (Intellectual Property Statement, Disclaimer etc)</p>
<dt><code>&#8211;nostrip</code></p>
<dd> Don&#8217;t strip headers and footers (or body)</p>
<dt><code>&#8211;ab-diff</code></p>
<dd> Before/After diff, suitable for rfc-editor <code>&#8211;abdiff</code></p>
<dt><code>&#8211;stdout</code></p>
<dd> Send output to stdout instead to a file </p>
</dl>
</dl>
