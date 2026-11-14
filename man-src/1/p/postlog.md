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
<p> By default, logging is sent to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) or <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8); when the standard error stream is connected to a terminal, logging is sent there as well. </p>
<p> The following options are implemented:</p>
<dl>
<dt><code>-c </code><i>config_dir</i></p>
<dd> Read the <code>main.cf</code> configuration file in the named directory instead of the default configuration directory.</p>
<dt><code>-i</code> (obsolete)</p>
<dd> Include the process ID in the logging tag. This flag is ignored as of Postfix 3.4, where the PID is always included.</p>
<dt><code>-p </code><i>priority</i> (default: <code>info</code>)</p>
<dd> Specifies the logging severity: <code>info</code>, <code>warn</code>, <code>error</code>, <code>fatal</code>, or <code>panic</code>. With Postfix 3.1 and later, the program will pause for 1 second after reporting a <code>fatal</code> or <code>panic</code> condition, just like other Postfix programs.</p>
<dt><code>-t </code><i>tag</i></p>
<dd> Specifies the logging tag, that is, the identifying name that appears at the beginning of each logging record. A default tag is used when none is specified.</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>MAIL_CONFIG</p>
<dd> Directory with the <code>main.cf</code> file.</dl>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd> The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd> A prefix that is prepended to the process name in syslog records, so that, for example, &quot;smtpd&quot; becomes &quot;prefix/smtpd&quot;.</dl>
<p> Available in Postfix 3.4 and later:</p>
<dl>
<dt><code>maillog_file (empty)</code></p>
<dd> The name of an optional logfile that is written by the Postfix <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8) service.</p>
<dt><code>postlog_service_name (postlog)</code></p>
<dd> The name of the <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8) service entry in master.cf.</dl>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/8-postlogd/">postlogd</a>(8), Postfix logging
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging
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
