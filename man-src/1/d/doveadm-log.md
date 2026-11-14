---
title: "doveadm-log(1)"
name: "doveadm-log"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-log/"
description: "doveadm-log – Locate, test or reopen Dovecot’s log files"
---

<h2>NAME</h2>
<p> doveadm-log &#8211; Locate, test or reopen Dovecot&#8217;s log files</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>log errors</code> [<code>-s</code> <i>min_timestamp</i>]<br />
 <code>doveadm</code> [<code>-Dv</code>] <code>log find</code> [<i>directory</i>]<br />
 <code>doveadm</code> [<code>-Dv</code>] <code>log reopen</code><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>log test</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>doveadm log</code> <i>commands</i> are used to locate and reopen the log files of <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1). It&#8217;s also possible to test the configured targets of the <i>*log_path</i> settings.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<h2>COMMANDS</h2>
<h3>log errors</h3>
<p> <code>doveadm log errors</code> [<code>-s</code> <i>min_timestamp</i>] </p>
<p> The <code>log errors</code> command is used to show the last &#8211; up to 1,000 &#8211; errors and warnings. If no output is generated, no errors have occurred since the last start. </p>
<dl>
<dt><code>-s</code><i>&nbsp;<wbr>min_timestamp</i></p>
<dd> An integer value, representing seconds since the epoch &#8211; also known as Unix timestamp. When a min_timestamp was given, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will only show errors occurred since that point in time.</dl>
<h3>log find</h3>
<p> <code>doveadm log find</code> [<i>directory</i>] </p>
<p> The <code>log find</code> command is used to show the location of the log files, to which <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1) sends its log messages. If <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1) logs its messages through <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) and <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) could not find any log files, you can specify the <i>directory</i> where your syslogd writes its log files.</p>
<h3>log reopen</h3>
<p> <code>doveadm log reopen</code> </p>
<p> This command causes <code>doveadm</code> to reopen all log files, configured in the <i>log_path</i>, <i>info_log_path</i> and <i>debug_log_path</i> settings. These settings are configured in <i>/etc/dovecot/conf.d/10-logging.conf</i>.<br />
 This is for example useful after manually rotating the log files.</p>
<h3>log test</h3>
<p> <code>doveadm log test</code> </p>
<p> This command causes <code>doveadm</code> to write the message &quot;This is Dovecot&#8217;s <i>priority</i> log (<i>timestamp</i>)&quot; to the configured log files. The used priorities are: <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code> and <code>fatal</code>.</p>
<h2>EXAMPLE</h2>
<p> This example shows how to locate the log files used by <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1). </p>
<pre>
<code>doveadm log find</code>
Looking for log files from /var/log
Debug: /var/log/dovecot.debug
Info: /var/log/mail.log
Warning: /var/log/mail.log
Error: /var/log/mail.log
Fatal: /var/log/mail.log
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
