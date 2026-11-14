---
title: "libnpx(1)"
name: "libnpx"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libnpx/"
description: "npx – execute npm package binaries"
---

<h2 class="name">NAME</h2>
<p> <code>npx</code> &#8211; execute npm package binaries </p>
<h2>SYNOPSIS</h2>
<p> <code>npx [options] &lt;command&gt;[@version] [command-arg]&#8230;</code> </p>
<p> <code>npx [options] [-p|&#8211;package &lt;pkg&gt;]&#8230; &lt;command&gt; [command-arg]&#8230;</code> </p>
<p> <code>npx [options] -c &#8216;&lt;command-string&gt;&#8217;</code> </p>
<p> <code>npx &#8211;shell-auto-fallback [shell]</code></p>
<h2>INSTALL</h2>
<p> <code>npm install -g npx</code></p>
<h2>DESCRIPTION</h2>
<p> Executes <code>&lt;command&gt;</code> either from a local <code>node_modules/.bin</code>, or from a central cache, installing any packages needed in order for <code>&lt;command&gt;</code> to run. </p>
<p> By default, <code>npx</code> will check whether <code>&lt;command&gt;</code> exists in <code>$PATH</code>, or in the local project binaries, and execute that. If <code>&lt;command&gt;</code> is not found, it will be installed prior to execution. </p>
<p> Unless a <code>&#8211;package</code> option is specified, <code>npx</code> will try to guess the name of the binary to invoke depending on the specifier provided. All package specifiers understood by <code>npm</code> may be used with <code>npx</code>, including git specifiers, remote tarballs, local directories, or scoped packages. </p>
<p> If a full specifier is included, or if <code>&#8211;package</code> is used, npx will always use a freshly-installed, temporary version of the package. This can also be forced with the <code>&#8211;ignore-existing</code> flag.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>-p, &#8211;package &lt;package&gt;</code> &#8211; define the package to be installed. This defaults to the value of <code>&lt;command&gt;</code>. This is only needed for packages with multiple binaries if you want to call one of the other executables, or where the binary name does not match the package name. If this option is provided <code>&lt;command&gt;</code> will be executed as-is, without interpreting <code>@version</code> if it&#8217;s there. Multiple <code>&#8211;package</code> options may be provided, and all the packages specified will be installed.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-install</code> &#8211; If passed to <code>npx</code>, it will only try to run <code>&lt;command&gt;</code> if it already exists in the current path or in <code>$prefix/node_modules/.bin</code>. It won&#8217;t try to install missing commands.</p>
<dt>&bull;</p>
<dd> <code>&#8211;cache &lt;path&gt;</code> &#8211; set the location of the npm cache. Defaults to npm&#8217;s own cache settings.</p>
<dt>&bull;</p>
<dd> <code>&#8211;userconfig &lt;path&gt;</code> &#8211; path to the user configuration file to pass to npm. Defaults to whatever npm&#8217;s current default is.</p>
<dt>&bull;</p>
<dd> <code>-c &lt;string&gt;</code> &#8211; Execute <code>&lt;string&gt;</code> inside an <code>npm run-script</code>-like shell environment, with all the usual environment variables available. Only the first item in <code>&lt;string&gt;</code> will be automatically used as <code>&lt;command&gt;</code>. Any others <i>must</i> use <code>-p</code>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;shell &lt;string&gt;</code> &#8211; The shell to invoke the command with, if any.</p>
<dt>&bull;</p>
<dd> <code>&#8211;shell-auto-fallback [&lt;shell&gt;]</code> &#8211; Generates shell code to override your shell&#8217;s &quot;command not found&quot; handler with one that calls <code>npx</code>. Tries to figure out your shell, or you can pass its name (either <code>bash</code>, <code>fish</code>, or <code>zsh</code>) as an option. See below for how to install.</p>
<dt>&bull;</p>
<dd> <code>&#8211;ignore-existing</code> &#8211; If this flag is set, npx will not look in <code>$PATH</code>, or in the current package&#8217;s <code>node_modules/.bin</code> for an existing version before deciding whether to install. Binaries in those paths will still be available for execution, but will be shadowed by any packages requested by this install.</p>
<dt>&bull;</p>
<dd> <code>-q, &#8211;quiet</code> &#8211; Suppressed any output from npx itself (progress bars, error messages, install reports). Subcommand output itself will not be silenced.</p>
<dt>&bull;</p>
<dd> <code>-n, &#8211;node-arg</code> &#8211; Extra node argument to supply to node when binary is a node script. You can supply this option multiple times to add more arguments.</p>
<dt>&bull;</p>
<dd> <code>-v, &#8211;version</code> &#8211; Show the current npx version. </p>
</dl>
</dl>
<h2>EXAMPLES</h2>
<h3>Running a project-local bin</h3>
<dl>
<dt>
<dd>
<pre>
$ npm i -D webpack
$ npx webpack ...
</pre>
</dl>
<h3>One-off invocation without local installation</h3>
<dl>
<dt>
<dd>
<pre>
$ npm rm webpack
$ npx webpack -- ...
$ cat package.json
...webpack not in &quot;devDependencies&quot;...
</pre>
</dl>
<h3>Invoking a command from a github repository</h3>
<dl>
<dt>
<dd>
<pre>
$ npx github:piuccio/cowsay
...or...
$ npx git+<a href="ssh://my.hosted.git:cowsay.git#semver:^1">ssh://my.hosted.git:cowsay.git#semver:^1</a>
...etc...
</pre>
</dl>
<h3>Execute a full shell command using one npx call w/ multiple packages</h3>
<dl>
<dt>
<dd>
<pre><code>
$ npx -p lolcatjs -p cowsay -c \
  'echo "$npm_package_name@$npm_package_version" | cowsay | lolcatjs'
...
 _____
&lt; your-cool-package [at] 1.2.3 &gt;
 -----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
</code></pre>
</dl>
<h3>Run node binary with &#8211;inspect</h3>
<dl>
<dt>
<dd>
<pre>
$ npx --node-arg=--inspect cowsay
Debugger listening on ws://127.0.0.1:9229/....
</pre>
</dl>
<h3>Specify a node version to run npm scripts (or anything else!)</h3>
<dl>
<dt>
<dd>
<pre>
npx -p node@8 npm run build
</pre>
</dl>
<h2>SHELL AUTO FALLBACK</h2>
<p> You can configure <code>npx</code> to run as your default fallback command when you type something in the command line with an <code>@</code> but the command is not found. This includes installing packages that were not found in the local prefix either. </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ npm@4 --version
(stderr) npm@4 not found. Trying with npx...
4.6.1
$ asdfasdfasf
zsh: command not found: asfdasdfasdf
</pre>
</dl>
<p> Currently, <code>zsh</code>, <code>bash</code> (&gt;= 4), and <code>fish</code> are supported. You can access these completion scripts using <code>npx &#8211;shell-auto-fallback &lt;shell&gt;</code>. </p>
<p> To install permanently, add the relevant line below to your <code>~/.bashrc</code>, <code>~/.zshrc</code>, <code>~/.config/fish/config.fish</code>, or as needed. To install just for the shell session, simply run the line. </p>
<p> You can optionally pass through <code>&#8211;no-install</code> when generating the fallback to prevent it from installing packages if the command is missing.</p>
<h3>For bash@&gt;=4:</h3>
<dl>
<dt>
<dd>
<pre>
$ source &lt;(npx --shell-auto-fallback bash)
</pre>
</dl>
<h3>For zsh:</h3>
<dl>
<dt>
<dd>
<pre>
$ source &lt;(npx --shell-auto-fallback zsh)
</pre>
</dl>
<h3>For fish:</h3>
<dl>
<dt>
<dd>
<pre>
$ source (npx --shell-auto-fallback fish | psub)
</pre>
</dl>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Huge thanks to Kwyn Meagher <i><a rel="nofollow" href="https://blog.kwyn.io">https://blog.kwyn.io</a></i> for generously donating the package name in the main npm registry. Previously <code>npx</code> was used for a Tessel board Neopixels library, which can now be found under <code>npx-tessel</code> <i><a rel="nofollow" href="https://npm.im/npx-tessel">https://npm.im/npx-tessel</a></i>.</p>
<h2>AUTHOR</h2>
<p> Written by Kat Marchan <i><a rel="nofollow" href="https://github.com/npm">https://github.com/npm</a></i>.</p>
<h2>REPORTING BUGS</h2>
<p> Please file any relevant issues on Github. <i><a rel="nofollow" href="https://github.com/npm/npx">https://github.com/npm/npx</a></i></p>
<h2>LICENSE</h2>
<p> This work is released by its authors into the public domain under CC0-1.0. See <code>LICENSE.md</code> for details.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/1-npm/">npm</a>(1)</code></p>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/1-npm-run-script/">npm-run-script</a>(1)</code></p>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/7-npm-config/">npm-config</a>(7)</code> </p>
</dl>
</dl>
<h2>Index</h2>
