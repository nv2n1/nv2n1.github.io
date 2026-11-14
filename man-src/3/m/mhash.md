---
title: "mhash(3)"
name: "mhash"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mhash/"
description: "mhash – Hash Library"
---

<h2>NAME</h2>
<p> <code>mhash &#8211; Hash Library</code></p>
<h2>VERSION</h2>
<p> mhash <font SIZE="-1">0.9.2</font></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include "mhash.h"
</code></pre>
<p> <code> Informative Functions </code> </p>
<p>size_t mhash_count(void);<br />
size_t mhash_get_block_size(hashid type);<br />
char *mhash_get_hash_name(hashid type);<br />
size_t mhash_get_hash_pblock(hashid type);<br />
hashid mhash_get_mhash_algo(MHASH);</p>
<p> <code> Key Generation Functions </code> </p>
<p>int mhash_keygen_ext(keygenid algorithm, KEYGEN algorithm_data,<br />
                     void *keyword, int keysize,<br />
                     unsigned char *password, int passwordlen);</p>
<p> <code> Initializing Functions </code> </p>
<p>MHASH mhash_init(hashid type);<br />
MHASH mhash_hmac_init(const hashid type, void *key, int keysize, int block);<br />
MHASH mhash_cp(MHASH);</p>
<p> <code> Update Functions </code> </p>
<p>int mhash(MHASH thread, const void *plaintext, size_t size);</p>
<p> <code> Save/Restore Functions </code> </p>
<p>int mhash_save_state_mem(MHASH thread, void *mem, int *mem_size);<br />
MHASH mhash_restore_state_mem(void *mem);</p>
<p> <code> Finalizing Functions </code> </p>
<p>void mhash_deinit(MHASH thread, void *result);<br />
void *mhash_end(MHASH thread);<br />
void *mhash_end_m(MHASH thread, void *(*hash_malloc)(size_t));</p>
<p>void *mhash_hmac_end(MHASH thread);<br />
void *mhash_hmac_end_m(MHASH thread, void *(*hash_malloc)(size_t));<br />
int mhash_hmac_deinit(MHASH thread, void *result);</p>
<p> <code> Available Hashes </code> </p>
<p> <i></i><font SIZE="-1"><i>CRC32</i></font><i></i>: The crc32 algorithm is used to compute checksums. The two variants used in mhash are: <font SIZE="-1"><code>MHASH_CRC32</code></font> (like the one used in ethernet) and <font SIZE="-1"><code>MHASH_CRC32B</code></font> (like the one used in <font SIZE="-1">ZIP</font> programs). </p>
<p> <i></i><font SIZE="-1"><i>ADLER32</i></font><i></i>: The adler32 algorithm is used to compute checksums. It is faster than <font SIZE="-1">CRC32</font> and it is considered to be as reliable as <font SIZE="-1">CRC32</font>. This algorithm is defined as <font SIZE="-1"><code>MHASH_ADLER32</code></font>. </p>
<p> <i></i><font SIZE="-1"><i>MD5</i></font><i></i>: The <font SIZE="-1">MD5</font> algorithm by Ron Rivest and <font SIZE="-1">RSA</font>. In mhash this algorithm is defined as <font SIZE="-1"><code>MHASH_MD5</code></font>. </p>
<p> <i></i><font SIZE="-1"><i>MD4</i></font><i></i>: The <font SIZE="-1">MD4</font> algorithm by Ron Rivest and <font SIZE="-1">RSA</font>. This algorithm is considered broken, so don&#8217;t use it. In mhash this algorithm is defined as <font SIZE="-1"><code>MHASH_MD4</code></font>. </p>
<p> <i></i><font SIZE="-1"><i>SHA1</i></font><i></i>/<i></i><font SIZE="-1"><i>SHA256</i></font><i></i>: The <font SIZE="-1">SHA</font> algorithm by <font SIZE="-1">US</font>. <font SIZE="-1">NIST/NSA</font>. This algorithm is specified for use in the <font SIZE="-1">NIST</font>&#8216;s Digital Signature Standard. In mhash these algorithm are defined as <font SIZE="-1"><code>MHASH_SHA1</code></font> and <font SIZE="-1"><code>MHASH_SHA256</code></font>. </p>
<p> <i></i><font SIZE="-1"><i>HAVAL</i></font><i></i>: <font SIZE="-1">HAVAL</font> is a one-way hashing algorithm with variable length of output. <font SIZE="-1">HAVAL</font> is a modification of <font SIZE="-1">MD5</font>. Defined in mhash as: <font SIZE="-1"><code>MHASH_HAVAL256</code></font><code>, </code><font SIZE="-1"><code>MHASH_HAVAL192</code></font><code>, </code><font SIZE="-1"><code>MHASH_HAVAL160</code></font><code>, </code><font SIZE="-1"><code>MHASH_HAVAL128</code></font>. </p>
<p> <i></i><font SIZE="-1"><i>RIPEMD160</i></font><i></i>: <font SIZE="-1">RIPEMD-160</font> is a 160-bit cryptographic hash function, designed by Hans Dobbertin, Antoon Bosselaers, and Bart Preneel. It is intended to be used as a secure replacement for the 128-bit hash functions <font SIZE="-1">MD4</font>, <font SIZE="-1">MD5</font>, and <font SIZE="-1">RIPEMD</font>. <font SIZE="-1">MD4</font> and <font SIZE="-1">MD5</font> were developed by Ron Rivest for <font SIZE="-1">RSA</font> Data Security, while <font SIZE="-1">RIPEMD</font> was developed in the framework of the <font SIZE="-1">EU</font> project <font SIZE="-1">RIPE</font> (<font SIZE="-1">RACE</font> Integrity Primitives Evaluation, 1988-1992). In mhash this algorithm is defined as <font SIZE="-1"><code>MHASH_RIPEMD160</code></font>. </p>
<p> <i></i><font SIZE="-1"><i>TIGER</i></font><i></i>: Tiger is a fast hash function, by Eli Biham and Ross Anderson. Tiger was designed to be very fast on modern computers, and in particular on the state-of-the-art 64-bit computers, while it is still not slower than other suggested hash functions on 32-bit machines. In mhash this algorithm is defined as: <font SIZE="-1"><code>MHASH_TIGER</code></font><code>, </code><font SIZE="-1"><code>MHASH_TIGER160</code></font><code>, </code><font SIZE="-1"><code>MHASH_TIGER128</code></font>. </p>
<p> <i></i><font SIZE="-1"><i>GOST</i></font><i></i>: <font SIZE="-1">GOST</font> algorithm is a russian standard and it uses the <font SIZE="-1">GOST</font> encryption algorithm to produce a 256 bit hash value. This algorithm is specified for use in the Russian Digital Signature Standard. In mhash this algorithm is defined as <font SIZE="-1"><code>MHASH_GOST</code></font>. </p>
<p> <code> Available Key Generation algorithms </code> </p>
<p> <i></i><font SIZE="-1"><i>KEYGEN_MCRYPT</i></font><i></i>: The key generator used in mcrypt. </p>
<p> <i></i><font SIZE="-1"><i>KEYGEN_ASIS</i></font><i></i>: Just returns the password as binary key. </p>
<p> <i></i><font SIZE="-1"><i>KEYGEN_HEX</i></font><i></i>: Just converts a hex key into a binary one. </p>
<p> <i></i><font SIZE="-1"><i>KEYGEN_PKDES</i></font><i></i>: The transformation used in Phil Karn&#8217;s <font SIZE="-1">DES</font> encryption program. </p>
<p> <i></i><font SIZE="-1"><i>KEYGEN_S2K_SIMPLE</i></font><i></i>: The OpenPGP (rfc2440) Simple S2K. </p>
<p> <i></i><font SIZE="-1"><i>KEYGEN_S2K_SALTED</i></font><i></i>: The OpenPGP Salted S2K. </p>
<p> <i></i><font SIZE="-1"><i>KEYGEN_S2K_ISALTED</i></font><i></i>: The OpenPGP Iterated Salted S2K.</p>
<h2>DESCRIPTION</h2>
<p> The <code>mhash</code> library provides an easy to use C interface for several <i>hash algorithms</i> (also known as &#8220;one-way&#8221; algorithms). These can be used to create checksums, message digests and more. Currently, <font SIZE="-1">MD5</font>, <font SIZE="-1">SHA1</font>, <font SIZE="-1">GOST</font>, <font SIZE="-1">TIGER</font>, <font SIZE="-1">RIPE-MD160</font>, <font SIZE="-1">HAVAL</font> and several other algorithms are supported. <code>mhash</code> support <i></i><font SIZE="-1"><i>HMAC</i></font><i> generation</i> (a mechanism for message authentication using cryptographic hash functions, and is described in rfc2104). <font SIZE="-1">HMAC</font> can be used to create message digests using a secret key, so that these message digests cannot be regenerated (or replaced) by someone else. A key generation mechanism was added to <code>mhash</code> since <i>key generation</i> algorithms usually involve hash algorithms.</p>
<h2>API FUNCTIONS</h2>
<p> We will describe the <font SIZE="-1">API</font> of <code>mhash</code> in detail now. The order follows the one in the <font SIZE="-1">SYNOPSIS</font> directly.</p>
<dl>
<dt>size_t <code>mhash_count</code>(void);</p>
<dd> This returns the <tt>&quot;hashid&quot;</tt> of the last available hash. Hashes are numbered from 0 to <tt>&quot;mhash_count()&quot;</tt>.</p>
<dt>size_t <code>mhash_get_block_size</code>(hashid <i>type</i>);</p>
<dd> If <i>type</i> exists, this returns the used blocksize of the hash <i>type</i> in bytes. Otherwise, it returns 0.</p>
<dt>char *<code>mhash_get_hash_name</code>(hashid <i>type</i>);</p>
<dd> If <i>type</i> exists, this returns the name of the hash <i>type</i>. Otherwise, a <tt>&quot;NULL&quot;</tt> pointer is returned. The string is allocated with <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) seperately, so do not forget to <i><a href="/docs/linux/man/3-free/">free</a></i>(3) it.</p>
<dt>const char *<code>mhash_get_hash_name_static</code>(hashid <i>type</i>);</p>
<dd> If <i>type</i> exists, this returns the name of the hash <i>type</i>. Otherwise, a <tt>&quot;NULL&quot;</tt> pointer is returned.</p>
<dt>size_t <code>mhash_get_hash_pblock</code>(hashid <i>type</i>);</p>
<dd> It returns the block size that the algorithm operates. This is used in mhash_hmac_init. If the return value is 0 you shouldn&#8217;t use that algorithm in <font SIZE="-1">HMAC</font>.</p>
<dt>hashid <code>mhash_get_mhash_algo</code>(<font SIZE="-1">MHASH</font> <i>src</i>);</p>
<dd> Returns the algorithm used in the state of <i>src</i>.</p>
<dt><font SIZE="-1">MHASH</font> <code>mhash_init</code>(hashid <i>type</i>);</p>
<dd> This setups a context to begin hashing using the algorithm <i>type</i>. It returns a descriptor to that context which will result in leaking memory, if you do not call <i><a href="/docs/linux/man/3-mhash_deinit/">mhash_deinit</a></i>(3) later. Returns <tt>&quot;MHASH_FAILED&quot;</tt> on failure.</p>
<dt><font SIZE="-1">MHASH</font> <code>mhash_hmac_init</code>(const hashid <i>type</i>, void *<i>key</i>, int <i>keysize</i>, int <i>block</i>);</p>
<dd> This setups a context to begin hashing using the algorithm type in <font SIZE="-1">HMAC</font> mode. <i>key</i> should be a pointer to the key and <i>keysize</i> its len. The <i>block</i> is the block size (in bytes) that the algorithm operates. It should be obtained by <i>mhash_get_hash_pblock()</i>. If its 0 it defaults to 64. After calling it you should use <i>mhash()</i> to update the context. It returns a descriptor to that context which will result in leaking memory, if you do not call <i><a href="/docs/linux/man/3-mhash_hmac_deinit/">mhash_hmac_deinit</a></i>(3) later. Returns <tt>&quot;MHASH_FAILED&quot;</tt> on failure.</p>
<dt><font SIZE="-1">MHASH</font> <code>mhash_cp</code>(<font SIZE="-1">MHASH</font> <i>src</i>);</p>
<dd> This setups a new context using the state of <i>src</i>.</p>
<dt>int <code>mhash</code>(<font SIZE="-1">MHASH</font> <i>thread</i>, const void *<i>plaintext</i>, size_t <i>size</i>);</p>
<dd> This updates the context described by <i>thread</i> with <i>plaintext</i>. <i>size</i> is the length of <i>plaintext</i> which may be binary data.</p>
<dt>int <code>mhash_save_state_mem</code>( <font SIZE="-1">MHASH</font> <i>thread</i>, void *<i>mem</i>, int* <i>mem_size</i>);</p>
<dd> Saves the state of a hashing algorithm such that it can be restored at some later point in time using <code>mhash_restore_state_mem</code>(). <i>mem_size</i> should contain the size of the given <i>mem</i> pointer. If it is not enough to hold the buffer the required value will be copied there.</p>
<dt><font SIZE="-1">MHASH</font> <code>mhash_restore_state_mem</code>(void* <i>mem</i>);</p>
<dd> Restores the state of a hashing algorithm that was saved using <code>mhash_save_state_mem</code>(). Use like <code>mhash_init</code>().</p>
<dt>void *<code>mhash_end</code>(<font SIZE="-1">MHASH</font> <i>thread</i>);</p>
<dd> This frees all resources associated with <i>thread</i> and returns the result of the whole hashing operation (the &#8220;<i>digest</i>&#8221;).</p>
<dt>void <code>mhash_deinit</code>(<font SIZE="-1">MHASH</font> <i>thread</i>, void* digest);</p>
<dd> This frees all resources associated with <i>thread</i> and stores the result of the whole hashing operation in memory pointed by <i>digest</i>. <i>digest</i> may be null.</p>
<dt>void *<code>mhash_hmac_end</code>(<font SIZE="-1">MHASH</font> <i>thread</i>);</p>
<dd> This frees all resources associated with thread and returns the result of the whole hashing operation (the &#8220;<i>mac</i>&#8221;).</p>
<dt>int <code>mhash_hmac_deinit</code>(<font SIZE="-1">MHASH</font> <i>thread</i>, void* digest);</p>
<dd> This frees all resources associated with <i>thread</i> and stores the result of the whole hashing operation in memory pointed by digest. Digest may be null. Returns non-zero in case of an error.</p>
<dt>void *<code>mhash_end_m</code>(<font SIZE="-1">MHASH</font> <i>thread</i>, void* (*hash_malloc)(size_t));</p>
<dd> This frees all resources associated with <i>thread</i> and returns the result of the whole hashing operation (the &#8220;<i>digest</i>&#8221;). The result will be allocated by using the <i>hash_malloc()</i> function provided.</p>
<dt>void *<code>mhash_hmac_end</code>(<font SIZE="-1">MHASH</font> <i>thread</i>, void* (*hash_malloc)(size_t));</p>
<dd> This frees all resources associated with thread and returns the result of the whole hashing operation (the &#8220;<i>mac</i>&#8221;). The result will be allocated by using the <i>hash_malloc()</i> function provided.</dl>
<h2>KEYGEN API FUNCTIONS</h2>
<p> We will now describe the Key Generation <font SIZE="-1">API</font> of <code>mhash</code> in detail.</p>
<dl>
<dt>int <code>mhash_keygen_ext</code>(keygenid <i>algorithm</i>, <font SIZE="-1">KEYGEN</font> <i>algorithm_data</i>, void* <i>keyword</i>, int <i>keysize</i>, unsigned char* <i>password</i>, int <i>passwordlen</i>);</p>
<dd> This function, generates a key from a password. The password is read from <i>password</i> and it&#8217;s len should be in <i>passwordlen</i>. The key generation algorithm is specified in <i>algorithm</i>, and that algorithm may (internally) use the <font SIZE="-1">KEYGEN</font> structure. The <font SIZE="-1">KEYGEN</font> structure consists of:<br />
&nbsp;<wbr>typedef struct keygen&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>hashid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hash_algorithm[2];<br />
&nbsp;<wbr>&nbsp;<wbr>unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>count;<br />
&nbsp;<wbr>&nbsp;<wbr>void*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>salt;<br />
&nbsp;<wbr>&nbsp;<wbr>int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>salt_size;<br />
&nbsp;<wbr>}&nbsp;<wbr><font SIZE="-1">KEYGEN</font>; </p>
<p> The algorithm(s) specified in <i>algorithm_data.hash_algorithm</i>, should be hash algorithms and may be used by the key generation algorithm. Some key generation algorithms may use more than one hash algorithms (view also <i>mhash_keygen_uses_hash_algorithm()</i>). If it is desirable (and supported by the algorithm, eg. <font SIZE="-1">KEYGEN_S2K_SALTED</font>) a salt may be specified in <i>algorithm_data.salt</i> of size <i>algorithm_data.salt_size</i> or may be <font SIZE="-1">NULL</font>. </p>
<p> The algorithm may use the <i>algorithm_data.count</i> internally (eg. <font SIZE="-1">KEYGEN_S2K_ISALTED</font>). The generated keyword is stored in <i>keyword</i>, which should be (at least) <i>keysize</i> bytes long. The generated keyword is a binary one. Returns a negative number on failure.</p>
<dt>int <code>mhash_keygen_uses_salt</code>( keygenid <i>algorithm</i>);</p>
<dd> This function returns 1 if the specified key generation algorithm needs a salt to be specified.</p>
<dt>int <code>mhash_keygen_uses_count</code>( keygenid <i>algorithm</i>);</p>
<dd> This function returns 1 if the specified key generation algorithm needs the algorithm_data.count field in <i>mhash_keygen_ext()</i>. The count field tells the algorithm to hash repeatedly the password and to stop when <code>count</code> bytes have been processed.</p>
<dt>int <code>mhash_get_keygen_salt_size</code>( keygenid <i>algorithm</i>);</p>
<dd> This function returns the size of the salt size, that the specific <i>algorithm</i> will use. If it returns 0, then there is no limitation in the size.</p>
<dt>int <code>mhash_get_keygen_max_key_size</code>( keygenid <i>algorithm</i>);</p>
<dd> This function returns the maximum size of the key, that the key generation algorithm may produce. If it returns 0, then there is no limitation in the size.</p>
<dt>int <code>mhash_keygen_uses_hash_algorithm</code>( keygenid <i>algorithm</i>);</p>
<dd> This function returns the number of the hash algorithms the key generation algorithm will use. If it is 0 then no hash algorithm is used by the key generation algorithm. This is for the <i>algorithm_data.hash_algorithm</i> field in <i>mhash_keygen_ext()</i>. If</p>
<dt>size_t <code>mhash_keygen_count</code>(void);</p>
<dd> This returns the <tt>&quot;keygenid&quot;</tt> of the last available key generation algorithm. Algorithms are numbered from 0 to <tt>&quot;mhash_keygen_count()&quot;</tt>.</p>
<dt>char *<code>mhash_get_keygen_name</code>(keygenid <i>type</i>);</p>
<dd> If <i>type</i> exists, this returns the name of the keygen <i>type</i>. Otherwise, a <tt>&quot;NULL&quot;</tt> pointer is returned. The string is allocated with <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) seperately, so do not forget to <i><a href="/docs/linux/man/3-free/">free</a></i>(3) it.</p>
<dt>const char *<code>mhash_get_keygen_name_static</code>(keygenid <i>type</i>);</p>
<dd> If <i>type</i> exists, this returns the name of the keygen <i>type</i>. Otherwise, a <tt>&quot;NULL&quot;</tt> pointer is returned.</dl>
<h2>EXAMPLE</h2>
<p> Hashing <font SIZE="-1">STDIN</font> until <font SIZE="-1">EOF</font>. </p>
<p>#include &lt;mhash.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;</p>
<p>int main(void)<br />
{<br />
    int i;<br />
    MHASH td;<br />
    unsigned char buffer;<br />
    unsigned char hash[16]; /* enough size for MD5 */</p>
<pre>
        td = mhash_init(MHASH_MD5);
</pre>
<p>if (td == MHASH_FAILED)<br />
    exit(1);</p>
<p>while (fread(&amp;buffer, 1, 1, stdin) == 1) {<br />
    mhash(td, &amp;buffer, 1);<br />
}</p>
<pre>
        mhash_deinit(td, hash);
</pre>
<p>printf(&#8220;Hash:&#8221;);<br />
for (i = 0; i &lt; mhash_get_block_size(MHASH_MD5); i++) {<br />
    printf(&#8220;%.2x&#8221;, hash[i]);<br />
}<br />
printf(&#8220;
&#8221;);</p>
<p>exit(0);<br />
}</p>
<h2>EXAMPLE</h2>
<p> An example program using <font SIZE="-1">HMAC:</font> </p>
<p>#include &lt;mhash.h&gt;<br />
#include &lt;stdio.h&gt;</p>
<pre>
 int main()
 {
</pre>
<p>char password[] = &#8220;Jefe&#8221;;<br />
int keylen = 4;<br />
char data[] = &#8220;what do ya want for nothing?&#8221;;<br />
int datalen = 28;<br />
MHASH td;<br />
unsigned char mac[16];<br />
int j;</p>
<pre>
        td = mhash_hmac_init(MHASH_MD5, password, keylen,
                            mhash_get_hash_pblock(MHASH_MD5));
</pre>
<p>mhash(td, data, datalen);<br />
mhash_hmac_deinit(td, mac);</p>
<pre>
 /* 
  * The output should be 0x750c783e6ab0b503eaa86e310a5db738
  * according to RFC 2104.
  */
</pre>
<p>printf(&#8220;0x&#8221;);<br />
for (j = 0; j &lt; mhash_get_block_size(MHASH_MD5); j++) {<br />
    printf(&#8220;%.2x&#8221;, mac[j]);<br />
}<br />
printf(&#8220;
&#8221;);</p>
<pre><code>
exit(0);
}
</code></pre>
<h2>HISTORY</h2>
<p> This library was originally written by <i>Nikos Mavroyanopoulos</i> &lt;nmav [at] hellug.gr&gt; who passed the project over to <i>Sascha Schumann</i> &lt;sascha [at] schumann.cx&gt; in May 1999. Sascha maintained it until March 2000. The library is now maintained by <i>Nikos Mavroyanopoulos</i>.</p>
<h2>BUGS</h2>
<p> If you find any, please send a bug report (preferrably together with a patch) to the maintainer with a detailed description on how to reproduce the bug.</p>
<h2>AUTHORS</h2>
<p> Sascha Schumann &lt;sascha [at] schumann.cx&gt; Nikos Mavroyanopoulos &lt;nmav [at] hellug.gr&gt; </p>
<h2>Index</h2>
