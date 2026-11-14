---
title: "pwmake(1)"
name: "pwmake"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pwmake/"
description: "pwmake – simple tool for generating random relatively easily pronounceable passwords"
---

<h2>NAME</h2>
<p> pwmake &#8211; simple tool for generating random relatively easily pronounceable passwords</p>
<h2>SYNOPSIS</h2>
<p> <code>pwmake</code> &lt;entropy-bits&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>pwmake</code> is a simple configurable tool for generating random and relatively easily pronounceable passwords. The tool allows you to specify the number of entropy bits that are used to generate the password. </p>
<p> The entropy is pulled from <code>/dev/urandom</code>. </p>
<p> The minimum number of bits is <code>56</code> which is usable for passwords on systems/services where brute force attacks are of very limited rate of tries. The <code>64</code> bits should be adequate for applications where the attacker does not have direct access to the password hash file. For situations where the attacker might obtain the direct access to the password hash or the password is used as an encryption key <code>80</code> to <code>128</code> bits should be used depending on your level of paranoia. </p>
<h2>OPTIONS</h2>
<p> The first and only argument is the number of bits of entropy used to generate the password. </p>
<h2>FILES</h2>
<p> <code>/etc/security/pwquality.conf</code> &#8211; The configuration file for the libpwquality library. </p>
<h2>RETURN CODES</h2>
<p> <code>pwmake</code> returns 0 on success, non zero on error. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pwscore/">pwscore</a>(1), <a href="/docs/linux/man/8-pam_pwquality/">pam_pwquality</a>(8) </p>
<h2>AUTHORS</h2>
<pre>
Tomas Mraz &lt;tmraz [at] redhat.com&gt;
</pre>
<h2>Index</h2>
