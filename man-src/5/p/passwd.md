---
title: "passwd(5)"
name: "passwd"
section: "5"
letter: "p"
url: "/docs/linux/man/5-passwd/"
description: "passwd – the password file"
---

<p>passwd &#8211; the password file</p>
<h2>Description</h2>
<p>/etc/passwd contains one line for each user account, with seven fields delimited by colons (&#8220;:&#8221;). These fields are: </p>
<dl>
<dd>&bull; login name</dl>
<dl>
<dd>&bull; optional encrypted password</dl>
<dl>
<dd>&bull; numerical user ID</dl>
<dl>
<dd>&bull; numerical group ID</dl>
<dl>
<dd>&bull; user name or comment field</dl>
<dl>
<dd>&bull; user home directory</dl>
<dl>
<dd>&bull; optional user command interpreter</dl>
<p> If the <i>password</i> field is a lower-case &#8220;x&#8221;, then the encrypted password is actually stored in the <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5) file instead; there <i>must</i> be a corresponding line in the /etc/shadow file, or else the user account is invalid. </p>
<p> The encrypted <i>password</i> field may be empty, in which case no password is required to authenticate as the specified login name. However, some applications which read the /etc/passwd file may decide not to permit <i>any</i> access at all if the <i>password</i> field is blank. </p>
<p> A <i>password</i> field which starts with an exclamation mark means that the password is locked. The remaining characters on the line represent the <i>password</i> field before the password was locked. </p>
<p> Refer to <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) for details on how this string is interpreted. </p>
<p> If the password field contains some string that is not a valid result of <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3), for instance ! or *, the user will not be able to use a unix password to log in (but the user may log in the system by other means). </p>
<p> The comment field is used by various system utilities, such as <code><a href="/docs/linux/man/1-finger/">finger</a></code>(1). </p>
<p> The home directory field provides the name of the initial working directory. The <code>login</code> program uses this information to set the value of the <code>$HOME</code> environmental variable. </p>
<p> The command interpreter field provides the name of the user&#8217;s command language interpreter, or the name of the initial program to execute. The <code>login</code> program uses this information to set the value of the <code>$SHELL</code> environmental variable. If this field is empty, it defaults to the value /bin/sh.</p>
<h2>Files</h2>
<p>/etc/passwd</p>
<dl>
<dd>User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dd>optional encrypted password file</dl>
<p> /etc/passwd-</p>
<dl>
<dd>Backup file for /etc/passwd. </p>
<p> Note that this file is used by the tools of the shadow toolsuite, but not by all user and password management tools.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3), <code><a href="/docs/linux/man/1-getent/">getent</a></code>(1), <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/8-pwck/">pwck</a></code>(8), <code><a href="/docs/linux/man/8-pwconv/">pwconv</a></code>(8), <code><a href="/docs/linux/man/8-pwunconv/">pwunconv</a></code>(8), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/8-sulogin/">sulogin</a></code>(8). </p>
