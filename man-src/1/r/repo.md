---

title: "repo(1)"
name: "repo"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repo/"
description: "npm-repo – Open package repository page in the browser"
---

<p> <code>npm-repo</code> &#8211; Open package repository page in the browser </p>
<h2>SYNOPSIS</h2>
<pre>
npm repo &lt;pkgname&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> This command tries to guess at the likely location of a package&#8217;s repository URL, and then tries to open it using the <code>&#8211;browser</code> config param.</p>
<h2>CONFIGURATION</h2>
<h3>browser</h3>
<dl>
<dt>&bull;</dt>
<dd> Default: OS X: <code>&quot;open&quot;</code>, Windows: <code>&quot;start&quot;</code>, Others: <code>&quot;xdg-open&quot;</code></dd>
<dt>&bull;</dt>
<dd> Type: String</dd>
</dl>
<p> The browser that is called by the <code>npm repo</code> command to open websites.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> npm help docs</dd>
<dt>&bull;</dt>
<dd> npm help config</dd>
</dl>
