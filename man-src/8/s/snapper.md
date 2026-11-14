---
title: "snapper(8)"
name: "snapper"
section: "8"
letter: "s"
url: "/docs/linux/man/8-snapper/"
description: "snapper – Command-line program for filesystem snapshot management"
---

<p>snapper &#8211; Command-line program for filesystem snapshot management</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snapper</code> [<i>&#8211;global-opts</i>] <i>command</i> [<i>&#8211;command-opts</i>] [<i>command-arguments</i>]</p>
<dt> <code>snapper</code> {&#8211;help}</dl>
<h2>Description</h2>
<dd>Snapper is a command-line program for filesystem snapshot management. It can create, delete and compare snapshots and undo changes done between snapshots. </p>
<p> Snapper never modifies the content of snapshots. Thus snapper creates read-only snapshots if supported by the kernel. Supported filesystems are btrfs as well as snapshots of LVM logical volumes with thin-provisioning.</p>
<h2>Concepts</h2>
<h3>Configurations</h3>
<p>For each filesystem or subvolume that should be snapshotted by snapper, a configuration file is required, see <code><a href="/docs/linux/man/5-snapper-configs/">snapper-configs</a></code>(5). The setup can be done with the create-config command.</p>
<h3>Snapshots</h3>
<p>Snapper distinguishes three types of snapshots. </p>
<p> pre</p>
<dl>
<dd>Pre snapshots should always have a corresponding post snapshot. The intention of pre/post snapshot pairs is to snapshot the filesystem before and after a modification.</dl>
<p> post</p>
<dl>
<dd>See pre type.</dl>
<p> single</p>
<dl>
<dd>These snapshots have no special relationship to other snapshots.</dl>
<p> Note that filesystem-wise all three types are the same.</p>
<h3>Snapshot Description and Userdata</h3>
<p>With each snapshot a description and some userdata can be associated. The description is a string. The userdata is a list of key-value pairs where the keys and values are strings.</p>
<h3>Automatic Snapshot Creation</h3>
<p>Next to manual snapshot creation, snapshots are also created automatically. </p>
<dl>
<dd>&bull; A cron-job creates hourly snapshots.</dl>
<h3>Cleanup Algorithms</h3>
<p>Snapper provides several algorithms to clean up old snapshots. The algorithms are executed in a daily cron-job. This can be configured in the corresponding configurations files along with parameters for every algorithm. </p>
<p> number</p>
<dl>
<dd>Deletes old snapshots when a certain number of snapshots is reached.</dl>
<p> timeline</p>
<dl>
<dd>Deletes old snapshots but keeps a number of hourly, daily, weekly, monthly and yearly snapshots.</dl>
<p> empty-pre-post</p>
<dl>
<dd>Deletes pre/post snapshot pairs with empty diffs.</dl>
<h3>Filters</h3>
<p>Some files keep state information of the system, e.g. /etc/mtab. Such files should never be reverted. To help users, snapper allows to ignore these files. </p>
<p> Each line in all files /etc/snapper/filters/*.txt specifies a pattern. When snapper computes the difference between two snapshots it ignores all files and directories matching any of those patterns by using <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3) with the flag FNM_LEADING_DIR. </p>
<p> Note that filters do not exclude files or directories from being snapshotted. For that, use subvolumes or mount points.</p>
<h2>Global Options</h2>
<p><code>-q, &#8211;quiet</code></p>
<dl>
<dd>Suppress normal output. Error messages will still be printed, though.</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>Increase verbosity.</dl>
<p> <code>&#8211;utc</code></p>
<dl>
<dd>Display dates and times in UTC.</dl>
<p> <code>&#8211;iso</code></p>
<dl>
<dd>Display dates and times in ISO format.</dl>
<p> <code>-t, &#8211;table-style</code></p>
<dl>
<dd>Specifies table style. Table style is identified by an integer number.</dl>
<p> <code>-c, &#8211;config </code><i>name</i></p>
<dl>
<dd>Use specified configuration instead of the default configuration. The default configuration is named &quot;root&quot;.</dl>
<p> <code>&#8211;no-dbus</code></p>
<dl>
<dd>Operate without a DBus connection. Only works for some commands. </p>
<p> Use with caution since a running snapperd will not know about modifications made to the system.</dl>
<p> <code>-r, &#8211;root </code><i>path</i></p>
<dl>
<dd>Operate on target root. Only works together with no-dbus and only for some commands.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print version and exit.</dl>
<h2>Commands</h2>
<p>Snapper provides a number of <i>commands</i>. Each command accepts the options listed in the GLOBAL OPTIONS section. These options must be specified <i>before</i> the command name. In addition, many commands have specific options, which are listed in this section. These command-specific options must be specified <i>after</i> the name of the command and <i>before</i> any of the command arguments. </p>
<p> <code>help</code></p>
<dl>
<dd>Show short help text.</dl>
<p> <code>list-configs</code></p>
<dl>
<dd>List available configurations.</dl>
<p> <code>create-config [options] </code><i>subvolume</i></p>
<dl>
<dd>Create a new configuration for a filesystem or subvolume. For this command you will likely need the global option <code>&#8211;config</code>, see GLOBAL OPTIONS and CONCEPTS. </p>
<p> <code>-f, &#8211;fstype</code> <i>fstype</i></p>
<dl>
<dd>Manually set filesystem type. Supported values are btrfs and lvm. For lvm, snapper uses LVM thin-provisioned snapshots. The filesystem type on top of LVM must be provided in parentheses, e.g. lvm(xfs). </p>
<p> Without this option snapper tries to detect the filesystem.</dl>
<p> <code>-t, &#8211;template</code> <i>name</i></p>
<dl>
<dd>Name of template for the new configuration file.</dl>
</dl>
<p> <code>delete-config</code></p>
<dl>
<dd>Delete a configuration for a filesystem or subvolume. For this command you will likely need to global option <code>&#8211;config</code>, see GLOBAL OPTIONS and CONCEPTS.</dl>
<p> <code>get-config</code></p>
<dl>
<dd>Displays the settings of the configuration.</dl>
<p> <code>set-config</code> <i>configdata</i></p>
<dl>
<dd>Changes the settings of the configuration. The settings <i>configdata</i> are a list of key-value-pairs separated by spaces and the key and value must be separated by an equal sign, e.g. &quot;NUMBER_CLEANUP=yes NUMBER_LIMIT=10&quot;. The value of SUBVOLUME and FSTYPE cannot be changed.</dl>
<p> <code>list (ls) [options]</code></p>
<dl>
<dd>List snapshots. </p>
<p> <code>-t, &#8211;type</code> <i>type</i></p>
<dl>
<dd>Selects type of snapshots to list. Possible values are all, single and pre-post.</dl>
<p> <code>-a, &#8211;all-configs</code></p>
<dl>
<dd>List snapshots from all configs accessible by the user.</dl>
</dl>
<p> <code>create [options]</code></p>
<dl>
<dd>Create a new snapshot. </p>
<p> <code>-t, &#8211;type</code> <i>type</i></p>
<dl>
<dd>Specifies the type of the new snapshot. Possible values are single, pre and post.</dl>
<p> <code>&#8211;pre-number</code> <i>number</i></p>
<dl>
<dd>For post snapshots the number of the pre snapshot must be provided.</dl>
<p> <code>-p, &#8211;print-number</code></p>
<dl>
<dd>Print number of the created snapshot.</dl>
<p> <code>-d, &#8211;description</code> <i>description</i></p>
<dl>
<dd>Description for the snapshot.</dl>
<p> <code>-c, &#8211;cleanup-algorithm</code> <i>cleanup-algorithm</i></p>
<dl>
<dd>Set the cleanup algorithm for the snapshot.</dl>
<p> <code>-u, &#8211;userdata</code> <i>userdata</i></p>
<dl>
<dd>Set userdata for the snapshot. The key-value pairs must be separated by comma and the key and value must be separated by an equal sign, e.g. requestid=42,user=arthur.</dl>
<p> <code>&#8211;command</code> <i>command</i></p>
<dl>
<dd>Create a pre and post snapshot and run command in between.</dl>
</dl>
<p> <code>modify [options] </code><i>number</i></p>
<dl>
<dd>Modify a snapshot. </p>
<p> <code>-d, &#8211;description</code> <i>description</i></p>
<dl>
<dd>New description for snapshot.</dl>
<p> <code>-c, &#8211;cleanup-algorithm</code> <i>cleanup-algorithm</i></p>
<dl>
<dd>Set the cleanup algorithm for the snapshot.</dl>
<p> <code>-u, &#8211;userdata</code> <i>userdata</i></p>
<dl>
<dd>Set userdata for the snapshot. The key-value pairs must be separated by comma and the key and value must be separated by an equal sign, e.g. requestid=42,user=arthur.</dl>
</dl>
<p> <code>delete (remove|rm) </code><i>number</i><code> | </code><i>number1-number2</i></p>
<dl>
<dd>Delete a snapshot or a range of snapshots. </p>
<p> <code>-s, &#8211;sync</code></p>
<dl>
<dd>Sync the filesystem after deleting the snapshots. The details depend on the filesystem type. </p>
<p> Btrfs normally asynchronously frees space after deleting snapshots. With this option snapper will wait until the space once used by the deleted snapshots is actually available again.</dl>
</dl>
<p> <code>mount </code><i>number</i></p>
<dl>
<dd>Mount a snapshot. Not required for all filesystem types.</dl>
<p> <code>umount </code><i>number</i></p>
<dl>
<dd>Unmount a snapshot. Not required for all filesystem types.</dl>
<p> <code>status [options] </code><i>number1</i><code>..</code><i>number2</i></p>
<dl>
<dd>Compare the snapshots <i>number1</i> and <i>number2</i>. This will show a list of files and directories that have been created, modified or deleted in the time between the two snapshots have been made. </p>
<p> <code>-o, &#8211;output</code> <i>file</i></p>
<dl>
<dd>Write output to file <i>file</i>.</dl>
<p> The output consists of a string encoding the status followed by the filename. The characters of the status string are: </p>
<dl>
<dd>1. A &quot;+&quot; means the file was created, a &quot;-&quot; means the file was deleted. A &quot;c&quot; means the content of the file has changed and a &quot;t&quot; means the type of the file has changed (e.g. from regular file to directory).</dl>
<dl>
<dd>2. A &quot;p&quot; means the permissions are have changed.</dl>
<dl>
<dd>3. An &quot;u&quot; means the user ownership has changed.</dl>
<dl>
<dd>4. A &quot;g&quot; means the group ownership has changed.</dl>
<dl>
<dd>5. A &quot;x&quot; means the extended attribute information has changed.</dl>
<dl>
<dd>6. An &quot;a&quot; means the ACL information has changed.</dl>
<p> If there is no change a &quot;.&quot; is outputted.</dl>
<p> <code>diff [options] </code><i>number1</i><code>..</code><i>number2</i><code> [files]</code></p>
<dl>
<dd>Compare the snapshots <i>number1</i> and <i>number2</i>. This will show a diff of the content of files and directories that have been created, modified or deleted in the time between the two snapshots have been made. </p>
<p> <code>-i, &#8211;input</code> <i>file</i></p>
<dl>
<dd>Read files to diff from file <i>file</i>.</dl>
<p> <code>&#8211;diff-cmd</code> <i>command</i></p>
<dl>
<dd>Command used for comparing files. The default is /usr/bin/diff &#8211;new-file &#8211;unified. The two files to compare are passed as parameters to the command.</dl>
<p> <code>-x, &#8211;extensions</code> <i>options</i></p>
<dl>
<dd>Extra options passed to the diff command.</dl>
</dl>
<p> <code>undochange [options] </code><i>number1</i><code>..</code><i>number2</i><code> [files]</code></p>
<dl>
<dd>Undo changes done between snapshot <i>number1</i> and <i>number2</i>. </p>
<p> <code>-i, &#8211;input</code> <i>file</i></p>
<dl>
<dd>Read files for which to undo changes from file <i>file</i>.</dl>
</dl>
<p> <code>rollback [options] [</code><i>number</i><code>]</code></p>
<dl>
<dd>Creates two new snapshots and sets the default subvolume. Per default the system boots from the default subvolume of the root filesystem. The exact actions depend on whether a number is provided or not: </p>
<dl>
<dd>&bull; Without a number, a first read-only snapshot of the default subvolume is created. A second read-write snapshot of the current system is created. The system is set to boot from the second snapshot.</dl>
<dl>
<dd>&bull; With a number, a first read-only snapshot of the current system in created. A second read-write snapshot is created of <i>number</i>. The system is set to boot from the second snapshot.</dl>
<p> Rollback is only supported with btrfs and requires a properly configured system. </p>
<p> <code>-p, &#8211;print-number</code></p>
<dl>
<dd>Print number of the second created snapshot.</dl>
<p> <code>-d, &#8211;description</code> <i>description</i></p>
<dl>
<dd>Description for the snapshot.</dl>
<p> <code>-c, &#8211;cleanup-algorithm</code> <i>cleanup-algorithm</i></p>
<dl>
<dd>Set the cleanup algorithm for the snapshot.</dl>
<p> <code>-u, &#8211;userdata</code> <i>userdata</i></p>
<dl>
<dd>Set userdata for the snapshot. The key-value pairs must be separated by comma and the key and value must be separated by an equal sign, e.g. requestid=42,user=arthur.</dl>
</dl>
<p> <code>cleanup </code><i>cleanup-algorithm</i></p>
<dl>
<dd>Run the cleanup algorithm <i>cleanup-algorithm</i>. Currently implemented cleanup algorithms are number, timeline and empty-pre-post.</dl>
<p> <code>xadiff </code><i>number1</i><code>..</code><i>number2</i><code> [files]</code></p>
<dl>
<dd>Compare the extended attributes between snapshot <i>number1</i> and <i>number2</i>. See examples below: </p>
<dl>
<dd>&bull; +:user.foo for created attributes</dl>
<dl>
<dd>&bull; -:user.bar for removed attributes</dl>
<dl>
<dd>&bull; -+:security.selinux for modified attributes</dl>
</dl>
<h2>Permissions</h2>
<p>Non-root users can be allowed to use a configuration by setting ALLOW_USERS or ALLOW_GROUPS in the config file. For all operations to work, the user must also be able to read and access the .snapshots directory inside the subvolume. The .snapshots directory must be owned by root and must not be writable by anybody else. </p>
<p> Here are some methods how to achieve that: </p>
<dl>
<dd>&bull; Make the directory accessible for everyone: </p>
<p> <code>chmod a+rx .snapshots</code></dl>
<dl>
<dd>&bull; Make the directory accessible for a group the user belongs to, e.g.: </p>
<p> <code>chown :users .snapshots</code></dl>
<dl>
<dd>&bull; Make the directory accessible for the user using ACLs, e.g.: </p>
<p> <code>setfacl -m u:tux:rx .snapshots</code></dl>
<p> The last method can be performed by snapper, see the SYNC_ACL setting in <code><a href="/docs/linux/man/5-snapper-configs/">snapper-configs</a></code>(5).</p>
<h2>Files</h2>
<p>/etc/sysconfig/snapper</p>
<dl>
<dd>Global configuration file.</dl>
<p> /etc/snapper/configs</p>
<dl>
<dd>Directory containing configuration files.</dl>
<p> /etc/snapper/config-templates</p>
<dl>
<dd>Directory containing configuration templates.</dl>
<p> /etc/snapper/filters/*.txt</p>
<dl>
<dd>Filter files.</dl>
<p> /var/log/snapper.log</p>
<dl>
<dd>Logfile. Please include this file in bug reports.</dl>
<h2>Notes</h2>
<p>There is no mechanism to ensure consistency of the files while a snapshot it made. E.g. the files of a database can be inconsistent while the database is running. </p>
<p> Consistency after undochange is not guaranteed. E.g. when the creation of a user is undone, there might still exist files from that user. </p>
<p> Support for individual filesystems, rollback and extended attributes are compile-time options and may not be available.</p>
<h2>Homepage</h2>
<p>m[blue]<code><a rel="nofollow" href="http://snapper.io/">http://snapper.io/</a></code>m[]</p>
<h2>Authors</h2>
<p>Arvin Schnell &lt;aschnell [at] suse.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-snapper-configs/">snapper-configs</a></code>(5), <code><a href="/docs/linux/man/8-snapper-zypp-plugin/">snapper-zypp-plugin</a></code>(8), <code><a href="/docs/linux/man/8-pam_snapper/">pam_snapper</a></code>(8), <code><a href="/docs/linux/man/8-btrfs/">btrfs</a></code>(8), <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/5-attr/">attr</a></code>(5), <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5) </p>
