---
title: "npm-access(1)"
name: "npm-access"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-access/"
description: "npm-access – Set access level on published packages"
---

<h2 class="name">NAME</h2>
<p> <code>npm-access</code> &#8211; Set access level on published packages </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm access public[&lt;package&gt;] npm access restricted[&lt;package&gt;] npm access grant&lt;read - only | read - write&gt;&lt;scope : team&gt;[&lt;package&gt;] npm access revoke&lt;scope : team&gt;[&lt;package&gt;] npm access 2fa - required[&lt;package&gt;] npm access 2fa - not -required[&lt;package&gt;] npm access ls - packages [&lt;user&gt; | &lt;scope&gt; | &lt; scope:team &gt; ] npm access ls - collaborators[&lt;package&gt;[&lt;user&gt;]] npm access edit[&lt;package&gt;]
</code></pre>
</dl>
<h3>Description</h3>
<p> Used to set access controls on private packages. </p>
<p> For all of the subcommands, <code>npm access</code> will perform actions on the packages in the current working directory if no package name is passed to the subcommand.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> public / restricted: Set a package to be either publicly accessible or restricted.</p>
<dt>&bull;</p>
<dd> grant / revoke: Add or remove the ability of users and teams to have read-only or read-write access to a package.</p>
<dt>&bull;</p>
<dd> 2fa-required / 2fa-not-required: Configure whether a package requires that anyone publishing it have two-factor authentication enabled on their account.</p>
<dt>&bull;</p>
<dd> ls-packages: Show all of the packages a user or a team is able to access, along with the access level, except for read-only public packages (it won&#8217;t print the whole registry listing)</p>
<dt>&bull;</p>
<dd> ls-collaborators: Show all of the access privileges for a package. Will only show permissions for packages to which you have at least read access. If <code>&lt;user&gt;</code> is passed in, the list is filtered only to teams <i>that</i> user happens to belong to.</p>
<dt>&bull;</p>
<dd> edit: Set the access privileges for a package at once using <code>$EDITOR</code>. </p>
</dl>
</dl>
<h3>Details</h3>
<p> <code>npm access</code> always operates directly on the current registry, configurable from the command line using <code>&#8211;registry=&lt;registry url&gt;</code>. </p>
<p> Unscoped packages are <i>always public</i>. </p>
<p> Scoped packages <i>default to restricted</i>, but you can either publish them as public using <code>npm publish &#8211;access=public</code>, or set their access as public using <code>npm access public</code> after the initial publish. </p>
<p> You must have privileges to set the access of a package:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> You are an owner of an unscoped or scoped package.</p>
<dt>&bull;</p>
<dd> You are a member of the team that owns a scope.</p>
<dt>&bull;</p>
<dd> You have been given read-write privileges for a package, either as a member of a team or directly as an owner. </p>
</dl>
</dl>
<p> If you have two-factor authentication enabled then you&#8217;ll have to pass in an otp with <code>&#8211;otp</code> when making access changes. </p>
<p> If your account is not paid, then attempts to publish scoped packages will fail with an HTTP 402 status code (logically enough), unless you use <code>&#8211;access=public</code>. </p>
<p> Management of teams and team memberships is done with the <code>npm team</code> command.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>libnpmaccess</code> <i><a rel="nofollow" href="https://npm.im/libnpmaccess">https://npm.im/libnpmaccess</a></i></p>
<dt>&bull;</p>
<dd> npm help team</p>
<dt>&bull;</p>
<dd> npm help publish</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help registry </p>
</dl>
</dl>
<h2>Index</h2>
