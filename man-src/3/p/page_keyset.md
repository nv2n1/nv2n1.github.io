---
title: "page_keyset(3)"
name: "page_keyset"
section: "3"
letter: "p"
url: "/docs/linux/man/3-page_keyset/"
description: "page_keyset – Certificate store operations Type of certificates store:"
---

<p>page_keyset &#8211; Certificate store operations Type of certificates store:</p>
<dl>
<dt>&bull;</dt>
<dd>MEMORY In memory based format. Doesnt support storing.</dd>
<dt>&bull;</dt>
<dd>FILE FILE supports raw DER certicates and PEM certicates. When PEM is used the file can contain may certificates and match private keys. Support storing the certificates. DER format only supports on certificate and no private key.</dd>
<dt>&bull;</dt>
<dd>PEM-FILE Same as FILE, defaulting to PEM encoded certificates.</dd>
<dt>&bull;</dt>
<dd>PEM-FILE Same as FILE, defaulting to DER encoded certificates.</dd>
<dt>&bull;</dt>
<dd>PKCS11</dd>
<dt>&bull;</dt>
<dd>PKCS12</dd>
<dt>&bull;</dt>
<dd>DIR</dd>
<dt>&bull;</dt>
<dd>KEYCHAIN Apple Mac OS X KeyChain backed keychain object.</dd></dl>
<p> See the library functions here: <code>hx509 certificate store functions</code> </p>
