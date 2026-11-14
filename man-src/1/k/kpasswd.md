---
title: "kpasswd(1)"
name: "kpasswd"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kpasswd/"
description: "kpasswd – change a user’s Kerberos password"
---

<h2>NAME</h2>
<p> kpasswd &#8211; change a user&#8217;s Kerberos password</p>
<h2>SYNOPSIS</h2>
<p> <code>kpasswd</code> [<i>principal</i>]</p>
<h2>DESCRIPTION</h2>
<p> The kpasswd command is used to change a Kerberos principal&#8217;s password. kpasswd first prompts for the current Kerberos password, then prompts the user twice for the new password, and the password is changed. </p>
<p> If the principal is governed by a policy that specifies the length and/or number of character classes required in the new password, the new password must conform to the policy. (The five character classes are lower case, upper case, numbers, punctuation, and all other characters.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>principal</i></p>
<dd> Change the password for the Kerberos principal principal. Otherwise, kpasswd uses the principal name from an existing ccache if there is one; if not, the principal is derived from the identity of the user invoking the kpasswd command.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i>, <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i></p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
