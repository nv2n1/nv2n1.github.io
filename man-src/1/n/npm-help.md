---
title: "npm-help(1)"
name: "npm-help"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-help/"
description: "npm-help – Get help on npm"
---

<h2 class="name">NAME</h2>
<p> <code>npm-help</code> &#8211; Get help on npm </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm help &lt;term&gt; [&lt;terms..&gt;]
</pre>
</dd></dl>
<h3>Description</h3>
<p> If supplied a topic, then show the appropriate documentation page. </p>
<p> If the topic does not exist, or if multiple terms are provided, then run the <code>help-search</code> command to find a match. Note that, if <code>help-search</code> finds a single subject, then it will run <code>help</code> on that topic, so unique matches are equivalent to specifying a topic name.</p>
<h3>Configuration</h3>
<h3>viewer</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: &quot;man&quot; on Posix, &quot;browser&quot; on Windows</dd>
<dt>&bull;</dt>
<dd> Type: path </dd>
</dl>
</dl>
<p> The program to use to view help content. </p>
<p> Set to <code>&quot;browser&quot;</code> to view html help content in the default web browser.</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help npm</dd>
<dt>&bull;</dt>
<dd> npm help folders</dd>
<dt>&bull;</dt>
<dd> npm help config</dd>
<dt>&bull;</dt>
<dd> npm help npmrc</dd>
<dt>&bull;</dt>
<dd> npm help package.json</dd>
<dt>&bull;</dt>
<dd> npm help help-search </dd>
</dl>
</dl>
<h2>Index</h2>
