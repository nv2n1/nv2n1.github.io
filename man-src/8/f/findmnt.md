---

title: "findmnt(8)"
name: "findmnt"
section: "8"
letter: "f"
url: "/docs/linux/man/8-findmnt/"
description: "findmnt – find a filesystem"
---

<p>findmnt &#8211; find a filesystem </p>

<p> <code>findmnt</code> [options] </p>
<p> <code>findmnt</code> [options] <i>device</i>|<i>mountpoint</i> </p>
<p> <code>findmnt</code> [options] [<code>--source</code>] <i>device</i> [<code>--target</code> <i>path</i>|<code>--mountpoint</code> <i>mountpoint</i>]  </p>
<h2>DESCRIPTION</h2>
<p> <code>findmnt</code> will list all mounted filesystems or search for a filesystem. The <code>findmnt</code> command is able to search in <i>/etc/fstab</i>, <i>/etc/mtab</i> or <i>/proc/self/mountinfo</i>. If <i>device</i> or <i>mountpoint</i> is not given, all filesystems are shown. </p>
<p>The device may be specified by device name, major:minor numbers, filesystem label or UUID, or partition label or UUID. Note that <code>findmnt</code> follows <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) behavior where a device name may be interpreted as a mountpoint (and vice versa) if the <code>--target</code>, <code>--mountpoint</code> or <code>--source</code> options are not specified. </p>
<p>The command-line option <code>--target</code> accepts any file or directory and then <code>findmnt</code> displays the filesystem for the given path. </p>
<p>The command prints all mounted filesystems in the tree-like format by default.  </p>
<h2>OPTIONS</h2>
<p> <code>-A</code>, <code>--all</code> </p>
<dl>
<dd> <p> Disable all built-in filters and print all filesystems. </p>
 </dd></dl>
<p> <code>-a</code>, <code>--ascii</code> </p>
<dl>
<dd> <p> Use ascii characters for tree formatting. </p>
 </dd></dl>
<p> <code>-b</code>, <code>--bytes</code> </p>
<dl>
<dd> <p> Print the SIZE, USED and AVAIL columns in bytes rather than in a human-readable format. </p>
 </dd></dl>
<p> <code>-C</code>, <code>--nocanonicalize</code> </p>
<dl>
<dd> <p> Do not canonicalize paths at all. This option affects the comparing of paths and the evaluation of tags (LABEL, UUID, etc.). </p>
 </dd></dl>
<p> <code>-c</code>, <code>--canonicalize</code> </p>
<dl>
<dd> <p> Canonicalize all printed paths. </p>
 </dd></dl>
<p> <code>-D</code>, <code>--df</code> </p>
<dl>
<dd> <p> Imitate the output of <code><a href="/docs/linux/man/1-df/">df</a></code>(1). This option is equivalent to <code>-o SOURCE,FSTYPE,SIZE,USED,AVAIL,USE%,TARGET</code> but excludes all pseudo filesystems. Use <code>--all</code> to print all filesystems. </p>
 </dd></dl>
<p> <code>-d</code>, <code>--direction</code> <i>word</i> </p>
<dl>
<dd> <p> The search direction, either <code>forward</code> or <code>backward</code>. </p>
 </dd></dl>
<p> <code>-e</code>, <code>--evaluate</code> </p>
<dl>
<dd> <p> Convert all tags (LABEL, UUID, PARTUUID or PARTLABEL) to the corresponding device names. </p>
 </dd></dl>
<p> <code>-F</code>, <code>--tab-file</code> <i>path</i> </p>
<dl>
<dd> <p> Search in an alternative file. If used with <code>--fstab</code>, <code>--mtab</code> or <code>--kernel</code>, then it overrides the default paths. If specified more than once, then tree-like output is disabled (see the <code>--list</code> option). </p>
 </dd></dl>
<p> <code>-f</code>, <code>--first-only</code> </p>
<dl>
<dd> <p> Print the first matching filesystem only. </p>
 </dd></dl>
<p> <code>-h</code>, <code>--help</code> </p>
<dl>
<dd> <p> Display help text and exit. </p>
 </dd></dl>
<p> <code>-i</code>, <code>--invert</code> </p>
<dl>
<dd> <p> Invert the sense of matching. </p>
 </dd></dl>
<p> <code>-J</code>, <code>--json</code> </p>
<dl>
<dd> <p> Use JSON output format. </p>
 </dd></dl>
<p> <code>-k</code>, <code>--kernel</code> </p>
<dl>
<dd> <p> Search in <i>/proc/self/mountinfo</i>. The output is in the tree-like format. This is the default. The output contains only mount options maintained by kernel (see also <code>--mtab)</code>. </p>
 </dd></dl>
<p> <code>-l</code>, <code>--list</code> </p>
<dl>
<dd> <p> Use the list output format. This output format is automatically enabled if the output is restricted by the <code>-t</code>, <code>-O</code>, <code>-S</code> or <code>-T</code> option and the option <code>--submounts</code> is not used or if more that one source file (the option <code>-F</code>) is specified. </p>
 </dd></dl>
<p> <code>-M</code>, <code>--mountpoint</code> <i>path</i> </p>
<dl>
<dd> <p> Explicitly define the mountpoint file or directory. See also <code>--target</code>. </p>
 </dd></dl>
<p> <code>-m</code>, <code>--mtab</code> </p>
<dl>
<dd> <p> Search in <i>/etc/mtab</i>. The output is in the list format by default (see <code>--tree</code>). The output may include user space mount options. </p>
 </dd></dl>
<p> <code>-N</code>, <code>--task</code> <i>tid</i> </p>
<dl>
<dd> <p> Use alternative namespace <i>/proc/&lt;tid&gt;/mountinfo</i> rather than the default <i>/proc/self/mountinfo</i>. If the option is specified more than once, then tree-like output is disabled (see the <code>--list</code> option). See also the <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1) command. </p>
 </dd></dl>
<p> <code>-n</code>, <code>--noheadings</code> </p>
<dl>
<dd> <p> Do not print a header line. </p>
 </dd></dl>
<p> <code>-O</code>, <code>--options</code> <i>list</i> </p>
<dl>
<dd> <p> Limit the set of printed filesystems. More than one option may be specified in a comma-separated list. The <code>-t</code> and <code>-O</code> options are cumulative in effect. It is different from <code>-t</code> in that each option is matched exactly; a leading <i>no</i> at the beginning does not have global meaning. The &quot;no&quot; can used for individual items in the list. The &quot;no&quot; prefix interpretation can be disabled by &quot;+&quot; prefix. </p>
 </dd></dl>
<p> <code>-o</code>, <code>--output</code> <i>list</i> </p>
<dl>
<dd> <p> Define output columns. See the <code>--help</code> output to get a list of the currently supported columns. The <code>TARGET</code> column contains tree formatting if the <code>--list</code> or <code>--raw</code> options are not specified. </p>
<p>The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i> (e.g., <code>findmnt -o +PROPAGATION</code>). </p>
 </dd></dl>
<p> <code>--output-all</code> </p>
<dl>
<dd> <p> Output almost all available columns. The columns that require <code>--poll</code> are not included. </p>
 </dd></dl>
<p> <code>-P</code>, <code>--pairs</code> </p>
<dl>
<dd> <p> Produce output in the form of key=&quot;value&quot; pairs. All potentially unsafe value characters are hex-escaped (\x&lt;code&gt;). </p>
 </dd></dl>
<p> <code>-p</code>, <code>--poll</code>[<i>=list</i>] </p>
<dl>
<dd> <p> Monitor changes in the <i>/proc/self/mountinfo</i> file. Supported actions are: mount, umount, remount and move. More than one action may be specified in a comma-separated list. All actions are monitored by default. </p>
<p>The time for which <code>--poll</code> will block can be restricted with the <code>--timeout</code> or <code>--first-only</code> options. </p>
<p>The standard columns always use the new version of the information from the mountinfo file, except the umount action which is based on the original information cached by <code>findmnt</code>. The poll mode allows using extra columns: </p>
<p> <code>ACTION</code> </p>
 </dd>
<dl>
<dd> <p> mount, umount, move or remount action name; this column is enabled by default </p>
 </dd></dl>
<p> <code>OLD-TARGET</code> </p>
<dl>
<dd> <p> available for umount and move actions </p>
 </dd></dl>
<p> <code>OLD-OPTIONS</code> </p>
<dl>
<dd> <p> available for umount and remount actions </p>
 </dd></dl>
</dl>
<p> <code>--pseudo</code> </p>
<dl>
<dd> <p> Print only pseudo filesystems. </p>
 </dd></dl>
<p> <code>--shadow</code> </p>
<dl>
<dd> <p> Print only filesystems over-mounted by another filesystem. </p>
 </dd></dl>
<p> <code>-R</code>, <code>--submounts</code> </p>
<dl>
<dd> <p> Print recursively all submounts for the selected filesystems. The restrictions defined by options <code>-t</code>, <code>-O</code>, <code>-S</code>, <code>-T</code> and <code>--direction</code> are not applied to submounts. All submounts are always printed in tree-like order. The option enables the tree-like output format by default. This option has no effect for <code>--mtab</code> or <code>--fstab</code>. </p>
 </dd></dl>
<p> <code>-r</code>, <code>--raw</code> </p>
<dl>
<dd> <p> Use raw output format. All potentially unsafe characters are hex-escaped (\x&lt;code&gt;). </p>
 </dd></dl>
<p> <code>--real</code> </p>
<dl>
<dd> <p> Print only real filesystems. </p>
 </dd></dl>
<p> <code>-S</code>, <code>--source</code> <i>spec</i> </p>
<dl>
<dd> <p> Explicitly define the mount source. Supported specifications are <i>device</i>, <i>maj</i><code>:</code><i>min</i>, <code>LABEL=</code><i>label</i>, <code>UUID=</code><i>uuid</i>, <code>PARTLABEL=</code><i>label</i> and <code>PARTUUID=</code><i>uuid</i>. </p>
 </dd></dl>
<p> <code>-s</code>, <code>--fstab</code> </p>
<dl>
<dd> <p> Search in <i>/etc/fstab</i>. The output is in the list format (see <code>--list</code>). </p>
 </dd></dl>
<p> <code>-T</code>, <code>--target</code> <i>path</i> </p>
<dl>
<dd> <p> Define the mount target. If <i>path</i> is not a mountpoint file or directory, then <code>findmnt</code> checks the <i>path</i> elements in reverse order to get the mountpoint (this feature is supported only when searching in kernel files and unsupported for <code>--fstab</code>). It&#8217;s recommended to use the option <code>--mountpoint</code> when checks of <i>path</i> elements are unwanted and <i>path</i> is a strictly specified mountpoint. </p>
 </dd></dl>
<p> <code>-t</code>, <code>--types</code> <i>list</i> </p>
<dl>
<dd> <p> Limit the set of printed filesystems. More than one type may be specified in a comma-separated list. The list of filesystem types can be prefixed with <code>no</code> to specify the filesystem types on which no action should be taken. For more details see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
 </dd></dl>
<p> <code>--tree</code> </p>
<dl>
<dd> <p> Enable tree-like output if possible. The options is silently ignored for tables where is missing child-parent relation (e.g., fstab). </p>
 </dd></dl>
<p> <code>--shadowed</code> </p>
<dl>
<dd> <p> Print only filesystems over-mounted by another filesystem. </p>
 </dd></dl>
<p> <code>-U</code>, <code>--uniq</code> </p>
<dl>
<dd> <p> Ignore filesystems with duplicate mount targets, thus effectively skipping over-mounted mount points. </p>
 </dd></dl>
<p> <code>-u</code>, <code>--notruncate</code> </p>
<dl>
<dd> <p> Do not truncate text in columns. The default is to not truncate the <code>TARGET</code>, <code>SOURCE</code>, <code>UUID</code>, <code>LABEL</code>, <code>PARTUUID</code>, <code>PARTLABEL</code> columns. This option disables text truncation also in all other columns. </p>
 </dd></dl>
<p> <code>-v</code>, <code>--nofsroot</code> </p>
<dl>
<dd> <p> Do not print a [/dir] in the SOURCE column for bind mounts or btrfs subvolumes. </p>
 </dd></dl>
<p> <code>-w</code>, <code>--timeout</code> <i>milliseconds</i> </p>
<dl>
<dd> <p> Specify an upper limit on the time for which <code>--poll</code> will block, in milliseconds. </p>
 </dd></dl>
<p> <code>-x</code>, <code>--verify</code> </p>
<dl>
<dd> <p> Check mount table content. The default is to verify <i>/etc/fstab</i> parsability and usability. It&#8217;s possible to use this option also with <code>--tab-file</code>. It&#8217;s possible to specify source (device) or target (mountpoint) to filter mount table. The option <code>--verbose</code> forces findmnt to print more details. </p>
 </dd></dl>
<p> <code>--verbose</code> </p>
<dl>
<dd> <p> Force findmnt to print more information (<code>--verify</code> only for now). </p>
 </dd></dl>
<p> <code>--vfs-all</code> </p>
<dl>
<dd> <p> When used with <code>VFS-OPTIONS</code> column, print all VFS (fs-independent) flags. This option is designed for auditing purposes to list also default VFS kernel mount options which are normally not listed. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p>LIBMOUNT_FSTAB=&lt;path&gt; </p>
<dl>
<dd> <p> overrides the default location of the fstab file </p>
 </dd></dl>
<p>LIBMOUNT_MTAB=&lt;path&gt; </p>
<dl>
<dd> <p> overrides the default location of the mtab file </p>
 </dd></dl>
<p>LIBMOUNT_DEBUG=all </p>
<dl>
<dd> <p> enables libmount debug output </p>
 </dd></dl>
<p>LIBSMARTCOLS_DEBUG=all </p>
<dl>
<dd> <p> enables libsmartcols debug output </p>
 </dd></dl>
<p>LIBSMARTCOLS_DEBUG_PADDING=on </p>
<dl>
<dd> <p> use visible padding characters. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> <code>findmnt --fstab -t nfs</code> </p>
<dl>
<dd> <p> Prints all NFS filesystems defined in <i>/etc/fstab</i>. </p>
 </dd></dl>
<p> <code>findmnt --fstab /mnt/foo</code> </p>
<dl>
<dd> <p> Prints all <i>/etc/fstab</i> filesystems where the mountpoint directory is <i>/mnt/foo</i>. It also prints bind mounts where <i>/mnt/foo</i> is a source. </p>
 </dd></dl>
<p> <code>findmnt --fstab --target /mnt/foo</code> </p>
<dl>
<dd> <p> Prints all <i>/etc/fstab</i> filesystems where the mountpoint directory is <i>/mnt/foo</i>. </p>
 </dd></dl>
<p> <code>findmnt --fstab --evaluate</code> </p>
<dl>
<dd> <p> Prints all <i>/etc/fstab</i> filesystems and converts LABEL= and UUID= tags to the real device names. </p>
 </dd></dl>
<p> <code>findmnt -n --raw --evaluate --output=target LABEL=/boot</code> </p>
<dl>
<dd> <p> Prints only the mountpoint where the filesystem with label &quot;/boot&quot; is mounted. </p>
 </dd></dl>
<p> <code>findmnt --poll --mountpoint /mnt/foo</code> </p>
<dl>
<dd> <p> Monitors mount, unmount, remount and move on <i>/mnt/foo</i>. </p>
 </dd></dl>
<p> <code>findmnt --poll=umount --first-only --mountpoint /mnt/foo</code> </p>
<dl>
<dd> <p> Waits for <i>/mnt/foo</i> unmount. </p>
 </dd></dl>
<p> <code>findmnt --poll=remount -t ext3 -O ro</code> </p>
<dl>
<dd> <p> Monitors remounts to read-only mode on all ext3 filesystems. </p>
 </dd></dl>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)  </p>
<h2>REPORTING BUGS</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.  </p>
<h2>AVAILABILITY</h2>
<p>The <code>findmnt</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
