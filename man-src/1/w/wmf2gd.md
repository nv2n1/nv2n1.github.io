---

title: "wmf2gd(1)"
name: "wmf2gd"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmf2gd/"
description: "wmf2gd – Convert metafile image to one of: png,jpg"
---

<p> wmf2gd &#8211; Convert metafile image to one of: png,jpg </p>
<h2>SYNOPSIS</h2>
<p> <code>wmf2gd</code> [<i>OPTION</i>] &#8230; [<code>-o</code><i> &lt;file.png</i>&gt;] &lt;<i>file.wmf</i>&gt; </p>
<p> <code>wmf2gd</code> [<i>OPTION</i>] &#8230; [<code>-t</code><i> jpeg] [</i><code>-o</code><i> &lt;file.jpg</i>&gt;] &lt;<i>file.wmf</i>&gt; </p>
<p> <code>wmf2gd</code> [<i>OPTION</i>] &#8230; <code>&#8211;auto</code><i> &lt;file1.wmf</i>&gt; [&lt;<i>file2.wmf</i>&gt; &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Convert metafile image to one of: png,jpg. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code> &lt;<i>type</i>&gt;</dt>
<dd> where &lt;<i>type</i>&gt; is one of: png,jpeg. </dd>
<dt><code>&#8211;maxwidth</code>=&lt;<i>w</i>&gt;</dt>
<dd> where &lt;<i>w</i>&gt; is maximum width image may have. </dd>
<dt><code>&#8211;maxheight</code>=&lt;<i>h</i>&gt;</dt>
<dd> where &lt;<i>h</i>&gt; is maximum height image may have. </dd>
<dt><code>&#8211;maxpect</code></dt>
<dd> scale image to maximum size keeping aspect. </dd>
<dt><code>&#8211;maxsize</code></dt>
<dd> scale image to maximum size. </dd>
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
<p> <code>wmf2gd</code> is originally written by Martin Vermeer and currently maintained by Caolán McNamara </p>
<p> This manual page was written by Yangfl for the Debian Project (and may be used by others). </p>
