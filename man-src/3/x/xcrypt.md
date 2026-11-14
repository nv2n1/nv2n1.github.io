---
title: "xcrypt(3)"
name: "xcrypt"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcrypt/"
description: "xencrypt, xdecrypt, passwd2des – RFS password encryption"
---

<p>xencrypt, xdecrypt, passwd2des &#8211; RFS password encryption</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;rpc/des_crypt.h&gt;
void passwd2des(char *passwd, char *key);
int xencrypt(char *secret, char *passwd);
int xdecrypt(char *secret, char *passwd);</code></pre>
<h2>Description</h2>
<p><code>WARNING</code>: Do not use these functions in new code. They do not achieve any type of acceptable cryptographic security guarantees. </p>
<p> The function <code>passwd2des</code>() takes a character string <i>passwd</i> of arbitrary length and fills a character array <i>key</i> of length 8. The array <i>key</i> is suitable for use as DES key. It has odd parity set in bit 0 of each byte. Both other functions described here use this function to turn their argument <i>passwd</i> into a DES key. </p>
<p> The <code>xencrypt</code>() function takes the ASCII character string <i>secret</i> given in hex, which must have a length that is a multiple of 16, encrypts it using the DES key derived from <i>passwd</i> by <code>passwd2des</code>(), and outputs the result again in <i>secret</i> as a hex string of the same length. </p>
<p> The <code>xdecrypt</code>() function performs the converse operation.</p>
<h2>Return Value</h2>
<p>The functions <code>xencrypt</code>() and <code>xdecrypt</code>() return 1 on success and 0 on error.</p>
<h2>Versions</h2>
<p>These functions are available in glibc since version 2.1.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>passwd2des</code>(), <code>xencrypt</code>(), <code>xdecrypt</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Bugs</h2>
<p>The prototypes are missing from the abovementioned include file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cbc_crypt/">cbc_crypt</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
