---
title: "clean-crl(8)"
name: "clean-crl"
section: "8"
letter: "c"
url: "/docs/linux/man/8-clean-crl/"
description: "clean-crl – remove orphaned CRL like files from a certificate directory"
---

<p>clean-crl &#8211; remove orphaned CRL like files from a certificate directory</p>
<h2>Synopsis</h2>
<p><code>clean-crl</code> [<code>-l crlpath</code>] [<code>-v</code>] [<code>-V</code>] [<code>-n</code>] [<code>-h</code>]</p>
<h2>Description</h2>
<p>The <i>clean-crl</i> utility will remove CRL like files named <i>hash</i>.r<i>n</i> from the directory specified with the <code>-l</code> option if there is no corresponding .<i>n</i> file in the same. In effect, if the directory is solely used to hold CA certificates in the common OpenSSL format, it will thus remove CRL files for which the corresponding CA does not or no longer exists in the directory. </p>
<h2>Options</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd>Show help text.</p>
<dt><code>-l &#8211;cadir metadata-directory</code></p>
<dd>The script will search this directory for files with the suffix .r<i>i</i>. There is no default &#8211; a common choice is /etc/pki/tls/certs, /etc/openldap/cacerts, or /etc/grid-security/certificates. </p>
<dt><code>-V &#8211;version </code></p>
<dd>Display version number (same as corresponding fetch-crl) </p>
<dt><code>-v &#8211;verbose</code></p>
<dd>Verbose mode </p>
<dt><code>-n &#8211;dryrun</code></p>
<dd>Do not actually remove any files (useful primarily with -v) </p>
</dl>
<h2>Configuration</h2>
<p>None.</p>
<h2>Notes</h2>
<p>This tool does not check the contents of the files removed, and will blindly unlink any file which even remotely looks like an OpenSSL CRL file. Use with extreme caution. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fetch-crl/">fetch-crl</a>(8), <a href="/docs/linux/man/1-openssl/">openssl</a>(1), <a rel="nofollow" href="http://wiki.nikhef.nl/grid/FetchCRL3">http://wiki.nikhef.nl/grid/FetchCRL3</a> </p>
<h2>Diagnostics</h2>
<p>Exit status is normally 0; if an error occurs, exit status is 1 and diagnostics will be written to standard error.</p>
<h2>License</h2>
<p>Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); </p>
<p> <code><a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a></code></p>
<h2>Bugs</h2>
<p>Does not check the contents of the files removed. </p>
