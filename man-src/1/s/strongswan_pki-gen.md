---
title: "strongswan_pki-gen(1)"
name: "strongswan_pki-gen"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongswan_pki-gen/"
description: "pki –gen – Generate a new RSA or ECDSA private key"
---

<p>pki &#8211;gen &#8211; Generate a new RSA or ECDSA private key</p>
<h2>Synopsis</h2>
<p>[ <code>&#8211;type </code><i>type</i> ] [ <code>&#8211;size </code><i>bits</i> ] [ <code>&#8211;safe-primes</code> ] [ <code>&#8211;shares </code><i>n</i> ] [ <code>&#8211;threshold </code><i>l</i> ] [ <code>&#8211;outform </code><i>encoding</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) is used to generate a new RSA or ECDSA private key.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h, &#8211;help</code></p>
<dd>Print usage information with a summary of the available options.</p>
<dt><code>-v, &#8211;debug </code><i>level</i></p>
<dd>Set debug level, default: 1.</p>
<dt><code>-+, &#8211;options </code><i>file</i></p>
<dd>Read command line options from <i>file</i>.</p>
<dt><code>-t, &#8211;type </code><i>type</i></p>
<dd>Type of key to generate. Either <i>rsa</i>, <i>ecdsa</i>, <i>ed25519</i> or <i>bliss</i>, defaults to <i>rsa</i>.</p>
<dt><code>-s, &#8211;size </code><i>bits</i></p>
<dd>Key length in bits. Defaults to 2048 for <i>rsa</i> and 384 for <i>ecdsa</i>. For <i>ecdsa</i> only three values are currently supported: 256, 384 and 521.</p>
<dt><code>-p, &#8211;safe-primes</code></p>
<dd>Generate RSA safe primes.</p>
<dt><code>-f, &#8211;outform </code><i>encoding</i></p>
<dd>Encoding of the generated private key. Either <i>der</i> (ASN.1 DER) or <i>pem</i> (Base64 PEM), defaults to <i>der</i>.</dl>
<h3>RSA Threshold Cryptography</h3>
<dl COMPACT>
<dt><code>-n, &#8211;shares </code><i>&lt;n&gt;</i></p>
<dd>Number of private RSA key shares.</p>
<dt><code>-l, &#8211;threshold </code><i>&lt;l&gt;</i></p>
<dd>Minimum number of participating RSA key shares.</dl>
<h2>Problems On Hosts With Low Entropy</h2>
<p>If the <i>gmp</i> plugin is used to generate RSA private keys the key material is read from <i>/dev/random</i> (via the <i>random</i> plugin). Therefore, the command may block if the system&#8217;s entropy pool is empty. To avoid this, either use a hardware random number generator to feed <i>/dev/random</i> or use OpenSSL (via the <i>openssl</i> plugin or the command line) which is not as strict in regards to the quality of the key material (it reads from <i>/dev/urandom</i> if necessary). It is also possible to configure the devices used by the <i>random</i> plugin in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). Setting <code>libstrongswan.plugins.random.random</code> to <i>/dev/urandom</i> forces the plugin to treat bytes read from <i>/dev/urandom</i> as high grade random data, thus avoiding the blocking. Of course, this doesn&#8217;t change the fact that the key material generated this way is of lower quality.</p>
<h2>Examples</h2>
<dl COMPACT>
<dt><code>pki &#8211;gen &#8211;size 3072 &gt; rsa_key.der</code></p>
<dd>Generates a 3072-bit RSA private key.</p>
<dt><code>pki &#8211;gen &#8211;type ecdsa &#8211;size 256 &gt; ecdsa_key.der</code></p>
<dd>Generates a 256-bit ECDSA private key.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
