---
title: "shrinkwrap-json(5)"
name: "shrinkwrap-json"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shrinkwrap-json/"
description: "npm-shrinkwrap.json – A publishable lockfile"
---

<p><code>npm-shrinkwrap.json</code> &#8211; A publishable lockfile</p>
<h3>Description</h3>
<p><code>npm-shrinkwrap.json</code> is a file created by npm help <code>shrinkwrap</code>. It is identical to <code>package-lock.json</code>, with one major caveat: Unlike <code>package-lock.json</code>, <code>npm-shrinkwrap.json</code> may be included when publishing a package. The recommended use-case for <code>npm-shrinkwrap.json</code> is applications deployed through the publishing process on the registry: for example, daemons and command-line tools intended as global installs or <code>devDependencies</code>. It&#8217;s strongly discouraged for library authors to publish this file, since that would prevent end users from having control over transitive dependency updates. Additionally, if both <code>package-lock.json</code> and <code>npm-shrinkwrap.json</code> are present in a package root, <code>package-lock.json</code> will be ignored in favor of this file. For full details and description of the <code>npm-shrinkwrap.json</code> file format, refer to the manual page for npm help package-lock.json.</p>
<h3>See also</h3>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>npm help shrinkwrap</p>
<dt>&bull;</p>
<dd>npm help package-lock.json</p>
<dt>&bull;</p>
<dd>npm help package.json</p>
<dt>&bull;</p>
<dd>npm help install </p>
