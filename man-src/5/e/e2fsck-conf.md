---
title: "e2fsck-conf(5)"
name: "e2fsck-conf"
section: "5"
letter: "e"
url: "/docs/linux/man/5-e2fsck-conf/"
description: "e2fsck.conf – Configuration file for e2fsck"
---

<p>e2fsck.conf &#8211; Configuration file for e2fsck</p>
<h2>Description</h2>
<p><i>e2fsck.conf</i> is the configuration file for <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8). It controls the default behavior of <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) while it is checking ext2, ext3, or ext4 file systems. The <i>e2fsck.conf</i> file uses an INI-style format. Stanzas, or top-level sections, are delimited by square braces: [ ]. Within each section, each line defines a relation, which assigns tags to values, or to a subsection, which contains further relations or subsections. An example of the INI-style format used by this configuration file follows below: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[section1]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>tag1 = value_a</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>tag1 = value_b</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>tag2 = value_c</p>
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
&quot; (for the newline character), &quot;	&quot; (for the tab character), &quot;&quot; (for the backspace character), and &quot;\&quot; (for the backslash character). The following stanzas are used in the <i>e2fsck.conf</i> file. They will be described in more detail in future sections of this document.</p>
<dl>
<dt><i>[options]</i></p>
<dd>This stanza contains general configuration parameters for <code>e2fsck</code>&#8216;s behavior.</p>
<dt><i>[defaults]</i></p>
<dd>Contains relations which define the default parameters used by <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8). In general, these defaults may be overridden by command-line options provided by the user.</p>
<dt><i>[problems]</i></p>
<dd>This stanza allows the administrator to reconfigure how e2fsck handles various file system inconsistencies.</p>
<dt><i>[scratch_files]</i></p>
<dd>This stanza controls when e2fsck will attempt to use scratch files to reduce the need for memory.</dl>
<h2>THE [options] STANZA</h2>
<p>The following relations are defined in the <i>[options]</i> stanza.</p>
<dl>
<dt><i>allow_cancellation</i></p>
<dd>If this relation is set to a boolean value of true, then if the user interrupts e2fsck using ^C, and the file system is not explicitly flagged as containing errors, e2fsck will exit with an exit status of 0 instead of 32. This setting defaults to false.</p>
<dt><i>accept_time_fudge</i></p>
<dd>Unfortunately, due to Windows&#8217; unfortunate design decision to configure the hardware clock to tick localtime, instead of the more proper and less error-prone UTC time, many users end up in the situation where the system clock is incorrectly set at the time when e2fsck is run.</p>
<dd>Historically this was usually due to some distributions having buggy init scripts and/or installers that didn&#8217;t correctly detect this case and take appropriate countermeasures. Unfortunately, this is occasionally true even today, usually due to a buggy or misconfigured virtualization manager or the installer not having access to a network time server during the installation process. So by default, we allow the superblock times to be fudged by up to 24 hours. This can be disabled by setting <i>accept_time_fudge</i> to the boolean value of false. This setting defaults to true.</p>
<dt><i>broken_system_clock</i></p>
<dd>The <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) program has some heuristics that assume that the system clock is correct. In addition, many system programs make similar assumptions. For example, the UUID library depends on time not going backwards in order for it to be able to make its guarantees about issuing universally unique ID&#8217;s. Systems with broken system clocks, are well, broken. However, broken system clocks, particularly in embedded systems, do exist. E2fsck will attempt to use heuristics to determine if the time can not be trusted; and to skip time-based checks if this is true. If this boolean is set to true, then e2fsck will always assume that the system clock can not be trusted.</p>
<dt><i>buggy_init_scripts</i></p>
<dd>This boolean relation is an alias for <i>accept_time_fudge</i> for backwards compatibility; it used to be that the behavior defined by <i>accept_time_fudge</i> above defaulted to false, and <i>buggy_init_scripts</i> would enable superblock time field to be wrong by up to 24 hours. When we changed the default, we also renamed this boolean relation to <i>accept_time_fudge.</i></p>
<dt><i>clear_test_fs_flag</i></p>
<dd>This boolean relation controls whether or not <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) will offer to clear the test_fs flag if the ext4 file system is available on the system. It defaults to true.</p>
<dt><i>defer_check_on_battery</i></p>
<dd>This boolean relation controls whether or not the interval between file system checks (either based on time or number of mounts) should be doubled if the system is running on battery. This setting defaults to true.</p>
<dt><i>indexed_dir_slack_percentage</i></p>
<dd>When <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) repacks a indexed directory, reserve the specified percentage of empty space in each leaf nodes so that a few new entries can be added to the directory without splitting leaf nodes, so that the average fill ratio of directories can be maintained at a higher, more efficient level. This relation defaults to 20 percent.</p>
<dt><i>inode_count_fullmap</i></p>
<dd>If this boolean relation is true, trade off using memory for speed when checking a file system with a large number of hard-linked files. The amount of memory required is proportional to the number of inodes in the file system. For large file systems, this can be gigabytes of memory. (For example a 40TB file system with 2.8 billion inodes will consume an additional 5.7 GB memory if this optimization is enabled.) This setting defaults to false.</p>
<dt><i>log_dir</i></p>
<dd>If the <i>log_filename</i> or <i>problem_log_filename</i> relations contains a relative pathname, then the log file will be placed in the directory named by the <i>log_dir</i> relation.</p>
<dt><i>log_dir_fallback</i></p>
<dd>This relation contains an alternate directory that will be used if the directory specified by <i>log_dir</i> is not available or is not writable.</p>
<dt><i>log_dir_wait</i></p>
<dd>If this boolean relation is true, them if the directories specified by <i>log_dir</i> or <i>log_dir_fallback</i> are not available or are not yet writable, e2fsck will save the output in a memory buffer, and a child process will periodically test to see if the log directory has become available after the boot sequence has mounted the requested file system for reading/writing. This implements the functionality provided by <code><a href="/docs/linux/man/8-logsave/">logsave</a></code>(8) for e2fsck log files.</p>
<dt><i>log_filename</i></p>
<dd>This relation specifies the file name where a copy of e2fsck&#8217;s output will be written. If certain problem reports are suppressed using the <i>max_count_problems</i> relation, (or on a per-problem basis using the <i>max_count</i> relation), the full set of problem reports will be written to the log file. The filename may contain various percent-expressions (%D, %T, %N, etc.) which will be expanded so that the file name for the log file can include things like date, time, device name, and other run-time parameters. See the <code>LOGGING</code> section for more details.</p>
<dt><i>max_count_problems</i></p>
<dd>This relation specifies the maximum number of problem reports of a particular type will be printed to stdout before further problem reports of that type are squelched. This can be useful if the console is slow (i.e., connected to a serial port) and so a large amount of output could end up delaying the boot process for a long time (potentially hours).</p>
<dt><i>no_optimize_extents</i></p>
<dd>If this boolean relation is true, do not offer to optimize the extent tree by reducing the tree&#8217;s width or depth. This setting defaults to false.</p>
<dt><i>problem_log_filename</i></p>
<dd>This relation specifies the file name where a log of problem codes found by e2fsck be written. The filename may contain various percent-expressions (%D, %T, %N, etc.) which will be expanded so that the file name for the log file can include things like date, time, device name, and other run-time parameters. See the <code>LOGGING</code> section for more details.</p>
<dt><i>readahead_mem_pct</i></p>
<dd>Use this percentage of memory to try to read in metadata blocks ahead of the main e2fsck thread. This should reduce run times, depending on the speed of the underlying storage and the amount of free memory. There is no default, but see <code>readahead_kb</code> for more details.</p>
<dt><i>readahead_kb</i></p>
<dd>Use this amount of memory to read in metadata blocks ahead of the main checking thread. Setting this value to zero disables readahead entirely. By default, this is set the size of two block groups&#8217; inode tables (typically 4MiB on a regular ext4 file system); if this amount is more than 1/50th of total physical memory, readahead is disabled.</p>
<dt><i>report_features</i></p>
<dd>If this boolean relation is true, e2fsck will print the file system features as part of its verbose reporting (i.e., if the <code>-v</code> option is specified)</p>
<dt><i>report_time</i></p>
<dd>If this boolean relation is true, e2fsck will run as if the options <code>-tt</code> are always specified. This will cause e2fsck to print timing statistics on a pass by pass basis for full file system checks.</p>
<dt><i>report_verbose</i></p>
<dd>If this boolean relation is true, e2fsck will run as if the option <code>-v</code> is always specified. This will cause e2fsck to print some additional information at the end of each full file system check.</dl>
<h2>THE [defaults] STANZA</h2>
<p>The following relations are defined in the <i>[defaults]</i> stanza.</p>
<dl>
<dt><i>undo_dir</i></p>
<dd>This relation specifies the directory where the undo file should be stored. It can be overridden via the <code>E2FSPROGS_UNDO_DIR</code> environment variable. If the directory location is set to the value <i>none</i>, <code>e2fsck</code> will not create an undo file.</dl>
<h2>THE [problems] STANZA</h2>
<p>Each tag in the <i>[problems]</i> stanza names a problem code specified with a leading &quot;0x&quot; followed by six hex digits. The value of the tag is a subsection where the relations in that subsection override the default treatment of that particular problem code. </p>
<p> Note that inappropriate settings in this stanza may cause <code>e2fsck</code> to behave incorrectly, or even crash. Most system administrators should not be making changes to this section without referring to source code. </p>
<p> Within each problem code&#8217;s subsection, the following tags may be used:</p>
<dl>
<dt><i>description</i></p>
<dd>This relation allows the message which is printed when this file system inconsistency is detected to be overridden.</p>
<dt><i>preen_ok</i></p>
<dd>This boolean relation overrides the default behavior controlling whether this file system problem should be automatically fixed when <code>e2fsck</code> is running in preen mode.</p>
<dt><i>max_count</i></p>
<dd>This integer relation overrides the <i>max_count_problems</i> parameter (set in the options section) for this particular problem.</p>
<dt><i>no_ok</i></p>
<dd>This boolean relation overrides the default behavior determining whether or not the file system will be marked as inconsistent if the user declines to fix the reported problem.</p>
<dt><i>no_default</i></p>
<dd>This boolean relation overrides whether the default answer for this problem (or question) should be &quot;no&quot;.</p>
<dt><i>preen_nomessage</i></p>
<dd>This boolean relation overrides the default behavior controlling whether or not the description for this file system problem should be suppressed when <code>e2fsck</code> is running in preen mode.</p>
<dt><i>no_nomsg</i></p>
<dd>This boolean relation overrides the default behavior controlling whether or not the description for this file system problem should be suppressed when a problem forced not to be fixed, either because <code>e2fsck</code> is run with the <code>-n</code> option or because the <i>force_no</i> flag has been set for the problem.</p>
<dt><i>force_no</i></p>
<dd>This boolean option, if set to true, forces a problem to never be fixed. That is, it will be as if the user problem responds &#8216;no&#8217; to the question of &#8216;should this problem be fixed?&#8217;. The <i>force_no</i> option even overrides the <code>-y</code> option given on the command-line (just for the specific problem, of course).</p>
<dt><i>not_a_fix</i></p>
<dd>This boolean option, it set to true, marks the problem as one where if the user gives permission to make the requested change, it does not mean that the file system had a problem which has since been fixed. This is used for requests to optimize the file system&#8217;s data structure, such as pruning an extent tree.</dl>
<h2>THE [scratch_files] STANZA</h2>
<p>The following relations are defined in the <i>[scratch_files]</i> stanza.</p>
<dl>
<dt><i>directory</i></p>
<dd>If the directory named by this relation exists and is writeable, then e2fsck will attempt to use this directory to store scratch files instead of using in-memory data structures.</p>
<dt><i>numdirs_threshold</i></p>
<dd>If this relation is set, then in-memory data structures will be used if the number of directories in the file system are fewer than amount specified.</p>
<dt><i>dirinfo</i></p>
<dd>This relation controls whether or not the scratch file directory is used instead of an in-memory data structure for directory information. It defaults to true.</p>
<dt><i>icount</i></p>
<dd>This relation controls whether or not the scratch file directory is used instead of an in-memory data structure when tracking inode counts. It defaults to true.</dl>
<h2>Logging</h2>
<p>E2fsck has the facility to save the information from an e2fsck run in a directory so that a system administrator can review its output at their leisure. This allows information captured during the automatic e2fsck preen run, as well as a manually started e2fsck run, to be saved for posterity. This facility is controlled by the <i>log_filename</i>, <i>log_dir</i>, <i>log_dir_fallback</i>, and <i>log_dir_wait</i> relations in the <i>[options]</i> stanza. </p>
<p> The filename in <i>log_filename</i> may contain the following percent-expressions that will be expanded as follows.</p>
<dl>
<dt><code>%d</code></p>
<dd>The current day of the month</p>
<dt><code>%D</code></p>
<dd>The current date; this is a equivalent of <code>%Y%m%d</code></p>
<dt><code>%h</code></p>
<dd>The hostname of the system.</p>
<dt><code>%H</code></p>
<dd>The current hour in 24-hour format (00..23)</p>
<dt><code>%m</code></p>
<dd>The current month as a two-digit number (01..12)</p>
<dt><code>%M</code></p>
<dd>The current minute (00..59)</p>
<dt><code>%N</code></p>
<dd>The name of the block device containing the file system, with any directory pathname stripped off.</p>
<dt><code>%p</code></p>
<dd>The pid of the e2fsck process</p>
<dt><code>%s</code></p>
<dd>The current time expressed as the number of seconds since 1970-01-01 00:00:00 UTC</p>
<dt><code>%S</code></p>
<dd>The current second (00..59)</p>
<dt><code>%T</code></p>
<dd>The current time; this is equivalent of <code>%H%M%S</code></p>
<dt><code>%u</code></p>
<dd>The name of the user running e2fsck.</p>
<dt><code>%U</code></p>
<dd>This percent expression does not expand to anything, but it signals that any following date or time expressions should be expressed in UTC time instead of the local timezone.</p>
<dt><code>%y</code></p>
<dd>The last two digits of the current year (00..99)</p>
<dt><code>%Y</code></p>
<dd>The current year (i.e., 2012).</dl>
<h2>Examples</h2>
<p>The following recipe will prevent e2fsck from aborting during the boot process when a file system contains orphaned files. (Of course, this is not always a good idea, since critical files that are needed for the security of the system could potentially end up in lost+found, and starting the system without first having a system administrator check things out may be dangerous.) [options]</p>
<p>max_count_problems = 16</p>
<p>log_dir = /var/log/e2fsck</p>
<p>log_filename = e2fsck-%N.%h.INFO.%D-%T</p>
<p>log_dir_wait = true<br />
 The following recipe will cause an e2fsck logfile to be written to the directory /var/log/e2fsck, with a filename that contains the device name, the hostname of the system, the date, and time: e.g., &quot;e2fsck-sda3.server.INFO.20120314-112142&quot;. If the directory containing /var/log is located on the root file system which is initially mounted read-only, then the output will be saved in memory and written out once the root file system has been remounted read/write. To avoid too much detail from being written to the serial console (which could potentially slow down the boot sequence), only print no more than 16 instances of each type of file system corruption. </p>
<pre><code>[options]

max_count_problems = 16

log_dir = /var/log/e2fsck

log_filename = e2fsck-%N.%h.INFO.%D-%T

log_dir_wait = true
</code></pre>
<h2>Files</h2>
<dl>
<dt><i>/etc/e2fsck.conf</i></p>
<dd>The configuration file for <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) </p>
