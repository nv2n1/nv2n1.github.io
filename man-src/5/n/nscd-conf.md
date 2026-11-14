---
title: "nscd-conf(5)"
name: "nscd-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nscd-conf/"
description: "/etc/nscd.conf – name service cache daemon configuration file"
---

<p>/etc/nscd.conf &#8211; name service cache daemon configuration file</p>
<h2>Description</h2>
<p>The file <i>/etc/nscd.conf</i> is read from <code><a href="/docs/linux/man/8-nscd/">nscd</a></code>(8) at startup. Each line specifies either an attribute and a value, or an attribute, service, and a value. Fields are separated either by SPACE or TAB characters. A &#8216;#&#8217; (number sign) indicates the beginning of a comment; following characters, up to the end of the line, are not interpreted by nscd. </p>
<p> Valid services are <i>passwd</i>, <i>group</i>, <i>hosts</i>, <i>services</i> or <i>netgroup</i>. </p>
<p> <code>logfile</code> <i>debug-file-name</i></p>
<dl>
<dd>Specifies name of the file to which debug info should be written.</dl>
<p> <code>debug-level</code> <i>value</i></p>
<dl>
<dd>Sets the desired debug level. The default is 0.</dl>
<p> <code>threads</code> <i>number</i></p>
<dl>
<dd>This is the number of threads that are started to wait for requests. At least five threads will always be created.</dl>
<p> <code>max-threads</code> <i>number</i></p>
<dl>
<dd>Specifies the maximum number of threads. The default is 32.</dl>
<p> <code>server-user</code> <i>user</i></p>
<dl>
<dd>If this option is set, nscd will run as this user and not as root. If a separate cache for every user is used (-S parameter), this option is ignored.</dl>
<p> <code>stat-user</code> <i>user</i></p>
<dl>
<dd>Specifies the user who is allowed to request statistics.</dl>
<p> <code>reload-count</code> unlimited | <i>number</i></p>
<dl>
<dd>Limit on the number of times a cached entry gets reloaded without being used before it gets removed. The default is 5.</dl>
<p> <code>paranoia</code> <i>&lt;yes|no&gt;</i></p>
<dl>
<dd>Enabling paranoia mode causes nscd to restart itself periodically. The default is no.</dl>
<p> <code>restart-interval</code> <i>time</i></p>
<dl>
<dd>Sets the restart interval to <i>time</i> seconds if periodic restart is enabled by enabling <code>paranoia</code> mode. The default is 3600.</dl>
<p> <code>enable-cache</code> <i>service</i> <i>&lt;yes|no&gt;</i></p>
<dl>
<dd>Enables or disables the specified <i>service</i> cache. The default is no.</dl>
<p> <code>positive-time-to-live</code> <i>service</i> <i>value</i></p>
<dl>
<dd>Sets the TTL (time-to-live) for positive entries (successful queries) in the specified cache for <i>service</i>. <i>Value</i> is in seconds. Larger values increase cache hit rates and reduce mean response times, but increase problems with cache coherence.</dl>
<p> <code>negative-time-to-live</code> <i>service</i> <i>value</i></p>
<dl>
<dd>Sets the TTL (time-to-live) for negative entries (unsuccessful queries) in the specified cache for <i>service</i>. <i>Value</i> is in seconds. Can result in significant performance improvements if there are several files owned by UIDs (user IDs) not in system databases (for example untarring the Linux kernel sources as root); should be kept small to reduce cache coherency problems.</dl>
<p> <code>suggested-size</code> <i>service</i> <i>value</i></p>
<dl>
<dd>This is the internal hash table size, <i>value</i> should remain a prime number for optimum efficiency. The default is 211.</dl>
<p> <code>check-files</code> <i>service</i> <i>&lt;yes|no&gt;</i></p>
<dl>
<dd>Enables or disables checking the file belonging to the specified <i>service</i> for changes. The files are <i>/etc/passwd</i>, <i>/etc/group</i>, <i>/etc/hosts</i>, <i>/etc/services</i> and <i>/etc/netgroup</i>. The default is yes.</dl>
<p> <code>persistent</code> <i>service</i> <i>&lt;yes|no&gt;</i></p>
<dl>
<dd>Keep the content of the cache for <i>service</i> over server restarts; useful when <code>paranoia</code> mode is set. The default is no.</dl>
<p> <code>shared</code> <i>service</i> <i>&lt;yes|no&gt;</i></p>
<dl>
<dd>The memory mapping of the nscd databases for <i>service</i> is shared with the clients so that they can directly search in them instead of having to ask the daemon over the socket each time a lookup is performed. The default is no.</dl>
<p> <code>max-db-size</code> <i>service</i> <i>bytes</i></p>
<dl>
<dd>The maximum allowable size, in bytes, of the database files for the <i>service</i>. The default is 33554432.</dl>
<p> <code>auto-propagate</code> <i>service</i> <i>&lt;yes|no&gt;</i></p>
<dl>
<dd>When set to <i>no</i> for <i>passwd</i> or <i>group</i> service, then the <i>.byname</i> requests are not added to <i>passwd.byuid</i> or <i>group.bygid</i> cache. This can help with tables containing multiple records for the same ID. The default is yes. This option is valid only for services <i>passwd</i> and <i>group</i>.</dl>
<h2>Notes</h2>
<p>The default values stated in this manual page originate from the source code of <code><a href="/docs/linux/man/8-nscd/">nscd</a></code>(8) and are used if not overriden in the configuration file. The default values used in the configuration file of your distribution might differ.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nscd/">nscd</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.53 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
