---
title: "git-branches-rename(1)"
name: "git-branches-rename"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-branches-rename/"
description: "git-branches-rename – Batch renames branches with a matching prefix to another prefix"
---

<h2>SYNOPSIS</h2>
<p> <code>git-branches-rename</code> [<i>options</i>] <i>BRANCH_PREFIX NEW_PREFIX</i></p>
<h2>DESCRIPTION</h2>
<p> Batch renames branches with a matching prefix to another prefix.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,<code>&nbsp;<wbr>&#8211;help</code></dt>
<dd> show usage information.</dd>
<dt><code>-v</code>,<code>&nbsp;<wbr>&#8211;verbose</code></dt>
<dd> print more details about what is being done.</dd>
<dt><code>-n</code>,<code>&nbsp;<wbr>&#8211;dry-run</code></dt>
<dd> do not actually rename the branches.</dd>
<dt><i>BRANCH_PREFIX</i></dt>
<dd> a prefix that matches the start of branch names.</dd>
<dt><i>NEW_PREFIX</i></dt>
<dd> the new prefix for the branch names.</dd></dl>
<h2>EXAMPLES</h2>
<pre><code>
$ git - rename - branches bug bugfix bug / 128-&gt;bugfix / 128 bug_test-&gt;bugfix_test $ git - rename - branches ma backup / ma master-&gt;backup / master main-&gt;backup / main
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="https://github.com/MestreLion/git-tools">https://github.com/MestreLion/git-tools</a></code></p>
<h2>AUTHOR</h2>
<p> Rodrigo Silva (MestreLion) linux [at] rodrigosilva.com </p>
