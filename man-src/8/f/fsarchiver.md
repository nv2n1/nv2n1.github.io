---
title: "fsarchiver(8)"
name: "fsarchiver"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsarchiver/"
description: "fsarchiver – filesystem archiver"
---

<p>fsarchiver &#8211; filesystem archiver</p>
<h2>Description</h2>
<p>fsarchiver is a system tool that allows you to save the contents of a filesystem to a compressed archive file. The file-system can be restored on a partition which has a different size and it can be restored on a different file-system. Unlike tar/dar, FSArchiver also creates the filesystem when it extracts the data to partitions. Everything is checksummed in the archive in order to protect the data. If the archive is corrupt, you just lose the current file, not the whole archive. </p>
<h2>Links</h2>
<h3>Official project homepage:</h3>
<p><a rel="nofollow" href="http://www.fsarchiver.org">http://www.fsarchiver.org</a></p>
<h3>Quick Start Guide:</h3>
<p><a rel="nofollow" href="http://www.fsarchiver.org/QuickStart">http://www.fsarchiver.org/QuickStart</a></p>
<h3>Forums where to ask questions:</h3>
<p><a rel="nofollow" href="http://www.fsarchiver.org/forums/">http://www.fsarchiver.org/forums/</a></p>
<h3>Report a bug:</h3>
<p><a rel="nofollow" href="http://www.fsarchiver.org/forums/viewforum.php?f=17">http://www.fsarchiver.org/forums/viewforum.php?f=17</a></p>
<h2>Synopsis</h2>
<p><code>fsarchiver [</code> <i>options</i> <code>] savefs</code> <i>archive</i> <i>filesystem</i> <code>&#8230;</code> <code>fsarchiver [</code> <i>options</i> <code>] restfs</code> <i>archive</i> <code>id=</code><i>n</i><code>,dest=</code><i>filesystem</i><code>[,mkfs=</code><i>fstype,</i><code>mkfsopt=</code><i>options</i><code>]</code> <code>&#8230;</code> <code>fsarchiver [</code> <i>options</i> <code>] savedir</code> <i>archive</i> <i>directory</i> <code>&#8230;</code> <code>fsarchiver [</code> <i>options</i> <code>] restdir</code> <i>archive destination</i> <code>fsarchiver [</code> <i>options</i> <code>] archinfo</code> <i>archive</i> <code>fsarchiver [</code> <i>options</i> <code>] probe [detailed]</code> </p>
<h2>Commands</h2>
<dl>
<dt><code>savefs</code></p>
<dd>Save <i>filesystems</i> to <i>archive</i>.</p>
<dt><code>restfs</code></p>
<dd>Restore filesystems from <i>archive</i>. This overwrites the existing data on <i>filesystems</i>. Zero-based index <i>n</i> indicates the part of the archive to restore. Optionally, a filesystem may be converted to <i>fstype</i>.</p>
<dt><code>savedir</code></p>
<dd>Save <i>directories</i> to <i>archive</i> (similar to a compressed tarball).</p>
<dt><code>restdir</code></p>
<dd>Restore data from <i>archive</i> which is not based on a filesystem to <i>destination</i>.</p>
<dt><code>archinfo</code></p>
<dd>Show information about an existing <i>archive</i> file and its contents.</p>
<dt><code>probe</code></p>
<dd>Show list of filesystems detected on the disks. </p>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show help and information about how to use fsarchiver with examples.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Show program version and exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Verbose mode (can be used several times to increase the level of details). The details will be printed to the console.</p>
<dt><code>-o, &#8211;overwrite</code></p>
<dd>Overwrite the archive if it already exists instead of failing.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd>Debug mode (can be used several times to increase the level of details). The details will be written in /var/log/fsarchiver.log.</p>
<dt><code>-A, &#8211;allow-rw-mounted</code></p>
<dd>Allow to save a filesystem which is mounted in read-write (live backup). By default fsarchiver fails with an error if the partition if mounted in read-write mode which allows modifications to be done on the filesystem during the backup. Modifications can drive to inconsistencies in the backup. Using lvm snapshots is the recommended way to make backups since it will provide consistency, but it is only available for filesystems which are on LVM logical-volumes.</p>
<dt><code>-a, &#8211;allow-no-acl-xattr</code></p>
<dd>Allow to run savefs when partition is mounted without the acl/xattr options. By default fsarchiver fails with an error if the partition is mounted in such a way that the ACL and Extended-Attributes are not readable. These attributes would not be saved and then such attributes could be lost. If you know what you don&#8217;t need ACL and Extended-Attributes to be preserved then it&#8217;s safe to run fsarchiver with that option.</p>
<dt><code>-e pattern, &#8211;exclude=pattern</code></p>
<dd>Exclude files and directories that match that pattern. The pattern can contains shell asterisks such as * and ?, and the pattern may be either a simple file/dir name or an absolute file/dir path. You must use quotes around the pattern each time you use wildcards, else it would be interpreted by the shell. The wildcards must be interpreted by fsarchiver. See examples below for more details about this option.</p>
<dt><code>-L label, &#8211;label=label</code></p>
<dd>Set the label of the archive: it&#8217;s just a comment about the contents. It can be used to remember a particular thing about the archive or the state of the filesystem for instance.</p>
<dt><code>-z level, &#8211;compress=level</code></p>
<dd>Valid compression levels are between 1 (very fast) and 9 (very good). The memory requirement increases a lot with the best compression levels, and it&#8217;s multiplied by the number of compression threads (option -j). Level 9 is considered as an extreme compression level and requires an huge amount of memory to run. For more details please read this page: <a rel="nofollow" href="http://www.fsarchiver.org/Compression">http://www.fsarchiver.org/Compression</a></p>
<dt><code>-s mbsize, &#8211;split=mbsize</code></p>
<dd>Split the archive into several files of mbsize megabytes each.</p>
<dt><code>-j count, &#8211;jobs=count</code></p>
<dd>Create more than one compression thread. Useful on multi-core CPUs. By default fsarchiver will only use one compression thread (-j 1) and then only one logical processor will be used for compression. You should use that option if you have a multi-core CPU or more than one physical CPU on your computer. The typical way to use this option is to specify the number of logical processors available so that all the processing power is used to compress the archive very quickly. You may also want to use all the logical processors but one for that task so that the system stays responsive for other applications.</p>
<dt><code>-c password, &#8211;cryptpass=password</code></p>
<dd>Encrypt/decrypt data in archive. Password length: 6 to 64 chars. You can either provide a real password or a dash (&quot;-c -&quot;) with this option if you do not want to provide the password in the command line and you want to be prompted for a password in the terminal instead. </p>
</dl>
<h2>Examples</h2>
<h3>save only one filesystem (/dev/sda1) to an archive:</h3>
<p>fsarchiver savefs /data/myarchive1.fsa /dev/sda1</p>
<h3>save two filesystems (/dev/sda1 and /dev/sdb1) to an archive:</h3>
<p>fsarchiver savefs /data/myarchive2.fsa /dev/sda1 /dev/sdb1</p>
<h3>restore the first filesystem from an archive (first = number 0):</h3>
<p>fsarchiver restfs /data/myarchive2.fsa id=0,dest=/dev/sda1</p>
<h3>restore the second filesystem from an archive (second = number 1):</h3>
<p>fsarchiver restfs /data/myarchive2.fsa id=1,dest=/dev/sdb1</p>
<h3>restore two filesystems from an archive (number 0 and 1):</h3>
<p>fsarchiver restfs /data/arch2.fsa id=0,dest=/dev/sda1 id=1,dest=/dev/sdb1</p>
<h3>restore a filesystem from an archive and convert it to reiserfs:</h3>
<p>fsarchiver restfs /data/myarchive1.fsa id=0,dest=/dev/sda1,mkfs=reiserfs</p>
<h3>restore a filesystem from an archive and specify extra mkfs options:</h3>
<p>fsarchiver restfs /data/myarchive1.fsa id=0,dest=/dev/sda1,mkfs=ext4,mkfsopt=&quot;-I 256&quot;</p>
<h3>save the contents of /usr/src/linux to an archive (similar to tar):</h3>
<p>fsarchiver savedir /data/linux-sources.fsa /usr/src/linux</p>
<h3>save a /dev/sda1 to an archive split into volumes of 680MB:</h3>
<p>fsarchiver savefs -s 680 /data/myarchive1.fsa /dev/sda1</p>
<h3>save a filesystem and exclude all files/dirs called &#8216;pagefile.*&#8217;</h3>
<p>fsarchiver savefs /data/myarchive.fsa /dev/sda1 &#8211;exclude=&#8217;pagefile.*&#8217;</p>
<h3>exclude &#8216;share&#8217; in both &#8216;/usr/share&#8217; and &#8216;/usr/local/share&#8217;:</h3>
<p>fsarchiver savefs /data/myarchive.fsa &#8211;exclude=share</p>
<h3>absolute exclude valid for &#8216;/usr/share&#8217; but not &#8216;/usr/local/share&#8217;</h3>
<p>fsarchiver savefs /data/myarchive.fsa &#8211;exclude=/usr/share</p>
<h3>save a filesystem (/dev/sda1) to an encrypted archive:</h3>
<p>fsarchiver savefs -c mypassword /data/myarchive1.fsa /dev/sda1</p>
<h3>extract an archive made of simple files to /tmp/extract:</h3>
<p>fsarchiver restdir /data/linux-sources.fsa /tmp/extract</p>
<h3>show information about an archive and its file systems:</h3>
<p>fsarchiver archinfo /data/myarchive2.fsa </p>
<h2>Warning</h2>
<p><code>fsarchiver</code> is still in development, don&#8217;t use it for critical data yet.</p>
<h2>Author</h2>
<p>fsarchiver was written by Francois Dupoux. It is released under the GPL2 (GNU General Public License version 2). This manpage was written by Ilya Barygin and Francois Dupoux.</p>
