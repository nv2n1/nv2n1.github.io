---
title: "expect_mkpasswd(1)"
name: "expect_mkpasswd"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expect_mkpasswd/"
description: "mkpasswd – generate new password, optionally apply it to a user"
---

<h2 class="name">NAME</h2>
<p> mkpasswd &#8211; generate new password, optionally apply it to a user </p>
<h2>SYNOPSIS</h2>
<p> <code>mkpasswd</code> <i>[</i> <i>args</i> ] [ <i>user</i> ]</p>
<h2>INTRODUCTION</h2>
<p> <code>mkpasswd</code> generates passwords and can apply them automatically to users. mkpasswd is based on the code from Chapter 23 of the O&#8217;Reilly book &quot;Exploring Expect&quot;.</p>
<h2>USAGE</h2>
<p> With no arguments, <code>mkpasswd</code> returns a new password. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>mkpasswd</p>
<p> With a user name, <code>mkpasswd</code> assigns a new password to the user. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>mkpasswd don</p>
<p> The passwords are randomly generated according to the flags below. </p>
<h2>FLAGS</h2>
<p> The <code>-l</code> flag defines the length of the password. The default is 9. The following example creates a 20 character password. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>mkpasswd -l 20</p>
<p> The <code>-d</code> flag defines the minimum number of digits that must be in the password. The default is 2. The following example creates a password with at least 3 digits. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>mkpasswd -d 3</p>
<p> The <code>-c</code> flag defines the minimum number of lowercase alphabetic characters that must be in the password. The default is 2. </p>
<p> The <code>-C</code> flag defines the minimum number of uppercase alphabetic characters that must be in the password. The default is 2. </p>
<p> The <code>-s</code> flag defines the minimum number of special characters that must be in the password. The default is 1. </p>
<p> The <code>-p</code> flag names a program to set the password. By default, /etc/yppasswd is used if present, otherwise /bin/passwd is used. </p>
<p> The <code>-2</code> flag causes characters to be chosen so that they alternate between right and left hands (qwerty-style), making it harder for anyone watching passwords being entered. This can also make it easier for a password-guessing program. </p>
<p> The <code>-v</code> flag causes the password-setting interaction to be visible. By default, it is suppressed. </p>
<h2>EXAMPLE</h2>
<p> The following example creates a 15-character password that contains at least 3 digits and 5 uppercase characters. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>mkpasswd -l 15 -d 3 -C 5</p>
<h2>SEE ALSO</h2>
<p> <i>&quot;Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs&quot;</i> by Don Libes, O&#8217;Reilly and Associates, January 1995.</p>
<h2>AUTHOR</h2>
<p> Don Libes, National Institute of Standards and Technology </p>
<p> <code>mkpasswd</code> is in the public domain. NIST and I would appreciate credit if this program or parts of it are used. </p>
<h2>Index</h2>
