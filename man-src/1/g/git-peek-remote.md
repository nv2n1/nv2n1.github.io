---
title: "git-peek-remote(1)"
name: "git-peek-remote"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-peek-remote/"
description: "git-peek-remote – List the references in a remote repository"
---

<h2 class="name">NAME</h2>
<p> git-peek-remote &#8211; List the references in a remote repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git peek - remote[--upload - pack = &lt;git - upload - pack&gt;] [&lt;host&gt;:]&lt;directory&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command is deprecated; use <i>git ls-remote</i> instead.</p>
<h2>OPTIONS</h2>
<p> &#8211;upload-pack=&lt;git-upload-pack&gt;</p>
<dl>
<dt>
<dd> Use this to specify the path to <i>git-upload-pack</i> on the remote side, if it is not found on your $PATH. Some installations of sshd ignores the user&#8217;s environment setup scripts for login shells (e.g. .bash_profile) and your privately installed git may not be found on the system default $PATH. Another workaround suggested is to set up your $PATH in &quot;.bashrc&quot;, but this flag is for people who do not want to pay the overhead for non-interactive shells, but prefer having a lean .bashrc file (they set most of the things up in .bash_profile).</dl>
<p> &lt;host&gt;</p>
<dl>
<dt>
<dd> A remote host that houses the repository. When this part is specified, <i>git-upload-pack</i> is invoked via ssh.</dl>
<p> &lt;directory&gt;</p>
<dl>
<dt>
<dd> The repository to sync from.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
