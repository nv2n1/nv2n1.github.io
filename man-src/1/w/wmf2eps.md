---

title: "wmf2eps(1)"
name: "wmf2eps"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmf2eps/"
description: "wmf2eps – Convert metafile image to postscript"
---

<p> wmf2eps &#8211; Convert metafile image to postscript </p>
<h2>SYNOPSIS</h2>
<p> <code>wmf2eps</code> [<i>OPTION</i>] &#8230; [<code>-o</code><i> &lt;file.eps</i>&gt;] &lt;<i>file.wmf</i>&gt; </p>
<p> <code>wmf2eps</code> [<i>OPTION</i>] &#8230; <code>&#8211;auto</code><i> &lt;file1.wmf</i>&gt; [&lt;<i>file2.wmf</i>&gt; &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Convert metafile image to postscript. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;eps</code></dt>
<dd> output as eps (default). </dd>
<dt><code>&#8211;ps</code></dt>
<dd> output as ps. </dd>
<dt><code>&#8211;page</code>=&lt;<i>page</i>&gt;</dt>
<dd> where &lt;<i>page</i>&gt; is one of A4 (default). [ps-mode only] </dd>
<dt><code>&#8211;landscape</code></dt>
<dd> switch to landscape view. [ps-mode only] </dd>
<dt><code>&#8211;portrait</code></dt>
<dd> switch to portrait view (default). [ps-mode only] </dd>
<dt><code>&#8211;bbox</code>=&lt;<i>geom</i>&gt;</dt>
<dd> geometry setting: <code>&#8211;bbox</code>=<i>W</i>x<i>H</i>+<i>X</i>+<i>Y</i> [ps-mode only] </dd>
<dt><code>&#8211;centre</code></dt>
<dd> centre image in page. [ps-mode only] </dd>
<dt><code>&#8211;maxpect</code></dt>
<dd> scale image to maximum size keeping aspect. [ps-mode only] </dd>
<dt><code>&#8211;title</code>=&lt;<i>str</i>&gt;</dt>
<dd> postscript %%Title </dd>
<dt><code>&#8211;creator</code>=&lt;<i>str</i>&gt;</dt>
<dd> postscript %%Creator </dd>
<dt><code>&#8211;date</code>=&lt;<i>str</i>&gt;</dt>
<dd> postscript %%Date </dd>
<dt><code>&#8211;for</code>=&lt;<i>str</i>&gt;</dt>
<dd> postscript %%For </dd>
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
<p> <code>wmf2eps</code> is originally written by Martin Vermeer and currently maintained by Caolán McNamara </p>
<p> This manual page was written by Yangfl for the Debian Project (and may be used by others). </p>
