---
title: "certmonger-conf(5)"
name: "certmonger-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-certmonger-conf/"
description: "certmonger.conf – configuration file for certmonger"
---

<p>certmonger.conf &#8211; configuration file for certmonger</p>
<h2>Description</h2>
<p>The <i>certmonger.conf</i> file contains default settings used by certmonger. Its format is more or less that of a typical INI-style file. The only sections currently of note are named <i>defaults</i> and <i>selfsign</i>. </p>
<h2>Defaults</h2>
<p>Within the <i>defaults</i> section, these variables and values are recognized: </p>
<dl>
<dt>notify_ttls</p>
<dd>This is the list of times, given in seconds, before a certificate&#8217;s not-after validity date (often referred to as its expiration time) when <i>certmonger</i> should warn that the certificate will soon no longer be valid. If this value is not specified, <i>certmonger</i> will attempt to use the value of the <i>ttls</i> setting. The default list of values is &quot;2419200, 604800, 259200, 172800, 86400&quot;. </p>
<dt>enroll_ttls</p>
<dd>This is the list of times, given in seconds, before a certificate&#8217;s not-after validity date (often referred to as its expiration time) when <i>certmonger</i> should attempt to automatically renew the certificate, if it is configured to do so. If this value is not specified, <i>certmonger</i> will attempt to use the value of the <i>ttls</i> setting. The default list of values is &quot;2419200, 604800, 259200, 172800, 86400&quot;. </p>
<dt>notification_method</p>
<dd>This is the method by which <i>certmonger</i> will notify the system administrator that a certificate will soon become invalid. The recognized values are <i>syslog</i>, <i>mail</i>, and <i>command</i>. The default is <i>syslog</i>. When sending mail, the notification message will be the mail message subject. When invoking a command, the notification message will be available in the &quot;CERTMONGER_NOTIFICATION&quot; environment variable. </p>
<dt>notification_destination</p>
<dd>This is the destination to which <i>certmonger</i> will send notifications. It can be a syslog priority and/or facility, separated by a period, it can be an email address, or it can be a command to run. The default value is <i>daemon.notice</i>. </p>
<dt>key_type</p>
<dd>This is the type of key pair which will be generated, used in certificate signing requests, and used when self-signing certificates. <i>RSA</i> and <i>DSA</i> are supported. <i>EC</i> (also known as <i>ECDSA</i>) is also supported. The default is <i>RSA</i>. </p>
<dt>symmetric_cipher</p>
<dd>This is the symmetric cipher which will be used to encrypt private keys stored in OpenSSL&#8217;s PEM format. Recognized values include <i>aes128</i> and <i>aes256</i>. The default is <i>aes128</i>. It is not recommended that this value be changed except in cases where the default is incompatible with other software. </p>
<dt>digest</p>
<dd>This is the digest algorithm which will be used when signing certificate signing requests and self-signed certificates. Recognized values include <i>sha1</i>, <i>sha256</i>, <i>sha384</i>, and <i>sha512</i>. The default is <i>sha256</i>. It is not recommended that this value be changed except in cases where the default is incompatible with other software. </p>
<dt>nss_ca_trust</p>
<dd>These are the trust attributes which are applied to CA certificates which should be trusted, when they are saved to NSS databases. The default is <i>CT,C,C</i>. </p>
<dt>nss_other_trust</p>
<dd>These are the trust attributes which are applied to certificates which are not necessarily to be trusted, when they are saved to NSS databases. The default is <i>,,</i>. </p>
</dl>
<h2>Selfsign</h2>
<p>Within the <i>selfsign</i> section, these variables and values are recognized: </p>
<dl>
<dt>validity_period</p>
<dd>This is the validity period given to self-signed certificates. The value is specified as a combination of years (y), months (M), weeks (w), days (d), hours (h), minutes (m), and/or seconds (s). If no unit of time is specified, seconds are assumed. The default value is <i>1y</i>. </p>
<dt>populate_unique_id</p>
<dd>This controls whether or not self-signed certificates will have their subjectUniqueID and issuerUniqueID fields populated. While RFC5280 prohibits their use, they may be needed and/or used by older applications. The default value is <i>no</i>. </p>
</dl>
<h2>Local</h2>
<p>Within the <i>local</i> section, these variables and values are recognized: </p>
<dl>
<dt>validity_period</p>
<dd>This is the validity period given to the locally-signed CA&#8217;s certificate when it is generated. The value is specified as a combination of years (y), months (M), weeks (w), days (d), hours (h), minutes (m), and/or seconds (s). If no unit of time is specified, seconds are assumed. If not set, the value of the <i>validity_period</i> setting from the <i>selfsign</i> section, if one is set there, will be used. The default value is <i>1y</i>. </p>
</dl>
<h2>Bugs</h2>
<p>Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
