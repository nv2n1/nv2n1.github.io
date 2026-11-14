---
title: "nntpd(8)"
name: "nntpd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nntpd/"
description: "nntpd – NNTP server process"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>nntpd &#8211; NNTP server process</p>
<h2>Synopsis</h2>
<p><code>nntpd</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-U</code> <i>uses</i> ] [ <code>-T</code> <i>timeout</i> ] [ <code>-D</code> ] </p>
<p>[ <code>-s</code> ] [ <code>-r</code> ] [ <code>-f</code> ] [ <code>-p</code> <i>ssf</i> ]</p>
<h2>Description</h2>
<p><i>Nntpd</i> is a NNTP server. It accepts commands on its standard input and responds on its standard output. It MUST invoked by <i><a href="/docs/linux/man/8-master/">master</a></i>(8) with those descriptors attached to a remote client connection. </p>
<p> <i>Nntpd</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. The optional <i>newsprefix</i> option specifies a prefix to be prepended to newsgroup names to make the corresponding IMAP mailbox names. The optional <i>newspostuser</i> option specifies the special userid to be used when contructing the To: header address for following up to articles when read via IMAP. The optional <i>newspeer</i> option specifies the fully qualified hostname of the upstream news server to which articles are fed. The optional <i>allownewnews</i> option enables the NNTP NEWNEWS command. NOTE: For servers with a large volume of articles, the NEWNEWS command can be expensive. </p>
<p> If the directory log/<i>user</i> exists under the directory specified in the <i>configdirectory</i> configuration option, then <i>nntpd</i> will create protocol telemetry logs for sessions authenticating as <i>user</i>. The telemetry logs will be stored in the log/<i>user</i> directory with a filename of the <i>nntpd</i> process-id.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-U</code><i> uses</i></p>
<dd>The maximum number of times that the process should be used for new connections before shutting down. The default is 250.</p>
<dt><code>-T</code><i> timeout</i></p>
<dd>The number of seconds that the process will wait for a new connection before shutting down. Note that a value of 0 (zero) will disable the timeout. The default is 60.</p>
<dt><code>-D</code></p>
<dd>Run external debugger specified in debug_command.</p>
<dt><code>-s</code></p>
<dd>Serve NNTP over SSL (nntps). All data to and from <i>nntpd</i> is encrypted using the Secure Sockets Layer.</p>
<dt><code>-r</code></p>
<dd>Only allow NNTP reader commands. Permitted clients will only be allowed to read/post articles.</p>
<dt><code>-f</code></p>
<dd>Only allow NNTP feeder commands. Permitted clients will only be allowed to feed articles (no reading).</p>
<dt><code>-p</code><i> ssf</i></p>
<dd>Tell <i>nntpd</i> that an external layer exists. An SSF (security strength factor) of 1 means an integrity protection layer exists. Any higher SSF implies some form of privacy protection.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code> </p>
