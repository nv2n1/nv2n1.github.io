---
title: "pp(1)"
name: "pp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pp/"
description: "pp – Prints certificates, keys, crls, and pkcs7 files"
---

<h2 class="name">NAME</h2>
<p> pp &#8211; Prints certificates, keys, crls, and pkcs7 files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pp -t type [-a] [-i input] [-o output] [-u] [-w]</code></dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> <code>pp </code>pretty-prints private and public key, certificate, certificate-request, pkcs7 or crl files</p>
<h2>OPTIONS</h2>
<p> <code>-t </code> <i>type</i></p>
<dl>
<dt>
<dd> specify the input, one of {private-key | public-key | certificate | certificate-request | pkcs7 | crl} </p>
</dl>
<p> <code>-a </code></p>
<dl>
<dt>
<dd> Input is in ascii encoded form (RFC1113)</dl>
<p> <code>-i </code> <i>inputfile</i></p>
<dl>
<dt>
<dd> Define an input file to use (default is stdin)</dl>
<p> <code>-o </code> <i>outputfile</i></p>
<dl>
<dt>
<dd> Define an output file to use (default is stdout)</dl>
<p> <code>-u </code></p>
<dl>
<dt>
<dd> Use UTF-8 (default is to show non-ascii as .)</dl>
<p> <code>-w </code></p>
<dl>
<dt>
<dd> Don&#8217;t wrap long output lines</dl>
<h2>ADDITIONAL RESOURCES</h2>
<p> NSS is maintained in conjunction with PKI and security-related projects through Mozilla and Fedora. The most closely-related project is Dogtag PKI, with a project wiki at m[blue]<code>PKI Wiki</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> For information specifically about NSS, the NSS project wiki is located at m[blue]<code>Mozilla NSS site</code>m[]<font SIZE="-2">[3]</font>. The NSS site relates directly to NSS code changes and releases. </p>
<p> Mailing lists: pki-devel [at] redhat.com and pki-users [at] redhat.com </p>
<p> IRC: Freenode at #dogtag-pki</p>
<h2>AUTHORS</h2>
<p> The NSS tools were written and maintained by developers with Netscape, Red Hat, Sun, Oracle, Mozilla, and Google. </p>
<p> Authors: Elio Maldonado &lt;emaldona [at] redhat.com&gt;, Deon Lackey &lt;dlackey [at] redhat.com&gt;.</p>
<h2>LICENSE</h2>
<p> Licensed under the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a rel="nofollow" href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Mozilla NSS bug 836477</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://bugzilla.mozilla.org/show_bug.cgi?id=836477">https://bugzilla.mozilla.org/show_bug.cgi?id=836477</a></dl>
<dt> 2.</p>
<dd> PKI Wiki</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://pki.fedoraproject.org/wiki/">http://pki.fedoraproject.org/wiki/</a></dl>
<dt> 3.</p>
<dd> Mozilla NSS site</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.mozilla.org/projects/security/pki/nss/">http://www.mozilla.org/projects/security/pki/nss/</a></dl>
</dl>
<h2>Index</h2>
