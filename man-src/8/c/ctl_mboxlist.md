---
title: "ctl_mboxlist(8)"
name: "ctl_mboxlist"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ctl_mboxlist/"
description: "ctl_mboxlist – perform operations on the mailbox list database"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>ctl_mboxlist &#8211; perform operations on the mailbox list database</p>
<h2>Synopsis</h2>
<p><code>ctl_mboxlist</code> [ <code>-C</code> <i>config-file</i> ] <code>-d</code> [ <code>-x</code> ] [ <code>-p </code><i>partition</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-f </code><i>filename</i> ]<br />
 <code>ctl_mboxlist</code> [ <code>-C</code> <i>config-file</i> ] <code>-u</code> [ <code>-f </code><i>filename</i> ]<br />
 <code>ctl_mboxlist</code> [ <code>-C</code> <i>config-file</i> ] <code>-m</code> [ <code>-a </code> ] [ <code>-w </code> ] [ <code>-i </code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-f </code><i>filename</i> ]<br />
 <code>ctl_mboxlist</code> [ <code>-C</code> <i>config-file</i> ] <code>-v</code> [ <code>-f </code><i>filename</i> ]</p>
<h2>Description</h2>
<p><i>Ctl_mboxlist</i> is used to perform various administrative operations on the mailbox list database. </p>
<p> <i>Ctl_mboxlist</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. The <i>configdirectory</i> option is used to determine the default location of the mailbox list database.</p>
<h2>Options</h2>
<dl>
<dt><code>-C&nbsp;<wbr></code><i>config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-d</code></p>
<dd>Dump the contents of the database to standard output in a portable flat-text format. NOTE: In Cyrus versions 2.2.13 and earlier, the dump format did not include the mailbox type flags, breaking remote mailboxes (frontends, mupdate master, unified backends) when undumped.</p>
<dt><code>-x</code></p>
<dd>When performing a dump, remove the mailboxes dumped from the mailbox list (mostly useful when specified with -p)</p>
<dt><code>-p&nbsp;<wbr></code><i>partition</i></p>
<dd>When performing a dump, dump only thise mailboxes that live on <i>partition</i></p>
<dt><code>-u</code></p>
<dd>Load the contents of the database from standard input. The input MUST be in the format output using the <code>-d</code> option. NOTE: Both the old and new formats can be loaded, but the old format will break remote mailboxes.</p>
<dt><code>-m</code></p>
<dd>For backend servers in the Cyrus Murder, synchronize the local mailbox list file with the MUPDATE server.</p>
<dt><code>-a</code></p>
<dd>When used with -m, assume the local mailboxes file is authoritiative, that is, only change the mupdate server, do not delete any local mailboxes. USE THIS OPTION WITH CARE, as it allows namespace collisions into the murder.</p>
<dt><code>-w</code></p>
<dd>When used with -m, print out what would be done but do not perform the operations.</p>
<dt><code>-i</code></p>
<dd>When used with -m, asks for verification before deleting local mailboxes.</p>
<dt><code>-v</code></p>
<dd>Verify the consistency of the mailbox list database and the spool partition(s). Mailboxes present in the database and not located on a spool partition, and those located on a spool partition (directory containing a valid cyrus.header file) and not present in the database will be reported. Note that this function is very I/O intensive.</p>
<dt><code>-f </code><i>filename</i></p>
<dd>Use the database specified by <i>filename</i> instead of the default (<i>configdirectory</i><code>/mailboxes.db</code>).</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code> </p>
