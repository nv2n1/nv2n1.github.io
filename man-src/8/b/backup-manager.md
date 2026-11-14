---
title: "backup-manager(8)"
name: "backup-manager"
section: "8"
letter: "b"
url: "/docs/linux/man/8-backup-manager/"
description: "backup-manager – An easy to use backup tool for your Linux box."
---

<p>backup-manager &#8211; An easy to use backup tool for your Linux box.</p>
<h2>Synopsis</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>backup-manager&nbsp;<wbr>[options]</p>
<h2>Description</h2>
<p>Backup Manager is an easy-to-use tool for generating archives. </p>
<p> It is designed with simplicity in mind for those who don&#8217;t want an obfuscated tool for making tarballs. </p>
<p> There are different methods for building archives: tarballs, incremental tarballs, mysql dumps, svn dump. You can also write your own method with a generic method that will execute a command and will archive its output. </p>
<p> Every times you run Backup Manager, you can upload archives thanks to a couple of upload methods: through FTP, SSH or even with RSYNC. </p>
<p> It&#8217;s also possible to export your archives to removable media like CDR or DVD.</p>
<h2>Configuration Files</h2>
<p>Backup Manager&#8217;s behavior is defined in configuration files. You can use different configuration files at the same time. The default configuration file is `/etc/backup-manager.conf&#8217;. </p>
<p> An example should have been provided with the program, most of the time it&#8217;s installed in `/usr/share/backup-manager/backup-manager.conf.tpl&#8217;. </p>
<p> If you want exhaustive details about how to write your own configuration files, please refer to the Backup Manager User Guide: <a rel="nofollow" href="http://www.backup-manager.org/documentation/user-guide/">http://www.backup-manager.org/documentation/user-guide/</a></p>
<h2>Options</h2>
<p><code>&#8211;version</code> Show the version number. </p>
<p> <code>&#8211;verbose|-v </code> Print what happens to STDOUT. </p>
<p> <code>&#8211;no-warnings</code> Disable warnings. </p>
<p> <code>&#8211;help|-h </code> Print a short help message. </p>
<p> <code>&#8211;upload|-u</code> Just upload the files. </p>
<p> <code>&#8211;purge|-p</code> Just purge old archives. </p>
<p> <code>&#8211;burn|-b </code> Just burn the archives. </p>
<p> <code>&#8211;md5check|-m</code> Just perform the MD5 checkup on the CDR/CDRW. </p>
<p> <code>&#8211;conffile|-c file</code> Use an alternate config file. </p>
<p> <code>&#8211;force|-f</code> Force overwrite of existing archives. </p>
<p> <code>&#8211;no-upload</code> Disable the uploading process. </p>
<p> <code>&#8211;no-burn</code> Disable the burning process. </p>
<p> <code>&#8211;no-purge</code> Disable the purging process.</p>
<h2>Bugs</h2>
<p>If you find a bug or want to submit a wish-list to the development team, feel free to use the official Bug Tracking System: <a rel="nofollow" href="http://bugzilla.backup-manager.org">http://bugzilla.backup-manager.org</a></p>
<h2>Website</h2>
<p>To find latest news and releases, come to the official website: <a rel="nofollow" href="http://www.backup-manager.org">http://www.backup-manager.org</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-backup-manager-upload/">backup-manager-upload</a></code>(8), <code><a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a></code>(1)</p>
<h2>Author</h2>
<p>Alexis Sukrieh &lt;sukria [at] backup-manager.org&gt;</p>
