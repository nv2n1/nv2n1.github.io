---
title: "ne_ssl_cert_export(3)"
name: "ne_ssl_cert_export"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_ssl_cert_export/"
description: "ne_ssl_cert_read, ne_ssl_cert_write, ne_ssl_cert_import, ne_ssl_cert_export – functions to read or write certificates to and from files or strings"
---

<p>ne_ssl_cert_read, ne_ssl_cert_write, ne_ssl_cert_import, ne_ssl_cert_export &#8211; functions to read or write certificates to and from files or strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_ssl.h&gt;

ne_ssl_certificate *ne_ssl_cert_read(const char *filename);

int ne_ssl_cert_write(const ne_ssl_certificate *cert, const char *filename);

ne_ssl_certificate *ne_ssl_cert_import(const char *data);

char *ne_ssl_cert_export(const ne_ssl_certificate *cert);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_ssl_cert_write</code> function writes a certificate to a file using the PEM encoding. The <code>ne_ssl_cert_export</code> function returns a base64-encoded NUL-terminated string representing the certificate. This string is malloc-allocated and should be destroyed using <code>free</code> by the caller. </p>
<p> The <code>ne_ssl_cert_read</code> function reads a certificate from a PEM-encoded file, and returns a certificate object. The <code>ne_ssl_cert_import</code> function returns a certificate object from a base64-encoded string, <i>data</i>, as returned by <code>ne_ssl_cert_export</code>. The certificate object returned by these functions should be destroyed using ne_ssl_cert_free after use.</p>
<h2>Return Value</h2>
<p><code>ne_ssl_cert_read</code> returns NULL if a certificate could not be read from the file. <code>ne_ssl_cert_write</code> returns non-zero if the certificate could not be written to the file. <code>ne_ssl_cert_export</code> always returns a NUL-terminated string, and never NULL. <code>ne_ssl_cert_import</code> returns NULL if the string was not a valid base64-encoded certificate.</p>
<h2>Encoding Formats</h2>
<p>The string produced by <code>ne_ssl_cert_export</code> is the base64 encoding of the DER representation of the certificate. The file written by <code>ne_ssl_cert_write</code> uses the PEM format: this is the base64 encoding of the DER representation with newlines every 64 characters, and start and end marker lines.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
