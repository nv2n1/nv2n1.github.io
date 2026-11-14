---
title: "chattr(1)"
name: "chattr"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chattr/"
description: "chattr – change file attributes on a Linux file system"
---

<h2 class="name">NAME</h2>
<p> chattr &#8211; change file attributes on a Linux file system </p>
<h2>SYNOPSIS</h2>
<p> <code>chattr</code> [ <code>-RVf</code> ] [ <code>-v</code> <i>version</i> ] [ <code>-p</code> <i>project</i> ] [ <i>mode</i> ] <i>files&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>chattr</code> changes the file attributes on a Linux file system. </p>
<p> The format of a symbolic mode is +-=[aAcCdDeFijmPsStTux]. </p>
<p> The operator &#8216;+&#8217; causes the selected attributes to be added to the existing attributes of the files; &#8216;-&#8216; causes them to be removed; and &#8216;=&#8217; causes them to be the only attributes that the files have. </p>
<p> The letters &#8216;aAcCdDeFijmPsStTux&#8217; select the new attributes for the files: append only (a), no atime updates (A), compressed (c), no copy on write (C), no dump (d), synchronous directory updates (D), extent format (e), case-insensitive directory lookups (F), immutable (i), data journaling (j), don&#8217;t compress (m), project hierarchy (P), secure deletion (s), synchronous updates (S), no tail-merging (t), top of directory hierarchy (T), undeletable (u), and direct access for files (x). </p>
<p> The following attributes are read-only, and may be listed by <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1) but not modified by chattr: encrypted (E), indexed directory (I), inline data (N), and verity (V). </p>
<p> Not all flags are supported or utilized by all file systems; refer to file system-specific man pages such as <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5), <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5), and <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5) for more file system-specific details.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-R</code></p>
<dd> Recursively change attributes of directories and their contents.</p>
<dt><code>-V</code></p>
<dd> Be verbose with chattr&#8217;s output and print the program version.</p>
<dt><code>-f</code></p>
<dd> Suppress most error messages.</p>
<dt><code>-v</code><i> version</i></p>
<dd> Set the file&#8217;s version/generation number.</p>
<dt><code>-p</code><i> project</i></p>
<dd> Set the file&#8217;s project number.</dl>
<h2>ATTRIBUTES</h2>
<dl>
<dt><code>a</code></p>
<dd> A file with the &#8216;a&#8217; attribute set can only be opened in append mode for writing. Only the superuser or a process possessing the CAP_LINUX_IMMUTABLE capability can set or clear this attribute.</p>
<dt><code>A</code></p>
<dd> When a file with the &#8216;A&#8217; attribute set is accessed, its atime record is not modified. This avoids a certain amount of disk I/O for laptop systems.</p>
<dt><code>c</code></p>
<dd> A file with the &#8216;c&#8217; attribute set is automatically compressed on the disk by the kernel. A read from this file returns uncompressed data. A write to this file compresses data before storing them on the disk. Note: please make sure to read the bugs and limitations section at the end of this document. (Note: For btrfs, If the &#8216;c&#8217; flag is set, then the &#8216;C&#8217; flag cannot be set. Also conflicts with btrfs mount option &#8216;nodatasum&#8217;)</p>
<dt><code>C</code></p>
<dd> A file with the &#8216;C&#8217; attribute set will not be subject to copy-on-write updates. This flag is only supported on file systems which perform copy-on-write. (Note: For btrfs, the &#8216;C&#8217; flag should be set on new or empty files. If it is set on a file which already has data blocks, it is undefined when the blocks assigned to the file will be fully stable. If the &#8216;C&#8217; flag is set on a directory, it will have no effect on the directory, but new files created in that directory will have the No_COW attribute set. If the &#8216;C&#8217; flag is set, then the &#8216;c&#8217; flag cannot be set.)</p>
<dt><code>d</code></p>
<dd> A file with the &#8216;d&#8217; attribute set is not a candidate for backup when the <code><a href="/docs/linux/man/8-dump/">dump</a></code>(8) program is run.</p>
<dt><code>D</code></p>
<dd> When a directory with the &#8216;D&#8217; attribute set is modified, the changes are written synchronously to the disk; this is equivalent to the &#8216;dirsync&#8217; mount option applied to a subset of the files.</p>
<dt><code>e</code></p>
<dd> The &#8216;e&#8217; attribute indicates that the file is using extents for mapping the blocks on disk. It may not be removed using <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1).</p>
<dt><code>E</code></p>
<dd> A file, directory, or symlink with the &#8216;E&#8217; attribute set is encrypted by the file system. This attribute may not be set or cleared using <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1), although it can be displayed by <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1).</p>
<dt><code>F</code></p>
<dd> A directory with the &#8216;F&#8217; attribute set indicates that all the path lookups inside that directory are made in a case-insensitive fashion. This attribute can only be changed in empty directories on file systems with the casefold feature enabled.</p>
<dt><code>i</code></p>
<dd> A file with the &#8216;i&#8217; attribute cannot be modified: it cannot be deleted or renamed, no link can be created to this file, most of the file&#8217;s metadata can not be modified, and the file can not be opened in write mode. Only the superuser or a process possessing the CAP_LINUX_IMMUTABLE capability can set or clear this attribute.</p>
<dt><code>I</code></p>
<dd> The &#8216;I&#8217; attribute is used by the htree code to indicate that a directory is being indexed using hashed trees. It may not be set or cleared using <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1), although it can be displayed by <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1).</p>
<dt><code>j</code></p>
<dd> A file with the &#8216;j&#8217; attribute has all of its data written to the ext3 or ext4 journal before being written to the file itself, if the file system is mounted with the &quot;data=ordered&quot; or &quot;data=writeback&quot; options and the file system has a journal. When the file system is mounted with the &quot;data=journal&quot; option all file data is already journalled and this attribute has no effect. Only the superuser or a process possessing the CAP_SYS_RESOURCE capability can set or clear this attribute.</p>
<dt><code>m</code></p>
<dd> A file with the &#8216;m&#8217; attribute is excluded from compression on file systems that support per-file compression.</p>
<dt><code>N</code></p>
<dd> A file with the &#8216;N&#8217; attribute set indicates that the file has data stored inline, within the inode itself. It may not be set or cleared using <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1), although it can be displayed by <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1).</p>
<dt><code>P</code></p>
<dd> A directory with the &#8216;P&#8217; attribute set will enforce a hierarchical structure for project id&#8217;s. This means that files and directories created in the directory will inherit the project id of the directory, rename operations are constrained so when a file or directory is moved into another directory, that the project ids must match. In addition, a hard link to file can only be created when the project id for the file and the destination directory match.</p>
<dt><code>s</code></p>
<dd> When a file with the &#8216;s&#8217; attribute set is deleted, its blocks are zeroed and written back to the disk. Note: please make sure to read the bugs and limitations section at the end of this document.</p>
<dt><code>S</code></p>
<dd> When a file with the &#8216;S&#8217; attribute set is modified, the changes are written synchronously to the disk; this is equivalent to the &#8216;sync&#8217; mount option applied to a subset of the files.</p>
<dt><code>t</code></p>
<dd> A file with the &#8216;t&#8217; attribute will not have a partial block fragment at the end of the file merged with other files (for those file systems which support tail-merging). This is necessary for applications such as LILO which read the file system directly, and which don&#8217;t understand tail-merged files. Note: As of this writing, the ext2, ext3, and ext4 file systems do not support tail-merging.</p>
<dt><code>T</code></p>
<dd> A directory with the &#8216;T&#8217; attribute will be deemed to be the top of directory hierarchies for the purposes of the Orlov block allocator. This is a hint to the block allocator used by ext3 and ext4 that the subdirectories under this directory are not related, and thus should be spread apart for allocation purposes. For example it is a very good idea to set the &#8216;T&#8217; attribute on the /home directory, so that /home/john and /home/mary are placed into separate block groups. For directories where this attribute is not set, the Orlov block allocator will try to group subdirectories closer together where possible.</p>
<dt><code>u</code></p>
<dd> When a file with the &#8216;u&#8217; attribute set is deleted, its contents are saved. This allows the user to ask for its undeletion. Note: please make sure to read the bugs and limitations section at the end of this document.</p>
<dt><code>x</code></p>
<dd> The &#8216;x&#8217; attribute can be set on a directory or file. If the attribute is set on an existing directory, it will be inherited by all files and subdirectories that are subsequently created in the directory. If an existing directory has contained some files and subdirectories, modifying the attribute on the parent directory doesn&#8217;t change the attributes on these files and subdirectories.</p>
<dt><code>V</code></p>
<dd> A file with the &#8216;V&#8217; attribute set has fs-verity enabled. It cannot be written to, and the file system will automatically verify all data read from it against a cryptographic hash that covers the entire file&#8217;s contents, e.g. via a Merkle tree. This makes it possible to efficiently authenticate the file. This attribute may not be set or cleared using <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1), although it can be displayed by <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1).</dl>
<h2>AUTHOR</h2>
<p> <code>chattr</code> was written by Remy Card &lt;Remy.Card [at] linux.org&gt;. It is currently being maintained by Theodore Ts&#8217;o &lt;tytso [at] alum.mit.edu&gt;.</p>
<h2>BUGS AND LIMITATIONS</h2>
<p> The &#8216;c&#8217;, &#8216;s&#8217;, and &#8216;u&#8217; attributes are not honored by the ext2, ext3, and ext4 file systems as implemented in the current mainline Linux kernels. Setting &#8216;a&#8217; and &#8216;i&#8217; attributes will not affect the ability to write to already existing file descriptors. </p>
<p> The &#8216;j&#8217; option is only useful for ext3 and ext4 file systems. </p>
<p> The &#8216;D&#8217; option is only useful on Linux kernel 2.5.19 and later.</p>
<h2>AVAILABILITY</h2>
<p> <code>chattr</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1), <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5), <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5). </p>
<h2>Index</h2>
