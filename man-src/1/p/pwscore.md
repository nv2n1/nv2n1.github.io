---
title: "pwscore(1)"
name: "pwscore"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pwscore/"
description: "pwscore – simple configurable tool for checking quality of a password"
---

<h2>NAME</h2>
<p> pwscore &#8211; simple configurable tool for checking quality of a password</p>
<h2>SYNOPSIS</h2>
<p> <code>pwscore</code> [user]</p>
<h2>DESCRIPTION</h2>
<p> <code>pwscore</code> is a simple tool for checking quality of a password. The password is read from stdin. </p>
<p> The tool uses the <code>libpwquality</code> library to perform configurable checks for minimum length, dictionary checking against cracklib dictionaries, and other checks. </p>
<p> It either reports an error if the password fails any of the checks, or it prints out the password quality score as an integer value between <code>0</code> and <code>100</code>. </p>
<p> The password quality score is relative to the <code>minlen</code> setting in the configuration file. But in general values below 50 can be treated as moderate quality and above it fairly strong quality. Any password that passes the quality checks (especially the mandatory cracklib check) should withstand dictionary attacks and scores above 50 with the default minlen setting even fast brute force attacks. </p>
<h2>OPTIONS</h2>
<p> The first and only optional argument is the user name that is used to check the similarity of the password to the username. </p>
<h2>FILES</h2>
<p> <code>/etc/security/pwquality.conf</code> &#8211; The configuration file for the libpwquality library. </p>
<h2>RETURN CODES</h2>
<p> <code>pwscore</code> returns 0 on success, non zero on error. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pwscore/">pwscore</a>(1), <a href="/docs/linux/man/5-pwquality-conf/">pwquality.conf</a>(5), <a href="/docs/linux/man/8-pam_pwquality/">pam_pwquality</a>(8) </p>
<h2>AUTHORS</h2>
<pre>
Tomas Mraz &lt;tmraz [at] redhat.com&gt;
</pre>
<h2>Index</h2>
