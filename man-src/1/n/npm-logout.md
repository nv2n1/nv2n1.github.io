---
title: "npm-logout(1)"
name: "npm-logout"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-logout/"
description: "npm-logout – Log out of the registry"
---

<h2 class="name">NAME</h2>
<p> <code>npm-logout</code> &#8211; Log out of the registry </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm logout[--registry = &lt;url&gt;][--scope = &lt;@scope&gt;]
</code></pre>
</dl>
<h3>Description</h3>
<p> When logged into a registry that supports token-based authentication, tell the server to end this token&#8217;s session. This will invalidate the token everywhere you&#8217;re using it, not just for the current environment. </p>
<p> When logged into a legacy registry that uses username and password authentication, this will clear the credentials in your user configuration. In this case, it will <i>only</i> affect the current environment. </p>
<p> If <code>&#8211;scope</code> is provided, this will find the credentials for the registry connected to that scope, if set.</p>
<h3>Configuration</h3>
<h3>registry</h3>
<p> Default: <a rel="nofollow" href="https://registry.npmjs.org/">https://registry.npmjs.org/</a> </p>
<p> The base URL of the npm package registry. If <code>scope</code> is also specified, it takes precedence.</p>
<h3>scope</h3>
<p> Default: The scope of your current project, if any, otherwise none. </p>
<p> If specified, you will be logged out of the specified scope. See npm help <code>scope</code>. </p>
<dl>
<dt>
<dd>
<pre>
npm logout --scope=@myco
</pre>
</dl>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help adduser</p>
<dt>&bull;</p>
<dd> npm help registry</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help whoami </p>
</dl>
</dl>
<h2>Index</h2>
