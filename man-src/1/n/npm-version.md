---
title: "npm-version(1)"
name: "npm-version"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-version/"
description: "npm-version – Bump a package version"
---

<h2 class="name">NAME</h2>
<p> <code>npm-version</code> &#8211; Bump a package version </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm version[&lt;newversion&gt; | major | minor | patch | premajor | preminor | prepatch | prerelease[--preid = &lt;prerelease - id&gt;] | from - git] 'npm [-v | --version]' to print npm version 'npm view &lt;pkg&gt; version' to view a package's published version 'npm ls' to inspect current package / dependency versions
</code></pre>
</dl>
<h3>Description</h3>
<p> Run this in a package directory to bump the version and write the new data back to <code>package.json</code>, <code>package-lock.json</code>, and, if present, <code>npm-shrinkwrap.json</code>. </p>
<p> The <code>newversion</code> argument should be a valid semver string, a valid second argument to semver.inc <i><a rel="nofollow" href="https://github.com/npm/node-semver#functions">https://github.com/npm/node-semver#functions</a></i> (one of <code>patch</code>, <code>minor</code>, <code>major</code>, <code>prepatch</code>, <code>preminor</code>, <code>premajor</code>, <code>prerelease</code>), or <code>from-git</code>. In the second case, the existing version will be incremented by 1 in the specified field. <code>from-git</code> will try to read the latest git tag, and use that as the new npm version. </p>
<p> If run in a git repo, it will also create a version commit and tag. This behavior is controlled by <code>git-tag-version</code> (see below), and can be disabled on the command line by running <code>npm &#8211;no-git-tag-version version</code>. It will fail if the working directory is not clean, unless the <code>-f</code> or <code>&#8211;force</code> flag is set. </p>
<p> If supplied with <code>-m</code> or <code>&#8211;message</code> config option, npm will use it as a commit message when creating a version commit. If the <code>message</code> config contains <code>%s</code> then that will be replaced with the resulting version number. For example: </p>
<dl>
<dt>
<dd>
<pre>
npm version patch -m &quot;Upgrade to %s for reasons&quot;
</pre>
</dl>
<p> If the <code>sign-git-tag</code> config is set, then the tag will be signed using the <code>-s</code> flag to git. Note that you must have a default GPG key set up in your git config for this to work properly. For example: </p>
<dl>
<dt>
<dd>
<pre>
$ npm config set sign-git-tag true
$ npm version patch
You need a passphrase to unlock the secret key for
user: &quot;isaacs (<a rel="nofollow" href="http://blog.izs.me/)">http://blog.izs.me/)</a> &lt;i@izs.me&gt;&quot;
2048-bit RSA key, ID 6C481CF6, created 2010-08-31
Enter passphrase:
</pre>
</dl>
<p> If <code>preversion</code>, <code>version</code>, or <code>postversion</code> are in the <code>scripts</code> property of the package.json, they will be executed as part of running <code>npm version</code>. </p>
<p> The exact order of execution is as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Check to make sure the git working directory is clean before we get started. Your scripts may add files to the commit in future steps. This step is skipped if the <code>&#8211;force</code> flag is set.</p>
<dt>2.</p>
<dd> Run the <code>preversion</code> script. These scripts have access to the old <code>version</code> in package.json. A typical use would be running your full test suite before deploying. Any files you want added to the commit should be explicitly added using <code>git add</code>.</p>
<dt>3.</p>
<dd> Bump <code>version</code> in <code>package.json</code> as requested (<code>patch</code>, <code>minor</code>, <code>major</code>, etc).</p>
<dt>4.</p>
<dd> Run the <code>version</code> script. These scripts have access to the new <code>version</code> in package.json (so they can incorporate it into file headers in generated files for example). Again, scripts should explicitly add generated files to the commit using <code>git add</code>.</p>
<dt>5.</p>
<dd> Commit and tag.</p>
<dt>6.</p>
<dd> Run the <code>postversion</code> script. Use it to clean up the file system or automatically push the commit and/or tag. </p>
</dl>
</dl>
<p> Take the following example: </p>
<dl>
<dt>
<dd>
<pre><code>
"scripts":
{
    "preversion" : "npm test",
                   "version" : "npm run build &amp;&amp; git add -A dist",
                               "postversion" : "git push &amp;&amp; git push --tags &amp;&amp; rm -rf build/temp"
}
</code></pre>
</dl>
<p> This runs all your tests, and proceeds only if they pass. Then runs your <code>build</code> script, and adds everything in the <code>dist</code> directory to the commit. After the commit, it pushes the new commit and tag up to the server, and deletes the <code>build/temp</code> directory.</p>
<h3>Configuration</h3>
<h3>allow-same-version</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: false</p>
<dt>&bull;</p>
<dd> Type: Boolean </p>
</dl>
</dl>
<p> Prevents throwing an error when <code>npm version</code> is used to set the new version to the same value as the current version.</p>
<h3>git-tag-version</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: true</p>
<dt>&bull;</p>
<dd> Type: Boolean </p>
</dl>
</dl>
<p> Commit and tag the version change.</p>
<h3>commit-hooks</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: true</p>
<dt>&bull;</p>
<dd> Type: Boolean </p>
</dl>
</dl>
<p> Run git commit hooks when committing the version change.</p>
<h3>sign-git-tag</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: false</p>
<dt>&bull;</p>
<dd> Type: Boolean </p>
</dl>
</dl>
<p> Pass the <code>-s</code> flag to git to sign the tag. </p>
<p> Note that you must have a default GPG key set up in your git config for this to work properly.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help init</p>
<dt>&bull;</p>
<dd> npm help run-script</p>
<dt>&bull;</p>
<dd> npm help scripts</p>
<dt>&bull;</p>
<dd> npm help package.json</p>
<dt>&bull;</p>
<dd> npm help semver</p>
<dt>&bull;</p>
<dd> npm help config </p>
</dl>
</dl>
<h2>Index</h2>
