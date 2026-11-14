---
title: "crypt_gensalt_rn(3)"
name: "crypt_gensalt_rn"
section: "3"
letter: "c"
url: "/docs/linux/man/3-crypt_gensalt_rn/"
description: "crypt_gensalt , crypt_gensalt_rn , crypt_gensalt_ra – encode settings for passphrase hashing"
---

<p>Openwall Project</p>
<h2 class="name">NAME</h2>
<p> <code>crypt_gensalt , crypt_gensalt_rn , crypt_gensalt_ra</code> &#8211; encode settings for passphrase hashing </p>
<h2>LIBRARY</h2>
<p> Lb libcrypt</p>
<h2>SYNOPSIS</h2>
<p> In crypt.h Ft char * Fo crypt_gensalt Fa const char *prefix Fa unsigned long count Fa const char *rbytes Fa int nrbytes Fc Ft char * Fo crypt_gensalt_rn Fa const char * prefix Fa unsigned long count Fa const char *rbytes Fa int nrbytes Fa char * output Fa int output_size Fc Ft char * Fo crypt_gensalt_ra Fa const char *prefix Fa unsigned long count Fa const char *rbytes Fa int nrbytes Fc</p>
<h2>DESCRIPTION</h2>
<p> The <code>crypt_gensalt</code> <code>crypt_gensalt_rn</code> and <code>crypt_gensalt_ra</code> functions compile a string for use as the Fa setting argument to <code>crypt</code> <code>crypt_r</code> <code>crypt_rn</code> and <code>crypt_ra</code> Fa prefix selects the hashing method to use. Fa count controls the CPU time cost of the hash; the valid range for Fa count and the exact meaning of &#8220;CPU time cost&#8221; depends on the hashing method, but larger numbers correspond to more costly hashes. Fa rbytes should point to Fa nrbytes cryptographically random bytes for use as &#8220;salt.&#8221; </p>
<p> If Fa prefix is a null pointer, the best available hashing method will be selected. Po Sy CAUTION : if Fa prefix is an empty string, the &#8220;traditional&#8221; DES-based hashing method will be selected; this method is unacceptably weak by modern standards. Pc If Fa count is 0, a low default cost will be selected. If Fa rbytes is a null pointer, an appropriate number of random bytes will be obtained from the operating system, and Fa nrbytes is ignored. </p>
<p> See <a href="/docs/linux/man/5-crypt/">crypt</a>(5) for other strings that can be used as Fa prefix , and valid values of Fa count for each.</p>
<h2>RETURN VALUES</h2>
<p> <code>crypt_gensalt</code> <code>crypt_gensalt_rn</code> and <code>crypt_gensalt_ra</code> return a pointer to an encoded setting string. This string will be entirely printable ASCII, and will not contain whitespace or the characters `<code>:</code> &#8216; `<code>;</code> &#8216; `<code>*</code> &#8216; `<code>!</code> &#8216; or `<code>\</code> &#8216; See <a href="/docs/linux/man/5-crypt/">crypt</a>(5) for more detail on the format of this string. Upon error, they return a null pointer and set <i>errno</i> to an appropriate error code. </p>
<p> <code>crypt_gensalt</code> places its result in a static storage area, which will be overwritten by subsequent calls to <code>crypt_gensalt</code> It is not safe to call <code>crypt_gensalt</code> from multiple threads simultaneously. However, it <i>is</i> safe to pass the string returned by <code>crypt_gensalt</code> directly to <code>crypt</code> without copying it; each function has its own static storage area. </p>
<p> <code>crypt_gensalt_rn</code> places its result in the supplied Fa output buffer, which has Fa output_size bytes of storage available. Fa output_size should be greater than or equal to <code>CRYPT_GENSALT_OUTPUT_SIZE</code> </p>
<p> <code>crypt_gensalt_ra</code> allocates memory for its result using <a href="/docs/linux/man/3-malloc/">malloc</a>(3). It should be freed with <a href="/docs/linux/man/3-free/">free</a>(3) after use. </p>
<p> Upon error, in addition to returning a null pointer, <code>crypt_gensalt</code> and <code>crypt_gensalt_rn</code> will write an invalid setting string to their output buffer, if there is enough space; this string will begin with a `<code>*</code> &#8216; and will not be equal to Fa prefix .</p>
<h2>ERRORS</h2>
<dl>
<dt><code>Er </code>EINVAL</p>
<dd> Fa prefix is invalid or not supported by this implementation; Fa count is invalid for the requested Fa prefix ; the input Fa nrbytes is insufficient for the smallest valid salt with the requested Fa prefix .</p>
<dt><code>Er </code>ERANGE</p>
<dd> <code>crypt_gensalt_rn</code> only: Fa output_size is too small to hold the compiled Fa setting string.</p>
<dt><code>Er </code>ENOMEM</p>
<dd> Failed to allocate internal scratch memory.<br />
 <code>crypt_gensalt_ra</code> only: failed to allocate memory for the compiled Fa setting string.</p>
<dt><code>Er </code>ENOSYS , EACCES , EIO , <code>etc.</code></p>
<dd> Obtaining random bytes from the operating system failed. This can only happen when Fa rbytes is a null pointer.</dl>
<h2>FEATURE TEST MACROS</h2>
<p> The following macros are defined by In crypt.h :</p>
<dl>
<dt><code>CRYPT_GENSALT_IMPLEMENTS_DEFAULT_PREFIX</code></p>
<dd> A null pointer can be specified as the Fa prefix argument.</p>
<dt><code>CRYPT_GENSALT_IMPLEMENTS_AUTO_ENTROPY</code></p>
<dd> A null pointer can be specified as the Fa rbytes argument.</dl>
<h2>PORTABILITY NOTES</h2>
<p> The functions <code>crypt_gensalt</code> <code>crypt_gensalt_rn</code> and <code>crypt_gensalt_ra</code> are not part of any standard. They originate with the Openwall project. A function with the name <code>crypt_gensalt</code> also exists on Solaris 10 and newer, but its prototype and semantics differ. </p>
<p> The default prefix and auto entropy features are available since libxcrypt version 4.0.0. Portable software can use feature test macros to find out whether null pointers can be used for the Fa prefix and Fa rbytes arguments. </p>
<p> The set of supported hashing methods varies considerably from system to system.</p>
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
<td> <code>crypt_gensalt</code> </td>
<td>Thread safety</td>
<td>MT-Unsafe race:crypt_gensalt
</td>
</tr>
<tr VALIGN=top>
<td> <code>crypt_gensalt_rn</code> <code>crypt_gensalt_ra</code> </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-crypt/">crypt</a>(3), <a href="/docs/linux/man/3-getpass/">getpass</a>(3), <a href="/docs/linux/man/3-getpwent/">getpwent</a>(3), <a href="/docs/linux/man/3-shadow/">shadow</a>(3), <a href="/docs/linux/man/1-login/">login</a>(1), <a href="/docs/linux/man/1-passwd/">passwd</a>(1), <a href="/docs/linux/man/5-crypt/">crypt</a>(5), <a href="/docs/linux/man/5-passwd/">passwd</a>(5), <a href="/docs/linux/man/5-shadow/">shadow</a>(5), <a href="/docs/linux/man/8-pam/">pam</a>(8) </p>
<h2>Index</h2>
