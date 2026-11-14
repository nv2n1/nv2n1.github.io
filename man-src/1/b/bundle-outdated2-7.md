---
title: "bundle-outdated2-7(1)"
name: "bundle-outdated2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-outdated2-7/"
description: "bundle-outdated – List installed gems with newer versions available"
---

<p><code>bundle-outdated</code> &#8211; List installed gems with newer versions available </p>
<h2>Synopsis</h2>
<p><code>bundle outdated</code> [GEM] [&#8211;local] [&#8211;pre] [&#8211;source] [&#8211;strict] [&#8211;parseable | &#8211;porcelain] [&#8211;group=GROUP] [&#8211;groups] [&#8211;update-strict] [&#8211;patch|&#8211;minor|&#8211;major] [&#8211;filter-major] [&#8211;filter-minor] [&#8211;filter-patch] [&#8211;only-explicit]</p>
<h2>Description</h2>
<p>Outdated lists the names and versions of gems that have a newer version available in the given source. Calling outdated with [GEM [GEM]] will only check for newer versions of the given gems. Prerelease gems are ignored by default. If your gems are up to date, Bundler will exit with a status of 0. Otherwise, it will exit 1.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;local</code></p>
<dd>Do not attempt to fetch gems remotely and use the gem cache instead.</p>
<dt><code>&#8211;pre</code></p>
<dd>Check for newer pre-release gems.</p>
<dt><code>&#8211;source</code></p>
<dd>Check against a specific source.</p>
<dt><code>&#8211;strict</code></p>
<dd>Only list newer versions allowed by your Gemfile requirements.</p>
<dt><code>&#8211;parseable</code>, <code>&#8211;porcelain</code></p>
<dd>Use minimal formatting for more parseable output.</p>
<dt><code>&#8211;group</code></p>
<dd>List gems from a specific group.</p>
<dt><code>&#8211;groups</code></p>
<dd>List gems organized by groups.</p>
<dt><code>&#8211;update-strict</code></p>
<dd>Strict conservative resolution, do not allow any gem to be updated past latest &#8211;patch | &#8211;minor| &#8211;major.</p>
<dt><code>&#8211;minor</code></p>
<dd>Prefer updating only to next minor version.</p>
<dt><code>&#8211;major</code></p>
<dd>Prefer updating to next major version (default).</p>
<dt><code>&#8211;patch</code></p>
<dd>Prefer updating only to next patch version.</p>
<dt><code>&#8211;filter-major</code></p>
<dd>Only list major newer versions.</p>
<dt><code>&#8211;filter-minor</code></p>
<dd>Only list minor newer versions.</p>
<dt><code>&#8211;filter-patch</code></p>
<dd>Only list patch newer versions.</p>
<dt><code>&#8211;only-explicit</code></p>
<dd>Only list gems specified in your Gemfile, not their dependencies.</dl>
<h2>Patch Level Options</h2>
<p>See bundle <a href="/docs/linux/man/1-update/">update</a>(1) <i>bundle-update.1.html</i> for details. </p>
<p> One difference between the patch level options in <code>bundle update</code> and here is the <code>&#8211;strict</code> option. <code>&#8211;strict</code> was already an option on outdated before the patch level options were added. <code>&#8211;strict</code> wasn&#8217;t altered, and the <code>&#8211;update-strict</code> option on <code>outdated</code> reflects what <code>&#8211;strict</code> does on <code>bundle update</code>.</p>
<h2>Filtering Output</h2>
<p>The 3 filtering options do not affect the resolution of versions, merely what versions are shown in the output. </p>
<p> If the regular output shows the following:</p>
<dl>
<dd>
<pre>* faker (newest 1.6.6, installed 1.6.5, requested ~&gt; 1.4) in groups &quot;development, test&quot;
* hashie (newest 3.4.6, installed 1.2.0, requested = 1.2.0) in groups &quot;default&quot;
* headless (newest 2.3.1, installed 2.2.3) in groups &quot;test&quot;</pre>
<dd></dl>
<p> <code>&#8211;filter-major</code> would only show:</p>
<dl>
<dd>
<pre>* hashie (newest 3.4.6, installed 1.2.0, requested = 1.2.0) in groups &quot;default&quot;</pre>
<dd></dl>
<p> <code>&#8211;filter-minor</code> would only show:</p>
<dl>
<dd>
<pre>* headless (newest 2.3.1, installed 2.2.3) in groups &quot;test&quot;</pre>
<dd></dl>
<p> <code>&#8211;filter-patch</code> would only show:</p>
<dl>
<dd>
<pre>* faker (newest 1.6.6, installed 1.6.5, requested ~&gt; 1.4) in groups &quot;development, test&quot;</pre>
<dd></dl>
<p> Filter options can be combined. <code>&#8211;filter-minor</code> and <code>&#8211;filter-patch</code> would show:</p>
<dl>
<dd>
<pre>* faker (newest 1.6.6, installed 1.6.5, requested ~&gt; 1.4) in groups &quot;development, test&quot;
* headless (newest 2.3.1, installed 2.2.3) in groups &quot;test&quot;</pre>
<dd></dl>
<p> Combining all three <code>filter</code> options would be the same result as providing none of them.</p>
