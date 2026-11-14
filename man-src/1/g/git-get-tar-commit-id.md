---
title: "git-get-tar-commit-id(1)"
name: "git-get-tar-commit-id"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-get-tar-commit-id/"
description: "git-get-tar-commit-id – Extract commit ID from an archive created using git-archive"
---

<h2 class="name">NAME</h2>
<p> git-get-tar-commit-id &#8211; Extract commit ID from an archive created using git-archive </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git get-tar-commit-id</i>
</pre>
<h2>DESCRIPTION</h2>
<p> Read a tar archive created by <i>git archive</i> from the standard input and extract the commit ID stored in it. It reads only the first 1024 bytes of input, thus its runtime is not influenced by the size of the tar archive very much. </p>
<p> If no commit ID is found, <i>git get-tar-commit-id</i> quietly exists with a return code of 1. This can happen if the archive had not been created using <i>git archive</i> or if the first parameter of <i>git archive</i> had been a tree ID instead of a commit ID or tag.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
