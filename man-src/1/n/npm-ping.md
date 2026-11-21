---
title: "npm-ping(1)"
name: "npm-ping"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-ping/"
description: "npm-ping – Ping npm registry"
---

<h2 class="name">NAME</h2>
<p> <code>npm-ping</code> &#8211; Ping npm registry </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm ping [--registry &lt;registry&gt;]
</pre>
</dd></dl>
<h3>Description</h3>
<p> Ping the configured or given npm registry and verify authentication. If it works it will output something like: </p>
<dl>
<dt>
</dt><dd>
<pre>
Ping success: {*Details about registry*}
</pre>
</dd></dl>
<p> otherwise you will get: </p>
<dl>
<dt>
</dt><dd>
<pre>
Ping error: {*Detail about error}
</pre>
</dd></dl>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help config</dd>
<dt>&bull;</dt>
<dd> npm help npmrc </dd>
</dl>
</dl>
