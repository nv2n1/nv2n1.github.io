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
<dt>The back up is optionally encrypted using either the default root GPG key or a named key. No passphrase is supported.</dt>
<dd>
</dd><dt>Backups are stored in a subdirectory in /var/lib/ipa/backup.</dt>
<dd>
</dd><dt>The naming convention for full backups is ipa-full-YEAR-MM-DD-HH-MM-SS in the GMT time zone.</dt>
<dd>
</dd><dt>The naming convention for data backups is ipa-data-YEAR-MM-DD-HH-MM-SS In the GMT time zone.</dt>
<dd>
</dd><dt>Within the subdirectory is file, header, that describes the back up including the type, system, date of backup, the version of IPA, the version of the backup and the services on the master.</dt>
<dd>
</dd><dt>A backup can not be restored on another host.</dt>
<dd>
</dd><dt>A backup can not be restored in a different version of IPA.</dt>
<dd></dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;data</code></dt>
<dd> Back up data only. The default is to back up all IPA files plus data.</dd>
<dt><code>&#8211;gpg</code></dt>
<dd> Encrypt the back up file.</dd>
<dt><code>&#8211;gpg-keyring</code>=<i>GPG_KEYRING</i></dt>
<dd> The full path to a GPG keyring. The keyring consists of two files, a public and a private key (.sec and .pub respectively). Specify the path without an extension.</dd>
<dt><code>&#8211;logs</code></dt>
<dd> Include the IPA service log files in the backup.</dd>
<dt><code>&#8211;online</code></dt>
<dd> Perform the backup on-line. Requires the &#8211;data option.</dd>
<dt><code>&#8211;v</code>, <code>&#8211;verbose</code></dt>
<dd> Print debugging information</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> Alias for &#8211;verbose</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Output only errors</dd>
<dt><code>&#8211;log-file</code>=<i>FILE</i></dt>
<dd> Log to the given file</dd></dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred</p>
<h2>FILES</h2>
<p> <i>/var/lib/ipa/backup</i></p>
<dl>
<dt>
</dt><dd> The default directory for storing backup files.</dd></dl>
<p> /var/log/ipabackup.log</p>
<dl>
<dt>
</dt><dd> The log file for backups </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ipa-restore/">ipa-restore</a>(1). </p>
