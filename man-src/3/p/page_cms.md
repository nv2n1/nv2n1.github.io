---
title: "page_cms(3)"
name: "page_cms"
section: "3"
letter: "p"
url: "/docs/linux/man/3-page_cms/"
description: "page_cms – CMS/PKCS7 message functions. CMS is defined in RFC 3369 and is an continuation of the RSA Labs standard PKCS7. The basic messages in CMS is"
---

<p>page_cms &#8211; CMS/PKCS7 message functions. CMS is defined in RFC 3369 and is an continuation of the RSA Labs standard PKCS7. The basic messages in CMS is</p>
<dl>
<dt>&bull;</dt>
<dd>SignedData Data signed with private key (RSA, DSA, ECDSA) or secret (symmetric) key</dd>
<dt>&bull;</dt>
<dd>EnvelopedData Data encrypted with private key (RSA)</dd>
<dt>&bull;</dt>
<dd>EncryptedData Data encrypted with secret (symmetric) key.</dd>
<dt>&bull;</dt>
<dd>ContentInfo Wrapper structure including type and data.</dd></dl>
<p> See the library functions here: <code>hx509 CMS/pkcs7 functions</code> </p>
