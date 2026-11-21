---
title: "package-json(5)"
name: "package-json"
section: "5"
letter: "p"
url: "/docs/linux/man/5-package-json/"
description: "The most important things in your package.json are the name and version fields. Those are actually required, and your package won’t install without them. The name and version together form an ident..."
---
<p> <code>package.json</code> - Specifics of npm&#8217;s package.json handling </p>
<h3>Description</h3>
<p>This document is all you need to know about what&#8217;s required in your package.json file. It must be actual JSON, not just a JavaScript object literal. </p>
<p>A lot of the behavior described in this document is affected by the config settings described in npm help <code>config</code>.  </p>
<h3>name</h3>
<p>If you plan to publish your package, the <i>most</i> important things in your package.json are the name and version fields as they will be required. The name and version together form an identifier that is assumed to be completely unique. Changes to the package should come along with changes to the version. If you don&#8217;t plan to publish your package, the name and version fields are optional. </p>
<p>The name is what your thing is called. </p>
<p>Some rules: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The name must be less than or equal to 214 characters. This includes the scope for scoped packages. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The names of scoped packages can begin with a dot or an underscore. This is not permitted without a scope. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New packages must not have uppercase letters in the name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The name ends up being part of a URL, an argument on the command line, and a folder name. Therefore, the name can&#8217;t contain any non-URL-safe characters. </p>
 </dd></dl>
</dl>
<p>Some tips: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Don&#8217;t use the same name as a core Node module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Don&#8217;t put &quot;js&quot; or &quot;node&quot; in the name. It&#8217;s assumed that it&#8217;s js, since you&#8217;re writing a package.json file, and you can specify the engine using the &quot;engines&quot; field. (See below.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The name will probably be passed as an argument to require(), so it should be something short, but also reasonably descriptive. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You may want to check the npm registry to see if there&#8217;s something by that name already, before you get too attached to it. <a rel="nofollow" href="https://www.npmjs.com/">https://www.npmjs.com/</a> </p>
 </dd></dl>
</dl>
<p>A name can be optionally prefixed by a scope, e.g. <code>@myorg/mypackage</code>. See npm help <code>scope</code> for more detail.  </p>
<h3>version</h3>
<p>If you plan to publish your package, the <i>most</i> important things in your package.json are the name and version fields as they will be required. The name and version together form an identifier that is assumed to be completely unique. Changes to the package should come along with changes to the version. If you don&#8217;t plan to publish your package, the name and version fields are optional. </p>
<p>Version must be parseable by node-semver <i><a rel="nofollow" href="https://github.com/isaacs/node-semver">https://github.com/isaacs/node-semver</a></i>, which is bundled with npm as a dependency. (<code>npm install semver</code> to use it yourself.) </p>
<p>More on version numbers and ranges at npm help semver.  </p>
<h3>description</h3>
<p>Put a description in it. It&#8217;s a string. This helps people discover your package, as it&#8217;s listed in <code>npm search</code>.  </p>
<h3>keywords</h3>
<p>Put keywords in it. It&#8217;s an array of strings. This helps people discover your package as it&#8217;s listed in <code>npm search</code>.  </p>
<h3>homepage</h3>
<p>The url to the project homepage. </p>
<p>Example: </p>
<dl>
<dd> <pre><code>&quot;homepage&quot;: &quot;https://github.com/owner/project#readme&quot;
</code></pre>
 </dd></dl>
<h3>bugs</h3>
<p>The url to your project&#8217;s issue tracker and / or the email address to which issues should be reported. These are helpful for people who encounter issues with your package. </p>
<p>It should look like this: </p>
<dl>
<dd> <pre><code>{ &quot;url&quot; : &quot;https://github.com/owner/project/issues&quot;
, &quot;email&quot; : &quot;project [at] hostname.com&quot;
}
</code></pre>
 </dd></dl>
<p>You can specify either one or both values. If you want to provide only a url, you can specify the value for &quot;bugs&quot; as a simple string instead of an object. </p>
<p>If a url is provided, it will be used by the <code>npm bugs</code> command.  </p>
<h3>license</h3>
<p>You should specify a license for your package so that people know how they are permitted to use it, and any restrictions you&#8217;re placing on it. </p>
<p>If you&#8217;re using a common license such as BSD-2-Clause or MIT, add a current SPDX license identifier for the license you&#8217;re using, like this: </p>
<dl>
<dd> <pre><code>{ &quot;license&quot; : &quot;BSD-3-Clause&quot; }
</code></pre>
 </dd></dl>
<p>You can check the full list of SPDX license IDs <i><a rel="nofollow" href="https://spdx.org/licenses/">https://spdx.org/licenses/</a></i>. Ideally you should pick one that is OSI <i><a rel="nofollow" href="https://opensource.org/licenses/alphabetical">https://opensource.org/licenses/alphabetical</a></i> approved. </p>
<p>If your package is licensed under multiple common licenses, use an SPDX license expression syntax version 2.0 string <i><a rel="nofollow" href="https://www.npmjs.com/package/spdx">https://www.npmjs.com/package/spdx</a></i>, like this: </p>
<dl>
<dd> <pre><code>{ &quot;license&quot; : &quot;(ISC OR GPL-3.0)&quot; }
</code></pre>
 </dd></dl>
<p>If you are using a license that hasn&#8217;t been assigned an SPDX identifier, or if you are using a custom license, use a string value like this one: </p>
<dl>
<dd> <pre><code>{ &quot;license&quot; : &quot;SEE LICENSE IN &lt;filename&gt;&quot; }
</code></pre>
 </dd></dl>
<p>Then include a file named <code>&lt;filename&gt;</code> at the top level of the package. </p>
<p>Some old packages used license objects or a &quot;licenses&quot; property containing an array of license objects: </p>
<dl>
<dd> <pre><code>// Not valid metadata
{ &quot;license&quot; :
  { &quot;type&quot; : &quot;ISC&quot;
  , &quot;url&quot; : &quot;https://opensource.org/licenses/ISC&quot;
  }
}
// Not valid metadata
{ &quot;licenses&quot; :
  [
    { &quot;type&quot;: &quot;MIT&quot;
    , &quot;url&quot;: &quot;https://www.opensource.org/licenses/mit-license.php&quot;
    }
  , { &quot;type&quot;: &quot;Apache-2.0&quot;
    , &quot;url&quot;: &quot;https://opensource.org/licenses/apache2.0.php&quot;
    }
  ]
}
</code></pre>
 </dd></dl>
<p>Those styles are now deprecated. Instead, use SPDX expressions, like this: </p>
<dl>
<dd> <pre><code>{ &quot;license&quot;: &quot;ISC&quot; }
{ &quot;license&quot;: &quot;(MIT OR Apache-2.0)&quot; }
</code></pre>
 </dd></dl>
<p>Finally, if you do not wish to grant others the right to use a private or unpublished package under any terms: </p>
<dl>
<dd> <pre><code>{ &quot;license&quot;: &quot;UNLICENSED&quot; }
</code></pre>
 </dd></dl>
<p>Consider also setting <code>&quot;private&quot;: true</code> to prevent accidental publication.  </p>
<h3>people fields: author, contributors</h3>
<p>The &quot;author&quot; is one person. &quot;contributors&quot; is an array of people. A &quot;person&quot; is an object with a &quot;name&quot; field and optionally &quot;url&quot; and &quot;email&quot;, like this: </p>
<dl>
<dd> <pre><code>{ &quot;name&quot; : &quot;Barney Rubble&quot;
, &quot;email&quot; : &quot;b@rubble.com&quot;
, &quot;url&quot; : &quot;http://barnyrubble.tumblr.com/&quot;
}
</code></pre>
 </dd></dl>
<p>Or you can shorten that all into a single string, and npm will parse it for you: </p>
<dl>
<dd> <pre><code>&quot;Barney Rubble &lt;b@rubble.com&gt; (http://barnyrubble.tumblr.com/)&quot;
</code></pre>
 </dd></dl>
<p>Both email and url are optional either way. </p>
<p>npm also sets a top-level &quot;maintainers&quot; field with your npm user info.  </p>
<h3>funding</h3>
<p>You can specify an object containing an URL that provides up-to-date information about ways to help fund development of your package, or a string URL, or an array of these: </p>
<dl>
<dd> <pre><code>&quot;funding&quot;: {
  &quot;type&quot; : &quot;individual&quot;,
  &quot;url&quot; : &quot;http://example.com/donate&quot;
}
&quot;funding&quot;: {
  &quot;type&quot; : &quot;patreon&quot;,
  &quot;url&quot; : &quot;https://www.patreon.com/my-account&quot;
}
&quot;funding&quot;: &quot;http://example.com/donate&quot;
&quot;funding&quot;: [
  {
    &quot;type&quot; : &quot;individual&quot;,
    &quot;url&quot; : &quot;http://example.com/donate&quot;
  },
  &quot;http://example.com/donateAlso&quot;,
  {
    &quot;type&quot; : &quot;patreon&quot;,
    &quot;url&quot; : &quot;https://www.patreon.com/my-account&quot;
  }
]
</code></pre>
 </dd></dl>
<p>Users can use the <code>npm fund</code> subcommand to list the <code>funding</code> URLs of all dependencies of their project, direct and indirect. A shortcut to visit each funding url is also available when providing the project name such as: <code>npm fund &lt;projectname&gt;</code> (when there are multiple URLs, the first one will be visited)  </p>
<h3>files</h3>
<p>The optional <code>files</code> field is an array of file patterns that describes the entries to be included when your package is installed as a dependency. File patterns follow a similar syntax to <code>.gitignore</code>, but reversed: including a file, directory, or glob pattern (<code>*</code>, <code>**/*</code>, and such) will make it so that file is included in the tarball when it&#8217;s packed. Omitting the field will make it default to <code>[&quot;*&quot;]</code>, which means it will include all files. </p>
<p>Some special files and directories are also included or excluded regardless of whether they exist in the <code>files</code> array (see below). </p>
<p>You can also provide a <code>.npmignore</code> file in the root of your package or in subdirectories, which will keep files from being included. At the root of your package it will not override the &quot;files&quot; field, but in subdirectories it will. The <code>.npmignore</code> file works just like a <code>.gitignore</code>. If there is a <code>.gitignore</code> file, and <code>.npmignore</code> is missing, <code>.gitignore</code>&#8216;s contents will be used instead. </p>
<p>Files included with the &quot;package.json#files&quot; field <i>cannot</i> be excluded through <code>.npmignore</code> or <code>.gitignore</code>. </p>
<p>Certain files are always included, regardless of settings: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>package.json</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>README</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CHANGES</code> / <code>CHANGELOG</code> / <code>HISTORY</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>LICENSE</code> / <code>LICENCE</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>NOTICE</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The file in the &quot;main&quot; field </p>
 </dd></dl>
</dl>
<p> <code>README</code>, <code>CHANGES</code>, <code>LICENSE</code> &amp; <code>NOTICE</code> can have any case and extension. </p>
<p>Conversely, some files are always ignored: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>.git</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CVS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>.svn</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>.hg</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>.lock-wscript</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>.wafpickle-N</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>.*.swp</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>.DS_Store</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>._*</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>npm-debug.log</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>.npmrc</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>node_modules</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>config.gypi</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>*.orig</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>package-lock.json</code> (use shrinkwrap instead) </p>
 </dd></dl>
</dl>
<h3>main</h3>
<p>The main field is a module ID that is the primary entry point to your program. That is, if your package is named <code>foo</code>, and a user installs it, and then does <code>require(&quot;foo&quot;)</code>, then your main module&#8217;s exports object will be returned. </p>
<p>This should be a module ID relative to the root of your package folder. </p>
<p>For most modules, it makes the most sense to have a main script and often not much else.  </p>
<h3>browser</h3>
<p>If your module is meant to be used client-side the browser field should be used instead of the main field. This is helpful to hint users that it might rely on primitives that aren&#8217;t available in Node.js modules. (e.g. <code>window</code>)  </p>
<h3>bin</h3>
<p>A lot of packages have one or more executable files that they&#8217;d like to install into the PATH. npm makes this pretty easy (in fact, it uses this feature to install the &quot;npm&quot; executable.) </p>
<p>To use this, supply a <code>bin</code> field in your package.json which is a map of command name to local file name. On install, npm will symlink that file into <code>prefix/bin</code> for global installs, or <code>./node_modules/.bin/</code> for local installs. </p>
<p>For example, myapp could have this: </p>
<dl>
<dd> <pre><code>{ &quot;bin&quot; : { &quot;myapp&quot; : &quot;./cli.js&quot; } }
</code></pre>
 </dd></dl>
<p>So, when you install myapp, it&#8217;ll create a symlink from the <code>cli.js</code> script to <code>/usr/local/bin/myapp</code>. </p>
<p>If you have a single executable, and its name should be the name of the package, then you can just supply it as a string. For example: </p>
<dl>
<dd> <pre><code>{ &quot;name&quot;: &quot;my-program&quot;
, &quot;version&quot;: &quot;1.2.5&quot;
, &quot;bin&quot;: &quot;./path/to/program&quot; }
</code></pre>
 </dd></dl>
<p>would be the same as this: </p>
<dl>
<dd> <pre><code>{ &quot;name&quot;: &quot;my-program&quot;
, &quot;version&quot;: &quot;1.2.5&quot;
, &quot;bin&quot; : { &quot;my-program&quot; : &quot;./path/to/program&quot; } }
</code></pre>
 </dd></dl>
<p>Please make sure that your file(s) referenced in <code>bin</code> starts with <code>#!/usr/bin/env node</code>, otherwise the scripts are started without the node executable!  </p>
<h3>man</h3>
<p>Specify either a single file or an array of filenames to put in place for the <code>man</code> program to find. </p>
<p>If only a single file is provided, then it&#8217;s installed such that it is the result from <code>man &lt;pkgname&gt;</code>, regardless of its actual filename. For example: </p>
<dl>
<dd> <pre><code>{ &quot;name&quot; : &quot;foo&quot;
, &quot;version&quot; : &quot;1.2.3&quot;
, &quot;description&quot; : &quot;A packaged foo fooer for fooing foos&quot;
, &quot;main&quot; : &quot;foo.js&quot;
, &quot;man&quot; : &quot;./man/doc.1&quot;
}
</code></pre>
 </dd></dl>
<p>would link the <code>./man/doc.1</code> file in such that it is the target for <code>man foo</code> </p>
<p>If the filename doesn&#8217;t start with the package name, then it&#8217;s prefixed. So, this: </p>
<dl>
<dd> <pre><code>{ &quot;name&quot; : &quot;foo&quot;
, &quot;version&quot; : &quot;1.2.3&quot;
, &quot;description&quot; : &quot;A packaged foo fooer for fooing foos&quot;
, &quot;main&quot; : &quot;foo.js&quot;
, &quot;man&quot; : [ &quot;./man/foo.1&quot;, &quot;./man/bar.1&quot; ]
}
</code></pre>
 </dd></dl>
<p>will create files to do <code>man foo</code> and <code>man foo-bar</code>. </p>
<p>Man files must end with a number, and optionally a <code>.gz</code> suffix if they are compressed. The number dictates which man section the file is installed into. </p>
<dl>
<dd> <pre><code>{ &quot;name&quot; : &quot;foo&quot;
, &quot;version&quot; : &quot;1.2.3&quot;
, &quot;description&quot; : &quot;A packaged foo fooer for fooing foos&quot;
, &quot;main&quot; : &quot;foo.js&quot;
, &quot;man&quot; : [ &quot;./man/foo.1&quot;, &quot;./man/foo.2&quot; ]
}
</code></pre>
 </dd></dl>
<p>will create entries for <code>man foo</code> and <code>man 2 foo</code>  </p>
<h3>directories</h3>
<p>The CommonJS Packages <i><a rel="nofollow" href="http://wiki.commonjs.org/wiki/Packages/1.0">http://wiki.commonjs.org/wiki/Packages/1.0</a></i> spec details a few ways that you can indicate the structure of your package using a <code>directories</code> object. If you look at npm&#8217;s package.json <i><a rel="nofollow" href="https://registry.npmjs.org/npm/latest">https://registry.npmjs.org/npm/latest</a></i>, you&#8217;ll see that it has directories for doc, lib, and man. </p>
<p>In the future, this information may be used in other creative ways.  </p>
<h3>directories.lib</h3>
<p>Tell people where the bulk of your library is. Nothing special is done with the lib folder in any way, but it&#8217;s useful meta info.  </p>
<h3>directories.bin</h3>
<p>If you specify a <code>bin</code> directory in <code>directories.bin</code>, all the files in that folder will be added. </p>
<p>Because of the way the <code>bin</code> directive works, specifying both a <code>bin</code> path and setting <code>directories.bin</code> is an error. If you want to specify individual files, use <code>bin</code>, and for all the files in an existing <code>bin</code> directory, use <code>directories.bin</code>.  </p>
<h3>directories.man</h3>
<p>A folder that is full of man pages. Sugar to generate a &quot;man&quot; array by walking the folder.  </p>
<h3>directories.doc</h3>
<p>Put markdown files in here. Eventually, these will be displayed nicely, maybe, someday.  </p>
<h3>directories.example</h3>
<p>Put example scripts in here. Someday, it might be exposed in some clever way.  </p>
<h3>directories.test</h3>
<p>Put your tests in here. It is currently not exposed, but it might be in the future.  </p>
<h3>repository</h3>
<p>Specify the place where your code lives. This is helpful for people who want to contribute. If the git repo is on GitHub, then the <code>npm docs</code> command will be able to find you. </p>
<p>Do it like this: </p>
<dl>
<dd> <pre><code>&quot;repository&quot;: {
  &quot;type&quot; : &quot;git&quot;,
  &quot;url&quot; : &quot;https://github.com/npm/cli.git&quot;
}
&quot;repository&quot;: {
  &quot;type&quot; : &quot;svn&quot;,
  &quot;url&quot; : &quot;https://v8.googlecode.com/svn/trunk/&quot;
}
</code></pre>
 </dd></dl>
<p>The URL should be a publicly available (perhaps read-only) url that can be handed directly to a VCS program without any modification. It should not be a url to an html project page that you put in your browser. It&#8217;s for computers. </p>
<p>For GitHub, GitHub gist, Bitbucket, or GitLab repositories you can use the same shortcut syntax you use for <code>npm install</code>: </p>
<dl>
<dd> <pre><code>&quot;repository&quot;: &quot;npm/npm&quot;
&quot;repository&quot;: &quot;github:user/repo&quot;
&quot;repository&quot;: &quot;gist:11081aaa281&quot;
&quot;repository&quot;: &quot;bitbucket:user/repo&quot;
&quot;repository&quot;: &quot;gitlab:user/repo&quot;
</code></pre>
 </dd></dl>
<p>If the <code>package.json</code> for your package is not in the root directory (for example if it is part of a monorepo), you can specify the directory in which it lives: </p>
<dl>
<dd> <pre><code>&quot;repository&quot;: {
  &quot;type&quot; : &quot;git&quot;,
  &quot;url&quot; : &quot;https://github.com/facebook/react.git&quot;,
  &quot;directory&quot;: &quot;packages/react-dom&quot;
}
</code></pre>
 </dd></dl>
<h3>scripts</h3>
<p>The &quot;scripts&quot; property is a dictionary containing script commands that are run at various times in the lifecycle of your package. The key is the lifecycle event, and the value is the command to run at that point. </p>
<p>See npm help <code>scripts</code> to find out more about writing package scripts.  </p>
<h3>config</h3>
<p>A &quot;config&quot; object can be used to set configuration parameters used in package scripts that persist across upgrades. For instance, if a package had the following: </p>
<dl>
<dd> <pre><code>{ &quot;name&quot; : &quot;foo&quot;
, &quot;config&quot; : { &quot;port&quot; : &quot;8080&quot; } }
</code></pre>
 </dd></dl>
<p>and then had a &quot;start&quot; command that then referenced the <code>npm_package_config_port</code> environment variable, then the user could override that by doing <code>npm config set foo:port 8001</code>. </p>
<p>See npm help <code>config</code> and npm help <code>scripts</code> for more on package configs.  </p>
<h3>dependencies</h3>
<p>Dependencies are specified in a simple object that maps a package name to a version range. The version range is a string which has one or more space-separated descriptors. Dependencies can also be identified with a tarball or git URL. </p>
<p> <code>Please do not put test harnesses or transpilers in your dependencies</code> object. See <code>devDependencies</code>, below. </p>
<p>See npm help semver for more details about specifying version ranges. </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>version</code> Must match <code>version</code> exactly </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&gt;version</code> Must be greater than <code>version</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&gt;=version</code> etc </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;version</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;=version</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>~version</code> &quot;Approximately equivalent to version&quot; See npm help semver </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>^version</code> &quot;Compatible with version&quot; See npm help semver </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>1.2.x</code> 1.2.0, 1.2.1, etc., but not 1.3.0 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code><a rel="nofollow" href="http://...">http://...</a></code> See &#8216;URLs as Dependencies&#8217; below </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>*</code> Matches any version </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;&quot;</code> (just an empty string) Same as <code>*</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>version1 - version2</code> Same as <code>&gt;=version1 &lt;=version2</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>range1 || range2</code> Passes if either range1 or range2 are satisfied. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>git...</code> See &#8216;Git URLs as Dependencies&#8217; below </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>user/repo</code> See &#8216;GitHub URLs&#8217; below </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>tag</code> A specific version tagged and published as <code>tag</code> See npm help <code>dist-tag</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>path/path/path</code> See Local Paths <i>#local-paths</i> below </p>
 </dd></dl>
</dl>
<p>For example, these are all valid: </p>
<dl>
<dd> <pre><code>{ &quot;dependencies&quot; :
  { &quot;foo&quot; : &quot;1.0.0 - 2.9999.9999&quot;
  , &quot;bar&quot; : &quot;&gt;=1.0.2 &lt;2.1.2&quot;
  , &quot;baz&quot; : &quot;&gt;1.0.2 &lt;=2.3.4&quot;
  , &quot;boo&quot; : &quot;2.0.1&quot;
  , &quot;qux&quot; : &quot;&lt;1.0.0 || &gt;=2.3.1 &lt;2.4.5 || &gt;=2.5.2 &lt;3.0.0&quot;
  , &quot;asd&quot; : &quot;http://asdf.com/asdf.tar.gz&quot;
  , &quot;til&quot; : &quot;~1.2&quot;
  , &quot;elf&quot; : &quot;~1.2.3&quot;
  , &quot;two&quot; : &quot;2.x&quot;
  , &quot;thr&quot; : &quot;3.3.x&quot;
  , &quot;lat&quot; : &quot;latest&quot;
  , &quot;dyl&quot; : &quot;file:../dyl&quot;
  }
}
</code></pre>
 </dd></dl>
<h3>URLs as Dependencies</h3>
<p>You may specify a tarball URL in place of a version range. </p>
<p>This tarball will be downloaded and installed locally to your package at install time.  </p>
<h3>Git URLs as Dependencies</h3>
<p>Git urls are of the form: </p>
<dl>
<dd> <pre><code>&lt;protocol&gt;://[&lt;user&gt;[:&lt;password&gt;]@]&lt;hostname&gt;[:&lt;port&gt;][:][/]&lt;path&gt;[#&lt;commit-ish&gt; | #semver:&lt;semver&gt;]
</code></pre>
 </dd></dl>
<p> <code>&lt;protocol&gt;</code> is one of <code>git</code>, <code>git+ssh</code>, <code>git+http</code>, <code>git+https</code>, or <code>git+file</code>. </p>
<p>If <code>#&lt;commit-ish&gt;</code> is provided, it will be used to clone exactly that commit. If the commit-ish has the format <code>#semver:&lt;semver&gt;</code>, <code>&lt;semver&gt;</code> can be any valid semver range or exact version, and npm will look for any tags or refs matching that range in the remote repository, much as it would for a registry dependency. If neither <code>#&lt;commit-ish&gt;</code> or <code>#semver:&lt;semver&gt;</code> is specified, then <code>master</code> is used. </p>
<p>Examples: </p>
<dl>
<dd> <pre><code>git+ssh://git@github.com:npm/cli.git#v1.0.27git+ssh://git@github.com:npm/cli#semver:^5.0git+https://isaacs@github.com/npm/cli.git
git://github.com/npm/cli.git#v1.0.27
</code></pre>
 </dd></dl>
<h3>GitHub URLs</h3>
<p>As of version 1.1.65, you can refer to GitHub urls as just &quot;foo&quot;: &quot;user/foo-project&quot;. Just as with git URLs, a <code>commit-ish</code> suffix can be included. For example: </p>
<dl>
<dd> <pre><code>{
  &quot;name&quot;: &quot;foo&quot;,
  &quot;version&quot;: &quot;0.0.0&quot;,
  &quot;dependencies&quot;: {
    &quot;express&quot;: &quot;expressjs/express&quot;,
    &quot;mocha&quot;: &quot;mochajs/mocha#4727d357ea&quot;,
    &quot;module&quot;: &quot;user/repo#feature\/branch&quot;
  }
}
</code></pre>
 </dd></dl>
<h3>Local Paths</h3>
<p>As of version 2.0.0 you can provide a path to a local directory that contains a package. Local paths can be saved using <code>npm install -S</code> or <code>npm install --save</code>, using any of these forms: </p>
<dl>
<dd> <pre><code>../foo/bar
~/foo/bar
./foo/bar
/foo/bar
</code></pre>
 </dd></dl>
<p>in which case they will be normalized to a relative path and added to your <code>package.json</code>. For example: </p>
<dl>
<dd> <pre><code>{
  &quot;name&quot;: &quot;baz&quot;,
  &quot;dependencies&quot;: {
    &quot;bar&quot;: &quot;file:../foo/bar&quot;
  }
}
</code></pre>
 </dd></dl>
<p>This feature is helpful for local offline development and creating tests that require npm installing where you don&#8217;t want to hit an external server, but should not be used when publishing packages to the public registry.  </p>
<h3>devDependencies</h3>
<p>If someone is planning on downloading and using your module in their program, then they probably don&#8217;t want or need to download and build the external test or documentation framework that you use. </p>
<p>In this case, it&#8217;s best to map these additional items in a <code>devDependencies</code> object. </p>
<p>These things will be installed when doing <code>npm link</code> or <code>npm install</code> from the root of a package, and can be managed like any other npm configuration param. See npm help <code>config</code> for more on the topic. </p>
<p>For build steps that are not platform-specific, such as compiling CoffeeScript or other languages to JavaScript, use the <code>prepare</code> script to do this, and make the required package a devDependency. </p>
<p>For example: </p>
<dl>
<dd> <pre><code>{ &quot;name&quot;: &quot;ethopia-waza&quot;,
  &quot;description&quot;: &quot;a delightfully fruity coffee varietal&quot;,
  &quot;version&quot;: &quot;1.2.3&quot;,
  &quot;devDependencies&quot;: {
    &quot;coffee-script&quot;: &quot;~1.6.3&quot;
  },
  &quot;scripts&quot;: {
    &quot;prepare&quot;: &quot;coffee -o lib/ -c src/waza.coffee&quot;
  },
  &quot;main&quot;: &quot;lib/waza.js&quot;
}
</code></pre>
 </dd></dl>
<p>The <code>prepare</code> script will be run before publishing, so that users can consume the functionality without requiring them to compile it themselves. In dev mode (ie, locally running <code>npm install</code>), it&#8217;ll run this script as well, so that you can test it easily.  </p>
<h3>peerDependencies</h3>
<p>In some cases, you want to express the compatibility of your package with a host tool or library, while not necessarily doing a <code>require</code> of this host. This is usually referred to as a <i>plugin</i>. Notably, your module may be exposing a specific interface, expected and specified by the host documentation. </p>
<p>For example: </p>
<dl>
<dd> <pre><code>{
  &quot;name&quot;: &quot;tea-latte&quot;,
  &quot;version&quot;: &quot;1.3.5&quot;,
  &quot;peerDependencies&quot;: {
    &quot;tea&quot;: &quot;2.x&quot;
  }
}
</code></pre>
 </dd></dl>
<p>This ensures your package <code>tea-latte</code> can be installed <i>along</i> with the second major version of the host package <code>tea</code> only. <code>npm install tea-latte</code> could possibly yield the following dependency graph: </p>
<dl>
<dd> <pre><code>├── tea-latte [at] 1.3.5
└── tea [at] 2.2.0
</code></pre>
 </dd></dl>
<p> <code>NOTE: npm versions 1 and 2 will automatically install peerDependencies</code> if they are not explicitly depended upon higher in the dependency tree. In the next major version of npm (npm@3), this will no longer be the case. You will receive a warning that the peerDependency is not installed instead. The behavior in npms 1 &amp; 2 was frequently confusing and could easily put you into dependency hell, a situation that npm is designed to avoid as much as possible. </p>
<p>Trying to install another plugin with a conflicting requirement will cause an error. For this reason, make sure your plugin requirement is as broad as possible, and not to lock it down to specific patch versions. </p>
<p>Assuming the host complies with semver <i><a rel="nofollow" href="https://semver.org/">https://semver.org/</a></i>, only changes in the host package&#8217;s major version will break your plugin. Thus, if you&#8217;ve worked with every 1.x version of the host package, use <code>&quot;^1.0&quot;</code> or <code>&quot;1.x&quot;</code> to express this. If you depend on features introduced in 1.5.2, use <code>&quot;&gt;= 1.5.2 &lt; 2&quot;</code>.  </p>
<h3>bundledDependencies</h3>
<p>This defines an array of package names that will be bundled when publishing the package. </p>
<p>In cases where you need to preserve npm packages locally or have them available through a single file download, you can bundle the packages in a tarball file by specifying the package names in the <code>bundledDependencies</code> array and executing <code>npm pack</code>. </p>
<p>For example: </p>
<p>If we define a package.json like this: </p>
<dl>
<dd> <pre><code>{
  &quot;name&quot;: &quot;awesome-web-framework&quot;,
  &quot;version&quot;: &quot;1.0.0&quot;,
  &quot;bundledDependencies&quot;: [
    &quot;renderized&quot;, &quot;super-streams&quot;
  ]
}
</code></pre>
 </dd></dl>
<p>we can obtain <code>awesome-web-framework-1.0.0.tgz</code> file by running <code>npm pack</code>. This file contains the dependencies <code>renderized</code> and <code>super-streams</code> which can be installed in a new project by executing <code>npm install awesome-web-framework-1.0.0.tgz</code>. Note that the package names do not include any versions, as that information is specified in <code>dependencies</code>. </p>
<p>If this is spelled <code>&quot;bundleDependencies&quot;</code>, then that is also honored.  </p>
<h3>optionalDependencies</h3>
<p>If a dependency can be used, but you would like npm to proceed if it cannot be found or fails to install, then you may put it in the <code>optionalDependencies</code> object. This is a map of package name to version or url, just like the <code>dependencies</code> object. The difference is that build failures do not cause installation to fail. Running <code>npm install --no-optional</code> will prevent these dependencies from being installed. </p>
<p>It is still your program&#8217;s responsibility to handle the lack of the dependency. For example, something like this: </p>
<dl>
<dd> <pre><code>try {
  var foo = require('foo')
  var fooVersion = require('foo/package.json').version
} catch (er) {
  foo = null
}
if ( notGoodFooVersion(fooVersion) ) {
  foo = null
}
// .. then later in your program ..
if (foo) {
  foo.doFooThings()
}
</code></pre>
 </dd></dl>
<p>Entries in <code>optionalDependencies</code> will override entries of the same name in <code>dependencies</code>, so it&#8217;s usually best to only put in one place.  </p>
<h3>engines</h3>
<p>You can specify the version of node that your stuff works on: </p>
<dl>
<dd> <pre><code>{ &quot;engines&quot; : { &quot;node&quot; : &quot;&gt;=0.10.3 &lt;0.12&quot; } }
</code></pre>
 </dd></dl>
<p>And, like with dependencies, if you don&#8217;t specify the version (or if you specify &quot;*&quot; as the version), then any version of node will do. </p>
<p>If you specify an &quot;engines&quot; field, then npm will require that &quot;node&quot; be somewhere on that list. If &quot;engines&quot; is omitted, then npm will just assume that it works on node. </p>
<p>You can also use the &quot;engines&quot; field to specify which versions of npm are capable of properly installing your program. For example: </p>
<dl>
<dd> <pre><code>{ &quot;engines&quot; : { &quot;npm&quot; : &quot;~1.0.20&quot; } }
</code></pre>
 </dd></dl>
<p>Unless the user has set the <code>engine-strict</code> config flag, this field is advisory only and will only produce warnings when your package is installed as a dependency.  </p>
<h3>engineStrict</h3>
<p> <code>This feature was removed in npm 3.0.0</code> </p>
<p>Prior to npm 3.0.0, this feature was used to treat this package as if the user had set <code>engine-strict</code>. It is no longer used.  </p>
<h3>os</h3>
<p>You can specify which operating systems your module will run on: </p>
<dl>
<dd> <pre><code>&quot;os&quot; : [ &quot;darwin&quot;, &quot;linux&quot; ]
</code></pre>
 </dd></dl>
<p>You can also blacklist instead of whitelist operating systems, just prepend the blacklisted os with a &#8216;!&#8216;: </p>
<dl>
<dd> <pre><code>&quot;os&quot; : [ &quot;!win32&quot; ]
</code></pre>
 </dd></dl>
<p>The host operating system is determined by <code>process.platform</code> </p>
<p>It is allowed to both blacklist, and whitelist, although there isn&#8217;t any good reason to do this.  </p>
<h3>cpu</h3>
<p>If your code only runs on certain cpu architectures, you can specify which ones. </p>
<dl>
<dd> <pre><code>&quot;cpu&quot; : [ &quot;x64&quot;, &quot;ia32&quot; ]
</code></pre>
 </dd></dl>
<p>Like the <code>os</code> option, you can also blacklist architectures: </p>
<dl>
<dd> <pre><code>&quot;cpu&quot; : [ &quot;!arm&quot;, &quot;!mips&quot; ]
</code></pre>
 </dd></dl>
<p>The host architecture is determined by <code>process.arch</code>  </p>
<h3>preferGlobal</h3>
<p> <code>DEPRECATED</code> </p>
<p>This option used to trigger an npm warning, but it will no longer warn. It is purely there for informational purposes. It is now recommended that you install any binaries as local devDependencies wherever possible.  </p>
<h3>private</h3>
<p>If you set <code>&quot;private&quot;: true</code> in your package.json, then npm will refuse to publish it. </p>
<p>This is a way to prevent accidental publication of private repositories. If you would like to ensure that a given package is only ever published to a specific registry (for example, an internal registry), then use the <code>publishConfig</code> dictionary described below to override the <code>registry</code> config param at publish-time.  </p>
<h3>publishConfig</h3>
<p>This is a set of config values that will be used at publish-time. It&#8217;s especially handy if you want to set the tag, registry or access, so that you can ensure that a given package is not tagged with &quot;latest&quot;, published to the global public registry or that a scoped module is private by default. </p>
<p>Any config values can be overridden, but only &quot;tag&quot;, &quot;registry&quot; and &quot;access&quot; probably matter for the purposes of publishing. </p>
<p>See npm help <code>config</code> to see the list of config options that can be overridden.  </p>
<h3>DEFAULT VALUES</h3>
<p>npm will default some values based on package contents. </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;scripts&quot;: {&quot;start&quot;: &quot;node server.js&quot;}</code> If there is a <code>server.js</code> file in the root of your package, then npm will default the <code>start</code> command to <code>node server.js</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;scripts&quot;:{&quot;install&quot;: &quot;node-gyp rebuild&quot;}</code> If there is a <code>binding.gyp</code> file in the root of your package and you have not defined an <code>install</code> or <code>preinstall</code> script, npm will default the <code>install</code> command to compile using node-gyp. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;contributors&quot;: [...]</code> If there is an <code>AUTHORS</code> file in the root of your package, npm will treat each line as a <code>Name &lt;email&gt; (url)</code> format, where email and url are optional. Lines which start with a <code>#</code> or are blank, will be ignored. </p>
 </dd></dl>
</dl>
<h3>SEE ALSO</h3>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> npm help semver </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> npm help init </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> npm help version </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> npm help config </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> npm help help </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> npm help install </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> npm help publish </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> npm help uninstall </p>
 </dd></dl>
</dl>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAC">Description</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">name</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">version</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">description</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">keywords</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">homepage</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">bugs</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">license</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">people fields: author, contributors</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">funding</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">files</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">main</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">browser</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">bin</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">man</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">directories</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">directories.lib</a></dt>
<dd>  </dd>
<dt><a href="#lbAT">directories.bin</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">directories.man</a></dt>
<dd>  </dd>
<dt><a href="#lbAV">directories.doc</a></dt>
<dd>  </dd>
<dt><a href="#lbAW">directories.example</a></dt>
<dd>  </dd>
<dt><a href="#lbAX">directories.test</a></dt>
<dd>  </dd>
<dt><a href="#lbAY">repository</a></dt>
<dd>  </dd>
<dt><a href="#lbAZ">scripts</a></dt>
<dd>  </dd>
<dt><a href="#lbBA">config</a></dt>
<dd>  </dd>
<dt><a href="#lbBB">dependencies</a></dt>
<dd>  </dd>
<dt><a href="#lbBC">URLs as Dependencies</a></dt>
<dd>  </dd>
<dt><a href="#lbBD">Git URLs as Dependencies</a></dt>
<dd>  </dd>
<dt><a href="#lbBE">GitHub URLs</a></dt>
<dd>  </dd>
<dt><a href="#lbBF">Local Paths</a></dt>
<dd>  </dd>
<dt><a href="#lbBG">devDependencies</a></dt>
<dd>  </dd>
<dt><a href="#lbBH">peerDependencies</a></dt>
<dd>  </dd>
<dt><a href="#lbBI">bundledDependencies</a></dt>
<dd>  </dd>
<dt><a href="#lbBJ">optionalDependencies</a></dt>
<dd>  </dd>
<dt><a href="#lbBK">engines</a></dt>
<dd>  </dd>
<dt><a href="#lbBL">engineStrict</a></dt>
<dd>  </dd>
<dt><a href="#lbBM">os</a></dt>
<dd>  </dd>
<dt><a href="#lbBN">cpu</a></dt>
<dd>  </dd>
<dt><a href="#lbBO">preferGlobal</a></dt>
<dd>  </dd>
<dt><a href="#lbBP">private</a></dt>
<dd>  </dd>
<dt><a href="#lbBQ">publishConfig</a></dt>
<dd>  </dd>
<dt><a href="#lbBR">DEFAULT VALUES</a></dt>
<dd>  </dd>
<dt><a href="#lbBS">SEE ALSO</a></dt>
<dd>  </dd></dl>
</dl>
