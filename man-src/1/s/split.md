---
title: "split(1)"
name: "split"
section: "1"
letter: "s"
url: "/docs/linux/man/1-split/"
description: "split – split a file into pieces"
---

<h2 class="name">NAME</h2>
<p> split &#8211; split a file into pieces </p>
<h2>SYNOPSIS</h2>
<p> <code>split</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE /</i>[<i>,PREFIX/</i>]]</p>
<h2>DESCRIPTION</h2>
<p> Output pieces of FILE to PREFIXaa, PREFIXab, &#8230;; default size is 1000 lines, and default PREFIX is &#8216;x&#8217;. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;suffix-length</code>=<i>,N/</i></dt>
<dd> generate suffixes of length N (default 2)</dd>
<dt><code>&#8211;additional-suffix</code>=<i>,SUFFIX/</i></dt>
<dd> append an additional SUFFIX to file names</dd>
<dt><code>-b</code>, <code>&#8211;bytes</code>=<i>,SIZE/</i></dt>
<dd> put SIZE bytes per output file</dd>
<dt><code>-C</code>, <code>&#8211;line-bytes</code>=<i>,SIZE/</i></dt>
<dd> put at most SIZE bytes of records per output file</dd>
<dt><code>-d</code></dt>
<dd> use numeric suffixes starting at 0, not alphabetic</dd>
<dt><code>&#8211;numeric-suffixes</code>[=<i>,FROM/</i>]</dt>
<dd> same as <code>-d</code>, but allow setting the start value</dd>
<dt><code>-x</code></dt>
<dd> use hex suffixes starting at 0, not alphabetic</dd>
<dt><code>&#8211;hex-suffixes</code>[=<i>,FROM/</i>]</dt>
<dd> same as <code>-x</code>, but allow setting the start value</dd>
<dt><code>-e</code>, <code>&#8211;elide-empty-files</code></dt>
<dd> do not generate empty output files with &#8216;-n&#8217;</dd>
<dt><code>&#8211;filter</code>=<i>,COMMAND/</i></dt>
<dd> write to shell COMMAND; file name is $FILE</dd>
<dt><code>-l</code>, <code>&#8211;lines</code>=<i>,NUMBER/</i></dt>
<dd> put NUMBER lines/records per output file</dd>
<dt><code>-n</code>, <code>&#8211;number</code>=<i>,CHUNKS/</i></dt>
<dd> generate CHUNKS output files; see explanation below</dd>
<dt><code>-t</code>, <code>&#8211;separator</code>=<i>,SEP/</i></dt>
<dd> use SEP instead of newline as the record separator; &#8216;
</dd></dl>