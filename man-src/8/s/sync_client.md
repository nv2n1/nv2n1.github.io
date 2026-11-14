---
title: "sync_client(8)"
name: "sync_client"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sync_client/"
description: "sync_client – client side of the synchronization (replication) engine"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>sync_client &#8211; client side of the synchronization (replication) engine</p>
<h2>Synopsis</h2>
<p><code>sync_client</code> [ <code>-v</code> ] [ <code>-l</code> ] [ <code>-z</code> ] [ <code>-C</code> <i>config-file</i> ] [ <code>-S</code> <i>servername</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-f</code> <i>input-file</i> ] [ <code>-F</code> <i>shutdown_file</i> ] [ <code>-w</code> <i>wait_interval</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-t</code> <i>timeout</i> ] [ <code>-d</code> <i>delay</i> ] [ <code>-r</code> ] [ <code>-u</code> ] [ <code>-m</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-s</code> ] <i>objects</i>&#8230; </p>
<h2>Description</h2>
<p><i>Sync_client</i> is the client side of the replication system. It runs on the client (master) system and connects to the target (replica) system and generates an appropriate sequence of transactions to synchronize the replica system with the master system.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code></p>
<dd>Verbose mode.</p>
<dt><code>-l</code></p>
<dd>Verbose logging mode.</p>
<dt><code>-o</code></p>
<dd>Only attempt to connect to the backend server once rather than waiting up to 1000 seconds before giving up.</p>
<dt><code>-z</code></p>
<dd>Enable compress. If you set &#8216;sync_compress&#8217; in the imapd.conf or pass -z to sync_client, the replication protocol will attempt to enable deflate compression on the connection.</p>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-S</code><i> servername</i></p>
<dd>Tells <code>sync_client</code> which server to communicate with. Overrides the <i>sync_host</i> configuration option.</p>
<dt><code>-f</code><i> input-file</i></p>
<dd>In mailbox or user replication mode: provides list of users or mailboxes to replicate. In rolling replication mode, specifies an alternate log file (sync_client will exit after processing the log file).</p>
<dt><code>-F</code><i> shutdown-file</i></p>
<dd>Rolling replication checks for this file at the end of each replication cycle and shuts down if it is present. Used to request nice clean shutdown at first convenient point. The file in question is removed on shutdown. Overrides <i>sync_shutdown_file</i> option in <i>imapd.conf</i></p>
<dt><code>-w</code><i> interval</i></p>
<dd>Wait this long before starting. Typically used so that we can attach a debugger to one end of the replication system or the other.</p>
<dt><code>-t</code><i> timeout</i></p>
<dd>Timeout for single replication run in rolling replication. <code>sync_client</code> will negotiate a restart after this many seconds. Default: 600 seconds</p>
<dt><code>-d</code><i> delay</i></p>
<dd>Minimum delay between replication runs in rolling replication mode. Larger values provide better efficiency as transactions can be merged. Smaller values mean that the replica system is more up to date and that you don&#8217;t end up with large blocks of replication transactions as a single group. Default: 3 seconds.</p>
<dt><code>-r</code></p>
<dd>Rolling (repeat) replication mode. Pick up a list of actions recorded by the <code><a href="/docs/linux/man/8-lmtpd/">lmtpd</a>(8), <a href="/docs/linux/man/8-imapd/">imapd</a>(8), <a href="/docs/linux/man/8-popd/">popd</a>(8) and <a href="/docs/linux/man/8-nntpd/">nntpd</a>(8)</code> daemons from the file specified in <i>sync_log_file.</i> Repeat until <i>sync_shutdwon_file</i> appears.</p>
<dt><code>-n</code></p>
<dd>Use the named channel for rolling replication mode. If multiple channels are specified in <i>sync_log_channels</i> then use one of them. This option is probably best combined with -S to connect to a different server with each channel.</p>
<dt><code>-u</code></p>
<dd>User mode. Remaining arguments are list of users who should be replicated.</p>
<dt><code>-m</code></p>
<dd>Mailbox mode. Remaining arguments are list of mailboxes which should be replicated.</p>
<dt><code>-s</code></p>
<dd>Sieve mode. Remaining arguments are list of users whose Sieve files should be replicated. Principally used for debugging purposes: not exposed to <code><a href="/docs/linux/man/8-sync_client/">sync_client</a>(8).</code></dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sync_server/">sync_server</a>(8)</code></p>
<h2>Authors</h2>
<p>David Carter (dpc22 [at] cam.ac.uk), Ken Murchison (ken [at] oceana.com)</p>
