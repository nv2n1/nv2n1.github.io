---
title: "bundle-remove2-7(1)"
name: "bundle-remove2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-remove2-7/"
description: "bundle-remove – Removes gems from the Gemfile"
---

<p><code>bundle-remove</code> &#8211; Removes gems from the Gemfile </p>
<h2>Synopsis</h2>
<p><code>bundle remove [GEM [GEM &#8230;]] [&#8211;install]</code></p>
<h2>Description</h2>
<p>Removes the given gems from the Gemfile while ensuring that the resulting Gemfile is still valid. If a gem cannot be removed, a warning is printed. If a gem is already absent from the Gemfile, and error is raised.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;install</code></p>
<dd>Runs <code>bundle install</code> after the given gems have been removed from the Gemfile, which ensures that both the lockfile and the installed gems on disk are also updated to remove the given gem(s).</dl>
<p> Example: </p>
<p> bundle remove rails </p>
<p> bundle remove rails rack </p>
<p> bundle remove rails rack &#8211;install</p>
