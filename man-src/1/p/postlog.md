---
title: "postlog(1)"
name: "postlog"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postlog/"
description: "postlog – Postfix-compatible logging utility"
---

<h2 class="name">NAME</h2>
<p> postlog &#8211; Postfix-compatible logging utility </p>
<h2>SYNOPSIS</h2>
<p> <code>postlog</code> [<code>-iv</code>] [<code>-c </code><i>config_dir</i>] [<code>-p </code><i>priority</i>] [<code>-t </code><i>tag</i>] [<i>text&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-postlog/">postlog</a></code>(1) command implements a Postfix-compatible logging interface for use in, for example, shell scripts. </p>
<p> By default, <code><a href="/docs/linux/man/1-postlog/">postlog</a></code>(1) logs the <i>text</i> given on the command line as one record. If no <i>text</i> is specified on the command line, <code><a href="/docs/linux/man/1-postlog/">postlog</a></code>(1) reads from standard input and logs each input line as one record. </p>
<p> By default, logging is sent to <code>syslogd</code>(8) or <code>postlogd</code>(8); when the standard error stream is connected to a terminal, logging is sent there as well. </p>
<p> The following options are implemented:</p>
<dl>
<dt><code>-c </code><i>config_dir</i></dt>
<dd> Read the <code>main.cf</code> configuration file in the named directory instead of the default configuration directory.</dd>
<dt><code>-i</code> (obsolete)</dt>
<dd> Include the process ID in the logging tag. This flag is ignored as of Postfix 3.4, where the PID is always included.</dd>
<dt><code>-p </code><i>priority</i> (default: <code>info</code>)</dt>
<dd> Specifies the logging severity: <code>info</code>, <code>warn</code>, <code>error</code>, <code>fatal</code>, or <code>panic</code>. With Postfix 3.1 and later, the program will pause for 1 second after reporting a <code>fatal</code> or <code>panic</code> condition, just like other Postfix programs.</dd>
<dt><code>-t </code><i>tag</i></dt>
<dd> Specifies the logging tag, that is, the identifying name that appears at the beginning of each logging record. A default tag is used when none is specified.</dd>
<dt><code>-v</code></dt>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>MAIL_CONFIG</dt>
<dd> Directory with the <code>main.cf</code> file.</dd></dl>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></dt>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</dd>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></dt>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</dd>
<dt><code>syslog_facility (mail)</code></dt>
<dd> The syslog facility of Postfix logging.</dd>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></dt>
<dd> A prefix that is prepended to the process name in syslog records, so that, for example, &quot;smtpd&quot; becomes &quot;prefix/smtpd&quot;.</dd></dl>
<p> Available in Postfix 3.4 and later:</p>
<dl>
<dt><code>maillog_file (empty)</code></dt>
<dd> The name of an optional logfile that is written by the Postfix <code>postlogd</code>(8) service.</dd>
<dt><code>postlog_service_name (postlog)</code></dt>
<dd> The name of the <code>postlogd</code>(8) service entry in master.cf.</dd></dl>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
postlogd(8), Postfix logging
syslogd(8), system logging
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
</pre>
<h2>Index</h2>
