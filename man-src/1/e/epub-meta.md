---
title: "epub-meta(1)"
name: "epub-meta"
section: "1"
letter: "e"
url: "/docs/linux/man/1-epub-meta/"
description: "epub-meta – read and write metadata from an EPUB ebook file"
---

<h2 class="name">NAME</h2>
<p> <code> epub-meta </code>&#8211; read and write metadata from an EPUB ebook file </p>
<h2>USAGE</h2>
<p> epub-meta [options] myfile.epub</p>
<h2>DESCRIPTION</h2>
<p> Read and write metadata from an ebook file. </p>
<p> Whenever you pass arguments to epub-meta that have spaces in them, enclose the arguments in quotation marks.</p>
<h2>MAIN OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-t</code> TITLE, <code>&#8211;title</code>=TITLE</dt>
<dd> Set the book title</dd>
<dt><code>-a</code> AUTHORS, <code>&#8211;authors</code>=AUTHORS</dt>
<dd> Set the authors</dd>
<dt><code>&#8211;comment</code>=COMMENT</dt>
<dd> Set the comment</dd>
<dt><code>&#8211;tags</code>=TAGS</dt>
<dd> A comma separated list of tags to set</dd>
<dt><code>&#8211;series</code>=SERIES</dt>
<dd> The series to which this book belongs</dd>
<dt><code>&#8211;series-index</code>=SERIES_INDEX</dt>
<dd> The series index</dd>
<dt><code>&#8211;language</code>=LANGUAGE</dt>
<dd> The book language</dd>
<dt><code>&#8211;get-cover</code></dt>
<dd> Extract the cover</dd></dl>
<h2>AUTHOR</h2>
<p> Created by Kovid Goyal &lt;kovid [at] kovidgoyal.net&gt; </p>
<h2>Index</h2>
