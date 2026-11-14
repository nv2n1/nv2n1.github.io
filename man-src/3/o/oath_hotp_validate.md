---
title: "oath_hotp_validate(3)"
name: "oath_hotp_validate"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_hotp_validate/"
description: "oath_hotp_validate – API function"
---

<p>oath_hotp_validate &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;oath.h&gt;
int oath_hotp_validate(const char *secret, size_t secret_length, uint64_t start_moving_factor, size_t window, const char *otp);</code></pre>
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
<dt>const char * otp</p>
<dd>the OTP to validate.</dl>
<h2>Description</h2>
<p>Validate an OTP according to OATH HOTP algorithm per RFC 4226. </p>
<p> Currently only OTP lengths of 6, 7 or 8 digits are supported. This restrictions may be lifted in future versions, although some limitations are inherent in the protocol.</p>
<h2>Returns</h2>
<p>Returns position in OTP window (zero is first position), or <code>OATH_INVALID_OTP</code> if no OTP was found in OTP window, or an error code.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
