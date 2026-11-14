---
title: "encrypt_r(3)"
name: "encrypt_r"
section: "3"
letter: "e"
url: "/docs/linux/man/3-encrypt_r/"
description: "encrypt, setkey, encrypt_r, setkey_r – encrypt 64-bit messages"
---

<h2 class="name">NAME</h2>
<p> encrypt, setkey, encrypt_r, setkey_r &#8211; encrypt 64-bit messages </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _XOPEN_SOURCE /* See feature_test_macros(7) */
#include &lt;unistd.h&gt;
void encrypt(char block[64], int edflag);
#define _XOPEN_SOURCE /* See feature_test_macros(7) */
#include &lt;stdlib.h&gt;
void setkey(const char *key);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;crypt.h&gt;
void setkey_r(const char *key, struct crypt_data *data);
void encrypt_r(char *block, int edflag, struct crypt_data *data);
</code></pre>
<p> Each of these requires linking with <i>-lcrypt</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions encrypt and decrypt 64-bit messages. The <code>setkey</code>() function sets the key used by <code>encrypt</code>(). The <i>key</i> argument used here is an array of 64 bytes, each of which has numerical value 1 or 0. The bytes key[n] where n=8*i-1 are ignored, so that the effective key length is 56 bits. </p>
<p> The <code>encrypt</code>() function modifies the passed buffer, encoding if <i>edflag</i> is 0, and decoding if 1 is being passed. Like the <i>key</i> argument, also <i>block</i> is a bit vector representation of the actual value that is encoded. The result is returned in that same vector. </p>
<p> These two functions are not reentrant, that is, the key data is kept in static storage. The functions <code>setkey_r</code>() and <code>encrypt_r</code>() are the reentrant versions. They use the following structure to hold the key data: </p>
<p> struct crypt_data {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char keysched[16&nbsp;*&nbsp;8];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char sb0[32768];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char sb1[32768];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char sb2[32768];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char sb3[32768];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char crypt_3_buf[14];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char current_salt[2];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long current_saltbits;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;direction;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;initialized; }; </p>
<p> Before calling <code>setkey_r</code>() set <i>data-&gt;initialized</i> to zero.</p>
<h2>RETURN VALUE</h2>
<p> These functions do not return any value.</p>
<h2>ERRORS</h2>
<p> Set <i>errno</i> to zero before calling the above functions. On success, it is unchanged.</p>
<dl>
<dt><code>ENOSYS</code></p>
<dd> The function is not provided. (For example because of former USA export restrictions.)</dl>
<h2>VERSIONS</h2>
<p> Because they employ the DES block cipher, which is no longer considered secure, <code>crypt</code>(), <code>crypt_r</code>(), <code>setkey</code>(), and <code>setkey_r</code>() were removed in glibc 2.28. Applications should switch to a modern cryptography library, such as <code>libgcrypt</code>.</p>
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
<td> <code>encrypt</code>(), <code>setkey</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:crypt
</td>
</tr>
<tr VALIGN=top>
<td> <code>encrypt_r</code>(), <code>setkey_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>encrypt</code>(), <code>setkey</code>(): POSIX.1-2001, POSIX.1-2008, SUS, SVr4. </p>
<p> The functions <code>encrypt_r</code>() and <code>setkey_r</code>() are GNU extensions.</p>
<h2>NOTES</h2>
<h3>Availability in glibc</h3>
<p> See <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3).</p>
<h3>Features in glibc</h3>
<p> In glibc 2.2, these functions use the DES algorithm.</p>
<h2>EXAMPLES</h2>
<p> #define _XOPEN_SOURCE #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;crypt.h&gt; </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char key[64];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char orig[9]&nbsp;=&nbsp;&quot;eggplant&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[64];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char txt[9]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;64;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key[i]&nbsp;=&nbsp;rand()&nbsp;&amp;&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;8;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;8;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf[i&nbsp;*&nbsp;8&nbsp;+&nbsp;j]&nbsp;=&nbsp;orig[i]&nbsp;&gt;&gt;&nbsp;j&nbsp;&amp;&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setkey(key);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Before encrypting:&nbsp;%s
&quot;, orig); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;encrypt(buf, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;8;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0, txt[i]&nbsp;=&nbsp;&#8216;
