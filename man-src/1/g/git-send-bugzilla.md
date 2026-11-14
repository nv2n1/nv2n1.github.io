---
title: "git-send-bugzilla(1)"
name: "git-send-bugzilla"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-send-bugzilla/"
description: "git-send-bugzilla – Attach patches to a bugzilla bug"
---

<h2 class="name">NAME</h2>
<p> git-send-bugzilla &#8211; Attach patches to a bugzilla bug </p>
<h2>SYNOPSIS</h2>
<pre><code>
git - send - bugzilla[OPTIONS](--dry - run | &lt;bugid&gt;)&lt;since&gt;[..&lt;until&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Attach each commit between &lt;since&gt; and &lt;until&gt; to the bug &lt;bugid&gt; on GNOMEcqs bugzilla. If ..&lt;until&gt; is not specified, the head of the current working tree is implied. </p>
<p> If -n (or bugzilla.numbered in the repository configuration) is specified, instead of &quot;[PATCH] Subject&quot;, the first line is formatted as &quot;[n/m] Subject&quot;.</p>
<h2>OPTIONS</h2>
<p> -b|&#8211;url &lt;url&gt;</p>
<dl>
<dt>
<dd> The Bugzilla URL.</dl>
<p> -u|&#8211;username &lt;username&gt;</p>
<dl>
<dt>
<dd> Your Bugzilla user name.</dl>
<p> -p|&#8211;password &lt;password&gt;</p>
<dl>
<dt>
<dd> Your Bugzilla password.</dl>
<p> -s|&#8211;squash</p>
<dl>
<dt>
<dd> Send all the selected commits as a single patch.</dl>
<p> -n|&#8211;numbered</p>
<dl>
<dt>
<dd> Prefix attachment names with [n/m].</dl>
<p> &#8211;start-number &lt;n&gt;</p>
<dl>
<dt>
<dd> Start numbering the patches at &lt;n&gt; instead of 1.</dl>
<p> &#8211;dry-run</p>
<dl>
<dt>
<dd> Doncqt do anything for real. If you use this option you shouldncqt specify a bug id.</dl>
<h2>CONFIGURATION</h2>
<p> You can specify an URL, an user name and a password for the bugzilla in the repository configuration as follows: </p>
<dl>
<dt>
<dd>
<pre><code>
[bugzilla] url = "http://bugzilla.kernel.org" username = "wanda [at] gnome.org" password = "********"
</code></pre>
</dl>
<p> If you doncqt specify one of them in the repository configuration nor in the command line, git-send-bugzilla will ask for it before trying to attach the patches.</p>
<h2>EXAMPLES</h2>
<p> git-send-bugzilla -n 12345 master Extract all commits which are in the current branch but not in the <i>master</i> branch. Each commit will be attached as a single patch to the bug #12345</p>
<h2>AUTHOR</h2>
<p> Written by Steve Fr&#8217;ecinaux &lt;m[blue]<code>code [at] istique.net</code>m[]<font SIZE="-2">[1]</font>&gt;.</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Steve Fr&#8217;ecinaux &lt;m[blue]<code>code [at] istique.net</code>m[]<font SIZE="-2">[1]</font>&gt;.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> code [at] istique.net</p>
<dl>
<dt>
<dd> mailto:code [at] istique.net</dl>
</dl>
<h2>Index</h2>
