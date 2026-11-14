---
title: "stg-push(1)"
name: "stg-push"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-push/"
description: "stg-push – Push one or more patches onto the stack"
---

<h2 class="name">NAME</h2>
<p> stg-push &#8211; Push one or more patches onto the stack </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg push[options][--][&lt;patch1&gt;][&lt;patch2&gt;][&lt;patch3&gt;..&lt;patch4&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Push one or more patches (defaulting to the first unapplied one) onto the stack. The <i>push</i> operation allows patch reordering by commuting them with the three-way merge algorithm. If there are conflicts while pushing a patch, those conflicts are written to the work tree, and the command halts. Conflicts raised during the push operation have to be fixed and the <i>git add &#8211;update</i> command run (alternatively, you may undo the conflicting push with <i>stg undo</i>). </p>
<p> The command also notifies when the patch becomes empty (fully merged upstream) or is modified (three-way merged) by the <i>push</i> operation.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> Push all the unapplied patches.</dl>
<p> -n NUMBER, &#8211;number NUMBER</p>
<dl>
<dt>
<dd> Push the specified number of patches. </p>
<p> With a negative number, push all but that many patches.</dl>
<p> &#8211;reverse</p>
<dl>
<dt>
<dd> Push the patches in reverse order.</dl>
<p> &#8211;set-tree</p>
<dl>
<dt>
<dd> Push the patches, but don&#8217;t perform a merge. Instead, the resulting tree will be identical to the tree that the patch previously created. </p>
<p> This can be useful when splitting a patch by first popping the patch and creating a new patch with some of the changes. Pushing the original patch with <i>&#8211;set-tree</i> will avoid conflicts and only the remaining changes will be in the patch.</dl>
<p> -k, &#8211;keep</p>
<dl>
<dt>
<dd> Keep the local changes.</dl>
<p> -m, &#8211;merged</p>
<dl>
<dt>
<dd> Check for patches merged upstream.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
