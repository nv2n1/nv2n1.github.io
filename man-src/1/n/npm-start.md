---
title: "npm-start(1)"
name: "npm-start"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-start/"
description: "npm-start – Start a package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-start</code> &#8211; Start a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm start [-- &lt;args&gt;]
</pre>
</dd></dl>
<h3>Description</h3>
<p> This runs an arbitrary command specified in the package&#8217;s <code>&quot;start&quot;</code> property of its <code>&quot;scripts&quot;</code> object. If no <code>&quot;start&quot;</code> property is specified on the <code>&quot;scripts&quot;</code> object, it will run <code>node server.js</code>. </p>
<p> As of <code>npm [at] 2.0.0</code> <i><a rel="nofollow" href="https://blog.npmjs.org/post/98131109725/npm-2-0-0">https://blog.npmjs.org/post/98131109725/npm-2-0-0</a></i>, you can use custom arguments when executing scripts. Refer to npm help <code>run-script</code> for more details.</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help run-script</dd>
<dt>&bull;</dt>
<dd> npm help scripts</dd>
<dt>&bull;</dt>
<dd> npm help test</dd>
<dt>&bull;</dt>
<dd> npm help restart</dd>
<dt>&bull;</dt>
<dd> npm help stop </dd>
</dl>
</dl>
<h2>Index</h2>
