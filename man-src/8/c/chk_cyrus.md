---
title: "chk_cyrus(8)"
name: "chk_cyrus"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chk_cyrus/"
description: "chk_cyrus – perform a consistency check of the cyrus mailstore"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>chk_cyrus &#8211; perform a consistency check of the cyrus mailstore</p>
<h2>Synopsis</h2>
<p><code>chk_cyrus</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-P</code> <i>partition</i> ] [ <code>-M</code> <i>mailbox</i> ]</p>
<h2>Description</h2>
<p><i>Chk_cyrus</i> is used to perform a consistency check on the cyrus datastore, and output a list of files/directories that are expected to exist, but do not. Status messagess are output to stderr, the list of files/directories is output to stdout. This list can be passed to a backup program to aid a partial restoral, for instance. </p>
<p> <i>Chk_cyrus</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-P</code><i> partition</i></p>
<dd>Run the consistency check for only the given partition. May not be specified with -M. <code>-M</code><i> mailbox</i> Run the consistency check for only the given mailbox. May not be specified with -P.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code> </p>
