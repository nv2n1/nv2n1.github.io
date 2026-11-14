---
title: "des_setparity(3)"
name: "des_setparity"
section: "3"
letter: "d"
url: "/docs/linux/man/3-des_setparity/"
description: "des_crypt, ecb_crypt, cbc_crypt, des_setparity, DES_FAILED – fast DES encryption"
---

<h2 class="name">NAME</h2>
<p> des_crypt, ecb_crypt, cbc_crypt, des_setparity, DES_FAILED &#8211; fast DES encryption </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;rpc/des_crypt.h&gt;
int ecb_crypt(char *key, char *data, unsigned datalen,
              unsigned mode);
int cbc_crypt(char *key, char *data, unsigned datalen,
              unsigned mode, char *ivec);
void des_setparity(char *key);
int DES_FAILED(int status);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ecb_crypt</code>() and <code>cbc_crypt</code>() implement the NBS DES (Data Encryption Standard). These routines are faster and more general purpose than <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3). They also are able to utilize DES hardware if it is available. <code>ecb_crypt</code>() encrypts in ECB (Electronic Code Book) mode, which encrypts blocks of data independently. <code>cbc_crypt</code>() encrypts in CBC (Cipher Block Chaining) mode, which chains together successive blocks. CBC mode protects against insertions, deletions and substitutions of blocks. Also, regularities in the clear text will not appear in the cipher text. </p>
<p> Here is how to use these routines. The first argument, <i>key</i>, is the 8-byte encryption key with parity. To set the key&#8217;s parity, which for DES is in the low bit of each byte, use <code>des_setparity</code>(). The second argument, <i>data</i>, contains the data to be encrypted or decrypted. The third argument, <i>datalen</i>, is the length in bytes of <i>data</i>, which must be a multiple of 8. The fourth argument, <i>mode</i>, is formed by ORing together some things. For the encryption direction OR in either <code>DES_ENCRYPT</code> or <code>DES_DECRYPT</code>. For software versus hardware encryption, OR in either <code>DES_HW</code> or <code>DES_SW</code>. If <code>DES_HW</code> is specified, and there is no hardware, then the encryption is performed in software and the routine returns <code>DESERR_NOHWDEVICE</code>. For <code>cbc_crypt</code>(), the argument <i>ivec</i> is the 8-byte initialization vector for the chaining. It is updated to the next initialization vector upon return.</p>
<h2>RETURN VALUE</h2>
<dl>
<dt><code>DESERR_NONE</code></p>
<dd> No error.</p>
<dt><code>DESERR_NOHWDEVICE</code></p>
<dd> Encryption succeeded, but done in software instead of the requested hardware.</p>
<dt><code>DESERR_HWERROR</code></p>
<dd> An error occurred in the hardware or driver.</p>
<dt><code>DESERR_BADPARAM</code></p>
<dd> Bad argument to routine.</dl>
<p> Given a result status <i>stat</i>, the macro <code>DES_FAILED(</code><i>stat</i><code>)</code> is false only for the first two statuses.</p>
<h2>VERSIONS</h2>
<p> These functions were added to glibc in version 2.1. </p>
<p> Because they employ the DES block cipher, which is no longer considered secure, <code>ecb_crypt</code>(), <code>ecb_crypt</code>(), <code>crypt_r</code>(), and <code>des_setparity</code>() were removed in glibc 2.28. Applications should switch to a modern cryptography library, such as <code>libgcrypt</code>.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ecb_crypt</code>(), <code>cbc_crypt</code>(), <code>des_setparity</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.3BSD. Not in POSIX.1.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-des/">des</a></code>(1), <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3), <code><a href="/docs/linux/man/3-xcrypt/">xcrypt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
