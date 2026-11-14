---
title: "oath_authenticate_usersfile(3)"
name: "oath_authenticate_usersfile"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_authenticate_usersfile/"
description: "oath_authenticate_usersfile – API function"
---

<p>oath_authenticate_usersfile &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;oath.h&gt;
int oath_authenticate_usersfile(const char *usersfile, const char *username, const char *otp, size_t window, const char *passwd, time_t *last_otp);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * usersfile</p>
<dd>string with user credential filename, in UsersFile format</p>
<dt>const char * username</p>
<dd>string with name of user</p>
<dt>const char * otp</p>
<dd>string with one-time password to authenticate</p>
<dt>size_t window</p>
<dd>how many past/future OTPs to search</p>
<dt>const char * passwd</p>
<dd>string with password, or NULL to disable password checking</p>
<dt>time_t * last_otp</p>
<dd>output variable holding last successful authentication</dl>
<h2>Description</h2>
<p>Authenticate user named <i>username</i> with the one-time password <i>otp</i> and (optional) password <i>passwd</i>. Credentials are read (and updated) from a text file named <i>usersfile</i>. </p>
<p> Note that for TOTP the usersfile will only record the last OTP and use that to make sure more recent OTPs have not been seen yet when validating a new OTP. That logics relies on using the same search window for the same user.</p>
<h2>Returns</h2>
<p>On successful validation, <code>OATH_OK</code> is returned. If the supplied <i>otp</i> is the same as the last successfully authenticated one-time password, <code>OATH_REPLAYED_OTP</code> is returned and the timestamp of the last authentication is returned in <i>last_otp</i>. If the one-time password is not found in the indicated search window, <code>OATH_INVALID_OTP</code> is returned. Otherwise, an error code is returned.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
