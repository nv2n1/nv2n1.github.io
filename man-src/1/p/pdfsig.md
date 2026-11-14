---
title: "pdfsig(1)"
name: "pdfsig"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfsig/"
description: "pdfsig – Portable Document Format (PDF) digital signatures tool"
---

<h2 class="name">NAME</h2>
<p> pdfsig &#8211; Portable Document Format (PDF) digital signatures tool </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfsig</code> [options] [<i>PDF-file</i>] [<i>Output-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pdfsig</code> verifies the digital signatures in a PDF document. It also displays the identity of each signer (commonName field and full distinguished name of the signer certificate), the time and date of the signature, the hash algorithm used for signing, the type of the signature as stated in the PDF and the signed ranges with a statement wether the total document is signed. It can also sign PDF documents (options -add-signature or -sign). </p>
<p> pdfsig uses the trusted certificates stored in the Network Security Services (NSS) Database. </p>
<p> pdfsig also uses the Online Certificate Status Protocol (OCSP) (refer to <a rel="nofollow" href="http://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol)">http://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol)</a> to look up the certificate online and check if it has been revoked (unless -no-ocsp has been specified). </p>
<p> The NSS Database is searched for in the following locations:</p>
<dl>
<dt>&bull;</p>
<dd> If the -nssdir option is specified, the directory specified by this option.</p>
<dt>&bull;</p>
<dd> The NSS Certificate database in the default Firefox profile. i.e. $HOME/.mozilla/firefox/*.default.</p>
<dt>&bull;</p>
<dd> The NSS Certificate database in /etc/pki/nssdb.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-nssdir [prefix]directory</code></p>
<dd> Specify the database directory containing the certificate and key database files. See <a href="/docs/linux/man/1-certutil/">certutil</a>(1) -d option for details of the prefix. If not specified the other search locations described in <code>DESCRIPTION</code> are used.</p>
<dt><code>-nss-pwd password</code></p>
<dd> Specify the password needed to access the NSS database (if any).</p>
<dt><code>-nocert</code></p>
<dd> Do not validate the certificate.</p>
<dt><code>-no-ocsp</code></p>
<dd> Do not perform online OCSP certificate revocation check (local Certificate Revocation Lists (CRL) are still used).</p>
<dt><code>-aia</code></p>
<dd> Enable the use of Authority Information Access (AIA) extension to fetch missing certificates to build the certificate chain.</p>
<dt><code>-dump</code></p>
<dd> Dump all signatures into current directory.</p>
<dt><code>-add-signature</code></p>
<dd> Add a new signature to the document.</p>
<dt><code>-new-signature-field-name name</code></p>
<dd> Specifies the field name to be used when adding a new signature. A random ID will be used by default.</p>
<dt><code>-sign n</code></p>
<dd> Sign the document in the n-th signature field present in the document (must be unsigned).</p>
<dt><code>-nick nickname</code></p>
<dd> Use the certificate with the given nickname for signing.</p>
<dt><code>-kpw password</code></p>
<dd> Use the given password for the signing key (this might be missing if the key isn&#8217;t password protected).</p>
<dt><code>-digest algorithm</code></p>
<dd> Use the given digest algorithm for signing (default: SHA256).</p>
<dt><code>-reason reason</code></p>
<dd> Set the given reason string for the signature (default: no reason set).</p>
<dt><code>-etsi</code></p>
<dd> Create a signature of type ETSI.CAdES.detached instead of adbe.pkcs7.detached.</p>
<dt><code>-list-nicks</code></p>
<dd> List available nicknames in the NSS database.</p>
<dt><code>-v</code></p>
<dd> Print copyright and version information.</p>
<dt><code>-h</code></p>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>pdfsig signed_file.pdf</p>
<dd> Displays signature info for signed_file.pdf.</p>
<dt>pdfsig input.pdf output.pdf -add-signature -nss-pwd password -nick my-cert -reason &#8216;for fun!&#8217;</p>
<dd> Creates a new pdf named output.pdf with the contents of input.pdf signed by the &#8216;my-cert&#8217; certificate.</p>
<dt>pdfsig input.pdf output.pdf -sign 0 -nss-pwd password -nick my-cert -reason &#8216;for fun!&#8217;</p>
<dd> Creates a new pdf named output.pdf with the contents of input.pdf signed by the &#8216;my-cert&#8217; certificate. input.pdf must have an already existing un-signed signature field.</dl>
<h2>AUTHOR</h2>
<p> The pdfsig software and documentation are copyright 1996-2004 Glyph &amp; Cog, LLC and copyright 2005-2015 The Poppler Developers &#8211; <a rel="nofollow" href="http://poppler.freedesktop.org">http://poppler.freedesktop.org</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) <code><a href="/docs/linux/man/1-certutil/">certutil</a></code>(1) </p>
<h2>Index</h2>
