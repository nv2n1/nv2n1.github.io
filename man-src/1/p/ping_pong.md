---
title: "ping_pong(1)"
name: "ping_pong"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ping_pong/"
description: "ping_pong – measures the ping-pong byte range lock latency"
---

<h2 class="name">NAME</h2>
<p> ping_pong &#8211; measures the ping-pong byte range lock latency </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ping_pong</code> {-r | -w | -rw} [-m] [-c] {<i>FILENAME</i>} {<i>NUM-LOCKS</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>ping_pong measures the byte range lock latency. It is especially useful on a cluster of nodes sharing a common lock manager as it will give some indication of the lock manager&#8217;s performance under stress. </p>
<p> FILENAME is a file on shared storage to use for byte range locking tests. </p>
<p> NUM-LOCKS is the number of byte range locks, so needs to be (strictly) greater than the number of nodes in the cluster.</p>
<h2>OPTIONS</h2>
<p> -r</p>
<dl>
<dt>
<dd> test read performance</dl>
<p> -w</p>
<dl>
<dt>
<dd> test write performance</dl>
<p> -m</p>
<dl>
<dt>
<dd> use mmap</dl>
<p> -c</p>
<dl>
<dt>
<dd> validate the locks</dl>
<h2>EXAMPLES</h2>
<p> Testing lock coherence </p>
<dl>
<dt>
<dd>
<pre>
      ping_pong test.dat N
    
</pre>
</dl>
<p> Testing lock coherence with lock validation </p>
<dl>
<dt>
<dd>
<pre>
      ping_pong -c test.dat N
    
</pre>
</dl>
<p> Testing IO coherence </p>
<dl>
<dt>
<dd>
<pre>
      ping_pong -rw test.dat N
    
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7), m[blue]<code><a rel="nofollow" href="https://wiki.samba.org/index.php/Ping_pong">https://wiki.samba.org/index.php/Ping_pong</a></code>m[]</p>
<h2>AUTHOR</h2>
<p> This documentation was written by Mathieu Parent</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002 Andrew Tridgell </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[]. </p>
<h2>Index</h2>
