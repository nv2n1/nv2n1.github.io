---
title: "ecryptfs-setup-private(1)"
name: "ecryptfs-setup-private"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-setup-private/"
description: "ecryptfs-setup-private – setup an eCryptfs private directory."
---

<h2 class="name">NAME</h2>
<p> ecryptfs-setup-private &#8211; setup an eCryptfs private directory.</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-setup-private [-f|&#8211;force] [-w|&#8211;wrapping] [-b|&#8211;bootstrap] [-n|&#8211;no-fnek] [&#8211;nopwcheck] [-u|&#8211;username USER] [-l|&#8211;loginpass LOGINPASS] [-m|&#8211;mountpass MOUNTPASS]</code> </p>
<h2>OPTIONS</h2>
<p> Options available for the <code>ecryptfs-setup-private</code> command:</p>
<dl>
<dt><code>-f, &#8211;force</code></dt>
<dd> Force overwriting of an existing setup</dd>
<dt><code>-w, &#8211;wrapping</code></dt>
<dd> Use an independent wrapping passphrase, different from the login passphrase</dd>
<dt><code>-u, &#8211;username USER</code></dt>
<dd> User to setup, default is current user if omitted</dd>
<dt><code>-l, &#8211;loginpass LOGINPASS</code></dt>
<dd> System passphrase for USER, used to wrap MOUNTPASS, will interactively prompt if omitted</dd>
<dt><code>-m, &#8211;mountpass MOUNTPASS</code></dt>
<dd> Passphrase for mounting the ecryptfs directory, default is 16 bytes from /dev/random if omitted</dd>
<dt><code>-b, &#8211;bootstrap</code></dt>
<dd> Bootstrap a new user&#8217;s entire home directory</dd>
<dt><code>&#8211;undo</code></dt>
<dd> Display instructions on how to undo an encrypted private setup</dd>
<dt><code>-n, &#8211;no-fnek</code></dt>
<dd> Do not encrypt filenames; otherwise, filenames will be encrypted on systems which support filename encryption</dd>
<dt><code>&#8211;nopwcheck</code></dt>
<dd> Do not check the validity of the specified login password (useful for LDAP user accounts)</dd>
<dt><code>&#8211;noautomount</code></dt>
<dd> Setup this user such that the encrypted private directory is not automatically mounted on login</dd>
<dt><code>&#8211;noautoumount</code></dt>
<dd> Setup this user such that the encrypted private directory is not automatically unmounted at logout </dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>ecryptfs-setup-private</code> is a program that sets up a private cryptographic mountpoint for a non-root user. </p>
<p> Be sure to properly escape your parameters according to your shell&#8217;s special character nuances, and also surround the parameters by double quotes, if necessary. Any of the parameters may be: </p>
<p>&nbsp;<wbr>&nbsp;1)&nbsp;exported as environment variables<br />
&nbsp;<wbr>&nbsp;2)&nbsp;specified on the command line<br />
&nbsp;<wbr>&nbsp;3)&nbsp;left empty and interactively prompted </p>
<p> <code>The user SHOULD ABSOLUTELY RECORD THE MOUNT PASSPHRASE AND STORE IN A SAFE LOCATION. If the mount passphase file is lost, or the mount passphrase is forgotten, THERE IS NO WAY TO RECOVER THE ENCRYPTED DATA.</code> </p>
<p> Using the values of USER, MOUNTPASS, and LOGINPASS, <code>ecryptfs-setup-private</code> will:<br />
&nbsp;<wbr>&nbsp;&#8211; Create&nbsp;~/.Private&nbsp;(permission 700)<br />
&nbsp;<wbr>&nbsp;&#8211; Create&nbsp;~/Private&nbsp;(permission 500)<br />
&nbsp;<wbr>&nbsp;&#8211; Backup any existing wrapped passphrases<br />
&nbsp;<wbr>&nbsp;&#8211; Use LOGINPASS to wrap and encrypt MOUNTPASS<br />
&nbsp;<wbr>&nbsp;&#8211; Write to&nbsp;~/.ecryptfs/wrapped-passphrase<br />
&nbsp;<wbr>&nbsp;&#8211; Add the passphrase to the current keyring<br />
&nbsp;<wbr>&nbsp;&#8211; Write the passphrase signature to&nbsp;~/.ecryptfs/Private.sig<br />
&nbsp;<wbr>&nbsp;&#8211; Test the cryptographic mount with a few reads and writes </p>
<p> The system administrator can add the pam_ecryptfs.so module to the PAM stack which will automatically use the login passphrase to unwrap the mount passphrase, add the passphrase to the user&#8217;s kernel keyring, and automatically perform the mount. See <a href="/docs/linux/man/8-pam_ecryptfs/">pam_ecryptfs</a>(8). </p>
<h2>FILES</h2>
<p> <i>~/.ecryptfs/auto-mount</i> </p>
<p> <i>~/.Private</i> &#8211; underlying directory containing encrypted data </p>
<p> <i>~/Private</i> &#8211; mountpoint containing decrypted data (when mounted) </p>
<p> <i>~/.ecryptfs/Private.sig</i> &#8211; file containing signature of mountpoint passphrase </p>
<p> <i>~/.ecryptfs/Private.mnt</i> &#8211; file containing path of the private directory mountpoint </p>
<p> <i>~/.ecryptfs/wrapped-passphrase</i> &#8211; file containing the mount passphrase, wrapped with the login passphrase </p>
<p> <i>~/.ecryptfs/wrapping-independent</i> &#8211; this file exists if the wrapping passphrase is independent from login passphrase </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-ecryptfs-rewrap-passphrase/">ecryptfs-rewrap-passphrase</a></code>(1), <code><a href="/docs/linux/man/1-mount-ecryptfs_private/">mount.ecryptfs_private</a></code>(1), <code><a href="/docs/linux/man/8-pam_ecryptfs/">pam_ecryptfs</a></code>(8), <code><a href="/docs/linux/man/1-umount-ecryptfs_private/">umount.ecryptfs_private</a></code>(1)</dt>
<dd>
</dd><dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></dt>
<dd>
</dd><dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></dt>
<dd>
</dd></dl>
<h2>AUTHOR</h2>
<p> This manpage and the <code>ecryptfs-setup-private</code> utility was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
