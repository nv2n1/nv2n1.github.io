---
title: "shadow(5)"
name: "shadow"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shadow/"
description: "shadow – shadowed password file"
---

<p>shadow &#8211; shadowed password file</p>
<h2>Description</h2>
<p>shadow is a file which contains the password information for the system&#8217;s accounts and optional aging information. </p>
<p> This file must not be readable by regular users if password security is to be maintained. </p>
<p> Each line of this file contains 9 fields, separated by colons (&#8220;:&#8221;), in the following order: </p>
<p> <code>login name</code></p>
<dl>
<dd>It must be a valid account name, which exist on the system.</dl>
<p> <code>encrypted password</code></p>
<dl>
<dd>This field may be empty, in which case no passwords are required to authenticate as the specified login name. However, some applications which read the /etc/shadow file may decide not to permit any access at all if the password field is empty. </p>
<p> A password field which starts with an exclamation mark means that the password is locked. The remaining characters on the line represent the password field before the password was locked. </p>
<p> Refer to <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) for details on how this string is interpreted. </p>
<p> If the password field contains some string that is not a valid result of <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3), for instance ! or *, the user will not be able to use a unix password to log in (but the user may log in the system by other means).</dl>
<p> <code>date of last password change</code></p>
<dl>
<dd>The date of the last password change, expressed as the number of days since Jan 1, 1970. </p>
<p> The value 0 has a special meaning, which is that the user should change her password the next time she will log in the system. </p>
<p> An empty field means that password aging features are disabled.</dl>
<p> <code>minimum password age</code></p>
<dl>
<dd>The minimum password age is the number of days the user will have to wait before she will be allowed to change her password again. </p>
<p> An empty field and value 0 mean that there are no minimum password age.</dl>
<p> <code>maximum password age</code></p>
<dl>
<dd>The maximum password age is the number of days after which the user will have to change her password. </p>
<p> After this number of days is elapsed, the password may still be valid. The user should be asked to change her password the next time she will log in. </p>
<p> An empty field means that there are no maximum password age, no password warning period, and no password inactivity period (see below). </p>
<p> If the maximum password age is lower than the minimum password age, the user cannot change her password.</dl>
<p> <code>password warning period</code></p>
<dl>
<dd>The number of days before a password is going to expire (see the maximum password age above) during which the user should be warned. </p>
<p> An empty field and value 0 mean that there are no password warning period.</dl>
<p> <code>password inactivity period</code></p>
<dl>
<dd>The number of days after a password has expired (see the maximum password age above) during which the password should still be accepted (and the user should update her password during the next login). </p>
<p> After expiration of the password and this expiration period is elapsed, no login is possible using the current user&#8217;s password. The user should contact her administrator. </p>
<p> An empty field means that there are no enforcement of an inactivity period.</dl>
<p> <code>account expiration date</code></p>
<dl>
<dd>The date of expiration of the account, expressed as the number of days since Jan 1, 1970. </p>
<p> Note that an account expiration differs from a password expiration. In case of an account expiration, the user shall not be allowed to login. In case of a password expiration, the user is not allowed to login using her password. </p>
<p> An empty field means that the account will never expire. </p>
<p> The value 0 should not be used as it is interpreted as either an account with no expiration, or as an expiration on Jan 1, 1970.</dl>
<p> <code>reserved field</code></p>
<dl>
<dd>This field is reserved for future use.</dl>
<h2>Files</h2>
<p>/etc/passwd</p>
<dl>
<dd>User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dd>Secure user account information.</dl>
<p> /etc/shadow-</p>
<dl>
<dd>Backup file for /etc/shadow. </p>
<p> Note that this file is used by the tools of the shadow toolsuite, but not by all user and password management tools.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chage/">chage</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/8-pwck/">pwck</a></code>(8), <code><a href="/docs/linux/man/8-pwconv/">pwconv</a></code>(8), <code><a href="/docs/linux/man/8-pwunconv/">pwunconv</a></code>(8), <code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/8-sulogin/">sulogin</a></code>(8). </p>
