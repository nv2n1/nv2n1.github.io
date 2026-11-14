---
title: "pmdazswap(1)"
name: "pmdazswap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdazswap/"
description: "pmdazswap – zswap (compressed swap) PMDA"
---

<h2>NAME</h2>
<p> <code>pmdazswap</code> &#8211; zswap (compressed swap) PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdazswap</code> is a Performance Metrics Domain Agent (PMDA) which exports metric values about compressed swap operation, as tracked by the <code>zswap</code> Linux kernel module. </p>
<p> Zswap is a lightweight compressed cache for swap pages. It takes pages that are in the process of being swapped out and attempts to compress them into a dynamically allocated RAM-based memory pool. Zswap trades CPU cycles for potentially reduced swap I/O. This tradeoff can also result in a performance improvement if reads from the compressed cache are faster than reads from a swap device. </p>
<p> This PMDA exports metrics about pool size, number of pages stored, and various counters for the reasons pages are rejected.</p>
<h2>INSTALLATION</h2>
<p> Install the zswap PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/zswap </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/zswap </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdazswap</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/zswap/Install</code></p>
<dd> installation script for the <code>pmdazswap</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/zswap/Remove</code></p>
<dd> undo installation script for the <code>pmdazswap</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/zswap.log</code></p>
<dd> default log file for error messages from <code>pmdazswap</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<h2>Index</h2>
