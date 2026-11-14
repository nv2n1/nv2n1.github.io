---
title: "npm-dist-tag(1)"
name: "npm-dist-tag"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-dist-tag/"
description: "npm-dist-tag – Modify package distribution tags"
---

<h2 class="name">NAME</h2>
<p> <code>npm-dist-tag</code> &#8211; Modify package distribution tags </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm dist - tag add&lt;pkg&gt; @&lt;version&gt;[&lt;tag&gt;] npm dist - tag rm&lt;pkg&gt;&lt;tag&gt; npm dist - tag ls[&lt;pkg&gt;] aliases : dist - tags
</code></pre>
</dl>
<h3>Description</h3>
<p> Add, remove, and enumerate distribution tags on a package:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> add: Tags the specified version of the package with the specified tag, or the <code>&#8211;tag</code> config if not specified. If you have two-factor authentication on auth-and-writes then you’ll need to include a one-time password on the command line with <code>&#8211;otp &lt;one-time password&gt;</code>.</p>
<dt>&bull;</p>
<dd> rm: Clear a tag that is no longer in use from the package.</p>
<dt>&bull;</p>
<dd> ls: Show all of the dist-tags for a package, defaulting to the package in the current prefix. This is the default action if none is specified. </p>
</dl>
</dl>
<p> A tag can be used when installing packages as a reference to a version instead of using a specific version number: </p>
<dl>
<dt>
<dd>
<pre>
npm install &lt;name&gt;@&lt;tag&gt;
</pre>
</dl>
<p> When installing dependencies, a preferred tagged version may be specified: </p>
<dl>
<dt>
<dd>
<pre>
npm install --tag &lt;tag&gt;
</pre>
</dl>
<p> This also applies to <code>npm dedupe</code>. </p>
<p> Publishing a package sets the <code>latest</code> tag to the published version unless the <code>&#8211;tag</code> option is used. For example, <code>npm publish &#8211;tag=beta</code>. </p>
<p> By default, <code>npm install &lt;pkg&gt;</code> (without any <code>@&lt;version&gt;</code> or <code>@&lt;tag&gt;</code> specifier) installs the <code>latest</code> tag.</p>
<h3>Purpose</h3>
<p> Tags can be used to provide an alias instead of version numbers. </p>
<p> For example, a project might choose to have multiple streams of development and use a different tag for each stream, e.g., <code>stable</code>, <code>beta</code>, <code>dev</code>, <code>canary</code>. </p>
<p> By default, the <code>latest</code> tag is used by npm to identify the current version of a package, and <code>npm install &lt;pkg&gt;</code> (without any <code>@&lt;version&gt;</code> or <code>@&lt;tag&gt;</code> specifier) installs the <code>latest</code> tag. Typically, projects only use the <code>latest</code> tag for stable release versions, and use other tags for unstable versions such as prereleases. </p>
<p> The <code>next</code> tag is used by some projects to identify the upcoming version. </p>
<p> By default, other than <code>latest</code>, no tag has any special significance to npm itself.</p>
<h3>Caveats</h3>
<p> This command used to be known as <code>npm tag</code>, which only created new tags, and so had a different syntax. </p>
<p> Tags must share a namespace with version numbers, because they are specified in the same slot: <code>npm install &lt;pkg&gt;@&lt;version&gt;</code> vs <code>npm install &lt;pkg&gt;@&lt;tag&gt;</code>. </p>
<p> Tags that can be interpreted as valid semver ranges will be rejected. For example, <code>v1.4</code> cannot be used as a tag, because it is interpreted by semver as <code>&gt;=1.4.0 &lt;1.5.0</code>. See <a rel="nofollow" href="https://github.com/npm/npm/issues/6082.">https://github.com/npm/npm/issues/6082.</a> </p>
<p> The simplest way to avoid semver problems with tags is to use tags that do not begin with a number or the letter <code>v</code>.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help publish</p>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help dedupe</p>
<dt>&bull;</p>
<dd> npm help registry</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc </p>
</dl>
</dl>
<h2>Index</h2>
