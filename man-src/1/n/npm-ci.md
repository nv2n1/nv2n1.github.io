---
title: "npm-ci(1)"
name: "npm-ci"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-ci/"
description: "npm-ci – Install a project with a clean slate"
---

<h2 class="name">NAME</h2>
<p> <code>npm-ci</code> &#8211; Install a project with a clean slate </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm ci
</pre>
</dl>
<h3>Example</h3>
<p> Make sure you have a package-lock and an up-to-date install: </p>
<dl>
<dt>
<dd>
<pre>
$ cd ./my/npm/project
$ npm install
added 154 packages in 10s
$ ls | grep package-lock
</pre>
</dl>
<p> Run <code>npm ci</code> in that project </p>
<dl>
<dt>
<dd>
<pre>
$ npm ci
added 154 packages in 5s
</pre>
</dl>
<p> Configure Travis to build using <code>npm ci</code> instead of <code>npm install</code>: </p>
<dl>
<dt>
<dd>
<pre>
# .travis.yml
install:
- npm ci
# keep the npm cache around to speed up installs
cache:
  directories:
  - &quot;$HOME/.npm&quot;
</pre>
</dl>
<h3>Description</h3>
<p> This command is similar to npm help <code>install</code>, except it&#8217;s meant to be used in automated environments such as test platforms, continuous integration, and deployment &#8212; or any situation where you want to make sure you&#8217;re doing a clean install of your dependencies. It can be significantly faster than a regular npm install by skipping certain user-oriented features. It is also more strict than a regular install, which can help catch errors or inconsistencies caused by the incrementally-installed local environments of most npm users. </p>
<p> In short, the main differences between using <code>npm install</code> and <code>npm ci</code> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The project <code>must</code> have an existing <code>package-lock.json</code> or <code>npm-shrinkwrap.json</code>.</p>
<dt>&bull;</p>
<dd> If dependencies in the package lock do not match those in <code>package.json</code>, <code>npm ci</code> will exit with an error, instead of updating the package lock.</p>
<dt>&bull;</p>
<dd> <code>npm ci</code> can only install entire projects at a time: individual dependencies cannot be added with this command.</p>
<dt>&bull;</p>
<dd> If a <code>node_modules</code> is already present, it will be automatically removed before <code>npm ci</code> begins its install.</p>
<dt>&bull;</p>
<dd> It will never write to <code>package.json</code> or any of the package-locks: installs are essentially frozen. </p>
</dl>
</dl>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help package-locks </p>
</dl>
</dl>
<h2>Index</h2>
