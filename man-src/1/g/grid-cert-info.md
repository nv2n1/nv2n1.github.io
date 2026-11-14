---
title: "grid-cert-info(1)"
name: "grid-cert-info"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-cert-info/"
description: "grid-cert-info – Display information about a certificate"
---

<h2 class="name">NAME</h2>
<p> grid-cert-info &#8211; Display information about a certificate </p>
<h2>SYNOPSIS</h2>
<p> <code>grid-cert-info</code> <i>-help</i> | <i>-usage</i> | <i>-version</i> | <i>-versions</i> </p>
<p> <code>grid-cert-info</code> OPTIONS</p>
<h2>DESCRIPTION</h2>
<p> The <code>grid-cert-info</code> program displays information contained within a certificate file. By default it shows a text representation of the entire certificate. Specific facts about the certificate can be shown instead by using command-line options. If any of those options are used, then the default display is suppressed. This can be added to the output by using the <i>-all</i> command-line option. </p>
<p> If multiple display options are included on the command-line, the facts related to those will be displayed on separate lines in the order that they occur. If an option is specified multiple time, that fact will be displayed multiple times.</p>
<h2>OPTIONS</h2>
<p> The full set of command-line options to <code>grid-cert-info</code> are: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Display the command-line options to <code>grid-cert-info</code> and exit.</dl>
<p> <code>-version, -versions</code></p>
<dl>
<dt>
<dd> Display the version number of the <code>grid-cert-info</code> command. The second form includes more details.</dl>
<p> <code>-file </code><i>CERTIFICATE-FILE</i></p>
<dl>
<dt>
<dd> Display information about the first certificate contained in the file named by <i>CERTIFICATE-FILE</i> instead of the default user certificate.</dl>
<p> <code>-rfc2253</code></p>
<dl>
<dt>
<dd> Display X.509 distinguished names using the string representation defined in RFC 2253 instead of the default OpenSSL <i>oneline</i> format.</dl>
<p> <code>-all</code></p>
<dl>
<dt>
<dd> Display the text representation of the entire certificate in addition to any other facts requested by command-line options. This is the default if no fact-specific command-line options are used.</dl>
<p> <code>-subject, -s</code></p>
<dl>
<dt>
<dd> Display the subject name of the X.509 certificate.</dl>
<p> <code>-issuer, -i</code></p>
<dl>
<dt>
<dd> Display the issuer name of the X.509 certificate.</dl>
<p> <code>-issuerhash, -ih</code></p>
<dl>
<dt>
<dd> Display the default hash of the issuer name of the X.509 certificate. This can be used to locate which CA certificate in the trusted certificate directory issued the certificate being inspected.</dl>
<p> <code>-startdate, -sd</code></p>
<dl>
<dt>
<dd> Display a string representation of the date and time when the certificate is valid from. This is displayed in the format used by the OpenSSL <code>x509</code> command.</dl>
<p> <code>-enddate, -ed</code></p>
<dl>
<dt>
<dd> Display a string representation of the date and time when the certificate is valid until. This is displayed in the format used by the OpenSSL <code>x509</code> command.</dl>
<h2>EXAMPLES</h2>
<p> Display the validity times for the default certificate </p>
<dl>
<dt>
<dd>
<pre>
% grid-cert-info -sd -ed
Aug 31 12:33:47 2009 GMT
Aug 31 12:33:47 2010 GMT
</pre>
</dl>
<p> Display the same information about a different certificate specified on the command-line </p>
<dl>
<dt>
<dd>
<pre>
% grid-cert-info -sd -ed -f /etc/grid-security/hostcert.pem
Jan 21 12:24:48 2003 GMT
Jul 15 11:30:57 2020 GMT
</pre>
</dl>
<p> Display the subject of a certificate in both the default and the RFC 2253 forms. </p>
<dl>
<dt>
<dd>
<pre>
% grid-cert-info -subject
/DC=org/DC=example/DC=grid/CN=Joe User
% grid-cert-info -subject -rfc2253
CN=Joe User,DC=grid,DC=example,DC=org
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>grid-cert-info</code>: </p>
<p> <code>X509_USER_CERT</code></p>
<dl>
<dt>
<dd> Path to the default certificate file to inspect.</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
