---
title: "bundle-binstubs2-7(1)"
name: "bundle-binstubs2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-binstubs2-7/"
description: "bundle-binstubs – Install the binstubs of the listed gems"
---

<p><code>bundle-binstubs</code> &#8211; Install the binstubs of the listed gems </p>
<h2>Synopsis</h2>
<p><code>bundle binstubs</code> <i>GEM_NAME</i> [&#8211;force] [&#8211;path PATH] [&#8211;standalone]</p>
<h2>Description</h2>
<p>Binstubs are scripts that wrap around executables. Bundler creates a small Ruby file (a binstub) that loads Bundler, runs the command, and puts it into <code>bin/</code>. Binstubs are a shortcut-or alternative- to always using <code>bundle exec</code>. This gives you a file that can be run directly, and one that will always run the correct gem version used by the application. </p>
<p> For example, if you run <code>bundle binstubs rspec-core</code>, Bundler will create the file <code>bin/rspec</code>. That file will contain enough code to load Bundler, tell it to load the bundled gems, and then run rspec. </p>
<p> This command generates binstubs for executables in <code>GEM_NAME</code>. Binstubs are put into <code>bin</code>, or the <code>&#8211;path</code> directory if one has been set. Calling binstubs with [GEM [GEM]] will create binstubs for all given gems.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;force</code></p>
<dd>Overwrite existing binstubs if they exist.</p>
<dt><code>&#8211;path</code></p>
<dd>The location to install the specified binstubs to. This defaults to <code>bin</code>.</p>
<dt><code>&#8211;standalone</code></p>
<dd>Makes binstubs that can work without depending on Rubygems or Bundler at runtime.</p>
<dt><code>&#8211;shebang</code></p>
<dd>Specify a different shebang executable name than the default (default &#8216;ruby&#8217;)</dl>
<h2>Bundle Install &#8211;Binstubs</h2>
<p>To create binstubs for all the gems in the bundle you can use the <code>&#8211;binstubs</code> flag in bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i>.</p>
