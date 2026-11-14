---
title: "otpprint(1)"
name: "otpprint"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otpprint/"
description: "otpprint – print lists of one-time passwords"
---

<h2 class="name">NAME</h2>
<p> <code>otpprint</code> &#8211; print lists of one-time passwords </p>
<h2>SYNOPSIS</h2>
<p> <code>otp</code> [-<code>n </code><i>count</i> ] [-<code>e</code> ] [-<code>h</code> ] [-<code>f </code><i>algorithm</i> ] <i>sequence-number</i> <i>seed</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>otp</code> program prints lists of OTPs. </p>
<p> Use this to print out a series of one-time passwords. You will have to supply the <i>sequence number</i> and the <i>seed</i> as arguments and then the program will prompt you for your pass-phrase. </p>
<p> There are several different print formats. The default is to print each password with six short english words. </p>
<p> Options are:</p>
<dl>
<dt><code>-e</code></p>
<dd> Print the passwords in &#8220;extended&#8221; format. In this format a prefix that says &#8220;hex:&#8221; or &#8220;word:&#8221; is included.</p>
<dt><code>-f</code></p>
<dd> To choose a different <i>algorithm</i> from the default md5. Pick any of: md4, md5, and sha.</p>
<dt><code>-h</code></p>
<dd> Print the passwords in hex.</p>
<dt><code>-n</code></p>
<dd> Print <i>count</i> one-time passwords, starting at <i>sequence-number</i> and going backwards. The default is 10.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-otp/">otp</a>(1) </p>
<h2>Index</h2>
