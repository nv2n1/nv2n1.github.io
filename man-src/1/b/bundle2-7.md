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
<p> See the bundler website <i><a rel="nofollow" href="https://bundler.io">https://bundler.io</a></i> for information on getting started, and Gemfile(5) for more information on the <code>Gemfile</code> format.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;no-color</code></dt>
<dd>Print all output without color</dd>
<dt><code>&#8211;retry</code>, <code>-r</code></dt>
<dd>Specify the number of times you wish to attempt network commands</dd>
<dt><code>&#8211;verbose</code>, <code>-V</code></dt>
<dd>Print out additional logging information</dd></dl>
<h2>Bundle Commands</h2>
<p>We divide <code>bundle</code> subcommands into primary commands and utilities:</p>
<h2>Primary Commands</h2>
<dl>
<dt><code>bundle <a href="/docs/linux/man/1-install/">install</a>(1)</code> <i>bundle-install.1.html</i></dt>
<dd>Install the gems specified by the <code>Gemfile</code> or <code>Gemfile.lock</code></dd>
<dt><code>bundle update(1)</code> <i>bundle-update.1.html</i></dt>
<dd>Update dependencies to their latest versions</dd>
<dt><code>bundle package(1)</code> <i>bundle-package.1.html</i></dt>
<dd>Package the .gem files required by your application into the <code>vendor/cache</code> directory</dd>
<dt><code>bundle <a href="/docs/linux/man/1-exec/">exec</a>(1)</code> <i>bundle-exec.1.html</i></dt>
<dd>Execute a script in the current bundle</dd>
<dt><code>bundle config(1)</code> <i>bundle-config.1.html</i></dt>
<dd>Specify and read configuration options for Bundler</dd>
<dt><code>bundle <a href="/docs/linux/man/1-help/">help</a>(1)</code></dt>
<dd>Display detailed help for each subcommand</dd></dl>
<h2>Utilities</h2>
<dl>
<dt><code>bundle add(1)</code> <i>bundle-add.1.html</i></dt>
<dd>Add the named gem to the Gemfile and run <code>bundle install</code></dd>
<dt><code>bundle binstubs(1)</code> <i>bundle-binstubs.1.html</i></dt>
<dd>Generate binstubs for executables in a gem</dd>
<dt><code>bundle check(1)</code> <i>bundle-check.1.html</i></dt>
<dd>Determine whether the requirements for your application are installed and available to Bundler</dd>
<dt><code>bundle <a href="/docs/linux/man/1-show/">show</a>(1)</code> <i>bundle-show.1.html</i></dt>
<dd>Show the source location of a particular gem in the bundle</dd>
<dt><code>bundle outdated(1)</code> <i>bundle-outdated.1.html</i></dt>
<dd>Show all of the outdated gems in the current bundle</dd>
<dt><code>bundle <a href="/docs/linux/man/1-console/">console</a>(1)</code></dt>
<dd>Start an IRB session in the current bundle</dd>
<dt><code>bundle <a href="/docs/linux/man/1-open/">open</a>(1)</code> <i>bundle-open.1.html</i></dt>
<dd>Open an installed gem in the editor</dd>
<dt><code>bundle lock(1)</code> <i>bundle-lock.1.html</i></dt>
<dd>Generate a lockfile for your dependencies</dd>
<dt><code>bundle viz(1)</code> <i>bundle-viz.1.html</i></dt>
<dd>Generate a visual representation of your dependencies</dd>
<dt><code>bundle <a href="/docs/linux/man/1-init/">init</a>(1)</code> <i>bundle-init.1.html</i></dt>
<dd>Generate a simple <code>Gemfile</code>, placed in the current directory</dd>
<dt><code>bundle <a href="/docs/linux/man/1-gem/">gem</a>(1)</code> <i>bundle-gem.1.html</i></dt>
<dd>Create a simple gem, suitable for development with Bundler</dd>
<dt><code>bundle platform(1)</code> <i>bundle-platform.1.html</i></dt>
<dd>Display platform compatibility information</dd>
<dt><code>bundle clean(1)</code> <i>bundle-clean.1.html</i></dt>
<dd>Clean up unused gems in your Bundler directory</dd>
<dt><code>bundle doctor(1)</code> <i>bundle-doctor.1.html</i></dt>
<dd>Display warnings about common problems</dd>
<dt><code>bundle remove(1)</code> <i>bundle-remove.1.html</i></dt>
<dd>Removes gems from the Gemfile</dd></dl>
<h2>Plugins</h2>
<p>When running a command that isn&#8217;t listed in PRIMARY COMMANDS or UTILITIES, Bundler will try to find an executable on your path named <code>bundler-&lt;command&gt;</code> and execute it, passing down any extra arguments to it.</p>
<h2>Obsolete</h2>
<p>These commands are obsolete and should no longer be used:</p>
<dl>
<dt>&bull;</dt>
<dd><code>bundle cache(1)</code></dd>
<dt>&bull;</dt>
<dd><code>bundle <a href="/docs/linux/man/1-show/">show</a>(1)</code></dd>
<dd></dd></dl>
