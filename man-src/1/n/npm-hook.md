---
title: "npm-hook(1)"
name: "npm-hook"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-hook/"
description: "npm-hook – Manage registry hooks"
---

<h2 class="name">NAME</h2>
<p> <code>npm-hook</code> &#8211; Manage registry hooks </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm hook ls[pkg] npm hook add&lt;entity&gt;&lt;url&gt;&lt;secret&gt;
    npm hook update&lt;id&gt;&lt;url&gt;[secret] npm hook rm&lt;id&gt;
</code></pre>
</dl>
<h3>Example</h3>
<p> Add a hook to watch a package for changes: </p>
<dl>
<dt>
<dd>
<pre>
$ npm hook add lodash <a rel="nofollow" href="https://example.com/">https://example.com/</a> my-shared-secret
</pre>
</dl>
<p> Add a hook to watch packages belonging to the user <code>substack</code>: </p>
<dl>
<dt>
<dd>
<pre>
$ npm hook add ~substack <a rel="nofollow" href="https://example.com/">https://example.com/</a> my-shared-secret
</pre>
</dl>
<p> Add a hook to watch packages in the scope <code>@npm</code> </p>
<dl>
<dt>
<dd>
<pre>
$ npm hook add @npm <a rel="nofollow" href="https://example.com/">https://example.com/</a> my-shared-secret
</pre>
</dl>
<p> List all your active hooks: </p>
<dl>
<dt>
<dd>
<pre>
$ npm hook ls
</pre>
</dl>
<p> List your active hooks for the <code>lodash</code> package: </p>
<dl>
<dt>
<dd>
<pre>
$ npm hook ls lodash
</pre>
</dl>
<p> Update an existing hook&#8217;s url: </p>
<dl>
<dt>
<dd>
<pre>
$ npm hook update id-deadbeef <a rel="nofollow" href="https://my-new-website.here/">https://my-new-website.here/</a>
</pre>
</dl>
<p> Remove a hook: </p>
<dl>
<dt>
<dd>
<pre>
$ npm hook rm id-deadbeef
</pre>
</dl>
<h3>Description</h3>
<p> Allows you to manage npm hooks <i><a rel="nofollow" href="https://blog.npmjs.org/post/145260155635/introducing-hooks-get-notifications-of-npm">https://blog.npmjs.org/post/145260155635/introducing-hooks-get-notifications-of-npm</a></i>, including adding, removing, listing, and updating. </p>
<p> Hooks allow you to configure URL endpoints that will be notified whenever a change happens to any of the supported entity types. Three different types of entities can be watched by hooks: packages, owners, and scopes. </p>
<p> To create a package hook, simply reference the package name. </p>
<p> To create an owner hook, prefix the owner name with <code>~</code> (as in, <code>~youruser</code>). </p>
<p> To create a scope hook, prefix the scope name with <code>@</code> (as in, <code>@yourscope</code>). </p>
<p> The hook <code>id</code> used by <code>update</code> and <code>rm</code> are the IDs listed in <code>npm hook ls</code> for that particular hook. </p>
<p> The shared secret will be sent along to the URL endpoint so you can verify the request came from your own configured hook.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> &quot;Introducing Hooks&quot; blog post <i><a rel="nofollow" href="https://blog.npmjs.org/post/145260155635/introducing-hooks-get-notifications-of-npm">https://blog.npmjs.org/post/145260155635/introducing-hooks-get-notifications-of-npm</a></i> </p>
</dl>
</dl>
<h2>Index</h2>
