---
title: "npm-tag(1)"
name: "npm-tag"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-tag/"
description: "npm-tag – Tag a published version"
---

<h2 class="name">NAME</h2>
<p> <code>npm-tag</code> &#8211; Tag a published version </p>
<h2>SYNOPSIS</h2>
<pre><code>
[DEPRECATED] npm tag&lt;name&gt; @&lt;version&gt;[&lt;tag&gt;] See `dist - tag`
</code></pre>
<h2>DESCRIPTION</h2>
<p> THIS COMMAND IS DEPRECATED. See npm help dist-tag for details. </p>
<p> Tags the specified version of the package with the specified tag, or the <code>&#8211;tag</code> config if not specified. </p>
<p> A tag can be used when installing packages as a reference to a version instead of using a specific version number:</p>
<dl>
<dt>
<dd>
<pre>
npm install &lt;name&gt;@&lt;tag&gt;
</pre>
<dt>
<dd></dl>
<p> When installing dependencies, a preferred tagged version may be specified:</p>
<dl>
<dt>
<dd>
<pre>
npm install --tag &lt;tag&gt;
</pre>
<dt>
<dd></dl>
<p> This also applies to <code>npm dedupe</code>. </p>
<p> Publishing a package always sets the &quot;latest&quot; tag to the published version.</p>
<h2>PURPOSE</h2>
<p> Tags can be used to provide an alias instead of version numbers. For example, <code>npm</code> currently uses the tag &quot;next&quot; to identify the upcoming version, and the tag &quot;latest&quot; to identify the current version. </p>
<p> A project might choose to have multiple streams of development, e.g., &quot;stable&quot;, &quot;canary&quot;.</p>
<h2>CAVEATS</h2>
<p> Tags must share a namespace with version numbers, because they are specified in the same slot: <code>npm install &lt;pkg&gt;@&lt;version&gt;</code> vs <code>npm install &lt;pkg&gt;@&lt;tag&gt;</code>. </p>
<p> Tags that can be interpreted as valid semver ranges will be rejected. For example, <code>v1.4</code> cannot be used as a tag, because it is interpreted by semver as <code>&gt;=1.4.0 &lt;1.5.0</code>. See <i><a rel="nofollow" href="https://github.com/npm/npm/issues/6082">https://github.com/npm/npm/issues/6082</a></i>. </p>
<p> The simplest way to avoid semver problems with tags is to use tags that do not begin with a number or the letter <code>v</code>.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> npm help publish</p>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help dedupe</p>
<dt>&bull;</p>
<dd> npm help 7 registry</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help 7 config</p>
<dt>&bull;</p>
<dd> npm apihelp tag</p>
<dt>&bull;</p>
<dd> npm help 5 npmrc</p>
<dt>
<dd>
</dl>
<h2>Index</h2>
