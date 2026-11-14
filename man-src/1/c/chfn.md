---
title: "chfn(1)"
name: "chfn"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chfn/"
description: "chfn – change real user name and information"
---

<h2 class="name">NAME</h2>
<p> chfn &#8211; change real user name and information </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>chfn</code> [<i>options</i>] [<i>LOGIN</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>chfn</code> command changes user fullname, office room number, office phone number, and home phone number information for a user&#8217;s account. This information is typically printed by <code><a href="/docs/linux/man/1-finger/">finger</a></code>(1) and similar programs. A normal user may only change the fields for her own account, subject to the restrictions in /etc/login.defs. (The default configuration is to prevent users from changing their fullname.) The superuser may change any field for any account. Additionally, only the superuser may use the <code>-o</code> option to change the undefined portions of the GECOS field. </p>
<p> These fields must not contain any colons. Except for the <i>other</i> field, they should not contain any comma or equal sign. It is also recommended to avoid non-US-ASCII characters, but this is only enforced for the phone numbers. The <i>other</i> field is used to store accounting information used by other applications.</p>
<h2>OPTIONS</h2>
<p> The options which apply to the <code>chfn</code> command are: </p>
<p> <code>-f</code>, <code>&#8211;full-name</code>&nbsp;<i>FULL_NAME</i></p>
<dl>
<dt>
<dd> Change the user&#8217;s full name.</dl>
<p> <code>-h</code>, <code>&#8211;home-phone</code>&nbsp;<i>HOME_PHONE</i></p>
<dl>
<dt>
<dd> Change the user&#8217;s home phone number.</dl>
<p> <code>-o</code>, <code>&#8211;other</code>&nbsp;<i>OTHER</i></p>
<dl>
<dt>
<dd> Change the user&#8217;s other GECOS information. This field is used to store accounting information used by other applications, and can be changed only by a superuser.</dl>
<p> <code>-r</code>, <code>&#8211;room</code>&nbsp;<i>ROOM_NUMBER</i></p>
<dl>
<dt>
<dd> Change the user&#8217;s room number.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dt>
<dd> Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-u</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<p> <code>-w</code>, <code>&#8211;work-phone</code>&nbsp;<i>WORK_PHONE</i></p>
<dl>
<dt>
<dd> Change the user&#8217;s office phone number.</dl>
<p> If none of the options are selected, <code>chfn</code> operates in an interactive fashion, prompting the user with the current values for all of the fields. Enter the new value to change the field, or leave the line blank to use the current value. The current value is displayed between a pair of <code>[ ]</code> marks. Without options, <code>chfn</code> prompts for the current user account.</p>
<h2>CONFIGURATION</h2>
<p> The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>CHFN_RESTRICT</code> (string)</p>
<dl>
<dt>
<dd> This parameter specifies which values in the <i>gecos</i> field of the /etc/passwd file may be changed by regular users using the <code>chfn</code> program. It can be any combination of letters <i>f</i>, <i>r</i>, <i>w</i>, <i>h</i>, for Full name, Room number, Work phone, and Home phone, respectively. For backward compatibility, <i>yes</i> is equivalent to <i>rwh</i> and <i>no</i> is equivalent to <i>frwh</i>. If not specified, only the superuser can make any changes. The most restrictive setting is better achieved by not installing <code>chfn</code> SUID.</dl>
<h2>FILES</h2>
<p> /etc/login.defs</p>
<dl>
<dt>
<dd> Shadow password suite configuration.</dl>
<p> /etc/passwd</p>
<dl>
<dt>
<dd> User account information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5). </p>
<h2>Index</h2>
