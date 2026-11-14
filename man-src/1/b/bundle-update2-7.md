---
title: "bundle-update2-7(1)"
name: "bundle-update2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-update2-7/"
description: "bundle-update – Update your gems to the latest available versions"
---

<p><code>bundle-update</code> &#8211; Update your gems to the latest available versions </p>
<h2>Synopsis</h2>
<p><code>bundle update</code> <i>*gems</i> [&#8211;all] [&#8211;group=NAME] [&#8211;source=NAME] [&#8211;local] [&#8211;ruby] [&#8211;bundler[=VERSION]] [&#8211;full-index] [&#8211;jobs=JOBS] [&#8211;quiet] [&#8211;patch|&#8211;minor|&#8211;major] [&#8211;redownload] [&#8211;strict] [&#8211;conservative]</p>
<h2>Description</h2>
<p>Update the gems specified (all gems, if <code>&#8211;all</code> flag is used), ignoring the previously installed gems specified in the <code>Gemfile.lock</code>. In general, you should use bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i> to install the same exact gems and versions across machines. </p>
<p> You would use <code>bundle update</code> to explicitly update the version of a gem.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;all</code></p>
<dd>Update all gems specified in Gemfile.</p>
<dt><code>&#8211;group=&lt;name&gt;</code>, <code>-g=[&lt;name&gt;]</code></p>
<dd>Only update the gems in the specified group. For instance, you can update all gems in the development group with <code>bundle update &#8211;group development</code>. You can also call <code>bundle update rails &#8211;group test</code> to update the rails gem and all gems in the test group, for example.</p>
<dt><code>&#8211;source=&lt;name&gt;</code></p>
<dd>The name of a <code>:git</code> or <code>:path</code> source used in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5). For instance, with a <code>:git</code> source of <code><a rel="nofollow" href="http://github.com/rails/rails.git">http://github.com/rails/rails.git</a></code>, you would call <code>bundle update &#8211;source rails</code></p>
<dt><code>&#8211;local</code></p>
<dd>Do not attempt to fetch gems remotely and use the gem cache instead.</p>
<dt><code>&#8211;ruby</code></p>
<dd>Update the locked version of Ruby to the current version of Ruby.</p>
<dt><code>&#8211;bundler</code></p>
<dd>Update the locked version of bundler to the invoked bundler version.</p>
<dt><code>&#8211;full-index</code></p>
<dd>Fall back to using the single-file index of all gems.</p>
<dt><code>&#8211;jobs=[&lt;number&gt;]</code>, <code>-j[&lt;number&gt;]</code></p>
<dd>Specify the number of jobs to run in parallel. The default is <code>1</code>.</p>
<dt><code>&#8211;retry=[&lt;number&gt;]</code></p>
<dd>Retry failed network or git requests for <i>number</i> times.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Only output warnings and errors.</p>
<dt><code>&#8211;redownload</code></p>
<dd>Force downloading every gem.</p>
<dt><code>&#8211;patch</code></p>
<dd>Prefer updating only to next patch version.</p>
<dt><code>&#8211;minor</code></p>
<dd>Prefer updating only to next minor version.</p>
<dt><code>&#8211;major</code></p>
<dd>Prefer updating to next major version (default).</p>
<dt><code>&#8211;strict</code></p>
<dd>Do not allow any gem to be updated past latest <code>&#8211;patch</code> | <code>&#8211;minor</code> | <code>&#8211;major</code>.</p>
<dt><code>&#8211;conservative</code></p>
<dd>Use bundle install conservative update behavior and do not allow shared dependencies to be updated.</dl>
<h2>Updating All Gems</h2>
<p>If you run <code>bundle update &#8211;all</code>, bundler will ignore any previously installed gems and resolve all dependencies again based on the latest versions of all gems available in the sources. </p>
<p> Consider the following <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5):</p>
<dl>
<dd>
<pre>source &quot;<a rel="nofollow" href="https://rubygems.org">https://rubygems.org</a>&quot;
gem &quot;rails&quot;, &quot;3.0.0.rc&quot;
gem &quot;nokogiri&quot;</pre>
<dd></dl>
<p> When you run bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i> the first time, bundler will resolve all of the dependencies, all the way down, and install what you need:</p>
<dl>
<dd>
<pre>Fetching gem metadata from <a rel="nofollow" href="https://rubygems.org/.........">https://rubygems.org/.........</a>
Resolving dependencies...
Installing builder 2.1.2
Installing abstract 1.0.0
Installing rack 1.2.8
Using bundler 1.7.6
Installing rake 10.4.0
Installing polyglot 0.3.5
Installing mime-types 1.25.1
Installing i18n 0.4.2
Installing mini_portile 0.6.1
Installing tzinfo 0.3.42
Installing rack-mount 0.6.14
Installing rack-test 0.5.7
Installing treetop 1.4.15
Installing thor 0.14.6
Installing activesupport 3.0.0.rc
Installing erubis 2.6.6
Installing activemodel 3.0.0.rc
Installing arel 0.4.0
Installing mail 2.2.20
Installing activeresource 3.0.0.rc
Installing actionpack 3.0.0.rc
Installing activerecord 3.0.0.rc
Installing actionmailer 3.0.0.rc
Installing railties 3.0.0.rc
Installing rails 3.0.0.rc
Installing nokogiri 1.6.5
Bundle complete! 2 Gemfile dependencies, 26 gems total.
Use `bundle show [gemname]` to see where a bundled gem is installed.</pre>
<dd></dl>
<p> As you can see, even though you have two gems in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5), your application needs 26 different gems in order to run. Bundler remembers the exact versions it installed in <code>Gemfile.lock</code>. The next time you run bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i>, bundler skips the dependency resolution and installs the same gems as it installed last time. </p>
<p> After checking in the <code>Gemfile.lock</code> into version control and cloning it on another machine, running bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i> will <i>still</i> install the gems that you installed last time. You don&#8217;t need to worry that a new release of <code>erubis</code> or <code>mail</code> changes the gems you use. </p>
<p> However, from time to time, you might want to update the gems you are using to the newest versions that still match the gems in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5). </p>
<p> To do this, run <code>bundle update &#8211;all</code>, which will ignore the <code>Gemfile.lock</code>, and resolve all the dependencies again. Keep in mind that this process can result in a significantly different set of the 25 gems, based on the requirements of new gems that the gem authors released since the last time you ran <code>bundle update &#8211;all</code>.</p>
<h2>Updating A List Of Gems</h2>
<p>Sometimes, you want to update a single gem in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5), and leave the rest of the gems that you specified locked to the versions in the <code>Gemfile.lock</code>. </p>
<p> For instance, in the scenario above, imagine that <code>nokogiri</code> releases version <code>1.4.4</code>, and you want to update it <i>without</i> updating Rails and all of its dependencies. To do this, run <code>bundle update nokogiri</code>. </p>
<p> Bundler will update <code>nokogiri</code> and any of its dependencies, but leave alone Rails and its dependencies.</p>
<h2>Overlapping Dependencies</h2>
<p>Sometimes, multiple gems declared in your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) are satisfied by the same second-level dependency. For instance, consider the case of <code>thin</code> and <code>rack-perftools-profiler</code>.</p>
<dl>
<dd>
<pre>source &quot;<a rel="nofollow" href="https://rubygems.org">https://rubygems.org</a>&quot;
gem &quot;thin&quot;
gem &quot;rack-perftools-profiler&quot;</pre>
<dd></dl>
<p> The <code>thin</code> gem depends on <code>rack &gt;= 1.0</code>, while <code>rack-perftools-profiler</code> depends on <code>rack ~&gt; 1.0</code>. If you run bundle install, you get:</p>
<dl>
<dd>
<pre>Fetching source index for <a rel="nofollow" href="https://rubygems.org/">https://rubygems.org/</a>
Installing daemons (1.1.0)
Installing eventmachine (0.12.10) with native extensions
Installing open4 (1.0.1)
Installing perftools.rb (0.4.7) with native extensions
Installing rack (1.2.1)
Installing rack-perftools_profiler (0.0.2)
Installing thin (1.2.7) with native extensions
Using bundler (1.0.0.rc.3)</pre>
<dd></dl>
<p> In this case, the two gems have their own set of dependencies, but they share <code>rack</code> in common. If you run <code>bundle update thin</code>, bundler will update <code>daemons</code>, <code>eventmachine</code> and <code>rack</code>, which are dependencies of <code>thin</code>, but not <code>open4</code> or <code>perftools.rb</code>, which are dependencies of <code>rack-perftools_profiler</code>. Note that <code>bundle update thin</code> will update <code>rack</code> even though it&#8217;s <i>also</i> a dependency of <code>rack-perftools_profiler</code>. </p>
<p> In short, by default, when you update a gem using <code>bundle update</code>, bundler will update all dependencies of that gem, including those that are also dependencies of another gem. </p>
<p> To prevent updating shared dependencies, prior to version 1.14 the only option was the <code>CONSERVATIVE UPDATING</code> behavior in bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i>: </p>
<p> In this scenario, updating the <code>thin</code> version manually in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5), and then running bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i> will only update <code>daemons</code> and <code>eventmachine</code>, but not <code>rack</code>. For more information, see the <code>CONSERVATIVE UPDATING</code> section of bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i>. </p>
<p> Starting with 1.14, specifying the <code>&#8211;conservative</code> option will also prevent shared dependencies from being updated.</p>
<h2>Patch Level Options</h2>
<p>Version 1.14 introduced 4 patch-level options that will influence how gem versions are resolved. One of the following options can be used: <code>&#8211;patch</code>, <code>&#8211;minor</code> or <code>&#8211;major</code>. <code>&#8211;strict</code> can be added to further influence resolution.</p>
<dl>
<dt><code>&#8211;patch</code></p>
<dd>Prefer updating only to next patch version.</p>
<dt><code>&#8211;minor</code></p>
<dd>Prefer updating only to next minor version.</p>
<dt><code>&#8211;major</code></p>
<dd>Prefer updating to next major version (default).</p>
<dt><code>&#8211;strict</code></p>
<dd>Do not allow any gem to be updated past latest <code>&#8211;patch</code> | <code>&#8211;minor</code> | <code>&#8211;major</code>.</dl>
<p> When Bundler is resolving what versions to use to satisfy declared requirements in the Gemfile or in parent gems, it looks up all available versions, filters out any versions that don&#8217;t satisfy the requirement, and then, by default, sorts them from newest to oldest, considering them in that order. </p>
<p> Providing one of the patch level options (e.g. <code>&#8211;patch</code>) changes the sort order of the satisfying versions, causing Bundler to consider the latest <code>&#8211;patch</code> or <code>&#8211;minor</code> version available before other versions. Note that versions outside the stated patch level could still be resolved to if necessary to find a suitable dependency graph. </p>
<p> For example, if gem &#8216;foo&#8217; is locked at 1.0.2, with no gem requirement defined in the Gemfile, and versions 1.0.3, 1.0.4, 1.1.0, 1.1.1, 2.0.0 all exist, the default order of preference by default (<code>&#8211;major</code>) will be &quot;2.0.0, 1.1.1, 1.1.0, 1.0.4, 1.0.3, 1.0.2&quot;. </p>
<p> If the <code>&#8211;patch</code> option is used, the order of preference will change to &quot;1.0.4, 1.0.3, 1.0.2, 1.1.1, 1.1.0, 2.0.0&quot;. </p>
<p> If the <code>&#8211;minor</code> option is used, the order of preference will change to &quot;1.1.1, 1.1.0, 1.0.4, 1.0.3, 1.0.2, 2.0.0&quot;. </p>
<p> Combining the <code>&#8211;strict</code> option with any of the patch level options will remove any versions beyond the scope of the patch level option, to ensure that no gem is updated that far. </p>
<p> To continue the previous example, if both <code>&#8211;patch</code> and <code>&#8211;strict</code> options are used, the available versions for resolution would be &quot;1.0.4, 1.0.3, 1.0.2&quot;. If <code>&#8211;minor</code> and <code>&#8211;strict</code> are used, it would be &quot;1.1.1, 1.1.0, 1.0.4, 1.0.3, 1.0.2&quot;. </p>
<p> Gem requirements as defined in the Gemfile will still be the first determining factor for what versions are available. If the gem requirement for <code>foo</code> in the Gemfile is &#8216;~&gt; 1.0&#8217;, that will accomplish the same thing as providing the <code>&#8211;minor</code> and <code>&#8211;strict</code> options.</p>
<h2>Patch Level Examples</h2>
<p>Given the following gem specifications:</p>
<dl>
<dd>
<pre>foo 1.4.3, requires: ~&gt; bar 2.0
foo 1.4.4, requires: ~&gt; bar 2.0
foo 1.4.5, requires: ~&gt; bar 2.1
foo 1.5.0, requires: ~&gt; bar 2.1
foo 1.5.1, requires: ~&gt; bar 3.0
bar with versions 2.0.3, 2.0.4, 2.1.0, 2.1.1, 3.0.0</pre>
<dd></dl>
<p> Gemfile:</p>
<dl>
<dd>
<pre>gem 'foo'</pre>
<dd></dl>
<p> Gemfile.lock:</p>
<dl>
<dd>
<pre>foo (1.4.3)
 bar (~&gt; 2.0)
bar (2.0.3)</pre>
<dd></dl>
<p> Cases:</p>
<dl>
<dd>
<pre># Command Line Result
------------------------------------------------------------
1 bundle update --patch 'foo 1.4.5', 'bar 2.1.1'
2 bundle update --patch foo 'foo 1.4.5', 'bar 2.1.1'
3 bundle update --minor 'foo 1.5.1', 'bar 3.0.0'
4 bundle update --minor --strict 'foo 1.5.0', 'bar 2.1.1'
5 bundle update --patch --strict 'foo 1.4.4', 'bar 2.0.4'</pre>
<dd></dl>
<p> In case 1, bar is upgraded to 2.1.1, a minor version increase, because the dependency from foo 1.4.5 required it. </p>
<p> In case 2, only foo is requested to be unlocked, but bar is also allowed to move because it&#8217;s not a declared dependency in the Gemfile. </p>
<p> In case 3, bar goes up a whole major release, because a minor increase is preferred now for foo, and when it goes to 1.5.1, it requires 3.0.0 of bar. </p>
<p> In case 4, foo is preferred up to a minor version, but 1.5.1 won&#8217;t work because the &#8211;strict flag removes bar 3.0.0 from consideration since it&#8217;s a major increment. </p>
<p> In case 5, both foo and bar have any minor or major increments removed from consideration because of the &#8211;strict flag, so the most they can move is up to 1.4.4 and 2.0.4.</p>
<h2>Recommended Workflow</h2>
<p>In general, when working with an application managed with bundler, you should use the following workflow:</p>
<dl>
<dt>&bull;</p>
<dd>After you create your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) for the first time, run</p>
<dd>$ bundle install</p>
<dt>&bull;</p>
<dd>Check the resulting <code>Gemfile.lock</code> into version control</p>
<dd>$ git add Gemfile.lock</p>
<dt>&bull;</p>
<dd>When checking out this repository on another development machine, run</p>
<dd>$ bundle install</p>
<dt>&bull;</p>
<dd>When checking out this repository on a deployment machine, run</p>
<dd>$ bundle install &#8211;deployment</p>
<dt>&bull;</p>
<dd>After changing the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5) to reflect a new or update dependency, run</p>
<dd>$ bundle install</p>
<dt>&bull;</p>
<dd>Make sure to check the updated <code>Gemfile.lock</code> into version control</p>
<dd>$ git add Gemfile.lock</p>
<dt>&bull;</p>
<dd>If bundle <a href="/docs/linux/man/1-install/">install</a>(1) <i>bundle-install.1.html</i> reports a conflict, manually update the specific gems that you changed in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</p>
<dd>$ bundle update rails thin</p>
<dt>&bull;</p>
<dd>If you want to update all the gems to the latest possible versions that still match the gems listed in the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5), run</p>
<dd>$ bundle update &#8211;all</p>
<dd></dl>
