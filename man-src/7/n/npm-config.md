---
title: "npm-config(7)"
name: "npm-config"
section: "7"
letter: "n"
url: "/docs/linux/man/7-npm-config/"
description: "npm-config – More than you probably want to know about npm configuration"
---

<p><code>npm-config</code> &#8211; More than you probably want to know about npm configuration</p>
<h2>Description</h2>
<p>npm gets its configuration values from the following sources, sorted by priority:</p>
<h3>Command Line Flags</h3>
<p>Putting <code>&#8211;foo bar</code> on the command line sets the <code>foo</code> configuration parameter to <code>&quot;bar&quot;</code>. A <code>&#8212;</code> argument tells the cli parser to stop reading flags. A <code>&#8211;flag</code> parameter that is at the <i>end</i> of the command will be given the value of <code>true</code>.</p>
<h3>Environment Variables</h3>
<p>Any environment variables that start with <code>npm_config_</code> will be interpreted as a configuration parameter. For example, putting <code>npm_config_foo=bar</code> in your environment will set the <code>foo</code> configuration parameter to <code>bar</code>. Any environment configurations that are not given a value will be given the value of <code>true</code>. Config values are case-insensitive, so <code>NPM_CONFIG_FOO=bar</code> will work the same.</p>
<h3>npmrc Files</h3>
<p>The four relevant files are:</p>
<dl>
<dt>&bull;</p>
<dd>per-project config file (/path/to/my/project/.npmrc)</p>
<dt>&bull;</p>
<dd>per-user config file (~/.npmrc)</p>
<dt>&bull;</p>
<dd>global config file ($PREFIX/etc/npmrc)</p>
<dt>&bull;</p>
<dd>npm builtin config file (/path/to/npm/npmrc)</p>
<dd></dl>
<p> See npm help 5 npmrc for more details.</p>
<h3>Default Configs</h3>
<p>Run <code>npm config ls -l</code> to see a set of configuration parameters that are internal to npm, and are defaults if nothing else is specified.</p>
<h2>Shorthands and Other CLI Niceties</h2>
<p>The following shorthands are parsed on the command-line:</p>
<dl>
<dt>&bull;</p>
<dd><code>-v</code>: <code>&#8211;version</code></p>
<dt>&bull;</p>
<dd><code>-h</code>, <code>-?</code>, <code>&#8211;help</code>, <code>-H</code>: <code>&#8211;usage</code></p>
<dt>&bull;</p>
<dd><code>-s</code>, <code>&#8211;silent</code>: <code>&#8211;loglevel silent</code></p>
<dt>&bull;</p>
<dd><code>-q</code>, <code>&#8211;quiet</code>: <code>&#8211;loglevel warn</code></p>
<dt>&bull;</p>
<dd><code>-d</code>: <code>&#8211;loglevel info</code></p>
<dt>&bull;</p>
<dd><code>-dd</code>, <code>&#8211;verbose</code>: <code>&#8211;loglevel verbose</code></p>
<dt>&bull;</p>
<dd><code>-ddd</code>: <code>&#8211;loglevel silly</code></p>
<dt>&bull;</p>
<dd><code>-g</code>: <code>&#8211;global</code></p>
<dt>&bull;</p>
<dd><code>-C</code>: <code>&#8211;prefix</code></p>
<dt>&bull;</p>
<dd><code>-l</code>: <code>&#8211;long</code></p>
<dt>&bull;</p>
<dd><code>-m</code>: <code>&#8211;message</code></p>
<dt>&bull;</p>
<dd><code>-p</code>, <code>&#8211;porcelain</code>: <code>&#8211;parseable</code></p>
<dt>&bull;</p>
<dd><code>-reg</code>: <code>&#8211;registry</code></p>
<dt>&bull;</p>
<dd><code>-f</code>: <code>&#8211;force</code></p>
<dt>&bull;</p>
<dd><code>-desc</code>: <code>&#8211;description</code></p>
<dt>&bull;</p>
<dd><code>-S</code>: <code>&#8211;save</code></p>
<dt>&bull;</p>
<dd><code>-D</code>: <code>&#8211;save-dev</code></p>
<dt>&bull;</p>
<dd><code>-O</code>: <code>&#8211;save-optional</code></p>
<dt>&bull;</p>
<dd><code>-B</code>: <code>&#8211;save-bundle</code></p>
<dt>&bull;</p>
<dd><code>-E</code>: <code>&#8211;save-exact</code></p>
<dt>&bull;</p>
<dd><code>-y</code>: <code>&#8211;yes</code></p>
<dt>&bull;</p>
<dd><code>-n</code>: <code>&#8211;yes false</code></p>
<dt>&bull;</p>
<dd><code>ll</code> and <code>la</code> commands: <code>ls &#8211;long</code></p>
<dd></dl>
<p> If the specified configuration param resolves unambiguously to a known configuration parameter, then it is expanded to that configuration parameter. For example:</p>
<dl>
<dd>
<pre>npm ls --par
# same as:
npm ls --parseable</pre>
<dd></dl>
<p> If multiple single-character shorthands are strung together, and the resulting combination is unambiguously not some other configuration param, then it is expanded to its various component pieces. For example:</p>
<dl>
<dd>
<pre>npm ls -gpld
# same as:
npm ls --global --parseable --long --loglevel info</pre>
<dd></dl>
<h2>Per-Package Config Settings</h2>
<p>When running scripts (see npm help 7 <code>npm-scripts</code>) the package.json &quot;config&quot; keys are overwritten in the environment if there is a config param of <code>&lt;name&gt;[@&lt;version&gt;]:&lt;key&gt;</code>. For example, if the package.json has this:</p>
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
<p> See npm help 5 package.json for more information.</p>
<h2>Config Settings</h2>
<h3>access</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>restricted</code></p>
<dt>&bull;</p>
<dd>Type: Access</p>
<dd></dl>
<p> When publishing scoped packages, the access level defaults to <code>restricted</code>. If you want your scoped package to be publicly viewable (and installable) set <code>&#8211;access=public</code>. The only valid values for <code>access</code> are <code>public</code> and <code>restricted</code>. Unscoped packages <i>always</i> have an access level of <code>public</code>.</p>
<h3>always-auth</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Force npm to always require authentication when accessing the registry, even for <code>GET</code> requests.</p>
<h3>also</h3>
<dl>
<dt>&bull;</p>
<dd>Default: null</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> When &quot;dev&quot; or &quot;development&quot; and running local <code>npm shrinkwrap</code>, <code>npm outdated</code>, or <code>npm update</code>, is an alias for <code>&#8211;dev</code>.</p>
<h3>bin-links</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>true</code></p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Tells npm to create symlinks (or <code>.cmd</code> shims on Windows) for package executables. </p>
<p> Set to false to have it not do this. This can be used to work around the fact that some file systems don&#8217;t support symlinks, even on ostensibly Unix systems.</p>
<h3>browser</h3>
<dl>
<dt>&bull;</p>
<dd>Default: OS X: <code>&quot;open&quot;</code>, Windows: <code>&quot;start&quot;</code>, Others: <code>&quot;xdg-open&quot;</code></p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> The browser that is called by the <code>npm docs</code> command to open websites.</p>
<h3>ca</h3>
<dl>
<dt>&bull;</p>
<dd>Default: The npm CA certificate</p>
<dt>&bull;</p>
<dd>Type: String, Array or null</p>
<dd></dl>
<p> The Certificate Authority signing certificate that is trusted for SSL connections to the registry. Values should be in PEM format with newlines replaced by the string &quot;
&quot;. For example:</p>
<dl>
<dd>
<pre>ca=&quot;-----BEGIN CERTIFICATE-----
XXXX
XXXX
-----END CERTIFICATE-----&quot;</pre>
<dd></dl>
<p> Set to <code>null</code> to only allow &quot;known&quot; registrars, or to a specific CA cert to trust only that specific signing authority. </p>
<p> Multiple CAs can be trusted by specifying an array of certificates:</p>
<dl>
<dd>
<pre>ca[]=&quot;...&quot;
ca[]=&quot;...&quot;</pre>
<dd></dl>
<p> See also the <code>strict-ssl</code> config.</p>
<h3>cafile</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>null</code></p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> A path to a file containing one or multiple Certificate Authority signing certificates. Similar to the <code>ca</code> setting, but allows for multiple CA&#8217;s, as well as for the CA information to be stored in a file on disk.</p>
<h3>cache</h3>
<dl>
<dt>&bull;</p>
<dd>Default: Windows: <code>%AppData%
pm-cache</code>, Posix: <code>~/.npm</code></p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> The location of npm&#8217;s cache directory. See npm help <code>npm-cache</code></p>
<h3>cache-lock-stale</h3>
<dl>
<dt>&bull;</p>
<dd>Default: 60000 (1 minute)</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> The number of ms before cache folder lockfiles are considered stale.</p>
<h3>cache-lock-retries</h3>
<dl>
<dt>&bull;</p>
<dd>Default: 10</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> Number of times to retry to acquire a lock on cache folder lockfiles.</p>
<h3>cache-lock-wait</h3>
<dl>
<dt>&bull;</p>
<dd>Default: 10000 (10 seconds)</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> Number of ms to wait for cache lock files to expire.</p>
<h3>cache-max</h3>
<dl>
<dt>&bull;</p>
<dd>Default: Infinity</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> The maximum time (in seconds) to keep items in the registry cache before re-checking against the registry. </p>
<p> Note that no purging is done unless the <code>npm cache clean</code> command is explicitly used, and that only GET requests use the cache.</p>
<h3>cache-min</h3>
<dl>
<dt>&bull;</p>
<dd>Default: 10</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> The minimum time (in seconds) to keep items in the registry cache before re-checking against the registry. </p>
<p> Note that no purging is done unless the <code>npm cache clean</code> command is explicitly used, and that only GET requests use the cache.</p>
<h3>cert</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>null</code></p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> A client certificate to pass when accessing the registry.</p>
<h3>color</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true on Posix, false on Windows</p>
<dt>&bull;</p>
<dd>Type: Boolean or <code>&quot;always&quot;</code></p>
<dd></dl>
<p> If false, never shows colors. If <code>&quot;always&quot;</code> then always shows colors. If true, then only prints color codes for tty file descriptors.</p>
<h3>depth</h3>
<dl>
<dt>&bull;</p>
<dd>Default: Infinity</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> The depth to go when recursing directories for <code>npm ls</code>, <code>npm cache ls</code>, and <code>npm outdated</code>. </p>
<p> For <code>npm outdated</code>, a setting of <code>Infinity</code> will be treated as <code>0</code> since that gives more useful information. To show the outdated status of all packages and dependents, use a large integer value, e.g., <code>npm outdated &#8211;depth 9999</code></p>
<h3>description</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Show the description in <code>npm search</code></p>
<h3>dev</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Install <code>dev-dependencies</code> along with packages. </p>
<p> Note that <code>dev-dependencies</code> are also installed if the <code>npat</code> flag is set.</p>
<h3>dry-run</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Indicates that you don&#8217;t want npm to make any changes and that it should only report what it would have done. This can be passed into any of the commands that modify your local installation, eg, <code>install</code>, <code>update</code>, <code>dedupe</code>, <code>uninstall</code>. This is NOT currently honored by network related commands, eg <code>dist-tags</code>, <code>owner</code>, <code>publish</code>, etc.</p>
<h3>editor</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>EDITOR</code> environment variable if set, or <code>&quot;vi&quot;</code> on Posix, or <code>&quot;notepad&quot;</code> on Windows.</p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> The command to run for <code>npm edit</code> or <code>npm config edit</code>.</p>
<h3>engine-strict</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> If set to true, then npm will stubbornly refuse to install (or even consider installing) any package that claims to not be compatible with the current Node.js version.</p>
<h3>force</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Makes various commands more forceful.</p>
<dl>
<dt>&bull;</p>
<dd>lifecycle script failure does not block progress.</p>
<dt>&bull;</p>
<dd>publishing clobbers previously published versions.</p>
<dt>&bull;</p>
<dd>skips cache when requesting from the registry.</p>
<dt>&bull;</p>
<dd>prevents checks against clobbering non-npm files.</p>
<dd></dl>
<h3>fetch-retries</h3>
<dl>
<dt>&bull;</p>
<dd>Default: 2</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> The &quot;retries&quot; config for the <code>retry</code> module to use when fetching packages from the registry.</p>
<h3>fetch-retry-factor</h3>
<dl>
<dt>&bull;</p>
<dd>Default: 10</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> The &quot;factor&quot; config for the <code>retry</code> module to use when fetching packages.</p>
<h3>fetch-retry-mintimeout</h3>
<dl>
<dt>&bull;</p>
<dd>Default: 10000 (10 seconds)</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> The &quot;minTimeout&quot; config for the <code>retry</code> module to use when fetching packages.</p>
<h3>fetch-retry-maxtimeout</h3>
<dl>
<dt>&bull;</p>
<dd>Default: 60000 (1 minute)</p>
<dt>&bull;</p>
<dd>Type: Number</p>
<dd></dl>
<p> The &quot;maxTimeout&quot; config for the <code>retry</code> module to use when fetching packages.</p>
<h3>git</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>&quot;git&quot;</code></p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> The command to use for git commands. If git is installed on the computer, but is not in the <code>PATH</code>, then set this to the full path to the git binary.</p>
<h3>git-tag-version</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>true</code></p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Tag the commit when using the <code>npm version</code> command.</p>
<h3>global</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Operates in &quot;global&quot; mode, so that packages are installed into the <code>prefix</code> folder instead of the current working directory. See npm help 5 <code>npm-folders</code> for more on the differences in behavior.</p>
<dl>
<dt>&bull;</p>
<dd>packages are installed into the <code>{prefix}/lib/node_modules</code> folder, instead of the current working directory.</p>
<dt>&bull;</p>
<dd>bin files are linked to <code>{prefix}/bin</code></p>
<dt>&bull;</p>
<dd>man pages are linked to <code>{prefix}/share/man</code></p>
<dd></dl>
<h3>globalconfig</h3>
<dl>
<dt>&bull;</p>
<dd>Default: {prefix}/etc/npmrc</p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> The config file to read for global config options.</p>
<h3>global-style</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Causes npm to install the package into your local <code>node_modules</code> folder with the same layout it uses with the global <code>node_modules</code> folder. Only your direct dependencies will show in <code>node_modules</code> and everything they depend on will be flattened in their <code>node_modules</code> folders. This obviously will elminate some deduping. If used with <code>legacy-bundling</code>, <code>legacy-bundling</code> will be preferred.</p>
<h3>group</h3>
<dl>
<dt>&bull;</p>
<dd>Default: GID of the current process</p>
<dt>&bull;</p>
<dd>Type: String or Number</p>
<dd></dl>
<p> The group to use when running package scripts in global mode as the root user.</p>
<h3>heading</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>&quot;npm&quot;</code></p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> The string that starts all the debugging log output.</p>
<h3>https-proxy</h3>
<dl>
<dt>&bull;</p>
<dd>Default: null</p>
<dt>&bull;</p>
<dd>Type: url</p>
<dd></dl>
<p> A proxy to use for outgoing https requests. If the <code>HTTPS_PROXY</code> or <code>https_proxy</code> or <code>HTTP_PROXY</code> or <code>http_proxy</code> environment variables are set, proxy settings will be honored by the underlying <code>request</code> library.</p>
<h3>if-present</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> If true, npm will not exit with an error code when <code>run-script</code> is invoked for a script that isn&#8217;t defined in the <code>scripts</code> section of <code>package.json</code>. This option can be used when it&#8217;s desirable to optionally run a script when it&#8217;s present and fail if the script fails. This is useful, for example, when running scripts that may only apply for some builds in an otherwise generic CI setup.</p>
<h3>ignore-scripts</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> If true, npm does not run scripts specified in package.json files.</p>
<h3>init-module</h3>
<dl>
<dt>&bull;</p>
<dd>Default: ~/.npm-init.js</p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> A module that will be loaded by the <code>npm init</code> command. See the documentation for the init-package-json <i><a rel="nofollow" href="https://github.com/isaacs/init-package-json">https://github.com/isaacs/init-package-json</a></i> module for more information, or npm help init.</p>
<h3>init-author-name</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> The value <code>npm init</code> should use by default for the package author&#8217;s name.</p>
<h3>init-author-email</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> The value <code>npm init</code> should use by default for the package author&#8217;s email.</p>
<h3>init-author-url</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> The value <code>npm init</code> should use by default for the package author&#8217;s homepage.</p>
<h3>init-license</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;ISC&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> The value <code>npm init</code> should use by default for the package license.</p>
<h3>init-version</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;1.0.0&quot;</p>
<dt>&bull;</p>
<dd>Type: semver</p>
<dd></dl>
<p> The value that <code>npm init</code> should use by default for the package version number, if not already set in package.json.</p>
<h3>json</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Whether or not to output JSON data, rather than the normal output. </p>
<p> This feature is currently experimental, and the output data structures for many commands is either not implemented in JSON yet, or subject to change. Only the output from <code>npm ls &#8211;json</code> is currently valid.</p>
<h3>key</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>null</code></p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> A client key to pass when accessing the registry.</p>
<h3>legacy-bundling</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Causes npm to install the package such that versions of npm prior to 1.4, such as the one included with node 0.8, can install the package. This eliminates all automatic deduping. If used with <code>global-style</code> this option will be preferred.</p>
<h3>link</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> If true, then local installs will link if there is a suitable globally installed package. </p>
<p> Note that this means that local installs can cause things to be installed into the global space at the same time. The link is only done if one of the two conditions are met:</p>
<dl>
<dt>&bull;</p>
<dd>The package is not already installed globally, or</p>
<dt>&bull;</p>
<dd>the globally installed version is identical to the version that is being installed locally.</p>
<dd></dl>
<h3>local-address</h3>
<dl>
<dt>&bull;</p>
<dd>Default: undefined</p>
<dt>&bull;</p>
<dd>Type: IP Address</p>
<dd></dl>
<p> The IP address of the local interface to use when making connections to the npm registry. Must be IPv4 in versions of Node prior to 0.12.</p>
<h3>loglevel</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;warn&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dt>&bull;</p>
<dd>Values: &quot;silent&quot;, &quot;error&quot;, &quot;warn&quot;, &quot;http&quot;, &quot;info&quot;, &quot;verbose&quot;, &quot;silly&quot;</p>
<dd></dl>
<p> What level of logs to report. On failure, <i>all</i> logs are written to <code>npm-debug.log</code> in the current working directory. </p>
<p> Any logs of a higher level than the setting are shown. The default is &quot;warn&quot;, which shows warn and error output.</p>
<h3>logstream</h3>
<dl>
<dt>&bull;</p>
<dd>Default: process.stderr</p>
<dt>&bull;</p>
<dd>Type: Stream</p>
<dd></dl>
<p> This is the stream that is passed to the npmlog <i><a rel="nofollow" href="https://github.com/npm/npmlog">https://github.com/npm/npmlog</a></i> module at run time. </p>
<p> It cannot be set from the command line, but if you are using npm programmatically, you may wish to send logs to somewhere other than stderr. </p>
<p> If the <code>color</code> config is set to true, then this stream will receive colored output if it is a TTY.</p>
<h3>long</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Show extended information in <code>npm ls</code> and <code>npm search</code>.</p>
<h3>message</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;%s&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> Commit message which is used by <code>npm version</code> when creating version commit. </p>
<p> Any &quot;%s&quot; in the message will be replaced with the version number.</p>
<h3>node-version</h3>
<dl>
<dt>&bull;</p>
<dd>Default: process.version</p>
<dt>&bull;</p>
<dd>Type: semver or false</p>
<dd></dl>
<p> The node version to use when checking a package&#8217;s <code>engines</code> map.</p>
<h3>npat</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Run tests on installation.</p>
<h3>onload-script</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> A node module to <code>require()</code> when npm loads. Useful for programmatic usage.</p>
<h3>only</h3>
<dl>
<dt>&bull;</p>
<dd>Default: null</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> When &quot;dev&quot; or &quot;development&quot; and running local <code>npm install</code> without any arguments, only devDependencies (and their dependencies) are installed. </p>
<p> When &quot;dev&quot; or &quot;development&quot; and running local <code>npm ls</code>, <code>npm outdated</code>, or <code>npm update</code>, is an alias for <code>&#8211;dev</code>. </p>
<p> When &quot;prod&quot; or &quot;production&quot; and running local <code>npm install</code> without any arguments, only non-devDependencies (and their dependencies) are installed. </p>
<p> When &quot;prod&quot; or &quot;production&quot; and running local <code>npm ls</code>, <code>npm outdated</code>, or <code>npm update</code>, is an alias for <code>&#8211;production</code>.</p>
<h3>optional</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Attempt to install packages in the <code>optionalDependencies</code> object. Note that if these packages fail to install, the overall installation process is not aborted.</p>
<h3>parseable</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Output parseable results from commands that write to standard output.</p>
<h3>prefix</h3>
<dl>
<dt>&bull;</p>
<dd>Default: see npm help 5 folders</p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> The location to install global items. If set on the command line, then it forces non-global commands to run in the specified folder.</p>
<h3>production</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Set to true to run in &quot;production&quot; mode.</p>
<dl>
<dt>1.</p>
<dd>devDependencies are not installed at the topmost level when running local <code>npm install</code> without any arguments.</p>
<dt>2.</p>
<dd>Set the NODE_ENV=&quot;production&quot; for lifecycle scripts.</p>
<dd></dl>
<h3>progress</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> When set to <code>true</code>, npm will display a progress bar during time intensive operations, if <code>process.stderr</code> is a TTY. </p>
<p> Set to <code>false</code> to suppress the progress bar.</p>
<h3>proprietary-attribs</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Whether or not to include proprietary extended attributes in the tarballs created by npm. </p>
<p> Unless you are expecting to unpack package tarballs with something other than npm &#8212; particularly a very outdated tar implementation &#8212; leave this as true.</p>
<h3>proxy</h3>
<dl>
<dt>&bull;</p>
<dd>Default: null</p>
<dt>&bull;</p>
<dd>Type: url</p>
<dd></dl>
<p> A proxy to use for outgoing http requests. If the <code>HTTP_PROXY</code> or <code>http_proxy</code> environment variables are set, proxy settings will be honored by the underlying <code>request</code> library.</p>
<h3>rebuild-bundle</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Rebuild bundled dependencies after installation.</p>
<h3>registry</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <a rel="nofollow" href="https://registry.npmjs.org/">https://registry.npmjs.org/</a></p>
<dt>&bull;</p>
<dd>Type: url</p>
<dd></dl>
<p> The base URL of the npm package registry.</p>
<h3>rollback</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Remove failed installs.</p>
<h3>save</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Save installed packages to a package.json file as dependencies. </p>
<p> When used with the <code>npm rm</code> command, it removes it from the <code>dependencies</code> object. </p>
<p> Only works if there is already a package.json file present.</p>
<h3>save-bundle</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> If a package would be saved at install time by the use of <code>&#8211;save</code>, <code>&#8211;save-dev</code>, or <code>&#8211;save-optional</code>, then also put it in the <code>bundleDependencies</code> list. </p>
<p> When used with the <code>npm rm</code> command, it removes it from the bundledDependencies list.</p>
<h3>save-dev</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Save installed packages to a package.json file as <code>devDependencies</code>. </p>
<p> When used with the <code>npm rm</code> command, it removes it from the <code>devDependencies</code> object. </p>
<p> Only works if there is already a package.json file present.</p>
<h3>save-exact</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Dependencies saved to package.json using <code>&#8211;save</code>, <code>&#8211;save-dev</code> or <code>&#8211;save-optional</code> will be configured with an exact version rather than using npm&#8217;s default semver range operator.</p>
<h3>save-optional</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Save installed packages to a package.json file as optionalDependencies. </p>
<p> When used with the <code>npm rm</code> command, it removes it from the <code>devDependencies</code> object. </p>
<p> Only works if there is already a package.json file present.</p>
<h3>save-prefix</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &#8216;^&#8217;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> Configure how versions of packages installed to a package.json file via <code>&#8211;save</code> or <code>&#8211;save-dev</code> get prefixed. </p>
<p> For example if a package has version <code>1.2.3</code>, by default its version is set to <code>^1.2.3</code> which allows minor upgrades for that package, but after <code>npm config set save-prefix=&#8217;~&#8217;</code> it would be set to <code>~1.2.3</code> which only allows patch upgrades.</p>
<h3>scope</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> Associate an operation with a scope for a scoped registry. Useful when logging in to a private registry for the first time: <code>npm login &#8211;scope=@organization &#8211;registry=registry.organization.com</code>, which will cause <code>@organization</code> to be mapped to the registry for future installation of packages specified according to the pattern <code>@organization/package</code>.</p>
<h3>searchopts</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> Space-separated options that are always passed to search.</p>
<h3>searchexclude</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> Space-separated options that limit the results from search.</p>
<h3>searchsort</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;name&quot;</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dt>&bull;</p>
<dd>Values: &quot;name&quot;, &quot;-name&quot;, &quot;date&quot;, &quot;-date&quot;, &quot;description&quot;, &quot;-description&quot;, &quot;keywords&quot;, &quot;-keywords&quot;</p>
<dd></dl>
<p> Indication of which field to sort search results by. Prefix with a <code>&#8211;</code> character to indicate reverse sort.</p>
<h3>shell</h3>
<dl>
<dt>&bull;</p>
<dd>Default: SHELL environment variable, or &quot;bash&quot; on Posix, or &quot;cmd&quot; on Windows</p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> The shell to run for the <code>npm explore</code> command.</p>
<h3>shrinkwrap</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> If set to false, then ignore <code>npm-shrinkwrap.json</code> files when installing.</p>
<h3>sign-git-tag</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> If set to true, then the <code>npm version</code> command will tag the version using <code>-s</code> to add a signature. </p>
<p> Note that git requires you to have set up GPG keys in your git configs for this to work properly.</p>
<h3>strict-ssl</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Whether or not to do SSL key validation when making requests to the registry via https. </p>
<p> See also the <code>ca</code> config.</p>
<h3>tag</h3>
<dl>
<dt>&bull;</p>
<dd>Default: latest</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> If you ask npm to install a package and don&#8217;t tell it a specific version, then it will install the specified tag. </p>
<p> Also the tag that is added to the package [at] version specified by the <code>npm tag</code> command, if no explicit tag is given.</p>
<h3>tag-version-prefix</h3>
<dl>
<dt>&bull;</p>
<dd>Default: <code>&quot;v&quot;</code></p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> If set, alters the prefix used when tagging a new version when performing a version increment using <code>npm-version</code>. To remove the prefix altogether, set it to the empty string: <code>&quot;&quot;</code>. </p>
<p> Because other tools may rely on the convention that npm version tags look like <code>v1.0.0</code>, <i>only use this property if it is absolutely necessary</i>. In particular, use care when overriding this setting for public packages.</p>
<h3>tmp</h3>
<dl>
<dt>&bull;</p>
<dd>Default: TMPDIR environment variable, or &quot;/tmp&quot;</p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> Where to store temporary files and folders. All temp files are deleted on success, but left behind on failure for forensic purposes.</p>
<h3>unicode</h3>
<dl>
<dt>&bull;</p>
<dd>Default: true on windows and mac/unix systems with a unicode locale</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> When set to true, npm uses unicode characters in the tree output. When false, it uses ascii characters to draw trees.</p>
<h3>unsafe-perm</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false if running as root, true otherwise</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Set to true to suppress the UID/GID switching when running package scripts. If set explicitly to false, then installing as a non-root user will fail.</p>
<h3>usage</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: Boolean</p>
<dd></dl>
<p> Set to show short usage output (like the -H output) instead of complete help when doing npm help <code>npm-help</code>.</p>
<h3>user</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;nobody&quot;</p>
<dt>&bull;</p>
<dd>Type: String or Number</p>
<dd></dl>
<p> The UID to set to when running package scripts as root.</p>
<h3>userconfig</h3>
<dl>
<dt>&bull;</p>
<dd>Default: ~/.npmrc</p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> The location of user-level configuration settings.</p>
<h3>umask</h3>
<dl>
<dt>&bull;</p>
<dd>Default: 022</p>
<dt>&bull;</p>
<dd>Type: Octal numeric string in range 0000..0777 (0..511)</p>
<dd></dl>
<p> The &quot;umask&quot; value to use when setting the file creation mode on files and folders. </p>
<p> Folders and executables are given a mode which is <code>0777</code> masked against this value. Other files are given a mode which is <code>0666</code> masked against this value. Thus, the defaults are <code>0755</code> and <code>0644</code> respectively.</p>
<h3>user-agent</h3>
<dl>
<dt>&bull;</p>
<dd>Default: node/{process.version} {process.platform} {process.arch}</p>
<dt>&bull;</p>
<dd>Type: String</p>
<dd></dl>
<p> Sets a User-Agent to the request header</p>
<h3>version</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: boolean</p>
<dd></dl>
<p> If true, output the npm version and exit successfully. </p>
<p> Only relevant when specified explicitly on the command line.</p>
<h3>versions</h3>
<dl>
<dt>&bull;</p>
<dd>Default: false</p>
<dt>&bull;</p>
<dd>Type: boolean</p>
<dd></dl>
<p> If true, output the npm version as well as node&#8217;s <code>process.versions</code> map, and exit successfully. </p>
<p> Only relevant when specified explicitly on the command line.</p>
<h3>viewer</h3>
<dl>
<dt>&bull;</p>
<dd>Default: &quot;man&quot; on Posix, &quot;browser&quot; on Windows</p>
<dt>&bull;</p>
<dd>Type: path</p>
<dd></dl>
<p> The program to use to view help content. </p>
<p> Set to <code>&quot;browser&quot;</code> to view html help content in the default web browser.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help config</p>
<dt>&bull;</p>
<dd>npm help 5 npmrc</p>
<dt>&bull;</p>
<dd>npm help 7 scripts</p>
<dt>&bull;</p>
<dd>npm help 5 folders</p>
<dt>&bull;</p>
<dd>npm help npm</p>
<dd>
