---
title: "git-ls-tree(1)"
name: "git-ls-tree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-ls-tree/"
description: "git-ls-tree – List the contents of a tree object"
---

<h2 class="name">NAME</h2>
<p> git-ls-tree &#8211; List the contents of a tree object </p>
<h2>SYNOPSIS</h2>
<pre><code>
git ls - tree[-d][-r][-t][-l][-z]
             [--name - only][--name - status][--full - name][--full - tree][--abbrev[=&lt;n&gt;]]&lt;tree - ish&gt;[&lt;path&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Lists the contents of a given tree object, like what &quot;/bin/ls -a&quot; does in the current working directory. Note that: </p>
<dl>
<dt>
<dd> &bull; the behaviour is slightly different from that of &quot;/bin/ls&quot; in that the <i>&lt;path&gt;</i> denotes just a list of patterns to match, e.g. so specifying directory name (without <code>-r</code>) will behave differently, and order of the arguments does not matter.</dl>
<dl>
<dt>
<dd> &bull; the behaviour is similar to that of &quot;/bin/ls&quot; in that the <i>&lt;path&gt;</i> is taken as relative to the current working directory. E.g. when you are in a directory <i>sub</i> that has a directory <i>dir</i>, you can run <i>git ls-tree -r HEAD dir</i> to list the contents of the tree (that is <code>sub/dir</code> in <code>HEAD</code>). You don&#8217;t want to give a tree that is not at the root level (e.g. <code>git ls-tree -r HEAD:sub dir</code>) in this case, as that would result in asking for <code>sub/sub/dir</code> in the <code>HEAD</code> commit. However, the current working directory can be ignored by passing &#8211;full-tree option.</dl>
<h2>OPTIONS</h2>
<p> &lt;tree-ish&gt;</p>
<dl>
<dt>
<dd> Id of a tree-ish.</dl>
<p> -d</p>
<dl>
<dt>
<dd> Show only the named tree entry itself, not its children.</dl>
<p> -r</p>
<dl>
<dt>
<dd> Recurse into sub-trees.</dl>
<p> -t</p>
<dl>
<dt>
<dd> Show tree entries even when going to recurse them. Has no effect if <code>-r</code> was not passed. <code>-d</code> implies <code>-t</code>.</dl>
<p> -l, &#8211;long</p>
<dl>
<dt>
<dd> Show object size of blob (file) entries.</dl>
<p> -z</p>
<dl>
<dt>
<dd> 
