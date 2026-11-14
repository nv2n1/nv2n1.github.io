---
title: "key_encryptsession(3)"
name: "key_encryptsession"
section: "3"
letter: "k"
url: "/docs/linux/man/3-key_encryptsession/"
description: "key_decryptsession, key_encryptsession, key_setsecret, key_gendes, key_secretkey_is_set – interfaces to rpc keyserver daemon"
---

<h2 class="name">NAME</h2>
<p> key_decryptsession, key_encryptsession, key_setsecret, key_gendes, key_secretkey_is_set &#8211; interfaces to rpc keyserver daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;rpc/rpc.h&gt;</code> </p>
<p> <code>int key_decryptsession(char *</code><i>remotename</i><code>,</code> <code>des_block *</code><i>deskey</i><code>);</code> </p>
<p> <code>int key_encryptsession(char *</code><i>remotename</i><code>,</code> <code>des_block *</code><i>deskey</i><code>);</code> </p>
<p> <code>int key_gendes(des_block *</code><i>deskey</i><code>);</code> </p>
<p> <code>int key_setsecret(char *</code><i>key</i><code>);</code> </p>
<p> <code>int key_secretkey_is_set(void);</code></p>
<h2>DESCRIPTION</h2>
<p> The functions here are used within the RPC&#8217;s secure authentication mechanism (AUTH_DES). There should be no need for user programs to use this functions. </p>
<p> The function <code>key_decryptsession</code>() uses the (remote) server netname and takes the DES key for decrypting. It uses the public key of the server and the secret key associated with the effective UID of the calling process. </p>
<p> The function <code>key_encryptsession</code>() is the inverse of <code>key_decryptsession</code>(). It encrypts the DES keys with the public key of the server and the secret key associated with the effective UID of the calling process. </p>
<p> The function <code>key_gendes</code>() is used to ask the keyserver for a secure conversation key. </p>
<p> The function <code>key_setsecret</code>() is used to set the key for the effective UID of the calling process. </p>
<p> The function <code>key_secretkey_is_set</code>() can be used to determine whether a key has been set for the effective UID of the calling process.</p>
<h2>RETURN VALUE</h2>
<p> These functions return 1 on success and 0 on failure.</p>
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
<td> <code>key_decryptsession</code>(),<br />
 <code>key_encryptsession</code>(),<br />
 <code>key_gendes</code>(),<br />
 <code>key_setsecret</code>(),<br />
 <code>key_secretkey_is_set</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>NOTES</h2>
<p> Note that we talk about two types of encryption here. One is asymmetric using a public and secret key. The other is symmetric, the 64-bit DES. </p>
<p> These routines were part of the Linux/Doors-project, abandoned by now.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
