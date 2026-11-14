---
title: "virtual(8)"
name: "virtual"
section: "8"
letter: "v"
url: "/docs/linux/man/8-virtual/"
description: "virtual – Postfix virtual domain mail delivery agent"
---

<p>virtual &#8211; Postfix virtual domain mail delivery agent</p>
<h2>Synopsis</h2>
<pre><code>virtual</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agent is designed for virtual mail hosting services. Originally based on the Postfix <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent, this agent looks up recipients with map lookups of their full recipient address, instead of using hard-coded unix password file lookups of the address local part only. </p>
<p> This delivery agent only delivers mail. Other features such as mail forwarding, out-of-office notifications, etc., must be configured via virtual_alias maps or via similar lookup mechanisms.</p>
<h2>Mailbox Location</h2>
<p>The mailbox location is controlled by the <code>virtual_mailbox_base</code> and <code>virtual_mailbox_maps</code> configuration parameters (see below). The <code>virtual_mailbox_maps</code> table is indexed by the recipient address as described under TABLE SEARCH ORDER below. </p>
<p> The mailbox pathname is constructed as follows: </p>
<pre> <code>$virtual_mailbox_base/$virtual_mailbox_maps(</code><i>recipient</i><code>)</code></pre>
<p>where <i>recipient</i> is the full recipient address.</p>
<h2>Unix Mailbox Format</h2>
<p>When the mailbox location does not end in <code>/</code>, the message is delivered in UNIX mailbox format. This format stores multiple messages in one textfile. </p>
<p> The <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agent prepends a &quot;<code>From </code><i>sender time_stamp</i>&quot; envelope header to each message, prepends a <code>Delivered-To:</code> message header with the envelope recipient address, prepends an <code>X-Original-To:</code> header with the recipient address as given to Postfix, prepends a <code>Return-Path:</code> message header with the envelope sender address, prepends a <code>&gt;</code> character to lines beginning with &quot;<code>From </code>&quot;, and appends an empty line. </p>
<p> The mailbox is locked for exclusive access while delivery is in progress. In case of problems, an attempt is made to truncate the mailbox to its original length.</p>
<h2>Qmail Maildir Format</h2>
<p>When the mailbox location ends in <code>/</code>, the message is delivered in qmail <code>maildir</code> format. This format stores one message per file. </p>
<p> The <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agent prepends a <code>Delivered-To:</code> message header with the final envelope recipient address, prepends an <code>X-Original-To:</code> header with the recipient address as given to Postfix, and prepends a <code>Return-Path:</code> message header with the envelope sender address. </p>
<p> By definition, <code>maildir</code> format does not require application-level file locking during mail delivery or retrieval.</p>
<h2>Mailbox Ownership</h2>
<p>Mailbox ownership is controlled by the <code>virtual_uid_maps</code> and <code>virtual_gid_maps</code> lookup tables, which are indexed with the full recipient address. Each table provides a string with the numerical user and group ID, respectively. </p>
<p> The <code>virtual_minimum_uid</code> parameter imposes a lower bound on numerical user ID values that may be specified in any <code>virtual_uid_maps</code>.</p>
<h2>Case Folding</h2>
<p>All delivery decisions are made using the full recipient address, folded to lower case. See also the next section for a few exceptions with optional address extensions.</p>
<h2>Table Search Order</h2>
<p>Normally, a lookup table is specified as a text file that serves as input to the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command. The result, an indexed file in <code>dbm</code> or <code>db</code> format, is used for fast searching by the mail system. </p>
<p> The search order is as follows. The search stops upon the first successful lookup.</p>
<dl>
<dt>&bull;</p>
<dd>When the recipient has an optional address extension the <i>user+extension [at] domain.tld</i> address is looked up first. </p>
<p> With Postfix versions before 2.1, the optional address extension is always ignored.</p>
<dt>&bull;</p>
<dd>The <i>user [at] domain.tld</i> address, without address extension, is looked up next.</p>
<dt>&bull;</p>
<dd>Finally, the recipient <i>@domain</i> is looked up.</dl>
<p> When the table is provided via other means such as NIS, LDAP or SQL, the same lookups are done as for ordinary indexed files. </p>
<p> Alternatively, a table can be provided as a regular-expression map where patterns are given as regular expressions. In that case, only the full recipient address is given to the regular-expression map.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agent is not security sensitive, provided that the lookup tables with recipient user/group ID information are adequately protected. This program is not designed to run chrooted. </p>
<p> The <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agent disallows regular expression substitution of $1 etc. in regular expression lookup tables, because that would open a security hole. </p>
<p> The <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agent will silently ignore requests to use the <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server. Instead it will open the table directly. Before Postfix version 2.2, the virtual delivery agent will terminate with a fatal error.</p>
<h2>Standards</h2>
<pre>RFC 822 (ARPA Internet Text Messages)</pre>
<h2>Diagnostics</h2>
<p>Mail bounces when the recipient has no mailbox or when the recipient is over disk quota. In all other cases, mail for an existing recipient is deferred and a warning is logged. </p>
<p> Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). Corrupted message files are marked so that the queue manager can move them to the <code>corrupt</code> queue afterwards. </p>
<p> Depending on the setting of the <code>notify_classes</code> parameter, the postmaster is notified of bounces and of other trouble.</p>
<h2>Bugs</h2>
<p>This delivery agent supports address extensions in email addresses and in lookup table keys, but does not propagate address extension information to the result of table lookup. </p>
<p> Postfix should have lookup tables that can return multiple result attributes. In order to avoid the inconvenience of maintaining three tables, use an LDAP or MYSQL database.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically, as <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Mailbox Delivery Controls</h2>
<dl>
<dt><code>virtual_mailbox_base (empty)</code></p>
<dd>A prefix that the <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agent prepends to all pathname results from $virtual_mailbox_maps table lookups.</p>
<dt><code>virtual_mailbox_maps (empty)</code></p>
<dd>Optional lookup tables with all valid addresses in the domains that match $virtual_mailbox_domains.</p>
<dt><code>virtual_minimum_uid (100)</code></p>
<dd>The minimum user ID value that the <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agent accepts as a result from $virtual_uid_maps table lookup.</p>
<dt><code>virtual_uid_maps (empty)</code></p>
<dd>Lookup tables with the per-recipient user ID that the <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agent uses while writing to the recipient&#8217;s mailbox.</p>
<dt><code>virtual_gid_maps (empty)</code></p>
<dd>Lookup tables with the per-recipient group ID for <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) mailbox delivery.</dl>
<p> Available in Postfix version 2.0 and later:</p>
<dl>
<dt><code>virtual_mailbox_domains ($virtual_mailbox_maps)</code></p>
<dd>Postfix is final destination for the specified list of domains; mail is delivered via the $virtual_transport mail delivery transport.</p>
<dt><code>virtual_transport (virtual)</code></p>
<dd>The default mail delivery transport and next-hop destination for final delivery to domains listed with $virtual_mailbox_domains.</dl>
<p> Available in Postfix version 2.5.3 and later:</p>
<dl>
<dt><code>strict_mailbox_ownership (yes)</code></p>
<dd>Defer delivery when a mailbox file is not owned by its recipient.</dl>
<h2>Locking Controls</h2>
<dl>
<dt><code>virtual_mailbox_lock (see &#8216;postconf -d&#8217; output)</code></p>
<dd>How to lock a UNIX-style <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) mailbox before attempting delivery.</p>
<dt><code>deliver_lock_attempts (20)</code></p>
<dd>The maximal number of attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile.</p>
<dt><code>deliver_lock_delay (1s)</code></p>
<dd>The time between attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile.</p>
<dt><code>stale_lock_time (500s)</code></p>
<dd>The time after which a stale exclusive mailbox lockfile is removed.</dl>
<h2>Resource And Rate Controls</h2>
<dl>
<dt><code>virtual_destination_concurrency_limit ($default_destination_concurrency_limit)</code></p>
<dd>The maximal number of parallel deliveries to the same destination via the virtual message delivery transport.</p>
<dt><code>virtual_destination_recipient_limit ($default_destination_recipient_limit)</code></p>
<dd>The maximal number of recipients per message for the virtual message delivery transport.</p>
<dt><code>virtual_mailbox_limit (51200000)</code></p>
<dd>The maximal size in bytes of an individual <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) mailbox or maildir file, or zero (no limit).</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>delay_logging_resolution_limit (2)</code></p>
<dd>The maximal number of digits after the decimal point when logging sub-second delay values.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/8-bounce/">bounce</a>(8), delivery status reports
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme_Files</h2>
<pre>Use &quot;<code>postconf readme_directory</code>&quot; or
&quot;<code>postconf html_directory</code>&quot; to locate this information.
VIRTUAL_README, domain hosting howto</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>This delivery agent was originally based on the Postfix local delivery agent. Modifications mainly consisted of removing code that either was not applicable or that was not safe in this context: aliases, ~user/.forward files, delivery to &quot;|command&quot; or to /file/name. </p>
<p> The <code>Delivered-To:</code> message header appears in the <code>qmail</code> system by Daniel Bernstein. </p>
<p> The <code>maildir</code> structure appears in the <code>qmail</code> system by Daniel Bernstein.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Andrew McNamara
andrewm [at] connect.com.au
connect.com.au Pty. Ltd.
Level 3, 213 Miller St
North Sydney 2060, NSW, Australia</pre>
