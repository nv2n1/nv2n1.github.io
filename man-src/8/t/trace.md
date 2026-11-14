---
title: "trace(8)"
name: "trace"
section: "8"
letter: "t"
url: "/docs/linux/man/8-trace/"
description: "bounce – Postfix delivery status reports"
---

<p>bounce &#8211; Postfix delivery status reports</p>
<h2>Synopsis</h2>
<pre><code>bounce</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) daemon maintains per-message log files with delivery status information. Each log file is named after the queue file that it corresponds to, and is kept in a queue subdirectory named after the service name in the <code>master.cf</code> file (either <code>bounce</code>, <code>defer</code> or <code>trace</code>). This program expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager. </p>
<p> The <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) daemon processes two types of service requests:</p>
<dl>
<dt>&bull;</p>
<dd>Append a recipient (non-)delivery status record to a per-message log file.</p>
<dt>&bull;</p>
<dd>Enqueue a delivery status notification message, with a copy of a per-message log file and of the corresponding message. When the delivery status notification message is enqueued successfully, the per-message log file is deleted.</dl>
<p> The software does a best notification effort. A non-delivery notification is sent even when the log file or the original message cannot be read. </p>
<p> Optionally, a bounce (defer, trace) client can request that the per-message log file be deleted when the requested operation fails. This is used by clients that cannot retry transactions by themselves, and that depend on retry logic in their own client.</p>
<h2>Standards</h2>
<pre>RFC 822 (ARPA Internet Text Messages)
RFC 2045 (Format of Internet Message Bodies)
RFC 2822 (Internet Message Format)
RFC 3462 (Delivery Status Notifications)
RFC 3464 (Delivery Status Notifications)
RFC 3834 (Auto-Submitted: message header)
RFC 5322 (Internet Message Format)</pre>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically, as <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>2bounce_notice_recipient (postmaster)</code></p>
<dd>The recipient of undeliverable mail that cannot be returned to the sender.</p>
<dt><code>backwards_bounce_logfile_compatibility (yes)</code></p>
<dd>Produce additional <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile records that can be read by Postfix versions before 2.0.</p>
<dt><code>bounce_notice_recipient (postmaster)</code></p>
<dd>The recipient of postmaster notifications with the message headers of mail that Postfix did not deliver and of SMTP conversation transcripts of mail that Postfix did not receive.</p>
<dt><code>bounce_size_limit (50000)</code></p>
<dd>The maximal amount of original message text that is sent in a non-delivery notification.</p>
<dt><code>bounce_template_file (empty)</code></p>
<dd>Pathname of a configuration file with bounce message templates.</p>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>delay_notice_recipient (postmaster)</code></p>
<dd>The recipient of postmaster notifications with the message headers of mail that cannot be delivered within $delay_warning_time time units.</p>
<dt><code>deliver_lock_attempts (20)</code></p>
<dd>The maximal number of attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile.</p>
<dt><code>deliver_lock_delay (1s)</code></p>
<dd>The time between attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>internal_mail_filter_classes (empty)</code></p>
<dd>What categories of Postfix-generated mail are subject to before-queue content inspection by non_smtpd_milters, header_checks and body_checks.</p>
<dt><code>mail_name (Postfix)</code></p>
<dd>The mail system name that is displayed in Received: headers, in the SMTP greeting banner, and in bounced mail.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>notify_classes (resource, software)</code></p>
<dd>The list of error classes that are reported to the postmaster.</p>
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
<h2>Files</h2>
<pre>/var/spool/postfix/bounce/* non-delivery records
/var/spool/postfix/defer/* non-delivery records
/var/spool/postfix/trace/* delivery status records</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/5-bounce/">bounce</a>(5), bounce message template format
<a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
