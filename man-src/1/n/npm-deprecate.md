---
title: "npm-deprecate(1)"
name: "npm-deprecate"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-deprecate/"
description: "npm-deprecate – Deprecate a version of a package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-deprecate</code> &#8211; Deprecate a version of a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm deprecate &lt;pkg&gt;[@&lt;version&gt;] &lt;message&gt;
</pre>
</dl>
<h3>Description</h3>
<p> This command will update the npm registry entry for a package, providing a deprecation warning to all who attempt to install it. </p>
<p> It works on version ranges <i><a rel="nofollow" href="https://semver.npmjs.com/">https://semver.npmjs.com/</a></i> as well as specific versions, so you can do something like this: </p>
<dl>
<dt>
<dd>
<pre>
npm deprecate my-thing@&quot;&lt; 0.2.3&quot; &quot;critical bug fixed in v0.2.3&quot;
</pre>
</dl>
<p> Note that you must be the package owner to deprecate something. See the <code>owner</code> and <code>adduser</code> help topics. </p>
<p> To un-deprecate a package, specify an empty string (<code>&quot;&quot;</code>) for the <code>message</code> argument. Note that you must use double quotes with no space between them to format an empty string.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help publish</p>
<dt>&bull;</p>
<dd> npm help registry </p>
</dl>
</dl>
<h2>Index</h2>
