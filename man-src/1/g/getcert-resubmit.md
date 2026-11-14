---
title: "getcert-resubmit(1)"
name: "getcert-resubmit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcert-resubmit/"
description: "getcert"
---

<h2 class="name">NAME</h2>
<p> getcert</p>
<h2>SYNOPSIS</h2>
<p> getcert resubmit [options] </p>
<h2>DESCRIPTION</h2>
<p> Tells <i>certmonger</i> to generate (or regenerate) a signing request and submit (or resubmit) the signing request to a CA for signing. </p>
<h2>SPECIFYING REQUESTS BY NICKNAME</h2>
<dl>
<dt><code>-i</code> NAME</p>
<dd> Resubmit a signing request for the tracking request which has this nickname. If this option is not specified, and a tracking entry which matches the key and certificate storage options which are specified already exists, that entry will be used. If not specified, the location of the certificate should be specified with either a combination of the <code>-d</code> and <code>-n</code> options, or with the <code>-f</code> option. </p>
</dl>
<h2>SPECIFYING REQUESTS BY CERTIFICATE LOCATION</h2>
<dl>
<dt><code>-d</code> DIR</p>
<dd> The certificate is in the NSS database in the specified directory.</p>
<dt><code>-n</code> NAME</p>
<dd> The certificate in the NSS database named with <code>-d</code> has the specified nickname. Only valid with <code>-d</code>.</p>
<dt><code>-t</code> TOKEN</p>
<dd> If the NSS database has more than one token available, the certificate is stored in this token. This argument only rarely needs to be specified. Only valid with <code>-d</code>.</p>
<dt><code>-f</code> FILE</p>
<dd> The certificate is stored in the named file. </p>
</dl>
<h2>ENROLLMENT OPTIONS</h2>
<dl>
<dt><code>-c</code> NAME</p>
<dd> Submit the new signing request to the specified CA rather than the one which was previously associated with this certificate. The name of the CA should correspond to one listed by <i>getcert list-cas</i>.</p>
<dt><code>-T</code> NAME</p>
<dd> Request a certificate using the named profile, template, or certtype, from the specified CA.</p>
<dt><code>-X</code> NAME</p>
<dd> Request a certificate using the named issuer from the specified CA.</p>
<dt><code>-I</code> NAME</p>
<dd> Assign the specified nickname to this task, replacing the previous nickname. </p>
</dl>
<h2>SIGNING REQUEST OPTIONS</h2>
<dl>
<dt><code>-N</code> NAME</p>
<dd> Change the subject name to include in the signing request.</p>
<dt><code>-u</code> keyUsage</p>
<dd> Add an extensionRequest for the specified keyUsage to the signing request. The keyUsage value is expected to be one of these names: </p>
<p> digitalSignature </p>
<p> nonRepudiation </p>
<p> keyEncipherment </p>
<p> dataEncipherment </p>
<p> keyAgreement </p>
<p> keyCertSign </p>
<p> cRLSign </p>
<p> encipherOnly </p>
<p> decipherOnly</p>
<dt><code>-U</code> EKU</p>
<dd> Change the extendedKeyUsage value specified in an extendedKeyUsage extension part of the extensionRequest attribute in the signing request. The EKU value is expected to be an object identifier (OID).</p>
<dt><code>-K</code> NAME</p>
<dd> Change the Kerberos principal name specified as part of a subjectAltName extension part of the extensionRequest attribute in the signing request.</p>
<dt><code>-E</code> EMAIL</p>
<dd> Change the email address specified as part of a subjectAltName extension part of the extensionRequest attribute in the signing request.</p>
<dt><code>-D</code> DNSNAME</p>
<dd> Change the DNS name specified as part of a subjectAltName extension part of the extensionRequest attribute in the signing request.</p>
<dt><code>-A</code> ADDRESS</p>
<dd> Change the IP address specified as part of a subjectAltName extension part of the extensionRequest attribute in the signing request.</p>
<dt><code>-l</code> FILE</p>
<dd> Add an optional ChallengePassword value, read from the file, to the signing request. A ChallengePassword is often required when the CA is accessed using SCEP.</p>
<dt><code>-L</code> PIN</p>
<dd> Add the argument value to the signing request as a ChallengePassword attribute. A ChallengePassword is often required when the CA is accessed using SCEP. </p>
</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-B</code> COMMAND</p>
<dd> When ever the certificate or the CA&#8217;s certificates are saved to the specified locations, run the specified command as the client user before saving the certificates.</p>
<dt><code>-C</code> COMMAND</p>
<dd> When ever the certificate or the CA&#8217;s certificates are saved to the specified locations, run the specified command as the client user after saving the certificates.</p>
<dt><code>-a</code> DIR</p>
<dd> When ever the certificate is saved to the specified location, if root certificates for the CA are available, save them to the specified NSS database.</p>
<dt><code>-F</code> FILE</p>
<dd> When ever the certificate is saved to the specified location, if root certificates for the CA are available, and when the local copies of the CA&#8217;s root certificates are updated, save them to the specified file.</p>
<dt><code>-w</code></p>
<dd> Wait for the certificate to be reissued and saved, or for the attempt to obtain one to fail.</p>
<dt><code>-v</code></p>
<dd> Be verbose about errors. Normally, the details of an error received from the daemon will be suppressed if the client can make a diagnostic suggestion. </p>
</dl>
<h2>BUGS</h2>
<p> Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh/">getcert-refresh</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
<h2>Index</h2>
