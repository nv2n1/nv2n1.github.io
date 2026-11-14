---
title: "pwqcheck(1)"
name: "pwqcheck"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pwqcheck/"
description: "pwqcheck – Check passphrase quality"
---

<h2 class="name">NAME</h2>
<p> <code>pwqcheck</code> &#8211; Check passphrase quality </p>
<h2>SYNOPSIS</h2>
<p> [<i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>Op Ar options</code> program checks passphrase quality using the libpasswdqc library. By default, it expects to read 3 lines from standard input: </p>
<dl>
<dt><code>first line is a new password,</code></p>
<dd>
<dt><code>second line is an old password, and</code></p>
<dd>
<dt><code>third line is either an existing account name or a</code></p>
<dd> <a href="/docs/linux/man/5-passwd/">passwd</a>(5) entry.</dl>
<p> There are a number of supported options, which can be used to control the <code>Op Ar options</code> behavior. </p>
<p> <code>Op Ar options</code> prints <i>OK</i> on success. Scripts invoking <code>Op Ar options</code> are suggested to check for both a zero exit status and the <i>OK</i> line.</p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>min =</code> <i>N0 , N1 , N2 , N3 , N4</i></p>
<dd> (default: min=disabled,24,11,8,7)</p>
<dd>The minimum allowed password lengths for different kinds of passwords/passphrases. The keyword <code>disabled</code> can be used to disallow passwords of a given kind regardless of their length. Each subsequent number is required to be no larger than the preceding one. </p>
<p> <i>N0</i> is used for passwords consisting of characters from one character class only. The character classes are: digits, lower-case letters, upper-case letters, and other characters. There is also a special class for <code>non- ASCII</code> characters, which could not be classified, but are assumed to be non-digits. </p>
<p> <i>N1</i> is used for passwords consisting of characters from two character classes that do not meet the requirements for a passphrase. </p>
<p> <i>N2</i> is used for passphrases. Note that besides meeting this length requirement, a passphrase must also consist of a sufficient number of words (see the <code>passphrase</code> option below). </p>
<p> <i>N3</i> and <i>N4</i> are used for passwords consisting of characters from three and four character classes, respectively. </p>
<p> When calculating the number of character classes, upper-case letters used as the first character and digits used as the last character of a password are not counted. </p>
<p> In addition to being sufficiently long, passwords are required to contain enough different characters for the character classes and the minimum length they have been checked against. </p>
<dt><code>max = </code><i>N</i></p>
<dd> (default: <code>max = 40</code> ) The maximum allowed password length. This can be used to prevent users from setting passwords that may be too long for some system services. The value 8 is treated specially: if <code>max</code> is set to 8, passwords longer than 8 characters will not be rejected, but will be truncated to 8 characters for the strength checks and the user will be warned. This is to be used with the traditional DES-based password hashes, which truncate the password at 8 characters. </p>
<p> It is important that you do set <code>max = 8</code> if you are using the traditional hashes, or some weak passwords will pass the checks.</p>
<dt><code>passphrase = </code><i>N</i></p>
<dd> (default: <code>passphrase = 3</code> ) The number of words required for a passphrase.</p>
<dt><code>match = </code><i>N</i></p>
<dd> (default: <code>match = 4</code> ) The length of common substring required to conclude that a password is at least partially based on information found in a character string, or 0 to disable the substring search. Note that the password will not be rejected once a weak substring is found; it will instead be subjected to the usual strength requirements with the weak substring partially discounted. </p>
<p> The substring search is case-insensitive and is able to detect and remove a common substring spelled backwards.</p>
<dt><code>config = </code><i>FILE</i></p>
<dd> Load config <i>FILE</i> in the <code>passwdqc.conf</code> format. This file may define any options described in passwdqc.conf5,butonlythe <code>min</code> <code>max</code> <code>passphrase</code> <code>match ,</code> and <code>config</code> options are honored by <code>.</code></p>
<dt><code>-1</code></p>
<dd> Read just 1 line (new passphrase). This is needed to use <code>Op Ar options</code> as the passwordcheck program on OpenBSD &#8211; e.g., with &quot;:passwordcheck=/usr/bin/pwqcheck -1:\&quot; in the &quot;default&quot; section in <code>/etc/login.conf</code></p>
<dt><code>-2</code></p>
<dd> Read just 2 lines (new and old passphrases).</p>
<dt><code>&#8211;multi</code></p>
<dd> Check multiple passphrases (until EOF). This option may be used on its own or along with the <code>-1</code> or <code>-2</code> options. <code>Op Ar options</code> will read 1, 2, or 3 lines and will output one line per passphrase to check. The lines will start with either <i>OK</i> or a message explaining why the passphrase did not pass the checks, followed by a colon and a space, and finally followed by the passphrase. The explanatory message is guaranteed to not include a colon. With this option, the exit status of <code>Op Ar options</code> depends solely on whether there were any errors preventing the strength of passphrases from being fully checked or not. A primary use for this option is to test different policies and/or different versions of passwdqc on large passphrase lists.</p>
<dt><code>&#8211;version</code></p>
<dd> Output <code>Op Ar options</code> program version and exit.</p>
<dt><code>-h , &#8211;help</code></p>
<dd> Output <code>Op Ar options</code> help text and exit.</dl>
<h2>EXIT STATUS</h2>
<p> <code>Op Ar options</code> exits with non-zero status when it encounters invalid config file, invalid option, invalid parameter value, invalid data in standard input, and in any case when it fails to check passphrase strength. Without the <code>&#8211;multi</code> option, <code>Op Ar options</code> also exits with non-zero status when it detects a weak passphrase.</p>
<h2>FILES</h2>
<p> /etc/passwdqc.conf</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pwqgen/">pwqgen</a>(1), <a href="/docs/linux/man/5-passwd/">passwd</a>(5), passwdqc.conf5, pam_passwdqc8. </p>
<p> <a rel="nofollow" href="http://www.openwall.com/passwdqc/">http://www.openwall.com/passwdqc/</a></p>
<h2>AUTHORS</h2>
<p> The pam_passwdqc module was written for Openwall GNU/*/Linux by Solar Designer. The <code>Op Ar options</code> program was originally written for ALT GNU/*/Linux by Dmitry V. Levin, indirectly reusing code from pam_passwdqc (via libpasswdqc). This manual page (derived from the pam_passwdqc documentation) was written for Openwall GNU/*/Linux by Dmitry V. Levin. </p>
<h2>Index</h2>
