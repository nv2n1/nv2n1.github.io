---
title: "xrdp-sesadmin(8)"
name: "xrdp-sesadmin"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdp-sesadmin/"
description: "xrdp-sesadmin – console XRDP sessions administration tool"
---

<p>xrdp-sesadmin &#8211; console XRDP sessions administration tool </p>
<h2>Synopsis</h2>
<p><code>xrdp-sesadmin</code> [<i>options</i>] <code>-c=</code><i>command</i> </p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>xrdp-sesadmin</code> command. <code>xrdp-sesadmin</code> is a console program to administer running XRDP sessions. </p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-u=</code><i>username</i></dt>
<dd><i>Username</i> for authentication on the server. Defaults to <code>root</code>. </dd>
<dt><code>-p=</code><i>password</i></dt>
<dd>The <i>password</i> to authenticate with. The default is to ask for the password interactively. </dd>
<dt><code>-s=</code><i>server</i></dt>
<dd>The host address of the <i>server</i> to connect to. Defaults to <code>localhost</code>. </dd>
<dt><code>-i=</code><i>port</i></dt>
<dd>The TCP <i>port</i> number to connect to. Defaults to <code>3350</code>. </dd>
<dt><code>-c=</code><i>command</i></dt>
<dd>Specifies the <i>command</i> to execute on the server. Valid commands are:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>list</code></dt>
<dd>List currently active sessions.</dd>
<dt><code>kill:</code><i>sid</i></dt>
<dd>Kills the session specified the given <i>session id</i>. (not yet implemented).</dd></dl>
</dl>
</dl>
<h2>Files</h2>
<p>xrdp-sesadmin.log</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8). </p>
