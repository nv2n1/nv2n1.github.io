---
title: "expiry(1)"
name: "expiry"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expiry/"
description: "expiry – check and enforce password expiration policy"
---

<h2 class="name">NAME</h2>
<p> expiry &#8211; check and enforce password expiration policy </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>expiry</code> <i>option</i></dt></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>expiry</code> command checks (<code>-c</code>) the current password expiration and forces (<code>-f</code>) changes when required. It is callable as a normal user command.</dd>
<h2>OPTIONS</h2>
<p> The options which apply to the <code>expiry</code> command are: </p>
<p> <code>-c</code>, <code>&#8211;check</code></p>
<dl>
<dt>
</dt><dd> Check the password expiration of the current user.</dd></dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
</dt><dd> Force a password change if the current user has an expired password.</dd></dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Display help message and exit.</dd></dl>
<h2>FILES</h2>
<p> /etc/passwd</p>
<dl>
<dt>
</dt><dd> User account information.</dd></dl>
<p> /etc/shadow</p>
<dl>
<dt>
</dt><dd> Secure user account information.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5). </p>
