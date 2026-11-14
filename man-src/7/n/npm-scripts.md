---
title: "npm-scripts(7)"
name: "npm-scripts"
section: "7"
letter: "n"
url: "/docs/linux/man/7-npm-scripts/"
description: "npm-scripts – How npm handles the \"scripts\" field"
---

<p><code>npm-scripts</code> &#8211; How npm handles the &quot;scripts&quot; field</p>
<h2>Description</h2>
<p>npm supports the &quot;scripts&quot; property of the package.json script, for the following scripts:</p>
<dl>
<dt>prepublish</p>
<dd>Run BEFORE the package is published. (Also run on local <code>npm install</code> without any arguments.)</p>
<dt>publish, postpublish</p>
<dd>Run AFTER the package is published.</p>
<dt>preinstall</p>
<dd>Run BEFORE the package is installed</p>
<dt>install, postinstall</p>
<dd>Run AFTER the package is installed.</p>
<dt>preuninstall, uninstall</p>
<dd>Run BEFORE the package is uninstalled.</p>
<dt>postuninstall</p>
<dd>Run AFTER the package is uninstalled.</p>
<dt>preversion, version</p>
<dd>Run BEFORE bump the package version.</p>
<dt>postversion</p>
<dd>Run AFTER bump the package version.</p>
<dt>pretest, test, posttest</p>
<dd>Run by the <code>npm test</code> command.</p>
<dt>prestop, stop, poststop</p>
<dd>Run by the <code>npm stop</code> command.</p>
<dt>prestart, start, poststart</p>
<dd>Run by the <code>npm start</code> command.</p>
<dt>prerestart, restart, postrestart</p>
<dd>Run by the <code>npm restart</code> command. Note: <code>npm restart</code> will run the stop and start scripts if no <code>restart</code> script is provided.</dl>
<p> Additionally, arbitrary scripts can be executed by running <code>npm run-script &lt;pkg&gt; &lt;stage&gt;</code>. <i>Pre</i> and <i>post</i> commands with matching names will be run for those as well (e.g. <code>premyscript</code>, <code>myscript</code>, <code>postmyscript</code>).</p>
<h2>Common Uses</h2>
<p>If you need to perform operations on your package before it is used, in a way that is not dependent on the operating system or architecture of the target system, use a <code>prepublish</code> script. This includes tasks such as:</p>
<dl>
<dt>&bull;</p>
<dd>Compiling CoffeeScript source code into JavaScript.</p>
<dt>&bull;</p>
<dd>Creating minified versions of JavaScript source code.</p>
<dt>&bull;</p>
<dd>Fetching remote resources that your package will use.</p>
<dd></dl>
<p> The advantage of doing these things at <code>prepublish</code> time is that they can be done once, in a single place, thus reducing complexity and variability. Additionally, this means that:</p>
<dl>
<dt>&bull;</p>
<dd>You can depend on <code>coffee-script</code> as a <code>devDependency</code>, and thus your users don&#8217;t need to have it installed.</p>
<dt>&bull;</p>
<dd>You don&#8217;t need to include minifiers in your package, reducing the size for your users.</p>
<dt>&bull;</p>
<dd>You don&#8217;t need to rely on your users having <code>curl</code> or <code>wget</code> or other system tools on the target machines.</p>
<dd></dl>
<h2>Default Values</h2>
<p>npm will default some script values based on package contents.</p>
<dl>
<dt><code>&quot;start&quot;: &quot;node server.js&quot;</code>:</p>
<dd>
<dd>If there is a <code>server.js</code> file in the root of your package, then npm will default the <code>start</code> command to <code>node server.js</code>.</p>
<dt><code>&quot;install&quot;: &quot;node-gyp rebuild&quot;</code>:</p>
<dd>
<dd>If there is a <code>binding.gyp</code> file in the root of your package, npm will default the <code>install</code> command to compile using node-gyp.</dl>
<h2>User</h2>
<p>If npm was invoked with root privileges, then it will change the uid to the user account or uid specified by the <code>user</code> config, which defaults to <code>nobody</code>. Set the <code>unsafe-perm</code> flag to run scripts with root privileges.</p>
<h2>Environment</h2>
<p>Package scripts run in an environment where many pieces of information are made available regarding the setup of npm and the current state of the process.</p>
<h3>path</h3>
<p>If you depend on modules that define executable scripts, like test suites, then those executables will be added to the <code>PATH</code> for executing the scripts. So, if your package.json has this:</p>
<dl>
<dd>
<pre>{ &quot;name&quot; : &quot;foo&quot;
, &quot;dependencies&quot; : { &quot;bar&quot; : &quot;0.1.x&quot; }
, &quot;scripts&quot;: { &quot;start&quot; : &quot;bar ./test&quot; } }</pre>
<dd></dl>
<p> then you could run <code>npm start</code> to execute the <code>bar</code> script, which is exported into the <code>node_modules/.bin</code> directory on <code>npm install</code>.</p>
<h3>package.json vars</h3>
<p>The package.json fields are tacked onto the <code>npm_package_</code> prefix. So, for instance, if you had <code>{&quot;name&quot;:&quot;foo&quot;, &quot;version&quot;:&quot;1.2.5&quot;}</code> in your package.json file, then your package scripts would have the <code>npm_package_name</code> environment variable set to &quot;foo&quot;, and the <code>npm_package_version</code> set to &quot;1.2.5&quot;</p>
<h3>configuration</h3>
<p>Configuration parameters are put in the environment with the <code>npm_config_</code> prefix. For instance, you can view the effective <code>root</code> config by checking the <code>npm_config_root</code> environment variable.</p>
<h3>Special: package.json The package.json &quot;config&quot; keys are overwritten in the environment if there is a config param of <code>&lt;name&gt;[@&lt;version&gt;]:&lt;key&gt;</code>. For example, if the package.json has this:</h3>
<dl>
<dd>
<pre>{ &quot;name&quot; : &quot;foo&quot;
, &quot;config&quot; : { &quot;port&quot; : &quot;8080&quot; }
, &quot;scripts&quot; : { &quot;start&quot; : &quot;node server.js&quot; } }</pre>
<dd></dl>
<p> and the server.js is this:</p>
<dl>
<dd>
<pre>http.createServer(...).listen(process.env.npm_package_config_port)</pre>
<dd></dl>
<p> then the user could change the behavior by doing:</p>
<dl>
<dd>
<pre>npm config set foo:port 80</pre>
<dd></dl>
<h3>current lifecycle event</h3>
<p>Lastly, the <code>npm_lifecycle_event</code> environment variable is set to whichever stage of the cycle is being executed. So, you could have a single script used for different parts of the process which switches based on what&#8217;s currently happening. </p>
<p> Objects are flattened following this format, so if you had <code>{&quot;scripts&quot;:{&quot;install&quot;:&quot;foo.js&quot;}}</code> in your package.json, then you&#8217;d see this in the script:</p>
<dl>
<dd>
<pre>process.env.npm_package_scripts_install === &quot;foo.js&quot;</pre>
<dd></dl>
<h2>Examples</h2>
<p>For example, if your package.json contains this:</p>
<dl>
<dd>
<pre>{ &quot;scripts&quot; :
 { &quot;install&quot; : &quot;scripts/install.js&quot;
 , &quot;postinstall&quot; : &quot;scripts/install.js&quot;
 , &quot;uninstall&quot; : &quot;scripts/uninstall.js&quot;
 }
}</pre>
<dd></dl>
<p> then the <code>scripts/install.js</code> will be called for the install, post-install, stages of the lifecycle, and the <code>scripts/uninstall.js</code> would be called when the package is uninstalled. Since <code>scripts/install.js</code> is running for three different phases, it would be wise in this case to look at the <code>npm_lifecycle_event</code> environment variable. </p>
<p> If you want to run a make command, you can do so. This works just fine:</p>
<dl>
<dd>
<pre>{ &quot;scripts&quot; :
 { &quot;preinstall&quot; : &quot;./configure&quot;
 , &quot;install&quot; : &quot;make &amp;&amp; make install&quot;
 , &quot;test&quot; : &quot;make test&quot;
 }
}</pre>
<dd></dl>
<h2>Exiting</h2>
<p>Scripts are run by passing the line as a script argument to <code>sh</code>. </p>
<p> If the script exits with a code other than 0, then this will abort the process. </p>
<p> Note that these script files don&#8217;t have to be nodejs or even javascript programs. They just have to be some kind of executable file.</p>
<h2>Hook Scripts</h2>
<p>If you want to run a specific script at a specific lifecycle event for ALL packages, then you can use a hook script. </p>
<p> Place an executable file at <code>node_modules/.hooks/{eventname}</code>, and it&#8217;ll get run for all packages when they are going through that point in the package lifecycle for any packages installed in that root. </p>
<p> Hook scripts are run exactly the same way as package.json scripts. That is, they are in a separate child process, with the env described above.</p>
<h2>Best Practices</h2>
<dl>
<dt>&bull;</p>
<dd>Don&#8217;t exit with a non-zero error code unless you <i>really</i> mean it. Except for uninstall scripts, this will cause the npm action to fail, and potentially be rolled back. If the failure is minor or only will prevent some optional features, then it&#8217;s better to just print a warning and exit successfully.</p>
<dt>&bull;</p>
<dd>Try not to use scripts to do what npm can do for you. Read through npm help 5 <code>package.json</code> to see all the things that you can specify and enable by simply describing your package appropriately. In general, this will lead to a more robust and consistent state.</p>
<dt>&bull;</p>
<dd>Inspect the env to determine where to put things. For instance, if the <code>npm_config_binroot</code> environment variable is set to <code>/home/user/bin</code>, then don&#8217;t try to install executables into <code>/usr/local/bin</code>. The user probably set it up that way for a reason.</p>
<dt>&bull;</p>
<dd>Don&#8217;t prefix your script commands with &quot;sudo&quot;. If root permissions are required for some reason, then it&#8217;ll fail with that error, and the user will sudo the npm command in question.</p>
<dt>&bull;</p>
<dd>Don&#8217;t use <code>install</code>. Use a <code>.gyp</code> file for compilation, and <code>prepublish</code> for anything else. You should almost never have to explicitly set a preinstall or install script. If you are doing this, please consider if there is another option. The only valid use of <code>install</code> or <code>preinstall</code> scripts is for compilation which must be done on the target architecture.</p>
<dd></dl>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help run-script</p>
<dt>&bull;</p>
<dd>npm help 5 package.json</p>
<dt>&bull;</p>
<dd>npm help 7 developers</p>
<dt>&bull;</p>
<dd>npm help install</p>
<dd>
