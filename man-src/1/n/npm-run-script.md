---
title: "npm-run-script(1)"
name: "npm-run-script"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-run-script/"
description: "npm-run-script – Run arbitrary package scripts"
---

<h2 class="name">NAME</h2>
<p> <code>npm-run-script</code> &#8211; Run arbitrary package scripts </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm run - script&lt;command&gt;[--silent][--&lt;args&gt;...] alias : npm run
</code></pre>
</dl>
<h3>Description</h3>
<p> This runs an arbitrary command from a package&#8217;s <code>&quot;scripts&quot;</code> object. If no <code>&quot;command&quot;</code> is provided, it will list the available scripts. <code>run[-script]</code> is used by the test, start, restart, and stop commands, but can be called directly, as well. When the scripts in the package are printed out, they&#8217;re separated into lifecycle (test, start, restart) and directly-run scripts. </p>
<p> As of <code>npm [at] 2.0.0</code> <i><a rel="nofollow" href="https://blog.npmjs.org/post/98131109725/npm-2-0-0">https://blog.npmjs.org/post/98131109725/npm-2-0-0</a></i>, you can use custom arguments when executing scripts. The special option <code>&#8212;</code> is used by getopt <i><a rel="nofollow" href="https://goo.gl/KxMmtG">https://goo.gl/KxMmtG</a></i> to delimit the end of the options. npm will pass all the arguments after the <code>&#8212;</code> directly to your script: </p>
<dl>
<dt>
<dd>
<pre>
npm run test -- --grep=&quot;pattern&quot;
</pre>
</dl>
<p> The arguments will only be passed to the script specified after <code>npm run</code> and not to any pre or post script. </p>
<p> The <code>env</code> script is a special built-in command that can be used to list environment variables that will be available to the script at runtime. If an &quot;env&quot; command is defined in your package, it will take precedence over the built-in. </p>
<p> In addition to the shell&#8217;s pre-existing <code>PATH</code>, <code>npm run</code> adds <code>node_modules/.bin</code> to the <code>PATH</code> provided to scripts. Any binaries provided by locally-installed dependencies can be used without the <code>node_modules/.bin</code> prefix. For example, if there is a <code>devDependency</code> on <code>tap</code> in your package, you should write: </p>
<dl>
<dt>
<dd>
<pre>
&quot;scripts&quot;: {&quot;test&quot;: &quot;tap test/\*.js&quot;}
</pre>
</dl>
<p> instead of </p>
<dl>
<dt>
<dd>
<pre>
&quot;scripts&quot;: {&quot;test&quot;: &quot;node_modules/.bin/tap test/\*.js&quot;}
</pre>
</dl>
<p> to run your tests. </p>
<p> The actual shell your script is run within is platform dependent. By default, on Unix-like systems it is the <code>/bin/sh</code> command, on Windows it is the <code>cmd.exe</code>. The actual shell referred to by <code>/bin/sh</code> also depends on the system. As of <code>npm [at] 5.1.0</code> <i><a rel="nofollow" href="https://github.com/npm/npm/releases/tag/v5.1.0">https://github.com/npm/npm/releases/tag/v5.1.0</a></i> you can customize the shell with the <code>script-shell</code> configuration. </p>
<p> Scripts are run from the root of the module, regardless of what your current working directory is when you call <code>npm run</code>. If you want your script to use different behavior based on what subdirectory you&#8217;re in, you can use the <code>INIT_CWD</code> environment variable, which holds the full path you were in when you ran <code>npm run</code>. </p>
<p> <code>npm run</code> sets the <code>NODE</code> environment variable to the <code>node</code> executable with which <code>npm</code> is executed. Also, if the <code>&#8211;scripts-prepend-node-path</code> is passed, the directory within which <code>node</code> resides is added to the <code>PATH</code>. If <code>&#8211;scripts-prepend-node-path=auto</code> is passed (which has been the default in <code>npm</code> v3), this is only performed when that <code>node</code> executable is not found in the <code>PATH</code>. </p>
<p> If you try to run a script without having a <code>node_modules</code> directory and it fails, you will be given a warning to run <code>npm install</code>, just in case you&#8217;ve forgotten. </p>
<p> You can use the <code>&#8211;silent</code> flag to prevent showing <code>npm ERR!</code> output on error. </p>
<p> You can use the <code>&#8211;if-present</code> flag to avoid exiting with a non-zero exit code when the script is undefined. This lets you run potentially undefined scripts without breaking the execution chain.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help scripts</p>
<dt>&bull;</p>
<dd> npm help test</p>
<dt>&bull;</p>
<dd> npm help start</p>
<dt>&bull;</p>
<dd> npm help restart</p>
<dt>&bull;</p>
<dd> npm help stop</p>
<dt>&bull;</p>
<dd> npm help config </p>
</dl>
</dl>
<h2>Index</h2>
