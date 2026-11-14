---
title: "bundle-lock2-7(1)"
name: "bundle-lock2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-lock2-7/"
description: "bundle-lock – Creates / Updates a lockfile without installing"
---

<p><code>bundle-lock</code> &#8211; Creates / Updates a lockfile without installing </p>
<h2>Synopsis</h2>
<p><code>bundle lock</code> [&#8211;update] [&#8211;local] [&#8211;print] [&#8211;lockfile=PATH] [&#8211;full-index] [&#8211;add-platform] [&#8211;remove-platform] [&#8211;patch] [&#8211;minor] [&#8211;major] [&#8211;strict] [&#8211;conservative]</p>
<h2>Description</h2>
<p>Lock the gems specified in Gemfile.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;update=&lt;*gems&gt;</code></p>
<dd>Ignores the existing lockfile. Resolve then updates lockfile. Taking a list of gems or updating all gems if no list is given.</p>
<dt><code>&#8211;local</code></p>
<dd>Do not attempt to connect to <code>rubygems.org</code>. Instead, Bundler will use the gems already present in Rubygems&#8217; cache or in <code>vendor/cache</code>. Note that if a appropriate platform-specific gem exists on <code>rubygems.org</code> it will not be found.</p>
<dt><code>&#8211;print</code></p>
<dd>Prints the lockfile to STDOUT instead of writing to the file system.</p>
<dt><code>&#8211;lockfile=&lt;path&gt;</code></p>
<dd>The path where the lockfile should be written to.</p>
<dt><code>&#8211;full-index</code></p>
<dd>Fall back to using the single-file index of all gems.</p>
<dt><code>&#8211;add-platform</code></p>
<dd>Add a new platform to the lockfile, re-resolving for the addition of that platform.</p>
<dt><code>&#8211;remove-platform</code></p>
<dd>Remove a platform from the lockfile.</p>
<dt><code>&#8211;patch</code></p>
<dd>If updating, prefer updating only to next patch version.</p>
<dt><code>&#8211;minor</code></p>
<dd>If updating, prefer updating only to next minor version.</p>
<dt><code>&#8211;major</code></p>
<dd>If updating, prefer updating to next major version (default).</p>
<dt><code>&#8211;strict</code></p>
<dd>If updating, do not allow any gem to be updated past latest &#8211;patch | &#8211;minor | &#8211;major.</p>
<dt><code>&#8211;conservative</code></p>
<dd>If updating, use bundle install conservative update behavior and do not allow shared dependencies to be updated.</dl>
<h2>Updating All Gems</h2>
<p>If you run <code>bundle lock</code> with <code>&#8211;update</code> option without list of gems, bundler will ignore any previously installed gems and resolve all dependencies again based on the latest versions of all gems available in the sources.</p>
<h2>Updating A List Of Gems</h2>
<p>Sometimes, you want to update a single gem in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5), and leave the rest of the gems that you specified locked to the versions in the <code>Gemfile.lock</code>. </p>
<p> For instance, you only want to update <code>nokogiri</code>, run <code>bundle lock &#8211;update nokogiri</code>. </p>
<p> Bundler will update <code>nokogiri</code> and any of its dependencies, but leave the rest of the gems that you specified locked to the versions in the <code>Gemfile.lock</code>.</p>
<h2>Supporting Other Platforms</h2>
<p>If you want your bundle to support platforms other than the one you&#8217;re running locally, you can run <code>bundle lock &#8211;add-platform PLATFORM</code> to add PLATFORM to the lockfile, force bundler to re-resolve and consider the new platform when picking gems, all without needing to have a machine that matches PLATFORM handy to install those platform-specific gems on. </p>
<p> For a full explanation of gem platforms, see <code>gem help platform</code>.</p>
<h2>Patch Level Options</h2>
<p>See bundle <a href="/docs/linux/man/1-update/">update</a>(1) <i>bundle-update.1.html</i> for details.</p>
