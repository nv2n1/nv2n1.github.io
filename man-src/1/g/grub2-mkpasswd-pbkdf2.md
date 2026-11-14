---
title: "grub2-mkpasswd-pbkdf2(1)"
name: "grub2-mkpasswd-pbkdf2"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-mkpasswd-pbkdf2/"
description: "grub-mkpasswd-pbkdf2 — Generate a PBKDF2 password hash."
---

<h2>NAME</h2>
<p> <code>grub-mkpasswd-pbkdf2</code> &#8212; Generate a PBKDF2 password hash. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mkpasswd-pbkdf2</code> [-c | &#8211;iteration-count=<i>NUM</i>] [-l | &#8211;buflen=<i>NUM</i>]</p>
<dl>
<dt>
<dd> [-s | &#8211;salt=<i>NUM</i>] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-mkpasswd-pbkdf2</code> generates a PBKDF2 password string suitable for use in a GRUB configuration file. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;iteration-count=<i>NUM</i></p>
<dd> Number of PBKDF2 iterations. </p>
<dt>&#8211;buflen=<i>NUM</i></p>
<dd> Length of generated hash. </p>
<dt>&#8211;salt=<i>NUM</i></p>
<dd> Length of salt to use. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>
