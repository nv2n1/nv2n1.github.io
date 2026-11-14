---
title: "ctl_deliver(8)"
name: "ctl_deliver"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ctl_deliver/"
description: "ctl_deliver – perform operations on the duplicate delivery database"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>ctl_deliver &#8211; perform operations on the duplicate delivery database</p>
<h2>Synopsis</h2>
<p><code>ctl_deliver</code> [ <code>-C</code> <i>config-file</i> ] <code>-d</code> [ <code>-f </code><i>filename</i> ]</p>
<h2>Description</h2>
<p><i>Ctl_deliver</i> is used to perform various administrative operations on the duplicate delivery database. </p>
<p> <i>Ctl_deliver</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-d</code></p>
<dd>Dump the contents of the database to standard output in a portable flat-text format.</p>
<dt><code>-f </code><i>filename</i></p>
<dd>Use the database specified by <i>filename</i> instead of the default (<i>configdirectory</i><code>/deliver.db</code>).</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code> </p>
