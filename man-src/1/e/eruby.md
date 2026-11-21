---
title: "eruby(1)"
name: "eruby"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eruby/"
description: "eruby – Embedded Ruby Language"
---

<h2>NAME</h2>
<p> eruby &#8211; Embedded Ruby Language</p>
<h2>SYNOPSIS</h2>
<p> eruby [options] [inputfile]</p>
<h2>DESCRIPTION</h2>
<p> eruby interprets a Ruby code embedded text file. For example, eruby enables you to embed a Ruby code to a HTML file. A Ruby block starts with `&lt;%&#8217; and ends with `%&gt;&#8217;. eRuby replaces the block with its output. If `&lt;%&#8217; is followed by `=&#8217;, eRuby replaces the block with a value of the block. If `&lt;%&#8217; is followed by `#&#8217;, the block is ignored as a comment.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
</dt><dd> <code>-d, &#8211;debug</code> set debugging flags (set $DEBUG to true)</dd>
<dt>
</dt><dd> <code>-Kkcode</code> specifies KANJI (Japanese) code-set</dd>
<dt>
</dt><dd> <code>-Mmode</code> specifies runtime mode </dd>
<pre>
    f: filter mode
    c: CGI mode
    n: NPH-CGI mode
</pre>
<dt>
</dt><dd> <code>-C charset</code> specifies charset parameter for Content-Type</dd>
<dt>
</dt><dd> <code>-n, &#8211;noheader</code> disables CGI header output</dd>
<dt>
</dt><dd> <code>-v, &#8211;verbose</code> enables verbose mode</dd>
<dt>
</dt><dd> <code>&#8211;version </code> print version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Shugo Maeda &lt;shugo [at] ruby-lang.org&gt; </p>
