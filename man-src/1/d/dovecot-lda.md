---
title: "dovecot-lda(1)"
name: "dovecot-lda"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dovecot-lda/"
description: "dovecot-lda – Dovecot’s local mail delivery agent"
---

<h2>NAME</h2>
<p> dovecot-lda &#8211; Dovecot&#8217;s local mail delivery agent</p>
<h2>SYNOPSIS</h2>
<p> <code>dovecot-lda</code> [<code>-ek</code>] [<code>-a</code> <i>address</i>] [<code>-c</code> <i>config_file</i>] [<code>-d</code> <i>username</i>] [<code>-f</code> <i>envelope_sender</i>] [<code>-m</code> <i>mailbox</i>] [<code>-o</code> <i>setting=value</i>] [<code>-p</code> <i>path</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>dovecot-lda</code> is a local mail delivery agent which takes mail from an MTA and delivers it to a user&#8217;s mailbox, while keeping Dovecot index files up to date. </p>
<p> Main features of the <code>dovecot-lda</code> are:</p>
<dl>
<dt>*</p>
<dd> Mailbox indexing during mail delivery, providing faster mailbox access later</p>
<dt>*</p>
<dd> Quota enforcing by the quota plugin</p>
<dt>*</p>
<dd> Sieve language support by the Pigeonhole sieve plugin</dl>
<h2>OPTIONS</h2>
<p> Options accepted by <code>dovecot-lda</code>:</p>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>address</i></p>
<dd> Destination address (e.g. user+ext [at] domain). Default is the same as <i>username</i>.</p>
<dt><code>-c&nbsp;<wbr></code><i>config_file</i></p>
<dd> Alternative configuration file path.</p>
<dt><code>-d&nbsp;<wbr></code><i>username</i></p>
<dd> Destination <i>username</i>. If given, the user information is looked up from userdb. Typically used with virtual users, but not necessarily with system users.</p>
<dt><code>-e</code></p>
<dd> If mail gets rejected, write the rejection reason to stderr and exit with status 77 (EX_NOPERM). The default is to send a rejection mail ourself.</p>
<dt><code>-f&nbsp;<wbr></code><i>envelope_sender</i></p>
<dd> Envelope sender address.</p>
<dt><code>-k</code></p>
<dd> Don&#8217;t clear all environment at startup.</p>
<dt><code>-m&nbsp;<wbr></code><i>mailbox</i></p>
<dd> Destination mailbox (default is <code>INBOX</code>). If the mailbox doesn&#8217;t exist, it will not be created (unless the <i>lda_mailbox_autocreate</i> setting is set to <code>yes</code>). If a message couldn&#8217;t be saved to the <i>mailbox</i> for any reason, it&#8217;s delivered to <code>INBOX</code> instead.</p>
<dt><code>-o&nbsp;<wbr></code><i>setting</i><code>=</code><i>value</i></p>
<dd> Overrides the configuration <i>setting</i> from <i>/etc/dovecot/dovecot.conf</i> and from the userdb with the given <i>value</i>. In order to override multiple settings, the <code>-o</code> option may be specified multiple times.</p>
<dt><code>-p&nbsp;<wbr></code><i>path</i></p>
<dd> Path to the mail to be delivered instead of reading from stdin. If using maildir the file is hard linked to the destination if possible. This allows a single mail to be delivered to multiple users using hard links, but currently it also prevents deliver from updating cache file so it shouldn&#8217;t be used unless really necessary.</dl>
<h2>EXIT STATUS</h2>
<p> <code>dovecot-lda</code> will exit with one of the following values:</p>
<dl>
<dt><code>0</code></p>
<dd> Delivery was successful. (EX_OK)</p>
<dt><code>64</code></p>
<dd> Invalid parameter given. (EX_USAGE)</p>
<dt><code>77</code></p>
<dd> <code>-e</code> option was used and mail was rejected. Typically this happens when user is over quota and <code>quota_full_tempfail = no</code> is configured. (EX_NOPERM)</p>
<dt><code>75</code></p>
<dd> A temporary failure. This is returned for almost all failures. See the log file for details. (EX_TEMPFAIL)</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/dovecot.conf</i></p>
<dd> Dovecot&#8217;s main configuration file.</p>
<dt><i>/etc/dovecot/conf.d/10-mail.conf</i></p>
<dd> Mailbox locations and namespaces.</p>
<dt><i>/etc/dovecot/conf.d/15-lda.conf</i></p>
<dd> LDA specific settings.</p>
<dt><i>/etc/dovecot/conf.d/90-plugin.conf</i></p>
<dd> Plugin specific settings.</p>
<dt><i>/etc/dovecot/conf.d/90-quota.conf</i></p>
<dd> Quota configuration.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1), <code><a href="/docs/linux/man/1-doveconf/">doveconf</a></code>(1), <code><a href="/docs/linux/man/1-dsync/">dsync</a></code>(1) </p>
<p> Related MTA specific documentation:</p>
<dl>
<dt>Postfix:</p>
<dd> <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5), <code><a href="/docs/linux/man/5-transport/">transport</a></code>(5), <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8)</dl>
<p> Exim:</p>
<dl>
<dt>The accept router</p>
<dd> <a rel="nofollow" href="http://exim.org/exim-html-current/doc/html/spec_html/ch16.html">http://exim.org/exim-html-current/doc/html/spec_html/ch16.html</a></p>
<dt>Generic options for transports</p>
<dd> <a rel="nofollow" href="http://exim.org/exim-html-current/doc/html/spec_html/ch24.html">http://exim.org/exim-html-current/doc/html/spec_html/ch24.html</a></p>
<dt>The pipe transport</p>
<dd> <a rel="nofollow" href="http://exim.org/exim-html-current/doc/html/spec_html/ch29.html">http://exim.org/exim-html-current/doc/html/spec_html/ch29.html</a> </p>
</dl>
<h2>Index</h2>
