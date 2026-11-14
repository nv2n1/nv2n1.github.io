---
title: "npm-help-search(1)"
name: "npm-help-search"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-help-search/"
description: "npm-help-search – Search npm help documentation"
---

<h2 class="name">NAME</h2>
<p> <code>npm-help-search</code> &#8211; Search npm help documentation </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm help-search &lt;text&gt;
</pre>
</dl>
<h3>Description</h3>
<p> This command will search the npm markdown documentation files for the terms provided, and then list the results, sorted by relevance. </p>
<p> If only one result is found, then it will show that help topic. </p>
<p> If the argument to <code>npm help</code> is not a known help topic, then it will call <code>help-search</code>. It is rarely if ever necessary to call this command directly.</p>
<h3>Configuration</h3>
<h3>long</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Type: Boolean</p>
<dt>&bull;</p>
<dd> Default: false </p>
</dl>
</dl>
<p> If true, the &quot;long&quot; flag will cause help-search to output context around where the terms were found in the documentation. </p>
<p> If false, then help-search will just list out the help topics found.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help npm</p>
<dt>&bull;</p>
<dd> npm help help </p>
</dl>
</dl>
<h2>Index</h2>
