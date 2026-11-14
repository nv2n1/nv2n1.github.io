---
title: "nscd(8)"
name: "nscd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nscd/"
description: "nscd – name service cache daemon"
---

<p>nscd &#8211; name service cache daemon</p>
<h2>Description</h2>
<p>Nscd is a daemon that provides a cache for the most common name service requests. The default configuration file, <i>/etc/nscd.conf</i>, determines the behavior of the cache daemon. See <code><a href="/docs/linux/man/5-nscd-conf/">nscd.conf</a></code>(5). </p>
<p> Nscd provides caching for accesses of the <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-group/">group</a></code>(5), and <code><a href="/docs/linux/man/5-hosts/">hosts</a></code>(5) databases through standard libc interfaces, such as <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3), <code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a></code>(3), <code><a href="/docs/linux/man/3-getgrgid/">getgrgid</a></code>(3), <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), and others. </p>
<p> There are two caches for each database: a positive one for items found, and a negative one for items not found. Each cache has a separate TTL (time-to-live) period for its data. Note that the shadow file is specifically not cached. <code><a href="/docs/linux/man/3-getspnam/">getspnam</a></code>(3) calls remain uncached as a result.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>will give you a list with all options and what they do.</dl>
<h2>Notes</h2>
<p>The daemon will try to watch for changes in configuration files appropriate for each database (e.g., <i>/etc/passwd</i> for the <i>passwd</i> database or <i>/etc/hosts</i> and <i>/etc/resolv.conf</i> for the <i>hosts</i> database), and flush the cache when these are changed. However, this will happen only after a short delay (unless the <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) mechanism is available and glibc 2.9 or later is available), and this auto-detection does not cover configuration files required by nonstandard NSS modules, if any are specified in <i>/etc/nsswitch.conf</i>. In that case, you need to run the following command after changing the configuration file of the database so that <code>nscd</code> invalidates its cache: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr><code>nscd -i</code>&nbsp;<wbr><i>&lt;database&gt;</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nscd-conf/">nscd.conf</a></code>(5), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.53 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
