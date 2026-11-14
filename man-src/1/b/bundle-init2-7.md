---
title: "bundle-init2-7(1)"
name: "bundle-init2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-init2-7/"
description: "bundle-init – Generates a Gemfile into the current working directory"
---

<p><code>bundle-init</code> &#8211; Generates a Gemfile into the current working directory </p>
<h2>Synopsis</h2>
<p><code>bundle init</code> [&#8211;gemspec=FILE]</p>
<h2>Description</h2>
<p>Init generates a default [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)] in the current working directory. When adding a [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)] to a gem with a gemspec, the <code>&#8211;gemspec</code> option will automatically add each dependency listed in the gemspec file to the newly created [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)].</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;gemspec</code></p>
<dd>Use the specified .gemspec to create the [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)]</dl>
<h2>Files</h2>
<p>Included in the default [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)] generated is the line <code># frozen_string_literal: true</code>. This is a magic comment supported for the first time in Ruby 2.3. The presence of this line results in all string literals in the file being implicitly frozen.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) <i><a rel="nofollow" href="https://bundler.io/man/gemfile.5.html">https://bundler.io/man/gemfile.5.html</a></i></p>
