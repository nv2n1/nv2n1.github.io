---
title: "cimcrl(8)"
name: "cimcrl"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cimcrl/"
description: "cimcrl – Add, remove or list X509 Certificate Revocation Lists in a PEM format CRL store."
---

<p>cimcrl &#8211; Add, remove or list X509 Certificate Revocation Lists in a PEM format CRL store.</p>
<h2>Synopsis</h2>
<p><code>cimcrl</code> -a -f file <code>cimcrl </code> -r -i issuer <code>cimcrl </code> -l [ -i issuer ] <code>cimcrl </code> &#8211;help <code>cimcrl</code> &#8211;version</p>
<h3>Remarks</h3>
<p>The cimcrl command requires that the cimserver is running. This command operates on a CRL store on the local system only. </p>
<h2>Description</h2>
<p>The cimcrl command provides a command line interface to manage X509 CRLs in the CRL store. The CRL store contains the CRLs used to revoke certificates in the CIM Server truststore. For more information on truststore operations see the <a href="/docs/linux/man/8-cimtrust/">cimtrust</a>(8) command. </p>
<p> The add option of the cimcrl command adds an X509 CRL from the specified file to the CRL store. If a CRL for the specified issuer already exists in the CRL store, the CRL is replaced with the specified CRL. </p>
<p> The remove option of the cimcrl command removes the X509 CRL matching the specified <code>issuer </code> from the CRL store. </p>
<p> The list option of the cimcrl command lists the X509 CRLs in the CRL store. The list can be filtered by <code>issuer. </code></p>
<h3>Options</h3>
<p><code>cimcrl </code> recognizes the following options:</p>
<dl>
<dd>
<dl>
<dt><code>-a</code></p>
<dd>Adds a CRL to the truststore. If the specified <code>file </code> does not contain a valid X509 CRL an error message is returned and no action is taken. If the CRL for the specified issuer already exists in the CRL store, it is replaced with the CRL in the specified <code>file</code></p>
<dt><code>-r</code></p>
<dd>Removes a CRL from the truststore. If no CRL exists for the specified <code>issuer </code> , an error message is returned and no action is taken.</p>
<dt><code>-l</code></p>
<dd>Displays the X509 CRLs in the truststore.</p>
<dt><code>-f file</code></p>
<dd>Specifies a PEM format file containing an X509 CRL.</p>
<dt><code>-i issuer</code></p>
<dd>Specifies the issuer name of the CRL.</p>
<dt><code>&#8211;help</code></p>
<dd>Displays the command help message.</p>
<dt><code>&#8211;version</code></p>
<dd>Displays the CIM Server version.</dl>
</dl>
<h2>Exit Status</h2>
<p>When an error occurs, an error message is written to the standard error stream and a non-zero exit status value is returned. The following exit status values are defined:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>Success</p>
<dt><code>1</code></p>
<dd>General error</p>
<dt><code>2</code></p>
<dd>Connection failed</p>
<dt><code>3</code></p>
<dd>Connection timed out</p>
<dt><code>4</code></p>
<dd>CRL does not exist</dl>
</dl>
<h2>Examples</h2>
<p>Add the CRL in class1crl.pem to the CRL store: cimcrl -a -f class1crl.pem Remove the CRL for a specified issuer:  List all the X509 CRLs in the trust store: cimcrl -l </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-cimserver/">cimserver</a>(8), <a href="/docs/linux/man/8-cimtrust/">cimtrust</a>(8), <a href="/docs/linux/man/8-cimconfig/">cimconfig</a>(8). </p>
