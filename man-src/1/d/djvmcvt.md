---
title: "djvmcvt(1)"
name: "djvmcvt"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvmcvt/"
description: "djvmcvt – Convert multi-page DjVu documents."
---

<h2 class="name">NAME</h2>
<p> djvmcvt &#8211; Convert multi-page DjVu documents.</p>
<h2>SYNOPSIS</h2>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Creating a bundled document:</h2>
<p> <code>djvmcvt -b[undled] </code><i>docin.djvu</i><i>docout.djvu</i></p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Creating an indirect document:</h2>
<p> <code>djvmcvt -i[ndirect] </code><i>docin.djvu</i><i>dir</i><i>index.djvu</i> </p>
<h2>DESCRIPTION</h2>
<p> This program converts any multi-page DjVu document to either the bundled or indirect multi-page format. The input file <i>docin.djvu</i> must be either the file name of a bundled document or the index file of an indirect document. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b[undled]</code></p>
<dd> Create a bundled multi-page DjVu document named <i>docout.djvu</i>.</p>
<dt><code>-i[ndirect]</code></p>
<dd> Create an indirect multi-page DjVu document. All the files composing the indirect document will be stored into directory <i>dir</i>. The index file will be named <i>index.djvu</i>. </p>
</dl>
<h2>CREDITS</h2>
<p> This program was initially written by Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt; and was improved by Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvmcvt/">djvmcvt</a></code>(1) </p>
<h2>Index</h2>
