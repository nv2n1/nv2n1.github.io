---
title: "crypt_r(3)"
name: "crypt_r"
section: "3"
letter: "c"
url: "/docs/linux/man/3-crypt_r/"
description: "crypt , crypt_r , crypt_rn , crypt_ra – passphrase hashing"
---

<p>Openwall Project</p>
<h2 class="name">NAME</h2>
<p> <code>crypt , crypt_r , crypt_rn , crypt_ra</code> &#8211; passphrase hashing </p>
<h2>LIBRARY</h2>
<p> Lb libcrypt</p>
<h2>SYNOPSIS</h2>
<p> In crypt.h Ft char * Fo crypt Fa const char *phrase Fa const char *setting Fc Ft char * Fo crypt_r Fa const char *phrase Fa const char *setting Fa struct crypt_data *data Fc Ft char * Fo crypt_rn Fa const char *phrase Fa const char *setting Fa struct crypt_data *data Fa int size Fc Ft char * Fo crypt_ra Fa const char *phrase Fa const char *setting Fa void **data Fa int *size Fc</p>
<h2>DESCRIPTION</h2>
<p> The <code>crypt</code> <code>crypt_r</code> <code>crypt_rn</code> and <code>crypt_ra</code> functions irreversibly &#8220;hash&#8221; Fa phrase for storage in the system password database (<a href="/docs/linux/man/5-shadow/">shadow</a>(5) ) using a cryptographic &#8220;hashing method.&#8221; The result of this operation is called a &#8220;hashed passphrase&#8221; or just a &#8220;hash.&#8221; Hashing methods are described in <a href="/docs/linux/man/5-crypt/">crypt</a>(5). </p>
<p> Fa setting controls which hashing method to use, and also supplies various parameters to the chosen method, most importantly a random &#8220;salt&#8221; which ensures that no two stored hashes are the same, even if the Fa phrase strings are the same. </p>
<p> The Fa data argument to <code>crypt_r</code> is a structure of type Vt struct crypt_data . It has at least these fields: </p>
<blockquote>
<pre><code>
struct crypt_data {
    char output[CRYPT_OUTPUT_SIZE];
    char setting[CRYPT_OUTPUT_SIZE];
    char phrase[CRYPT_MAX_PASSPHRASE_SIZE];
    char initialized;
};
</code></pre>
</blockquote>
<p> Upon a successful return from <code>crypt_r</code> the hashed passphrase will be stored in Fa output . Applications are encouraged, but not required, to use the Fa phrase and Fa setting fields to store the strings that they will pass as Fa phrase and Fa setting to <code>crypt_r</code> This will make it easier to erase all sensitive data after it is no longer needed. </p>
<p> The Fa initialized field must be set to zero before the first time a Vt struct crypt_data object is first used in a call to Fn crypt_r . We recommend zeroing the entire object, not just Fa initialized and not just the documented fields, before the first use. (Of course, do this before storing anything in Fa setting and Fa phrase . ) </p>
<p> The Fa data argument to <code>crypt_rn</code> should also point to a Vt struct crypt_data object, and Fa size should be the size of that object, cast to Vt int . When used with <code>crypt_rn</code> the entire Fa data object (except for the Fa phrase and Fa setting fields) must be zeroed before its first use; this is not just a recommendation, as it is for <code>crypt_r</code> Otherwise, the fields of the object have the same uses that they do for <code>crypt_r</code> </p>
<p> On the first call to <code>crypt_ra</code> Fa data should be the address of a Vt void * variable set to NULL, and Fa size should be the address of an Vt int variable set to zero. <code>crypt_ra</code> will allocate and initialize a Vt struct crypt_data object, using <a href="/docs/linux/man/3-malloc/">malloc</a>(3), and write its address and size into the variables pointed to by Fa data and Fa size . These can be reused in subsequent calls. After the application is done hashing passphrases, it should deallocate the Vt struct crypt_data object using <a href="/docs/linux/man/3-free/">free</a>(3).</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, <code>crypt</code> <code>crypt_r</code> <code>crypt_rn</code> and <code>crypt_ra</code> return a pointer to a string which encodes both the hashed passphrase, and the settings that were used to encode it. This string is directly usable as Fa setting in other calls to <code>crypt</code> <code>crypt_r</code> <code>crypt_rn</code> and <code>crypt_ra</code> and as Fa prefix in calls to <code>crypt_gensalt</code> <code>crypt_gensalt_rn</code> and <code>crypt_gensalt_ra</code> It will be entirely printable ASCII, and will not contain whitespace or the characters `<code>:</code> &#8216; `<code>;</code> &#8216; `<code>*</code> &#8216; `<code>!</code> &#8216; or `<code>\</code> &#8216; See <a href="/docs/linux/man/5-crypt/">crypt</a>(5) for more detail on the format of hashed passphrases. </p>
<p> <code>crypt</code> places its result in a static storage area, which will be overwritten by subsequent calls to <code>crypt</code> It is not safe to call <code>crypt</code> from multiple threads simultaneously. </p>
<p> <code>crypt_r</code> <code>crypt_rn</code> and <code>crypt_ra</code> place their result in the Fa output field of their Fa data argument. It is safe to call them from multiple threads simultaneously, as long as a separate Fa data object is used for each thread. </p>
<p> Upon error, <code>crypt_r</code> <code>crypt_rn</code> and <code>crypt_ra</code> write an <i>invalid</i> hashed passphrase to the Fa output field of their Fa data argument, and <code>crypt</code> writes an invalid hash to its static storage area. This string will be shorter than 13 characters, will begin with a `<code>*</code> &#8216; and will not compare equal to Fa setting . </p>
<p> Upon error, <code>crypt_rn</code> and <code>crypt_ra</code> return a null pointer. <code>crypt_r</code> and <code>crypt</code> may also return a null pointer, or they may return a pointer to the invalid hash, depending on how libcrypt was configured. (The option to return the invalid hash is for compatibility with old applications that assume that <code>crypt</code> cannot return a null pointer. See Sx PORTABILITY NOTES below.) </p>
<p> All four functions set <i>errno</i> when they fail.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>Er </code>EINVAL</p>
<dd> Fa setting is invalid, or requests a hashing method that is not supported.</p>
<dt><code>Er </code>ERANGE</p>
<dd> Fa phrase is too long (more than <code>CRYPT_MAX_PASSPHRASE_SIZE</code> characters; some hashing methods may have lower limits).<br />
 <code>crypt_rn</code> only: Fa size is too small for the hashing method requested by Fa setting .</p>
<dt><code>Er </code>ENOMEM</p>
<dd> Failed to allocate internal scratch memory.<br />
 <code>crypt_ra</code> only: failed to allocate memory for Fa data .</p>
<dt><code>Er </code>ENOSYS <code>or Er </code>EOPNOTSUPP</p>
<dd> Hashing passphrases is not supported at all on this installation, or the hashing method requested by Fa setting is not supported. These error codes are not used by this version of libcrypt, but may be encountered on other systems.</dl>
<h2>PORTABILITY NOTES</h2>
<p> <code>crypt</code> is included in POSIX, but <code>crypt_r</code> <code>crypt_rn</code> and <code>crypt_ra</code> are not part of any standard. </p>
<p> POSIX does not specify any hashing methods, and does not require hashed passphrases to be portable between systems. In practice, hashed passphrases are portable as long as both systems support the hashing method that was used. However, the set of supported hashing methods varies considerably from system to system. </p>
<p> The behavior of <code>crypt</code> on errors isn&#8217;t well standardized. Some implementations simply can&#8217;t fail (except by crashing the program), others return a null pointer or a fixed string. Most implementations don&#8217;t set <i>errno</i> but some do. POSIX specifies returning a null pointer and setting <i>errno</i> but it defines only one possible error, Er ENOSYS , in the case where <code>crypt</code> is not supported at all. Some older applications are not prepared to handle null pointers returned by <code>crypt</code> The behavior described above for this implementation, setting <i>errno</i> and returning an invalid hashed passphrase different from Fa setting , is chosen to make these applications fail closed when an error occurs. </p>
<p> Due to historical restrictions on the export of cryptographic software from the USA, <code>crypt</code> is an optional POSIX component. Applications should therefore be prepared for <code>crypt</code> not to be available, or to always fail (setting <i>errno</i> to Er ENOSYS ) at runtime. </p>
<p> POSIX specifies that <code>crypt</code> is declared in In unistd.h , but only if the macro <code>_XOPEN_CRYPT</code> is defined and has a value greater than or equal to zero. Since libcrypt does not provide In unistd.h , it declares <code>crypt</code> <code>crypt_r</code> <code>crypt_rn</code> and <code>crypt_ra</code> in In crypt.h instead. </p>
<p> On a minority of systems (notably recent versions of Solaris), <code>crypt</code> uses a thread-specific static storage buffer, which makes it safe to call from multiple threads simultaneously, but does not prevent each call within a thread from overwriting the results of the previous one.</p>
<h2>BUGS</h2>
<p> Some implementations of <code>crypt</code> upon error, return an invalid hash that is stored in a read-only location or only initialized once, which means that it is only safe to erase the buffer pointed to by the <code>crypt</code> return value if an error did not occur. </p>
<p> Vt struct crypt_data may be quite large (32kB in this implementation of libcrypt; over 128kB in some other implementations). This is large enough that it may be unwise to allocate it on the stack. </p>
<p> Some recently designed hashing methods need even more scratch memory, but the <code>crypt_r</code> interface makes it impossible to change the size of Vt struct crypt_data without breaking binary compatibility. The <code>crypt_rn</code> interface could accommodate larger allocations for specific hashing methods, but the caller of <code>crypt_rn</code> has no way of knowing how much memory to allocate. <code>crypt_ra</code> does the allocation itself, but can only make a single call to <a href="/docs/linux/man/3-malloc/">malloc</a>(3).</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <a href="/docs/linux/man/7-attributes/">attributes</a>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>crypt</code> </td>
<td>Thread safety</td>
<td>MT-Unsafe race:crypt
</td>
</tr>
<tr VALIGN=top>
<td> <code>crypt_r</code> <code>crypt_rn</code> <code>crypt_ra</code> </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>HISTORY</h2>
<p> A rotor-based <code>crypt</code> function appeared in AT&amp;T System v6 . The &#8220;traditional&#8221; DES-based <code>crypt</code> first appeared in AT&amp;T System v7 . </p>
<p> <code>crypt_r</code> originates with the GNU C Library. There&#8217;s also a <code>crypt_r</code> function on HP-UX and MKS Toolkit, but the prototypes and semantics differ. </p>
<p> <code>crypt_rn</code> and <code>crypt_ra</code> originate with the Openwall project.</p>
<h2>SEE ALSO</h2>
<p> crypt_gensalt3, <a href="/docs/linux/man/3-getpass/">getpass</a>(3), <a href="/docs/linux/man/3-getpwent/">getpwent</a>(3), <a href="/docs/linux/man/3-shadow/">shadow</a>(3), <a href="/docs/linux/man/1-login/">login</a>(1), <a href="/docs/linux/man/1-passwd/">passwd</a>(1), <a href="/docs/linux/man/5-crypt/">crypt</a>(5), <a href="/docs/linux/man/5-passwd/">passwd</a>(5), <a href="/docs/linux/man/5-shadow/">shadow</a>(5), <a href="/docs/linux/man/8-pam/">pam</a>(8) </p>
<h2>Index</h2>
