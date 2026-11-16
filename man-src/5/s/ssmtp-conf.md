---
title: "ssmtp-conf(5)"
name: "ssmtp-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-ssmtp-conf/"
description: "ssmtp.conf – ssmtp configuration file"
---

<p><code>ssmtp.conf</code> &#8211; ssmtp configuration file</p>
<h2>Description</h2>
<p><code>ssmtp</code> reads configuration data from /etc/ssmtp/ssmtp.conf The file contains keyword-argument pairs, one per line. Lines starting with `#&#8217; and empty lines are interpreted as comments. </p>
<p> The possible keywords and their meanings are as follows (both are case-insensitive):</p>
<dl>
<dt><code>Root</code></dt>
<dd>The user that gets all mail for userids less than 1000. If blank, address rewriting is disabled. </dd>
<dt><code>Mailhub</code></dt>
<dd>The host to send mail to, in the form <i>host </i><code>| </code><i>IP_addr </i>[: <i>port </i>] The default port is 25. </dd>
<dt><code>RewriteDomain</code></dt>
<dd>The domain from which mail seems to come. for user authentication. </dd>
<dt><code>Hostname</code></dt>
<dd>The full qualified name of the host. If not specified, the host is queried for its hostname. </dd>
<dt><code>FromLineOverride</code></dt>
<dd>Specifies whether the From header of an email, if any, may override the default domain. The default is &#8220;no&#8221; </dd>
<dt><code>UseTLS</code></dt>
<dd>Specifies whether ssmtp uses TLS to talk to the SMTP server. The default is &#8220;no&#8221; </dd>
<dt><code>UseSTARTTLS</code></dt>
<dd>Specifies whether ssmtp does a EHLO/STARTTLS before starting SSL negotiation. See RFC 2487. </dd>
<dt><code>TLSCert</code></dt>
<dd>The file name of an RSA certificate to use for TLS, if required.</dd>
<dt><code>TLSKey</code></dt>
<dd>The file name of an RSA key to use for TLS, if required.</dd>
<dt><code>TLS_CA_File</code></dt>
<dd>A file of trusted certificates for validating the server, if required. </dd>
<dt><code>TLS_CA_Dir</code></dt>
<dd>A directory of trusted certificates for validating the server, if required. </dd>
<dt><code>AuthUser</code></dt>
<dd>The user name to use for SMTP AUTH. The default is blank, in which case SMTP AUTH is not used. sent without </dd>
<dt><code>AuthPass</code></dt>
<dd>The password to use for SMTP AUTH. </dd>
<dt><code>AuthMethod</code></dt>
<dd>The authorization method to use. If unset, plain text is used. May also be set to &#8220;cram-md5&#8221;</dd></dl>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/ssmtp/ssmtp.conf </code></dt>
<dd>Contains configuration data for <code>ssmtp</code></dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ssmtp/">ssmtp</a>(8)</p>
<h2>Authors</h2>
<p>Matt Ryan (mryan [at] debian.org), Hugo Haas (hugo [at] debian.org), Christoph Lameter (clameter [at] debian.org) and Dave Collier-Brown (davecb [at] hobbes.ss.org). Reuben Thomas (rrt [at] sc3d.org) wrote the man page.</p>
