---
title: "wmf2svg(1)"
name: "wmf2svg"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmf2svg/"
description: "wmf2svg – Convert metafile image to W3C’s scalable vector graphic (SVG) format"
---

<h2 class="name">NAME</h2>
<p> wmf2svg &#8211; Convert metafile image to W3C&#8217;s scalable vector graphic (SVG) format </p>
<h2>SYNOPSIS</h2>
<p> <code>wmf2svg</code> [<i>OPTION</i>] &#8230; [<code>-o</code><i> &lt;file.swg</i>&gt;] &lt;<i>file.wmf</i>&gt; </p>
<p> <code>wmf2svg</code> [<i>OPTION</i>] &#8230; <code>&#8211;auto</code><i> &lt;file1.wmf</i>&gt; [&lt;<i>file2.wmf</i>&gt; &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Convert metafile image to W3C&#8217;s scalable vector graphic (SVG) format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-z</code></p>
<dd> compressed output (.svgz) </p>
<dt><code>&#8211;inline</code></p>
<dd> include images in the svg code </p>
<dt><code>&#8211;desc</code>=&lt;<i>str</i>&gt;</p>
<dd> description tag </p>
<dt><code>&#8211;maxwidth</code>=&lt;<i>w</i>&gt;</p>
<dd> where &lt;<i>w</i>&gt; is maximum width image may have. </p>
<dt><code>&#8211;maxheight</code>=&lt;<i>h</i>&gt;</p>
<dd> where &lt;<i>h</i>&gt; is maximum height image may have. </p>
<dt><code>&#8211;maxpect</code></p>
<dd> scale image to maximum size keeping aspect. </p>
<dt><code>&#8211;maxsize</code></p>
<dd> scale image to maximum size. </p>
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
<p> <code>wmf2svg</code> is originally written by Martin Vermeer and currently maintained by Caolán McNamara </p>
<p> This manual page was written by Yangfl for the Debian Project (and may be used by others). </p>
<h2>Index</h2>
