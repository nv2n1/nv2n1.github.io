---
title: "pickup(8)"
name: "pickup"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pickup/"
description: "pickup – Postfix local mail pickup"
---

<p>pickup &#8211; Postfix local mail pickup</p>
<h2>Synopsis</h2>
<pre><code>pickup</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8) daemon waits for hints that new mail has been dropped into the <code>maildrop</code> directory, and feeds it into the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon. Ill-formatted files are deleted without notifying the originator. This program expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager.</p>
<h2>Standards</h2>
<p>None. The <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8) daemon does not interact with the outside world.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8) daemon is moderately security sensitive. It runs with fixed low privilege and can run in a chrooted environment. However, the program reads files from potentially hostile users. The <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8) daemon opens no files for writing, is careful about what files it opens for reading, and does not actually touch any data that is sent to its public service endpoint.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Bugs</h2>
<p>The <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8) daemon copies mail from file to the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon. It could avoid message copying overhead by sending a file descriptor instead of file data, but then the already complex <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon would have to deal with unfiltered user data.</p>
<h2>Configuration Parameters</h2>
<p>As the <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8) daemon is a relatively long-running process, up to an hour may pass before a <code>main.cf</code> change takes effect. Use the command &quot;<code>postfix reload</code>&quot; command to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Content Inspection Controls</h2>
<dl>
<dt><code>content_filter (empty)</code></p>
<dd>After the message is queued, send the entire message to the specified <i>transport:destination</i>.</p>
<dt><code>receive_override_options (empty)</code></p>
<dd>Enable or disable recipient validation, built-in content filtering, or address mapping.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>line_length_limit (2048)</code></p>
<dd>Upon input, long lines are chopped up into pieces of at most this length; upon delivery, long lines are reconstructed.</p>
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
<pre><a href="//www.systutorials.com/docs/linux/man/8-cleanup/">cleanup</a>(8), message canonicalization
<a href="//www.systutorials.com/docs/linux/man/1-sendmail/">sendmail</a>(1), Sendmail-compatible interface
<a href="//www.systutorials.com/docs/linux/man/1-postdrop/">postdrop</a>(1), mail posting agent
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
