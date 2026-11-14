---
title: "doveadm-pw(1)"
name: "doveadm-pw"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-pw/"
description: "doveadm-pw – Dovecot’s password hash generator"
---

<h2>NAME</h2>
<p> doveadm-pw &#8211; Dovecot&#8217;s password hash generator</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>pw -l</code><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>pw</code> [<code>-p</code> <i>password</i>] [<code>-r</code> <i>rounds</i>] [<code>-s</code> <i>scheme</i>] [<code>-u</code> <i>user</i>] [<code>-V</code>]<br />
 <code>doveadm</code> [<code>-Dv</code>] <code>pw -t</code> <i>hash</i> [<code>-p</code> <i>password</i>] [<code>-u</code> <i>user</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>doveadm pw</code> is used to generate password hashes for different password <i>scheme</i>s and optionally verify the generated hash. </p>
<p> All generated password hashes have a {<i>scheme</i>} prefix, for example {<code>SHA512-CRYPT.HEX</code>}. All passdbs have a default scheme for passwords stored without the {<i>scheme</i>} prefix. The default scheme can be overridden by storing the password with the scheme prefix. </p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<p> Command specific <i>options</i>:</p>
<dl>
<dt><code>-l</code></p>
<dd> List all supported password <i>scheme</i>s and exit successfully.<br />
 There are up to three optional password <i>scheme</i>s: <code>BLF-CRYPT</code> (Blowfish crypt), <code>SHA256-CRYPT&nbsp;<wbr></code>and <code>SHA512-CRYPT</code>. Their availability depends on the system&#8217;s currently used libc.</p>
<dt><code>-p&nbsp;<wbr></code><i>password</i></p>
<dd> The plain text <i>password</i> for which the hash should be generated. If no <i>password</i> was given <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will prompt interactively for one.</p>
<dt><code>-r&nbsp;<wbr></code><i>rounds</i></p>
<dd> The password <i>scheme</i>s <code>BLF-CRYPT</code>, <code>SHA256-CRYPT&nbsp;<wbr></code>and <code>SHA512-CRYPT</code> supports a variable number of encryption <i>rounds</i>. The following table shows the minimum/maximum number of encryption <i>rounds</i> per scheme. When the <code>-r</code> option was omitted the default number of encryption rounds will be applied. </p>
<pre><code>
Scheme | Minimum | Maximum | Default-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --BLF - CRYPT | 4 | 31 | 5 SHA256 - CRYPT | 1000 | 999999999 | 5000 SHA512 - CRYPT | 1000 | 999999999 | 5000
</code></pre>
<dt><code>-s&nbsp;<wbr></code><i>scheme</i></p>
<dd> The password <i>scheme</i> which should be used to generate the hashed password. By default the <code>CRAM-MD5&nbsp;<wbr></code><i>scheme</i> will be used. It is also possible to append an encoding suffix to the <i>scheme</i>. Supported encoding suffixes are: <code>.b64</code>, <code>.base64&nbsp;<wbr></code>and <code>.hex</code>.<br />
 See also <a rel="nofollow" href="http://wiki2.dovecot.org/Authentication/PasswordSchemes">http://wiki2.dovecot.org/Authentication/PasswordSchemes</a> for more details about password schemes.</p>
<dt><code>-t&nbsp;<wbr></code><i>hash</i></p>
<dd> Test if the given password <i>hash</i> matches a given plain text password. The plain text password may be passed using the <code>-p</code> option. When no password was specified, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will prompt interactively for one.</p>
<dt><code>-u&nbsp;<wbr></code><i>user</i></p>
<dd> When the <code>DIGEST-MD5&nbsp;<wbr></code><i>scheme</i> is used, also the <i>user</i> name must be given, because the user name is a part of the generated hash. For more information about Digest-MD5 please read also: <a rel="nofollow" href="http://wiki2.dovecot.org/Authentication/Mechanisms/DigestMD5">http://wiki2.dovecot.org/Authentication/Mechanisms/DigestMD5</a></p>
<dt><code>-V</code></p>
<dd> When this option is given, the hashed password will be internally verified. The result of the verification will be shown after the hashed password, enclosed in parenthesis.</dl>
<h2>EXAMPLE</h2>
<p> The first password hash is a DIGEST-MD5 hash for jane.roe [at] example.com. The second password hash is a CRAM-MD5 hash for john.doe [at] example.com. </p>
<pre><code>
doveadm pw - s digest - md5 - u jane.roe[at] example.com Enter new password : Retype new password:
{
    DIGEST - MD5
}
9b9dcb4466233a9307bbc33708dffda0 doveadm pw
    Enter new password : Retype new password:
{
    CRAM - MD5
}
913331d8782236a8ecba7764a63aa27b26437fd40ca878d887f11d81245c2c6b
</code></pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
