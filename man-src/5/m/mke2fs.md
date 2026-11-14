---
title: "mke2fs(5)"
name: "mke2fs"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mke2fs/"
description: "mke2fs.conf – Configuration file for mke2fs"
---

<p>mke2fs.conf &#8211; Configuration file for mke2fs</p>
<h2>Description</h2>
<p><i>mke2fs.conf</i> is the configuration file for <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8). It controls the default parameters used by <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) when it is creating ext2, ext3, or ext4 filesystems. The <i>mke2fs.conf</i> file uses an INI-style format. Stanzas, or top-level sections, are delimited by square braces: [ ]. Within each section, each line defines a relation, which assigns tags to values, or to a subsection, which contains further relations or subsections. An example of the INI-style format used by this configuration file follows below: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[section1]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tag1 = value_a</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tag1 = value_b</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tag2 = value_c</p>
<pre><code>[section 2]

tag3 = {

    subtag1 = subtag_value_a

    subtag1 = subtag_value_b

    subtag2 = subtag_value_c

}

tag1 = value_d

tag2 = value_e

}</code></pre>
<p> Comments are delimited by a semicolon (&#8216;;&#8217;) or a hash (&#8216;#&#8217;) character at the beginning of the comment, and are terminated by the end of line character. Tags and values must be quoted using double quotes if they contain spaces. Within a quoted string, the standard backslash interpretations apply: &quot;
&quot; (for the newline character), &quot;	&quot; (for the tab character), &quot;&quot; (for the backspace character), and &quot;\&quot; (for the backslash character). Some relations expect a boolean value. The parser is quite liberal on recognizing &#8220;yes&#8221;, &#8216;`y&#8221;, &#8220;true&#8221;, &#8220;t&#8221;, &#8220;1&#8221;, &#8220;on&#8221;, etc. as a boolean true value, and &#8220;no&#8221;, &#8220;n&#8221;, &#8220;false&#8221;, &#8220;nil&#8221;, &#8220;0&#8221;, &#8220;off&#8221; as a boolean false value. The following stanzas are used in the <i>mke2fs.conf</i> file. They will be described in more detail in future sections of this document.</p>
<dl>
<dt><i>[options]</i></p>
<dd>Contains relations which influence how mke2fs behaves.</p>
<dt><i>[defaults]</i></p>
<dd>Contains relations which define the default parameters used by <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8). In general, these defaults may be overridden by a definition in the <code>fs_types</code> stanza, or by an command-line option provided by the user.</p>
<dt><i>[fs_types]</i></p>
<dd>Contains relations which define defaults that should be used for specific filesystem types. The filesystem type can be specified explicitly using the <code>-T</code> option to <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8).</dl>
<h2>THE [options] STANZA</h2>
<p>The following relations are defined in the <i>[options]</i> stanza.</p>
<dl>
<dt><i>proceed_delay</i></p>
<dd>If this relation is set to a positive integer, then if mke2fs will proceed after waiting <i>proceed_delay</i> seconds, after asking the user for permission to proceed, even if the user has not answered the question. Defaults to 0, which means to wait until the user answers the question one way or another.</dl>
<h2>THE [defaults] STANZA</h2>
<p>The following relations are defined in the <i>[defaults]</i> stanza.</p>
<dl>
<dt><i>base_features</i></p>
<dd>This relation specifies the filesystems features which are enabled in newly created filesystems. It may be overridden by the <i>base_features</i> relation found in the filesystem or usage type subsection of the <i>[fs_types] </i> stanza.</p>
<dt><i>default_features</i></p>
<dd>This relation specifies a set of features that should be added or removed to the features listed in the <i>base_features</i> relation. It may be overridden by the filesystem-specific <i>default_features</i> in the filesystem or usage type subsection of <i>[fs_types]</i>, and by the <code>-O</code> command-line option to <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8).</p>
<dt><i>enable_periodic_fsck</i></p>
<dd>This boolean relation specifies whether periodic filesystem checks should be enforced at boot time. If set to true, checks will be forced every 180 days, or after a random number of mounts. These values may be changed later via the <code>-i</code> and <code>-c</code> command-line options to <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8).</p>
<dt><i>force_undo</i></p>
<dd>This boolean relation, if set to a value of true, forces <code>mke2fs</code> to always try to create an undo file, even if the undo file might be huge and it might extend the time to create the filesystem image because the inode table isn&#8217;t being initialized lazily.</p>
<dt><i>fs_type</i></p>
<dd>This relation specifies the default filesystem type if the user does not specify it via the <code>-t</code> option, or if <code>mke2fs</code> is not started using a program name of the form <code>mkfs.</code><i>fs-type</i>. If both the user and the <code>mke2fs.conf</code> file does not specify a default filesystem type, mke2fs will use a default filesystem type of <i>ext3</i> if a journal was requested via a command-line option, or <i>ext2</i> if not.</p>
<dt><i>blocksize</i></p>
<dd>This relation specifies the default blocksize if the user does not specify a blocksize on the command line, and the filesystem-type specific section of the configuration file does not specify a blocksize.</p>
<dt><i>hash_alg</i></p>
<dd>This relation specifies the default hash algorithm used for the new filesystems with hashed b-tree directories. Valid algorithms accepted are: <i>legacy</i>, <i>half_md4</i>, and <i>tea</i>.</p>
<dt><i>inode_ratio</i></p>
<dd>This relation specifies the default inode ratio if the user does not specify one on the command line, and the filesystem-type specific section of the configuration file does not specify a default inode ratio.</p>
<dt><i>inode_size</i></p>
<dd>This relation specifies the default inode size if the user does not specify one on the command line, and the filesystem-type specific section of the configuration file does not specify a default inode size.</p>
<dt><i>reserved_ratio</i></p>
<dd>This relation specifies the default percentage of filesystem blocks reserved for the super-user, if the user does not specify one on the command line, and the filesystem-type specific section of the configuration file does not specify a default reserved ratio. This value can be a floating point number.</p>
<dt><i>undo_dir</i></p>
<dd>This relation specifies the directory where the undo file should be stored. It can be overridden via the <code>E2FSPROGS_UNDO_DIR</code> environment variable. If the directory location is set to the value <i>none</i>, <code>mke2fs</code> will not create an undo file.</dl>
<h2>THE [fs_types] STANZA</h2>
<p>Each tag in the <i>[fs_types] </i> stanza names a filesystem type or usage type which can be specified via the <code>-t</code> or <code>-T</code> options to <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), respectively. </p>
<p> The <code>mke2fs</code> program constructs a list of fs_types by concatenating the filesystem type (i.e., ext2, ext3, etc.) with the usage type list. For most configuration options, <code>mke2fs</code> will look for a subsection in the <i>[fs_types]</i> stanza corresponding with each entry in the constructed list, with later entries overriding earlier filesystem or usage types. For example, consider the following <code>mke2fs.conf</code> fragment: </p>
<p> [defaults]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>base_features = sparse_super,filetype,resize_inode,dir_index</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>blocksize = 4096</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>inode_size = 256</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>inode_ratio = 16384</p>
<p> [fs_types]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ext3 = {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>features = has_journal</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ext4 = {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>features = extents,flex_bg</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>inode_size = 256</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>small = {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>blocksize = 1024</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>inode_ratio = 4096</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>floppy = {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>features = ^resize_inode</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>blocksize = 1024</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>inode_size = 128</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> If mke2fs started with a program name of <code>mke2fs.ext4</code>, then the filesystem type of ext4 will be used. If the filesystem is smaller than 3 megabytes, and no usage type is specified, then <code>mke2fs</code> will use a default usage type of <i>floppy</i>. This results in an fs_types list of &quot;ext4, floppy&quot;. Both the ext4 subsection and the floppy subsection define an <i>inode_size</i> relation, but since the later entries in the fs_types list supersede earlier ones, the configuration parameter for fs_types.floppy.inode_size will be used, so the filesystem will have an inode size of 128. </p>
<p> The exception to this resolution is the <i>features</i> tag, which is specifies a set of changes to the features used by the filesystem, and which is cumulative. So in the above example, first the configuration relation defaults.base_features would enable an initial feature set with the sparse_super, filetype, resize_inode, and dir_index features enabled. Then configuration relation fs_types.ext4.features would enable the extents and flex_bg features, and finally the configuration relation fs_types.floppy.features would remove the resize_inode feature, resulting in a filesystem feature set consisting of the sparse_super, filetype, resize_inode, dir_index, extents_and flex_bg features. </p>
<p> For each filesystem type, the following tags may be used in that fs_type&#8217;s subsection:</p>
<dl>
<dt><i>base_features</i></p>
<dd>This relation specifies the features which are initially enabled for this filesystem type. Only one <i>base_features</i> will be used, so if there are multiple entries in the fs_types list whose subsections define the <i>base_features</i> relation, only the last will be used by <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8).</p>
<dt><i>features</i></p>
<dd>This relation specifies a comma-separated list of features edit requests which modify the feature set used by the newly constructed filesystem. The syntax is the same as the <code>-O</code> command-line option to <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8); that is, a feature can be prefixed by a caret (&#8216;^&#8217;) symbol to disable a named feature. Each <i>feature</i> relation specified in the fs_types list will be applied in the order found in the fs_types list.</p>
<dt><i>default_features</i></p>
<dd>This relation specifies set of features which should be enabled or disabled after applying the features listed in the <i>base_features</i> and <i>features</i> relations. It may be overridden by the <code>-O</code> command-line option to <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8).</p>
<dt><i>auto_64-bit_support</i></p>
<dd>This relation is a boolean which specifies whether <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) should automatically add the 64bit feature if the number of blocks for the file system requires this feature to be enabled. The resize_inode feature is also automatically disabled since it doesn&#8217;t support 64-bit block numbers.</p>
<dt><i>default_mntopts</i></p>
<dd>This relation specifies the set of mount options which should be enabled by default. These may be changed at a later time with the <code>-o</code> command-line option to <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8).</p>
<dt><i>blocksize</i></p>
<dd>This relation specifies the default blocksize if the user does not specify a blocksize on the command line.</p>
<dt><i>lazy_itable_init</i></p>
<dd>This boolean relation specifies whether the inode table should be lazily initialized. It only has meaning if the uninit_bg feature is enabled. If lazy_itable_init is true and the uninit_bg feature is enabled, the inode table will not fully initialized by <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8). This speeds up filesystem initialization noticeably, but it requires the kernel to finish initializing the filesystem in the background when the filesystem is first mounted.</p>
<dt><i>journal_location</i></p>
<dd>This relation specifies the location of the journal.</p>
<dt><i>num_backup_sb</i></p>
<dd>This relation indicates whether file systems with the <code>sparse_super2</code> feature enabled should be created with 0, 1, or 2 backup superblocks.</p>
<dt><i>packed_meta_blocks</i></p>
<dd>This boolean relation specifes whether the allocation bitmaps, inode table, and journal should be located at the beginning of the file system.</p>
<dt><i>inode_ratio</i></p>
<dd>This relation specifies the default inode ratio if the user does not specify one on the command line.</p>
<dt><i>inode_size</i></p>
<dd>This relation specifies the default inode size if the user does not specify one on the command line.</p>
<dt><i>reserved_ratio</i></p>
<dd>This relation specifies the default percentage of filesystem blocks reserved for the super-user, if the user does not specify one on the command line.</p>
<dt><i>hash_alg</i></p>
<dd>This relation specifies the default hash algorithm used for the new filesystems with hashed b-tree directories. Valid algorithms accepted are: <i>legacy</i>, <i>half_md4</i>, and <i>tea</i>.</p>
<dt><i>flex_bg_size</i></p>
<dd>This relation specifies the number of block groups that will be packed together to create one large virtual block group on an ext4 filesystem. This improves meta-data locality and performance on meta-data heavy workloads. The number of groups must be a power of 2 and may only be specified if the flex_bg filesystem feature is enabled.</p>
<dt><i>options</i></p>
<dd>This relation specifies additional extended options which should be treated by <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) as if they were prepended to the argument of the <code>-E</code> option. This can be used to configure the default extended options used by <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) on a per-filesystem type basis.</p>
<dt><i>discard</i></p>
<dd>This boolean relation specifies whether the <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) should attempt to discard device prior to filesystem creation.</p>
<dt><i>cluster_size</i></p>
<dd>This relation specifies the default cluster size if the bigalloc file system feature is enabled. It can be overridden via the <code>-C</code> command line option to <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8)</p>
<dt><i>make_hugefiles</i></p>
<dd>This boolean relation enables the creation of pre-allocated files as part of formatting the file system.</p>
<dt><i>hugefiles_uid</i></p>
<dd>This relation controls the user ownership for all of the files and directories created by the <i>make_hugefiles</i> feature.</p>
<dt><i>hugefiles_gid</i></p>
<dd>This relation controls the group ownership for all of the files and directories created by the <i>make_hugefiles</i> feature.</p>
<dt><i>hugefiles_umask</i></p>
<dd>This relation specifies the umask used when creating the files and directories by the <i>make_hugefiles</i> feature.</p>
<dt><i>num_hugefiles</i></p>
<dd>This relation specifies the number of huge files to be created. If this relation is not specified, or is set to zero, and the <i>hugefiles_size</i> relation is non-zero, then <i>make_hugefiles</i> will create as many huge files as can fit to fill the entire file system.</p>
<dt><i>hugefiles_slack</i></p>
<dd>This relation specifies how much space should be reserved for other files.</p>
<dt><i>hugefiles_size</i></p>
<dd>This relation specifies the size of the huge files. If this relation is not specified, the default is to fill the entire file system.</p>
<dt><i>hugefiles_align</i></p>
<dd>This relation specifies the alignment for the start block of the huge files. It also forces the size of huge files to be a multiple of the requested alignment. If this relation is not specified, no alignment requirement will be imposed on the huge files.</p>
<dt><i>hugefiles_align_disk</i></p>
<dd>Thie relations specifies whether the alignment should be relative to the beginning of the hard drive (assuming that the starting offset of the partition is available to mke2fs). The default value is false, which if will cause hugefile alignment to be relative to the beginning of the file system.</p>
<dt><i>hugefiles_name</i></p>
<dd>This relation specifies the base file name for the huge files.</p>
<dt><i>hugefiles_digits</i></p>
<dd>This relation specifies the (zero-padded) width of the field for the huge file number.</p>
<dt><i>zero_hugefiles</i></p>
<dd>This boolean relation specifies whether or not zero blocks will be written to the hugefiles while <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a>(8)</code> is creating them. By default, zero blocks will be written to the huge files to avoid stale data from being made available to potentially untrusted user programs, unless the device supports a discard/trim operation which will take care of zeroing the device blocks. By <i>zero_hugefiles</i> to false, this step will always be skipped, which can be useful if it is known that the disk has been previously erased, or if the user programs that will have access to the huge files are trusted to not reveal stale data.</dl>
<h2>THE [devices] STANZA</h2>
<p>Each tag in the <i>[devices] </i> stanza names device name so that per-device defaults can be specified.</p>
<dl>
<dt><i>fs_type</i></p>
<dd>This relation specifies the default parameter for the <code>-t</code> option, if this option isn&#8217;t specified on the command line.</p>
<dt><i>usage_types</i></p>
<dd>This relation specifies the default parameter for the <code>-T</code> option, if this option isn&#8217;t specified on the command line.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/mke2fs.conf</i></p>
<dd>The configuration file for <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) </p>
