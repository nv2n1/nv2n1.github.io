---
title: "djvm(1)"
name: "djvm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvm/"
description: "djvm – Manipulate bundled multi-page DjVu documents."
---

<h2 class="name">NAME</h2>
<p> djvm &#8211; Manipulate bundled multi-page DjVu documents.</p>
<h2>SYNOPSIS</h2>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Creating a bundled document:</h2>
<p> <code>djvm -c[reate] </code><i>doc.djvu</i><i>page1.djvu</i><code> &#8230; </code><i>pageN.djvu</i></p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Inserting:</h2>
<p> <code>djvm -i[nsert] </code><i>doc.djvu</i><i>page.djvu</i><code> [</code><i>pagenum</i><code>]</code></p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Removing:</h2>
<p> <code>djvm -d[elete] </code><i>doc.djvu</i><i>pagenum</i></p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Listing:</h2>
<p> <code>djvm -l[ist] </code><i>doc.djvu</i> </p>
<h2>DESCRIPTION</h2>
<p> This program creates or modifies a bundled multi-page DjVu document. Multi-page bundled documents can be used directly or converted to indirect document using command <code>djvmcvt</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c[reate]</code></p>
<dd> Create a bundled DjVu document named <i>doc.djvu</i> by collecting files <i>page1.djvu</i> to <i>pageN.djvu</i>.</p>
<dt><code>-i[nsert]</code></p>
<dd> Modify the bundled DjVu document named <i>doc.djvu</i> by inserting file <i>page.djvu</i> as page <i>pagenum</i>. Omitting argument <i>pagenum</i> means that the page should be appended at the end of the document. File <i>page.djvu</i> also can be a multi-page DjVu document. All pages will be inserted at the specified location.</p>
<dt><code>-d[elete]</code></p>
<dd> Remove page <i>pagenum</i> from the bundled multi-page DjVu document <i>doc.djvu</i>.</p>
<dt><code>-l[ist]</code></p>
<dd> List all component files in the multi-page DjVu document <i>doc.djvu</i>. </p>
</dl>
<h2>CREDITS</h2>
<p> This program was initially written by Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt; and was improved by Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvmcvt/">djvmcvt</a></code>(1) </p>
<h2>Index</h2>
