---
title: "npm-folders(5)"
name: "npm-folders"
section: "5"
letter: "n"
url: "/docs/linux/man/5-npm-folders/"
description: "npm-folders – Folder Structures Used by npm"
---

<p><code>npm-folders</code> &#8211; Folder Structures Used by npm</p>
<h2>Description</h2>
<p>npm puts various things on your computer. That&#8217;s its job. </p>
<p> This document will tell you what it puts where.</p>
<h3>tl;dr</h3>
<dl>
<dt>&bull;</p>
<dd>Local install (default): puts stuff in <code>./node_modules</code> of the current package root.</p>
<dt>&bull;</p>
<dd>Global install (with <code>-g</code>): puts stuff in /usr/local or wherever node is installed.</p>
<dt>&bull;</p>
<dd>Install it <code>locally</code> if you&#8217;re going to <code>require()</code> it.</p>
<dt>&bull;</p>
<dd>Install it <code>globally</code> if you&#8217;re going to run it on the command line.</p>
<dt>&bull;</p>
<dd>If you need both, then install it in both places, or use <code>npm link</code>.</p>
<dd></dl>
<h3>prefix Configuration</h3>
<p>The <code>prefix</code> config defaults to the location where node is installed. On most systems, this is <code>/usr/local</code>, and most of the time is the same as node&#8217;s <code>process.installPrefix</code>. </p>
<p> On windows, this is the exact location of the node.exe binary. On Unix systems, it&#8217;s one level up, since node is typically installed at <code>{prefix}/bin/node</code> rather than <code>{prefix}/node.exe</code>. </p>
<p> When the <code>global</code> flag is set, npm installs things into this prefix. When it is not set, it uses the root of the current package, or the current working directory if not in a package already.</p>
<h3>Node Modules</h3>
<p>Packages are dropped into the <code>node_modules</code> folder under the <code>prefix</code>. When installing locally, this means that you can <code>require(&quot;packagename&quot;)</code> to load its main module, or <code>require(&quot;packagename/lib/path/to/sub/module&quot;)</code> to load other modules. </p>
<p> Global installs on Unix systems go to <code>{prefix}/lib/node_modules</code>. Global installs on Windows go to <code>{prefix}/node_modules</code> (that is, no <code>lib</code> folder.) </p>
<p> Scoped packages are installed the same way, except they are grouped together in a sub-folder of the relevant <code>node_modules</code> folder with the name of that scope prefix by the @ symbol, e.g. <code>npm install @myorg/package</code> would place the package in <code>{prefix}/node_modules/@myorg/package</code>. See npm help 7 <code>scope</code> for more details. </p>
<p> If you wish to <code>require()</code> a package, then install it locally.</p>
<h3>Executables</h3>
<p>When in global mode, executables are linked into <code>{prefix}/bin</code> on Unix, or directly into <code>{prefix}</code> on Windows. </p>
<p> When in local mode, executables are linked into <code>./node_modules/.bin</code> so that they can be made available to scripts run through npm. (For example, so that a test runner will be in the path when you run <code>npm test</code>.)</p>
<h3>Man Pages</h3>
<p>When in global mode, man pages are linked into <code>{prefix}/share/man</code>. </p>
<p> When in local mode, man pages are not installed. </p>
<p> Man pages are not installed on Windows systems.</p>
<h3>Cache</h3>
<p>See npm help <code>npm-cache</code>. Cache files are stored in <code>~/.npm</code> on Posix, or <code>~/npm-cache</code> on Windows. </p>
<p> This is controlled by the <code>cache</code> configuration param.</p>
<h3>Temp Files</h3>
<p>Temporary files are stored by default in the folder specified by the <code>tmp</code> config, which defaults to the TMPDIR, TMP, or TEMP environment variables, or <code>/tmp</code> on Unix and <code>c:\windows	emp</code> on Windows. </p>
<p> Temp files are given a unique folder under this root for each run of the program, and are deleted upon successful exit.</p>
<h2>More Information</h2>
<p>When installing locally, npm first tries to find an appropriate <code>prefix</code> folder. This is so that <code>npm install foo [at] 1.2.3</code> will install to the sensible root of your package, even if you happen to have <code>cd</code>ed into some other folder. </p>
<p> Starting at the $PWD, npm will walk up the folder tree checking for a folder that contains either a <code>package.json</code> file, or a <code>node_modules</code> folder. If such a thing is found, then that is treated as the effective &quot;current directory&quot; for the purpose of running npm commands. (This behavior is inspired by and similar to git&#8217;s .git-folder seeking logic when running git commands in a working dir.) </p>
<p> If no package root is found, then the current folder is used. </p>
<p> When you run <code>npm install foo [at] 1.2.3</code>, then the package is loaded into the cache, and then unpacked into <code>./node_modules/foo</code>. Then, any of foo&#8217;s dependencies are similarly unpacked into <code>./node_modules/foo/node_modules/&#8230;</code>. </p>
<p> Any bin files are symlinked to <code>./node_modules/.bin/</code>, so that they may be found by npm scripts when necessary.</p>
<h3>Global Installation</h3>
<p>If the <code>global</code> configuration is set to true, then npm will install packages &quot;globally&quot;. </p>
<p> For global installation, packages are installed roughly the same way, but using the folders described above.</p>
<h3>Cycles, Conflicts, and Folder Parsimony</h3>
<p>Cycles are handled using the property of node&#8217;s module system that it walks up the directories looking for <code>node_modules</code> folders. So, at every stage, if a package is already installed in an ancestor <code>node_modules</code> folder, then it is not installed at the current location. </p>
<p> Consider the case above, where <code>foo -&gt; bar -&gt; baz</code>. Imagine if, in addition to that, baz depended on bar, so you&#8217;d have: <code>foo -&gt; bar -&gt; baz -&gt; bar -&gt; baz &#8230;</code>. However, since the folder structure is: <code>foo/node_modules/bar/node_modules/baz</code>, there&#8217;s no need to put another copy of bar into <code>&#8230;/baz/node_modules</code>, since when it calls require(&quot;bar&quot;), it will get the copy that is installed in <code>foo/node_modules/bar</code>. </p>
<p> This shortcut is only used if the exact same version would be installed in multiple nested <code>node_modules</code> folders. It is still possible to have <code>a/node_modules/b/node_modules/a</code> if the two &quot;a&quot; packages are different versions. However, without repeating the exact same package multiple times, an infinite regress will always be prevented. </p>
<p> Another optimization can be made by installing dependencies at the highest level possible, below the localized &quot;target&quot; folder.</p>
<h3>Example</h3>
<p>Consider this dependency graph:</p>
<dl>
<dd>
<pre>foo
+-- blerg [at] 1.2.5
+-- bar [at] 1.2.3
| +-- blerg@1.x (latest=1.3.7)
| +-- baz@2.x
| | `-- quux@3.x
| | `-- bar [at] 1.2.3 (cycle)
| `-- asdf@*
`-- baz [at] 1.2.3
 `-- quux@3.x
 `-- bar</pre>
<dd></dl>
<p> In this case, we might expect a folder structure like this:</p>
<dl>
<dd>
<pre>foo
+-- node_modules
 +-- blerg (1.2.5) &lt;---[A]
 +-- bar (1.2.3) &lt;---[B]
 | `-- node_modules
 | +-- baz (2.0.2) &lt;---[C]
 | | `-- node_modules
 | | `-- quux (3.2.0)
 | `-- asdf (2.3.4)
 `-- baz (1.2.3) &lt;---[D]
 `-- node_modules
 `-- quux (3.2.0) &lt;---[E]</pre>
<dd></dl>
<p> Since foo depends directly on <code>bar [at] 1.2.3</code> and <code>baz [at] 1.2.3</code>, those are installed in foo&#8217;s <code>node_modules</code> folder. </p>
<p> Even though the latest copy of blerg is 1.3.7, foo has a specific dependency on version 1.2.5. So, that gets installed at [A]. Since the parent installation of blerg satisfies bar&#8217;s dependency on <code>blerg@1.x</code>, it does not install another copy under [B]. </p>
<p> Bar [B] also has dependencies on baz and asdf, so those are installed in bar&#8217;s <code>node_modules</code> folder. Because it depends on <code>baz@2.x</code>, it cannot re-use the <code>baz [at] 1.2.3</code> installed in the parent <code>node_modules</code> folder [D], and must install its own copy [C]. </p>
<p> Underneath bar, the <code>baz -&gt; quux -&gt; bar</code> dependency creates a cycle. However, because bar is already in quux&#8217;s ancestry [B], it does not unpack another copy of bar into that folder. </p>
<p> Underneath <code>foo -&gt; baz</code> [D], quux&#8217;s [E] folder tree is empty, because its dependency on bar is satisfied by the parent folder copy installed at [B]. </p>
<p> For a graphical breakdown of what is installed where, use <code>npm ls</code>.</p>
<h3>Publishing</h3>
<p>Upon publishing, npm will look in the <code>node_modules</code> folder. If any of the items there are not in the <code>bundledDependencies</code> array, then they will not be included in the package tarball. </p>
<p> This allows a package maintainer to install all of their dependencies (and dev dependencies) locally, but only re-publish those items that cannot be found elsewhere. See npm help 5 <code>package.json</code> for more information.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help 7 faq</p>
<dt>&bull;</p>
<dd>npm help 5 package.json</p>
<dt>&bull;</p>
<dd>npm help install</p>
<dt>&bull;</p>
<dd>npm help pack</p>
<dt>&bull;</p>
<dd>npm help cache</p>
<dt>&bull;</p>
<dd>npm help config</p>
<dt>&bull;</p>
<dd>npm help 5 npmrc</p>
<dt>&bull;</p>
<dd>npm help 7 config</p>
<dt>&bull;</p>
<dd>npm help publish</p>
<dd>
