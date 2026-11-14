---
title: "bundle-cache2-7(1)"
name: "bundle-cache2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-cache2-7/"
description: "bundle-cache – Package your needed .gem files into your application"
---

<p><code>bundle-cache</code> &#8211; Package your needed <code>.gem</code> files into your application </p>
<h2>Synopsis</h2>
<p><code>bundle cache</code></p>
<h2>Description</h2>
<p>Copy all of the <code>.gem</code> files needed to run the application into the <code>vendor/cache</code> directory. In the future, when running [bundle <a href="/docs/linux/man/1-install/">install</a>(1)][bundle-install], use the gems in the cache in preference to the ones on <code>rubygems.org</code>.</p>
<h2>Git And Path Gems</h2>
<p>The <code>bundle cache</code> command can also package <code>:git</code> and <code>:path</code> dependencies besides .gem files. This needs to be explicitly enabled via the <code>&#8211;all</code> option. Once used, the <code>&#8211;all</code> option will be remembered.</p>
<h2>Support For Multiple Platforms</h2>
<p>When using gems that have different packages for different platforms, Bundler supports caching of gems for other platforms where the Gemfile has been resolved (i.e. present in the lockfile) in <code>vendor/cache</code>. This needs to be enabled via the <code>&#8211;all-platforms</code> option. This setting will be remembered in your local bundler configuration.</p>
<h2>Remote Fetching</h2>
<p>By default, if you run <code>bundle <a href="/docs/linux/man/1-install/">install</a>(1)</code>](bundle-install.1.html) after running bundle <a href="/docs/linux/man/1-cache/">cache</a>(1) <i>bundle-cache.1.html</i>, bundler will still connect to <code>rubygems.org</code> to check whether a platform-specific gem exists for any of the gems in <code>vendor/cache</code>. </p>
<p> For instance, consider this <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5):</p>
<dl>
<dd>
<pre>source &quot;<a rel="nofollow" href="https://rubygems.org">https://rubygems.org</a>&quot;
gem &quot;nokogiri&quot;</pre>
<dd></dl>
<p> If you run <code>bundle cache</code> under C Ruby, bundler will retrieve the version of <code>nokogiri</code> for the <code>&quot;ruby&quot;</code> platform. If you deploy to JRuby and run <code>bundle install</code>, bundler is forced to check to see whether a <code>&quot;java&quot;</code> platformed <code>nokogiri</code> exists. </p>
<p> Even though the <code>nokogiri</code> gem for the Ruby platform is <i>technically</i> acceptable on JRuby, it has a C extension that does not run on JRuby. As a result, bundler will, by default, still connect to <code>rubygems.org</code> to check whether it has a version of one of your gems more specific to your platform. </p>
<p> This problem is also not limited to the <code>&quot;java&quot;</code> platform. A similar (common) problem can happen when developing on Windows and deploying to Linux, or even when developing on OSX and deploying to Linux. </p>
<p> If you know for sure that the gems packaged in <code>vendor/cache</code> are appropriate for the platform you are on, you can run <code>bundle install &#8211;local</code> to skip checking for more appropriate gems, and use the ones in <code>vendor/cache</code>. </p>
<p> One way to be sure that you have the right platformed versions of all your gems is to run <code>bundle cache</code> on an identical machine and check in the gems. For instance, you can run <code>bundle cache</code> on an identical staging box during your staging process, and check in the <code>vendor/cache</code> before deploying to production. </p>
<p> By default, bundle <a href="/docs/linux/man/1-cache/">cache</a>(1) <i>bundle-cache.1.html</i> fetches and also installs the gems to the default location. To package the dependencies to <code>vendor/cache</code> without installing them to the local install location, you can run <code>bundle cache &#8211;no-install</code>.</p>
