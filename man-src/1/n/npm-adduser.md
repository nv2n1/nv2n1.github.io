---
title: "npm-adduser(1)"
name: "npm-adduser"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-adduser/"
description: "npm-adduser – Add a registry user account"
---

<h2 class="name">NAME</h2>
<p> <code>npm-adduser</code> &#8211; Add a registry user account </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm adduser[--registry = url][--scope = @orgname][--always - auth][--auth - type = legacy] aliases : login, add - user
</code></pre>
</dl>
<h3>Description</h3>
<p> Create or verify a user named <code>&lt;username&gt;</code> in the specified registry, and save the credentials to the <code>.npmrc</code> file. If no registry is specified, the default registry will be used (see npm help <code>config</code>). </p>
<p> The username, password, and email are read in from prompts. </p>
<p> To reset your password, go to <a rel="nofollow" href="https://www.npmjs.com/forgot">https://www.npmjs.com/forgot</a> </p>
<p> To change your email address, go to <a rel="nofollow" href="https://www.npmjs.com/email-edit">https://www.npmjs.com/email-edit</a> </p>
<p> You may use this command multiple times with the same user account to authorize on a new machine. When authenticating on a new machine, the username, password and email address must all match with your existing record. </p>
<p> <code>npm login</code> is an alias to <code>adduser</code> and behaves exactly the same way.</p>
<h3>Configuration</h3>
<h3>registry</h3>
<p> Default: <a rel="nofollow" href="https://registry.npmjs.org/">https://registry.npmjs.org/</a> </p>
<p> The base URL of the npm package registry. If <code>scope</code> is also specified, this registry will only be used for packages with that scope. <code>scope</code> defaults to the scope of the project directory you&#8217;re currently in, if any. See npm help <code>scope</code>.</p>
<h3>scope</h3>
<p> Default: none </p>
<p> If specified, the user and login credentials given will be associated with the specified scope. See npm help <code>scope</code>. You can use both at the same time, e.g. </p>
<dl>
<dt>
<dd>
<pre>
    npm adduser --registry=<a rel="nofollow" href="http://myregistry.example.com">http://myregistry.example.com</a> --scope=@myco
</pre>
</dl>
<p> This will set a registry for the given scope and login or create a user for that registry at the same time.</p>
<h3>always-auth</h3>
<p> Default: false </p>
<p> If specified, save configuration indicating that all requests to the given registry should include authorization information. Useful for private registries. Can be used with <code>&#8211;registry</code> and / or <code>&#8211;scope</code>, e.g. </p>
<dl>
<dt>
<dd>
<pre>
    npm adduser --registry=<a rel="nofollow" href="http://private-registry.example.com">http://private-registry.example.com</a> --always-auth
</pre>
</dl>
<p> This will ensure that all requests to that registry (including for tarballs) include an authorization header. This setting may be necessary for use with private registries where metadata and package tarballs are stored on hosts with different hostnames. See <code>always-auth</code> in npm help <code>config</code> for more details on always-auth. Registry-specific configuration of <code>always-auth</code> takes precedence over any global configuration.</p>
<h3>auth-type</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: <code>&#8216;legacy&#8217;</code></p>
<dt>&bull;</p>
<dd> Type: <code>&#8216;legacy&#8217;</code>, <code>&#8216;sso&#8217;</code>, <code>&#8216;saml&#8217;</code>, <code>&#8216;oauth&#8217;</code> </p>
</dl>
</dl>
<p> What authentication strategy to use with <code>adduser</code>/<code>login</code>. Some npm registries (for example, npmE) might support alternative auth strategies besides classic username/password entry in legacy npm.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help registry</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc</p>
<dt>&bull;</p>
<dd> npm help owner</p>
<dt>&bull;</p>
<dd> npm help whoami </p>
</dl>
</dl>
<h2>Index</h2>
