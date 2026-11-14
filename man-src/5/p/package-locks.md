---
title: "package-locks(5)"
name: "package-locks"
section: "5"
letter: "p"
url: "/docs/linux/man/5-package-locks/"
description: "package-locks – An explanation of npm lockfiles"
---

<p><code>package-locks</code> &#8211; An explanation of npm lockfiles</p>
<h3>Description</h3>
<p>Conceptually, the &quot;input&quot; to npm help <code>install</code> is a npm help package.json, while its &quot;output&quot; is a fully-formed <code>node_modules</code> tree: a representation of the dependencies you declared. In an ideal world, npm would work like a pure function: the same <code>package.json</code> should produce the exact same <code>node_modules</code> tree, any time. In some cases, this is indeed true. But in many others, npm is unable to do this. There are multiple reasons for this:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>different versions of npm (or other package managers) may have been used to install a package, each using slightly different installation algorithms.</p>
<dt>&bull;</p>
<dd>a new version of a direct semver-range package may have been published since the last time your packages were installed, and thus a newer version will be used.</p>
<dt>&bull;</p>
<dd>A dependency of one of your dependencies may have published a new version, which will update even if you used pinned dependency specifiers (<code>1.2.3</code> instead of <code>^1.2.3</code>)</p>
<dt>&bull;</p>
<dd>The registry you installed from is no longer available, or allows mutation of versions (unlike the primary npm registry), and a different version of a package exists under the same version number now.  As an example, consider package A: </p>
<pre><code>{
    &quot;name&quot;: &quot;A&quot;,
    &quot;version&quot;: &quot;0.1.0&quot;,
    &quot;dependencies&quot;: {
        &quot;B&quot;: &quot;&lt;0.1.0&quot;
    }
}</code></pre>
<p> package B: {<br />
    &quot;name&quot;: &quot;B&quot;,<br />
    &quot;version&quot;: &quot;0.0.1&quot;,<br />
    &quot;dependencies&quot;: {<br />
        &quot;C&quot;: &quot;&lt;0.1.0&quot;<br />
    }<br />
} and package C: {<br />
    &quot;name&quot;: &quot;C&quot;,<br />
    &quot;version&quot;: &quot;0.0.1&quot;<br />
} If these are the only versions of A, B, and C available in the registry, then a normal <code>npm install A</code> will install:</p>
<dl>
<dd>
<pre>A@0.1.0
`-- B@0.0.1
 `-- C@0.0.1</pre>
</dl>
<p> However, if B@0.0.2 is published, then a fresh <code>npm install A</code> will install:</p>
<dl>
<dd>
<pre>A@0.1.0
`-- B@0.0.2
 `-- C@0.0.1</pre>
</dl>
<p> assuming the new version did not modify B&#8217;s dependencies. Of course, the new version of B could include a new version of C and any number of new dependencies. If such changes are undesirable, the author of A could specify a dependency on B@0.0.1. However, if A&#8217;s author and B&#8217;s author are not the same person, there&#8217;s no way for A&#8217;s author to say that he or she does not want to pull in newly published versions of C when B hasn&#8217;t changed at all. To prevent this potential issue, npm uses npm help package-lock.json or, if present, npm help npm-shrinkwrap.json. These files are called package locks, or lockfiles. Whenever you run <code>npm install</code>, npm generates or updates your package lock, which will look something like this: </p>
<pre><code>{
    &quot;name&quot;: &quot;A&quot;,
    &quot;version&quot;: &quot;0.1.0&quot;,
    ...metadata fields...
    &quot;dependencies&quot;: {
        &quot;B&quot;: {
            &quot;version&quot;: &quot;0.0.1&quot;,
            &quot;resolved&quot;: &quot;https://registry.npmjs.org/B/-/B-0.0.1.tgz&quot;,
            &quot;integrity&quot;: &quot;sha512-DeAdb33F+&quot;
            &quot;dependencies&quot;: {
                &quot;C&quot;: {
                    &quot;version&quot;: &quot;git://github.com/org/C.git#5c380ae319fc4efe9e7f2d9c78b0faa588fd99b4&quot;
                }
            }
        }
    }
}</code></pre>
<p> This file describes an <i>exact</i>, and more importantly <i>reproducible</i> <code>node_modules</code> tree. Once it&#8217;s present, any future installation will base its work off this file, instead of recalculating dependency versions off npm help package.json. The presence of a package lock changes the installation behavior such that:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>The module tree described by the package lock is reproduced. This means reproducing the structure described in the file, using the specific files referenced in &quot;resolved&quot; if available, falling back to normal package resolution using &quot;version&quot; if one isn&#8217;t.</p>
<dt>2.</p>
<dd>The tree is walked and any missing dependencies are installed in the usual fashion.  If <code>preshrinkwrap</code>, <code>shrinkwrap</code> or <code>postshrinkwrap</code> are in the <code>scripts</code> property of the <code>package.json</code>, they will be executed in order. <code>preshrinkwrap</code> and <code>shrinkwrap</code> are executed before the shrinkwrap, <code>postshrinkwrap</code> is executed afterwards. These scripts run for both <code>package-lock.json</code> and <code>npm-shrinkwrap.json</code>. For example to run some postprocessing on the generated file:</p>
<dl>
<dd>
<pre> &quot;scripts&quot;: {
 &quot;postshrinkwrap&quot;: &quot;json -I -e \&quot;this.myMetadata = $MY_APP_METADATA\&quot;&quot;
 }</pre>
</dl>
<h3>Using locked packages</h3>
<p>Using a locked package is no different than using any package without a package lock: any commands that update <code>node_modules</code> and/or <code>package.json</code>&#8216;s dependencies will automatically sync the existing lockfile. This includes <code>npm install</code>, <code>npm rm</code>, <code>npm update</code>, etc. To prevent this update from happening, you can use the <code>&#8211;no-save</code> option to prevent saving altogether, or <code>&#8211;no-shrinkwrap</code> to allow <code>package.json</code> to be updated while leaving <code>package-lock.json</code> or <code>npm-shrinkwrap.json</code> intact. It is highly recommended you commit the generated package lock to source control: this will allow anyone else on your team, your deployments, your CI/continuous integration, and anyone else who runs <code>npm install</code> in your package source to get the exact same dependency tree that you were developing on. Additionally, the diffs from these changes are human-readable and will inform you of any changes npm has made to your <code>node_modules</code>, so you can notice if any transitive dependencies were updated, hoisted, etc.</p>
<h3>Resolving lockfile conflicts</h3>
<p>Occasionally, two separate npm install will create package locks that cause merge conflicts in source control systems. As of <code>npm [at] 5.7.0</code>, these conflicts can be resolved by manually fixing any <code>package.json</code> conflicts, and then running <code>npm install [&#8211;package-lock-only]</code> again. npm will automatically resolve any conflicts for you and write a merged package lock that includes all the dependencies from both branches in a reasonable tree. If <code>&#8211;package-lock-only</code> is provided, it will do this without also modifying your local <code>node_modules/</code>. To make this process seamless on git, consider installing <code>npm-merge-driver</code> <i><a rel="nofollow" href="https://npm.im/npm-merge-driver">https://npm.im/npm-merge-driver</a></i>, which will teach git how to do this itself without any user interaction. In short: <code>$ npx npm-merge-driver install -g</code> will let you do this, and even works with pre-<code>npm [at] 5.7.0</code> versions of npm 5, albeit a bit more noisily. Note that if <code>package.json</code> itself conflicts, you will have to resolve that by hand and run <code>npm install</code> manually, even with the merge driver.</p>
<h3>See Also</h3>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><a rel="nofollow" href="https://medium.com/@sdboyer/so-you-want-to-write-a-package-manager-4ae9c17d9527">https://medium.com/@sdboyer/so-you-want-to-write-a-package-manager-4ae9c17d9527</a></p>
<dt>&bull;</p>
<dd>npm help package.json</p>
<dt>&bull;</p>
<dd>npm help package-lock.json</p>
<dt>&bull;</p>
<dd>npm help shrinkwrap.json</p>
<dt>&bull;</p>
<dd>npm help shrinkwrap </p>
