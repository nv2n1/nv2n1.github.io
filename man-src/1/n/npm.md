---
title: "npm(1)"
name: "npm"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm/"
description: "npm – javascript package manager"
---

<h2 class="name">NAME</h2>
<p> <code>npm</code> &#8211; javascript package manager </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm &lt;command&gt; [args]
</pre>
</dl>
<h3>Version</h3>
<p> 6.14.4</p>
<h3>Description</h3>
<p> npm is the package manager for the Node JavaScript platform. It puts modules in place so that node can find them, and manages dependency conflicts intelligently. </p>
<p> It is extremely configurable to support a wide variety of use cases. Most commonly, it is used to publish, discover, install, and develop node programs. </p>
<p> Run <code>npm help</code> to get a list of available commands.</p>
<h3>Important</h3>
<p> npm is configured to use npm, Inc.&#8217;s public registry at <a rel="nofollow" href="https://registry.npmjs.org">https://registry.npmjs.org</a> by default. Use of the npm public registry is subject to terms of use available at <a rel="nofollow" href="https://www.npmjs.com/policies/terms.">https://www.npmjs.com/policies/terms.</a> </p>
<p> You can configure npm to use any compatible registry you like, and even run your own registry. Use of someone else&#8217;s registry may be governed by their terms of use.</p>
<h3>Introduction</h3>
<p> You probably got npm because you want to install stuff. </p>
<p> Use <code>npm install blerg</code> to install the latest version of &quot;blerg&quot;. Check out npm help <code>install</code> for more info. It can do a lot of stuff. </p>
<p> Use the <code>npm search</code> command to show everything that&#8217;s available. Use <code>npm ls</code> to show everything you&#8217;ve installed.</p>
<h3>Dependencies</h3>
<p> If a package references to another package with a git URL, npm depends on a preinstalled git. </p>
<p> If one of the packages npm tries to install is a native node module and requires compiling of C++ Code, npm will use node-gyp <i><a rel="nofollow" href="https://github.com/TooTallNate/node-gyp">https://github.com/TooTallNate/node-gyp</a></i> for that task. For a Unix system, node-gyp <i><a rel="nofollow" href="https://github.com/TooTallNate/node-gyp">https://github.com/TooTallNate/node-gyp</a></i> needs Python, make and a buildchain like GCC. On Windows, Python and Microsoft Visual Studio C++ are needed. Python 3 is not supported by node-gyp <i><a rel="nofollow" href="https://github.com/TooTallNate/node-gyp">https://github.com/TooTallNate/node-gyp</a></i>. For more information visit the node-gyp repository <i><a rel="nofollow" href="https://github.com/TooTallNate/node-gyp">https://github.com/TooTallNate/node-gyp</a></i> and the node-gyp Wiki <i><a rel="nofollow" href="https://github.com/TooTallNate/node-gyp/wiki">https://github.com/TooTallNate/node-gyp/wiki</a></i>.</p>
<h3>Directories</h3>
<p> See npm help <code>folders</code> to learn about where npm puts stuff. </p>
<p> In particular, npm has two modes of operation:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> global mode: npm installs packages into the install prefix at <code>prefix/lib/node_modules</code> and bins are installed in <code>prefix/bin</code>.</p>
<dt>&bull;</p>
<dd> local mode: npm installs packages into the current project directory, which defaults to the current working directory. Packages are installed to <code>./node_modules</code>, and bins are installed to <code>./node_modules/.bin</code>. </p>
</dl>
</dl>
<p> Local mode is the default. Use <code>-g</code> or <code>&#8211;global</code> on any command to operate in global mode instead.</p>
<h3>Developer Usage</h3>
<p> If you&#8217;re using npm to develop and publish your code, check out the following help topics:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> json: Make a package.json file. See npm help <code>package.json</code>.</p>
<dt>&bull;</p>
<dd> link: For linking your current working code into Node&#8217;s path, so that you don&#8217;t have to reinstall every time you make a change. Use <code>npm link</code> to do this.</p>
<dt>&bull;</p>
<dd> install: It&#8217;s a good idea to install things if you don&#8217;t need the symbolic link. Especially, installing other peoples code from the registry is done via <code>npm install</code></p>
<dt>&bull;</p>
<dd> adduser: Create an account or log in. Credentials are stored in the user config file.</p>
<dt>&bull;</p>
<dd> publish: Use the <code>npm publish</code> command to upload your code to the registry. </p>
</dl>
</dl>
<h3>Configuration</h3>
<p> npm is extremely configurable. It reads its configuration options from 5 places.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Command line switches: Set a config with <code>&#8211;key val</code>. All keys take a value, even if they are booleans (the config parser doesn&#8217;t know what the options are at the time of parsing). If no value is provided, then the option is set to boolean <code>true</code>.</p>
<dt>&bull;</p>
<dd> Environment Variables: Set any config by prefixing the name in an environment variable with <code>npm_config_</code>. For example, <code>export npm_config_key=val</code>.</p>
<dt>&bull;</p>
<dd> User Configs: The file at $HOME/.npmrc is an ini-formatted list of configs. If present, it is parsed. If the <code>userconfig</code> option is set in the cli or env, then that will be used instead.</p>
<dt>&bull;</p>
<dd> Global Configs: The file found at ../etc/npmrc (from the node executable, by default this resolves to /usr/local/etc/npmrc) will be parsed if it is found. If the <code>globalconfig</code> option is set in the cli, env, or user config, then that file is parsed instead.</p>
<dt>&bull;</p>
<dd> Defaults: npm&#8217;s default configuration options are defined in lib/utils/config-defs.js. These must not be changed. </p>
</dl>
</dl>
<p> See npm help <code>config</code> for much much more information.</p>
<h3>Contributions</h3>
<p> Patches welcome! </p>
<p> If you would like to contribute, but don&#8217;t know what to work on, read the contributing guidelines and check the issues list.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> CONTRIBUTING.md <i><a rel="nofollow" href="https://github.com/npm/cli/blob/latest/CONTRIBUTING.md">https://github.com/npm/cli/blob/latest/CONTRIBUTING.md</a></i></p>
<dt>&bull;</p>
<dd> Bug tracker <i><a rel="nofollow" href="https://github.com/npm/cli/issues">https://github.com/npm/cli/issues</a></i> </p>
</dl>
</dl>
<h3>Bugs</h3>
<p> When you find issues, please report them:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> web: <a rel="nofollow" href="https://npm.community/c/bugs">https://npm.community/c/bugs</a> </p>
</dl>
</dl>
<p> Be sure to follow the template and bug reporting guidelines. You can also ask for help in the support forum <i><a rel="nofollow" href="https://npm.community/c/support">https://npm.community/c/support</a></i> if you&#8217;re unsure if it&#8217;s actually a bug or are having trouble coming up with a detailed reproduction to report.</p>
<h3>Author</h3>
<p> Isaac Z. Schlueter <i><a rel="nofollow" href="http://blog.izs.me/">http://blog.izs.me/</a></i> :: isaacs <i><a rel="nofollow" href="https://github.com/isaacs/">https://github.com/isaacs/</a></i> :: @izs <i><a rel="nofollow" href="https://twitter.com/izs">https://twitter.com/izs</a></i> :: i@izs.me</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help help</p>
<dt>&bull;</p>
<dd> npm help package.json</p>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc </p>
</dl>
</dl>
<h2>Index</h2>
