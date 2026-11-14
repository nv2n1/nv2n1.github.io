---
title: "oath_totp_generate(3)"
name: "oath_totp_generate"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_totp_generate/"
description: "oath_totp_generate – API function"
---

<p>oath_totp_generate &#8211; API function</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;oath.h&gt;</code> </p>
<p> <code>int oath_totp_generate(const char * </code><i>secret</i><code>, size_t </code><i>secret_length</i><code>, time_t </code><i>now</i><code>, unsigned </code><i>time_step_size</i><code>, time_t </code><i>start_offset</i><code>, unsigned </code><i>digits</i><code>, char * </code><i>output_otp</i><code>);</code></p>
<h2>Arguments</h2>
<dl COMPACT>
<dt>const char * secret</p>
<dd> the shared secret string</p>
<dt>size_t secret_length</p>
<dd> length of <i>secret</i></p>
<dt>time_t now</p>
<dd> Unix time value to compute TOTP for</p>
<dt>unsigned time_step_size</p>
<dd> time step system parameter (typically 30)</p>
<dt>time_t start_offset</p>
<dd> Unix time of when to start counting time steps (typically 0)</p>
<dt>unsigned digits</p>
<dd> number of requested digits in the OTP, excluding checksum</p>
<dt>char * output_otp</p>
<dd> output buffer, must have room for the output OTP plus zero</dl>
<h2>Description</h2>
<p> Generate a one-time-password using the time-variant TOTP algorithm described in RFC 6238. The input parameters are taken as time values. </p>
<p> The system parameter <i>time_step_size</i> describes how long the time window for each OTP is. The recommended value is 30 seconds, and you can use the value 0 or the symbol <code>OATH_TOTP_DEFAULT_TIME_STEP_SIZE</code> to indicate this. </p>
<p> The system parameter <i>start_offset</i> denote the Unix time when time steps are started to be counted. The recommended value is 0, to fall back on the Unix epoch) and you can use the symbol <code>OATH_TOTP_DEFAULT_START_TIME</code> to indicate this. </p>
<p> The <i>output_otp</i> buffer must have room for at least <i>digits</i> characters, plus one for the terminating NUL. </p>
<p> Currently only values 6, 7 and 8 for <i>digits</i> are supported. This restriction may be lifted in future versions.</p>
<h2>Returns</h2>
<p> On success, <code>OATH_OK</code> (zero) is returned, otherwise an error code is returned.</p>
<h2>Since</h2>
<p> 1.4.0</p>
<h2>Reporting Bugs</h2>
<p> Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p> Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
