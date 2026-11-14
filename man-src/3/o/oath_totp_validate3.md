---
title: "oath_totp_validate3(3)"
name: "oath_totp_validate3"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_totp_validate3/"
description: "oath_totp_validate3 – API function"
---

<p>oath_totp_validate3 &#8211; API function</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;oath.h&gt;</code> </p>
<p> <code>int oath_totp_validate3(const char * </code><i>secret</i><code>, size_t </code><i>secret_length</i><code>, time_t </code><i>now</i><code>, unsigned </code><i>time_step_size</i><code>, time_t </code><i>start_offset</i><code>, size_t </code><i>window</i><code>, int * </code><i>otp_pos</i><code>, uint64_t * </code><i>otp_counter</i><code>, const char * </code><i>otp</i><code>);</code></p>
<h2>Arguments</h2>
<dl COMPACT>
<dt>const char * secret</p>
<dd> the shared secret string</p>
<dt>size_t secret_length</p>
<dd> length of <i>secret</i></p>
<dt>time_t now</p>
<dd> Unix time value to validate TOTP for</p>
<dt>unsigned time_step_size</p>
<dd> time step system parameter (typically 30)</p>
<dt>time_t start_offset</p>
<dd> Unix time of when to start counting time steps (typically 0)</p>
<dt>size_t window</p>
<dd> how many OTPs after/before start OTP to test</p>
<dt>int * otp_pos</p>
<dd> output search position in search window (may be NULL).</p>
<dt>uint64_t * otp_counter</p>
<dd> counter value used to calculate OTP value (may be NULL).</p>
<dt>const char * otp</p>
<dd> the OTP to validate.</dl>
<h2>Description</h2>
<p> Validate an OTP according to OATH TOTP algorithm per RFC 6238. </p>
<p> Currently only OTP lengths of 6, 7 or 8 digits are supported. This restrictions may be lifted in future versions, although some limitations are inherent in the protocol.</p>
<h2>Returns</h2>
<p> Returns absolute value of position in OTP window (zero is first position), or <code>OATH_INVALID_OTP</code> if no OTP was found in OTP window, or an error code.</p>
<h2>Since</h2>
<p> 2.4.0</p>
<h2>Reporting Bugs</h2>
<p> Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p> Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
