---
title: "pwqgen(1)"
name: "pwqgen"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pwqgen/"
description: "pwqgen – Generate quality controllable random passphrase"
---

<h2 class="name">NAME</h2>
<p> <code>pwqgen</code> &#8211; Generate quality controllable random passphrase </p>
<h2>SYNOPSIS</h2>
<p> [<i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>Op Ar options</code> program generates a random passphrase using the libpasswdqc library. Strength of the generated passphrase depends on the amount of randomness read from /dev/urandom</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>random = </code><i>N</i></p>
<dd> (default: <code>random = 47</code> ) The size of randomly-generated passphrase in bits (24 to 85).</p>
<dt><code>config = </code><i>FILE</i></p>
<dd> Load config <i>FILE</i> in the <code>passwdqc.conf</code> format. This file may define any options described in passwdqc.conf5,butonlythe <code>random</code> and <code>config</code> options are honored by <code>.</code></p>
<dt><code>&#8211;version</code></p>
<dd> Output <code>Op Ar options</code> program version and exit.</p>
<dt><code>-h , &#8211;help</code></p>
<dd> Output <code>Op Ar options</code> help text and exit.</dl>
<h2>EXIT STATUS</h2>
<p> <code>Op Ar options</code> exits with non-zero status when it encounters invalid config file, invalid option, invalid parameter value, when it fails to obtain enough randomness, and in any case when it fails to generate a passphrase.</p>
<h2>FILES</h2>
<p> /etc/passwdqc.conf</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pwqcheck/">pwqcheck</a>(1), <a href="/docs/linux/man/4-urandom/">urandom</a>(4), passwdqc.conf5, pam_passwdqc8. </p>
<p> <a rel="nofollow" href="http://www.openwall.com/passwdqc/">http://www.openwall.com/passwdqc/</a></p>
<h2>AUTHORS</h2>
<p> The pam_passwdqc module was written for Openwall GNU/*/Linux by Solar Designer. The <code>Op Ar options</code> program was originally written for ALT GNU/*/Linux by Dmitry V. Levin, indirectly reusing code from pam_passwdqc (via libpasswdqc). This manual page was written for Openwall GNU/*/Linux by Dmitry V. Levin. </p>
<h2>Index</h2>
