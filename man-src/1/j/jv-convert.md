---
title: "jv-convert(1)"
name: "jv-convert"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jv-convert/"
description: "jv-convert – Convert file from one encoding to another"
---

<h2 class="name">NAME</h2>
<p> jv-convert &#8211; Convert file from one encoding to another </p>
<h2>SYNOPSIS</h2>
<p> <code>jv-convert</code> [<font SIZE="-1"><code>OPTION</code></font>] &#8230; [<i></i><font SIZE="-1"><i>INPUTFILE</i></font><i></i> [<i></i><font SIZE="-1"><i>OUTPUTFILE</i></font><i></i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>jv-convert</code> is a utility included with <tt>&quot;libgcj&quot;</tt> which converts a file from one encoding to another. It is similar to the Unix <code>iconv</code> utility. </p>
<p> The encodings supported by <code>jv-convert</code> are platform-dependent. Currently there is no way to get a list of all supported encodings.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;encoding</code> <i>name</i></p>
<dd>
<dt><code>&#8211;from</code> <i>name</i></p>
<dd> Use <i>name</i> as the input encoding. The default is the current locale&#8217;s encoding.</p>
<dt><code>&#8211;to</code> <i>name</i></p>
<dd> Use <i>name</i> as the output encoding. The default is the <tt>&quot;JavaSrc&quot;</tt> encoding; this is <font SIZE="-1">ASCII</font> with <code>
