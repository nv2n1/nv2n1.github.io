---
title: "cimtrust(8)"
name: "cimtrust"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cimtrust/"
description: "cimtrust – Add, remove or list X509 certificates in a PEM format trust store."
---

<p>cimtrust &#8211; Add, remove or list X509 certificates in a PEM format trust store.</p>
<h2>Synopsis</h2>
<p><code>cimtrust</code> -a [ -U certuser ] -f file -T ( a | e | s ) <code>cimtrust </code> -r -i issuer ( -n serialnumber | -S subject ) <code>cimtrust </code> -l [ -i issuer [ -n serialnumber | -S subject ] ] <code>cimtrust </code> &#8211;help <code>cimtrust</code> &#8211;version</p>
<h3>Remarks</h3>
<p>The cimtrust command requires that the cimserver is running. This command operates on a truststore on the local system only. </p>
<h2>Description</h2>
<p>The add option of the cimtrust command adds an X509 certificate file of a specified type to the truststore. The certuser specifies the username to be associated with the certificate in the file. If no certuser is specified, the certificate may not be used to authenticate a user. </p>
<p> The remove option of the cimtrust command removes the X509 certificate(s) matching the specified <code>issuer </code> and either <code>serialnumber </code> or <code>subject </code> from the truststore. </p>
<p> The list option of the cimtrust command lists the X509 certificates in the truststore. The list can be filtered by <code>issuer </code> and either <code>serialnumber </code> or <code>subject. </code> </p>
<p> Certificates in the trust store may be revoked by adding a Certificate Revocation List to the CRL store. For more information on CRL operations see the <code><a href="/docs/linux/man/8-cimcrl/">cimcrl</a>(8)</code> command.</p>
<h3>Options</h3>
<p><code>cimtrust </code> recognizes the following options:</p>
<dl>
<dd>
</dd><dl>
<dt><code>-a</code></dt>
<dd>Adds a certificate to the truststore. If the specified <code>file </code> does not contain a valid X509 certificate an error message is returned and no action is taken. If the X509 certificate already exists in the truststore, an error message is returned.</dd>
<dt><code>-r</code></dt>
<dd>Removes certificate(s) from the truststore. If the truststore contains multiple certificates matching the specified <code>issuer </code> and <code>subject, </code> all the matching certificates are removed. If no certificate exists for the specified <code>issuer </code> and either <code>serialnumber </code> or <code>subject</code> , an error message is returned and no action is taken.</dd>
<dt><code>-l</code></dt>
<dd>Displays the X509 certificates in the truststore.</dd>
<dt><code>-f file</code></dt>
<dd>Specifies a PEM format file containing an X509 certificate.</dd>
<dt><code>-U certuser</code></dt>
<dd>Specifies a username to be associated with the specified certificate. The username specified should be a valid system user on the target system.</dd>
<dt><code>-i issuer</code></dt>
<dd>Specifies the issuer name of the certificate.</dd>
<dt><code>-n serialnumber</code></dt>
<dd>Specifies the serial number of the certificate.</dd>
<dt><code>-S subject</code></dt>
<dd>Specifies the subject name of the certificate.</dd>
<dt><code>-T ( a | e | s )</code></dt>
<dd>Specifies the type of a certificate. The type must be one of the following: </dd>
<p> authority (a): root/intermediate authority certificates. Certificates of this type are added to the trusted certificate store. The certuser is optional for authority certificates. If no certuser is specified, the certificate may not be used to authenticate a user. </p>
<p> authority issued end-entity (e): Certificates of this type are not added to the trusted certificate store. The certuser is required for authority issued end-entity certificates. </p>
<p> Self-signed identity certificate (s): Certificates of this type are added to the trusted certificate store. The certuser is required for self-signed identity certificates.</p>
<dt><code>&#8211;help</code></dt>
<dd>Displays the command help message.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Displays the CIM Server version.</dd></dl>
</dl>
<h2>Exit Status</h2>
<p>When an error occurs, an error message is written to the standard error stream and a non-zero exit status value is returned. The following exit status values are defined:</p>
<dl>
<dd>
</dd><dl>
<dt><code>0</code></dt>
<dd>Success</dd>
<dt><code>1</code></dt>
<dd>General error</dd>
<dt><code>2</code></dt>
<dd>Connection failed</dd>
<dt><code>3</code></dt>
<dd>Connection timed out</dd>
<dt><code>4</code></dt>
<dd>Certificate already exists</dd>
<dt><code>5</code></dt>
<dd>Certificate does not exist</dd>
<dt><code>6</code></dt>
<dd>Invalid system user</dd></dl>
</dl>
<h2>Examples</h2>
<p>Add the X509 self-signed identity certificate in the cert.pem file and associate it to certuser guest. This certificate will be added to the trusted certificate store: cimtrust -a -U guest -f cert.pem -T s Add the X509 authority root CA certificate in the ca.pem file with no certuser association. This certificate will be added to the trusted certificate store but may not be used to authenticate a user: cimtrust -a -f ca.pem -T a Add the X509 authority issued end-entity certificate in the user.pem file and associate it to certuser pegasus. This certificate may be used to authenticate user pegasus but will not be added to the trusted certificate store: cimtrust -a -f user.pem -U pegasus -T e Remove the certificate matching the specified issuer and serialnumber from the trust store: cimtrust -r -i &quot;/C=US/ST=California/L=Cupertino/O=Smart &amp; Secure/OU=Secure Software Division/CN=dev.admin.ss.com&quot; -n 01 Remove the certificate(s) matching the specified issuer and subject from the trust store:  List all the X509 certificates in the trust store: cimtrust -l </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-cimserver/">cimserver</a>(8), <a href="/docs/linux/man/8-cimcrl/">cimcrl</a>(8), <a href="/docs/linux/man/8-cimconfig/">cimconfig</a>(8). </p>
