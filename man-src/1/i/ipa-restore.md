---
title: "ipa-restore(1)"
name: "ipa-restore"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-restore/"
description: "ipa-restore – Restore an IPA master"
---

<h2>NAME</h2>
<p> ipa-restore &#8211; Restore an IPA master</p>
<h2>SYNOPSIS</h2>
<p> ipa-restore [<i>OPTION</i>]&#8230; BACKUP</p>
<h2>DESCRIPTION</h2>
<p> Only the name of the backup needs to be passed in, not the full path. Backups are stored in a subdirectory in /var/lib/ipa/backup. If a backup is in another location then the full path must be provided.</p>
<dl>
<dt>The naming convention for full backups is ipa-full-YEAR-MM-DD-HH-MM-SS in the GMT time zone.</p>
<dd>
<dt>The naming convention for data backups is ipa-data-YEAR-MM-DD-HH-MM-SS In the GMT time zone.</p>
<dd>
<dt>The type of backup is automatically detected. A data restore can be done from either type.</p>
<dd>
<dt><code>WARNING</code>: A full restore will restore files like /etc/passwd, /etc/group, /etc/resolv.conf as well. Any file that IPA may have touched is backed up and restored.</p>
<dd>
<dt>An encrypted backup is also automatically detected and the root keyring is used by default. The &#8211;keyring option can be used to define the full path to the private and public keys.</p>
<dd>
<dt>Within the subdirectory is file, header, that describes the back up including the type, system, date of backup, the version of IPA, the version of the backup and the services on the master.</p>
<dd>
<dt>A backup can not be restored on another host.</p>
<dd>
<dt>A backup can not be restored in a different version of IPA.</p>
<dd>
<dt>Restoring from backup sets the server as the new data master. All other masters will need to be re-initialized. The first step in restoring a backup is to disable replication on all the other masters. This is to prevent the changelog from overwriting the data in the backup.</p>
<dd>
<dt>Use the ipa-replica-manage and ipa-csreplica-manage commands to re-initialize other masters. ipa-csreplica-manage only needs to be executed on masters that have a CA installed.</p>
<dd></dl>
<h2>REPLICATION</h2>
<p> The restoration on other masters needs to be done carefully, to match the replication topology, working outward from the restored master. For example, if your topology is A &lt;-&gt; B &lt;-&gt; C and you restored master A you would restore B first, then C.</p>
<dl>
<dt>Replication is disabled on all masters that are available when a restoration is done. If a master is down at the time of the restoration you will need to proceed with extreme caution. If this master is brought back up after the restoration is complete it may send out replication updates that apply the very changes you were trying to back out. The only safe answer is to reinstall the master. This would involve deleting all replication agreements to the master. This could have a cascading effect if the master is a hub to other masters. They would need to be connected to other masters before removing the downed master.</p>
<dd>
<dt>If the restore point is from a period prior to a replication agreement then the master will need to be re-installed. For example, you have masters A and B and you create a backup. You then add master C from B. Then you restore from the backup. The restored data is going to lose the replication agreement to C. The master on C will have a replication agreement pointing to B, but B won&#8217;t have the reverse agreement. Master C won&#8217;t be registered as an IPA master. It may be possible to manually correct these and re-connect C to B but it would be very prone to error.</p>
<dd>
<dt>If re-initializing on an IPA master version prior to 3.2 then the replication agreements will need to be manually re-enabled otherwise the re-initialization will never complete. To manually enable an agreement use ldapsearch to find the agreement name in cn=mapping tree,cn=config. The value of nsds5ReplicaEnabled needs to be on, and enabled on both sides. Remember that CA replication is done through a separate agreement and will need to be updated separately.</p>
<dd>
<dt>If you have older masters you should consider re-creating them rather than trying to re-initialize them.</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;password</code>=<i>PASSWORD</i></p>
<dd> The Directory Manager password.</p>
<dt><code>&#8211;data</code></p>
<dd> Restore the data only. The default is to restore everything in the backup.</p>
<dt><code>&#8211;gpg-keyring</code>=<i>GPG_KEYRING</i></p>
<dd> The full path to a GPG keyring. The keyring consists of two files, a public and a private key (.sec and .pub respectively). Specify the path without an extension.</p>
<dt><code>&#8211;no-logs</code></p>
<dd> Exclude the IPA service log files in the backup (if they were backed up).</p>
<dt><code>&#8211;online</code></p>
<dd> Perform the restore on-line. Requires data-only backup or the &#8211;data option.</p>
<dt><code>&#8211;instance</code>=<i>INSTANCE</i></p>
<dd> Restore only the databases in this 389-ds instance. The default is to restore all found (at most this is the IPA REALM instance and the PKI-IPA instance). Requires data-only backup or the &#8211;data option.</p>
<dt><code>&#8211;backend</code>=<i>BACKEND</i></p>
<dd> The backend to restore within an instance or instances. Requires data-only backup or the &#8211;data option.</p>
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
<p> /var/log/iparestore.log</p>
<dl>
<dt>
<dd> The log file for restoration </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ipa-backup/">ipa-backup</a>(1). </p>
<h2>Index</h2>
