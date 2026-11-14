---
title: "chgpasswd(8)"
name: "chgpasswd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chgpasswd/"
description: "chgpasswd – update group passwords in batch mode"
---

<p>chgpasswd &#8211; update group passwords in batch mode</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>chgpasswd</code> [<i>options</i>]</dl>
<h2>Description</h2>
<dd>The <code>chgpasswd</code> command reads a list of group name and password pairs from standard input and uses this information to update a set of existing groups. Each line is of the format: </p>
<p> <i>group_name</i>:<i>password</i> </p>
<p> By default the supplied password must be in clear-text, and is encrypted by <code>chgpasswd</code>. </p>
<p> The default encryption algorithm can be defined for the system with the <code>ENCRYPT_METHOD</code> variable of /etc/login.defs, and can be overwritten with the <code>-e</code>, <code>-m</code>, or <code>-c</code> options. </p>
<p> This command is intended to be used in a large system environment where many accounts are created at a single time.</p>
<h2>Options</h2>
<p>The options which apply to the <code>chgpasswd</code> command are: </p>
<p> <code>-c</code>, <code>&#8211;crypt-method</code></p>
<dl>
<dd>Use the specified method to encrypt the passwords. </p>
<p> The available methods are DES, MD5, NONE, and SHA256 or SHA512 if your libc support these methods.</dl>
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
<p> <code>-s</code>, <code>&#8211;sha-rounds</code></p>
<dl>
<dd>Use the specified number of rounds to encrypt the passwords. </p>
<p> The value 0 means that the system will choose the default number of rounds for the crypt method (5000). </p>
<p> A minimal value of 1000 and a maximal value of 999,999,999 will be enforced. </p>
<p> You can only use this option with the SHA256 or SHA512 crypt method. </p>
<p> By default, the number of rounds is defined by the SHA_CRYPT_MIN_ROUNDS and SHA_CRYPT_MAX_ROUNDS variables in /etc/login.defs.</dl>
<h2>Caveats</h2>
<p>Remember to set permissions or umask to prevent readability of unencrypted files by other users. </p>
<p> You should make sure the passwords and the encryption method respect the system&#8217;s password policy.</p>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>ENCRYPT_METHOD</code> (string)</p>
<dl>
<dd>This defines the system default encryption algorithm for encrypting passwords (if no algorithm are specified on the command line). </p>
<p> It can take one of these values: <i>DES</i> (default), <i>MD5</i>, <i>SHA256</i>, <i>SHA512</i>. </p>
<p> Note: this parameter overrides the <code>MD5_CRYPT_ENAB</code> variable. </p>
<p> Note: This only affect the generation of group passwords. The generation of user passwords is done by PAM and subject to the PAM configuration. It is recommended to set this variable consistently with the PAM configuration.</dl>
<p> <code>MAX_MEMBERS_PER_GROUP</code> (number)</p>
<dl>
<dd>Maximum members per group entry. When the maximum is reached, a new group entry (line) is started in /etc/group (with the same name, same password, and same GID). </p>
<p> The default value is 0, meaning that there are no limits in the number of members in a group. </p>
<p> This feature (split group) permits to limit the length of lines in the group file. This is useful to make sure that lines for NIS groups are not larger than 1024 characters. </p>
<p> If you need to enforce such limit, you can use 25. </p>
<p> Note: split groups may not be supported by all tools (even in the Shadow toolsuite). You should not use this variable unless you really need it.</dl>
<p> <code>MD5_CRYPT_ENAB</code> (boolean)</p>
<dl>
<dd>Indicate if passwords must be encrypted using the MD5-based algorithm. If set to <i>yes</i>, new passwords will be encrypted using the MD5-based algorithm compatible with the one used by recent releases of FreeBSD. It supports passwords of unlimited length and longer salt strings. Set to <i>no</i> if you need to copy encrypted passwords to other systems which don&#8217;t understand the new algorithm. Default is <i>no</i>. </p>
<p> This variable is superseded by the <code>ENCRYPT_METHOD</code> variable or by any command line option used to configure the encryption algorithm. </p>
<p> This variable is deprecated. You should use <code>ENCRYPT_METHOD</code>. </p>
<p> Note: This only affect the generation of group passwords. The generation of user passwords is done by PAM and subject to the PAM configuration. It is recommended to set this variable consistently with the PAM configuration.</dl>
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
<p>/etc/group</p>
<dl>
<dd>Group account information.</dl>
<p> /etc/gshadow</p>
<dl>
<dd>Secure group account information.</dl>
<p> /etc/login.defs</p>
<dl>
<dd>Shadow password suite configuration.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gpasswd/">gpasswd</a></code>(1), <code><a href="/docs/linux/man/8-groupadd/">groupadd</a></code>(8), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5). </p>
