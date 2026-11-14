---
title: "pkcs11-keygen(8)"
name: "pkcs11-keygen"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pkcs11-keygen/"
description: "pkcs11-keygen – generate keys on a PKCS#11 device"
---

<p>pkcs11-keygen &#8211; generate keys on a PKCS#11 device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pkcs11-keygen</code> {-a&nbsp;<wbr><i>algorithm</i>} [<code>-b&nbsp;<wbr></code><i>keysize</i>] [<code>-e</code>] [<code>-i&nbsp;<wbr></code><i>id</i>] [<code>-m&nbsp;<wbr></code><i>module</i>] [<code>-P</code>] [<code>-p&nbsp;<wbr></code><i>PIN</i>] [<code>-q</code>] [<code>-S</code>] [<code>-s&nbsp;<wbr></code><i>slot</i>] {label}</dl>
<h2>Description</h2>
<p><code>pkcs11-keygen</code></p>
<dd>causes a PKCS#11 device to generate a new key pair with the given <code>label</code> (which must be unique) and with <code>keysize</code> bits of prime.</p>
<h2>Arguments</h2>
<p>-a <i>algorithm</i></p>
<dl>
<dd>Specify the key algorithm class: Supported classes are RSA, DSA, DH, and ECC. In addition to these strings, the <code>algorithm</code> can be specified as a DNSSEC signing algorithm that will be used with this key; for example, NSEC3RSASHA1 maps to RSA, and ECDSAP256SHA256 maps to ECC. The default class is &quot;RSA&quot;.</dl>
<p> -b <i>keysize</i></p>
<dl>
<dd>Create the key pair with <code>keysize</code> bits of prime. For ECC keys, the only valid values are 256 and 384, and the default is 256.</dl>
<p> -e</p>
<dl>
<dd>For RSA keys only, use a large exponent.</dl>
<p> -i <i>id</i></p>
<dl>
<dd>Create key objects with id. The id is either an unsigned short 2 byte or an unsigned long 4 byte number.</dl>
<p> -m <i>module</i></p>
<dl>
<dd>Specify the PKCS#11 provider module. This must be the full path to a shared library object implementing the PKCS#11 API for the device.</dl>
<p> -P</p>
<dl>
<dd>Set the new private key to be non-sensitive and extractable. The allows the private key data to be read from the PKCS#11 device. The default is for private keys to be sensitive and non-extractable.</dl>
<p> -p <i>PIN</i></p>
<dl>
<dd>Specify the PIN for the device. If no PIN is provided on the command line, <code>pkcs11-ecgen</code> will prompt for it.</dl>
<p> -e</p>
<dl>
<dd>Quiet mode: suppress unnecessary output.</dl>
<p> -S</p>
<dl>
<dd>For Diffie-Hellman (DH) keys only, use a special prime of 768, 1024 or 1536 bit size and base (aka generator) 2. If not specified, bit size will default to 1024.</dl>
<p> -s <i>slot</i></p>
<dl>
<dd>Open the session with the given PKCS#11 slot. The default is slot 0.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pkcs11-rsagen/">pkcs11-rsagen</a></code>(3), <code><a href="/docs/linux/man/3-pkcs11-dsagen/">pkcs11-dsagen</a></code>(3), <code><a href="/docs/linux/man/3-pkcs11-list/">pkcs11-list</a></code>(3), <code><a href="/docs/linux/man/3-pkcs11-destroy/">pkcs11-destroy</a></code>(3), <code><a href="/docs/linux/man/3-dnssec-keyfromlabel/">dnssec-keyfromlabel</a></code>(3),</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
