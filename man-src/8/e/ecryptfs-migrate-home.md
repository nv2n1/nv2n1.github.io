---
title: "ecryptfs-migrate-home(8)"
name: "ecryptfs-migrate-home"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ecryptfs-migrate-home/"
description: "ecryptfs-migrate-home – migrate a user’s home directory to an encrypted home setup"
---

<p>ecryptfs-migrate-home &#8211; migrate a user&#8217;s home directory to an encrypted home setup</p>
<h2>Synopsis</h2>
<p><code>ecryptfs-migrate-home</code> [-u|&#8211;user USER] </p>
<h2>Options</h2>
<dl>
<dt><code>-u, &#8211;user USER</code></p>
<dd>Migrate USER&#8217;s home directory to an encrypted home directory </p>
</dl>
<h2>Description</h2>
<p><code>WARNING</code>: Make a complete backup copy of the non-encrypted data to another system or external media. This script is dangerous and in case of an error, could result in data lost, or USER locked out of the system! This program must be executed by root. This program will attempt to migrate a user&#8217;s home directory to an encrypted home directory. This program requires free disk space 2.5x the current size of the home directory to be migrated. Once successful, you can recover most of this space by deleting the cleartext directory. The USER must be logged out of all sessions in order to perform the migration, and have no open files according to <code><a href="/docs/linux/man/1-lsof/">lsof</a></code>(1). Once the migration has completed, the USER must login immediately, BEFORE THE NEXT REBOOT in order to complete the migration. After logging in, if USER can read and write files in their home directory successfully, then the migration has completed successfully and can remove the cleartext backup in <i>/home/</i>. After a successful migration, the USER really must run <code><a href="/docs/linux/man/1-ecryptfs-unwrap-passphrase/">ecryptfs-unwrap-passphrase</a></code>(1) or <code><a href="/docs/linux/man/1-zescrow/">zescrow</a></code>(1) and record their randomly generated mount passphrase. If swap is not already encrypted, it is highly recommended that your administrator setup encrypted swap using <code><a href="/docs/linux/man/1-ecryptfs-setup-swap/">ecryptfs-setup-swap</a></code>(1). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ecryptfs-unwrap-passphrase/">ecryptfs-unwrap-passphrase</a></code>(1), <code><a href="/docs/linux/man/1-ecryptfs-setup-private/">ecryptfs-setup-private</a></code>(1), <code><a href="/docs/linux/man/1-ecryptfs-setup-swap/">ecryptfs-setup-swap</a></code>(1), <code><a href="/docs/linux/man/1-lsof/">lsof</a></code>(1), <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1), <code><a href="/docs/linux/man/1-zescrow/">zescrow</a></code>(1) <i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i> </p>
<h2>Author</h2>
<p>This manpage was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
