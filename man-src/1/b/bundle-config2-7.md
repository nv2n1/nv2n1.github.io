---
title: "bundle-config2-7(1)"
name: "bundle-config2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-config2-7/"
description: "bundle-config – Set bundler configuration options"
---

<p><code>bundle-config</code> &#8211; Set bundler configuration options </p>
<h2>Synopsis</h2>
<p><code>bundle config</code> [list|get|set|unset] [<i>name</i> [<i>value</i>]]</p>
<h2>Description</h2>
<p>This command allows you to interact with Bundler&#8217;s configuration system. </p>
<p> Bundler loads configuration settings in this order:</p>
<dl>
<dt>1.</p>
<dd>Local config (<code>app/.bundle/config</code>)</p>
<dt>2.</p>
<dd>Environmental variables (<code>ENV</code>)</p>
<dt>3.</p>
<dd>Global config (<code>~/.bundle/config</code>)</p>
<dt>4.</p>
<dd>Bundler default config</p>
<dd></dl>
<p> Executing <code>bundle config list</code> with will print a list of all bundler configuration for the current bundle, and where that configuration was set. </p>
<p> Executing <code>bundle config get &lt;name&gt;</code> will print the value of that configuration setting, and where it was set. </p>
<p> Executing <code>bundle config set &lt;name&gt; &lt;value&gt;</code> will set that configuration to the value specified for all bundles executed as the current user. The configuration will be stored in <code>~/.bundle/config</code>. If <i>name</i> already is set, <i>name</i> will be overridden and user will be warned. </p>
<p> Executing <code>bundle config set &#8211;global &lt;name&gt; &lt;value&gt;</code> works the same as above. </p>
<p> Executing <code>bundle config set &#8211;local &lt;name&gt; &lt;value&gt;</code> will set that configuration to the local application. The configuration will be stored in <code>app/.bundle/config</code>. </p>
<p> Executing <code>bundle config unset &lt;name&gt;</code> will delete the configuration in both local and global sources. </p>
<p> Executing <code>bundle config unset &#8211;global &lt;name&gt;</code> will delete the configuration only from the user configuration. </p>
<p> Executing <code>bundle config unset &#8211;local &lt;name&gt; &lt;value&gt;</code> will delete the configuration only from the local application. </p>
<p> Executing bundle with the <code>BUNDLE_IGNORE_CONFIG</code> environment variable set will cause it to ignore all configuration. </p>
<p> Executing <code>bundle config set disable_multisource true</code> upgrades the warning about the Gemfile containing multiple primary sources to an error. Executing <code>bundle config unset disable_multisource</code> downgrades this error to a warning.</p>
<h2>Remembering Options</h2>
<p>Flags passed to <code>bundle install</code> or the Bundler runtime, such as <code>&#8211;path foo</code> or <code>&#8211;without production</code>, are remembered between commands and saved to your local application&#8217;s configuration (normally, <code>./.bundle/config</code>). </p>
<p> However, this will be changed in bundler 3, so it&#8217;s better not to rely on this behavior. If these options must be remembered, it&#8217;s better to set them using <code>bundle config</code> (e.g., <code>bundle config set path foo</code>). </p>
<p> The options that can be configured are:</p>
<dl>
<dt><code>bin</code></p>
<dd>Creates a directory (defaults to <code>~/bin</code>) and place any executables from the gem there. These executables run in Bundler&#8217;s context. If used, you might add this directory to your environment&#8217;s <code>PATH</code> variable. For instance, if the <code>rails</code> gem comes with a <code>rails</code> executable, this flag will create a <code>bin/rails</code> executable that ensures that all referred dependencies will be resolved using the bundled gems.</p>
<dt><code>deployment</code></p>
<dd>In deployment mode, Bundler will &#8216;roll-out&#8217; the bundle for <code>production</code> use. Please check carefully if you want to have this option enabled in <code>development</code> or <code>test</code> environments.</p>
<dt><code>path</code></p>
<dd>The location to install the specified gems to. This defaults to Rubygems&#8217; setting. Bundler shares this location with Rubygems, <code>gem install &#8230;</code> will have gem installed there, too. Therefore, gems installed without a <code>&#8211;path &#8230;</code> setting will show up by calling <code>gem list</code>. Accordingly, gems installed to other locations will not get listed.</p>
<dt><code>without</code></p>
<dd>A space-separated list of groups referencing gems to skip during installation.</p>
<dt><code>with</code></p>
<dd>A space-separated list of groups referencing gems to include during installation.</dl>
<h2>Build Options</h2>
<p>You can use <code>bundle config</code> to give Bundler the flags to pass to the gem installer every time bundler tries to install a particular gem. </p>
<p> A very common example, the <code>mysql</code> gem, requires Snow Leopard users to pass configuration flags to <code>gem install</code> to specify where to find the <code>mysql_config</code> executable.</p>
<dl>
<dd>
<pre>gem install mysql -- --with-mysql-config=/usr/local/mysql/bin/mysql_config</pre>
<dd></dl>
<p> Since the specific location of that executable can change from machine to machine, you can specify these flags on a per-machine basis.</p>
<dl>
<dd>
<pre>bundle config set build.mysql --with-mysql-config=/usr/local/mysql/bin/mysql_config</pre>
<dd></dl>
<p> After running this command, every time bundler needs to install the <code>mysql</code> gem, it will pass along the flags you specified.</p>
<h2>Configuration Keys</h2>
<p>Configuration keys in bundler have two forms: the canonical form and the environment variable form. </p>
<p> For instance, passing the <code>&#8211;without</code> flag to bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i> prevents Bundler from installing certain groups specified in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5). Bundler persists this value in <code>app/.bundle/config</code> so that calls to <code>Bundler.setup</code> do not try to find gems from the <code>Gemfile</code> that you didn&#8217;t install. Additionally, subsequent calls to bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i> remember this setting and skip those groups. </p>
<p> The canonical form of this configuration is <code>&quot;without&quot;</code>. To convert the canonical form to the environment variable form, capitalize it, and prepend <code>BUNDLE_</code>. The environment variable form of <code>&quot;without&quot;</code> is <code>BUNDLE_WITHOUT</code>. </p>
<p> Any periods in the configuration keys must be replaced with two underscores when setting it via environment variables. The configuration key <code>local.rack</code> becomes the environment variable <code>BUNDLE_LOCAL__RACK</code>.</p>
<h2>List Of Available Keys</h2>
<p>The following is a list of all configuration keys and their purpose. You can learn more about their operation in bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i>.</p>
<dl>
<dt>&bull;</p>
<dd><code>allow_bundler_dependency_conflicts</code> (<code>BUNDLE_ALLOW_BUNDLER_DEPENDENCY_CONFLICTS</code>): Allow resolving to specifications that have dependencies on <code>bundler</code> that are incompatible with the running Bundler version.</p>
<dt>&bull;</p>
<dd><code>allow_deployment_source_credential_changes</code> (<code>BUNDLE_ALLOW_DEPLOYMENT_SOURCE_CREDENTIAL_CHANGES</code>): When in deployment mode, allow changing the credentials to a gem&#8217;s source. Ex: <code><a rel="nofollow" href="https://some.host.com/gems/path/">https://some.host.com/gems/path/</a></code> -&gt; <code><a rel="nofollow" href="https://user_name:password@some.host.com/gems/path">https://user_name:password@some.host.com/gems/path</a></code></p>
<dt>&bull;</p>
<dd><code>allow_offline_install</code> (<code>BUNDLE_ALLOW_OFFLINE_INSTALL</code>): Allow Bundler to use cached data when installing without network access.</p>
<dt>&bull;</p>
<dd><code>auto_clean_without_path</code> (<code>BUNDLE_AUTO_CLEAN_WITHOUT_PATH</code>): Automatically run <code>bundle clean</code> after installing when an explicit <code>path</code> has not been set and Bundler is not installing into the system gems.</p>
<dt>&bull;</p>
<dd><code>auto_install</code> (<code>BUNDLE_AUTO_INSTALL</code>): Automatically run <code>bundle install</code> when gems are missing.</p>
<dt>&bull;</p>
<dd><code>bin</code> (<code>BUNDLE_BIN</code>): Install executables from gems in the bundle to the specified directory. Defaults to <code>false</code>.</p>
<dt>&bull;</p>
<dd><code>cache_all</code> (<code>BUNDLE_CACHE_ALL</code>): Cache all gems, including path and git gems.</p>
<dt>&bull;</p>
<dd><code>cache_all_platforms</code> (<code>BUNDLE_CACHE_ALL_PLATFORMS</code>): Cache gems for all platforms.</p>
<dt>&bull;</p>
<dd><code>cache_path</code> (<code>BUNDLE_CACHE_PATH</code>): The directory that bundler will place cached gems in when running <code>bundle package</code>, and that bundler will look in when installing gems. Defaults to <code>vendor/cache</code>.</p>
<dt>&bull;</p>
<dd><code>clean</code> (<code>BUNDLE_CLEAN</code>): Whether Bundler should run <code>bundle clean</code> automatically after <code>bundle install</code>.</p>
<dt>&bull;</p>
<dd><code>console</code> (<code>BUNDLE_CONSOLE</code>): The console that <code>bundle console</code> starts. Defaults to <code>irb</code>.</p>
<dt>&bull;</p>
<dd><code>default_install_uses_path</code> (<code>BUNDLE_DEFAULT_INSTALL_USES_PATH</code>): Whether a <code>bundle install</code> without an explicit <code>&#8211;path</code> argument defaults to installing gems in <code>.bundle</code>.</p>
<dt>&bull;</p>
<dd><code>deployment</code> (<code>BUNDLE_DEPLOYMENT</code>): Disallow changes to the <code>Gemfile</code>. When the <code>Gemfile</code> is changed and the lockfile has not been updated, running Bundler commands will be blocked.</p>
<dt>&bull;</p>
<dd><code>disable_checksum_validation</code> (<code>BUNDLE_DISABLE_CHECKSUM_VALIDATION</code>): Allow installing gems even if they do not match the checksum provided by RubyGems.</p>
<dt>&bull;</p>
<dd><code>disable_exec_load</code> (<code>BUNDLE_DISABLE_EXEC_LOAD</code>): Stop Bundler from using <code>load</code> to launch an executable in-process in <code>bundle exec</code>.</p>
<dt>&bull;</p>
<dd><code>disable_local_branch_check</code> (<code>BUNDLE_DISABLE_LOCAL_BRANCH_CHECK</code>): Allow Bundler to use a local git override without a branch specified in the Gemfile.</p>
<dt>&bull;</p>
<dd><code>disable_multisource</code> (<code>BUNDLE_DISABLE_MULTISOURCE</code>): When set, Gemfiles containing multiple sources will produce errors instead of warnings. Use <code>bundle config unset disable_multisource</code> to unset.</p>
<dt>&bull;</p>
<dd><code>disable_platform_warnings</code> (<code>BUNDLE_DISABLE_PLATFORM_WARNINGS</code>): Disable warnings during bundle install when a dependency is unused on the current platform.</p>
<dt>&bull;</p>
<dd><code>disable_shared_gems</code> (<code>BUNDLE_DISABLE_SHARED_GEMS</code>): Stop Bundler from accessing gems installed to RubyGems&#8217; normal location.</p>
<dt>&bull;</p>
<dd><code>disable_version_check</code> (<code>BUNDLE_DISABLE_VERSION_CHECK</code>): Stop Bundler from checking if a newer Bundler version is available on rubygems.org.</p>
<dt>&bull;</p>
<dd><code>force_ruby_platform</code> (<code>BUNDLE_FORCE_RUBY_PLATFORM</code>): Ignore the current machine&#8217;s platform and install only <code>ruby</code> platform gems. As a result, gems with native extensions will be compiled from source.</p>
<dt>&bull;</p>
<dd><code>frozen</code> (<code>BUNDLE_FROZEN</code>): Disallow changes to the <code>Gemfile</code>. When the <code>Gemfile</code> is changed and the lockfile has not been updated, running Bundler commands will be blocked. Defaults to <code>true</code> when <code>&#8211;deployment</code> is used.</p>
<dt>&bull;</p>
<dd><code>gem.push_key</code> (<code>BUNDLE_GEM__PUSH_KEY</code>): Sets the <code>&#8211;key</code> parameter for <code>gem push</code> when using the <code>rake release</code> command with a private gemstash server.</p>
<dt>&bull;</p>
<dd><code>gemfile</code> (<code>BUNDLE_GEMFILE</code>): The name of the file that bundler should use as the <code>Gemfile</code>. This location of this file also sets the root of the project, which is used to resolve relative paths in the <code>Gemfile</code>, among other things. By default, bundler will search up from the current working directory until it finds a <code>Gemfile</code>.</p>
<dt>&bull;</p>
<dd><code>global_gem_cache</code> (<code>BUNDLE_GLOBAL_GEM_CACHE</code>): Whether Bundler should cache all gems globally, rather than locally to the installing Ruby installation.</p>
<dt>&bull;</p>
<dd><code>ignore_messages</code> (<code>BUNDLE_IGNORE_MESSAGES</code>): When set, no post install messages will be printed. To silence a single gem, use dot notation like <code>ignore_messages.httparty true</code>.</p>
<dt>&bull;</p>
<dd><code>init_gems_rb</code> (<code>BUNDLE_INIT_GEMS_RB</code>) Generate a <code>gems.rb</code> instead of a <code>Gemfile</code> when running <code>bundle init</code>.</p>
<dt>&bull;</p>
<dd><code>jobs</code> (<code>BUNDLE_JOBS</code>): The number of gems Bundler can install in parallel. Defaults to 1.</p>
<dt>&bull;</p>
<dd><code>no_install</code> (<code>BUNDLE_NO_INSTALL</code>): Whether <code>bundle package</code> should skip installing gems.</p>
<dt>&bull;</p>
<dd><code>no_prune</code> (<code>BUNDLE_NO_PRUNE</code>): Whether Bundler should leave outdated gems unpruned when caching.</p>
<dt>&bull;</p>
<dd><code>only_update_to_newer_versions</code> (<code>BUNDLE_ONLY_UPDATE_TO_NEWER_VERSIONS</code>): During <code>bundle update</code>, only resolve to newer versions of the gems in the lockfile.</p>
<dt>&bull;</p>
<dd><code>path</code> (<code>BUNDLE_PATH</code>): The location on disk where all gems in your bundle will be located regardless of <code>$GEM_HOME</code> or <code>$GEM_PATH</code> values. Bundle gems not found in this location will be installed by <code>bundle install</code>. Defaults to <code>Gem.dir</code>. When &#8211;deployment is used, defaults to vendor/bundle.</p>
<dt>&bull;</p>
<dd><code>path.system</code> (<code>BUNDLE_PATH__SYSTEM</code>): Whether Bundler will install gems into the default system path (<code>Gem.dir</code>).</p>
<dt>&bull;</p>
<dd><code>path_relative_to_cwd</code> (<code>BUNDLE_PATH_RELATIVE_TO_CWD</code>) Makes <code>&#8211;path</code> relative to the CWD instead of the <code>Gemfile</code>.</p>
<dt>&bull;</p>
<dd><code>plugins</code> (<code>BUNDLE_PLUGINS</code>): Enable Bundler&#8217;s experimental plugin system.</p>
<dt>&bull;</p>
<dd><code>prefer_patch</code> (BUNDLE_PREFER_PATCH): Prefer updating only to next patch version during updates. Makes <code>bundle update</code> calls equivalent to <code>bundler update &#8211;patch</code>.</p>
<dt>&bull;</p>
<dd><code>print_only_version_number</code> (<code>BUNDLE_PRINT_ONLY_VERSION_NUMBER</code>) Print only version number from <code>bundler &#8211;version</code>.</p>
<dt>&bull;</p>
<dd><code>redirect</code> (<code>BUNDLE_REDIRECT</code>): The number of redirects allowed for network requests. Defaults to <code>5</code>.</p>
<dt>&bull;</p>
<dd><code>retry</code> (<code>BUNDLE_RETRY</code>): The number of times to retry failed network requests. Defaults to <code>3</code>.</p>
<dt>&bull;</p>
<dd><code>setup_makes_kernel_gem_public</code> (<code>BUNDLE_SETUP_MAKES_KERNEL_GEM_PUBLIC</code>): Have <code>Bundler.setup</code> make the <code>Kernel#gem</code> method public, even though RubyGems declares it as private.</p>
<dt>&bull;</p>
<dd><code>shebang</code> (<code>BUNDLE_SHEBANG</code>): The program name that should be invoked for generated binstubs. Defaults to the ruby install name used to generate the binstub.</p>
<dt>&bull;</p>
<dd><code>silence_deprecations</code> (<code>BUNDLE_SILENCE_DEPRECATIONS</code>): Whether Bundler should silence deprecation warnings for behavior that will be changed in the next major version.</p>
<dt>&bull;</p>
<dd><code>silence_root_warning</code> (<code>BUNDLE_SILENCE_ROOT_WARNING</code>): Silence the warning Bundler prints when installing gems as root.</p>
<dt>&bull;</p>
<dd><code>skip_default_git_sources</code> (<code>BUNDLE_SKIP_DEFAULT_GIT_SOURCES</code>): Whether Bundler should skip adding default git source shortcuts to the Gemfile DSL.</p>
<dt>&bull;</p>
<dd><code>specific_platform</code> (<code>BUNDLE_SPECIFIC_PLATFORM</code>): Allow bundler to resolve for the specific running platform and store it in the lockfile, instead of only using a generic platform. A specific platform is the exact platform triple reported by <code>Gem::Platform.local</code>, such as <code>x86_64-darwin-16</code> or <code>universal-java-1.8</code>. On the other hand, generic platforms are those such as <code>ruby</code>, <code>mswin</code>, or <code>java</code>. In this example, <code>x86_64-darwin-16</code> would map to <code>ruby</code> and <code>universal-java-1.8</code> to <code>java</code>.</p>
<dt>&bull;</p>
<dd><code>ssl_ca_cert</code> (<code>BUNDLE_SSL_CA_CERT</code>): Path to a designated CA certificate file or folder containing multiple certificates for trusted CAs in PEM format.</p>
<dt>&bull;</p>
<dd><code>ssl_client_cert</code> (<code>BUNDLE_SSL_CLIENT_CERT</code>): Path to a designated file containing a X.509 client certificate and key in PEM format.</p>
<dt>&bull;</p>
<dd><code>ssl_verify_mode</code> (<code>BUNDLE_SSL_VERIFY_MODE</code>): The SSL verification mode Bundler uses when making HTTPS requests. Defaults to verify peer.</p>
<dt>&bull;</p>
<dd><code>suppress_install_using_messages</code> (<code>BUNDLE_SUPPRESS_INSTALL_USING_MESSAGES</code>): Avoid printing <code>Using &#8230;</code> messages during installation when the version of a gem has not changed.</p>
<dt>&bull;</p>
<dd><code>system_bindir</code> (<code>BUNDLE_SYSTEM_BINDIR</code>): The location where RubyGems installs binstubs. Defaults to <code>Gem.bindir</code>.</p>
<dt>&bull;</p>
<dd><code>timeout</code> (<code>BUNDLE_TIMEOUT</code>): The seconds allowed before timing out for network requests. Defaults to <code>10</code>.</p>
<dt>&bull;</p>
<dd><code>unlock_source_unlocks_spec</code> (<code>BUNDLE_UNLOCK_SOURCE_UNLOCKS_SPEC</code>): Whether running <code>bundle update &#8211;source NAME</code> unlocks a gem with the given name. Defaults to <code>true</code>.</p>
<dt>&bull;</p>
<dd><code>update_requires_all_flag</code> (<code>BUNDLE_UPDATE_REQUIRES_ALL_FLAG</code>) Require passing <code>&#8211;all</code> to <code>bundle update</code> when everything should be updated, and disallow passing no options to <code>bundle update</code>.</p>
<dt>&bull;</p>
<dd><code>user_agent</code> (<code>BUNDLE_USER_AGENT</code>): The custom user agent fragment Bundler includes in API requests.</p>
<dt>&bull;</p>
<dd><code>with</code> (<code>BUNDLE_WITH</code>): A <code>:</code>-separated list of groups whose gems bundler should install.</p>
<dt>&bull;</p>
<dd><code>without</code> (<code>BUNDLE_WITHOUT</code>): A <code>:</code>-separated list of groups whose gems bundler should not install.</p>
<dd></dl>
<p> In general, you should set these settings per-application by using the applicable flag to the bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i> or bundle <a href="/docs/linux/man/1-package/">package</a>(1) <i>bundle-package.1.html</i> command. </p>
<p> You can set them globally either via environment variables or <code>bundle config</code>, whichever is preferable for your setup. If you use both, environment variables will take preference over global settings.</p>
<h2>Local Git Repos</h2>
<p>Bundler also allows you to work against a git repository locally instead of using the remote version. This can be achieved by setting up a local override:</p>
<dl>
<dd>
<pre>bundle config set local.GEM_NAME /path/to/local/git/repository</pre>
<dd></dl>
<p> For example, in order to use a local Rack repository, a developer could call:</p>
<dl>
<dd>
<pre>bundle config set local.rack ~/Work/git/rack</pre>
<dd></dl>
<p> Now instead of checking out the remote git repository, the local override will be used. Similar to a path source, every time the local git repository change, changes will be automatically picked up by Bundler. This means a commit in the local git repo will update the revision in the <code>Gemfile.lock</code> to the local git repo revision. This requires the same attention as git submodules. Before pushing to the remote, you need to ensure the local override was pushed, otherwise you may point to a commit that only exists in your local machine. You&#8217;ll also need to CGI escape your usernames and passwords as well. </p>
<p> Bundler does many checks to ensure a developer won&#8217;t work with invalid references. Particularly, we force a developer to specify a branch in the <code>Gemfile</code> in order to use this feature. If the branch specified in the <code>Gemfile</code> and the current branch in the local git repository do not match, Bundler will abort. This ensures that a developer is always working against the correct branches, and prevents accidental locking to a different branch. </p>
<p> Finally, Bundler also ensures that the current revision in the <code>Gemfile.lock</code> exists in the local git repository. By doing this, Bundler forces you to fetch the latest changes in the remotes.</p>
<h2>Mirrors Of Gem Sources</h2>
<p>Bundler supports overriding gem sources with mirrors. This allows you to configure rubygems.org as the gem source in your Gemfile while still using your mirror to fetch gems.</p>
<dl>
<dd>
<pre>bundle config set mirror.SOURCE_URL MIRROR_URL</pre>
<dd></dl>
<p> For example, to use a mirror of rubygems.org hosted at rubygems-mirror.org:</p>
<dl>
<dd>
<pre>bundle config set mirror.<a rel="nofollow" href="http://rubygems.org">http://rubygems.org</a> <a rel="nofollow" href="http://rubygems-mirror.org">http://rubygems-mirror.org</a></pre>
<dd></dl>
<p> Each mirror also provides a fallback timeout setting. If the mirror does not respond within the fallback timeout, Bundler will try to use the original server instead of the mirror.</p>
<dl>
<dd>
<pre>bundle config set mirror.SOURCE_URL.fallback_timeout TIMEOUT</pre>
<dd></dl>
<p> For example, to fall back to rubygems.org after 3 seconds:</p>
<dl>
<dd>
<pre>bundle config set mirror.<a rel="nofollow" href="https://rubygems.org.fallback_timeout">https://rubygems.org.fallback_timeout</a> 3</pre>
<dd></dl>
<p> The default fallback timeout is 0.1 seconds, but the setting can currently only accept whole seconds (for example, 1, 15, or 30).</p>
<h2>Credentials For Gem Sources</h2>
<p>Bundler allows you to configure credentials for any gem source, which allows you to avoid putting secrets into your Gemfile.</p>
<dl>
<dd>
<pre>bundle config set SOURCE_HOSTNAME USERNAME:PASSWORD</pre>
<dd></dl>
<p> For example, to save the credentials of user <code>claudette</code> for the gem source at <code>gems.longerous.com</code>, you would run:</p>
<dl>
<dd>
<pre>bundle config set gems.longerous.com claudette:s00pers3krit</pre>
<dd></dl>
<p> Or you can set the credentials as an environment variable like this:</p>
<dl>
<dd>
<pre>export BUNDLE_GEMS__LONGEROUS__COM=&quot;claudette:s00pers3krit&quot;</pre>
<dd></dl>
<p> For gems with a git source with HTTP(S) URL you can specify credentials like so:</p>
<dl>
<dd>
<pre>bundle config set <a rel="nofollow" href="https://github.com/bundler/bundler.git">https://github.com/bundler/bundler.git</a> username:password</pre>
<dd></dl>
<p> Or you can set the credentials as an environment variable like so:</p>
<dl>
<dd>
<pre>export BUNDLE_GITHUB__COM=username:password</pre>
<dd></dl>
<p> This is especially useful for private repositories on hosts such as Github, where you can use personal OAuth tokens:</p>
<dl>
<dd>
<pre>export BUNDLE_GITHUB__COM=abcd0123generatedtoken:x-oauth-basic</pre>
<dd></dl>
<h2>Configure Bundler Directories</h2>
<p>Bundler&#8217;s home, config, cache and plugin directories are able to be configured through environment variables. The default location for Bundler&#8217;s home directory is <code>~/.bundle</code>, which all directories inherit from by default. The following outlines the available environment variables and their default values</p>
<dl>
<dd>
<pre>BUNDLE_USER_HOME : $HOME/.bundle
BUNDLE_USER_CACHE : $BUNDLE_USER_HOME/cache
BUNDLE_USER_CONFIG : $BUNDLE_USER_HOME/config
BUNDLE_USER_PLUGIN : $BUNDLE_USER_HOME/plugin</pre>
<dd></dl>
