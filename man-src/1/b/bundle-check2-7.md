---
title: "bundle-check2-7(1)"
name: "bundle-check2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-check2-7/"
description: "bundle-check – Verifies if dependencies are satisfied by installed gems"
---

<p><code>bundle-check</code> &#8211; Verifies if dependencies are satisfied by installed gems </p>
<h2>Synopsis</h2>
<p><code>bundle check</code> [&#8211;dry-run] [&#8211;gemfile=FILE] [&#8211;path=PATH]</p>
<h2>Description</h2>
<p><code>check</code> searches the local machine for each of the gems requested in the Gemfile. If all gems are found, Bundler prints a success message and exits with a status of 0. </p>
<p> If not, the first missing gem is listed and Bundler exits status 1.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;dry-run</code></p>
<dd>Locks the [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)] before running the command.</p>
<dt><code>&#8211;gemfile</code></p>
<dd>Use the specified gemfile instead of the [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)].</p>
<dt><code>&#8211;path</code></p>
<dd>Specify a different path than the system default (<code>$BUNDLE_PATH</code> or <code>$GEM_HOME</code>). Bundler will remember this value for future installs on this machine. </p>
</dl>
