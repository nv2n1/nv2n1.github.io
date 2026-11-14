---
title: "git-branches-rename(1)"
name: "git-branches-rename"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-branches-rename/"
description: "git-branches-rename – Batch renames branches with a matching prefix to another prefix"
---

<h2 class="name">NAME</h2>
<p> git-branches-rename &#8211; Batch renames branches with a matching prefix to another prefix </p>
<h2>SYNOPSIS</h2>
<p> <code>git-branches-rename</code> [<i>options</i>] <i>BRANCH_PREFIX NEW_PREFIX</i></p>
<h2>DESCRIPTION</h2>
<p> Batch renames branches with a matching prefix to another prefix.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,<code>&nbsp;<wbr>&#8211;help</code></p>
<dd> show usage information.</p>
<dt><code>-v</code>,<code>&nbsp;<wbr>&#8211;verbose</code></p>
<dd> print more details about what is being done.</p>
<dt><code>-n</code>,<code>&nbsp;<wbr>&#8211;dry-run</code></p>
<dd> do not actually rename the branches.</p>
<dt><i>BRANCH_PREFIX</i></p>
<dd> a prefix that matches the start of branch names.</p>
<dt><i>NEW_PREFIX</i></p>
<dd> the new prefix for the branch names.</dl>
<h2>EXAMPLES</h2>
<pre><code>
$ git - rename - branches bug bugfix bug / 128-&gt;bugfix / 128 bug_test-&gt;bugfix_test $ git - rename - branches ma backup / ma master-&gt;backup / master main-&gt;backup / main
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="https://github.com/MestreLion/git-tools">https://github.com/MestreLion/git-tools</a></code></p>
<h2>AUTHOR</h2>
<p> Rodrigo Silva (MestreLion) linux [at] rodrigosilva.com </p>
<h2>Index</h2>
