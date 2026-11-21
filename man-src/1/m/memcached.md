---
title: "memcached(1)"
name: "memcached"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memcached/"
description: "memcached – high-performance memory object caching system"
---

<h2>NAME</h2>
<p> memcached &#8211; high-performance memory object caching system</p>
<h2>SYNOPSIS</h2>
<p> <code>memcached</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>memcached</code> memory object caching daemon. </p>
<p> <code>memcached</code> is a flexible memory object caching daemon designed to alleviate database load in dynamic web applications by storing objects in memory. It&#8217;s based on libevent to scale to any size needed, and is specifically optimized to avoid swapping and always use non-blocking I/O. </p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax. A summary of options is included below.</p>
<dl>
<dt><code>-s &lt;file&gt;</code></dt>
<dd> Unix socket path to listen on (disables network support).</dd>
<dt><code>-A</code></dt>
<dd> Enable ascii &quot;shutdown&quot; command.</dd>
<dt><code>-a &lt;perms&gt;</code></dt>
<dd> Permissions (in octal format) for Unix socket created with -s option.</dd>
<dt><code>-l &lt;addr&gt;</code></dt>
<dd> Listen on &lt;addr&gt;; default to INADDR_ANY. &lt;addr&gt; may be specified as host:port. If you don&#8217;t specify a port number, the value you specified with -p or -U is used. You may specify multiple addresses separated by comma or by using -l multiple times. This is an important option to consider as there is no other way to secure the installation. Binding to an internal or firewalled network interface is suggested.</dd>
<dt><code>-d</code></dt>
<dd> Run memcached as a daemon.</dd>
<dt><code>-u &lt;username&gt;</code></dt>
<dd> Assume the identity of &lt;username&gt; (only when run as root).</dd>
<dt><code>-m &lt;num&gt;</code></dt>
<dd> Use &lt;num&gt; MB memory max to use for object storage; the default is 64 megabytes.</dd>
<dt><code>-c &lt;num&gt;</code></dt>
<dd> Use &lt;num&gt; max simultaneous connections; the default is 1024.</dd>
<dt><code>-R &lt;num&gt;</code></dt>
<dd> This option seeks to prevent client starvation by setting a limit to the number of sequential requests the server will process from an individual client connection. Once a connection has exceeded this value, the server will attempt to process I/O on other connections before handling any further request from this connection. The default value for this option is 20.</dd>
<dt><code>-k</code></dt>
<dd> Lock down all paged memory. This is a somewhat dangerous option with large caches, so consult the README and memcached homepage for configuration suggestions.</dd>
<dt><code>-p &lt;num&gt;</code></dt>
<dd> Listen on TCP port &lt;num&gt;, the default is port 11211.</dd>
<dt><code>-U &lt;num&gt;</code></dt>
<dd> Listen on UDP port &lt;num&gt;, the default is port 11211, 0 is off.</dd>
<dt><code>-M</code></dt>
<dd> Disable automatic removal of items from the cache when out of memory. Additions will not be possible until adequate space is freed up.</dd>
<dt><code>-r</code></dt>
<dd> Raise the core file size limit to the maximum allowable.</dd>
<dt><code>-f &lt;factor&gt;</code></dt>
<dd> Use &lt;factor&gt; as the multiplier for computing the sizes of memory chunks that items are stored in. A lower value may result in less wasted memory depending on the total amount of memory available and the distribution of item sizes. The default is 1.25.</dd>
<dt><code>-n &lt;size&gt;</code></dt>
<dd> Allocate a minimum of &lt;size&gt; bytes for the item key, value, and flags. The default is 48. If you have a lot of small keys and values, you can get a significant memory efficiency gain with a lower value. If you use a high chunk growth factor (-f option), on the other hand, you may want to increase the size to allow a bigger percentage of your items to fit in the most densely packed (smallest) chunks.</dd>
<dt><code>-C</code></dt>
<dd> Disable the use of CAS (and reduce the per-item size by 8 bytes).</dd>
<dt><code>-h</code></dt>
<dd> Show the version of memcached and a summary of options.</dd>
<dt><code>-v</code></dt>
<dd> Be verbose during the event loop; print out errors and warnings.</dd>
<dt><code>-vv</code></dt>
<dd> Be even more verbose; same as -v but also print client commands and responses.</dd>
<dt><code>-vvv</code></dt>
<dd> Be extremely verbose; same of the above and also print internal state transitions.</dd>
<dt><code>-i</code></dt>
<dd> Print memcached and libevent licenses.</dd>
<dt><code>-P &lt;filename&gt;</code></dt>
<dd> Print pidfile to &lt;filename&gt;, only used under -d option.</dd>
<dt><code>-t &lt;threads&gt;</code></dt>
<dd> Number of threads to use to process incoming requests. This option is only meaningful if memcached was compiled with thread support enabled. It is typically not useful to set this higher than the number of CPU cores on the memcached server. Setting a high number (64 or more) of worker threads is not recommended. The default is 4.</dd>
<dt><code>-D &lt;char&gt;</code></dt>
<dd> Use &lt;char&gt; as the delimiter between key prefixes and IDs. This is used for per-prefix stats reporting. The default is &quot;:&quot; (colon). If this option is specified, stats collection is turned on automatically; if not, then it may be turned on by sending the &quot;stats detail on&quot; command to the server.</dd>
<dt><code>-L</code></dt>
<dd> Try to use large memory pages (if available). Increasing the memory page size could reduce the number of TLB misses and improve the performance. In order to get large pages from the OS, memcached will allocate the total item-cache in one large chunk. Only available if supported on your OS.</dd>
<dt><code>-b &lt;num&gt;</code></dt>
<dd> Set the backlog queue limit to &lt;num&gt; connections. The default is 1024.</dd>
<dt><code>-B &lt;proto&gt;</code></dt>
<dd> Specify the binding protocol to use. By default, the server will autonegotiate client connections. By using this option, you can specify the protocol clients must speak. Possible options are &quot;auto&quot; (the default, autonegotiation behavior), &quot;ascii&quot; and &quot;binary&quot;.</dd>
<dt><code>-I &lt;size&gt;</code></dt>
<dd> Override the default size of each slab page. The default size is 1mb. Default value for this parameter is 1m, minimum is 1k, max is 128m. Adjusting this value changes the item size limit. Beware that this also increases the number of slabs (use -v to view), and the overal memory usage of memcached.</dd>
<dt><code>-S</code></dt>
<dd> Turn on SASL authentication. This option is only meaningful if memcached was compiled with SASL support enabled.</dd>
<dt><code>-F</code></dt>
<dd> Disables the &quot;flush_all&quot; command. The cmd_flush counter will increment, but clients will receive an error message and the flush will not occur.</dd>
<dt><code>-o &lt;options&gt;</code></dt>
<dd> Comma separated list of extended or experimental options. See -h or wiki for up to date list.</dd>
<dt><code>-V</code></dt>
<dd> print version and exit
</dd></dl>
<h2>LICENSE</h2>
<p> The memcached daemon is copyright Danga Interactive and is distributed under the BSD license. Note that daemon clients are licensed separately. </p>
<h2>SEE ALSO</h2>
<p> The README file that comes with memcached<br />
 <code><a rel="nofollow" href="http://www.memcached.org">http://www.memcached.org</a></code></p>
<h2>AUTHOR</h2>
<p> The memcached daemon was written by Anatoly Vorobey <code>&lt;mellon [at] pobox.com&gt;</code> and Brad Fitzpatrick <code>&lt;brad [at] danga.com&gt;</code> and the rest of the crew of Danga Interactive <code><a rel="nofollow" href="http://www.danga.com">http://www.danga.com</a></code> </p>
