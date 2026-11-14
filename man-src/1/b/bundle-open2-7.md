---
title: "bundle-open2-7(1)"
name: "bundle-open2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-open2-7/"
description: "bundle-open – Opens the source directory for a gem in your bundle"
---

<p><code>bundle-open</code> &#8211; Opens the source directory for a gem in your bundle </p>
<h2>Synopsis</h2>
<p><code>bundle open</code> [GEM]</p>
<h2>Description</h2>
<p>Opens the source directory of the provided GEM in your editor. </p>
<p> For this to work the <code>EDITOR</code> or <code>BUNDLER_EDITOR</code> environment variable has to be set. </p>
<p> Example:</p>
<dl>
<dd>
<pre>bundle open 'rack'</pre>
<dd></dl>
<p> Will open the source directory for the &#8216;rack&#8217; gem in your bundle.</p>
