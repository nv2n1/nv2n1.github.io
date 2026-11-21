---

title: "efivar(1)"
name: "efivar"
section: "1"
letter: "e"
url: "/docs/linux/man/1-efivar/"
description: "efivar – Tool to manipulate UEFI variables"
---

<p> efivar &#8211; Tool to manipulate UEFI variables</p>
<h2>SYNOPSIS</h2>
<p> <code>efivar</code> [<i>,OPTION/</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;list</code></dt>
<dd> list current variables</dd>
<dt><code>-p</code>, <code>&#8211;print</code></dt>
<dd> print variable specified by <code>&#8211;name</code></dd>
<dt><code>-n</code>, <code>&#8211;name=</code>&lt;guid-name&gt;</dt>
<dd> variable to manipulate, in the form 8be4df61-93ca-11d2-aa0d-00e098032b8c-Boot0000</dd>
<dt><code>-a</code>, <code>&#8211;append</code></dt>
<dd> append to variable specified by <code>&#8211;name</code></dd>
<dt><code>-f</code>, <code>&#8211;fromfile=</code>&lt;file&gt;</dt>
<dd> use data from &lt;file&gt;</dd>
<dt><code>-t</code>, <code>&#8211;attributes=</code>&lt;attributes&gt;</dt>
<dd> attributes to use on append</dd></dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></dt>
<dd> Show this help message</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display brief usage message </dd>
</dl>
