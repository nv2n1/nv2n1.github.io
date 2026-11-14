---
title: "chsh(1)"
name: "chsh"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chsh/"
description: "chsh – change login shell"
---

<h2 class="name">NAME</h2>
<p> chsh &#8211; change login shell </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>chsh</code> [<i>options</i>] [<i>LOGIN</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>chsh</code> command changes the user login shell. This determines the name of the user&#8217;s initial login command. A normal user may only change the login shell for her own account; the superuser may change the login shell for any account.</p>
<h2>OPTIONS</h2>
<p> The options which apply to the <code>chsh</code> command are: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dt>
<dd> Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-s</code>, <code>&#8211;shell</code>&nbsp;<i>SHELL</i></p>
<dl>
<dt>
<dd> The name of the user&#8217;s new login shell. Setting this field to blank causes the system to select the default login shell.</dl>
<p> If the <code>-s</code> option is not selected, <code>chsh</code> operates in an interactive fashion, prompting the user with the current login shell. Enter the new value to change the shell, or leave the line blank to use the current one. The current shell is displayed between a pair of <i>[ ]</i> marks.</p>
<h2>NOTE</h2>
<p> The only restriction placed on the login shell is that the command name must be listed in /etc/shells, unless the invoker is the superuser, and then any value may be added. An account with a restricted login shell may not change her login shell. For this reason, placing /bin/rsh in /etc/shells is discouraged since accidentally changing to a restricted shell would prevent the user from ever changing her login shell back to its original value.</p>
<h2>FILES</h2>
<p> /etc/passwd</p>
<dl>
<dt>
<dd> User account information.</dl>
<p> /etc/shells</p>
<dl>
<dt>
<dd> List of valid login shells.</dl>
<p> /etc/login.defs</p>
<dl>
<dt>
<dd> Shadow password suite configuration.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5). </p>
<h2>Index</h2>
