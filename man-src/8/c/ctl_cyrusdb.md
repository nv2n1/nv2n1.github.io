---
title: "ctl_cyrusdb(8)"
name: "ctl_cyrusdb"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ctl_cyrusdb/"
description: "ctl_cyrusdb – perform operations common to all Cyrus databases"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>ctl_cyrusdb &#8211; perform operations common to all Cyrus databases</p>
<h2>Synopsis</h2>
<p><code>ctl_cyrusdb</code> [ <code>-C</code> <i>config-file</i> ] <code>-r</code> [ <code>-x</code> ]<br />
 <code>ctl_cyrusdb</code> [ <code>-C</code> <i>config-file</i> ] <code>-c</code></p>
<h2>Description</h2>
<p><i>Ctl_cyrusdb</i> is used to perform various administrative operations on the Cyrus databases. </p>
<p> <i>Ctl_cyrusdb</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. The <i>configdirectory</i> option is used to determine the default location of the Cyrus databases.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-r</code></p>
<dd>Recover the databases after an application or system failure. Also performs database cleanup like removing mailbox reservations (and any associated mailbox files). </p>
<p> All mailbox files are also checked to make sure the file format matches the configured database type in imapd.conf. If not, the file is automatically converted using the same logic as cvt_cyrusdb.</p>
<dt><code>-x</code></p>
<dd>Used with -r to recover the database only. (Prevents database cleanup).</p>
<dt><code>-c</code></p>
<dd>Checkpoint and archive the databases. Changes to the database which are part of committed transactions are written to disk. Also, a <i>hot</i> backup of the databases is made and inactive log files are removed.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code> </p>
