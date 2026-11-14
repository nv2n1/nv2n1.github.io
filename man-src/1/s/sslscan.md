---
title: "sslscan(1)"
name: "sslscan"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sslscan/"
description: "sslscan – Fast SSL/TLS scanner"
---

<h2>NAME</h2>
<p> sslscan &#8211; Fast SSL/TLS scanner</p>
<h2>SYNOPSIS</h2>
<p> <code>sslscan</code> [<i>options</i>]<i> [host:port | host]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>sslscan</code> command </p>
<p> <code>sslscan</code> queries SSL/TLS services, such as HTTPS, in order to determine the ciphers that are supported.<br />
 SSLScan is designed to be easy, lean and fast. The output includes preferred ciphers of the SSL/TLS service,<br />
 the certificate and output is in text and XML formats. It is TLS SNI aware when used with a supported version of OpenSSL.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>
 Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>&#8211;targets=&lt;file&gt;</code></p>
<dd> A file containing a list of hosts to check. Hosts can be supplied with ports (i.e. host:port). One target per line.</p>
<dt><code>&#8211;no-failed</code></p>
<dd> List only accepted ciphers (default is to listing all ciphers).</p>
<dt><code>&#8211;ssl2</code></p>
<dd>
 Only check SSLv2 ciphers.</p>
<dt><code>&#8211;ssl3</code></p>
<dd>
 Only check SSLv3 ciphers.</p>
<dt><code>&#8211;tls1</code></p>
<dd>
 Only check TLSv1 ciphers.</p>
<dt><code>&#8211;tls11</code></p>
<dd>
 Only check TLSv11 ciphers.</p>
<dt><code>&#8211;tls12</code></p>
<dd>
 Only check TLSv12 ciphers.</p>
<dt><code>&#8211;pk=&lt;file&gt;</code></p>
<dd> A file containing the private key or a PKCS#12 file containing a private key/certificate pair (as produced by MSIE and Netscape).</p>
<dt><code>&#8211;pkpass=&lt;password&gt;</code></p>
<dd> The password for the private key or PKCS#12 file.</p>
<dt><code>&#8211;certs=&lt;file&gt;</code></p>
<dd> A file containing PEM/ASN1 formatted client certificates.</p>
<dt><code>&#8211;renegotiation</code></p>
<dd> Attempt TLS renegotiation</p>
<dt><code>&#8211;starttls-ftp</code></p>
<dd> STARTTLS setup for FTP</p>
<dt><code>&#8211;starttls-imap</code></p>
<dd> STARTTLS setup for IMAP</p>
<dt><code>&#8211;starttls-pop3</code></p>
<dd> STARTTLS setup for POP3</p>
<dt><code>&#8211;starttls-smtp</code></p>
<dd> STARTTLS setup for SMTP</p>
<dt><code>&#8211;starttls-xmpp</code></p>
<dd> STARTTLS setup for XMPP</p>
<dt><code>&#8211;html</code></p>
<dd> Makes a HTML request after a successful connection and returns the server response code.</p>
<dt><code>&#8211;bugs</code></p>
<dd> Enables workarounds for SSL bugs.</p>
<dt><code>&#8211;xml=&lt;file&gt;</code></p>
<dd> Output results to an XML file.
</dl>
<h2>AUTHOR</h2>
<p> sslscan was originally written by Ian Ventura-Whiting &lt;fizz [at] titania.co.uk&gt;. sslscan was extended by Jacob Appelbaum &lt;jacob [at] appelbaum.net&gt;.<br />
 This manual page was originally written by Marvin Stark &lt;marv [at] der-marv.de&gt;. </p>
<h2>Index</h2>
