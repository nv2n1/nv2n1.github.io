---
title: "npm-developers(7)"
name: "npm-developers"
section: "7"
letter: "n"
url: "/docs/linux/man/7-npm-developers/"
description: "npm-developers – Developer Guide"
---

<p><code>npm-developers</code> &#8211; Developer Guide</p>
<h2>Description</h2>
<p>So, you&#8217;ve decided to use npm to develop (and maybe publish/deploy) your project. </p>
<p> Fantastic! </p>
<p> There are a few things that you need to do above the simple steps that your users will do to install your program.</p>
<h2>About These Documents</h2>
<p>These are man pages. If you install npm, you should be able to then do <code>man npm-thing</code> to get the documentation on a particular topic, or <code>npm help thing</code> to see the same information.</p>
<h2>What is a &lt;code&gt;package&lt;/code&gt;</h2>
<p>A package is:</p>
<dl>
<dt>&bull;</p>
<dd>a) a folder containing a program described by a package.json file</p>
<dt>&bull;</p>
<dd>b) a gzipped tarball containing (a)</p>
<dt>&bull;</p>
<dd>c) a url that resolves to (b)</p>
<dt>&bull;</p>
<dd>d) a <code>&lt;name&gt;@&lt;version&gt;</code> that is published on the registry with (c)</p>
<dt>&bull;</p>
<dd>e) a <code>&lt;name&gt;@&lt;tag&gt;</code> that points to (d)</p>
<dt>&bull;</p>
<dd>f) a <code>&lt;name&gt;</code> that has a &quot;latest&quot; tag satisfying (e)</p>
<dt>&bull;</p>
<dd>g) a <code>git</code> url that, when cloned, results in (a).</p>
<dd></dl>
<p> Even if you never publish your package, you can still get a lot of benefits of using npm if you just want to write a node program (a), and perhaps if you also want to be able to easily install it elsewhere after packing it up into a tarball (b). </p>
<p> Git urls can be of the form:</p>
<dl>
<dd>
<pre><a href="git://github.com/user/project.git#commit-ish">git://github.com/user/project.git#commit-ish</a>
git+<a href="ssh://user@hostname:project.git#commit-ish">ssh://user@hostname:project.git#commit-ish</a>
git+<a rel="nofollow" href="http://user@hostname/project/blah.git#commit-ish">http://user@hostname/project/blah.git#commit-ish</a>
git+<a rel="nofollow" href="https://user@hostname/project/blah.git#commit-ish">https://user@hostname/project/blah.git#commit-ish</a></pre>
<dd></dl>
<p> The <code>commit-ish</code> can be any tag, sha, or branch which can be supplied as an argument to <code>git checkout</code>. The default is <code>master</code>.</p>
<h2>The package.json File</h2>
<p>You need to have a <code>package.json</code> file in the root of your project to do much of anything with npm. That is basically the whole interface. </p>
<p> See npm help 5 <code>package.json</code> for details about what goes in that file. At the very least, you need:</p>
<dl>
<dt>name</p>
<dd>This should be a string that identifies your project. Please do not use the name to specify that it runs on node, or is in JavaScript. You can use the &quot;engines&quot; field to explicitly state the versions of node (or whatever else) that your program requires, and it&#8217;s pretty well assumed that it&#8217;s javascript.</p>
<dd>It does not necessarily need to match your github repository name.</p>
<dd>So, <code>node-foo</code> and <code>bar-js</code> are bad names. <code>foo</code> or <code>bar</code> are better.</p>
<dt>version</p>
<dd>A semver-compatible version.</p>
<dt>engines</p>
<dd>Specify the versions of node (or whatever else) that your program runs on. The node API changes a lot, and there may be bugs or new functionality that you depend on. Be explicit.</p>
<dt>author</p>
<dd>Take some credit.</p>
<dt>scripts</p>
<dd>If you have a special compilation or installation script, then you should put it in the <code>scripts</code> object. You should definitely have at least a basic smoke-test command as the &quot;scripts.test&quot; field. See npm help 7 scripts.</p>
<dt>main</p>
<dd>If you have a single module that serves as the entry point to your program (like what the &quot;foo&quot; package gives you at require(&quot;foo&quot;)), then you need to specify that in the &quot;main&quot; field.</p>
<dt>directories</p>
<dd>This is an object mapping names to folders. The best ones to include are &quot;lib&quot; and &quot;doc&quot;, but if you use &quot;man&quot; to specify a folder full of man pages, they&#8217;ll get installed just like these ones.</dl>
<p> You can use <code>npm init</code> in the root of your package in order to get you started with a pretty basic package.json file. See npm help <code>npm-init</code> for more info.</p>
<h2>Keeping files &lt;em&gt;out&lt;/em&gt; of your package</h2>
<p>Use a <code>.npmignore</code> file to keep stuff out of your package. If there&#8217;s no <code>.npmignore</code> file, but there <i>is</i> a <code>.gitignore</code> file, then npm will ignore the stuff matched by the <code>.gitignore</code> file. If you <i>want</i> to include something that is excluded by your <code>.gitignore</code> file, you can create an empty <code>.npmignore</code> file to override it. Like <code>git</code>, <code>npm</code> looks for <code>.npmignore</code> and <code>.gitignore</code> files in all subdirectories of your package, not only the root directory. </p>
<p> <code>.npmignore</code> files follow the same pattern rules <i><a rel="nofollow" href="http://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Ignoring-Files">http://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Ignoring-Files</a></i> as <code>.gitignore</code> files:</p>
<dl>
<dt>&bull;</p>
<dd>Blank lines or lines starting with <code>#</code> are ignored.</p>
<dt>&bull;</p>
<dd>Standard glob patterns work.</p>
<dt>&bull;</p>
<dd>You can end patterns with a forward slash <code>/</code> to specify a directory.</p>
<dt>&bull;</p>
<dd>You can negate a pattern by starting it with an exclamation point <code>!</code>.</p>
<dd></dl>
<p> By default, the following paths and files are ignored, so there&#8217;s no need to add them to <code>.npmignore</code> explicitly:</p>
<dl>
<dt>&bull;</p>
<dd><code>.*.swp</code></p>
<dt>&bull;</p>
<dd><code>._*</code></p>
<dt>&bull;</p>
<dd><code>.DS_Store</code></p>
<dt>&bull;</p>
<dd><code>.git</code></p>
<dt>&bull;</p>
<dd><code>.hg</code></p>
<dt>&bull;</p>
<dd><code>.npmrc</code></p>
<dt>&bull;</p>
<dd><code>.lock-wscript</code></p>
<dt>&bull;</p>
<dd><code>.svn</code></p>
<dt>&bull;</p>
<dd><code>.wafpickle-*</code></p>
<dt>&bull;</p>
<dd><code>config.gypi</code></p>
<dt>&bull;</p>
<dd><code>CVS</code></p>
<dt>&bull;</p>
<dd><code>npm-debug.log</code></p>
<dd></dl>
<p> Additionally, everything in <code>node_modules</code> is ignored, except for bundled dependencies. npm automatically handles this for you, so don&#8217;t bother adding <code>node_modules</code> to <code>.npmignore</code>. </p>
<p> The following paths and files are never ignored, so adding them to <code>.npmignore</code> is pointless:</p>
<dl>
<dt>&bull;</p>
<dd><code>package.json</code></p>
<dt>&bull;</p>
<dd><code>README</code> (and its variants)</p>
<dt>&bull;</p>
<dd><code>CHANGELOG</code> (and its variants)</p>
<dt>&bull;</p>
<dd><code>LICENSE</code> / <code>LICENCE</code></p>
<dd></dl>
<h2>Link Packages</h2>
<p><code>npm link</code> is designed to install a development package and see the changes in real time without having to keep re-installing it. (You do need to either re-link or <code>npm rebuild -g</code> to update compiled packages, of course.) </p>
<p> More info at npm help <code>npm-link</code>.</p>
<h2>Before Publishing: Make Sure Your Package Installs and Works</h2>
<p><code>This is important.</code> </p>
<p> If you can not install it locally, you&#8217;ll have problems trying to publish it. Or, worse yet, you&#8217;ll be able to publish it, but you&#8217;ll be publishing a broken or pointless package. So don&#8217;t do that. </p>
<p> In the root of your package, do this:</p>
<dl>
<dd>
<pre>npm install . -g</pre>
<dd></dl>
<p> That&#8217;ll show you that it&#8217;s working. If you&#8217;d rather just create a symlink package that points to your working directory, then do this:</p>
<dl>
<dd>
<pre>npm link</pre>
<dd></dl>
<p> Use <code>npm ls -g</code> to see if it&#8217;s there. </p>
<p> To test a local install, go into some other folder, and then do:</p>
<dl>
<dd>
<pre>cd ../some-other-folder
npm install ../my-package</pre>
<dd></dl>
<p> to install it locally into the node_modules folder in that other place. </p>
<p> Then go into the node-repl, and try using require(&quot;my-thing&quot;) to bring in your module&#8217;s main module.</p>
<h2>Create a User Account</h2>
<p>Create a user with the adduser command. It works like this:</p>
<dl>
<dd>
<pre>npm adduser</pre>
<dd></dl>
<p> and then follow the prompts. </p>
<p> This is documented better in npm help adduser.</p>
<h2>Publish your package</h2>
<p>This part&#8217;s easy. In the root of your folder, do this:</p>
<dl>
<dd>
<pre>npm publish</pre>
<dd></dl>
<p> You can give publish a url to a tarball, or a filename of a tarball, or a path to a folder. </p>
<p> Note that pretty much <code>everything in that folder will be exposed</code> by default. So, if you have secret stuff in there, use a <code>.npmignore</code> file to list out the globs to ignore, or publish from a fresh checkout.</p>
<h2>Brag about it</h2>
<p>Send emails, write blogs, blab in IRC. </p>
<p> Tell the world how easy it is to install your program!</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help 7 faq</p>
<dt>&bull;</p>
<dd>npm help npm</p>
<dt>&bull;</p>
<dd>npm help init</p>
<dt>&bull;</p>
<dd>npm help 5 package.json</p>
<dt>&bull;</p>
<dd>npm help 7 scripts</p>
<dt>&bull;</p>
<dd>npm help publish</p>
<dt>&bull;</p>
<dd>npm help adduser</p>
<dt>&bull;</p>
<dd>npm help 7 registry</p>
<dd>
