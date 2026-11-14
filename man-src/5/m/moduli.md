---
title: "moduli(5)"
name: "moduli"
section: "5"
letter: "m"
url: "/docs/linux/man/5-moduli/"
description: "moduli – Diffie-Hellman moduli"
---

<p><code>moduli</code> &#8211; Diffie-Hellman moduli</p>
<h2>Description</h2>
<p>The /etc/ssh/moduli file contains prime numbers and generators for use by <a href="/docs/linux/man/8-sshd/">sshd</a>(8) in the Diffie-Hellman Group Exchange key exchange method. New moduli may be generated with ssh-keygen1 using a two-step process. An initial <i>candidate generation</i> pass, using <code>ssh-keygen -G</code> calculates numbers that are likely to be useful. A second <i>primality testing</i> pass, using <code>ssh-keygen -T</code> provides a high degree of assurance that the numbers are prime and are safe for use in Diffie-Hellman operations by <a href="/docs/linux/man/8-sshd/">sshd</a>(8). This <code>moduli</code> format is used as the output from each pass. The file consists of newline-separated records, one per modulus, containing seven space-separated fields. These fields are as follows:</p>
<dl>
<dt><code>timestamp</code></p>
<dd>The time that the modulus was last processed as YYYYMMDDHHMMSS.</p>
<dt><code>type</code></p>
<dd>Decimal number specifying the internal structure of the prime modulus. Supported types are: </p>
<dt><code>0</code></p>
<dd>Unknown, not tested.</p>
<dt><code>2</code></p>
<dd>&quot;Safe&quot; prime; (p-1)/2 is also prime.</p>
<dt><code>4</code></p>
<dd>Sophie Germain; 2p+1 is also prime.</dl>
<p> Moduli candidates initially produced by ssh-keygen1 are Sophie Germain primes (type 4). Further primality testing with ssh-keygen1 produces safe prime moduli (type 2) that are ready for use in <a href="/docs/linux/man/8-sshd/">sshd</a>(8). Other types are not used by OpenSSH.</p>
<dt><code>tests</code></p>
<dd>Decimal number indicating the type of primality tests that the number has been subjected to represented as a bitmask of the following values: </p>
<dt><code>0x00</code></p>
<dd>Not tested.</p>
<dt><code>0x01</code></p>
<dd>Composite number &#8211; not prime.</p>
<dt><code>0x02</code></p>
<dd>Sieve of Eratosthenes.</p>
<dt><code>0x04</code></p>
<dd>Probabilistic Miller-Rabin primality tests.</dl>
<p> The ssh-keygen1 moduli candidate generation uses the Sieve of Eratosthenes (flag 0x02). Subsequent ssh-keygen1 primality tests are Miller-Rabin tests (flag 0x04).</p>
<dt><code>trials</code></p>
<dd>Decimal number indicating the number of primality trials that have been performed on the modulus.</p>
<dt><code>size</code></p>
<dd>Decimal number indicating the size of the prime in bits.</p>
<dt><code>generator</code></p>
<dd>The recommended generator for use with this modulus (hexadecimal).</p>
<dt><code>modulus</code></p>
<dd>The modulus itself in hexadecimal.</dl>
<p> When performing Diffie-Hellman Group Exchange, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) first estimates the size of the modulus required to produce enough Diffie-Hellman output to sufficiently key the selected symmetric cipher. <a href="/docs/linux/man/8-sshd/">sshd</a>(8) then randomly selects a modulus from Fa /etc/ssh/moduli that best meets the size requirement.</p>
<h2>See Also</h2>
<p>ssh-keygen1, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>Standards</h2>
<dl>
<dd>M. Friedl N. Provos W. Simpson March 2006 <i>RFC 4419</i> <i>Diffie-Hellman Group Exchange for the Secure Shell (SSH) Transport Layer Protocol</i> 2006</dl>
