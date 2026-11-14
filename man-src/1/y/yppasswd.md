---
title: "yppasswd(1)"
name: "yppasswd"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yppasswd/"
description: "yppasswd, ypchfn, ypchsh – change your password in the NIS database"
---

<h2>NAME</h2>
<p> yppasswd, ypchfn, ypchsh &#8211; change your password in the NIS database</p>
<h2>SYNOPSIS</h2>
<p> <code>yppasswd [-f] [-l] [-p] [user]</code><br />
 <code>ypchfn [user]</code><br />
 <code>ypchsh [user]</code></p>
<h2>DESCRIPTION</h2>
<p> In the old days, the standard <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1) and <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1) tools could not be used under Linux to change the users NIS password, shell and GECOS information. For changing the NIS information, they were replaced by their NIS counterparts, <code>yppasswd</code>, <code>ypchfn</code> and <code>ypchsh</code>. </p>
<p> Today, this versions are deprecated and should not be used any longer. </p>
<p> Using the command line switches, you can choose whether to update your password <code>-p</code>, your login shell <code>-l</code>, or your GECOS field <code>-f</code>, or a combination of them. <code>yppasswd</code> implies the <code>-p</code> option, if no other option is given. If you use the <code>-f</code> or <code>-l</code> option, you also need to add the <code>-p</code> flag. <code>ypchfn</code> implies the <code>-f</code> option, and <code>ypchsh</code> <code>-l</code>. </p>
<p> When invoked without the <i>user</i> argument, the account information for the invoking user will be updated, otherwise that of <i>user</i> will be updated. This option is only available to the super-user. If the yppasswdd daemon on the server supports it, you can give the root password of the server instead of the users [old] password. </p>
<p> All tools will first prompt the user for the current NIS password needed for authentication with the <code><a href="/docs/linux/man/8-yppasswdd/">yppasswdd</a></code>(8) daemon. Subsequently, the program prompts for the updated information: </p>
<p> If we use shadowing passwords using passwd.adjunct, SHA-512 will be used for hashing a new password by default. If we want to use MD5, SHA_256 or older DES, we need to set the environment variable YP_PASSWD_HASH. Possible values are &quot;DES&quot;, &quot;MD5&quot;, &quot;SHA-256&quot; and &quot;SHA-512&quot; (value is case-insensitive).</p>
<dl>
<dt><code>yppasswd</code> or <code>-p</code></p>
<dd> Change the user&#8217;s NIS password.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>The user is prompted for the new password.<br />
 While typing the password, echoing is turned off, so the password does not appear on the screen. An empty password is rejected, as are passwords shorter than six characters. The user will then be requested to retype the password to make sure it wasn&#8217;t<tt>&nbsp;<wbr></tt>misspelled the first time.</p>
<dt><code>ypchsh</code> or <code>-l</code></p>
<dd> Change the user&#8217;s login shell. The user is prompted for a new shell, offering the old one as default:</p>
<dt>
<dd>
<pre>
Login shell [/bin/sh]: _
</pre>
<dt>
<dd> To accept the default, simply press return. To clear the shell field in your <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5) file entry (so that the system&#8217;s default shell is selected), enter the string <i>none</i>.</p>
<dt><code>ypchfn</code> or <code>-f</code></p>
<dd> Change the user&#8217;s full name and related information. Traditionally, some applications expect the GECOS field (field 4) of the <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5) file to contain the user&#8217;s real name (as opposed to the login name) plus some additional information like the office phone number. This information is displayed by <code><a href="/docs/linux/man/1-finger/">finger</a></code>(1) and probably some other tools, too.</p>
<dt>
<dd> When setting the full name, <code>ypchfn</code> displays the following prompts, with the defaults in brackets:</p>
<dt>
<dd>
<pre><code>
Name[Joe Doe] : Location[2nd floor, bldg 34] : Office Phone[12345] : Home Phone[]:
</code></pre>
<dt>
<dd> To accept a default, simply press return. To clear a field, enter the string <i>none</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-finger/">finger</a></code>(1), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/1-ypcat/">ypcat</a></code>(1), <code><a href="/docs/linux/man/8-yppasswdd/">yppasswdd</a></code>(8), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/1-ypwhich/">ypwhich</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> <code>yppasswd</code> is part of the <code>yp-tools</code> package, which was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;. </p>
<h2>Index</h2>
