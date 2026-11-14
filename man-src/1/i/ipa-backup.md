---
title: "ipa-backup(1)"
name: "ipa-backup"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-backup/"
description: "ipa-backup – Back up an IPA master"
---

<h2>NAME</h2>
<p> ipa-backup &#8211; Back up an IPA master</p>
<h2>SYNOPSIS</h2>
<p> ipa-backup [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Two kinds of backups: full and data-only.</p>
<dl>
<dt>The back up is optionally encrypted using either the default root GPG key or a named key. No passphrase is supported.</p>
<dd>
<dt>Backups are stored in a subdirectory in /var/lib/ipa/backup.</p>
<dd>
<dt>The naming convention for full backups is ipa-full-YEAR-MM-DD-HH-MM-SS in the GMT time zone.</p>
<dd>
<dt>The naming convention for data backups is ipa-data-YEAR-MM-DD-HH-MM-SS In the GMT time zone.</p>
<dd>
<dt>Within the subdirectory is file, header, that describes the back up including the type, system, date of backup, the version of IPA, the version of the backup and the services on the master.</p>
<dd>
<dt>A backup can not be restored on another host.</p>
<dd>
<dt>A backup can not be restored in a different version of IPA.</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;data</code></p>
<dd> Back up data only. The default is to back up all IPA files plus data.</p>
<dt><code>&#8211;gpg</code></p>
<dd> Encrypt the back up file.</p>
<dt><code>&#8211;gpg-keyring</code>=<i>GPG_KEYRING</i></p>
<dd> The full path to a GPG keyring. The keyring consists of two files, a public and a private key (.sec and .pub respectively). Specify the path without an extension.</p>
<dt><code>&#8211;logs</code></p>
<dd> Include the IPA service log files in the backup.</p>
<dt><code>&#8211;online</code></p>
<dd> Perform the backup on-line. Requires the &#8211;data option.</p>
<dt><code>&#8211;v</code>, <code>&#8211;verbose</code></p>
<dd> Print debugging information</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Alias for &#8211;verbose</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Output only errors</p>
<dt><code>&#8211;log-file</code>=<i>FILE</i></p>
<dd> Log to the given file</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred</p>
<h2>FILES</h2>
<p> <i>/var/lib/ipa/backup</i></p>
<dl>
<dt>
<dd> The default directory for storing backup files.</dl>
<p> /var/log/ipabackup.log</p>
<dl>
<dt>
<dd> The log file for backups </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ipa-restore/">ipa-restore</a>(1). </p>
<h2>Index</h2>
