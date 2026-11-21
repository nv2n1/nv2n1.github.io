---

title: "yarnpkg(1)"
name: "yarnpkg"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yarnpkg/"
description: "yarnpkg – Fast, reliable and secure npm alternative"
---

<p> <code>yarnpkg</code> &#8211; Fast, reliable and secure npm alternative </p>
<h2>SYNOPSIS</h2>
<p> yarnpkg command [package]@[version]</p>
<h2>DESCRIPTION</h2>
<p> Fast: Yarnpkg caches every package it downloads so it never needs to again. It also parallelizes operations to maximize resource utilization so install times are faster than ever. </p>
<p> Reliable: Using a detailed, but concise, lockfile format, and a deterministic algorithm for installs, Yarnpkg is able to guarantee that an install that worked on one system will work exactly the same way on any other system. </p>
<p> Secure: Yarnpkg uses checksums to verify the integrity of every installed package before its code is executed.</p>
<h2>EXAMPLES</h2>
<p> Here are some of the most common commands you’ll need. </p>
<p> Starting a new project </p>
<dl>
<dt>
</dt><dd>
<pre>
yarn init
</pre>
</dd></dl>
<p> Adding a dependency </p>
<dl>
<dt>
</dt><dd>
<pre><code>
yarn add[package] yarn add[package] @[ version ] yarn add[package] @[ tag ]
</code></pre>
</dd></dl>
<p> Updating a dependency </p>
<dl>
<dt>
</dt><dd>
<pre><code>
yarn upgrade[package] yarn upgrade[package] @[ version ] yarn upgrade[package] @[ tag ]
</code></pre>
</dd></dl>
<p> Removing a dependency </p>
<dl>
<dt>
</dt><dd>
<pre>
yarn remove [package]
</pre>
</dd></dl>
<p> Installing all the dependencies of project </p>
<dl>
<dt>
</dt><dd>
<pre>
yarn
</pre>
</dd></dl>
<p> or </p>
<dl>
<dt>
</dt><dd>
<pre>
yarn install
</pre>
</dd></dl>
<h2>COMMANDS</h2>
<p> Yarn provides a rich set of command-line commands to help you with various aspects of your Yarn package, including installation, administration, publishing, etc. </p>
<p> Some of the more popular commands are:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <code>yarn add</code>: adds a package to use in your current package.</dd>
<dt>&bull;</dt>
<dd> <code>yarn init</code>: initializes the development of a package.</dd>
<dt>&bull;</dt>
<dd> <code>yarn install</code>: installs all the dependencies defined in a package.json file.</dd>
<dt>&bull;</dt>
<dd> <code>yarn publish</code>: publishes a package to a package manager.</dd>
<dt>&bull;</dt>
<dd> <code>yarn remove</code>: removes an unused package from your current package. </dd>
</dl>
</dl>
<h3>Default Command</h3>
<p> Running yarn with no command will run yarn install, passing through any provided flags. </p>
<p> ###Concurrency and &#8211;mutex </p>
<p> When running multiple instances of yarn as the same user on the same server, you can ensure only one instance runs at any given time (and avoid conflicts) by passing the global flag &#8211;mutex followed by file or network. </p>
<p> When using file Yarn will write/read a mutex file .yarn-single-instance in the current working directory by default. You can also specify an alternate or global filename. </p>
<dl>
<dt>
</dt><dd>
<pre>
--mutex file
--mutex file:/tmp/.yarn-mutex
</pre>
</dd></dl>
<p> When using network Yarn will create a server at port 31997 by default. You can also specify an alternate port. </p>
<dl>
<dt>
</dt><dd>
<pre>
--mutex network
--mutex network:30330
</pre>
</dd></dl>
<h2>AUTHOR</h2>
<p> The Yarn Contributors</p>
<h2>COPYRIGHT</h2>
<p> This manual page was written by Paolo Greppi <code>&lt;paolo.greppi [at] libpf.com&gt;</code> for the Debian project (and may be used by others), based on material from the yarnpkg project itself. </p>
