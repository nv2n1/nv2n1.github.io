---
title: "pmdamemcache(1)"
name: "pmdamemcache"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdamemcache/"
description: "pmdamemcache – memcached performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdamemcache</code> &#8211; memcached performance metrics domain agent (PMDA)</p>
<h2>DESCRIPTION</h2>
<p> This <font SIZE="-1">PMDA</font> extracts performance data from memcached, a distributed memory caching daemon commonly used to improve web serving performance. A farm of memcached processes over multiple servers can be utilised by a single web application, increasing the total available object cache size, and decreasing the database load associated with smaller cache sizes. This system is described in detail at <a rel="nofollow" href="http://www.danga.com/memcached.">http://www.danga.com/memcached.</a></p>
<h2>INSTALLATION</h2>
<p> Configure <code>pmdamemcache</code> to extract the values from set of hosts used in the memcache farm. These hosts can be listed in the <tt>$PCP_PMDAS_DIR</tt>/memcache/memcache.conf file, in the format (i.e. Perl array) described at the top of pmdamemcache.pl. A custom refresh rate can also be configured using this mechanism. </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/memcache </p>
<p>#&nbsp;<wbr>[&nbsp;<wbr>edit memcache.conf&nbsp;<wbr>] </p>
<p> Once this is setup, you can access the names and values for the memcache performance metrics by doing the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/memcache </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/memcache </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdamemcache</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/memcache/memcache.conf</code></p>
<dd> optional configuration file listing monitored memcache instances</p>
<dt><code>$PCP_PMDAS_DIR/memcache/Install</code></p>
<dd> installation script for the <code>pmdamemcache</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/memcache/Remove</code></p>
<dd> undo installation script for the <code>pmdamemcache</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/memcache.log</code></p>
<dd> default log file for error messages from <code>pmdamemcache</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). </p>
<h2>Index</h2>
