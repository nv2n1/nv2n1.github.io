---
title: "npm-org(1)"
name: "npm-org"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-org/"
description: "npm-org – Manage orgs"
---

<h2 class="name">NAME</h2>
<p> <code>npm-org</code> &#8211; Manage orgs </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm org set&lt;orgname&gt;&lt;username&gt;[developer | admin | owner] npm org rm&lt;orgname&gt;&lt;username&gt;
    npm org ls&lt;orgname&gt;[&lt;username&gt;]
</code></pre>
</dl>
<h3>Example</h3>
<p> Add a new developer to an org: </p>
<dl>
<dt>
<dd>
<pre>
$ npm org set my-org @mx-smith
</pre>
</dl>
<p> Add a new admin to an org (or change a developer to an admin): </p>
<dl>
<dt>
<dd>
<pre>
$ npm org set my-org @mx-santos admin
</pre>
</dl>
<p> Remove a user from an org: </p>
<dl>
<dt>
<dd>
<pre>
$ npm org rm my-org mx-santos
</pre>
</dl>
<p> List all users in an org: </p>
<dl>
<dt>
<dd>
<pre>
$ npm org ls my-org
</pre>
</dl>
<p> List all users in JSON format: </p>
<dl>
<dt>
<dd>
<pre>
$ npm org ls my-org --json
</pre>
</dl>
<p> See what role a user has in an org: </p>
<dl>
<dt>
<dd>
<pre>
$ npm org ls my-org @mx-santos
</pre>
</dl>
<h3>Description</h3>
<p> You can use the <code>npm org</code> commands to manage and view users of an organization. It supports adding and removing users, changing their roles, listing them, and finding specific ones and their roles.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation on npm Orgs <i><a rel="nofollow" href="https://docs.npmjs.com/orgs/">https://docs.npmjs.com/orgs/</a></i> </p>
</dl>
</dl>
<h2>Index</h2>
