---
title: "bundle-doctor2-7(1)"
name: "bundle-doctor2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-doctor2-7/"
description: "bundle-doctor – Checks the bundle for common problems"
---

<p><code>bundle-doctor</code> &#8211; Checks the bundle for common problems </p>
<h2>Synopsis</h2>
<p><code>bundle doctor</code> [&#8211;quiet] [&#8211;gemfile=GEMFILE]</p>
<h2>Description</h2>
<p>Checks your Gemfile and gem environment for common problems. If issues are detected, Bundler prints them and exits status 1. Otherwise, Bundler prints a success message and exits status 0. </p>
<p> Examples of common problems caught by bundle-doctor include:</p>
<dl>
<dt>&bull;</p>
<dd>Invalid Bundler settings</p>
<dt>&bull;</p>
<dd>Mismatched Ruby versions</p>
<dt>&bull;</p>
<dd>Mismatched platforms</p>
<dt>&bull;</p>
<dd>Uninstalled gems</p>
<dt>&bull;</p>
<dd>Missing dependencies</p>
<dd></dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;quiet</code></p>
<dd>Only output warnings and errors.</p>
<dt><code>&#8211;gemfile=&lt;gemfile&gt;</code></p>
<dd>The location of the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) which Bundler should use. This defaults to a <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) in the current working directory. In general, Bundler will assume that the location of the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) is also the project&#8217;s root and will try to find <code>Gemfile.lock</code> and <code>vendor/cache</code> relative to this location. </p>
</dl>
