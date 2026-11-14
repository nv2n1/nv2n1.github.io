---
title: "oath_hotp_validate_callback(3)"
name: "oath_hotp_validate_callback"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_hotp_validate_callback/"
description: "oath_hotp_validate_callback – API function"
---

<p>oath_hotp_validate_callback &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;oath.h&gt;
int oath_hotp_validate_callback(const char *secret, size_t secret_length, uint64_t start_moving_factor, size_t window, unsigned digits, oath_validate_strcmp_function strcmp_otp, void *strcmp_handle);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * secret</p>
<dd>the shared secret string</p>
<dt>size_t secret_length</p>
<dd>length of <i>secret</i></p>
<dt>uint64_t start_moving_factor</p>
<dd>start counter in OTP stream</p>
<dt>size_t window</p>
<dd>how many OTPs after start counter to test</p>
<dt>unsigned digits</p>
<dd>number of requested digits in the OTP</p>
<dt>oath_validate_strcmp_function strcmp_otp</p>
<dd>function pointer to a strcmp-like function.</p>
<dt>void * strcmp_handle</p>
<dd>caller handle to be passed on to <i>strcmp_otp</i>.</dl>
<h2>Description</h2>
<p>Validate an OTP according to OATH HOTP algorithm per RFC 4226. Validation is implemented by generating a number of potential OTPs and performing a call to the <i>strcmp_otp</i> function, to compare the potential OTP against the given <i>otp</i>. It has the following prototype: </p>
<pre><code>int (*oath_validate_strcmp_function)(void *handle, const char *test_otp);</code></pre>
<p> The function should be similar to strcmp in that it return 0 only on matches. It differs by permitting use of negative return codes as indication of internal failures in the callback. Positive values indicate OTP mismatch. This callback interface is useful when you cannot compare OTPs directly using normal strcmp, but instead for example only have a hashed OTP. You would then typically pass in the hashed OTP in the <i>strcmp_handle</i> and let your implementation of <i>strcmp_otp</i> hash the test_otp OTP using the same hash, and then compare the results. Currently only OTP lengths of 6, 7 or 8 digits are supported. This restrictions may be lifted in future versions, although some limitations are inherent in the protocol.</p>
<h2>Returns</h2>
<p>Returns position in OTP window (zero is first position), or <code>OATH_INVALID_OTP</code> if no OTP was found in OTP window, or an error code.</p>
<h2>Since</h2>
<p>1.4.0</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
