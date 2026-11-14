---
title: "twfiles(5)"
name: "twfiles"
section: "5"
letter: "t"
url: "/docs/linux/man/5-twfiles/"
description: "twfiles – overview of files used by Tripwire and file backup process"
---

<p>twfiles &#8211; overview of files used by <i>Tripwire</i> and file backup process</p>
<h2>Description</h2>
<p>.SS Configuration File default: <i>/etc/tripwire/tw.cfg</i><br />
 The configuration file stores system-specific information, such as the location of <i>Tripwire</i> data files. The configuration settings are generated during the installation process, but can be changed by the system administrator at any time. See the <code><a href="/docs/linux/man/4-twconfig/">twconfig</a></code>(4) man page for a more complete discussion. .SS Policy File default: <i>/etc/tripwire/tw.pol</i><br />
 The policy file consists of a series of rules specifying the system objects that <i>Tripwire</i> should monitor, and the data for each object that should be collected and stored in the database file. Should unexpected changes occur, the policy file can describe the person to be notified and the severity of the violation. See the <i>policyguide.txt</i> file in the policy directory and the <code><a href="/docs/linux/man/4-twpolicy/">twpolicy</a></code>(4) man page for a more complete discussion. .SS Database File default: <i>/var/lib/$(HOSTNAME).twd</i><br />
 The database file serves as the baseline for integrity checking. After installation, <i>Tripwire</i> creates the initial database file, a &quot;snapshot&quot; of the filesystem in a known secure state. Later, when an integrity check is run, <i>Tripwire</i> compares each system object described in the policy file against its corresponding entry in the database. A report is created, and if an object has changed outside of constraints defined in the policy file, a violation is reported. See the <code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8) and <code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8) man pages for more information on creating and maintaining database files. .SS Report Files default: <i>/var/lib/tripwire/report/$(HOSTNAME)-$(DATE).twr</i><br />
 Once the above three files have been created, <i>Tripwire</i> can run an integrity check and search for any differences between the current system and the data stored in the &quot;baseline&quot; <i>Tripwire</i> database. This information is archived into report files, a collection of rule violations discovered during an integrity check. With the appropriate settings, a report can also be emailed to one or more recipients. See the <code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8) and <code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8) man pages for information on creating and printing report files. .SS Key Files defaults: <i>/etc/tripwire/site.key</i> and <i>/etc/tripwire/$(HOSTNAME)-local.key</i><br />
 It is critical that <i>Tripwire</i> files be protected from unauthorized access&#8211;an attacker who is able to modify these files can subvert <i>Tripwire</i> operation. For this reason, all of the above files are signed using public key cryptography to prevent unauthorized modification. Two separate sets of keys protect critical <i>Tripwire</i> data files. One or both of these key sets is necessary for performing almost every <i>Tripwire</i> task. </p>
<p> The site key is used to protect files that could be used across several systems. This includes the policy and configuration files. The local key is used to protect files specific to the local machine, such as the <i>Tripwire</i> database. The local key may also be used for signing integrity check reports. See the <code><a href="/docs/linux/man/8-twadmin/">twadmin</a></code>(8) man page for more information on keys.</p>
<h3>File Backup</h3>
<p>To prevent the accidental deletion of important data, <i>Tripwire</i> automatically creates backup files whenever any <i>Tripwire</i> file is overwritten. The existing file will be renamed with a <i>.bak</i> extension, and the new version of the file will take its place. Only one backup copy for each filename can exist at any time. If a backup copy of a file already exists, the older backup file will be deleted and replaced with the newer one. </p>
<p> File backup is an integral part of <i>Tripwire</i>, and cannot be removed or changed.</p>
<h2>Version Information</h2>
<p>This man page describes <i>Tripwire 2.4</i>.</p>
<h2>Authors</h2>
<p>Tripwire, Inc.</p>
<h2>Copying Permissions</h2>
<p>Permission is granted to make and distribute verbatim copies of this man page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this man page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this man page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by Tripwire, Inc. </p>
<p> Copyright 2000-2017 Tripwire, Inc. Tripwire is a registered trademark of Tripwire, Inc. in the United States and other countries. All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-twintro/">twintro</a></code>(8), <code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8), <code><a href="/docs/linux/man/8-twadmin/">twadmin</a></code>(8), <code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8), <code><a href="/docs/linux/man/8-siggen/">siggen</a></code>(8), <code><a href="/docs/linux/man/4-twconfig/">twconfig</a></code>(4), <code><a href="/docs/linux/man/4-twpolicy/">twpolicy</a></code>(4) </p>
