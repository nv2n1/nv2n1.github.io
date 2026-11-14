---
title: "rsync-ssl(1)"
name: "rsync-ssl"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rsync-ssl/"
description: "rsync-ssl – a helper script for connecting to an ssl rsync daemon"
---

<h2 class="name">NAME</h2>
<p> rsync-ssl &#8211; a helper script for connecting to an ssl rsync daemon</p>
<h2>SYNOPSIS</h2>
<pre>
rsync-ssl [--type=SSL_TYPE] RSYNC_ARGS
</pre>
<p> The online version of this manpage (that includes cross-linking of topics) is available at <a rel="nofollow" href="https://download.samba.org/pub/rsync/rsync-ssl.1.">https://download.samba.org/pub/rsync/rsync-ssl.1.</a> </p>
<h2>DESCRIPTION</h2>
<p> The rsync-ssl script helps you to run an rsync copy to/from an rsync daemon that requires ssl connections. </p>
<p> The script requires that you specify an rsync-daemon arg in the style of either <code>hostname::</code> (with 2 colons) or <code><a href="rsync://hostname/">rsync://hostname/</a></code>. The default port used for connecting is 874 (one higher than the normal 873) unless overridden in the environment. You can specify an overriding port via <code>&#8211;port</code> or by including it in the normal spot in the URL format, though both of those require your rsync version to be at least 3.2.0. </p>
<h2>OPTIONS</h2>
<p> If the <code>first</code> arg is a <code>&#8211;type=SSL_TYPE</code> option, the script will only use that particular program to open an ssl connection instead of trying to find an openssl or stunnel executable via a simple heuristic (assuming that the <code>RSYNC_SSL_TYPE</code> environment variable is not set as well &#8212; see below). This option must specify one of <code>openssl</code> or <code>stunnel</code>. The equal sign is required for this particular option. </p>
<p> All the other options are passed through to the rsync command, so consult the <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1) manpage for more information on how it works. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The ssl helper scripts are affected by the following environment variables: </p>
<dl>
<dt><code>RSYNC_SSL_TYPE</code></p>
<dd> Specifies the program type that should be used to open the ssl connection. It must be one of <code>openssl</code> or <code>stunnel</code>. The <code>&#8211;type=SSL_TYPE</code> option overrides this, when specified.</p>
<dt><code>RSYNC_SSL_PORT</code></p>
<dd> If specified, the value is the port number that is used as the default when the user does not specify a port in their rsync command. When not specified, the default port number is 874. (Note that older rsync versions (prior to 3.2.0) did not communicate an overriding port number value to the helper script.)</p>
<dt><code>RSYNC_SSL_CERT</code></p>
<dd> If specified, the value is a filename that contains a certificate to use for the connection.</p>
<dt><code>RSYNC_SSL_KEY</code></p>
<dd> If specified, the value is a filename that contains a key for the provided certificate to use for the connection.</p>
<dt><code>RSYNC_SSL_CA_CERT</code></p>
<dd> If specified, the value is a filename that contains a certificate authority certificate that is used to validate the connection.</p>
<dt><code>RSYNC_SSL_OPENSSL</code></p>
<dd> Specifies the openssl executable to run when the connection type is set to openssl. If unspecified, the $PATH is searched for &quot;openssl&quot;.</p>
<dt><code>RSYNC_SSL_GNUTLS</code></p>
<dd> Specifies the gnutls-cli executable to run when the connection type is set to gnutls. If unspecified, the $PATH is searched for &quot;gnutls-cli&quot;.</p>
<dt><code>RSYNC_SSL_STUNNEL</code></p>
<dd> Specifies the stunnel executable to run when the connection type is set to stunnel. If unspecified, the $PATH is searched first for &quot;stunnel4&quot; and then for &quot;stunnel&quot;.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
rsync-ssl -aiv example.com::mod/ dest
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
rsync-ssl --type=openssl -aiv example.com::mod/ dest
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
rsync-ssl -aiv --port 9874 example.com::mod/ dest
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
rsync-ssl -aiv <a href="rsync://example.com:9874/mod/">rsync://example.com:9874/mod/</a> dest
</pre>
</dl>
<h2>THE SERVER SIDE</h2>
<p> For help setting up an SSL/TLS supporting rsync, see the instructions in rsyncd.conf. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1), <code><a href="/docs/linux/man/5-rsyncd-conf/">rsyncd.conf</a></code>(5) </p>
<h2>CAVEATS</h2>
<p> Note that using an stunnel connection requires at least version 4 of stunnel, which should be the case on modern systems. Also, it does not verify a connection against the CA certificate collection, so it only encrypts the connection without any cert validation unless you have specified the certificate environment options. </p>
<p> This script also supports a <code>&#8211;type=gnutls</code> option, but at the time of this release the gnutls-cli command was dropping output, making it unusable. If that bug has been fixed in your version, feel free to put gnutls into an exported RSYNC_SSL_TYPE environment variable to make its use the default. </p>
<h2>BUGS</h2>
<p> Please report bugs! See the web site at <a rel="nofollow" href="https://rsync.samba.org/.">https://rsync.samba.org/.</a> </p>
<h2>VERSION</h2>
<p> This manpage is current for version 3.2.7 of rsync. </p>
<h2>CREDITS</h2>
<p> Rsync is distributed under the GNU General Public License. See the file COPYING for details. </p>
<p> A web site is available at <a rel="nofollow" href="https://rsync.samba.org/.">https://rsync.samba.org/.</a> The site includes an FAQ-O-Matic which may cover questions unanswered by this manual page. </p>
<h2>AUTHOR</h2>
<p> This manpage was written by Wayne Davison. </p>
<p> Mailing lists for support and development are available at <a rel="nofollow" href="https://lists.samba.org/.">https://lists.samba.org/.</a> </p>
<h2>Index</h2>
