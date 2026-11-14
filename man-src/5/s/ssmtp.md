---
title: "ssmtp(5)"
name: "ssmtp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-ssmtp/"
description: "ssmtp.conf – ssmtp configuration file"
---

<p><code>ssmtp.conf</code> &#8211; ssmtp configuration file</p>
<h2>Description</h2>
<p><code>ssmtp</code> reads configuration data from /etc/ssmtp/ssmtp.conf The file contains keyword-argument pairs, one per line. Lines starting with `#&#8217; and empty lines are interpreted as comments. </p>
<p> The possible keywords and their meanings are as follows (both are case-insensitive):</p>
<dl>
<dt><code>Root</code></p>
<dd>The user that gets all mail for userids less than 1000. If blank, address rewriting is disabled. </p>
<dt><code>Mailhub</code></p>
<dd>The host to send mail to, in the form <i>host </i><code>| </code><i>IP_addr </i>[: <i>port </i>] The default port is 25. </p>
<dt><code>RewriteDomain</code></p>
<dd>The domain from which mail seems to come. for user authentication. </p>
<dt><code>Hostname</code></p>
<dd>The full qualified name of the host. If not specified, the host is queried for its hostname. </p>
<dt><code>FromLineOverride</code></p>
<dd>Specifies whether the From header of an email, if any, may override the default domain. The default is &#8220;no&#8221; </p>
<dt><code>UseTLS</code></p>
<dd>Specifies whether ssmtp uses TLS to talk to the SMTP server. The default is &#8220;no&#8221; </p>
<dt><code>UseSTARTTLS</code></p>
<dd>Specifies whether ssmtp does a EHLO/STARTTLS before starting SSL negotiation. See RFC 2487. </p>
<dt><code>TLSCert</code></p>
<dd>The file name of an RSA certificate to use for TLS, if required.</p>
<dt><code>TLSKey</code></p>
<dd>The file name of an RSA key to use for TLS, if required.</p>
<dt><code>TLS_CA_File</code></p>
<dd>A file of trusted certificates for validating the server, if required. </p>
<dt><code>TLS_CA_Dir</code></p>
<dd>A directory of trusted certificates for validating the server, if required. </p>
<dt><code>AuthUser</code></p>
<dd>The user name to use for SMTP AUTH. The default is blank, in which case SMTP AUTH is not used. sent without </p>
<dt><code>AuthPass</code></p>
<dd>The password to use for SMTP AUTH. </p>
<dt><code>AuthMethod</code></p>
<dd>The authorization method to use. If unset, plain text is used. May also be set to &#8220;cram-md5&#8221;</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/ssmtp/ssmtp.conf </code></p>
<dd>Contains configuration data for <code>ssmtp</code></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ssmtp/">ssmtp</a>(8)</p>
<h2>Authors</h2>
<p>Matt Ryan (mryan [at] debian.org), Hugo Haas (hugo [at] debian.org), Christoph Lameter (clameter [at] debian.org) and Dave Collier-Brown (davecb [at] hobbes.ss.org). Reuben Thomas (rrt [at] sc3d.org) wrote the man page.</p>
