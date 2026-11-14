---
title: "cyr_df(8)"
name: "cyr_df"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cyr_df/"
description: "cyr_df – report Cyrus spool partition disk space usage"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>cyr_df &#8211; report Cyrus spool partition disk space usage</p>
<h2>Synopsis</h2>
<p><code>cyr_df</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-m</code> ]</p>
<h2>Description</h2>
<p><i>Cyr_df</i> examines the Cyrus spool partitions and reports on their disk space usage. <i>Cyr_df</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-m</code></p>
<dd>Report on metadata partitions rather than message file partitions.</dl>
<h2>Files</h2>
<p><code>/etc/imapd.conf</code></p>
