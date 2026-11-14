---
title: "npm-doctor(1)"
name: "npm-doctor"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-doctor/"
description: "npm-doctor – Check your environments"
---

<h2 class="name">NAME</h2>
<p> <code>npm-doctor</code> &#8211; Check your environments </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm doctor
</pre>
</dl>
<h3>Description</h3>
<p> <code>npm doctor</code> runs a set of checks to ensure that your npm installation has what it needs to manage your JavaScript packages. npm is mostly a standalone tool, but it does have some basic requirements that must be met:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Node.js and git must be executable by npm.</p>
<dt>&bull;</p>
<dd> The primary npm registry, <code>registry.npmjs.com</code>, or another service that uses the registry API, is available.</p>
<dt>&bull;</p>
<dd> The directories that npm uses, <code>node_modules</code> (both locally and globally), exist and can be written by the current user.</p>
<dt>&bull;</p>
<dd> The npm cache exists, and the package tarballs within it aren&#8217;t corrupt. </p>
</dl>
</dl>
<p> Without all of these working properly, npm may not work properly. Many issues are often attributable to things that are outside npm&#8217;s code base, so <code>npm doctor</code> confirms that the npm installation is in a good state. </p>
<p> Also, in addition to this, there are also very many issue reports due to using old versions of npm. Since npm is constantly improving, running <code>npm [at] latest</code> is better than an old version. </p>
<p> <code>npm doctor</code> verifies the following items in your environment, and if there are any recommended changes, it will display them.</p>
<h3><code>npm ping</code></h3>
<p> By default, npm installs from the primary npm registry, <code>registry.npmjs.org</code>. <code>npm doctor</code> hits a special ping endpoint within the registry. This can also be checked with <code>npm ping</code>. If this check fails, you may be using a proxy that needs to be configured, or may need to talk to your IT staff to get access over HTTPS to <code>registry.npmjs.org</code>. </p>
<p> This check is done against whichever registry you&#8217;ve configured (you can see what that is by running <code>npm config get registry</code>), and if you&#8217;re using a private registry that doesn&#8217;t support the <code>/whoami</code> endpoint supported by the primary registry, this check may fail.</p>
<h3><code>npm -v</code></h3>
<p> While Node.js may come bundled with a particular version of npm, it&#8217;s the policy of the CLI team that we recommend all users run <code>npm [at] latest</code> if they can. As the CLI is maintained by a small team of contributors, there are only resources for a single line of development, so npm&#8217;s own long-term support releases typically only receive critical security and regression fixes. The team believes that the latest tested version of npm is almost always likely to be the most functional and defect-free version of npm.</p>
<h3><code>node -v</code></h3>
<p> For most users, in most circumstances, the best version of Node will be the latest long-term support (LTS) release. Those of you who want access to new ECMAscript features or bleeding-edge changes to Node&#8217;s standard library may be running a newer version, and some of you may be required to run an older version of Node because of enterprise change control policies. That&#8217;s OK! But in general, the npm team recommends that most users run Node.js LTS.</p>
<h3><code>npm config get registry</code></h3>
<p> Some of you may be installing from private package registries for your project or company. That&#8217;s great! Others of you may be following tutorials or StackOverflow questions in an effort to troubleshoot problems you may be having. Sometimes, this may entail changing the registry you&#8217;re pointing at. This part of <code>npm doctor</code> just lets you, and maybe whoever&#8217;s helping you with support, know that you&#8217;re not using the default registry.</p>
<h3><code>which git</code></h3>
<p> While it&#8217;s documented in the README, it may not be obvious that npm needs Git installed to do many of the things that it does. Also, in some cases – especially on Windows – you may have Git set up in such a way that it&#8217;s not accessible via your <code>PATH</code> so that npm can find it. This check ensures that Git is available.</p>
<h3>Permissions checks</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Your cache must be readable and writable by the user running npm.</p>
<dt>&bull;</p>
<dd> Global package binaries must be writable by the user running npm.</p>
<dt>&bull;</p>
<dd> Your local <code>node_modules</code> path, if you&#8217;re running <code>npm doctor</code> with a project directory, must be readable and writable by the user running npm. </p>
</dl>
</dl>
<h3>Validate the checksums of cached packages</h3>
<p> When an npm package is published, the publishing process generates a checksum that npm uses at install time to verify that the package didn&#8217;t get corrupted in transit. <code>npm doctor</code> uses these checksums to validate the package tarballs in your local cache (you can see where that cache is located with <code>npm config get cache</code>, and see what&#8217;s in that cache with <code>npm cache ls</code> – probably more than you were expecting!). In the event that there are corrupt packages in your cache, you should probably run <code>npm cache clean</code> and reset the cache.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help bugs</p>
<dt>&bull;</p>
<dd> npm help help</p>
<dt>&bull;</p>
<dd> npm help ping </p>
</dl>
</dl>
<h2>Index</h2>
</dl>
