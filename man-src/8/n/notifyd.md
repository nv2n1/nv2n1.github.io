---

title: "notifyd(8)"
name: "notifyd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-notifyd/"
description: "notifyd – Cyrus notification server"
---

<p>&nbsp;<wbr>*</p>

<p>notifyd &#8211; Cyrus notification server</p>
<h2>Synopsis</h2>
<p><code>notifyd</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-U</code> <i>uses</i> ] [ <code>-T</code> <i>timeout</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>-D</code> ]</p>
<h2>Description</h2>
<p><code>Notifyd</code> is a daemon started from <a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8) that handles notification requests on behalf of <a href="/docs/linux/man/8-lmtpd/">lmtpd</a>(8). <code>Notifyd</code> accepts the request and performs the notification using the method specified in the request. </p>
<p> Note that for <code>notifyd</code> to run properly you must set proto=udp in its cyrus.conf services entry. prefork=1 is also recommended. </p>
<p> <code>Notifyd</code> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. The <i>notifysocket</i> option is used to specify the Unix domain socket to listen on for notifications.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></dt>
<dd>Read configuration options from <i>config-file</i>.</dd>
<dt><code>-U</code><i> uses</i></dt>
<dd>The maximum number of times that the process should be used for new connections before shutting down. The default is 250.</dd>
<dt><code>-T</code><i> timeout</i></dt>
<dd>The number of seconds that the process will wait for a new connection before shutting down. Note that a value of 0 (zero) will disable the timeout. The default is 60.</dd>
<dt><code>-D</code></dt>
<dd>Run external debugger specified in debug_command.</dd></dl>
<h2>Notification Methods</h2>
<dl>
<dt><code>null</code></dt>
<dd>Ignore the notification request.</dd>
<dt><code>log</code></dt>
<dd>Log the notification to syslog (for testing).</dd>
<dt><code>mailto</code></dt>
<dd>Email the notification. This method can ONLY be used in a Sieve &#8216;notify&#8217; action as it requires a <i>mailto:</i> URL to be specified as an <i>:option</i>.</dd>
<dt><code>zephyr</code></dt>
<dd>Send the notification as a zephyrgram. If used in a Sieve &#8216;notify&#8217; action, additional recipients can be specified as <i>:options</i>.</dd>
<dt><code>external</code></dt>
<dd>Send the notification via an external program. The path to the program is specified using the <i>notify_external</i> option in the configuration file.</dd></dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></dt>
<dd>Default configuration file.</dd>
<dt><code>/etc/cyrus.conf</code></dt>
<dd>Cyrus Master process configuration file.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code>cyrus.conf</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code>, <code><a href="/docs/linux/man/8-lmtpd/">lmtpd</a>(8)</code> </p>
