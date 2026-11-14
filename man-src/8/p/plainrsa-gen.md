---
title: "plainrsa-gen(8)"
name: "plainrsa-gen"
section: "8"
letter: "p"
url: "/docs/linux/man/8-plainrsa-gen/"
description: "plainrsa-gen – generator for Plain RSA keys"
---

<p><code>plainrsa-gen</code> &#8211; generator for Plain RSA keys</p>
<h2>Synopsis</h2>
<p><code>plainrsa-gen</code> -words [-<code>b </code><i>bits</i> ] [-<code>e </code><i>pubexp</i> ] [-<code>f </code><i>outfile</i> ] [-<code>h</code> ]</p>
<h2>Description</h2>
<p><code>plainrsa-gen</code> can be used to generate <code>Plain RSA keys</code> for authentication purposes. Using <code>Plain RSA keys</code> is optional. Other possibilities are <code>Pre-shared keys</code> or <code>X.509 certificates</code></p>
<dl>
<dt><code>-b </code><i>bits</i></p>
<dd>bit length of the key. Default is <code>1024</code> recommended length is <code>2048</code> or even <code>4096</code> bits. Note that generating longer keys takes longer time.</p>
<dt><code>-e </code><i>pubexp</i></p>
<dd>value of RSA public exponent. Default is <code>0x3</code> Don&#8217;t change this unless you really know what you are doing!</p>
<dt><code>-f </code><i>outfile</i></p>
<dd><i>outfile</i> instead of <code>stdout</code> If the file already exists it won&#8217;t be overwritten. You wouldn&#8217;t like to lose your private key by accident, would you?</dl>
<h2>Output File Format</h2>
<p>This is the secret <code>private key</code> that should <code>never</code> leave your computer: </p>
<pre>: RSA {
 # RSA 1024 bits
 # pubkey=0sAQOrWlcwbAIdNSMhDt...
 Modulus: 0xab5a57306c021d3523...
 PublicExponent: 0x03
 PrivateExponent: 0x723c3a2048...
 Prime1: 0xd309b30e6adf9d85c01...
 Prime2: 0xcfdc2a8aa5b2b3c90e3...
 Exponent1: 0x8cb122099c9513ae...
 Exponent2: 0x8a92c7071921cd30...
 Coefficient: 0x722751305eafe9...
 }</pre>
<p>The line <code>pubkey=0sAQOrW&#8230;</code> of the <code>private key</code> contains a <code>public key</code> that should be stored in the other peer&#8217;s configuration in this format: </p>
<pre>: PUB 0sAQOrWlcwbAIdNSMhDt...</pre>
<p>You can also specify <code>from</code> and <code>to</code> addresses for which the key is valid: </p>
<pre>0.0.0.0/0 10.20.30.0/24 : PUB 0sAQOrWlcwbAIdNSMhDt...</pre>
<h2>See Also</h2>
<p>racoon.conf5, <a href="/docs/linux/man/8-racoon/">racoon</a>(8)</p>
<h2>History</h2>
<p><code>plainrsa-gen</code> was written by An Michal Ludvig Aq michal [at] logix.cz and first appeared in <code>ipsec-tools 0.4</code></p>
