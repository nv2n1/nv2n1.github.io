---
title: "git-request-pull(1)"
name: "git-request-pull"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-request-pull/"
description: "git-request-pull – Generates a summary of pending changes"
---

<h2 class="name">NAME</h2>
<p> git-request-pull &#8211; Generates a summary of pending changes </p>
<h2>SYNOPSIS</h2>
<pre><code>
git request - pull[-p]&lt;start&gt;&lt;url&gt;[&lt;end&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Generate a request asking your upstream project to pull changes into their tree. The request, printed to the standard output, begins with the branch description, summarizes the changes and indicates from where they can be pulled. </p>
<p> The upstream project is expected to have the commit named by <code>&lt;start&gt;</code> and the output asks it to integrate the changes you made since that commit, up to the commit named by <code>&lt;end&gt;</code>, by visiting the repository named by <code>&lt;url&gt;</code>.</p>
<h2>OPTIONS</h2>
<p> -p</p>
<dl>
<dt>
<dd> Include patch text in the output.</dl>
<p> &lt;start&gt;</p>
<dl>
<dt>
<dd> Commit to start at. This names a commit that is already in the upstream history.</dl>
<p> &lt;url&gt;</p>
<dl>
<dt>
<dd> The repository URL to be pulled from.</dl>
<p> &lt;end&gt;</p>
<dl>
<dt>
<dd> Commit to end at (defaults to HEAD). This names the commit at the tip of the history you are asking to be pulled. </p>
<p> When the repository named by <code>&lt;url&gt;</code> has the commit at a tip of a ref that is different from the ref you have locally, you can use the <code>&lt;local&gt;:&lt;remote&gt;</code> syntax, to have its local name, a colon <code>:</code>, and its remote name.</dl>
<h2>EXAMPLES</h2>
<p> Imagine that you built your work on your <code>master</code> branch on top of the <code>v1.0</code> release, and want it to be integrated to the project. First you push that change to your public repository for others to see: </p>
<dl>
<dt>
<dd>
<pre>
git push <a rel="nofollow" href="https://git.ko.xz/project">https://git.ko.xz/project</a> master
</pre>
</dl>
<p> Then, you run this command: </p>
<dl>
<dt>
<dd>
<pre>
git request-pull v1.0 <a rel="nofollow" href="https://git.ko.xz/project">https://git.ko.xz/project</a> master
</pre>
</dl>
<p> which will produce a request to the upstream, summarizing the changes between the <code>v1.0</code> release and your <code>master</code>, to pull it from your public repository. </p>
<p> If you pushed your change to a branch whose name is different from the one you have locally, e.g. </p>
<dl>
<dt>
<dd>
<pre>
git push <a rel="nofollow" href="https://git.ko.xz/project">https://git.ko.xz/project</a> master:for-linus
</pre>
</dl>
<p> then you can ask that to be pulled with </p>
<dl>
<dt>
<dd>
<pre>
git request-pull v1.0 <a rel="nofollow" href="https://git.ko.xz/project">https://git.ko.xz/project</a> master:for-linus
</pre>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
