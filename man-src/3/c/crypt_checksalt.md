---
title: "crypt_checksalt(3)"
name: "crypt_checksalt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-crypt_checksalt/"
description: "crypt_checksalt – validate a crypt setting string"
---

<p>libxcrypt</p>
<h2 class="name">NAME</h2>
<p> <code>crypt_checksalt</code> &#8211; validate a crypt setting string </p>
<h2>LIBRARY</h2>
<p> Lb libcrypt</p>
<h2>SYNOPSIS</h2>
<p> In crypt.h Ft int Fo crypt_checksalt Fa const char *setting Fc</p>
<h2>DESCRIPTION</h2>
<p> <code>crypt_checksalt</code> checks the <i>setting</i> string against the system configuration and reports whether the hashing method and parameters it specifies are acceptable. It is intended to be used by programs such as <a href="/docs/linux/man/1-login/">login</a>(1) to determine whether the user&#8217;s passphrase should be re-hashed using the currently preferred hashing method.</p>
<h2>RETURN VALUES</h2>
<p> The return value is 0 if there is nothing wrong with this setting. Otherwise, it is one of the following constants:</p>
<dl>
<dt><code>CRYPT_SALT_OK</code></p>
<dd> <i>setting</i> is a fully correct setting string. This constant is guaranteed to equal 0.</p>
<dt><code>CRYPT_SALT_INVALID</code></p>
<dd> <i>setting</i> is not a valid setting string; either it specifies a hashing method that is not known to this version of libxcrypt, or it specifies invalid parameters for the method.</p>
<dt><code>CRYPT_SALT_METHOD_DISABLED (Not implemented, yet)</code></p>
<dd> <i>setting</i> specifies a hashing method that is no longer allowed to be used at all; <code>crypt</code> will fail if passed this <i>setting</i> Manual intervention will be required to reactivate the user&#8217;s account.</p>
<dt><code>CRYPT_SALT_METHOD_LEGACY</code></p>
<dd> <i>setting</i> specifies a hashing method that is no longer considered strong enough for use with new passphrases. <code>crypt</code> will still authenticate a passphrase against this setting, but if authentication succeeds, the passphrase should be re-hashed using the currently preferred method.</p>
<dt><code>CRYPT_SALT_TOO_CHEAP (Not implemented, yet)</code></p>
<dd> <i>setting</i> specifies cost parameters that are considered too cheap for use with new passphrases. <code>crypt</code> will still authenticate a passphrase against this setting, but if authentication succeeds, the passphrase should be re-hashed using the currently preferred method.</dl>
<h2>FEATURE TEST MACROS</h2>
<p> In crypt.h will define the macro <code>CRYPT_CHECKSALT_AVAILABLE</code> if <code>crypt_checksalt</code> is available in the current version of libxcrypt.</p>
<h2>BUGS</h2>
<p> Since full configurability is not yet implemented, the current implementation will only ever return <code>CRYPT_SALT_OK (0)</code> or <code>CRYPT_SALT_INVALID</code> when invoked.</p>
<h2>PORTABILITY NOTES</h2>
<p> The function <code>crypt_checksalt</code> is not part of any standard. It was added to libxcrypt in version 4.3.0.</p>
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
<td> <code>crypt_checksalt</code> </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-crypt/">crypt</a>(3), crypt_gensalt3, <a href="/docs/linux/man/5-crypt/">crypt</a>(5) </p>
<h2>Index</h2>
