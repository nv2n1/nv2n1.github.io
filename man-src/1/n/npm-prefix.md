---

title: "npm-prefix(1)"
name: "npm-prefix"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-prefix/"
description: "npm-prefix – Display prefix"
---

<p> <code>npm-prefix</code> &#8211; Display prefix </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm prefix [-g]
</pre>
</dd></dl>
<h3>Description</h3>
<p> Print the local prefix to standard out. This is the closest parent directory to contain a <code>package.json</code> file or <code>node_modules</code> directory, unless <code>-g</code> is also specified. </p>
<p> If <code>-g</code> is specified, this will be the value of the global prefix. See npm help <code>config</code> for more detail.</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help root</dd>
<dt>&bull;</dt>
<dd> npm help bin</dd>
<dt>&bull;</dt>
<dd> npm help folders</dd>
<dt>&bull;</dt>
<dd> npm help config</dd>
<dt>&bull;</dt>
<dd> npm help npmrc </dd>
</dl>
</dl>
