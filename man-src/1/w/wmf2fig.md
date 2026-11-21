---

title: "wmf2fig(1)"
name: "wmf2fig"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmf2fig/"
description: "wmf2fig – Convert metafile image to XFig format"
---

<p> wmf2fig &#8211; Convert metafile image to XFig format </p>
<h2>SYNOPSIS</h2>
<p> <code>wmf2fig</code> [<i>OPTION</i>] &#8230; [<code>-o</code><i> &lt;file.eps</i>&gt;] &lt;<i>file.wmf</i>&gt; </p>
<p> <code>wmf2fig</code> [<i>OPTION</i>] &#8230; <code>&#8211;auto</code><i> &lt;file1.wmf</i>&gt; [&lt;<i>file2.wmf</i>&gt; &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Convert metafile image to XFig format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;figunit</code>=&lt;<i>int</i>&gt;</dt>
<dd> the FIG unit as fraction of inch, default: 1200 </dd>
<dt><code>&#8211;page</code>=&lt;<i>page</i>&gt;</dt>
<dd> where &lt;<i>page</i>&gt; is one of (default A4): </dd>
<p> A[01234] B5 Letter Legal Ledger Tabloid. </p>
<dt><code>&#8211;landscape</code></dt>
<dd> switch to landscape view. </dd>
<dt><code>&#8211;portrait</code></dt>
<dd> switch to portrait view (default). </dd>
<dt><code>&#8211;maxpect</code></dt>
<dd> scale image: fit to page (1 inch margins) </dd>
<dt><code>&#8211;no-margins</code></dt>
<dd> ignore margins when scaling </dd>
<dt><code>&#8211;flat</code></dt>
<dd> render at one depth value </dd>
<dt><code>&#8211;image</code>=&lt;<i>fmt</i>&gt;</dt>
<dd> where &lt;<i>fmt</i>&gt; is one of (default eps): eps,png,jpg </dd>
<dt><code>&#8211;title</code>=&lt;<i>str</i>&gt;</dt>
<dd> comment # Title </dd>
<dt><code>&#8211;creator</code>=&lt;<i>str</i>&gt;</dt>
<dd> comment # Creator </dd>
<dt><code>&#8211;date</code>=&lt;<i>str</i>&gt;</dt>
<dd> comment # Date </dd>
<dt><code>&#8211;for</code>=&lt;<i>str</i>&gt;</dt>
<dd> comment # For </dd>
<dt><code>&#8211;version</code></dt>
<dd> display version info and exit. </dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit. </dd>
<dt><code>&#8211;wmf-help</code></dt>
<dd> display wmf-related help and exit. </dd>
</dl>
<h2>Additional wmf-related options</h2>
<dl>
<dt><code>&#8211;wmf-error</code>[=yes|no]</dt>
<dd> switch for error reports. </dd>
<dt><code>&#8211;wmf-debug</code>[=yes|no]</dt>
<dd> switch for debug reports, if any. </dd>
<dt><code>&#8211;wmf-ignore-nonfatal</code>[=yes|no]</dt>
<dd> switch to ignore (some) non-fatal errors. </dd>
<dt><code>&#8211;wmf-diagnostics</code></dt>
<dd> emit diagnostic information. </dd>
<dt><code>&#8211;wmf-fontdir</code>=&lt;<i>path</i>&gt;</dt>
<dd> add &lt;<i>path</i>&gt; to list of font directories. </dd>
<dt><code>&#8211;wmf-sys-fonts</code></dt>
<dd> use system fonts, if any found. </dd>
<dt><code>&#8211;wmf-sys-fontmap</code>=&lt;<i>file</i>&gt;</dt>
<dd> use system xml-fontmap file &lt;<i>file</i>&gt;. </dd>
<dt><code>&#8211;wmf-xtra-fonts</code></dt>
<dd> use non-system fonts, if any found. </dd>
<dt><code>&#8211;wmf-xtra-fontmap</code>=&lt;<i>file</i>&gt;</dt>
<dd> use non-system xml-fontmap file &lt;<i>file</i>&gt;. </dd>
<dt><code>&#8211;wmf-gs-fontmap</code>=&lt;<i>file</i>&gt;</dt>
<dd> use ghostscript file &lt;<i>file</i>&gt;. </dd>
<dt><code>&#8211;wmf-write</code>=&lt;<i>file</i>&gt;</dt>
<dd> write metafile to &lt;<i>file</i>&gt;. </dd>
</dl>
<h2>AUTHOR</h2>
<p> <code>wmf2fig</code> is originally written by Martin Vermeer and currently maintained by Caolán McNamara </p>
<p> This manual page was written by Yangfl for the Debian Project (and may be used by others). </p>
