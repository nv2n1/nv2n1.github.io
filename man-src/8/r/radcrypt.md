---
title: "radcrypt(8)"
name: "radcrypt"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radcrypt/"
description: "radcrypt – generate password hash for use with radius, or validates a password hash"
---

<p>radcrypt &#8211; generate password hash for use with radius, or validates a password hash</p>
<h2>Synopsis</h2>
<p><code>radcrypt</code> [<code>-d</code>|<code>&#8211;des</code>] [<code>-m</code>|<code>&#8211;md5</code>] [<code>-c</code>|<code>&#8211;check</code>] <i>plaintext_password</i> [<i>hashed_password</i>]</p>
<h2>Description</h2>
<p><code>radcrypt</code> generates a hashed digest of a plaintext password, or can validate if a password hash matches a plaintext password. DES and MD5 hashes are currently supported. When generating a password hash a random salt is generated and applied. A hashed password can be validated by specifying <i>-c</i> or <i>&#8211;check</i> and passing <i>hashed_password</i> after <i>plaintext_password</i> on the command line. In this case <i>hashed_password</i> will be checked to see if it matches <i>plaintext_password</i>. If so &quot;Password OK&quot; will be printed and the exit status will be 1, otherwise &quot;Password BAD&quot; will be printed and exit status will be 0 (Note this is the opposite of a normal successful shell status). </p>
<h2>Options</h2>
<dl>
<dt>-d &#8211;des</p>
<dd>Use a DES (Data Encryption Standard) hash (default). Ignored if performing a password check.</p>
<dt>-m &#8211;md5</p>
<dd>Use a MD5 (Message Digest 5) hash. Ignored if performing a password check.</p>
<dt>-c &#8211;check</p>
<dd>Perform a validation check on a password hash to verify if it matches the plantext password. </p>
</dl>
<h2>Examples</h2>
<pre>$ radcrypt foobar
HaX0xn7Qy650Q
$ radcrypt -c foobar HaX0xn7Qy650Q
Password OK</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-radiusd/">radiusd</a>(8), <a href="/docs/linux/man/3-crypt/">crypt</a>(3)</p>
<h2>Authors</h2>
<p>Miquel van Smoorenburg &lt;miquels [at] cistron-office.nl&gt;</p>
