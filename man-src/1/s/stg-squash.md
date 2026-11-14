---
title: "stg-squash(1)"
name: "stg-squash"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-squash/"
description: "stg-squash – Squash two or more patches into one"
---

<h2 class="name">NAME</h2>
<p> stg-squash &#8211; Squash two or more patches into one </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg squash[options][--]&lt;patches&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Squash two or more patches, creating one big patch that contains all their changes. In more detail: </p>
<dl>
<dt>
<dd> 1. Pop all the given patches, plus any other patches on top of them.</dl>
<dl>
<dt>
<dd> 2. Push the given patches in the order they were given on the command line.</dl>
<dl>
<dt>
<dd> 3. Squash the given patches into one big patch.</dl>
<dl>
<dt>
<dd> 4. Allow the user to edit the commit message of the new patch interactively.</dl>
<dl>
<dt>
<dd> 5. Push the other patches that were popped in step (1).</dl>
<p> Conflicts can occur whenever we push a patch; that is, in step (2) and (5). If there are conflicts, the command will stop so that you can resolve them.</p>
<h2>OPTIONS</h2>
<p> -n NAME, &#8211;name NAME</p>
<dl>
<dt>
<dd> Name of squashed patch.</dl>
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
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
