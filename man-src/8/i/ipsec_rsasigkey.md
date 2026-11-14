---
title: "ipsec_rsasigkey(8)"
name: "ipsec_rsasigkey"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_rsasigkey/"
description: "ipsec_rsasigkey – generate RSA signature key"
---

<p>ipsec_rsasigkey &#8211; generate RSA signature key</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>rsasigkey</i> [&#8211;verbose] [&#8211;seeddev&nbsp;<wbr><i>device</i>] [&#8211;seed&nbsp;<wbr><i>numbits</i>] [&#8211;nssdir&nbsp;<wbr><i>nssdir</i>] [&#8211;password&nbsp;<wbr><i>nsspassword</i>] [&#8211;hostname&nbsp;<wbr><i>hostname</i>] [nbits]</dl>
<h2>Description</h2>
<p><i>rsasigkey</i></p>
<dd>generates an RSA public/private key pair, suitable for digital signatures, of (exactly) <i>nbits</i> bits (that is, two primes each of exactly <i>nbits</i>/2 bits, and related numbers) and emits it on standard output as ASCII (mostly hex) data. <i>nbits</i> must be a multiple of 16. </p>
<p> The public exponent is forced to the value <code>3</code>, which has important speed advantages for signature checking. Beware that the resulting keys have known weaknesses as encryption keys <code>and should not be used for that purpose</code>. </p>
<p> The <code>&#8211;verbose</code> option makes <i>rsasigkey</i> give a running commentary on standard error. By default, it works in silence until it is ready to generate output. </p>
<p> The <code>&#8211;seeddev</code> option specifies a source for random bits used to seed the crypto library&#8217;s RNG. The default is /dev/random (see <code><a href="/docs/linux/man/4-random/">random</a></code>(4)). FreeS/WAN and Openswan without NSS support used this option to specify the random source used to directly create keys. Libreswan only uses it to seed the NSS crypto libraries RNG. Under Linux with hardware random support, special devices might show up as /dev/*rng* devices. However, these should never be accessed directly using this option, as hardware failures could lead to extremely non-random values (streams of zeroes have been observed in the wild) </p>
<p> The <code>&#8211;seedbits</code> option specifies how many seed bits are pulled from the random device to seed the NSS PRNG. The default of 480bit comes from FIPS requirements. Seed bits are rounded up to a multiple of 8. </p>
<p> The use of a different random device or a reduction of seedbits from the default value is prevented when the system is running in FIPS mode. </p>
<p> The <code>&#8211;nssdir</code> option specifies the directory to use for the nss database. This is the directory where the NSS certificate, key and security modules databases reside. The default value is /etc/ipsec.d. </p>
<p> The <code>&#8211;password</code> option specifies the nss cryptographic module authentication password if the NSS module has been configured to require it. A password is required by hardware tokens and also by the internal software token module when configured to run in FIPS mode. If the argument is <i>/etc/ipsec.d</i>/nsspassword, the password comes from that file; otherwise argument is the password. </p>
<p> The <code>&#8211;hostname</code> option specifies what host name to use in the first line of the output (see below); the default is what <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2) returns. </p>
<p> The output format looks like this (with long numbers trimmed down for clarity): </p>
<dl>
<dd>
<pre> # RSA 3744 bits road.toad.com Mon Apr 17 22:20:35 2017
 # for signatures only, UNSAFE FOR ENCRYPTION
 #ckaid=a953473e6014dd4e08eb051e4679dc39be160fea
 #pubkey=0sBAEAA...sKbTzwE=
 Modulus: 0xb84ae7d...b0a6d3cf01
 PublicExponent: 0x010001</pre>
</dl>
<p> The first (comment) line, indicating the nature and date of the key, and giving a host name, is used by <code><a href="/docs/linux/man/8-ipsec_showhostkey/">ipsec_showhostkey</a></code>(8) when generating some forms of key output. </p>
<p> The commented-out <code>pubkey=</code> line contains the public key, the public exponent and the modulus combined in approximately RFC 2537 format (the one deviation is that the combined value is given with a <i>0s</i> prefix, rather than in unadorned base-64), suitable for use in the ipsec.conf file. </p>
<p> The <code>Modulus</code>, <code>PublicExponent</code> and <code>PrivateExponent</code> lines give the basic signing and verification data. </p>
<p> The <code>Prime1</code> and <code>Prime2</code> lines give the primes themselves (aka <i>p</i> and <i>q</i>), largest first. The <code>Exponent1</code> and <code>Exponent2</code> lines give the private exponent mod <i>p-1</i> and <i>q-1</i> respectively. The <code>Coefficient</code> line gives the Chinese Remainder Theorem coefficient, which is the inverse of <i>q</i>, mod <i>p</i>. These additional numbers (which must all be kept as secret as the private exponent) are precomputed aids to rapid signature generation. When NSS is used, these values are not available outside the NSS security database (software token or hardware token) and are instead filled in with the CKA_ID. </p>
<p> No attempt is made to break long lines. </p>
<p> The US patent on the RSA algorithm expired 20 Sept 2000.</p>
<h2>Examples</h2>
<p><code>ipsec rsasigkey &#8211;verbose 4096 &gt;mykey.txt</code></p>
<dl>
<dd>generates a 4096-bit signature key and puts it in the file mykey.txt, with running commentary on standard error. The file contents can be inserted verbatim into a suitable entry in the ipsec.secrets file (see <code><a href="/docs/linux/man/5-ipsec_secrets/">ipsec_secrets</a></code>(5)), and the public key can then be extracted and edited into the ipsec.conf (see <code><a href="/docs/linux/man/8-ipsec_showhostkey/">ipsec_showhostkey</a></code>(8)).</dl>
<h2>Files</h2>
<p>/dev/random, /dev/urandom</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-random/">random</a></code>(4), <code><a href="/docs/linux/man/8-rngd/">rngd</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_showhostkey/">ipsec_showhostkey</a></code>(8), <i>Applied Cryptography, 2nd. ed., by Bruce Schneier, Wiley 1996</i>, <i>RFCs 2537, 2313</i>, <i>GNU MP, the GNU multiple precision arithmetic library, edition 2.0.2, by Torbj Granlund</i></p>
<h2>History</h2>
<p>Originally written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt; by Henry Spencer. Updated for the Libreswan Project by Paul Wouters. </p>
<p> The <i>&#8211;round</i> and <i>&#8211;noopt</i> options were obsoleted as these were only used with the old non-library crypto code </p>
<p> The <i>&#8211;random</i> device is only used for seeding the crypto library, not for direct random to generate keys</p>
<h2>Bugs</h2>
<p>There is an internal limit on <i>nbits</i>, currently 20000. </p>
<p> <i>rsasigkey</i>&#8216;s run time is difficult to predict, since /dev/random output can be arbitrarily delayed if the system&#8217;s entropy pool is low on randomness, and the time taken by the search for primes is also somewhat unpredictable. Specifically, embedded systems and most virtual machines are low on entropy. In such a situation, consider generating the RSA key on another machine, and copying ipsec.secrets and the /etc/ipsec.d directory tree to the embedded platform. Note that NSS embeds the full path in the DB files, so the path on proxy machine must be identical to the path on the destination machine.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
