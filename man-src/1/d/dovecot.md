---
title: "dovecot(1)"
name: "dovecot"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dovecot/"
description: "dovecot – a secure and highly configurable IMAP and POP3 server"
---

<h2>NAME</h2>
<p> dovecot &#8211; a secure and highly configurable IMAP and POP3 server</p>
<h2>SYNOPSIS</h2>
<p> <code>dovecot</code> [<code>-Fp</code>] [<code>-c</code> <i>config-file</i>]<br />
 <code>dovecot -a</code> [<code>-c</code> <i>config-file</i>]<br />
 <code>dovecot -n</code> [<code>-c</code> <i>config-file</i>]<br />
 <code>dovecot &#8211;build-options</code><br />
 <code>dovecot &#8211;help</code><br />
 <code>dovecot &#8211;hostdomain</code><br />
 <code>dovecot &#8211;version</code><br />
 <code>dovecot reload</code><br />
 <code>dovecot stop</code></p>
<h2>DESCRIPTION</h2>
<p> Dovecot is an open source IMAP and POP3 server for Linux/UNIX-like systems, written with security primarily in mind. Dovecot is an excellent choice for both small and large installations. It&#8217;s fast, simple to set up, requires no special administration and it uses very little memory.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Dump all configuration settings to stdout and exit successfully. The same as <i>doveconf -a</i>.</p>
<dt><code>-c&nbsp;<wbr></code><i>config-file</i></p>
<dd> Start <code>dovecot</code> with an alternative configuration.</p>
<dt><code>-F</code></p>
<dd> Run <code>dovecot</code> in foreground, do not daemonize.</p>
<dt><code>-n</code></p>
<dd> Dump non-default settings to stdout and exit successfully. The same as <i>doveconf -n</i>.</p>
<dt><code>-p</code></p>
<dd> Prompt for the ssl key password for the configured <i>ssl_key</i> on startup.</p>
<dt><code>&#8211;build-options</code></p>
<dd> Show Dovecot&#8217;s build options and exit successfully.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a usage message to stdout and exit successfully.</p>
<dt><code>&#8211;hostdomain</code></p>
<dd> Shows the current <i>host</i>.<i>domain</i> name of the system. If the domain lookup should fail for some reason, only the hostname will be shown.</p>
<dt><code>&#8211;version</code></p>
<dd> Show Dovecot&#8217;s version and exit successfully.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>reload</code></p>
<dd> Force <code>dovecot</code> to reload its configuration.</p>
<dt><code>stop</code></p>
<dd> Shutdown <code>dovecot</code> and all its child processes.</dl>
<p> When <i>shutdown_clients</i> is set to <code>no</code>, existing sessions will continue to use the old settings, after a <code>dovecot reload</code>. Also all sessions will keep alive after a <code>dovecot stop</code>.<br />
 By default all active sessions will be shut down.</p>
<h2>SIGNALS</h2>
<p> Dovecot handles the following <i>signals</i> as described:</p>
<dl>
<dt><code>HUP</code></p>
<dd> Force <code>dovecot</code> to reload its configuration.</p>
<dt><code>INT</code></p>
<dd> Shutdown <code>dovecot</code> and all its child processes.</p>
<dt><code>TERM</code></p>
<dd> Shutdown <code>dovecot</code> and all its child processes.</p>
<dt><code>USR1</code></p>
<dd> Force <code>dovecot</code> to reopen all configured log files (<i>log_path</i>, <i>info_log_path&nbsp;<wbr></i>and <i>debug_log_path</i>).</dl>
<p> The <i>signals</i> <code>ALARM&nbsp;<wbr></code>and <code>PIPE</code> are ignored.</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/dovecot.conf</i></p>
<dd> Dovecot&#8217;s main configuration file.</p>
<dt><i>/etc/dovecot/dovecot-ldap.conf.ext</i></p>
<dd> Dovecot&#8217;s LDAP authdb/userdb module configuration file.</p>
<dt><i>/etc/dovecot/dovecot-sql.conf.ext</i></p>
<dd> Dovecot&#8217;s SQL authdb/userdb module configuration file.</p>
<dt><i>/etc/dovecot/dovecot-dict-sql.conf.ext</i></p>
<dd> Dovecot&#8217;s dict configuration with SQL-backend.</p>
<dt><i>/etc/dovecot/conf.d/auth-*-conf.ext</i></p>
<dd> Configuration files of different authentication modules.</p>
<dt><i>/etc/dovecot/conf.d/*.conf</i></p>
<dd> Configuration files of different services and settings.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>AUTHOR</h2>
<p> Dovecot &lt;<a rel="nofollow" href="http://dovecot.org">http://dovecot.org</a>&gt; and its manual pages were written by the Dovecot authors &lt;<a rel="nofollow" href="http://dovecot.org/doc/AUTHORS">http://dovecot.org/doc/AUTHORS</a>&gt;, mainly Timo Sirainen &lt;tss at iki.fi&gt;, and are licensed under the terms of the MIT and LGPLv2.1 licenses, see &lt;<a rel="nofollow" href="http://dovecot.org/doc/COPYING">http://dovecot.org/doc/COPYING</a>&gt; for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveconf/">doveconf</a></code>(1), <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1), <code><a href="/docs/linux/man/1-dsync/">dsync</a></code>(1) </p>
<h2>Index</h2>
