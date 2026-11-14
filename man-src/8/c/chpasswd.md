---
title: "chpasswd(8)"
name: "chpasswd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chpasswd/"
description: "chpasswd – update passwords in batch mode"
---

<p>chpasswd &#8211; update passwords in batch mode</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>chpasswd</code> [<i>options</i>]</dl>
<h2>Description</h2>
<dd>The <code>chpasswd</code> command reads a list of user name and password pairs from standard input and uses this information to update a group of existing users. Each line is of the format: </p>
<p> <i>user_name</i>:<i>password</i> </p>
<p> By default the passwords must be supplied in clear-text, and are encrypted by <code>chpasswd</code>. Also the password age will be updated, if present. </p>
<p> By default, passwords are encrypted by PAM, but (even if not recommended) you can select a different encryption method with the <code>-e</code>, <code>-m</code>, or <code>-c</code> options. </p>
<p> Except when PAM is used to encrypt the passwords, <code>chpasswd</code> first updates all the passwords in memory, and then commits all the changes to disk if no errors occurred for any user. </p>
<p> When PAM is used to encrypt the passwords (and update the passwords in the system database) then if a password cannot be updated <code>chpasswd</code> continues updating the passwords of the next users, and will return an error code on exit. </p>
<p> This command is intended to be used in a large system environment where many accounts are created at a single time.</p>
<h2>Options</h2>
<p>The options which apply to the <code>chpasswd</code> command are: </p>
<p> <code>-c</code>, <code>&#8211;crypt-method</code>&nbsp;<i>METHOD</i></p>
<dl>
<dd>Use the specified method to encrypt the passwords. </p>
<p> The available methods are DES, MD5, NONE, and SHA256 or SHA512 if your libc support these methods. </p>
<p> By default, PAM is used to encrypt the passwords.</dl>
<p> <code>-e</code>, <code>&#8211;encrypted</code></p>
<dl>
<dd>Supplied passwords are in encrypted form.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-m</code>, <code>&#8211;md5</code></p>
<dl>
<dd>Use MD5 encryption instead of DES when the supplied passwords are not encrypted.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-s</code>, <code>&#8211;sha-rounds</code>&nbsp;<i>ROUNDS</i></p>
<dl>
<dd>Use the specified number of rounds to encrypt the passwords. </p>
<p> The value 0 means that the system will choose the default number of rounds for the crypt method (5000). </p>
<p> A minimal value of 1000 and a maximal value of 999,999,999 will be enforced. </p>
<p> You can only use this option with the SHA256 or SHA512 crypt method. </p>
<p> By default, the number of rounds is defined by the <code>SHA_CRYPT_MIN_ROUNDS</code> and <code>SHA_CRYPT_MAX_ROUNDS</code> variables in /etc/login.defs.</dl>
<h2>Caveats</h2>
<p>Remember to set permissions or umask to prevent readability of unencrypted files by other users.</p>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>SHA_CRYPT_MIN_ROUNDS</code> (number), <code>SHA_CRYPT_MAX_ROUNDS</code> (number)</p>
<dl>
<dd>When <code>ENCRYPT_METHOD</code> is set to <i>SHA256</i> or <i>SHA512</i>, this defines the number of SHA rounds used by the encryption algorithm by default (when the number of rounds is not specified on the command line). </p>
<p> With a lot of rounds, it is more difficult to brute forcing the password. But note also that more CPU resources will be needed to authenticate users. </p>
<p> If not specified, the libc will choose the default number of rounds (5000). </p>
<p> The values must be inside the 1000-999,999,999 range. </p>
<p> If only one of the <code>SHA_CRYPT_MIN_ROUNDS</code> or <code>SHA_CRYPT_MAX_ROUNDS</code> values is set, then this value will be used. </p>
<p> If <code>SHA_CRYPT_MIN_ROUNDS</code> &gt; <code>SHA_CRYPT_MAX_ROUNDS</code>, the highest value will be used. </p>
<p> Note: This only affect the generation of group passwords. The generation of user passwords is done by PAM and subject to the PAM configuration. It is recommended to set this variable consistently with the PAM configuration.</dl>
<h2>Files</h2>
<p>/etc/passwd</p>
<dl>
<dd>User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dd>Secure user account information.</dl>
<p> /etc/login.defs</p>
<dl>
<dd>Shadow password suite configuration.</dl>
<p> /etc/pam.d/chpasswd</p>
<dl>
<dd>PAM configuration for <code>chpasswd</code>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/8-newusers/">newusers</a></code>(8), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8). </p>
