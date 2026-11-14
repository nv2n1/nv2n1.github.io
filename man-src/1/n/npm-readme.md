---
title: "npm-readme(1)"
name: "npm-readme"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-readme/"
description: "npm – a JavaScript package manager"
---

<p><code>npm</code> &#8211; a JavaScript package manager </p>
<p> Build Status <i></p>
<p> <a rel="nofollow" href="https://travis-ci.org/npm/npm">https://travis-ci.org/npm/npm</a></i></p>
<h2>Synopsis</h2>
<p>This is just enough info to get you up and running. </p>
<p> Much more info will be available via <code>npm help</code> once it&#8217;s installed.</p>
<h2>Important</h2>
<p><code>You need node v6 or higher to run this program.</code> </p>
<p> To install an old <code>and unsupported</code> version of npm that works on node v5 and prior, clone the git repo and dig through the old tags and branches. </p>
<p> <code>npm is configured to use npm, Inc.&#8217;s public registry at <a rel="nofollow" href="https://registry.npmjs.org">https://registry.npmjs.org</a> by default.</code> Use of the npm public registry is subject to terms of use available at <a rel="nofollow" href="https://www.npmjs.com/policies/terms.">https://www.npmjs.com/policies/terms.</a> </p>
<p> You can configure npm to use any compatible registry you like, and even run your own registry. Check out the doc on registries <i><a rel="nofollow" href="https://docs.npmjs.com/misc/registry">https://docs.npmjs.com/misc/registry</a></i>.</p>
<h2>Super Easy Install</h2>
<p>npm is bundled with node <i><a rel="nofollow" href="https://nodejs.org/en/download/">https://nodejs.org/en/download/</a></i>.</p>
<h3>Windows Computers</h3>
<p>Get the MSI <i><a rel="nofollow" href="https://nodejs.org/en/download/">https://nodejs.org/en/download/</a></i>. npm is in it.</p>
<h3>Apple Macintosh Computers</h3>
<p>Get the pkg <i><a rel="nofollow" href="https://nodejs.org/en/download/">https://nodejs.org/en/download/</a></i>. npm is in it.</p>
<h3>Other Sorts of Unices</h3>
<p>Run <code>make install</code>. npm will be installed with node. </p>
<p> If you want a more fancy pants install (a different version, customized paths, etc.) then read on.</p>
<h2>Fancy Install (Unix)</h2>
<p>There&#8217;s a pretty robust install script at <a rel="nofollow" href="https://www.npmjs.com/install.sh.">https://www.npmjs.com/install.sh.</a> You can download that and run it. </p>
<p> Here&#8217;s an example using curl: </p>
<dl COMPACT>
<dd>
<pre>curl -L <a rel="nofollow" href="https://www.npmjs.com/install.sh">https://www.npmjs.com/install.sh</a> | sh</pre>
</dl>
<h3>Slightly Fancier</h3>
<p>You can set any npm configuration params with that script: </p>
<dl COMPACT>
<dd>
<pre>npm_config_prefix=/some/path sh install.sh</pre>
</dl>
<p> Or, you can run it in uber-debuggery mode: </p>
<dl COMPACT>
<dd>
<pre>npm_debug=1 sh install.sh</pre>
</dl>
<h3>Even Fancier</h3>
<p>Get the code with git. Use <code>make</code> to build the docs and do other stuff. If you plan on hacking on npm, <code>make link</code> is your friend. </p>
<p> If you&#8217;ve got the npm source code, you can also semi-permanently set arbitrary config keys using the <code>./configure &#8211;key=val &#8230;</code>, and then run npm commands by doing <code>node bin/npm-cli.js &lt;command&gt; &lt;args&gt;</code>. (This is helpful for testing, or running stuff without actually installing npm itself.)</p>
<h2>Windows Install or Upgrade</h2>
<p>Many improvements for Windows users have been made in npm 3 &#8211; you will have a better experience if you run a recent version of npm. To upgrade, either use Microsoft&#8217;s upgrade tool <i><a rel="nofollow" href="https://github.com/felixrieseberg/npm-windows-upgrade">https://github.com/felixrieseberg/npm-windows-upgrade</a></i>, download a new version of Node <i><a rel="nofollow" href="https://nodejs.org/en/download/">https://nodejs.org/en/download/</a></i>, or follow the Windows upgrade instructions in the Installing/upgrading npm <i><a rel="nofollow" href="https://npm.community/t/installing-upgrading-npm/251/2">https://npm.community/t/installing-upgrading-npm/251/2</a></i> post. </p>
<p> If that&#8217;s not fancy enough for you, then you can fetch the code with git, and mess with it directly.</p>
<h2>Installing on Cygwin</h2>
<p>No.</p>
<h2>Uninstalling</h2>
<p>So sad to see you go. </p>
<dl COMPACT>
<dd>
<pre>sudo npm uninstall npm -g</pre>
</dl>
<p> Or, if that fails, </p>
<dl COMPACT>
<dd>
<pre>sudo make uninstall</pre>
</dl>
<h2>More Severe Uninstalling</h2>
<p>Usually, the above instructions are sufficient. That will remove npm, but leave behind anything you&#8217;ve installed. </p>
<p> If you would like to remove all the packages that you have installed, then you can use the <code>npm ls</code> command to find them, and then <code>npm rm</code> to remove them. </p>
<p> To remove cruft left behind by npm 0.x, you can use the included <code>clean-old.sh</code> script file. You can run it conveniently like this: </p>
<dl COMPACT>
<dd>
<pre>npm explore npm -g -- sh scripts/clean-old.sh</pre>
</dl>
<p> npm uses two configuration files, one for per-user configs, and another for global (every-user) configs. You can view them by doing: </p>
<dl COMPACT>
<dd>
<pre>npm config get userconfig # defaults to ~/.npmrc
npm config get globalconfig # defaults to /usr/local/etc/npmrc</pre>
</dl>
<p> Uninstalling npm does not remove configuration files by default. You must remove them yourself manually if you want them gone. Note that this means that future npm installs will not remember the settings that you have chosen.</p>
<h2>More Docs</h2>
<p>Check out the docs <i><a rel="nofollow" href="https://docs.npmjs.com/">https://docs.npmjs.com/</a></i>. </p>
<p> You can use the <code>npm help</code> command to read any of them. </p>
<p> If you&#8217;re a developer, and you want to use npm to publish your program, you should read this <i><a rel="nofollow" href="https://docs.npmjs.com/misc/developers">https://docs.npmjs.com/misc/developers</a></i>.</p>
<h2>Bugs</h2>
<p>When you find issues, please report them:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>web: <a rel="nofollow" href="https://npm.community/c/bugs">https://npm.community/c/bugs</a> </p>
</dl>
</dl>
<p> Be sure to include <i>all</i> of the output from the npm command that didn&#8217;t work as expected. The <code>npm-debug.log</code> file is also helpful to provide.</p>
<h2>See Also</h2>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-npm/">npm</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-npm-help/">npm-help</a>(1) </p>
</dl>
</dl>
