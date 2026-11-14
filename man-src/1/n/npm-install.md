---
title: "npm-install(1)"
name: "npm-install"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-install/"
description: "npm-install – Install a package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-install</code> &#8211; Install a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm install(with no args, in package dir)
        npm install[&lt;@scope&gt; / ]&lt;name&gt; npm install[&lt;@scope&gt; / ]&lt;name&gt; @&lt;tag&gt; npm install[&lt;@scope&gt; / ]&lt;name&gt; @&lt;version&gt; npm install[&lt;@scope&gt; / ]&lt;name&gt; @&lt;version range&gt; npm install&lt;alias&gt; @npm : &lt;name&gt; npm install&lt;git - host&gt; : &lt;git - user&gt; /
                                                                                                                                                                                                                                  &lt;repo - name&gt; npm install&lt;git repo url&gt; npm install&lt;tarball file&gt; npm install&lt;tarball url&gt; npm install&lt;folder&gt; aliases : npm i,
    npm add
    common options : [-P | --save - prod | -D | --save - dev | -O | --save - optional][-E | --save - exact][-B | --save - bundle][--no - save][--dry - run]
</code></pre>
</dl>
<h3>Description</h3>
<p> This command installs a package, and any packages that it depends on. If the package has a package-lock or shrinkwrap file, the installation of dependencies will be driven by that, with an <code>npm-shrinkwrap.json</code> taking precedence if both files exist. See npm help package-lock.json and npm help <code>shrinkwrap</code>. </p>
<p> A <code>package</code> is:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> a) a folder containing a program described by a npm help <code>package.json</code> file</p>
<dt>&bull;</p>
<dd> b) a gzipped tarball containing (a)</p>
<dt>&bull;</p>
<dd> c) a url that resolves to (b)</p>
<dt>&bull;</p>
<dd> d) a <code>&lt;name&gt;@&lt;version&gt;</code> that is published on the registry (see npm help <code>registry</code>) with (c)</p>
<dt>&bull;</p>
<dd> e) a <code>&lt;name&gt;@&lt;tag&gt;</code> (see npm help <code>dist-tag</code>) that points to (d)</p>
<dt>&bull;</p>
<dd> f) a <code>&lt;name&gt;</code> that has a &quot;latest&quot; tag satisfying (e)</p>
<dt>&bull;</p>
<dd> g) a <code>&lt;git remote url&gt;</code> that resolves to (a) </p>
</dl>
</dl>
<p> Even if you never publish your package, you can still get a lot of benefits of using npm if you just want to write a node program (a), and perhaps if you also want to be able to easily install it elsewhere after packing it up into a tarball (b).</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>npm install</code> (in package directory, no arguments):<br />
&nbsp;<wbr>&nbsp;Install the dependencies in the local node_modules folder.<br />
&nbsp;<wbr>&nbsp;In global mode&nbsp;(ie, with&nbsp;<code>-g</code>&nbsp;or&nbsp;<code>&#8211;global</code>&nbsp;appended to the command),<br />
&nbsp;<wbr>&nbsp;it installs the current package context&nbsp;(ie, the current working<br />
&nbsp;<wbr>&nbsp;directory)&nbsp;as a global package.<br />
&nbsp;<wbr>&nbsp;By default,&nbsp;<code>npm install</code>&nbsp;will install all modules listed as dependencies<br />
&nbsp;<wbr>&nbsp;in npm help&nbsp;<code>package.json</code>.<br />
&nbsp;<wbr>&nbsp;With the&nbsp;<code>&#8211;production</code>&nbsp;flag&nbsp;(or when the&nbsp;<code>NODE_ENV</code>&nbsp;environment variable<br />
&nbsp;<wbr>&nbsp;is set to&nbsp;<code>production</code>), npm will not install modules listed in<br />
&nbsp;<wbr>&nbsp;<code>devDependencies</code>. To install all modules listed in both&nbsp;<code>dependencies</code>&nbsp;<br />
&nbsp;<wbr>&nbsp;and&nbsp;<code>devDependencies</code>&nbsp;when&nbsp;<code>NODE_ENV</code>&nbsp;environment variable is set to&nbsp;<code>production</code>,&nbsp;<br />
&nbsp;<wbr>&nbsp;you can use&nbsp;<code>&#8211;production=false</code>. NOTE: The <code>&#8211;production</code> flag has no particular meaning when adding a<br />
&nbsp;<wbr>&nbsp;dependency to a project. </p>
<dt>&bull;</p>
<dd> <code>npm install &lt;folder&gt;</code>:<br />
&nbsp;<wbr>&nbsp;Install the package in the directory as a symlink in the current project.<br />
&nbsp;<wbr>&nbsp;Its dependencies will be installed before it&#8217;s linked. If&nbsp;<code>&lt;folder&gt;</code>&nbsp;sits<br />
&nbsp;<wbr>&nbsp;inside the root of your project, its dependencies may be hoisted to the<br />
&nbsp;<wbr>&nbsp;toplevel&nbsp;<code>node_modules</code>&nbsp;as they would for other types of dependencies.</p>
<dt>&bull;</p>
<dd> <code>npm install &lt;tarball file&gt;</code>:<br />
&nbsp;<wbr>&nbsp;Install a package that is sitting on the filesystem.&nbsp;<wbr>&nbsp;Note: if you just want<br />
&nbsp;<wbr>&nbsp;to link a dev directory into your npm root, you can do this more easily by<br />
&nbsp;<wbr>&nbsp;using&nbsp;<code>npm link</code>.<br />
&nbsp;<wbr>&nbsp;Tarball requirements:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The filename <i>must</i> use <code>.tar</code>, <code>.tar.gz</code>, or <code>.tgz</code> as the extension.</p>
<dt>&bull;</p>
<dd> The package contents should reside in a subfolder inside the tarball (usually it is called <code>package/</code>). npm strips one directory layer when installing the package (an equivalent of <code>tar x &#8211;strip-components=1</code> is run).</p>
<dt>&bull;</p>
<dd> The package must contain a <code>package.json</code> file with <code>name</code> and <code>version</code> properties. Example:</dl>
<dl>
<dt>
<dd>
<pre>
npm install ./package.tgz
</pre>
</dl>
</dl>
<dt>&bull;</p>
<dd> <code>npm install &lt;tarball url&gt;</code>:<br />
&nbsp;<wbr>&nbsp;Fetch the tarball url, and then install it.&nbsp;<wbr>&nbsp;In order to distinguish between<br />
&nbsp;<wbr>&nbsp;this and other options, the argument must start with&nbsp;&quot;http://&quot;&nbsp;or&nbsp;&quot;https://&quot;<br />
&nbsp;<wbr>&nbsp;Example:</dl>
<dl>
<dt>
<dd>
<pre>
    npm install <a rel="nofollow" href="https://github.com/indexzero/forever/tarball/v0.5.6">https://github.com/indexzero/forever/tarball/v0.5.6</a>
</pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> <code>npm install [&lt;@scope&gt;/]&lt;name&gt;</code>:<br />
&nbsp;<wbr>&nbsp;Do a&nbsp;<code>&lt;name&gt;@&lt;tag&gt;</code>&nbsp;install, where&nbsp;<code>&lt;tag&gt;</code>&nbsp;is the&nbsp;&quot;tag&quot;&nbsp;config.&nbsp;(See<br />
&nbsp;<wbr>&nbsp;npm help&nbsp;<code>config</code>. The config&#8217;s default value is&nbsp;<code>latest</code>.)<br />
&nbsp;<wbr>&nbsp;In most cases, this will install the version of the modules tagged as<br />
&nbsp;<wbr>&nbsp;<code>latest</code>&nbsp;on the npm registry.<br />
&nbsp;<wbr>&nbsp;Example:</dl>
<dl>
<dt>
<dd>
<pre>
    npm install sax
</pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> <code>npm install &lt;alias&gt;@npm:&lt;name&gt;</code>:<br />
&nbsp;<wbr>&nbsp;Install a package under a custom alias. Allows multiple versions of<br />
&nbsp;<wbr>&nbsp;a same-name package side-by-side, more convenient import names for<br />
&nbsp;<wbr>&nbsp;packages with otherwise long ones and using git forks replacements<br />
&nbsp;<wbr>&nbsp;or forked npm packages as replacements. Aliasing works only on your<br />
&nbsp;<wbr>&nbsp;project and does not rename packages in transitive dependencies.<br />
&nbsp;<wbr>&nbsp;Aliases should follow the naming conventions stated in<br />
&nbsp;<wbr>&nbsp;<code>validate-npm-package-name</code>&nbsp;<i><a rel="nofollow" href="https://www.npmjs.com/package/validate-npm-package-name#naming-rules">https://www.npmjs.com/package/validate-npm-package-name#naming-rules</a></i>.<br />
&nbsp;<wbr>&nbsp;Examples:</dl>
<dl>
<dt>
<dd>
<pre>
    npm install my-react@npm:react
    npm install jquery2@npm:jquery@2
    npm install jquery3@npm:jquery@3
    npm install npa@npm:npm-package-arg
</pre>
</dl>
</dl>
<dl>
<dt>
<dd>
`npm install` saves any specified packages into `dependencies` by default.Additionally, you can control where and how they get saved with some additional flags : * `- P, &#8211;save &#8211; prod`: Package will appear in your `dependencies`.This is the default unless `- D` or `- O` are present.* `- D, &#8211;save &#8211; dev`: Package will appear in your `devDependencies`.* `- O, &#8211;save &#8211; optional`: Package will appear in your `optionalDependencies`.* `&#8211;no &#8211; save`: Prevents saving to `dependencies`.When using any of the above options to save dependencies to your package.json, there are two additional, optional flags : * `- E, &#8211;save &#8211; exact`: Saved dependencies will be configured with an exact version rather than using npm&#8217;s default semver range operator.* `- B, &#8211;save &#8211; bundle`: Saved dependencies will also be added to your `bundleDependencies` list.Further, if you have an `npm &#8211; shrinkwrap.json` or `package &#8211; lock.json` then it will be updated as well.<br />
`&lt;scope&gt;` is optional.The package will be downloaded from the registry associated with the specified scope.If no registry is associated with the given scope the default registry is assumed.See npm help `scope`.Note : if you do not include the @-symbol on your scope name, npm will interpret this as a GitHub repository instead, see below.Scopes names must also be followed by a slash.Examples :<br />
&#8220;`bash npm install sax npm install githubname / reponame npm install @myorg / privatepackage npm install node &#8211; tap&#8211; save &#8211; dev npm install dtrace &#8211; provider&#8211; save &#8211; optional npm install readable &#8211; stream&#8211; save &#8211; exact npm install ansi &#8211; regex&#8211; save &#8211; bundle<br />
&#8220;` **Note ** : If there is a file or folder named `&lt;name&gt;` in the current working directory, then it will try to install that, and only try to fetch the package by name if it is not valid.
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>npm install [&lt;@scope&gt;/]&lt;name&gt;@&lt;tag&gt;</code>:<br />
&nbsp;<wbr>&nbsp;Install the version of the package that is referenced by the specified tag.<br />
&nbsp;<wbr>&nbsp;If the tag does not exist in the registry data for that package, then this<br />
&nbsp;<wbr>&nbsp;will fail.<br />
&nbsp;<wbr>&nbsp;Example:</dl>
<dl>
<dt>
<dd>
npm install sax[at] latest<br />
        npm install @myorg /<br />
    mypackage[at] latest
</dl>
<dl>
<dt>&bull;</p>
<dd> <code>npm install [&lt;@scope&gt;/]&lt;name&gt;@&lt;version&gt;</code>:<br />
&nbsp;<wbr>&nbsp;Install the specified version of the package.&nbsp;<wbr>&nbsp;This will fail if the<br />
&nbsp;<wbr>&nbsp;version has not been published to the registry.<br />
&nbsp;<wbr>&nbsp;Example:</dl>
<dl>
<dt>
<dd>
npm install sax[at] 0.1.1 npm install @myorg / privatepackage[at] 1.5.0
</dl>
<dl>
<dt>&bull;</p>
<dd> <code>npm install [&lt;@scope&gt;/]&lt;name&gt;@&lt;version range&gt;</code>:<br />
&nbsp;<wbr>&nbsp;Install a version of the package matching the specified version range.&nbsp;<wbr>&nbsp;This<br />
&nbsp;<wbr>&nbsp;will follow the same rules for resolving dependencies described in npm help&nbsp;<code>package.json</code>.<br />
&nbsp;<wbr>&nbsp;Note that most version ranges must be put in quotes so that your shell will<br />
&nbsp;<wbr>&nbsp;treat it as a single argument.<br />
&nbsp;<wbr>&nbsp;Example:</dl>
<dl>
<dt>
<dd>
<pre>
  npm install sax@&quot;&gt;=0.1.0 &lt;0.2.0&quot;
  npm install @myorg/privatepackage@&quot;&gt;=0.1.0 &lt;0.2.0&quot;
</pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> <code>npm install &lt;git remote url&gt;</code>:<br />
&nbsp;<wbr>&nbsp;Installs the package from the hosted git provider, cloning it with&nbsp;<code>git</code>.<br />
&nbsp;<wbr>&nbsp;For a full git remote url, only that URL will be attempted.</dl>
<dl>
<dt>
<dd>
    &lt;protocol&gt;://[&lt;user&gt;[:&lt;password&gt;]@]&lt;hostname&gt;[:&lt;port&gt;][:][/]&lt;path&gt;[#&lt;commit-ish&gt; | #semver:&lt;semver&gt;]
</dl>
<p>&nbsp;<wbr>&nbsp;<code>&lt;protocol&gt;</code>&nbsp;is one of&nbsp;<code>git</code>,&nbsp;<code>git+ssh</code>,&nbsp;<code>git+http</code>,&nbsp;<code>git+https</code>, or<br />
&nbsp;<wbr>&nbsp;<code>git+file</code>.<br />
&nbsp;<wbr>&nbsp;If&nbsp;<code>#&lt;commit-ish&gt;</code>&nbsp;is provided, it will be used to clone exactly that<br />
&nbsp;<wbr>&nbsp;commit. If the commit-ish has the format&nbsp;<code>#semver:&lt;semver&gt;</code>,&nbsp;<code>&lt;semver&gt;</code>&nbsp;can<br />
&nbsp;<wbr>&nbsp;be any valid semver range or exact version, and npm will look for any tags<br />
&nbsp;<wbr>&nbsp;or refs matching that range in the remote repository, much as it would for a<br />
&nbsp;<wbr>&nbsp;registry dependency. If neither&nbsp;<code>#&lt;commit-ish&gt;</code>&nbsp;or&nbsp;<code>#semver:&lt;semver&gt;</code>&nbsp;is<br />
&nbsp;<wbr>&nbsp;specified, then the default branch of the repository is used.<br />
&nbsp;<wbr>&nbsp;If the repository makes use of submodules, those submodules will be cloned<br />
&nbsp;<wbr>&nbsp;as well.<br />
&nbsp;<wbr>&nbsp;If the package being installed contains a&nbsp;<code>prepare</code>&nbsp;script, its<br />
&nbsp;<wbr>&nbsp;<code>dependencies</code>&nbsp;and&nbsp;<code>devDependencies</code>&nbsp;will be installed, and the prepare<br />
&nbsp;<wbr>&nbsp;script will be run, before the package is packaged and installed.<br />
&nbsp;<wbr>&nbsp;The following git environment variables are recognized by npm and will be<br />
&nbsp;<wbr>&nbsp;added to the environment when running git:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>GIT_ASKPASS</code></p>
<dt>&bull;</p>
<dd> <code>GIT_EXEC_PATH</code></p>
<dt>&bull;</p>
<dd> <code>GIT_PROXY_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>GIT_SSH</code></p>
<dt>&bull;</p>
<dd> <code>GIT_SSH_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>GIT_SSL_CAINFO</code></p>
<dt>&bull;</p>
<dd> <code>GIT_SSL_NO_VERIFY</code> See the git man page for details. Examples:</dl>
<dl>
<dt>
<dd>
<pre>
npm install git+<a href="ssh://git@github.com:npm/cli.git#v1.0.27">ssh://git@github.com:npm/cli.git#v1.0.27</a>
npm install git+<a href="ssh://git@github.com:npm/cli#semver:^5.0">ssh://git@github.com:npm/cli#semver:^5.0</a>
npm install git+<a rel="nofollow" href="https://isaacs@github.com/npm/cli.git">https://isaacs@github.com/npm/cli.git</a>
npm install <a href="git://github.com/npm/cli.git#v1.0.27">git://github.com/npm/cli.git#v1.0.27</a>
GIT_SSH_COMMAND='ssh -i ~/.ssh/custom_ident' npm install git+<a href="ssh://git@github.com:npm/cli.git">ssh://git@github.com:npm/cli.git</a>
</pre>
</dl>
</dl>
<dl>
<dt>&bull;</p>
<dd> <code>npm install &lt;githubname&gt;/&lt;githubrepo&gt;[#&lt;commit-ish&gt;]</code>:</p>
<dt>&bull;</p>
<dd> <code>npm install github:&lt;githubname&gt;/&lt;githubrepo&gt;[#&lt;commit-ish&gt;]</code>:<br />
&nbsp;<wbr>&nbsp;Install the package at&nbsp;<code><a rel="nofollow" href="https://github.com/githubname/githubrepo">https://github.com/githubname/githubrepo</a></code>&nbsp;by<br />
&nbsp;<wbr>&nbsp;attempting to clone it using&nbsp;<code>git</code>.<br />
&nbsp;<wbr>&nbsp;If&nbsp;<code>#&lt;commit-ish&gt;</code>&nbsp;is provided, it will be used to clone exactly that<br />
&nbsp;<wbr>&nbsp;commit. If the commit-ish has the format&nbsp;<code>#semver:&lt;semver&gt;</code>,&nbsp;<code>&lt;semver&gt;</code>&nbsp;can<br />
&nbsp;<wbr>&nbsp;be any valid semver range or exact version, and npm will look for any tags<br />
&nbsp;<wbr>&nbsp;or refs matching that range in the remote repository, much as it would for a<br />
&nbsp;<wbr>&nbsp;registry dependency. If neither&nbsp;<code>#&lt;commit-ish&gt;</code>&nbsp;or&nbsp;<code>#semver:&lt;semver&gt;</code>&nbsp;is<br />
&nbsp;<wbr>&nbsp;specified, then&nbsp;<code>master</code>&nbsp;is used.<br />
&nbsp;<wbr>&nbsp;As with regular git dependencies,&nbsp;<code>dependencies</code>&nbsp;and&nbsp;<code>devDependencies</code>&nbsp;will<br />
&nbsp;<wbr>&nbsp;be installed if the package has a&nbsp;<code>prepare</code>&nbsp;script, before the package is<br />
&nbsp;<wbr>&nbsp;done installing.<br />
&nbsp;<wbr>&nbsp;Examples:</dl>
<dl>
<dt>
<dd>
<pre>
  npm install mygithubuser/myproject
  npm install github:mygithubuser/myproject
</pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> <code>npm install gist:[&lt;githubname&gt;/]&lt;gistID&gt;[#&lt;commit-ish&gt;|#semver:&lt;semver&gt;]</code>:<br />
&nbsp;<wbr>&nbsp;Install the package at&nbsp;<code><a rel="nofollow" href="https://gist.github.com/gistID">https://gist.github.com/gistID</a></code>&nbsp;by attempting to<br />
&nbsp;<wbr>&nbsp;clone it using&nbsp;<code>git</code>. The GitHub username associated with the gist is<br />
&nbsp;<wbr>&nbsp;optional and will not be saved in&nbsp;<code>package.json</code>.<br />
&nbsp;<wbr>&nbsp;As with regular git dependencies,&nbsp;<code>dependencies</code>&nbsp;and&nbsp;<code>devDependencies</code>&nbsp;will<br />
&nbsp;<wbr>&nbsp;be installed if the package has a&nbsp;<code>prepare</code>&nbsp;script, before the package is<br />
&nbsp;<wbr>&nbsp;done installing.<br />
&nbsp;<wbr>&nbsp;Example:</dl>
<dl>
<dt>
<dd>
<pre>
  npm install gist:101a11beef
</pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> <code>npm install bitbucket:&lt;bitbucketname&gt;/&lt;bitbucketrepo&gt;[#&lt;commit-ish&gt;]</code>:<br />
&nbsp;<wbr>&nbsp;Install the package at&nbsp;<code><a rel="nofollow" href="https://bitbucket.org/bitbucketname/bitbucketrepo">https://bitbucket.org/bitbucketname/bitbucketrepo</a></code><br />
&nbsp;<wbr>&nbsp;by attempting to clone it using&nbsp;<code>git</code>.<br />
&nbsp;<wbr>&nbsp;If&nbsp;<code>#&lt;commit-ish&gt;</code>&nbsp;is provided, it will be used to clone exactly that<br />
&nbsp;<wbr>&nbsp;commit. If the commit-ish has the format&nbsp;<code>#semver:&lt;semver&gt;</code>,&nbsp;<code>&lt;semver&gt;</code>&nbsp;can<br />
&nbsp;<wbr>&nbsp;be any valid semver range or exact version, and npm will look for any tags<br />
&nbsp;<wbr>&nbsp;or refs matching that range in the remote repository, much as it would for a<br />
&nbsp;<wbr>&nbsp;registry dependency. If neither&nbsp;<code>#&lt;commit-ish&gt;</code>&nbsp;or&nbsp;<code>#semver:&lt;semver&gt;</code>&nbsp;is<br />
&nbsp;<wbr>&nbsp;specified, then&nbsp;<code>master</code>&nbsp;is used.<br />
&nbsp;<wbr>&nbsp;As with regular git dependencies,&nbsp;<code>dependencies</code>&nbsp;and&nbsp;<code>devDependencies</code>&nbsp;will<br />
&nbsp;<wbr>&nbsp;be installed if the package has a&nbsp;<code>prepare</code>&nbsp;script, before the package is<br />
&nbsp;<wbr>&nbsp;done installing.<br />
&nbsp;<wbr>&nbsp;Example:</dl>
<dl>
<dt>
<dd>
<pre>
  npm install bitbucket:mybitbucketuser/myproject
</pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> <code>npm install gitlab:&lt;gitlabname&gt;/&lt;gitlabrepo&gt;[#&lt;commit-ish&gt;]</code>:<br />
&nbsp;<wbr>&nbsp;Install the package at&nbsp;<code><a rel="nofollow" href="https://gitlab.com/gitlabname/gitlabrepo">https://gitlab.com/gitlabname/gitlabrepo</a></code><br />
&nbsp;<wbr>&nbsp;by attempting to clone it using&nbsp;<code>git</code>.<br />
&nbsp;<wbr>&nbsp;If&nbsp;<code>#&lt;commit-ish&gt;</code>&nbsp;is provided, it will be used to clone exactly that<br />
&nbsp;<wbr>&nbsp;commit. If the commit-ish has the format&nbsp;<code>#semver:&lt;semver&gt;</code>,&nbsp;<code>&lt;semver&gt;</code>&nbsp;can<br />
&nbsp;<wbr>&nbsp;be any valid semver range or exact version, and npm will look for any tags<br />
&nbsp;<wbr>&nbsp;or refs matching that range in the remote repository, much as it would for a<br />
&nbsp;<wbr>&nbsp;registry dependency. If neither&nbsp;<code>#&lt;commit-ish&gt;</code>&nbsp;or&nbsp;<code>#semver:&lt;semver&gt;</code>&nbsp;is<br />
&nbsp;<wbr>&nbsp;specified, then&nbsp;<code>master</code>&nbsp;is used.<br />
&nbsp;<wbr>&nbsp;As with regular git dependencies,&nbsp;<code>dependencies</code>&nbsp;and&nbsp;<code>devDependencies</code>&nbsp;will<br />
&nbsp;<wbr>&nbsp;be installed if the package has a&nbsp;<code>prepare</code>&nbsp;script, before the package is<br />
&nbsp;<wbr>&nbsp;done installing.<br />
&nbsp;<wbr>&nbsp;Example:</dl>
<dl>
<dt>
<dd>
<pre>
  npm install gitlab:mygitlabuser/myproject
  npm install gitlab:myusr/myproj#semver:^5.0
</pre>
</dl>
</dl>
<p> You may combine multiple arguments, and even multiple types of arguments. For example: </p>
<dl>
<dt>
<dd>
<pre>
npm install sax@&quot;&gt;=0.1.0 &lt;0.2.0&quot; bench supervisor
</pre>
</dl>
<p> The <code>&#8211;tag</code> argument will apply to all of the specified install targets. If a tag with the given name exists, the tagged version is preferred over newer versions. </p>
<p> The <code>&#8211;dry-run</code> argument will report in the usual way what the install would have done without actually installing anything. </p>
<p> The <code>&#8211;package-lock-only</code> argument will only update the <code>package-lock.json</code>, instead of checking <code>node_modules</code> and downloading dependencies. </p>
<p> The <code>-f</code> or <code>&#8211;force</code> argument will force npm to fetch remote resources even if a local copy exists on disk. </p>
<dl>
<dt>
<dd>
<pre>
npm install sax --force
</pre>
</dl>
<p> The <code>&#8211;no-fund</code> argument will hide the message displayed at the end of each install that acknowledges the number of dependencies looking for funding. See <code><a href="/docs/linux/man/1-npm-fund/">npm-fund</a>(1)</code> </p>
<p> The <code>-g</code> or <code>&#8211;global</code> argument will cause npm to install the package globally rather than locally. See npm help folders. </p>
<p> The <code>&#8211;global-style</code> argument will cause npm to install the package into your local <code>node_modules</code> folder with the same layout it uses with the global <code>node_modules</code> folder. Only your direct dependencies will show in <code>node_modules</code> and everything they depend on will be flattened in their <code>node_modules</code> folders. This obviously will eliminate some deduping. </p>
<p> The <code>&#8211;ignore-scripts</code> argument will cause npm to not execute any scripts defined in the package.json. See npm help <code>scripts</code>. </p>
<p> The <code>&#8211;legacy-bundling</code> argument will cause npm to install the package such that versions of npm prior to 1.4, such as the one included with node 0.8, can install the package. This eliminates all automatic deduping. </p>
<p> The <code>&#8211;link</code> argument will cause npm to link global installs into the local space in some cases. </p>
<p> The <code>&#8211;no-bin-links</code> argument will prevent npm from creating symlinks for any binaries the package might contain. </p>
<p> The <code>&#8211;no-optional</code> argument will prevent optional dependencies from being installed. </p>
<p> The <code>&#8211;no-shrinkwrap</code> argument, which will ignore an available package lock or shrinkwrap file and use the package.json instead. </p>
<p> The <code>&#8211;no-package-lock</code> argument will prevent npm from creating a <code>package-lock.json</code> file. When running with package-lock&#8217;s disabled npm will not automatically prune your node modules when installing. </p>
<p> The <code>&#8211;nodedir=/path/to/node/source</code> argument will allow npm to find the node source code so that npm can compile native modules. </p>
<p> The <code>&#8211;only={prod[uction]|dev[elopment]}</code> argument will cause either only <code>devDependencies</code> or only non-<code>devDependencies</code> to be installed regardless of the <code>NODE_ENV</code>. </p>
<p> The <code>&#8211;no-audit</code> argument can be used to disable sending of audit reports to the configured registries. See <code>npm-audit</code> <i>npm-audit</i> for details on what is sent. </p>
<p> See npm help <code>config</code>. Many of the configuration params have some effect on installation, since that&#8217;s most of what npm does.</p>
<h3>Algorithm</h3>
<p> To install a package, npm uses the following algorithm: </p>
<dl>
<dt>
<dd>
<pre>
load the existing node_modules tree from disk
clone the tree
fetch the package.json and assorted metadata and add it to the clone
walk the clone and add any missing dependencies
  dependencies will be added as close to the top as is possible
  without breaking any other modules
compare the original tree with the cloned tree and make a list of
actions to take to convert one to the other
execute all of the actions, deepest first
  kinds of actions are install, update, remove and move
</pre>
</dl>
<p> For this <code>package{dep}</code> structure: <code>A{B,C}, B{C}, C{D}</code>, this algorithm produces: </p>
<dl>
<dt>
<dd>
<pre>
A
+-- B
+-- C
+-- D
</pre>
</dl>
<p> That is, the dependency from B to C is satisfied by the fact that A already caused C to be installed at a higher level. D is still installed at the top level because nothing conflicts with it. </p>
<p> For <code>A{B,C}, B{C,D@1}, C{D@2}</code>, this algorithm produces: </p>
<dl>
<dt>
<dd>
A + &#8211;B + &#8211;C<br />
   `&#8211;D @2 + &#8211;D @1
</dl>
<p> Because B&#8217;s D@1 will be installed in the top level, C now has to install D@2 privately for itself. This algorithm is deterministic, but different trees may be produced if two dependencies are requested for installation in a different order. </p>
<p> See npm help folders for a more detailed description of the specific folder structures that npm creates.</p>
<h3>Limitations of npm&#8217;s Install Algorithm</h3>
<p> npm will refuse to install any package with an identical name to the current package. This can be overridden with the <code>&#8211;force</code> flag, but in most cases can simply be addressed by changing the local package name. </p>
<p> There are some very rare and pathological edge-cases where a cycle can cause npm to try to install a never-ending tree of packages. Here is the simplest case: </p>
<dl>
<dt>
<dd>
<pre><code>
A-&gt;B-&gt;A ' -&gt; B'-&gt;A-&gt;B-&gt;A ' -&gt; B'-&gt;A-&gt;...
</code></pre>
</dl>
<p> where <code>A</code> is some version of a package, and <code>A&#8217;</code> is a different version of the same package. Because <code>B</code> depends on a different version of <code>A</code> than the one that is already in the tree, it must install a separate copy. The same is true of <code>A&#8217;</code>, which must install <code>B&#8217;</code>. Because <code>B&#8217;</code> depends on the original version of <code>A</code>, which has been overridden, the cycle falls into infinite regress. </p>
<p> To avoid this situation, npm flat-out refuses to install any <code>name [at] version</code> that is already present anywhere in the tree of package folder ancestors. A more correct, but more complex, solution would be to symlink the existing version into the new location. If this ever affects a real use-case, it will be investigated.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help update</p>
<dt>&bull;</p>
<dd> npm help audit</p>
<dt>&bull;</p>
<dd> npm help fund</p>
<dt>&bull;</p>
<dd> npm help link</p>
<dt>&bull;</p>
<dd> npm help rebuild</p>
<dt>&bull;</p>
<dd> npm help scripts</p>
<dt>&bull;</p>
<dd> npm help build</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc</p>
<dt>&bull;</p>
<dd> npm help registry</p>
<dt>&bull;</p>
<dd> npm help dist-tag</p>
<dt>&bull;</p>
<dd> npm help uninstall</p>
<dt>&bull;</p>
<dd> npm help shrinkwrap</p>
<dt>&bull;</p>
<dd> npm help package.json </p>
</dl>
</dl>
<h2>Index</h2>
