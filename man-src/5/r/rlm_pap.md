---
title: "rlm_pap(5)"
name: "rlm_pap"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_pap/"
description: "rlm_pap – FreeRADIUS Module"
---

<p>rlm_pap &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_pap</i> module authenticates RADIUS Access-Request packets that contain a User-Password attribute. The module should also be listed last in the <i>authorize</i> section, so that it can set the Auth-Type attribute as appropriate. </p>
<p> When a RADIUS packet contains a clear-text password in the form of a User-Password attribute, the <i>rlm_pap</i> module may be used for authentication. The module requires a &quot;known good&quot; password, which it uses to validate the password given in the RADIUS packet. That &quot;known good&quot; password must be supplied by another module (e.g. <i>rlm_files</i>, <i>rlm_ldap</i>, etc.), and is usually taken from a database.</p>
<h2>Configuration</h2>
<p>The only relevant configuration item is:</p>
<dl>
<dt>normify</p>
<dd>The default is &quot;yes&quot;. This means that the module will try to convert hex passwords and base64-encoded passwords to &quot;normalized&quot; form. However, some clear text passwords may be erroneously converted. Setting this to &quot;no&quot; prevents that conversion.</dl>
<p> The module looks for the Password-With-Header attribute to find the &quot;known good password. The header is given by the following table. </p>
<dl>
<dd>
<pre><br>
Header Attribute Description
<br>
------ --------- -----------
<br>
{clear} Cleartext-Password clear-text passwords
<br>
{cleartext} Cleartext-Password clear-text passwords
<br>
{crypt} Crypt-Password Unix-style &quot;crypt&quot;ed passwords
<br>
{md5} MD5-Password MD5 hashed passwords
<br>
{smd5} SMD5-Password MD5 hashed passwords, with a salt
<br>
{sha} SHA-Password SHA1 hashed passwords
<br>
{ssha} SSHA-Password SHA1 hashed passwords, with a salt
<br>
{nt} NT-Password Windows NT hashed passwords
<br>
{x-nthash} NT-Password Windows NT hashed passwords
<br>
{lm} LM-Password Windows Lan Manager (LM) passwords.</pre>
</dl>
<p> The module tries to be flexible when handling the various password formats. It will automatically handle Base-64 encoded data, hex strings, and binary data, and convert them to a format that the server can use. </p>
<p> If there is no Password-With-Header attribute, the module looks for Cleartext-Password, NT-Password, Crypt-Password, etc. </p>
<p> It is important to understand the difference between the User-Password and Cleartext-Password attributes. The Cleartext-Password attribute is the &quot;known good&quot; password for the user. Simply supplying the Cleartext-Password to the server will result in most authentication methods working. The User-Password attribute is the password as typed in by the user on their private machine. The two are not the same, and should be treated very differently. That is, you should generally not use the User-Password attribute anywhere in the RADIUS configuration. </p>
<p> For backwards compatibility, there are old configuration parameters which may be work, although we do not recommend using them.</p>
<h2>Sections</h2>
<p><code>authorize</code> <code>authenticate</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] freeradius.org&gt;</p>
