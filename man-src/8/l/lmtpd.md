---

title: "lmtpd(8)"
name: "lmtpd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lmtpd/"
description: "lmtpd – LMTP server process"
---

<p>&nbsp;<wbr>*</p>

<p>lmtpd &#8211; LMTP server process</p>
<h2>Synopsis</h2>
<p><code>lmtpd</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-U</code> <i>uses</i> ] [ <code>-T</code> <i>timeout</i> ] [ <code>-D</code> ] </p>
<p>[ <code>-a</code> ]</p>
<h2>Description</h2>
<p><i>Lmtpd</i> is an LMTP server used to deliver mail to the IMAP mailstore. It accepts commands on its standard input and responds on its standard output. It MUST be invoked by <i><a href="/docs/linux/man/8-master/">master</a></i>(8) with those descriptors attached to a remote client connection. </p>
<p> <i>Lmtpd</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></dt>
<dd>Read configuration options from <i>config-file</i>.</dd>
<dt><code>-U</code><i> uses</i></dt>
<dd>The maximum number of times that the process should be used for new connections before shutting down. The default is 250.</dd>
<dt><code>-T</code><i> timeout</i></dt>
<dd>The number of seconds that the process will wait for a new connection before shutting down. Note that a value of 0 (zero) will disable the timeout. The default is 60.</dd>
<dt><code>-D</code></dt>
<dd>Run external debugger specified in debug_command.</dd>
<dt><code>-a</code></dt>
<dd>Preauthorize connections initiated on an internet socket, instead of requiring LMTP AUTH. This should only be used for connections coming from trusted hosts.</dd></dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></dt>
<dd></dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code> </p>
