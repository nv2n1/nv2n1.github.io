---
title: "exempi(1)"
name: "exempi"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exempi/"
---

<h2 class="name">NAME</h2>
 

 

 exempi - command line tool to manipulate XMP metadata

<h2>SYNTAX</h2>

 

 exempi { -h | [ -R ] [ -x ] [ { -w | -o &lt;file&gt; } ] [ { -g &lt;prop_name&gt; | -s &lt;prop_name&gt; -v &lt;value&gt; } ] } &lt;files&gt; 

<h2>OPTIONS</h2>

 

<dl>
<dt>-h: show this help
<dd>
<dt>-R: don't reconcile
<dd>
<dt>-x: dump XML
<dd>
<dt>-X: file(s) is XMP
<dd>
<dt>-w: write in place. Only for -s. Not compatible with -o.
<dd>
<dt>-o &lt;file&gt;: file to write the output to.
<dd>
<dt>-n &lt;ns&gt; &lt;prefix&gt;: set the prefix for a namespace.
<dd>
<dt>-g &lt;prop_name&gt;: retrieve the value with prop_name.
<dd>
<dt>-s &lt;prop_name&gt; -v &lt;value&gt;: retrieve or get the value.
<dd>
<dt>&lt;files&gt; the files to read from.
<dd> 

</dl>

<h2>SECURITY</h2>

 

 The source code hasn't been audited for security. The command line tool doesn't have a strong input sanity checking easier. 

 Be careful not to run the tool as super-user. Be careful if you decide to use it in an online (web) application. 

 Patches and suggestions welcome. 

<h2>AUHTORS</h2>

 

 Exempi is written by Hubert Figuiere 

 It contains the XMP SDK written by Adobe Systems Inc. 

<h2>LICENSE</h2>

 

 Exempi is licensed under the BSD license. 

<h2>Index</h2>


