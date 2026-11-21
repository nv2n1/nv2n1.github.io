---
title: "memcached-tool(1)"
name: "memcached-tool"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memcached-tool/"
description: "memcached-tool – stats and management tool for memcached"
---

<h2>NAME</h2>
<p> memcached-tool &#8211; stats and management tool for memcached </p>
<h2>SYNOPSIS</h2>
<p> <code>memcached-tool</code> &lt;<i>host</i>[:<i>port</i>] | <i>/path/to/socket</i>&gt; [<i>mode</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>memcached-tool</code> is a Perl script used to print statistics from a running memcached instance. The first parameter specifies the address of the daemon either by a hostname, optionally followed by the port number (the default is 11211), or a path to UNIX domain socket. The second parameter specifies the mode in which the tool should run. </p>
<h2>MODES</h2>
<dl>
<dt><code>display</code></dt>
<dd> Print slab class statistics. This is the default mode if no mode is specified. The printed columns are:</dd>
<dl>
<dl>
<dt><code>#</code></dt>
<dd> Number of the slab class.</dd>
<dt><code>Item_Size</code></dt>
<dd> The amount of space each chunk uses. One item uses one chunk of the appropriate size.</dd>
<dt><code>Max_age</code></dt>
<dd> Age of the oldest item in the LRU.</dd>
<dt><code>Pages</code></dt>
<dd> Total number of pages allocated to the slab class.</dd>
<dt><code>Count</code></dt>
<dd> Number of items presently stored in this class. Expired items are not automatically excluded.</dd>
<dt><code>Full?</code></dt>
<dd> Yes if there are no free chunks at the end of the last allocated page.</dd>
<dt><code>Evicted</code></dt>
<dd> Number of times an item had to be evicted from the LRU before it expired.</dd>
<dt><code>Evict_Time</code></dt>
<dd> Seconds since the last access for the most recent item evicted from this class.</dd>
<dt><code>OOM</code></dt>
<dd> Number of times the underlying slab class was unable to store a new item.</dd></dl>
</dl>
<dt><code>stats</code></dt>
<dd> Print general-purpose statistics of the daemon. Each line contains the name of the statistic and its value.</dd>
<dt><code>dump</code></dt>
<dd> Make a partial dump of the cache written in the add statements of the memcached protocol. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-memcached/">memcached</a></code>(1),<br />
 <code><a rel="nofollow" href="http://www.memcached.org">http://www.memcached.org</a></code> </p>
<h2>AUTHOR</h2>
<p> The memcached-tool script was written by Brad Fitzpatrick <code>&lt;brad [at] danga.com&gt;</code> </p>
