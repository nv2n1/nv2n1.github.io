---
title: "stg-id(1)"
name: "stg-id"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-id/"
description: "stg-id – Print the git hash value of a StGit reference"
---

<h2 class="name">NAME</h2>
<p> stg-id &#8211; Print the git hash value of a StGit reference </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg id[options][--][&lt;id&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Print the SHA1 value of a Git id (defaulting to HEAD). In addition to the standard Git id&#8217;s like heads and tags, this command also accepts <i>[&lt;branch&gt;:]&lt;patch&gt;</i> for the id of a patch, <i>[&lt;branch&gt;:]{base}</i> for the base of the stack and <i>[&lt;branch&gt;:]{public}</i> for the public branch corresponding to the stack (see the <i>publish</i> command for details). If no branch is specified, it defaults to the current one. The bottom of a patch is accessible with the <i>[&lt;branch&gt;:]&lt;patch&gt;^</i> format.</p>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
