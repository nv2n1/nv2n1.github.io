---
title: "npm-cache(1)"
name: "npm-cache"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-cache/"
description: "npm-cache – Manipulates packages cache"
---

<h2 class="name">NAME</h2>
<p> <code>npm-cache</code> &#8211; Manipulates packages cache </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm cache add &lt;tarball file&gt;
npm cache add &lt;folder&gt;
npm cache add &lt;tarball url&gt;
npm cache add &lt;name&gt;@&lt;version&gt;
npm cache clean [&lt;path&gt;]
aliases: npm cache clear, npm cache rm
npm cache verify
</pre>
</dl>
<h3>Description</h3>
<p> Used to add, list, or clean the npm cache folder.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> add: Add the specified package to the local cache. This command is primarily intended to be used internally by npm, but it can provide a way to add data to the local installation cache explicitly.</p>
<dt>&bull;</p>
<dd> clean: Delete all data out of the cache folder.</p>
<dt>&bull;</p>
<dd> verify: Verify the contents of the cache folder, garbage collecting any unneeded data, and verifying the integrity of the cache index and all cached data. </p>
</dl>
</dl>
<h3>Details</h3>
<p> npm stores cache data in an opaque directory within the configured <code>cache</code>, named <code>_cacache</code>. This directory is a <code>cacache</code>-based content-addressable cache that stores all http request data as well as other package-related data. This directory is primarily accessed through <code>pacote</code>, the library responsible for all package fetching as of npm@5. </p>
<p> All data that passes through the cache is fully verified for integrity on both insertion and extraction. Cache corruption will either trigger an error, or signal to <code>pacote</code> that the data must be refetched, which it will do automatically. For this reason, it should never be necessary to clear the cache for any reason other than reclaiming disk space, thus why <code>clean</code> now requires <code>&#8211;force</code> to run. </p>
<p> There is currently no method exposed through npm to inspect or directly manage the contents of this cache. In order to access it, <code>cacache</code> must be used directly. </p>
<p> npm will not remove data by itself: the cache will grow as new packages are installed.</p>
<h3>A note about the cache&#8217;s design</h3>
<p> The npm cache is strictly a cache: it should not be relied upon as a persistent and reliable data store for package data. npm makes no guarantee that a previously-cached piece of data will be available later, and will automatically delete corrupted contents. The primary guarantee that the cache makes is that, if it does return data, that data will be exactly the data that was inserted. </p>
<p> To run an offline verification of existing cache contents, use <code>npm cache verify</code>.</p>
<h3>Configuration</h3>
<h3>cache</h3>
<p> Default: <code>~/.npm</code> on Posix, or <code>%AppData%/npm-cache</code> on Windows. </p>
<p> The root cache folder.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc</p>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help publish</p>
<dt>&bull;</p>
<dd> npm help pack</p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="https://npm.im/cacache">https://npm.im/cacache</a></p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="https://npm.im/pacote">https://npm.im/pacote</a> </p>
</dl>
</dl>
<h2>Index</h2>
