---
title: "npm-publish(1)"
name: "npm-publish"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-publish/"
description: "npm-publish – Publish a package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-publish</code> &#8211; Publish a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm publish[&lt;tarball&gt; | &lt;folder&gt;][--tag&lt;tag&gt;][--access&lt;public | restricted&gt;][--otp otpcode][--dry - run] Publishes '.' if no argument supplied
    Sets tag 'latest' if no-- tag specified
</code></pre>
</dl>
<h3>Description</h3>
<p> Publishes a package to the registry so that it can be installed by name. All files in the package directory are included if no local <code>.gitignore</code> or <code>.npmignore</code> file exists. If both files exist and a file is ignored by <code>.gitignore</code> but not by <code>.npmignore</code> then it will be included. See npm help <code>developers</code> for full details on what&#8217;s included in the published package, as well as details on how the package is built. </p>
<p> By default npm will publish to the public registry. This can be overridden by specifying a different default registry or using a npm help <code>scope</code> in the name (see npm help <code>package.json</code>).</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>&lt;folder&gt;</code>: A folder containing a package.json file</p>
<dt>&bull;</p>
<dd> <code>&lt;tarball&gt;</code>: A url or file path to a gzipped tar archive containing a single folder with a package.json file inside.</p>
<dt>&bull;</p>
<dd> <code>[&#8211;tag &lt;tag&gt;]</code> Registers the published package with the given tag, such that <code>npm install &lt;name&gt;@&lt;tag&gt;</code> will install this version. By default, <code>npm publish</code> updates and <code>npm install</code> installs the <code>latest</code> tag. See <code>npm-dist-tag</code> <i>npm-dist-tag</i> for details about tags.</p>
<dt>&bull;</p>
<dd> <code>[&#8211;access &lt;public|restricted&gt;]</code> Tells the registry whether this package should be published as public or restricted. Only applies to scoped packages, which default to <code>restricted</code>. If you don&#8217;t have a paid account, you must publish with <code>&#8211;access public</code> to publish scoped packages.</p>
<dt>&bull;</p>
<dd> <code>[&#8211;otp &lt;otpcode&gt;]</code> If you have two-factor authentication enabled in <code>auth-and-writes</code> mode then you can provide a code from your authenticator with this. If you don&#8217;t include this and you&#8217;re running from a TTY then you&#8217;ll be prompted.</p>
<dt>&bull;</p>
<dd> <code>[&#8211;dry-run]</code> As of <code>npm@6</code>, does everything publish would do except actually publishing to the registry. Reports the details of what would have been published. </p>
</dl>
</dl>
<p> Fails if the package name and version combination already exists in the specified registry. </p>
<p> Once a package is published with a given name and version, that specific name and version combination can never be used again, even if it is removed with npm help <code>unpublish</code>. </p>
<p> As of <code>npm@5</code>, both a sha1sum and an integrity field with a sha512sum of the tarball will be submitted to the registry during publication. Subsequent installs will use the strongest supported algorithm to verify downloads. </p>
<p> Similar to <code>&#8211;dry-run</code> see npm help <code>pack</code>, which figures out the files to be included and packs them into a tarball to be uploaded to the registry.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help registry</p>
<dt>&bull;</p>
<dd> npm help scope</p>
<dt>&bull;</p>
<dd> npm help adduser</p>
<dt>&bull;</p>
<dd> npm help owner</p>
<dt>&bull;</p>
<dd> npm help deprecate</p>
<dt>&bull;</p>
<dd> npm help dist-tag</p>
<dt>&bull;</p>
<dd> npm help pack</p>
<dt>&bull;</p>
<dd> npm help profile </p>
</dl>
</dl>
<h2>Index</h2>
