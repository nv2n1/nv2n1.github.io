---
title: "cachefilesd(8)"
name: "cachefilesd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cachefilesd/"
description: "cachefilesd – CacheFiles userspace management daemon"
---

<p>cachefilesd &#8211; CacheFiles userspace management daemon</p>
<h2>Synopsis</h2>
<p><code>cachefilesd [-d]* [-s] [-n] [-N] [-f &lt;configfile&gt;]</code></p>
<h2>Description</h2>
<p>The <code>cachefilesd</code> daemon manages the cache data store that is used by network filesystems such a AFS and NFS to cache data locally on disk. </p>
<p> The README file should be read before attempting to configure this facility:</p>
<dl>
<dd>/usr/share/doc/cachefilesd/README</dl>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Turn on debugging mode (message written to stderr).</p>
<dt><code>-s</code></p>
<dd>Don&#8217;t use syslog.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t daemonise.</p>
<dt><code>-N</code></p>
<dd>Disable culling and scanning to fill the cull table.</p>
<dt><code>-p &lt;pidfile&gt;</code></p>
<dd>Use an alternate PID file to /var/run/cachefilesd.pid.</p>
<dt><code>-f &lt;configfile&gt;</code></p>
<dd>Read the alternate configuration files.</dl>
<h2>Files</h2>
<p><code>/etc/cachefilesd.conf</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-cachefilesd-conf/">cachefilesd.conf</a></code>(5), /usr/share/doc/cachefilesd/README</p>
<h2>Authors</h2>
<p>David Howells &lt;dhowells [at] redhat.com&gt;</p>
