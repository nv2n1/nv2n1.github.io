---
title: "bundle2-7(1)"
name: "bundle2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle2-7/"
description: "bundle – Ruby Dependency Management"
---

<p><code>bundle</code> &#8211; Ruby Dependency Management </p>
<h2>Synopsis</h2>
<p><code>bundle</code> COMMAND [&#8211;no-color] [&#8211;verbose] [ARGS]</p>
<h2>Description</h2>
<p>Bundler manages an <code>application&#8217;s dependencies</code> through its entire life across many machines systematically and repeatably. </p>
<p> See the bundler website <i><a rel="nofollow" href="https://bundler.io">https://bundler.io</a></i> for information on getting started, and <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) for more information on the <code>Gemfile</code> format.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;no-color</code></p>
<dd>Print all output without color</p>
<dt><code>&#8211;retry</code>, <code>-r</code></p>
<dd>Specify the number of times you wish to attempt network commands</p>
<dt><code>&#8211;verbose</code>, <code>-V</code></p>
<dd>Print out additional logging information</dl>
<h2>Bundle Commands</h2>
<p>We divide <code>bundle</code> subcommands into primary commands and utilities:</p>
<h2>Primary Commands</h2>
<dl>
<dt><code>bundle <a href="/docs/linux/man/1-install/">install</a>(1)</code> <i>bundle-install.1.html</i></p>
<dd>Install the gems specified by the <code>Gemfile</code> or <code>Gemfile.lock</code></p>
<dt><code>bundle <a href="/docs/linux/man/1-update/">update</a>(1)</code> <i>bundle-update.1.html</i></p>
<dd>Update dependencies to their latest versions</p>
<dt><code>bundle <a href="/docs/linux/man/1-package/">package</a>(1)</code> <i>bundle-package.1.html</i></p>
<dd>Package the .gem files required by your application into the <code>vendor/cache</code> directory</p>
<dt><code>bundle <a href="/docs/linux/man/1-exec/">exec</a>(1)</code> <i>bundle-exec.1.html</i></p>
<dd>Execute a script in the current bundle</p>
<dt><code>bundle <a href="/docs/linux/man/1-config/">config</a>(1)</code> <i>bundle-config.1.html</i></p>
<dd>Specify and read configuration options for Bundler</p>
<dt><code>bundle <a href="/docs/linux/man/1-help/">help</a>(1)</code></p>
<dd>Display detailed help for each subcommand</dl>
<h2>Utilities</h2>
<dl>
<dt><code>bundle <a href="/docs/linux/man/1-add/">add</a>(1)</code> <i>bundle-add.1.html</i></p>
<dd>Add the named gem to the Gemfile and run <code>bundle install</code></p>
<dt><code>bundle <a href="/docs/linux/man/1-binstubs/">binstubs</a>(1)</code> <i>bundle-binstubs.1.html</i></p>
<dd>Generate binstubs for executables in a gem</p>
<dt><code>bundle <a href="/docs/linux/man/1-check/">check</a>(1)</code> <i>bundle-check.1.html</i></p>
<dd>Determine whether the requirements for your application are installed and available to Bundler</p>
<dt><code>bundle <a href="/docs/linux/man/1-show/">show</a>(1)</code> <i>bundle-show.1.html</i></p>
<dd>Show the source location of a particular gem in the bundle</p>
<dt><code>bundle <a href="/docs/linux/man/1-outdated/">outdated</a>(1)</code> <i>bundle-outdated.1.html</i></p>
<dd>Show all of the outdated gems in the current bundle</p>
<dt><code>bundle <a href="/docs/linux/man/1-console/">console</a>(1)</code></p>
<dd>Start an IRB session in the current bundle</p>
<dt><code>bundle <a href="/docs/linux/man/1-open/">open</a>(1)</code> <i>bundle-open.1.html</i></p>
<dd>Open an installed gem in the editor</p>
<dt><code>bundle <a href="/docs/linux/man/1-lock/">lock</a>(1)</code> <i>bundle-lock.1.html</i></p>
<dd>Generate a lockfile for your dependencies</p>
<dt><code>bundle <a href="/docs/linux/man/1-viz/">viz</a>(1)</code> <i>bundle-viz.1.html</i></p>
<dd>Generate a visual representation of your dependencies</p>
<dt><code>bundle <a href="/docs/linux/man/1-init/">init</a>(1)</code> <i>bundle-init.1.html</i></p>
<dd>Generate a simple <code>Gemfile</code>, placed in the current directory</p>
<dt><code>bundle <a href="/docs/linux/man/1-gem/">gem</a>(1)</code> <i>bundle-gem.1.html</i></p>
<dd>Create a simple gem, suitable for development with Bundler</p>
<dt><code>bundle <a href="/docs/linux/man/1-platform/">platform</a>(1)</code> <i>bundle-platform.1.html</i></p>
<dd>Display platform compatibility information</p>
<dt><code>bundle <a href="/docs/linux/man/1-clean/">clean</a>(1)</code> <i>bundle-clean.1.html</i></p>
<dd>Clean up unused gems in your Bundler directory</p>
<dt><code>bundle <a href="/docs/linux/man/1-doctor/">doctor</a>(1)</code> <i>bundle-doctor.1.html</i></p>
<dd>Display warnings about common problems</p>
<dt><code>bundle <a href="/docs/linux/man/1-remove/">remove</a>(1)</code> <i>bundle-remove.1.html</i></p>
<dd>Removes gems from the Gemfile</dl>
<h2>Plugins</h2>
<p>When running a command that isn&#8217;t listed in PRIMARY COMMANDS or UTILITIES, Bundler will try to find an executable on your path named <code>bundler-&lt;command&gt;</code> and execute it, passing down any extra arguments to it.</p>
<h2>Obsolete</h2>
<p>These commands are obsolete and should no longer be used:</p>
<dl>
<dt>&bull;</p>
<dd><code>bundle <a href="/docs/linux/man/1-cache/">cache</a>(1)</code></p>
<dt>&bull;</p>
<dd><code>bundle <a href="/docs/linux/man/1-show/">show</a>(1)</code></p>
<dd></dl>
