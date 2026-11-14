---
title: "globus-update-certificate-dir(8)"
name: "globus-update-certificate-dir"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-update-certificate-dir/"
description: "globus-update-certificate-dir – Update symlinks in the trusted CA directory"
---

<p>globus-update-certificate-dir &#8211; Update symlinks in the trusted CA directory</p>
<h2>Synopsis</h2>
<p><code>globus-update-certificate-dir</code> -help </p>
<p> <code>globus-update-certificate-dir</code> [-d <i>DIRECTORY</i>]</p>
<h2>Description</h2>
<p>The <code>globus-update-certificate-dir</code> program creates symlinks between files (CA certificates, certificate revocation lists, signing policy, and certificate request configuration files) using the certificate hash the installed version of OpenSSL uses. OpenSSL 1.0.0 uses a different name hashing algorithm than previous versions, so CA distributions created with older versions of OpenSSL might not be able to locate trusted CAs and related files. Running <code>globus-update-certificate-dir</code> against a trusted CA directory will add symlinks to the files to the hash if needed.</p>
<h2>Options</h2>
<p><code>-help</code></p>
<dl>
<dd>Display a help message to standard output and exit</dl>
<p> <code>-d </code><i>DIRECTORY</i></p>
<dl>
<dd>Create links in the trusted CA directory <i>DIRECTORY</i> instead of using the default search path.</dl>
<h2>Environment</h2>
<p>The following variables affect the execution of <code>globus-update-certificate-dir</code>: </p>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dd>Default trusted certificate directory.</dl>
<p> <code>HOME</code></p>
<dl>
<dd>Path to the current user&#8217;s home directory.</dl>
<p> <code>GLOBUS_LOCATION</code></p>
<dl>
<dd>Path to the Globus installation.</dl>
<h2>Author</h2>
<p>Copyright &#169; 1999-2014 University of Chicago</p>
