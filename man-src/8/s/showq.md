---
title: "showq(8)"
name: "showq"
section: "8"
letter: "s"
url: "/docs/linux/man/8-showq/"
description: "showq – list the Postfix mail queue"
---

<p>showq &#8211; list the Postfix mail queue</p>
<h2>Synopsis</h2>
<pre><code>showq</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) daemon reports the Postfix mail queue status. It is the program that emulates the sendmail `mailq&#8217; command. </p>
<p> The <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) daemon can also be run in stand-alone mode by the superuser. This mode of operation is used to emulate the `mailq&#8217; command while the Postfix mail system is down.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) daemon can run in a chroot jail at fixed low privilege, and takes no input from the client. Its service port is accessible to local untrusted users, so the service can be susceptible to denial of service attacks.</p>
<h2>Standards</h2>
<p>None. The <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) daemon does not interact with the outside world.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically as <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>duplicate_filter_limit (1000)</code></p>
<dd>The maximal number of addresses remembered by the address duplicate filter for <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) or <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) alias expansion, or for <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) queue displays.</p>
<dt><code>empty_address_recipient (MAILER-DAEMON)</code></p>
<dd>The recipient of mail addressed to the null address.</p>
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
<p> Available in Postfix version 2.9 and later:</p>
<dl>
<dt><code>enable_long_queue_ids (no)</code></p>
<dd>Enable long, non-repeating, queue IDs (queue file names).</dl>
<h2>Files</h2>
<pre>/var/spool/postfix, queue directories</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-pickup/">pickup</a>(8), local mail pickup service
<a href="//www.systutorials.com/docs/linux/man/8-cleanup/">cleanup</a>(8), canonicalize and enqueue mail
<a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
