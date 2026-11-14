---
title: "crypt(5)"
name: "crypt"
section: "5"
letter: "c"
url: "/docs/linux/man/5-crypt/"
description: "crypt – storage format for hashed passphrases and available hashing methods"
---

<p>Openwall Project</p>
<h2>Name</h2>
<p><code>crypt</code> &#8211; storage format for hashed passphrases and available hashing methods</p>
<h2>Description</h2>
<p>The hashing methods implemented by <a href="/docs/linux/man/3-crypt/">crypt</a>(3) are designed only to process user passphrases for storage and authentication; they are not suitable for use as general-purpose cryptographic hashes. </p>
<p> Passphrase hashing is not a replacement for strong passphrases. It is always possible for an attacker with access to the hashed passphrases to guess and check possible cleartext passphrases. However, with a strong hashing method, guessing will be too slow for the attacker to discover a strong passphrase. </p>
<p> All of the hashing methods use a &#8220;salt&#8221; to perturb the hash function, so that the same passphrase may produce many possible hashes. Newer methods accept longer salt strings. The salt should be chosen at random for each user. Salt defeats a number of attacks: </p>
<ol>
<li> It is not possible to hash a passphrase once and then test it against each account&#8217;s stored hash; the hash calculation must be repeated for each account.
<li> It is not possible to tell whether two accounts use the same passphrase without successfully guessing one of the phrases.
<li> Tables of precalculated hashes of commonly used passphrases must have an entry for each possible salt, which makes them impractically large. </ol>
<p> All of the hashing methods are also deliberately engineered to be slow; they use many iterations of an underlying cryptographic primitive to increase the cost of each guess. The newer hashing methods allow the number of iterations to be adjusted, using the &#8220;CPU time cost&#8221; parameter to crypt_gensalt3. This makes it possible to keep the hash slow as hardware improves.</p>
<h2>Format Of Hashed Passphrases</h2>
<p>All of the hashing methods supported by <a href="/docs/linux/man/3-crypt/">crypt</a>(3) produce a hashed passphrase which consists of four components: <i>prefix</i> <i>options</i> <i>salt</i> and <i>hash</i> The prefix controls which hashing method is to be used, and is the appropriate string to pass to crypt_gensalt3 to select that method. The contents of <i>options</i> <i>salt</i> and <i>hash</i> are up to the method. Depending on the method, the <i>prefix</i> and <i>options</i> components may be empty. </p>
<p> The Fa setting argument to <a href="/docs/linux/man/3-crypt/">crypt</a>(3) must begin with the first three components of a valid hashed passphrase, but anything after that is ignored. This makes authentication simple: hash the input passphrase using the stored passphrase as the setting, and then compare the result to the stored passphrase. </p>
<p> Hashed passphrases are always entirely printable ASCII, and do not contain any whitespace or the characters `<code>:</code> &#8216; `<code>;</code> &#8216; `<code>*</code> &#8216; `<code>!</code> &#8216; or `<code>\</code> &#8216; (These characters are used as delimiters and special markers in the <a href="/docs/linux/man/5-passwd/">passwd</a>(5) and <a href="/docs/linux/man/5-shadow/">shadow</a>(5) files.) </p>
<p> The syntax of each component of a hashed passphrase is up to the hashing method. `<code>$</code> &#8216; characters usually delimit components, and the salt and hash are usually encoded as numerals in base 64. The details of this base-64 encoding vary among hashing methods. The common &#8220;base64&#8221; encoding specified by RFC 4648 is usually <i>not</i> used.</p>
<h2>Available Hashing Methods</h2>
<p>This is a list of <i>all</i> the hashing methods supported by <a href="/docs/linux/man/3-crypt/">crypt</a>(3), in decreasing order of strength. Many of the older methods are now considered too weak to use for new passphrases. The hashed passphrase format is expressed with extended regular expressions (see <a href="/docs/linux/man/7-regex/">regex</a>(7)) and does not show the division into prefix, options, salt, and hash.</p>
<h3>yescrypt</h3>
<p>yescrypt is a scalable passphrase hashing scheme designed by Solar Designer, which is based on Colin Percival&#8217;s scrypt. Recommended for new hashes.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$y$&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$y\$[./A-Za-z0-9]+\$[./A-Za-z0-9]{,86}\$[./A-Za-z0-9]{43} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited</p>
<dt><code>Hash size</code></p>
<dd>256 bits</p>
<dt><code>Salt size</code></p>
<dd>up to 512 (128+ recommended) bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>1 to 11 (logarithmic)</dl>
<h3>gost-yescrypt</h3>
<p>gost-yescrypt uses the output from the yescrypt hashing method in place of a hmac message. Thus, the yescrypt crypto properties are superseded by the GOST R 34.11-2012 (Streebog) hash function with a 256 bit digest. This hashing method is useful in applications that need modern passphrase hashing methods, but require to rely on the cryptographic properties of GOST algorithms. The GOST R 34.11-2012 (Streebog) hash function has been published by the IETF as RFC 6986. Recommended for new hashes.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$gy$&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$gy\$[./A-Za-z0-9]+\$[./A-Za-z0-9]{,86}\$[./A-Za-z0-9]{43} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited</p>
<dt><code>Hash size</code></p>
<dd>256 bits</p>
<dt><code>Salt size</code></p>
<dd>up to 512 (128+ recommended) bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>1 to 11 (logarithmic)</dl>
<h3>scrypt</h3>
<p>scrypt is a password-based key derivation function created by Colin Percival, originally for the Tarsnap online backup service. The algorithm was specifically designed to make it costly to perform large-scale custom hardware attacks by requiring large amounts of memory. In 2016, the scrypt algorithm was published by IETF as RFC 7914.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$7$&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$7\$[./A-Za-z0-9]{11,97}\$[./A-Za-z0-9]{43} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited</p>
<dt><code>Hash size</code></p>
<dd>256 bits</p>
<dt><code>Salt size</code></p>
<dd>up to 512 (128+ recommended) bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>6 to 11 (logarithmic)</dl>
<h3>bcrypt</h3>
<p>A hash based on the Blowfish block cipher, modified to have an extra-expensive key schedule. Originally developed by Niels Provos and David Mazieres for OpenBSD and also supported on recent versions of FreeBSD and NetBSD, on Solaris 10 and newer, and on several GNU/*/Linux distributions.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$2b$&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$2[abxy]\$[0-9]{2}\$[./A-Za-z0-9]{53} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>72 characters</p>
<dt><code>Hash size</code></p>
<dd>184 bits</p>
<dt><code>Salt size</code></p>
<dd>128 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>4 to 31 (logarithmic)</dl>
<p> The alternative prefix &quot;$2y$&quot; is equivalent to &quot;$2b$&quot;. It exists for historical reasons only. The alternative prefixes &quot;$2a$&quot; and &quot;$2x$&quot; provide bug-compatibility with crypt_blowfish 1.0.4 and earlier, which incorrectly processed characters with the 8th bit set.</p>
<h3>sha512crypt</h3>
<p>A hash based on SHA-2 with 512-bit output, originally developed by Ulrich Drepper for GNU libc. Supported on Linux but not common elsewhere. Acceptable for new hashes. The default CPU time cost parameter is 5000, which is too low for modern hardware.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$6$&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$6\$(rounds=[1-9][0-9]+\$)?[^$:
]{1,16}\$[./0-9A-Za-z]{86} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited</p>
<dt><code>Hash size</code></p>
<dd>512 bits</p>
<dt><code>Salt size</code></p>
<dd>6 to 96 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>1000 to 999,999,999</dl>
<h3>sha256crypt</h3>
<p>A hash based on SHA-2 with 256-bit output, originally developed by Ulrich Drepper for GNU libc. Supported on Linux but not common elsewhere. Acceptable for new hashes. The default CPU time cost parameter is 5000, which is too low for modern hardware.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$5$&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$5\$(rounds=[1-9][0-9]+\$)?[^$:
]{1,16}\$[./0-9A-Za-z]{43} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited</p>
<dt><code>Hash size</code></p>
<dd>256 bits</p>
<dt><code>Salt size</code></p>
<dd>6 to 96 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>1000 to 999,999,999</dl>
<h3>sha1crypt</h3>
<p>A hash based on HMAC-SHA1. Originally developed by Simon Gerraty for NetBSD. Not as weak as the DES-based hashes below, but SHA1 is so cheap on modern hardware that it should not be used for new hashes.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$sha1&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$sha1\$[1-9][0-9]+\$[./0-9A-Za-z]{1,64}\$[./0-9A-Za-z]{8,64}[./0-9A-Za-z]{32} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited</p>
<dt><code>Hash size</code></p>
<dd>160 bits</p>
<dt><code>Salt size</code></p>
<dd>6 to 384 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>4 to 4,294,967,295</dl>
<h3>SunMD5</h3>
<p>A hash based on the MD5 algorithm, with additional cleverness to make precomputation difficult, originally developed by Alec David Muffet for Solaris. Not adopted elsewhere, to our knowledge. Not as weak as the DES-based hashes below, but MD5 is so cheap on modern hardware that it should not be used for new hashes.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$md5&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$md5(,rounds=[1-9][0-9]+)?\$[./0-9A-Za-z]{8}\${1,2}[./0-9A-Za-z]{22} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited</p>
<dt><code>Hash size</code></p>
<dd>128 bits</p>
<dt><code>Salt size</code></p>
<dd>48 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>4096 to 4,294,963,199</dl>
<h3>md5crypt</h3>
<p>A hash based on the MD5 algorithm, originally developed by Poul-Henning Kamp for FreeBSD. Supported on most free Unixes and newer versions of Solaris. Not as weak as the DES-based hashes below, but MD5 is so cheap on modern hardware that it should not be used for new hashes. CPU time cost is not adjustable.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$1$&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$1\$[^$:
]{1,8}\$[./0-9A-Za-z]{22} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited</p>
<dt><code>Hash size</code></p>
<dd>128 bits</p>
<dt><code>Salt size</code></p>
<dd>6 to 48 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>1000</dl>
<h3>bsdicrypt (BSDI extended DES)</h3>
<p>A weak extension of traditional DES, which eliminates the length limit, increases the salt size, and makes the time cost tunable. It originates with BSDI and is also available on at least NetBSD, OpenBSD, and FreeBSD due to the use of David Burren&#8217;s FreeSec library. It is better than bigcrypt and traditional DES, but still should not be used for new hashes.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;_&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal _[./0-9A-Za-z]{19} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited (ignores 8th bit)</p>
<dt><code>Hash size</code></p>
<dd>64 bits</p>
<dt><code>Effective key size</code></p>
<dd>56 bits</p>
<dt><code>Salt size</code></p>
<dd>24 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>1 to 16,777,215 (must be odd)</dl>
<h3>bigcrypt</h3>
<p>A weak extension of traditional DES, available on some System V-derived Unixes. All it does is raise the length limit from 8 to 128 characters, and it does this in a crude way that allows attackers to guess chunks of a long passphrase in parallel. It should not be used for new hashes.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;&quot;</code> Ef (empty string)</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal [./0-9A-Za-z]{13,178} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>128 characters (ignores 8th bit)</p>
<dt><code>Hash size</code></p>
<dd>up to 1024 bits</p>
<dt><code>Effective key size</code></p>
<dd>up to 896 bits</p>
<dt><code>Salt size</code></p>
<dd>12 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>25</dl>
<h3>descrypt (Traditional DES)</h3>
<p>The original hashing method from Unix V7, based on the DES block cipher. Because DES is cheap on modern hardware, because there are only 4096 possible salts and 2**56 possible hashes, and because it truncates passphrases to 8 characters, it is feasible to discover <i>any</i> passphrase hashed with this method. It should only be used if you absolutely have to generate hashes that will work on an old operating system that supports nothing else.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;&quot;</code> Ef (empty string)</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal [./0-9A-Za-z]{13} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>8 characters (ignores 8th bit)</p>
<dt><code>Hash size</code></p>
<dd>64 bits</p>
<dt><code>Effective key size</code></p>
<dd>56 bits</p>
<dt><code>Salt size</code></p>
<dd>12 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>25</dl>
<h3>Nt</h3>
<p>The hashing method used for network authentication in some versions of the SMB/CIFS protocol. Available, for cross-compatibility&#8217;s sake, on FreeBSD. Based on MD4. Has no salt or tunable cost parameter. Like traditional DES, it is so weak that <i>any</i> passphrase hashed with this method is guessable. It should only be used if you absolutely have to generate hashes that will work on an old operating system that supports nothing else.</p>
<dl>
<dt><code>Prefix</code></p>
<dd>Bf <code>&quot;$3$&quot;</code> Ef</p>
<dt><code>Hashed passphrase format</code></p>
<dd>Bf -literal \$3\$\$[0-9a-f]{32} Ef</p>
<dt><code>Maximum passphrase length</code></p>
<dd>unlimited</p>
<dt><code>Hash size</code></p>
<dd>256 bits</p>
<dt><code>Salt size</code></p>
<dd>0 bits</p>
<dt><code>CPU time cost parameter</code></p>
<dd>1</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-crypt/">crypt</a>(3), crypt_gensalt3, <a href="/docs/linux/man/3-getpwent/">getpwent</a>(3), <a href="/docs/linux/man/5-passwd/">passwd</a>(5), <a href="/docs/linux/man/5-shadow/">shadow</a>(5), <a href="/docs/linux/man/8-pam/">pam</a>(8)</p>
<dl>
<dd>Niels Provos David Mazieres <i>A Future-Adaptable Password Scheme</i> <i>Proceedings of the 1999 USENIX Annual Technical Conference</i> June 1999</dl>
<dl>
<dd>Robert Morris Ken Thompson <i>Password Security: A Case History</i> <i>Communications of the ACM</i> 22 11 1979</dl>
