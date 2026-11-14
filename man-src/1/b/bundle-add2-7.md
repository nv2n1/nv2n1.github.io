---
title: "bundle-add2-7(1)"
name: "bundle-add2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-add2-7/"
description: "bundle-add – Add gem to the Gemfile and run bundle install"
---

<p><code>bundle-add</code> &#8211; Add gem to the Gemfile and run bundle install </p>
<h2>Synopsis</h2>
<p><code>bundle add</code> <i>GEM_NAME</i> [&#8211;group=GROUP] [&#8211;version=VERSION] [&#8211;source=SOURCE] [&#8211;git=GIT] [&#8211;branch=BRANCH] [&#8211;skip-install] [&#8211;strict] [&#8211;optimistic]</p>
<h2>Description</h2>
<p>Adds the named gem to the Gemfile and run <code>bundle install</code>. <code>bundle install</code> can be avoided by using the flag <code>&#8211;skip-install</code>. </p>
<p> Example: </p>
<p> bundle add rails </p>
<p> bundle add rails &#8211;version &quot;&lt; 3.0, &gt; 1.1&quot; </p>
<p> bundle add rails &#8211;version &quot;~&gt; 5.0.0&quot; &#8211;source &quot;<a rel="nofollow" href="https://gems.example.com">https://gems.example.com</a>&quot; &#8211;group &quot;development&quot; </p>
<p> bundle add rails &#8211;skip-install </p>
<p> bundle add rails &#8211;group &quot;development, test&quot;</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd>Specify version requirements(s) for the added gem.</p>
<dt><code>&#8211;group</code>, <code>-g</code></p>
<dd>Specify the group(s) for the added gem. Multiple groups should be separated by commas.</p>
<dt><code>&#8211;source</code>, , <code>-s</code></p>
<dd>Specify the source for the added gem.</p>
<dt><code>&#8211;git</code></p>
<dd>Specify the git source for the added gem.</p>
<dt><code>&#8211;branch</code></p>
<dd>Specify the git branch for the added gem.</p>
<dt><code>&#8211;skip-install</code></p>
<dd>Adds the gem to the Gemfile but does not install it.</p>
<dt><code>&#8211;optimistic</code></p>
<dd>Adds optimistic declaration of version</p>
<dt><code>&#8211;strict</code></p>
<dd>Adds strict declaration of version </p>
</dl>
