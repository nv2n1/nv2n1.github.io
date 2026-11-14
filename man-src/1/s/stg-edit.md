---
title: "stg-edit(1)"
name: "stg-edit"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-edit/"
description: "stg-edit – Edit a patch description or diff"
---

<h2 class="name">NAME</h2>
<p> stg-edit &#8211; Edit a patch description or diff </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg edit[options][--][&lt;patch&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Edit the description and author information of the given patch (or the current patch if no patch name was given). With &#8211;diff, also edit the diff. </p>
<p> The editor is invoked with the following contents: </p>
<dl>
<dt>
<dd>
<pre>
From: A U Thor &lt;author [at] example.com&gt;
Date: creation date
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Patch description
</pre>
</dl>
<p> If &#8211;diff was specified, the diff appears at the bottom, after a separator: </p>
<dl>
<dt>
<dd>
<pre>
---
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Diff text
</pre>
</dl>
<p> Command-line options can be used to modify specific information without invoking the editor. (With the &#8211;edit option, the editor is invoked even if such command-line options are given.) </p>
<p> If the patch diff is edited but does not apply, no changes are made to the patch at all. The edited patch is saved to a file which you can feed to &quot;stg edit &#8211;file&quot;, once you have made sure it does apply. </p>
<p> With &#8211;set-tree you set the git tree of the patch to the specified TREE-ISH without changing the tree of any other patches. When used on the top patch, the index and work tree will be updated to match the tree. This low-level option is primarily meant to be used by tools built on top of StGit, such as the Emacs mode. See also the &#8211;set-tree flag of stg push.</p>
<h2>OPTIONS</h2>
<p> -d, &#8211;diff</p>
<dl>
<dt>
<dd> Edit the patch diff.</dl>
<p> -e, &#8211;edit</p>
<dl>
<dt>
<dd> Invoke interactive editor.</dl>
<p> &#8211;sign</p>
<dl>
<dt>
<dd> Add a &quot;Signed-off-by:&quot; to the end of the patch.</dl>
<p> &#8211;ack</p>
<dl>
<dt>
<dd> Add an &quot;Acked-by:&quot; line to the end of the patch.</dl>
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
<p> -O OPTIONS, &#8211;diff-opts OPTIONS</p>
<dl>
<dt>
<dd> Extra options to pass to &quot;git diff&quot;.</dl>
<p> -t TREE-ISH, &#8211;set-tree TREE-ISH</p>
<dl>
<dt>
<dd> Set the git tree of the patch to TREE-ISH.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
