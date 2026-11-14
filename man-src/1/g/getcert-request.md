---
title: "getcert-request(1)"
name: "getcert-request"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcert-request/"
description: "getcert"
---

<h2 class="name">NAME</h2>
<p> getcert</p>
<h2>SYNOPSIS</h2>
<p> getcert request [options] </p>
<h2>DESCRIPTION</h2>
<p> Tells <i>certmonger</i> to use an existing key pair (or to generate one if one is not already found in the specified location), to generate a signing request using the key pair, and to submit them for signing to a CA. </p>
<h2>KEY AND CERTIFICATE STORAGE OPTIONS</h2>
<dl>
<dt><code>-d</code> DIR</p>
<dd> Use an NSS database in the specified directory for storing this certificate and key.</p>
<dt><code>-n</code> NAME</p>
<dd> Use the key with this nickname to generate the signing request. If no such key is found, generate one. Give the enrolled certificate this nickname, too. Only valid with <code>-d</code>.</p>
<dt><code>-t</code> TOKEN</p>
<dd> If the NSS database has more than one token available, use the token with this name for storing and accessing the certificate and key. This argument only rarely needs to be specified. Only valid with <code>-d</code>.</p>
<dt><code>-f</code> FILE</p>
<dd> Store the issued certificate in this file. For safety&#8217;s sake, do not use the same file specified with the <code>-k</code> option.</p>
<dt><code>-k</code> FILE</p>
<dd> Use the key stored in this file to generate the signing request. If no such file is found, generate a new key pair and store them in the file. Only valid with <code>-f</code>. </p>
</dl>
<h2>KEY ENCRYPTION OPTIONS</h2>
<dl>
<dt><code>-p</code> FILE</p>
<dd> Encrypt private key files or databases using the PIN stored in the named file as the passphrase.</p>
<dt><code>-P</code> PIN</p>
<dd> Encrypt private key files or databases using the specified PIN as the passphrase. Because command-line arguments to running processes are trivially discoverable, use of this option is not recommended except for testing. </p>
</dl>
<h2>KEY GENERATION OPTIONS</h2>
<dl>
<dt><code>-G</code> TYPE</p>
<dd> In case a new key pair needs to be generated, this option specifies the type of the keys to be generated. If not specified, a reasonable default (currently <i>RSA</i>) will be used.</p>
<dt><code>-g</code> BITS</p>
<dd> In case a new key pair needs to be generated, this option specifies the size of the key. If not specified, a reasonable default (currently 2048 bits) will be used. </p>
</dl>
<h2>TRACKING OPTIONS</h2>
<dl>
<dt><code>-r</code></p>
<dd> Attempt to obtain a new certificate from the CA when the expiration date of a certificate nears. This is the default setting.</p>
<dt><code>-R</code></p>
<dd> Don&#8217;t attempt to obtain a new certificate from the CA when the expiration date of a certificate nears. If this option is specified, an expired certificate will simply stay expired.</p>
<dt><code>-I</code> NAME</p>
<dd> Assign the specified nickname to this task. If this option is not specified, a name will be assigned automatically. </p>
</dl>
<h2>ENROLLMENT OPTIONS</h2>
<dl>
<dt><code>-c</code> NAME</p>
<dd> Enroll with the specified CA rather than a possible default. The name of the CA should correspond to one listed by <i>getcert list-cas</i>.</p>
<dt><code>-T</code> NAME</p>
<dd> Request a certificate using the named profile, template, or certtype, from the specified CA.</p>
<dt><code>-X</code> NAME</p>
<dd> Request a certificate using the named issuer from the specified CA. </p>
</dl>
<h2>SIGNING REQUEST OPTIONS</h2>
<p> If none of <code>-N</code>, <code>-U</code>, <code>-K</code>, <code>-E</code>, and <code>-D</code> are specified, a default group of settings will be used to request an SSL server certificate for the current host, with the <i>host</i> Kerberos service as an additional name. </p>
<dl>
<dt><code>-N</code> NAME</p>
<dd> Set the subject name to include in the signing request. The default used is CN=<i>hostname</i>, where <i>hostname</i> is the local hostname.</p>
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
<dd> Add an extensionRequest for the specified extendedKeyUsage to the signing request. The EKU value is expected to be an object identifier (OID), but some specific names are also recognized. These are some names and their associated OID values: </p>
<p> id-kp-serverAuth 1.3.6.1.5.5.7.3.1 </p>
<p> id-kp-clientAuth 1.3.6.1.5.5.7.3.2 </p>
<p> id-kp-codeSigning 1.3.6.1.5.5.7.3.3 </p>
<p> id-kp-emailProtection 1.3.6.1.5.5.7.3.4 </p>
<p> id-kp-timeStamping 1.3.6.1.5.5.7.3.8 </p>
<p> id-kp-OCSPSigning 1.3.6.1.5.5.7.3.9 </p>
<p> id-pkinit-KPClientAuth 1.3.6.1.5.2.3.4 </p>
<p> id-pkinit-KPKdc 1.3.6.1.5.2.3.5 </p>
<p> id-ms-kp-sc-logon 1.3.6.1.4.1.311.20.2.2</p>
<dt><code>-K</code> NAME</p>
<dd> Add an extensionRequest for a subjectAltName, with the specified Kerberos principal name as its value, to the signing request.</p>
<dt><code>-E</code> EMAIL</p>
<dd> Add an extensionRequest for a subjectAltName, with the specified email address as its value, to the signing request.</p>
<dt><code>-D</code> DNSNAME</p>
<dd> Add an extensionRequest for a subjectAltName, with the specified DNS name as its value, to the signing request.</p>
<dt><code>-A</code> ADDRESS</p>
<dd> Add an extensionRequest for a subjectAltName, with the specified IP address as its value, to the signing request.</p>
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
<dd> Wait for the certificate to be issued and saved, or for the attempt to obtain one to fail.</p>
<dt><code>-v</code></p>
<dd> Be verbose about errors. Normally, the details of an error received from the daemon will be suppressed if the client can make a diagnostic suggestion. </p>
</dl>
<h2>NOTES</h2>
<p> Locations specified for key and certificate storage need to be accessible to the <i>certmonger</i> daemon process. When run as a system daemon on a system which uses a mandatory access control mechanism such as SELinux, the system policy must ensure that the daemon is allowed to access the locations where certificates and keys that it will manage will be stored (these locations are typically labeled as <i>cert_t</i> or an equivalent). More SELinux-specific information can be found in the <i>selinux.txt</i> documentation file for this package. </p>
<h2>BUGS</h2>
<p> Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh/">getcert-refresh</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
<h2>Index</h2>
