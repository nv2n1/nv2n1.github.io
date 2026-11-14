---
title: "reconstruct(8)"
name: "reconstruct"
section: "8"
letter: "r"
url: "/docs/linux/man/8-reconstruct/"
description: "reconstruct – reconstruct mailboxes"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>reconstruct &#8211; reconstruct mailboxes</p>
<h2>Synopsis</h2>
<p><code>reconstruct</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-p</code> <i>partition</i> ] [ <code>-x</code> ] [ <code>-r</code> ] [ <code>-f</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-k </code> ] [ <code>-s</code> ] [ <code>-g</code> ] [ <code>-G</code> ] [ <code>-R</code> ] [ <code>-o</code> ] [ <code>-O</code> ] <i>mailbox</i>&#8230; </p>
<p> <code>reconstruct</code> [ <code>-C</code> <i>config-file</i> ] <code>-m</code></p>
<h2>Description</h2>
<p><i>Reconstruct</i> rebuilds one or more IMAP mailboxes. When invoked with the <code>-m</code> switch, it rebuilds the master mailboxes file. It can be used to recover from almost any sort of data corruption. </p>
<p> If <i>Reconstruct</i> can find existing header and index files, it attempts to preserve any data in them that is not derivable from the message files themselves. The state <i>reconstruct</i> attempts to preserve includes the flag names, flag state, and internaldate. <i>Reconstruct</i> derives all other information from the message files. </p>
<p> <i>Reconstruct</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. Any mailbox directory underneath the path specified in the <i>partition-news</i> configuration option is assumed to be in news format. </p>
<p> <i>Reconstruct</i> does not adjust the quota usage recorded in any quota root files. After running <i>reconstruct</i>, it is advisable to run <i><a href="/docs/linux/man/8-quota/">quota</a></i>(8) with the <i>-f</i> switch in order to fix the quota root files.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-p</code><i> partition</i></p>
<dd>Search for the listed (non-existant) mailboxes on the indicated partition. Create the mailboxes in the database in addition to reconstructing them. (not compatible with the use of wildcards)</p>
<dt><code>-x</code></p>
<dd>When processing a mailbox which is not in the mailbox list (e.g. via the -p or -f options), do not import the metadata from the mailbox, instead create it anew (this specifically affects at least the mailbox&#8217;s seen state unique identifier, user flags, and ACL).</p>
<dt><code>-r</code></p>
<dd>Recursively reconstruct all sub-mailboxes of the mailboxes or mailbox prefixes given as arguments.</p>
<dt><code>-f</code></p>
<dd>Examine the filesystem underneath mailbox, adding all directories with a cyrus.header found there as new mailboxes. Useful for restoring mailboxes from backups.</p>
<dt><code>-s</code></p>
<dd>Don&#8217;t stat underlying files. This makes reconstruct run faster, at the expense of not noticing some issues (like zero byte files or size mistmatches). &quot;reconstruct -s&quot; should be quite fast.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t make any changes. This gives equivalent behaviour to <i>chk_cyrus</i> where problems are reported, but not fixed.</p>
<dt><code>-G</code></p>
<dd>Force re-parsing of the underlying message (checks GUID correctness). Reconstruct with -G should fix all possible individual message issues, including corrupted data files.</p>
<dt><code>-R</code></p>
<dd>Perform a UID upgrade operation on GUID mismatch files. Use this option if you think your index is corrupted rather than your message files, or if all backup attempts have failed and you&#8217;re happy to be served the missing files.</p>
<dt><code>-U</code></p>
<dd>Use this option if you have corrupt message files in your spool and have been unable to restore them from backup. This will make the mailbox IOERROR free and fix replication. <code>WARNING</code> this deletes corrupt message files for ever &#8211; so make sure you&#8217;ve exhausted other options first!</p>
<dt><code>-o</code></p>
<dd>Ignore odd files in your mailbox disk directories. Probably useful if you are using some tool which adds additional tracking files.</p>
<dt><code>-O</code></p>
<dd>Delete odd files. This is the opposite of &#8216;-o&#8217;.</p>
<dt><code>-m</code></p>
<dd><code>NOTE: CURRENTLY UNAVAILABLE</code><br />
 Rebuild the <i>mailboxes</i> file. Use whatever data in the existing <i>mailboxes</i> file it can scavenge, then scans all partitions listed in the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file for additional mailboxes.</dl>
<h2>Examples</h2>
<p>You want to reconstruct the index files for a user, you have recovered a deleted mail file from backup and given it a suitable name (eg user/ben-lacy/33.), but it is not visible since it is not indexed: </p>
<pre>reconstruct -r user.ben-lacy</pre>
<p>If you have the <code>unixhierarchysep:yes</code> option set in <code>/etc/imapd.conf</code> you would need to run: </p>
<pre>reconstruct -r user/ben.lacy</pre>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
