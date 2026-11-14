---
title: "smtpd-opensmtpd(8)"
name: "smtpd-opensmtpd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smtpd-opensmtpd/"
description: "smtpd – Simple Mail Transfer Protocol daemon"
---

<p><code>smtpd</code> &#8211; Simple Mail Transfer Protocol daemon</p>
<h2>Synopsis</h2>
<pre><code>smtpd
[-dhnv]
[-D macro=value]
[-f file]
[-P system]
[-T trace]</code></pre>
<h2>Description</h2>
<p><code>smtpd</code> is a Simple Mail Transfer Protocol (SMTP) daemon which can be used as a machine&#8217;s primary mail system. <code>smtpd</code> can listen on a network interface and handle SMTP transactions; it can also be fed messages through the standard <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8) interface. It can relay messages through remote mail transfer agents or store them locally using either the mbox or maildir format. This implementation supports SMTP as defined by RFC 5321 as well as several extensions. A running <code>smtpd</code> can be controlled through <code><a href="/docs/linux/man/8-smtpctl/">smtpctl</a></code>(8). </p>
<p> The options are as follows:</p>
<dl>
<dd>
<dl>
<dt><code>-D</code> <i>macro</i>=<i>value</i></p>
<dd>Define <i>macro</i> to be set to <i>value</i> on the command line. Overrides the definition of <i>macro</i> in the configuration file.</p>
<dt><code>-d</code></p>
<dd>Do not daemonize. If this option is specified, <code>smtpd</code> will run in the foreground and log to <i>stderr.</i></p>
<dt><code>-f</code> <i>file</i></p>
<dd>Specify an alternative configuration file.</p>
<dt><code>-h</code></p>
<dd>Display version and usage.</p>
<dt><code>-n</code></p>
<dd>Configtest mode. Only check the configuration file for validity.</p>
<dt><code>-P</code> <i>system</i></p>
<dd>Pause a specific subsystem at startup. Normal operation can be resumed using <code><a href="/docs/linux/man/8-smtpctl/">smtpctl</a></code>(8). This option can be used multiple times. The accepted values are:</dl>
<dl>
<dd>
<dl>
<dt>mda</p>
<dd>Do not schedule local deliveries.</p>
<dt>mta</p>
<dd>Do not schedule remote transfers.</p>
<dt>smtp</p>
<dd>Do not listen on SMTP sockets.</dl>
</dl>
<dl>
<dt><code>-T</code> <i>trace</i></p>
<dd>Enables real-time tracing at startup. Normal operation can be resumed using <code><a href="/docs/linux/man/8-smtpctl/">smtpctl</a></code>(8). This option can be used multiple times. The accepted values are:</dl>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>imsg</p>
<dt>&bull;</p>
<dd>io</p>
<dt>&bull;</p>
<dd>smtp (incoming sessions)</p>
<dt>&bull;</p>
<dd>filters</p>
<dt>&bull;</p>
<dd>transfer (outgoing sessions)</p>
<dt>&bull;</p>
<dd>bounce</p>
<dt>&bull;</p>
<dd>scheduler</p>
<dt>&bull;</p>
<dd>expand (aliases/virtual/forward expansion)</p>
<dt>&bull;</p>
<dd>lookup (user/credentials lookups)</p>
<dt>&bull;</p>
<dd>stat</p>
<dt>&bull;</p>
<dd>rules (matched by incoming sessions)</p>
<dt>&bull;</p>
<dd>mproc</p>
<dt>&bull;</p>
<dd>all</dl>
</dl>
<dl>
<dt><code>-v</code></p>
<dd>Produce more verbose output.</dl>
</dl>
<h2>Files</h2>
<dl>
<dd>
<dl>
<dt><code>/etc/opensmtpd/mailname</code></p>
<dd>Alternate server name to use.</p>
<dt><code>/etc/opensmtpd/smtpd.conf</code></p>
<dd>Default <code>smtpd</code> configuration file.</p>
<dt><code>/var/run/smtpd.sock</code></p>
<dd>Ux -domain socket used for communication with <code><a href="/docs/linux/man/8-smtpctl/">smtpctl</a></code>(8).</p>
<dt><code>/var/spool/smtpd/</code></p>
<dd>Spool directories for mail during processing.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-smtpd-conf/">smtpd.conf</a></code>(5), <code><a href="/docs/linux/man/8-mailwrapper/">mailwrapper</a></code>(8), <code><a href="/docs/linux/man/8-smtpctl/">smtpctl</a></code>(8)</p>
<h2>Standards</h2>
<p>Rs %A J. Klensin %D October 2008 %R RFC 5321 %T Simple Mail Transfer Protocol Re</p>
<h2>History</h2>
<p>The <code>smtpd</code> program first appeared in OpenBSD 4.6.</p>
