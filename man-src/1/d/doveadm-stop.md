---
title: "doveadm-stop(1)"
name: "doveadm-stop"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-stop/"
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
<dt><code>-D</code></dt>
<dd> Enables verbosity and debug messages.</dd>
<dt><code>-f&nbsp;<wbr></code><i>formatter</i></dt>
<dd> Specifies the <i>formatter</i> for formatting the output. Supported formatters are:</dd>
<dl>
<dl>
<dt><code>flow</code></dt>
<dd> prints each line with <i>key</i><code>=</code><i>value</i> pairs.</dd>
<dt><code>pager</code></dt>
<dd> prints each <i>key</i>:&nbsp;<wbr><i>value</i> pair on its own line and separates records with form feed character (<code>^L</code>).</dd>
<dt><code>tab</code></dt>
<dd> prints a table header followed by tab separated value lines.</dd>
<dt><code>table</code></dt>
<dd> prints a table header followed by adjusted value lines.</dd></dl>
</dl>
<dt><code>-v</code></dt>
<dd> Enables verbosity, including progress counter.</dd></dl>
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
<dt><code>doveadm director</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-director/">doveadm-director</a></code>(1), Manage Dovecot directors (if used by proxy servers).</dd>
<dt><code>doveadm exec</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-exec/">doveadm-exec</a></code>(1), Easily execute commands from Dovecot&#8217;s libexec_dir.</dd>
<dt><code>doveadm instance</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-instance/">doveadm-instance</a></code>(1), Manage the list of running Dovecot instances.</dd>
<dt><code>doveadm kick</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-kick/">doveadm-kick</a></code>(1), Disconnect users by user name and/or IP address.</dd>
<dt><code>doveadm log</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-log/">doveadm-log</a></code>(1), Locate, test or reopen Dovecot&#8217;s log files.</dd>
<dt><code>doveadm mount</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-mount/">doveadm-mount</a></code>(1), Manage the list of mountpoints where mails are stored.</dd>
<dt><code>doveadm penalty</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-penalty/">doveadm-penalty</a></code>(1), Show current penalties.</dd>
<dt><code>doveadm who</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-who/">doveadm-who</a></code>(1); Show who is logged in to the Dovecot server.</dd></dl>
<h3>AUTHENTICATION COMMANDS</h3>
<dl>
<dt><code>doveadm auth</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-auth/">doveadm-auth</a></code>(1), Test authentication for a user.</dd>
<dt><code>doveadm pw</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-pw/">doveadm-pw</a></code>(1), Dovecot&#8217;s password hash generator.</dd>
<dt><code>doveadm user</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-user/">doveadm-user</a></code>(1), Perform a user lookup in Dovecot&#8217;s userdbs</dd></dl>
<h3>MAILBOX COMMANDS</h3>
<dl>
<dt><code>doveadm altmove</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-altmove/">doveadm-altmove</a></code>(1), Move matching mails to the alternative storage.</dd>
<dt><code>doveadm batch</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-batch/">doveadm-batch</a></code>(1), Execute multiple commands for multiple users.</dd>
<dt><code>doveadm copy</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-copy/">doveadm-copy</a></code>(1), Copy messages matching the given search query into another mailbox.</dd>
<dt><code>doveadm deduplicate</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-deduplicate/">doveadm-deduplicate</a></code>(1), Expunge duplicate messages.</dd>
<dt><code>doveadm dump</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-dump/">doveadm-dump</a></code>(1), Dump the content of Dovecot&#8217;s binary mailbox index/log.</dd>
<dt><code>doveadm expunge</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-expunge/">doveadm-expunge</a></code>(1), Expunge messages matching given search query.</dd>
<dt><code>doveadm fetch</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-fetch/">doveadm-fetch</a></code>(1), Fetch messages matching given search query.</dd>
<dt><code>doveadm flags</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-flags/">doveadm-flags</a></code>(1), Add, remove or replace messages&#8217; flags.</dd>
<dt><code>doveadm force-resync</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-force-resync/">doveadm-force-resync</a></code>(1), Repair broken mailboxes, in case Dovecot doesn&#8217;t automatically do that.</dd>
<dt><code>doveadm import</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-import/">doveadm-import</a></code>(1), Import messages matching given search query.</dd>
<dt><code>doveadm index</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-index/">doveadm-index</a></code>(1), Index messages in a given mailbox.</dd>
<dt><code>doveadm mailbox</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-mailbox/">doveadm-mailbox</a></code>(1), Various commands related to handling mailboxes.</dd>
<dt><code>doveadm move</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-move/">doveadm-move</a></code>(1) Move messages matching the given search query into another mailbox.</dd>
<dt><code>doveadm purge</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-purge/">doveadm-purge</a></code>(1) Remove messages with refcount=0 from mdbox files.</dd>
<dt><code>doveadm quota</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-quota/">doveadm-quota</a></code>(1), Initialize/recalculate or show current quota usage.</dd>
<dt><code>doveadm search</code></dt>
<dd> <code><a href="/docs/linux/man/1-doveadm-search/">doveadm-search</a></code>(1), Show a list of mailbox GUIDs and message UIDs matching given search query.</dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>doveadm</code> will exit with one of the following values:</p>
<dl>
<dt><code>0</code></dt>
<dd> Selected command was executed successful.</dd>
<dt><code>&gt;0</code></dt>
<dd> Command failed in some way.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>USER</code></dt>
<dd> This environment variable is used to determine the <i>user</i> if a command accepts a <i>user</i> but none was specified.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/dovecot.conf</i></dt>
<dd> Dovecot&#8217;s main configuration file.</dd>
<dt><i>/etc/dovecot/conf.d/10-mail.conf</i></dt>
<dd> Mailbox locations and namespaces.</dd>
<dt><i>/etc/dovecot/conf.d/90-plugin.conf</i></dt>
<dd> Plugin specific settings.</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm-help/">doveadm-help</a></code>(1), <code><a href="/docs/linux/man/1-doveconf/">doveconf</a></code>(1), <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1), <code><a href="/docs/linux/man/1-dsync/">dsync</a></code>(1), <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) </p>
<h2>Index</h2>
