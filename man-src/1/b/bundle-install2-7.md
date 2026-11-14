---
title: "bundle-install2-7(1)"
name: "bundle-install2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-install2-7/"
description: "bundle-install – Install the dependencies specified in your Gemfile"
---

<p><code>bundle-install</code> &#8211; Install the dependencies specified in your Gemfile </p>
<h2>Synopsis</h2>
<p><code>bundle install</code> [&#8211;binstubs[=DIRECTORY]] [&#8211;clean] [&#8211;deployment] [&#8211;frozen] [&#8211;full-index] [&#8211;gemfile=GEMFILE] [&#8211;jobs=NUMBER] [&#8211;local] [&#8211;no-cache] [&#8211;no-prune] [&#8211;path PATH] [&#8211;quiet] [&#8211;redownload] [&#8211;retry=NUMBER] [&#8211;shebang] [&#8211;standalone[=GROUP[ GROUP&#8230;]]] [&#8211;system] [&#8211;trust-policy=POLICY] [&#8211;with=GROUP[ GROUP&#8230;]] [&#8211;without=GROUP[ GROUP&#8230;]]</p>
<h2>Description</h2>
<p>Install the gems specified in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5). If this is the first time you run bundle install (and a <code>Gemfile.lock</code> does not exist), Bundler will fetch all remote sources, resolve dependencies and install all needed gems. </p>
<p> If a <code>Gemfile.lock</code> does exist, and you have not updated your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5), Bundler will fetch all remote sources, but use the dependencies specified in the <code>Gemfile.lock</code> instead of resolving dependencies. </p>
<p> If a <code>Gemfile.lock</code> does exist, and you have updated your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5), Bundler will use the dependencies in the <code>Gemfile.lock</code> for all gems that you did not update, but will re-resolve the dependencies of gems that you did update. You can find more information about this update process below under <i>CONSERVATIVE UPDATING</i>.</p>
<h2>Options</h2>
<p>To apply any of <code>&#8211;binstubs</code>, <code>&#8211;deployment</code>, <code>&#8211;path</code>, or <code>&#8211;without</code> every time <code>bundle install</code> is run, use <code>bundle config</code> (see <a href="/docs/linux/man/1-bundle-config/">bundle-config</a>(1)).</p>
<dl>
<dt><code>&#8211;binstubs[=&lt;directory&gt;]</code></p>
<dd>Binstubs are scripts that wrap around executables. Bundler creates a small Ruby file (a binstub) that loads Bundler, runs the command, and puts it in <code>bin/</code>. This lets you link the binstub inside of an application to the exact gem version the application needs.</p>
<dd>Creates a directory (defaults to <code>~/bin</code>) and places any executables from the gem there. These executables run in Bundler&#8217;s context. If used, you might add this directory to your environment&#8217;s <code>PATH</code> variable. For instance, if the <code>rails</code> gem comes with a <code>rails</code> executable, this flag will create a <code>bin/rails</code> executable that ensures that all referred dependencies will be resolved using the bundled gems.</p>
<dt><code>&#8211;clean</code></p>
<dd>On finishing the installation Bundler is going to remove any gems not present in the current <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5). Don&#8217;t worry, gems currently in use will not be removed.</p>
<dt><code>&#8211;deployment</code></p>
<dd>In <i>deployment mode</i>, Bundler will &#8216;roll-out&#8217; the bundle for production or CI use. Please check carefully if you want to have this option enabled in your development environment.</p>
<dt><code>&#8211;redownload</code></p>
<dd>Force download every gem, even if the required versions are already available locally.</p>
<dt><code>&#8211;frozen</code></p>
<dd>Do not allow the Gemfile.lock to be updated after this install. Exits non-zero if there are going to be changes to the Gemfile.lock.</p>
<dt><code>&#8211;full-index</code></p>
<dd>Bundler will not call Rubygems&#8217; API endpoint (default) but download and cache a (currently big) index file of all gems. Performance can be improved for large bundles that seldom change by enabling this option.</p>
<dt><code>&#8211;gemfile=&lt;gemfile&gt;</code></p>
<dd>The location of the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) which Bundler should use. This defaults to a <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) in the current working directory. In general, Bundler will assume that the location of the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) is also the project&#8217;s root and will try to find <code>Gemfile.lock</code> and <code>vendor/cache</code> relative to this location.</p>
<dt><code>&#8211;jobs=[&lt;number&gt;]</code>, <code>-j[&lt;number&gt;]</code></p>
<dd>The maximum number of parallel download and install jobs. The default is <code>1</code>.</p>
<dt><code>&#8211;local</code></p>
<dd>Do not attempt to connect to <code>rubygems.org</code>. Instead, Bundler will use the gems already present in Rubygems&#8217; cache or in <code>vendor/cache</code>. Note that if a appropriate platform-specific gem exists on <code>rubygems.org</code> it will not be found.</p>
<dt><code>&#8211;no-cache</code></p>
<dd>Do not update the cache in <code>vendor/cache</code> with the newly bundled gems. This does not remove any gems in the cache but keeps the newly bundled gems from being cached during the install.</p>
<dt><code>&#8211;no-prune</code></p>
<dd>Don&#8217;t remove stale gems from the cache when the installation finishes.</p>
<dt><code>&#8211;path=&lt;path&gt;</code></p>
<dd>The location to install the specified gems to. This defaults to Rubygems&#8217; setting. Bundler shares this location with Rubygems, <code>gem install &#8230;</code> will have gem installed there, too. Therefore, gems installed without a <code>&#8211;path &#8230;</code> setting will show up by calling <code>gem list</code>. Accordingly, gems installed to other locations will not get listed.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Do not print progress information to the standard output. Instead, Bundler will exit using a status code (<code>$?</code>).</p>
<dt><code>&#8211;retry=[&lt;number&gt;]</code></p>
<dd>Retry failed network or git requests for <i>number</i> times.</p>
<dt><code>&#8211;shebang=&lt;ruby-executable&gt;</code></p>
<dd>Uses the specified ruby executable (usually <code>ruby</code>) to execute the scripts created with <code>&#8211;binstubs</code>. In addition, if you use <code>&#8211;binstubs</code> together with <code>&#8211;shebang jruby</code> these executables will be changed to execute <code>jruby</code> instead.</p>
<dt><code>&#8211;standalone[=&lt;list&gt;]</code></p>
<dd>Makes a bundle that can work without depending on Rubygems or Bundler at runtime. A space separated list of groups to install has to be specified. Bundler creates a directory named <code>bundle</code> and installs the bundle there. It also generates a <code>bundle/bundler/setup.rb</code> file to replace Bundler&#8217;s own setup in the manner required. Using this option implicitly sets <code>path</code>, which is a [remembered option][REMEMBERED OPTIONS].</p>
<dt><code>&#8211;system</code></p>
<dd>Installs the gems specified in the bundle to the system&#8217;s Rubygems location. This overrides any previous configuration of <code>&#8211;path</code>.</p>
<dt><code>&#8211;trust-policy=[&lt;policy&gt;]</code></p>
<dd>Apply the Rubygems security policy <i>policy</i>, where policy is one of <code>HighSecurity</code>, <code>MediumSecurity</code>, <code>LowSecurity</code>, <code>AlmostNoSecurity</code>, or <code>NoSecurity</code>. For more details, please see the Rubygems signing documentation linked below in <i>SEE ALSO</i>.</p>
<dt><code>&#8211;with=&lt;list&gt;</code></p>
<dd>A space-separated list of groups referencing gems to install. If an optional group is given it is installed. If a group is given that is in the remembered list of groups given to &#8211;without, it is removed from that list.</p>
<dt><code>&#8211;without=&lt;list&gt;</code></p>
<dd>A space-separated list of groups referencing gems to skip during installation. If a group is given that is in the remembered list of groups given to &#8211;with, it is removed from that list.</dl>
<h2>Deployment Mode</h2>
<p>Bundler&#8217;s defaults are optimized for development. To switch to defaults optimized for deployment and for CI, use the <code>&#8211;deployment</code> flag. Do not activate deployment mode on development machines, as it will cause an error when the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) is modified.</p>
<dl>
<dt>1.</p>
<dd>A <code>Gemfile.lock</code> is required.</p>
<dd>To ensure that the same versions of the gems you developed with and tested with are also used in deployments, a <code>Gemfile.lock</code> is required.</p>
<dd>This is mainly to ensure that you remember to check your <code>Gemfile.lock</code> into version control.</p>
<dt>2.</p>
<dd>The <code>Gemfile.lock</code> must be up to date</p>
<dd>In development, you can modify your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) and re-run <code>bundle install</code> to <i>conservatively update</i> your <code>Gemfile.lock</code> snapshot.</p>
<dd>In deployment, your <code>Gemfile.lock</code> should be up-to-date with changes made in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5).</p>
<dt>3.</p>
<dd>Gems are installed to <code>vendor/bundle</code> not your default system location</p>
<dd>In development, it&#8217;s convenient to share the gems used in your application with other applications and other scripts that run on the system.</p>
<dd>In deployment, isolation is a more important default. In addition, the user deploying the application may not have permission to install gems to the system, or the web server may not have permission to read them.</p>
<dd>As a result, <code>bundle install &#8211;deployment</code> installs gems to the <code>vendor/bundle</code> directory in the application. This may be overridden using the <code>&#8211;path</code> option.</p>
<dd></dl>
<h2>Sudo Usage</h2>
<p>By default, Bundler installs gems to the same location as <code>gem install</code>. </p>
<p> In some cases, that location may not be writable by your Unix user. In that case, Bundler will stage everything in a temporary directory, then ask you for your <code>sudo</code> password in order to copy the gems into their system location. </p>
<p> From your perspective, this is identical to installing the gems directly into the system. </p>
<p> You should never use <code>sudo bundle install</code>. This is because several other steps in <code>bundle install</code> must be performed as the current user:</p>
<dl>
<dt>&bull;</p>
<dd>Updating your <code>Gemfile.lock</code></p>
<dt>&bull;</p>
<dd>Updating your <code>vendor/cache</code>, if necessary</p>
<dt>&bull;</p>
<dd>Checking out private git repositories using your user&#8217;s SSH keys</p>
<dd></dl>
<p> Of these three, the first two could theoretically be performed by <code>chown</code>ing the resulting files to <code>$SUDO_USER</code>. The third, however, can only be performed by invoking the <code>git</code> command as the current user. Therefore, git gems are downloaded and installed into <code>~/.bundle</code> rather than $GEM_HOME or $BUNDLE_PATH. </p>
<p> As a result, you should run <code>bundle install</code> as the current user, and Bundler will ask for your password if it is needed to put the gems into their final location.</p>
<h2>Installing Groups</h2>
<p>By default, <code>bundle install</code> will install all gems in all groups in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5), except those declared for a different platform. </p>
<p> However, you can explicitly tell Bundler to skip installing certain groups with the <code>&#8211;without</code> option. This option takes a space-separated list of groups. </p>
<p> While the <code>&#8211;without</code> option will skip <i>installing</i> the gems in the specified groups, it will still <i>download</i> those gems and use them to resolve the dependencies of every gem in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5). </p>
<p> This is so that installing a different set of groups on another machine (such as a production server) will not change the gems and versions that you have already developed and tested against. </p>
<p> <code>Bundler offers a rock-solid guarantee that the third-party code you are running in development and testing is also the third-party code you are running in production. You can choose to exclude some of that code in different environments, but you will never be caught flat-footed by different versions of third-party code being used in different environments.</code> </p>
<p> For a simple illustration, consider the following <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5):</p>
<dl>
<dd>
<pre>source '<a rel="nofollow" href="https://rubygems.org'">https://rubygems.org'</a>
gem 'sinatra'
group :production do
 gem 'rack-perftools-profiler'
end</pre>
<dd></dl>
<p> In this case, <code>sinatra</code> depends on any version of Rack (<code>&gt;= 1.0</code>), while <code>rack-perftools-profiler</code> depends on 1.x (<code>~&gt; 1.0</code>). </p>
<p> When you run <code>bundle install &#8211;without production</code> in development, we look at the dependencies of <code>rack-perftools-profiler</code> as well. That way, you do not spend all your time developing against Rack 2.0, using new APIs unavailable in Rack 1.x, only to have Bundler switch to Rack 1.2 when the <code>production</code> group <i>is</i> used. </p>
<p> This should not cause any problems in practice, because we do not attempt to <code>install</code> the gems in the excluded groups, and only evaluate as part of the dependency resolution process. </p>
<p> This also means that you cannot include different versions of the same gem in different groups, because doing so would result in different sets of dependencies used in development and production. Because of the vagaries of the dependency resolution process, this usually affects more than the gems you list in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5), and can (surprisingly) radically change the gems you are using.</p>
<h2>The Gemfile.Lock</h2>
<p>When you run <code>bundle install</code>, Bundler will persist the full names and versions of all gems that you used (including dependencies of the gems specified in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)) into a file called <code>Gemfile.lock</code>. </p>
<p> Bundler uses this file in all subsequent calls to <code>bundle install</code>, which guarantees that you always use the same exact code, even as your application moves across machines. </p>
<p> Because of the way dependency resolution works, even a seemingly small change (for instance, an update to a point-release of a dependency of a gem in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)) can result in radically different gems being needed to satisfy all dependencies. </p>
<p> As a result, you <code>SHOULD</code> check your <code>Gemfile.lock</code> into version control, in both applications and gems. If you do not, every machine that checks out your repository (including your production server) will resolve all dependencies again, which will result in different versions of third-party code being used if <code>any</code> of the gems in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) or any of their dependencies have been updated. </p>
<p> When Bundler first shipped, the <code>Gemfile.lock</code> was included in the <code>.gitignore</code> file included with generated gems. Over time, however, it became clear that this practice forces the pain of broken dependencies onto new contributors, while leaving existing contributors potentially unaware of the problem. Since <code>bundle install</code> is usually the first step towards a contribution, the pain of broken dependencies would discourage new contributors from contributing. As a result, we have revised our guidance for gem authors to now recommend checking in the lock for gems.</p>
<h2>Conservative Updating</h2>
<p>When you make a change to the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) and then run <code>bundle install</code>, Bundler will update only the gems that you modified. </p>
<p> In other words, if a gem that you <code>did not modify</code> worked before you called <code>bundle install</code>, it will continue to use the exact same versions of all dependencies as it used before the update. </p>
<p> Let&#8217;s take a look at an example. Here&#8217;s your original <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5):</p>
<dl>
<dd>
<pre>source '<a rel="nofollow" href="https://rubygems.org'">https://rubygems.org'</a>
gem 'actionpack', '2.3.8'
gem 'activemerchant'</pre>
<dd></dl>
<p> In this case, both <code>actionpack</code> and <code>activemerchant</code> depend on <code>activesupport</code>. The <code>actionpack</code> gem depends on <code>activesupport 2.3.8</code> and <code>rack ~&gt; 1.1.0</code>, while the <code>activemerchant</code> gem depends on <code>activesupport &gt;= 2.3.2</code>, <code>braintree &gt;= 2.0.0</code>, and <code>builder &gt;= 2.0.0</code>. </p>
<p> When the dependencies are first resolved, Bundler will select <code>activesupport 2.3.8</code>, which satisfies the requirements of both gems in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5). </p>
<p> Next, you modify your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) to:</p>
<dl>
<dd>
<pre>source '<a rel="nofollow" href="https://rubygems.org'">https://rubygems.org'</a>
gem 'actionpack', '3.0.0.rc'
gem 'activemerchant'</pre>
<dd></dl>
<p> The <code>actionpack 3.0.0.rc</code> gem has a number of new dependencies, and updates the <code>activesupport</code> dependency to <code>= 3.0.0.rc</code> and the <code>rack</code> dependency to <code>~&gt; 1.2.1</code>. </p>
<p> When you run <code>bundle install</code>, Bundler notices that you changed the <code>actionpack</code> gem, but not the <code>activemerchant</code> gem. It evaluates the gems currently being used to satisfy its requirements:</p>
<dl>
<dt><code>activesupport 2.3.8</code></p>
<dd>also used to satisfy a dependency in <code>activemerchant</code>, which is not being updated</p>
<dt><code>rack ~&gt; 1.1.0</code></p>
<dd>not currently being used to satisfy another dependency</dl>
<p> Because you did not explicitly ask to update <code>activemerchant</code>, you would not expect it to suddenly stop working after updating <code>actionpack</code>. However, satisfying the new <code>activesupport 3.0.0.rc</code> dependency of actionpack requires updating one of its dependencies. </p>
<p> Even though <code>activemerchant</code> declares a very loose dependency that theoretically matches <code>activesupport 3.0.0.rc</code>, Bundler treats gems in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) that have not changed as an atomic unit together with their dependencies. In this case, the <code>activemerchant</code> dependency is treated as <code>activemerchant 1.7.1 + activesupport 2.3.8</code>, so <code>bundle install</code> will report that it cannot update <code>actionpack</code>. </p>
<p> To explicitly update <code>actionpack</code>, including its dependencies which other gems in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) still depend on, run <code>bundle update actionpack</code> (see <code>bundle <a href="/docs/linux/man/1-update/">update</a>(1)</code>). </p>
<p> <code>Summary</code>: In general, after making a change to the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) , you should first try to run <code>bundle install</code>, which will guarantee that no other gem in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) is impacted by the change. If that does not work, run bundle <a href="/docs/linux/man/1-update/">update</a>(1) <i>bundle-update.1.html</i>.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>Gem install docs <i><a rel="nofollow" href="http://guides.rubygems.org/rubygems-basics/#installing-gems">http://guides.rubygems.org/rubygems-basics/#installing-gems</a></i></p>
<dt>&bull;</p>
<dd>Rubygems signing docs <i><a rel="nofollow" href="http://guides.rubygems.org/security/">http://guides.rubygems.org/security/</a></i></p>
<dd></dl>
