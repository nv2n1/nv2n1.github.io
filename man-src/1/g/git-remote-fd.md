---
title: "git-remote-fd(1)"
name: "git-remote-fd"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-remote-fd/"
description: "git-remote-fd – Reflect smart transport stream back to caller"
---

<h2 class="name">NAME</h2>
<p> git-remote-fd &#8211; Reflect smart transport stream back to caller </p>
<h2>SYNOPSIS</h2>
<p> &quot;fd::&lt;infd&gt;[,&lt;outfd&gt;][/&lt;anything&gt;]&quot; (as URL)</p>
<h2>DESCRIPTION</h2>
<p> This helper uses specified file descriptors to connect to a remote Git server. This is not meant for end users but for programs and scripts calling git fetch, push or archive. </p>
<p> If only &lt;infd&gt; is given, it is assumed to be a bidirectional socket connected to remote Git server (git-upload-pack, git-receive-pack or git-upload-archive). If both &lt;infd&gt; and &lt;outfd&gt; are given, they are assumed to be pipes connected to a remote Git server (&lt;infd&gt; being the inbound pipe and &lt;outfd&gt; being the outbound pipe. </p>
<p> It is assumed that any handshaking procedures have already been completed (such as sending service request for <a href="git://)">git://)</a> before this helper is started. </p>
<p> &lt;anything&gt; can be any string. It is ignored. It is meant for providing information to user in the URL in case that URL is displayed in some context.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> GIT_TRANSLOOP_DEBUG</p>
<dl>
<dt>
<dd> If set, prints debugging information about various reads/writes.</dl>
<h2>EXAMPLES</h2>
<p> <code>git fetch fd::17 master</code></p>
<dl>
<dt>
<dd> Fetch master, using file descriptor #17 to communicate with git-upload-pack.</dl>
<p> <code>git fetch fd::17/foo master</code></p>
<dl>
<dt>
<dd> Same as above.</dl>
<p> <code>git push fd::7,8 master (as URL)</code></p>
<dl>
<dt>
<dd> Push master, using file descriptor #7 to read data from git-receive-pack and file descriptor #8 to write data to same service.</dl>
<p> <code>git push fd::7,8/bar master</code></p>
<dl>
<dt>
<dd> Same as above.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gitremote-helpers/">gitremote-helpers</a></code>(7)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
