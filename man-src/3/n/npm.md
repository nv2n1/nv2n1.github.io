---
title: "npm(3)"
name: "npm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm/"
description: "npm — node package manager"
---

<p><code>npm</code> &#8212; node package manager</p>
<h2>Synopsis</h2>
<pre>var npm = require(&quot;npm&quot;)
npm.load([configObject,] function (er, npm) {
 // use the npm object, now that it's loaded.
 npm.config.set(key, val)
 val = npm.config.get(key)
 console.log(&quot;prefix = %s&quot;, npm.prefix)
 npm.commands.install([&quot;package&quot;], cb)
})</pre>
<h2>Version</h2>
<p>1.3.6</p>
<h2>Description</h2>
<p>This is the API documentation for npm. To find documentation of the command line npm help client, see <code>npm</code>. </p>
<p> Prior to using npm&#8217;s commands, <code>npm.load()</code> must be called. If you provide <code>configObject</code> as an object hash of top-level configs, they override the values stored in the various config locations. In the npm command line client, this set of configs is parsed from the command line options. Additional configuration npm help npm help params are loaded from two configuration files. See <code>npm-config</code>, <code>npm-confignpm help </code>, and <code>npmrc</code> for more information. </p>
<p> After that, each of the functions are accessible in the npm help commands object: <code>npm.commands.&lt;cmd&gt;</code>. See <code>npm-index</code> for a list of all possible commands. </p>
<p> All commands on the command object take an <code>array</code> of positional argument <code>strings</code>. The last argument to any function is a callback. Some commands take other optional arguments. </p>
<p> Configs cannot currently be set on a per function basis, as each call to npm.config.set will change the value for <i>all</i> npm commands in that process. </p>
<p> To find API documentation for a specific command, run the <code>npm apihelp</code> command.</p>
<h2>Methods And Properties</h2>
<dl>
<dt>&bull;</dt>
<dd><code>npm.load(configs, cb)</code></dd>
<dd>Load the configuration params, and call the <code>cb</code> function once the globalconfig and userconfig files have been loaded as well, or on nextTick if they&#8217;ve already been loaded.</dd>
<dt>&bull;</dt>
<dd><code>npm.config</code></dd>
<dd>An object for accessing npm configuration parameters.</dd>
<dt>&bull;</dt>
<dd><code>npm.config.get(key)</code></dd>
<dt>&bull;</dt>
<dd><code>npm.config.set(key, val)</code></dd>
<dt>&bull;</dt>
<dd><code>npm.config.del(key)</code></dd>
<dd>
</dd><dt>&bull;</dt>
<dd><code>npm.dir</code> or <code>npm.root</code></dd>
<dd>The <code>node_modules</code> directory where npm will operate.</dd>
<dt>&bull;</dt>
<dd><code>npm.prefix</code></dd>
<dd>The prefix where npm is operating. (Most often the current working directory.)</dd>
<dt>&bull;</dt>
<dd><code>npm.cache</code></dd>
<dd>The place where npm keeps JSON and tarballs it fetches from the registry (or uploads to the registry).</dd>
<dt>&bull;</dt>
<dd><code>npm.tmp</code></dd>
<dd>npm&#8217;s temporary working directory.</dd>
<dt>&bull;</dt>
<dd><code>npm.deref</code></dd>
<dd>Get the &quot;real&quot; name for a command that has either an alias or abbreviation.</dd>
<dd></dd></dl>
<h2>Magic</h2>
<p>For each of the methods in the <code>npm.commands</code> hash, a method is added to the npm object, which takes a set of positional string arguments rather than an array and a callback. </p>
<p> If the last argument is a callback, then it will use the supplied callback. However, if no callback is provided, then it will print out the error or results. </p>
<p> For example, this would work in a node repl:</p>
<dl>
<dd>
<pre>&gt; npm = require(&quot;npm&quot;)
&gt; npm.load() // wait a sec...
&gt; npm.install(&quot;dnode&quot;, &quot;express&quot;)</pre>
</dd><dd></dd></dl>
<p> Note that that <i>won&#8217;t</i> work in a node program, since the <code>install</code> method will get called before the configuration load is completed.</p>
<h2>Abbrevs</h2>
<p>In order to support <code>npm ins foo</code> instead of <code>npm install foo</code>, the <code>npm.commands</code> object has a set of abbreviations as well as the full method names. Use the <code>npm.deref</code> method to find the real name. </p>
<p> For example:</p>
<dl>
<dd>
<pre>var cmd = npm.deref(&quot;unp&quot;) // cmd === &quot;unpublish&quot;</pre>
</dd><dd></dd></dl>
