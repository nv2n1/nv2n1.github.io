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
<dt>&bull;</p>
<dd>MEMORY In memory based format. Doesnt support storing.</p>
<dt>&bull;</p>
<dd>FILE FILE supports raw DER certicates and PEM certicates. When PEM is used the file can contain may certificates and match private keys. Support storing the certificates. DER format only supports on certificate and no private key.</p>
<dt>&bull;</p>
<dd>PEM-FILE Same as FILE, defaulting to PEM encoded certificates.</p>
<dt>&bull;</p>
<dd>PEM-FILE Same as FILE, defaulting to DER encoded certificates.</p>
<dt>&bull;</p>
<dd>PKCS11</p>
<dt>&bull;</p>
<dd>PKCS12</p>
<dt>&bull;</p>
<dd>DIR</p>
<dt>&bull;</p>
<dd>KEYCHAIN Apple Mac OS X KeyChain backed keychain object.</dl>
<p> See the library functions here: <code>hx509 certificate store functions</code> </p>
