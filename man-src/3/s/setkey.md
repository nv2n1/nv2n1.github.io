---
title: "setkey(3)"
name: "setkey"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setkey/"
description: "encrypt, setkey, encrypt_r, setkey_r – encrypt 64-bit messages"
---

<p>encrypt, setkey, encrypt_r, setkey_r &#8211; encrypt 64-bit messages</p>
<h2>Synopsis</h2>
<pre><code>#define _XOPEN_SOURCE /* See feature_test_macros(7) */
#include &lt;unistd.h&gt;

void encrypt(char block[64], int edflag);

#define _XOPEN_SOURCE /* See feature_test_macros(7) */
#include &lt;stdlib.h&gt;

void setkey(const char *key);

#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;crypt.h&gt;

void setkey_r(const char *key, struct crypt_data *data);
void encrypt_r(char *block, int edflag, struct crypt_data *data);</code></pre>
<p> Each of these requires linking with <i>-lcrypt</i>.</p>
<h2>Description</h2>
<p>These functions encrypt and decrypt 64-bit messages. The <code>setkey</code>() function sets the key used by <code>encrypt</code>(). The <i>key</i> argument used here is an array of 64 bytes, each of which has numerical value 1 or 0. The bytes key[n] where n=8*i-1 are ignored, so that the effective key length is 56 bits. The <code>encrypt</code>() function modifies the passed buffer, encoding if <i>edflag</i> is 0, and decoding if 1 is being passed. Like the <i>key</i> argument, also <i>block</i> is a bit vector representation of the actual value that is encoded. The result is returned in that same vector. These two functions are not reentrant, that is, the key data is kept in static storage. The functions <code>setkey_r</code>() and <code>encrypt_r</code>() are the reentrant versions. They use the following structure to hold the key data: struct crypt_data {<br />
    char keysched[16 * 8];<br />
    char sb0[32768];<br />
    char sb1[32768];<br />
    char sb2[32768];<br />
    char sb3[32768];<br />
    char crypt_3_buf[14];<br />
    char current_salt[2];<br />
    long current_saltbits;<br />
    int direction;<br />
    int initialized;<br />
}; Before calling <code>setkey_r</code>() set <i>data-&gt;initialized</i> to zero.</p>
<h2>Return Value</h2>
<p>These functions do not return any value.</p>
<h2>Errors</h2>
<p>Set <i>errno</i> to zero before calling the above functions. On success, it is unchanged.</p>
<dl>
<dt><code>ENOSYS</code></p>
<dd>The function is not provided. (For example because of former USA export restrictions.)</dl>
<h2>Versions</h2>
<p>Because they employ the DES block cipher, which is no longer considered secure, <code>crypt</code>(), <code>crypt_r</code>(), <code>setkey</code>(), and <code>setkey_r</code>() were removed in glibc 2.28. Applications should switch to a modern cryptography library, such as <code>libgcrypt</code>.</p>
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
<h2>Conforming To</h2>
<p><code>encrypt</code>(), <code>setkey</code>(): POSIX.1-2001, POSIX.1-2008, SUS, SVr4. </p>
<p> The functions <code>encrypt_r</code>() and <code>setkey_r</code>() are GNU extensions.</p>
<h2>Notes</h2>
<h3>Availability in glibc</h3>
<p>See <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3).</p>
<h3>Features in glibc</h3>
<p>In glibc 2.2, these functions use the DES algorithm.</p>
<h2>Examples</h2>
<pre><code>#define _XOPEN_SOURCE
#include &lt;crypt.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
int main(void)
{
    char key[64];
    char orig[9] = &quot;eggplant&quot;;
    char buf[64];
    char txt[9];
    for (int i = 0; i &lt; 64; i++) {
        key[i] = rand() &amp; 1;
    }
    for (int i = 0; i &lt; 8; i++) {
        for (int j = 0; j &lt; 8; j++) {
            buf[i * 8 + j] = orig[i] &gt;&gt; j &amp; 1;
        }
        setkey(key);
    }
    printf(&quot;Before encrypting: %s
&quot;, orig);
    encrypt(buf, 0);
    for (int i = 0; i &lt; 8; i++) {
        for (int j = 0, txt[i] = '
