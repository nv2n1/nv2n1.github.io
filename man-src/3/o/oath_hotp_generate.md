---
title: "oath_hotp_generate(3)"
name: "oath_hotp_generate"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_hotp_generate/"
description: "oath_hotp_generate – API function"
---

<p>oath_hotp_generate &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;oath.h&gt;
int oath_hotp_generate(const char *secret, size_t secret_length, uint64_t moving_factor, unsigned digits, bool add_checksum, size_t truncation_offset, char *output_otp);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * secret</p>
<dd>the shared secret string</p>
<dt>size_t secret_length</p>
<dd>length of <i>secret</i></p>
<dt>uint64_t moving_factor</p>
<dd>a counter indicating the current OTP to generate</p>
<dt>unsigned digits</p>
<dd>number of requested digits in the OTP, excluding checksum</p>
<dt>bool add_checksum</p>
<dd>whether to add a checksum digit or not</p>
<dt>size_t truncation_offset</p>
<dd>use a specific truncation offset</p>
<dt>char * output_otp</p>
<dd>output buffer, must have room for the output OTP plus zero</dl>
<h2>Description</h2>
<p>Generate a one-time-password using the HOTP algorithm as described in RFC 4226. </p>
<p> Use a value of <code>OATH_HOTP_DYNAMIC_TRUNCATION</code> for <i>truncation_offset</i> unless you really need a specific truncation offset. </p>
<p> To find out the size of the OTP you may use the <code>OATH_HOTP_LENGTH()</code> macro. The <i>output_otp</i> buffer must be have room for that length plus one for the terminating NUL. </p>
<p> Currently only values 6, 7 and 8 for <i>digits</i> are supported, and the <i>add_checksum</i> value is ignored. These restrictions may be lifted in future versions, although some limitations are inherent in the protocol.</p>
<h2>Returns</h2>
<p>On success, <code>OATH_OK</code> (zero) is returned, otherwise an error code is returned.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
