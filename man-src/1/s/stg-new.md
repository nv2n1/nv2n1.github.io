---
title: "stg-new(1)"
name: "stg-new"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-new/"
description: "stg-new – Create a new, empty patch"
---

<h2 class="name">NAME</h2>
<p> stg-new &#8211; Create a new, empty patch </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg new[options][--][&lt;name&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Create a new, empty patch on the current stack. The new patch is created on top of the currently applied patches, and is made the new top of the stack. Uncommitted changes in the work tree are not included in the patch &#8212; that is handled by <code><a href="/docs/linux/man/1-stg-refresh/">stg-refresh</a></code>(1). </p>
<p> The given name must be unique in the stack, and may only contain alphanumeric characters, dashes and underscores. If no name is given, one is generated from the first line of the patch&#8217;s commit message. </p>
<p> An editor will be launched to edit the commit message to be used for the patch, unless the <i>&#8211;message</i> flag already specified one. The <i>patchdescr.tmpl</i> template file (if available) is used to pre-fill the editor.</p>
<h2>OPTIONS</h2>
<p> &#8211;author &quot;NAME &lt;EMAIL&gt;&quot;</p>
<dl>
<dt>
<dd> Set the author details.</dl>
<p> &#8211;authname NAME</p>
<dl>
<dt>
<dd> Set the author name.</dl>
<p> &#8211;authemail EMAIL</p>
<dl>
<dt>
<dd> Set the author email.</dl>
<p> &#8211;authdate DATE</p>
<dl>
<dt>
<dd> Set the author date.</dl>
<p> -m MESSAGE, &#8211;message MESSAGE</p>
<dl>
<dt>
<dd> Use MESSAGE instead of invoking the editor.</dl>
<p> -f FILE, &#8211;file FILE</p>
<dl>
<dt>
<dd> Use the contents of FILE instead of invoking the editor. (If FILE is &quot;-&quot;, write to stdout.)</dl>
<p> &#8211;save-template FILE</p>
<dl>
<dt>
<dd> Instead of running the command, just write the message template to FILE, and exit. (If FILE is &quot;-&quot;, write to stdout.) </p>
<p> When driving StGit from another program, it is often useful to first call a command with <i>&#8211;save-template</i>, then let the user edit the message, and then call the same command with <i>&#8211;file</i>.</dl>
<p> &#8211;sign</p>
<dl>
<dt>
<dd> Add a &quot;Signed-off-by:&quot; to the end of the patch.</dl>
<p> &#8211;ack</p>
<dl>
<dt>
<dd> Add an &quot;Acked-by:&quot; line to the end of the patch.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
