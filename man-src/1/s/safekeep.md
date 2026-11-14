---
title: "safekeep(1)"
name: "safekeep"
section: "1"
letter: "s"
url: "/docs/linux/man/1-safekeep/"
description: "safekeep – Client/server backup script"
---

<h2 class="name">NAME</h2>
<p> safekeep &#8211; Client/server backup script </p>
<h2>SYNOPSIS</h2>
<p> <i>safekeep</i> &#8211;server [-q] [-v] [&#8211;noemail] [&#8211;force] [-c file] [&#8211;cleanup] &lt;clientid&gt;* </p>
<p> <i>safekeep</i> &#8211;keys [-q] [-v] [&#8211;noemail] [-c file] [-i file] [&#8211;status] [&#8211;print] [&#8211;deploy] &lt;clientid&gt;* </p>
<p> <i>safekeep</i> &#8211;list [-q] [-v] [&#8211;noemail] [-c file] [&#8211;increments] [&#8211;parsable-output] [&#8211;sizes] [&#8211;changed=&lt;time&gt;] [&#8211;at-time=&lt;time&gt;] &lt;clientid&gt;* </p>
<p> <i>safekeep</i> &#8211;client [&#8211;cleanup] </p>
<p> <i>safekeep</i> -h | -V</p>
<h2>DESCRIPTION</h2>
<p> SafeKeep is a client/server backup script which enhances the power of rdiff-backup with simple configuration and use. </p>
<p> SafeKeep can work in server mode, client mode, SSH key management mode or list mode. </p>
<p> In server mode, SafeKeep parses a set of configurations files which defines a set of backup clients. For each backup client, SafeKeep connects to the client host over SSH (using a public key authentification system previously set up using safekeep &#8211;keys &#8211;deploy), and launches safekeep &#8211;client onto the client host. The client does the real backup and sends the data over SSH to the SafeKeep server which stores it in the specified location. </p>
<p> In client mode, SafeKeep does a few setup steps, depending on the client configuration (database dump, LVM device snapshot), then backups the client data using rdiff-backup, and then cleanups the state (removes the database dumps, deactivates the LVM snapshots) </p>
<p> Note that the client mode of SafeKeep should never be invoked manually, this mode is meant to be used only by the server mode of SafeKeep. The only exception to this is if run with the &#8211;cleanup option, which is used to remove LVM snapshots and mounts created by Safekeep, after a crash or some other failure, without a connection to the server. Normally this cleanup would be performed through the server command safekeep &#8211;server &#8211;cleanup. </p>
<p> The SSH key management mode is a helper mode for deploying or verifying the setup of the SSH authentification keys. </p>
<p> In list mode, SafeKeep lists the details of existing archives. This is basically an interface to the relevant options for rdiff-backup. </p>
<p> In server, keys management and list mode, you can restrict the operation to a specific set of clients by listing the desired client IDs as arguments. If no client ID is given, SafeKeep will operate over all known clients. </p>
<p> Each mode accepts a few options as described below.</p>
<h2>OPERATION MODE</h2>
<p> &#8211;server</p>
<dl>
<dt>
<dd> Selects the server mode</dl>
<p> &#8211;client</p>
<dl>
<dt>
<dd> Selects the client mode. This should never be invoked manually, the clients are started automatically by the server on the client machines using SSH.</dl>
<p> &#8211;keys</p>
<dl>
<dt>
<dd> Selects the SSH key management mode</dl>
<p> &#8211;list</p>
<dl>
<dt>
<dd> Selects the list mode</dl>
<p> Please note that you must always specify an operation mode. Earlier versions used do default to &#8211;server mode, but that proved to work out poorly in practice.</p>
<h2>GENERAL OPTIONS</h2>
<p> -c, &#8211;conf=FILE</p>
<dl>
<dt>
<dd> Specifies the configuration file location. If not specified at all, SafeKeep will default to /etc/safekeep/safekeep.conf, or optionally in ~/.safekeep/safekeep.conf for non-root users, if it exists. Simply using this default is the recommended usage.</dl>
<p> -h, &#8211;help</p>
<dl>
<dt>
<dd> Selects the help mode, in which safekeep prints out the online help and exits.</dl>
<p> -V, &#8211;version</p>
<dl>
<dt>
<dd> Selects the version mode, in which safekeep prints out the version number and exits.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Decreases the verbosity level. Can be specified more than once.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Increases the verbosity level. Can be specified more than once.</dl>
<p> &#8211;noemail</p>
<dl>
<dt>
<dd> Disables the sending of email, no matter what the settings within the configuration file.</dl>
<h2>SERVER OPTIONS</h2>
<p> &#8211;force</p>
<dl>
<dt>
<dd> Pass the &#8211;force option to rdiff-backup, allowing it to overwrite the backup directory metadata. This option is potentially dangerous, and should only be used if the backup directory becomes corrupt, and rdiff-backup error logs tells you to use this option.</dl>
<p> &#8211;cleanup</p>
<dl>
<dt>
<dd> Remove LVM snapshots and mounts left by Safekeep after a crash or other failure. This will run also run the standard cleanup processes, such as the removal of an DB dumps, and forces a consistency check of the rdiff-backup destination directory. This is the prefered cleanup procedure and can be run with no danger of corrupting the system if there is nothing to cleanup.</dl>
<h2>CLIENT OPTIONS</h2>
<p> &#8211;cleanup</p>
<dl>
<dt>
<dd> Remove LVM snapshots and mounts left after a crash or other failure from the local system. Unlike the equivalent &#8211;server option, it does not do any other of the standard cleanups. This option should only be used when it is not possible to refer to the server, for example, when the network connection to the server is no longer available.</dl>
<h2>KEYS OPTIONS</h2>
<p> -i FILE</p>
<dl>
<dt>
<dd> Forces <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to use FILE for the identity (private key) in RSA/DSA authentication. If not specified, <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will use its default identity files.</dl>
<p> &#8211;status</p>
<dl>
<dt>
<dd> Display the key status for the clients. It is implied if no other option is specified. In effect this option prints the steps that will be taken when the keys are deployed to the client.</dl>
<p> &#8211;print</p>
<dl>
<dt>
<dd> Display the authorization keys for the clients. This is useful in case you want to manually copy it into the client&#8217;s ~/.ssh/authorized_keys file. This option is seldom useful.</dl>
<p> &#8211;deploy</p>
<dl>
<dt>
<dd> Deploy the authorization keys on the clients.</dl>
<h2>LIST OPTIONS</h2>
<p> &#8211;increments</p>
<dl>
<dt>
<dd> Pass the &#8211;list-increments option to rdiff-backup, to list the number and date of partial incremental backups for the given or all clients. This is the default list option.</dl>
<p> &#8211;parseable-output</p>
<dl>
<dt>
<dd> Pass the &#8211;parsable-output option to rdiff-backup to generate output in a format that is easily parsed by other programs. This currently only works with the &#8211;increments.</dl>
<p> &#8211;sizes</p>
<dl>
<dt>
<dd> Pass the &#8211;list-increment-sizes option to rdiff-backup, to list the total size of all increment and mirror files by time for the given or all clients. Note, this may take some time.</dl>
<p> &#8211;changed=TIME</p>
<dl>
<dt>
<dd> Pass the &#8211;list-changed-since option for TIME to rdiff-backup, to list the files changed since TIME for the given clients. TIME is passed directly to rdiff-backup. Note, this may take some time and generate considerable output. Also, unlike rdiff-backup the is no option to select sub-directories.</dl>
<p> &#8211;at-time=TIME</p>
<dl>
<dt>
<dd> Pass the &#8211;list-at-time option for TIME to rdiff-backup, to list the files in the archive that were present at the given time for the given clients. Note, this may take some time and generate considerable output. Also, unlike rdiff-backup the is no option to select sub-directories.</dl>
<h2>CONFIGURATION</h2>
<p> Normally the configuration files are placed in the /etc/safekeep/backup.d/ directory, or optionally in ~/.safekeep/backup.d/ for non-root users, from where they will get picked up automatically by SafeKeep. Each backup client is described by a configuration file in XML format. The minimum configuration file is: </p>
<dl>
<dt>
<dd>
<pre>
&lt;backup&gt;
  &lt;host name=&quot;my_workstation&quot; /&gt;
&lt;/backup&gt;
</pre>
</dl>
<p> This will simply backup all relevant files (excluding temporary files, caches, etc) from the client with the address my_workstation. </p>
<p> A more realistic example: </p>
<dl>
<dt>
<dd>
<pre><code>
&lt;backup&gt;
  &lt;host name="my_workstation" /&gt;
  &lt;repo retention="10D" /&gt;
  &lt;setup&gt;
      &lt;dump type="postgres" dbuser="postgres" file="/var/lib/pgsql/backups/all_dbs" /&gt;
      &lt;dump type="mysql" user="mysql" dbuser="dbbackup" db="adatabase" file="/var/backups/dumps/adatabase_dbs" /&gt;
      &lt;dump type="mysql" user="mysql" dbuser="dbbackup" db="mysql" file="/var/backups/dumps/mysql_dbs" cleanup="true" /&gt;
      &lt;snapshot device="/dev/mapper/VolGroup00-LogVol00" size="500M" /&gt;
  &lt;/setup&gt;
  &lt;data&gt;
    &lt;exclude regexp=".*\.ogg"/&gt;
    &lt;exclude regexp=".*\.mp3"/&gt;
    &lt;include path="/etc"/&gt;
    &lt;exclude glob="/home/*/tmp"/&gt;
    &lt;include path="/home"/&gt;
    &lt;include path="/root"/&gt;
    &lt;include path="/srv"/&gt;
    &lt;exclude path="/var/cache"/&gt;
    &lt;exclude path="/var/lock"/&gt;
    &lt;exclude path="/var/run"/&gt;
    &lt;exclude path="/var/tmp"/&gt;
    &lt;include path="/var/named/chroot/etc"/&gt;
    &lt;include path="/var/named/chroot/var/named"/&gt;
    &lt;exclude path="/var/named/chroot"/&gt;
    &lt;include path="/var"/&gt;
    &lt;exclude path="/"/&gt;
  &lt;/data&gt;
&lt;/backup&gt;
</code></pre>
</dl>
<p> In this case, SafeKeep will dump all databases managed by PostgreSQL, snapshot the disk via LVM, and proceed to backup /etc, /home, /root, /srv, /var, while excluding some unneeded files and directories. Older data will be retained for 10 days. </p>
<p> For full reference documentation of the configuration format, see <a href="/docs/linux/man/5-safekeep-backup/">safekeep.backup</a>(5).</p>
<h2>CLIENT IDS</h2>
<p> Normally the client IDs are generated automatically from the configuration filenames without the extension. E.g. if a configuration file is named my_workstation.conf, the client ID becomes my_workstation. For more information on this topic, see <a href="/docs/linux/man/5-safekeep-backup/">safekeep.backup</a>(5).</p>
<h2>KEY DEPLOYMENT</h2>
<p> The <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) server needs to access the clients in order to conduct the backup. To that end, it establishes two <a href="/docs/linux/man/1-ssh/">ssh</a>(1) pipes: one for control, and one for data. To simplify the deployment of the keys, <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) has a key deploy mode. </p>
<p> When deploying keys using the built-in key management functionality, <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) needs to be invoked as the user under which it will function as a server. By default, that user is <i>safekeep</i>. For extra security, you can not login into that account, so you have to invoke <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) as <i>root</i>: </p>
<dl>
<dt>
<dd>
<pre><code>
[root[at] yourbox ~] #safekeep-- keys-- deploy
</code></pre>
</dl>
<h2>RESTORING</h2>
<p> Since <a href="/docs/linux/man/1-safekeep/">safekeep</a>(1) is built around <a href="/docs/linux/man/1-rdiff-backup/">rdiff-backup</a>(1), it doesn&#8217;t have any built-in restore capabilities. It simply relies on rdiff-backup to perform this task. </p>
<p> To do so, you just need to know the directory where the data is actually stored. In a typical installation, for a box configured via the file /etc/safekeep/backup.d/mybox.backup, the data will be stored under /var/lib/safekeep/mybox/. Please refer to <a href="/docs/linux/man/5-safekeep-backup/">safekeep.backup</a>(5) for more information on this matter. </p>
<p> Once you have determined where the data will be stored (we&#8217;ll continue the example above), all you have to do is run rdiff-backup: </p>
<dl>
<dt>
<dd>
<pre>
        # rdiff-backup -r 1s /var/lib/safekeep/mybox my-restore-dir
</pre>
</dl>
<p> You will be able to find more information on the restore procedure in the <a href="/docs/linux/man/1-rdiff-backup/">rdiff-backup</a>(1) man page.</p>
<h2>FILE SELECTION</h2>
<p> It is important to note that the include/exclude directives that control file selection are matched in the order they appear in the configuration file, and the first one that matches dictates whether the file will be included or excluded. As a result, you have to add the more specific ones first, or the more generic specifications will always win. For example: </p>
<dl>
<dt>
<dd>
<pre>
...
    &lt;include path=&quot;/home&quot;/&gt;
    &lt;exclude path=&quot;/home/joe&quot;/&gt;
...
</pre>
</dl>
<p> will NOT do what you expect, because the /home will match before /home/joe, and thus all files under /home will be included. The correct way is to flip the two around </p>
<dl>
<dt>
<dd>
<pre>
...
    &lt;exclude path=&quot;/home/joe&quot;/&gt;
    &lt;include path=&quot;/home&quot;/&gt;
...
</pre>
</dl>
<p> Please see <a href="/docs/linux/man/5-safekeep-backup/">safekeep.backup</a>(5) for more information on file selection.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rdiff-backup/">rdiff-backup</a>(1), <a href="/docs/linux/man/5-safekeep-conf/">safekeep.conf</a>(5), <a href="/docs/linux/man/5-safekeep-backup/">safekeep.backup</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by Dimi Paun &lt;m[blue]<code>dimi [at] lattica.com</code>m[]<font SIZE="-2">[1]</font>&gt; and Stelian Pop &lt;m[blue]<code>stelian [at] lattica.com</code>m[]<font SIZE="-2">[2]</font>&gt;.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> dimi [at] lattica.com</p>
<dl>
<dt>
<dd> mailto:dimi [at] lattica.com</dl>
<dt> 2.</p>
<dd> stelian [at] lattica.com</p>
<dl>
<dt>
<dd> mailto:stelian [at] lattica.com</dl>
</dl>
<h2>Index</h2>
