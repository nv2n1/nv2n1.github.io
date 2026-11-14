---
title: "wmf2fig(1)"
name: "wmf2fig"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmf2fig/"
description: "wmf2fig – Convert metafile image to XFig format"
---

<h2 class="name">NAME</h2>
<p> wmf2fig &#8211; Convert metafile image to XFig format </p>
<h2>SYNOPSIS</h2>
<p> <code>wmf2fig</code> [<i>OPTION</i>] &#8230; [<code>-o</code><i> &lt;file.eps</i>&gt;] &lt;<i>file.wmf</i>&gt; </p>
<p> <code>wmf2fig</code> [<i>OPTION</i>] &#8230; <code>&#8211;auto</code><i> &lt;file1.wmf</i>&gt; [&lt;<i>file2.wmf</i>&gt; &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Convert metafile image to XFig format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;figunit</code>=&lt;<i>int</i>&gt;</p>
<dd> the FIG unit as fraction of inch, default: 1200 </p>
<dt><code>&#8211;page</code>=&lt;<i>page</i>&gt;</p>
<dd> where &lt;<i>page</i>&gt; is one of (default A4): </p>
<p> A[01234] B5 Letter Legal Ledger Tabloid. </p>
<dt><code>&#8211;landscape</code></p>
<dd> switch to landscape view. </p>
<dt><code>&#8211;portrait</code></p>
<dd> switch to portrait view (default). </p>
<dt><code>&#8211;maxpect</code></p>
<dd> scale image: fit to page (1 inch margins) </p>
<dt><code>&#8211;no-margins</code></p>
<dd> ignore margins when scaling </p>
<dt><code>&#8211;flat</code></p>
<dd> render at one depth value </p>
<dt><code>&#8211;image</code>=&lt;<i>fmt</i>&gt;</p>
<dd> where &lt;<i>fmt</i>&gt; is one of (default eps): eps,png,jpg </p>
<dt><code>&#8211;title</code>=&lt;<i>str</i>&gt;</p>
<dd> comment # Title </p>
<dt><code>&#8211;creator</code>=&lt;<i>str</i>&gt;</p>
<dd> comment # Creator </p>
<dt><code>&#8211;date</code>=&lt;<i>str</i>&gt;</p>
<dd> comment # Date </p>
<dt><code>&#8211;for</code>=&lt;<i>str</i>&gt;</p>
<dd> comment # For </p>
<dt><code>&#8211;version</code></p>
<dd> display version info and exit. </p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit. </p>
<dt><code>&#8211;wmf-help</code></p>
<dd> display wmf-related help and exit. </p>
</dl>
<h2>Additional wmf-related options</h2>
<dl>
<dt><code>&#8211;wmf-error</code>[=yes|no]</p>
<dd> switch for error reports. </p>
<dt><code>&#8211;wmf-debug</code>[=yes|no]</p>
<dd> switch for debug reports, if any. </p>
<dt><code>&#8211;wmf-ignore-nonfatal</code>[=yes|no]</p>
<dd> switch to ignore (some) non-fatal errors. </p>
<dt><code>&#8211;wmf-diagnostics</code></p>
<dd> emit diagnostic information. </p>
<dt><code>&#8211;wmf-fontdir</code>=&lt;<i>path</i>&gt;</p>
<dd> add &lt;<i>path</i>&gt; to list of font directories. </p>
<dt><code>&#8211;wmf-sys-fonts</code></p>
<dd> use system fonts, if any found. </p>
<dt><code>&#8211;wmf-sys-fontmap</code>=&lt;<i>file</i>&gt;</p>
<dd> use system xml-fontmap file &lt;<i>file</i>&gt;. </p>
<dt><code>&#8211;wmf-xtra-fonts</code></p>
<dd> use non-system fonts, if any found. </p>
<dt><code>&#8211;wmf-xtra-fontmap</code>=&lt;<i>file</i>&gt;</p>
<dd> use non-system xml-fontmap file &lt;<i>file</i>&gt;. </p>
<dt><code>&#8211;wmf-gs-fontmap</code>=&lt;<i>file</i>&gt;</p>
<dd> use ghostscript file &lt;<i>file</i>&gt;. </p>
<dt><code>&#8211;wmf-write</code>=&lt;<i>file</i>&gt;</p>
<dd> write metafile to &lt;<i>file</i>&gt;. </p>
</dl>
<h2>AUTHOR</h2>
<p> <code>wmf2fig</code> is originally written by Martin Vermeer and currently maintained by Caolán McNamara </p>
<p> This manual page was written by Yangfl for the Debian Project (and may be used by others). </p>
<h2>Index</h2>
