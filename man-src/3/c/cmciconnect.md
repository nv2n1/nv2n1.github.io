---
title: "cmciconnect(3)"
name: "cmciconnect"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciconnect/"
description: "cmciConnect() – Create a CMCIClient object and connection"
---

<p>cmciConnect() &#8211; Create a CMCIClient object and connection</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMCIClient</code><i>*</i>
<code>cmciConnect</code><i>(const</i><code>char*</code><i>hostName,</i><code>const</code><i>char*</i><code>scheme,</code>
<br>
<code>const</code><i>char*</i><code>hostPort,</code><i>const</i><code>char*</code><i>CimUsername,</i>
<br>
<code>const</code><i>char*</i><code>CimPassword,</code><i>CMPIStatus*</i><code>rc);</code>
<br>
<code>CMCIClient</code><i>*</i>
<code>cmciConnect2</code><i>(const</i><code>char*</code><i>hostName,</i><code>const</code><i>char*</i><code>scheme,</code>
<br>
<code>const</code><i>char*</i><code>hostPort,</code><i>const</i><code>char*</code><i>CimUsername,</i>
<br>
<code>int</code><i>verifyMode,</i><code>const</code><i>char*</i><code>trustStore,</code>
<br>
<code>const</code><i>char*</i><code>certFile,</code><i>const</i><code>char</code><i>*</i><code>keyFile,</code>
<br>
<code>const</code><i>char*</i><code>CimPassword,</code><i>CMPIStatus*</i><code>rc);</code>
<br></pre>
<h2>Description</h2>
<p>Create a CMCIClient object and initialize it with the CIMOM connection hostname and port, the security credentials to log into the CIMOM, and the internals for sending requests and receiving responses from the CIMOM. </p>
<p> Arguments are the <i>hostName</i> and <i>hostPort</i> to connect, the <i>CimUsername</i> and <i>CimPassword</i> credentials for authentication with the CIMOM, and a pointer to an object to receive the CMPIStatus operation status. </p>
<p> The function cmciConnect2 has the same purpose but offers extra parameters to control SSL operations. </p>
<p> <i>verifyMode</i> specifies whether the server certificate for an SSL connection is to be verified. If set to CMCI_VERIFY_NONE the server ceritificat will not be verified, if set to CMCI_VERIFY_PEER it will be verified agains the certificates in <i>trustStore</i>. </p>
<p> <i>trustStore</i> contains the name of a file containing CA or client certificates against which the server certificate will be verified if <i>verifyMode</i> is set to CMCI_VERIFY_PEER. </p>
<p> <i>certFile</i> specifies the name of a file containing a client certificate which will be presented to the CIM server, if the CIM server implements certificate-based client authentication. Must be set to NULL, if no client certificates are available. </p>
<p> <i>keyFile</i> specifies the name of a file containing the private key for the certificate specified via <i>certFile</i>. Must be set to NULL, if no client certificates are available.</p>
<h2>Return Value</h2>
<p>When successful the <i>cmciConnect</i> function returns a pointer to a dynamically allocated and initialized CMCIClient object with a successful operation status code set. When unsuccessful it returns NULL and sets <i>rc</i> object with the error code and corresponding error string.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<pre> CMCIClient *cc;
 /* Setup a local conncetion to the CIMOM */ 
 cc = cmciConnect(&quot;localhost&quot;, NULL, NULL, NULL, NULL, NULL);</pre>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
