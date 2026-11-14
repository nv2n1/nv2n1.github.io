---
title: "passwdqc(5)"
name: "passwdqc"
section: "5"
letter: "p"
url: "/docs/linux/man/5-passwdqc/"
description: "passwdqc.conf – libpasswdqc configuration file"
---

<p><code>passwdqc.conf</code> &#8211; libpasswdqc configuration file</p>
<h2>Description</h2>
<p>libpasswdqc is a simple password strength checking library. In addition to checking regular passwords, it offers support for passphrases and can provide randomly generated ones. A configuration file may be used to override default libpasswdqc settings.</p>
<h2>Format</h2>
<p>A file consists of 0 or more lines of the following format: </p>
<blockquote><p><tt></tt><i>option </i><code>= </code><i>value</i> </p></blockquote>
<p> Empty lines and lines beginning with &#8220;<code>#</code> &#8221; are ignored. Whitespace characters between the <i>option</i> &#8220;<code>=</code> &#8221; and <i>value</i> are not allowed.</p>
<h2>Directive Options</h2>
<dl>
<dt><code>config = </code><i>FILE</i></p>
<dd>Load the specified configuration <i>FILE</i> in the <code>passwdqc.conf</code> format. This file may define any options described in this manual, including load of yet another configuration file, but loops are not allowed.</dl>
<h2>Password Quality Control Options</h2>
<dl>
<dt> <code>min =</code> <i>N0 , N1 , N2 , N3 , N4</i></p>
<dd>(default: min=disabled,24,11,8,7)</p>
<dd>The minimum allowed password lengths for different kinds of passwords/passphrases. The keyword <code>disabled</code> can be used to disallow passwords of a given kind regardless of their length. Each subsequent number is required to be no larger than the preceding one. </p>
<p> <i>N0</i> is used for passwords consisting of characters from one character class only. The character classes are: digits, lower-case letters, upper-case letters, and other characters. There is also a special class for <code>non- ASCII</code> characters, which could not be classified, but are assumed to be non-digits. </p>
<p> <i>N1</i> is used for passwords consisting of characters from two character classes that do not meet the requirements for a passphrase. </p>
<p> <i>N2</i> is used for passphrases. Note that besides meeting this length requirement, a passphrase must also consist of a sufficient number of words (see the <code>passphrase</code> option below). </p>
<p> <i>N3</i> and <i>N4</i> are used for passwords consisting of characters from three and four character classes, respectively. </p>
<p> When calculating the number of character classes, upper-case letters used as the first character and digits used as the last character of a password are not counted. </p>
<p> In addition to being sufficiently long, passwords are required to contain enough different characters for the character classes and the minimum length they have been checked against. </p>
<dt><code>max = </code><i>N</i></p>
<dd>(default: <code>max = 40</code> ) The maximum allowed password length. This can be used to prevent users from setting passwords that may be too long for some system services. The value 8 is treated specially: if <code>max</code> is set to 8, passwords longer than 8 characters will not be rejected, but will be truncated to 8 characters for the strength checks and the user will be warned. This is to be used with the traditional DES-based password hashes, which truncate the password at 8 characters. </p>
<p> It is important that you do set <code>max = 8</code> if you are using the traditional hashes, or some weak passwords will pass the checks.</p>
<dt><code>passphrase = </code><i>N</i></p>
<dd>(default: <code>passphrase = 3</code> ) The number of words required for a passphrase, or 0 to disable the support for user-chosen passphrases.</p>
<dt><code>match = </code><i>N</i></p>
<dd>(default: <code>match = 4</code> ) The length of common substring required to conclude that a password is at least partially based on information found in a character string, or 0 to disable the substring search. Note that the password will not be rejected once a weak substring is found; it will instead be subjected to the usual strength requirements with the weak substring partially discounted. </p>
<p> The substring search is case-insensitive and is able to detect and remove a common substring spelled backwards.</p>
<dt> <code>similar = permit | deny</code></p>
<dd>(default: <code>similar = deny</code> )</p>
<dd>Whether a new password is allowed to be similar to the old one. The passwords are considered to be similar when there is a sufficiently long common substring and the new password with the substring partially discounted would be weak.</p>
<dt> <code>random = </code><i>N</i> [, <code>only</code> ]</p>
<dd>(default: <code>random = 47</code> )</p>
<dd>The size of randomly-generated passphrases in bits (24 to 85), or 0 to disable this feature. Any passphrase that contains the offered randomly-generated string will be allowed regardless of other possible restrictions. </p>
<p> The <code>only</code> modifier can be used to disallow user-chosen passwords.</dl>
<h2>Pam Module Options</h2>
<dl>
<dt> <code>enforce = none | users | everyone</code></p>
<dd>(default: <code>enforce = everyone</code> )</p>
<dd>The PAM module can be configured to warn of weak passwords only, but not actually enforce strong passwords. The <code>users</code> setting will enforce strong passwords for invocations by non-root users only.</p>
<dt><code>non-unix</code></p>
<dd>Normally, the PAM module uses <a href="/docs/linux/man/3-getpwnam/">getpwnam</a>(3) to obtain the user&#8217;s personal login information and use that during the password strength checks. This behavior can be disabled with the <code>non-unix</code> option.</p>
<dt><code>retry = </code><i>N</i></p>
<dd>(default: <code>retry = 3</code> ) The number of times the PAM module will ask for a new password if the user fails to provide a sufficiently strong password and enter it twice the first time.</p>
<dt><code>ask_oldauthtok </code>[= <code>update</code> ]</p>
<dd>Ask for the old password as well. Normally, the PAM module leaves this task for subsequent modules. With no argument, the <code>ask_oldauthtok</code> option will cause the PAM module to ask for the old password during the preliminary check phase. If the <code>ask_oldauthtok</code> option is specified with the <code>update</code> argument, the PAM module will do that during the update phase.</p>
<dt><code>check_oldauthtok</code></p>
<dd>This tells the PAM module to validate the old password before giving a new password prompt. Normally, this task is left for subsequent modules. </p>
<p> The primary use for this option is when <code>ask_oldauthtok = update</code> is also specified, in which case no other module gets a chance to ask for and validate the password. Of course, this will only work with UNIX passwords.</p>
<dt><code>use_first_pass , use_authtok</code></p>
<dd>Use the new password obtained by other modules stacked before the PAM module. This disables user interaction within the PAM module. The only difference between <code>use_first_pass</code> and <code>use_authtok</code> is that the former is incompatible with <code>ask_oldauthtok</code></dl>
<h2>Files</h2>
<p>/etc/passwdqc.conf</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-getpwnam/">getpwnam</a>(3), pam_passwdqc8. </p>
<p> <a rel="nofollow" href="http://www.openwall.com/passwdqc/">http://www.openwall.com/passwdqc/</a></p>
<h2>Authors</h2>
<p>The pam_passwdqc module was written for Openwall GNU/*/Linux by An Solar Designer Aq solar at openwall.com . This manual page was derived from pam_passwdqc8.Thelatter,derivedfromtheauthor&#8217;s documentation, was written for the Fx Project by ThinkSec AS and NAI Labs, the Security Research Division of Network Associates, Inc. under DARPA/SPAWAR contract N66001-01-C-8035 (&#8220;CBOSS&#8221; ) as part of the DARPA CHATS research program.</p>
