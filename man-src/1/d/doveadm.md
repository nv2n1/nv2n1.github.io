---
title: "doveadm(1)"
name: "doveadm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm/"
description: "doveadm – Dovecot’s administration utility"
---

<h2>NAME</h2>
<p> doveadm &#8211; Dovecot&#8217;s administration utility</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <i>command</i> [<i>command_options</i>] [<i>command_arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>doveadm</code> is the Dovecot administration tool. It can be used to manage various parts of Dovecot, as well as access users&#8217; mailboxes.<br />
 Execute <code>doveadm help</code>, for a command usage listing.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-f&nbsp;<wbr></code><i>formatter</i></p>
<dd> Specifies the <i>formatter</i> for formatting the output. Supported formatters are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>flow</code></p>
<dd> prints each line with <i>key</i><code>=</code><i>value</i> pairs.</p>
<dt><code>pager</code></p>
<dd> prints each <i>key</i>:&nbsp;<wbr><i>value</i> pair on its own line and separates records with form feed character (<code>^L</code>).</p>
<dt><code>tab</code></p>
<dd> prints a table header followed by tab separated value lines.</p>
<dt><code>table</code></p>
<dd> prints a table header followed by adjusted value lines.</dl>
</dl>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<h2>COMMANDS</h2>
<p> These commands work directly with Dovecot&#8217;s master process.</p>
<h3>reload</h3>
<p> <code>doveadm reload</code> </p>
<p> Force <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1) to reload the configuration.</p>
<h3>stop</h3>
<p> <code>doveadm stop</code> </p>
<p> Stop <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1) and all its child processes.</p>
<h3>ADDITIONAL MASTER COMMANDS</h3>
<dl>
<dt><code>doveadm director</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-director/">doveadm-director</a></code>(1), Manage Dovecot directors (if used by proxy servers).</p>
<dt><code>doveadm exec</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-exec/">doveadm-exec</a></code>(1), Easily execute commands from Dovecot&#8217;s libexec_dir.</p>
<dt><code>doveadm instance</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-instance/">doveadm-instance</a></code>(1), Manage the list of running Dovecot instances.</p>
<dt><code>doveadm kick</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-kick/">doveadm-kick</a></code>(1), Disconnect users by user name and/or IP address.</p>
<dt><code>doveadm log</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-log/">doveadm-log</a></code>(1), Locate, test or reopen Dovecot&#8217;s log files.</p>
<dt><code>doveadm mount</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-mount/">doveadm-mount</a></code>(1), Manage the list of mountpoints where mails are stored.</p>
<dt><code>doveadm penalty</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-penalty/">doveadm-penalty</a></code>(1), Show current penalties.</p>
<dt><code>doveadm who</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-who/">doveadm-who</a></code>(1); Show who is logged in to the Dovecot server.</dl>
<h3>AUTHENTICATION COMMANDS</h3>
<dl>
<dt><code>doveadm auth</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-auth/">doveadm-auth</a></code>(1), Test authentication for a user.</p>
<dt><code>doveadm pw</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-pw/">doveadm-pw</a></code>(1), Dovecot&#8217;s password hash generator.</p>
<dt><code>doveadm user</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-user/">doveadm-user</a></code>(1), Perform a user lookup in Dovecot&#8217;s userdbs</dl>
<h3>MAILBOX COMMANDS</h3>
<dl>
<dt><code>doveadm altmove</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-altmove/">doveadm-altmove</a></code>(1), Move matching mails to the alternative storage.</p>
<dt><code>doveadm batch</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-batch/">doveadm-batch</a></code>(1), Execute multiple commands for multiple users.</p>
<dt><code>doveadm copy</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-copy/">doveadm-copy</a></code>(1), Copy messages matching the given search query into another mailbox.</p>
<dt><code>doveadm deduplicate</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-deduplicate/">doveadm-deduplicate</a></code>(1), Expunge duplicate messages.</p>
<dt><code>doveadm dump</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-dump/">doveadm-dump</a></code>(1), Dump the content of Dovecot&#8217;s binary mailbox index/log.</p>
<dt><code>doveadm expunge</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-expunge/">doveadm-expunge</a></code>(1), Expunge messages matching given search query.</p>
<dt><code>doveadm fetch</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-fetch/">doveadm-fetch</a></code>(1), Fetch messages matching given search query.</p>
<dt><code>doveadm flags</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-flags/">doveadm-flags</a></code>(1), Add, remove or replace messages&#8217; flags.</p>
<dt><code>doveadm force-resync</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-force-resync/">doveadm-force-resync</a></code>(1), Repair broken mailboxes, in case Dovecot doesn&#8217;t automatically do that.</p>
<dt><code>doveadm import</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-import/">doveadm-import</a></code>(1), Import messages matching given search query.</p>
<dt><code>doveadm index</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-index/">doveadm-index</a></code>(1), Index messages in a given mailbox.</p>
<dt><code>doveadm mailbox</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-mailbox/">doveadm-mailbox</a></code>(1), Various commands related to handling mailboxes.</p>
<dt><code>doveadm move</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-move/">doveadm-move</a></code>(1) Move messages matching the given search query into another mailbox.</p>
<dt><code>doveadm purge</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-purge/">doveadm-purge</a></code>(1) Remove messages with refcount=0 from mdbox files.</p>
<dt><code>doveadm quota</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-quota/">doveadm-quota</a></code>(1), Initialize/recalculate or show current quota usage.</p>
<dt><code>doveadm search</code></p>
<dd> <code><a href="/docs/linux/man/1-doveadm-search/">doveadm-search</a></code>(1), Show a list of mailbox GUIDs and message UIDs matching given search query.</dl>
<h2>EXIT STATUS</h2>
<p> <code>doveadm</code> will exit with one of the following values:</p>
<dl>
<dt><code>0</code></p>
<dd> Selected command was executed successful.</p>
<dt><code>&gt;0</code></p>
<dd> Command failed in some way.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>USER</code></p>
<dd> This environment variable is used to determine the <i>user</i> if a command accepts a <i>user</i> but none was specified.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/dovecot.conf</i></p>
<dd> Dovecot&#8217;s main configuration file.</p>
<dt><i>/etc/dovecot/conf.d/10-mail.conf</i></p>
<dd> Mailbox locations and namespaces.</p>
<dt><i>/etc/dovecot/conf.d/90-plugin.conf</i></p>
<dd> Plugin specific settings.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm-help/">doveadm-help</a></code>(1), <code><a href="/docs/linux/man/1-doveconf/">doveconf</a></code>(1), <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1), <code><a href="/docs/linux/man/1-dsync/">dsync</a></code>(1), <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) </p>
<h2>Index</h2>
