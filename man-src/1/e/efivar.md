---
title: "efivar(1)"
name: "efivar"
section: "1"
letter: "e"
url: "/docs/linux/man/1-efivar/"
description: "efivar – Tool to manipulate UEFI variables"
---

<h2>NAME</h2>
<p> efivar &#8211; Tool to manipulate UEFI variables</p>
<h2>SYNOPSIS</h2>
<p> <code>efivar</code> [<i>,OPTION/</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> list current variables</p>
<dt><code>-p</code>, <code>&#8211;print</code></p>
<dd> print variable specified by <code>&#8211;name</code></p>
<dt><code>-n</code>, <code>&#8211;name=</code>&lt;guid-name&gt;</p>
<dd> variable to manipulate, in the form 8be4df61-93ca-11d2-aa0d-00e098032b8c-Boot0000</p>
<dt><code>-a</code>, <code>&#8211;append</code></p>
<dd> append to variable specified by <code>&#8211;name</code></p>
<dt><code>-f</code>, <code>&#8211;fromfile=</code>&lt;file&gt;</p>
<dd> use data from &lt;file&gt;</p>
<dt><code>-t</code>, <code>&#8211;attributes=</code>&lt;attributes&gt;</p>
<dd> attributes to use on append</dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show this help message</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message </p>
</dl>
<h2>Index</h2>
