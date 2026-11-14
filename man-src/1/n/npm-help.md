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
<dd>
<pre>
npm help &lt;term&gt; [&lt;terms..&gt;]
</pre>
</dl>
<h3>Description</h3>
<p> If supplied a topic, then show the appropriate documentation page. </p>
<p> If the topic does not exist, or if multiple terms are provided, then run the <code>help-search</code> command to find a match. Note that, if <code>help-search</code> finds a single subject, then it will run <code>help</code> on that topic, so unique matches are equivalent to specifying a topic name.</p>
<h3>Configuration</h3>
<h3>viewer</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: &quot;man&quot; on Posix, &quot;browser&quot; on Windows</p>
<dt>&bull;</p>
<dd> Type: path </p>
</dl>
</dl>
<p> The program to use to view help content. </p>
<p> Set to <code>&quot;browser&quot;</code> to view html help content in the default web browser.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help npm</p>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc</p>
<dt>&bull;</p>
<dd> npm help package.json</p>
<dt>&bull;</p>
<dd> npm help help-search </p>
</dl>
</dl>
<h2>Index</h2>
