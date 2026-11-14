---
title: "postfix-tls(1)"
name: "postfix-tls"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postfix-tls/"
description: "postfix-tls – Postfix TLS management"
---

<h2 class="name">NAME</h2>
<p> postfix-tls &#8211; Postfix TLS management </p>
<h2>SYNOPSIS</h2>
<pre>
<code>postfix tls</code> <i>subcommand</i>
</pre>
<h2>DESCRIPTION</h2>
<p> The &quot;<code>postfix tls </code><i>subcommand</i>&quot; feature enables opportunistic TLS in the Postfix SMTP client or server, and manages Postfix SMTP server private keys and certificates. </p>
<p> The following subcommands are available:</p>
<dl>
<dt><code>enable-client</code> [<code>-r </code><i>randsource</i>]</p>
<dd> Enable opportunistic TLS in the Postfix SMTP client, if all SMTP client TLS settings are at their default values. Otherwise, suggest parameter settings without making any changes. </p>
<p> Specify <i>randsource</i> to update the value of the <code>tls_random_source</code> configuration parameter (typically, /dev/urandom). Prepend <code>dev:</code> to device paths or <code>egd:</code> to EGD socket paths. </p>
<p> See also the <code>all-default-client</code> subcommand.</p>
<dt><code>enable-server</code> [<code>-r </code><i>randsource</i>] [<code>-a </code><i>algorithm</i>] [<code>-b </code><i>bits</i>] [<i>hostname</i><code>&#8230;</code>]</p>
<dd> Create a new private key and self-signed server certificate and enable opportunistic TLS in the Postfix SMTP server, if all SMTP server TLS settings are at their default values. Otherwise, suggest parameter settings without making any changes. </p>
<p> The <i>randsource</i> parameter is as with <code>enable-client</code> above, and the remaining options are as with <code>new-server-key</code> below. </p>
<p> See also the <code>all-default-server</code> subcommand.</p>
<dt><code>new-server-key</code> [<code>-a </code><i>algorithm</i>] [<code>-b </code><i>bits</i>] [<i>hostname</i><code>&#8230;</code>]</p>
<dd> Create a new private key and self-signed server certificate, but do not deploy them. Log and display commands to deploy the new key and corresponding certificate. Also log and display commands to output a corresponding CSR or TLSA records which may be needed to obtain a CA certificate or to update DNS before the new key can be deployed. </p>
<p> The <i>algorithm</i> defaults to <code>rsa</code>, and <i>bits</i> defaults to 2048. If you choose the <code>ecdsa</code> <i>algorithm</i> then <i>bits</i> will be an EC curve name (by default <code>secp256r1</code>, also known as prime256v1). Curves other than <code>secp256r1</code>, <code>secp384r1</code> or <code>secp521r1</code> are unlikely to be widely interoperable. When generating EC keys, use one of these three. DSA keys are obsolete and are not supported. </p>
<p> Note: ECDSA support requires OpenSSL 1.0.0 or later and may not be available on your system. Not all client systems will support ECDSA, so you&#8217;ll generally want to deploy both RSA and ECDSA certificates to make use of ECDSA with compatible clients and RSA with the rest. If you want to deploy certificate chains with intermediate CAs for both RSA and ECDSA, you&#8217;ll want at least OpenSSL 1.0.2, as earlier versions may not handle multiple chain files correctly. </p>
<p> The first <i>hostname</i> argument will be the <code>CommonName</code> of both the subject and issuer of the self-signed certificate. It, and any additional <i>hostname</i> arguments, will also be listed as DNS alternative names in the certificate. If no <i>hostname</i> is provided the value of the <code>myhostname</code> main.cf parameter will be used. </p>
<p> For RSA, the generated private key and certificate files are named <code>key-</code><i>yyyymmdd-hhmmss</i><code>.pem</code> and <code>cert-</code><i>yyyymmdd-hhmmss</i><code>.pem</code>, where <i>yyyymmdd</i> is the calendar date and <i>hhmmss</i> is the time of day in UTC. For ECDSA, the file names start with <code>eckey-</code> and <code>eccert-</code> instead of <code>key-</code> and <code>cert-</code> respectively. </p>
<p> Before deploying the new key and certificate with DANE, update the DNS with new DANE TLSA records, then wait for secondary nameservers to update and then for stale records in remote DNS caches to expire. </p>
<p> Before deploying a new CA certificate make sure to include all the required intermediate issuing CA certificates in the certificate chain file. The server certificate must be the first certificate in the chain file. Overwrite and deploy the file with the original self-signed certificate that was generated together with the key.</p>
<dt><code>new-server-cert</code> [<code>-a </code><i>algorithm</i>] [<code>-b </code><i>bits</i>] [<i>hostname</i><code>&#8230;</code>]</p>
<dd> This is just like <code>new-server-key</code> except that, rather than generating a new private key, any currently deployed private key is copied to the new key file. Thus if you&#8217;re publishing DANE TLSA &quot;3 1 1&quot; or &quot;3 1 2&quot; records, there is no need to update DNS records. The <i>algorithm</i> and <i>bits</i> arguments are used only if no key of the same algorithm is already configured. </p>
<p> This command is rarely needed, because the self-signed certificates generated have a 100-year nominal expiration time. The underlying public key algorithms may well be obsoleted by quantum computers long before then. </p>
<p> The most plausible reason for using this command is when the system hostname changes, and you&#8217;d like the name in the certificate to match the new hostname (not required for DANE &quot;3 1 1&quot;, but some needlessly picky non-DANE opportunistic TLS clients may log warnings or even refuse to communicate).</p>
<dt><code>deploy-server-cert </code><i>certfile</i><i>keyfile</i></p>
<dd> This subcommand deploys the certificates in <i>certfile</i> and private key in <i>keyfile</i> (which are typically generated by the commands above, which will also log and display the full command needed to deploy the generated key and certificate). After the new certificate and key are deployed any obsolete keys and certificates may be removed by hand. The <i>keyfile</i> and <i>certfile</i> filenames may be relative to the Postfix configuration directory.</p>
<dt><code>output-server-csr</code> [<code>-k </code><i>keyfile</i>] [<i>hostname</i><code>&#8230;</code>]</p>
<dd> Write to stdout a certificate signing request (CSR) for the specified <i>keyfile</i>. </p>
<p> Instead of an absolute pathname or a pathname relative to $config_directory, <i>keyfile</i> may specify one of the supported key algorithm names (see &quot;<code>postconf -T public-key-algorithms</code>&quot;). In that case, the corresponding setting from main.cf is used to locate the <i>keyfile</i>. The default <i>keyfile</i> value is <code>rsa</code>. </p>
<p> Zero or more <i>hostname</i> values can be specified. The default <i>hostname</i> is the value of <code>myhostname</code> main.cf parameter.</p>
<dt><code>output-server-tlsa</code> [<code>-h </code><i>hostname</i>] [<i>keyfile</i><code>&#8230;</code>]</p>
<dd> Write to stdout a DANE TLSA RRset suitable for a port 25 SMTP server on host <i>hostname</i> with keys from any of the specified <i>keyfile</i> values. The default <i>hostname</i> is the value of the <code>myhostname</code> main.cf parameter. </p>
<p> Instead of absolute pathnames or pathnames relative to $config_directory, the <i>keyfile</i> list may specify names of supported public key algorithms (see &quot;<code>postconf -T public-key-algorithms</code>&quot;). In that case, the actual <i>keyfile</i> list uses the values of the corresponding Postfix server TLS key file parameters. If a parameter value is empty or equal to <code>none</code>, then no TLSA record is output for that algorithm. </p>
<p> The default <i>keyfile</i> list consists of the two supported algorithms <code>rsa</code> and <code>ecdsa</code>.</dl>
<h2>AUXILIARY COMMANDS</h2>
<pre><code>

all - default - clientExit with status 0(success) if all SMTP client TLS settings are at their default values.Otherwise, exit with a non - zero status.This is typically used as follows : postfix tls all - default - client &amp;&amp;postfix tls enable - client all - default - serverExit with status 0(success) if all SMTP server TLS settings are at their default values.Otherwise, exit with a non - zero status.This is typically used as follows : postfix tls all - default - server &amp;&amp;postfix tls enable - server
</code></pre>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The &quot;<code>postfix tls </code><i>subcommand</i>&quot; feature reads or updates the following configuration parameters.</p>
<dl>
<dt><code>command_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of all postfix administrative commands.</p>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>openssl_path (openssl)</code></p>
<dd> The location of the OpenSSL command line program <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1).</p>
<dt><code>smtp_tls_loglevel (0)</code></p>
<dd> Enable additional Postfix SMTP client logging of TLS activity.</p>
<dt><code>smtp_tls_security_level (empty)</code></p>
<dd> The default SMTP TLS security level for the Postfix SMTP client; when a non-empty value is specified, this overrides the obsolete parameters smtp_use_tls, smtp_enforce_tls, and smtp_tls_enforce_peername.</p>
<dt><code>smtp_tls_session_cache_database (empty)</code></p>
<dd> Name of the file containing the optional Postfix SMTP client TLS session cache.</p>
<dt><code>smtpd_tls_cert_file (empty)</code></p>
<dd> File with the Postfix SMTP server RSA certificate in PEM format.</p>
<dt><code>smtpd_tls_eccert_file (empty)</code></p>
<dd> File with the Postfix SMTP server ECDSA certificate in PEM format.</p>
<dt><code>smtpd_tls_eckey_file ($smtpd_tls_eccert_file)</code></p>
<dd> File with the Postfix SMTP server ECDSA private key in PEM format.</p>
<dt><code>smtpd_tls_key_file ($smtpd_tls_cert_file)</code></p>
<dd> File with the Postfix SMTP server RSA private key in PEM format.</p>
<dt><code>smtpd_tls_loglevel (0)</code></p>
<dd> Enable additional Postfix SMTP server logging of TLS activity.</p>
<dt><code>smtpd_tls_received_header (no)</code></p>
<dd> Request that the Postfix SMTP server produces Received: message headers that include information about the protocol and cipher used, as well as the remote SMTP client CommonName and client certificate issuer CommonName.</p>
<dt><code>smtpd_tls_security_level (empty)</code></p>
<dd> The SMTP TLS security level for the Postfix SMTP server; when a non-empty value is specified, this overrides the obsolete parameters smtpd_use_tls and smtpd_enforce_tls.</p>
<dt><code>tls_random_source (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The external entropy source for the in-memory <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) pseudo random number generator (PRNG) pool.</dl>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8) Postfix master program
<a href="//www.systutorials.com/docs/linux/man/1-postfix/">postfix</a>(1) Postfix administrative interface
</pre>
<h2>README FILES</h2>
<p> Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>
TLS_README, Postfix TLS configuration and operation
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>HISTORY</h2>
<p> The &quot;<code>postfix tls</code>&quot; command was introduced with Postfix version 3.1.</p>
<h2>AUTHOR(S)</h2>
<pre>
Viktor Dukhovni
</pre>
<h2>Index</h2>
