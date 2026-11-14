---
title: "rlm_ippool_tool(8)"
name: "rlm_ippool_tool"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rlm_ippool_tool/"
description: "rlm_ippool_tool – dump the contents of the FreeRadius ippool database files"
---

<p>rlm_ippool_tool &#8211; dump the contents of the FreeRadius ippool database files</p>
<h2>Synopsis</h2>
<p>If an ipaddress is specified then that address is used to limit the actions or output. <code>rlm_ippool_tool</code> [<code>-a</code>] [<code>-c</code>] [<code>-o</code>] [<code>-v</code>] <i>session-db</i> <i>index-db</i> [<i>ipaddress</i>] Mark the entry nasIP/nasPort as having ipaddress <code>rlm_ippool_tool</code> -n <i>session-db</i> <i>index-db</i> <i>ipaddress</i> <i>nasIP</i> <i>nasPort</i> Update old format database to new. <code>rlm_ippool_tool</code> -u <i>session-db</i> <i>new-session-db</i> </p>
<h2>Description</h2>
<p><code>rlm_ippool_tool</code> dumps the contents of the FreeRADIUS ippool databases for analyses or for removal of active (stuck?) entries. Or with the <code>-n</code> argument adds a usage entry to the FreeRADIUS ippool databases. </p>
<h2>Options</h2>
<dl>
<dt>-a</p>
<dd>Print all active entries.</p>
<dt>-c</p>
<dd>Report number of active entries.</p>
<dt>-r</p>
<dd>Remove active entries.</p>
<dt>-v</p>
<dd>Verbose report of all entries.</p>
<dt>-o</p>
<dd>Assume old database format (nas/port pair, not md5 output).</p>
<dt>-n</p>
<dd>Mark the entry nasIP/nasPort as having ipaddress.</p>
<dt>-u</p>
<dd>Update old format database to new. </p>
</dl>
<h2>Examples</h2>
<pre><code>Given the syntax in the FreeRadius radiusd.conf:



ippool myippool {
    range-start = 192.0.2.0
    range-stop = 192.0.2.255
    [...]
    session-db = ${raddbdir}/ip-pool.db
    ip-index = ${raddbdir}/ip-index.db
}</code></pre>
<p> To see the number of active entries in this pool, use:</p>
<dl>
<dd>
<pre> $ rlm_ippool_tool -c ip-pool.db ip-index.db
 13</pre>
</dl>
<p> To see all active entries in this pool, use:</p>
<dl>
<dd>
<pre> $ rlm_ippool_tool -a ip-pool.db ip-index.db
 192.0.2.5
 192.0.2.82
 192.0.2.244
 192.0.2.57
 192.0.2.120
 192.0.2.27
 [...]</pre>
</dl>
<p> To see all information about the active entries in the use, use:</p>
<dl>
<dd>
<pre> $ rlm_ippool_tool -av ip-pool.db ip-index.db
 NAS:172.16.1.1 port:0x2e8 - ipaddr:192.0.2.5 active:1 cli:0 num:1
 NAS:172.16.1.1 port:0x17c - ipaddr:192.0.2.82 active:1 cli:0 num:1
 NAS:172.16.1.1 port:0x106 - ipaddr:192.0.2.244 active:1 cli:0 num:1
 NAS:172.16.1.1 port:0x157 - ipaddr:192.0.2.57 active:1 cli:0 num:1
 NAS:172.16.1.1 port:0x2d8 - ipaddr:192.0.2.120 active:1 cli:0 num:1
 NAS:172.16.1.1 port:0x162 - ipaddr:192.0.2.27 active:1 cli:0 num:1
 [...]</pre>
</dl>
<p> To see only information of one entry, use:</p>
<dl>
<dd>
<pre> $ rlm_ippool_tool -v ip-pool.db ip-index.db 192.0.2.1
 NAS:172.16.1.1 port:0x90 - ipaddr:192.0.2.1 active:0 cli:0 num:0</pre>
</dl>
<p> To add an IP address usage entry, use:</p>
<dl>
<dd>
<pre> $ rlm_ippool_tool -n ip-pool.db ip-index.db 192.0.0.1 172.16.1.1 0x90
 rlm_ippool_tool: Allocating ip to nas/port: 172.16.1.1/144
 rlm_ippool_tool: num: 1
 rlm_ippool_tool: Allocated ip 192.0.2.1 to client on nas 172.16.1.1,port 144</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-radiusd/">radiusd</a>(8)</p>
<h2>Authors</h2>
<p>Currently part of the FreeRADIUS Project (<a rel="nofollow" href="http://www.freeradius.org)">http://www.freeradius.org)</a> Originally by Edwin Groothuis, edwin [at] mavetju.org (<a rel="nofollow" href="http://www.mavetju.org)">http://www.mavetju.org)</a> </p>
<p> Mailing list details are at <a rel="nofollow" href="http://www.freeradius.org/">http://www.freeradius.org/</a></p>
