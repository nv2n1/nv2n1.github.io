---
title: "npm-owner(1)"
name: "npm-owner"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-owner/"
description: "npm-owner – Manage package owners"
---

<h2 class="name">NAME</h2>
<p> <code>npm-owner</code> &#8211; Manage package owners </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm owner add&lt;user&gt;[&lt;@scope&gt; / ]&lt;pkg&gt;
    npm owner rm&lt;user&gt;[&lt;@scope&gt; / ]&lt;pkg&gt;
        npm owner ls[&lt;@scope&gt; / ]&lt;pkg&gt;
            aliases : author
</code></pre>
</dl>
<h3>Description</h3>
<p> Manage ownership of published packages.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> ls: List all the users who have access to modify a package and push new versions. Handy when you need to know who to bug for help.</p>
<dt>&bull;</p>
<dd> add: Add a new user as a maintainer of a package. This user is enabled to modify metadata, publish new versions, and add other owners.</p>
<dt>&bull;</p>
<dd> rm: Remove a user from the package owner list. This immediately revokes their privileges. </p>
</dl>
</dl>
<p> Note that there is only one level of access. Either you can modify a package, or you can&#8217;t. Future versions may contain more fine-grained access levels, but that is not implemented at this time. </p>
<p> If you have two-factor authentication enabled with <code>auth-and-writes</code> then you&#8217;ll need to include an otp on the command line when changing ownership with <code>&#8211;otp</code>.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help publish</p>
<dt>&bull;</p>
<dd> npm help registry</p>
<dt>&bull;</p>
<dd> npm help adduser</p>
<dt>&bull;</p>
<dd> npm help disputes </p>
</dl>
</dl>
<h2>Index</h2>
