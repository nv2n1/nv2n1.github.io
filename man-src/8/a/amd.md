---
title: "amd(8)"
name: "amd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amd/"
description: "amd – automatically mount file systems"
---

<p>amd &#8211; automatically mount file systems</p>
<h2>Synopsis</h2>
<p><code>amd</code> <code>-H</code><br />
 <code>amd</code> [ <code>-F</code><i> conf_file</i> ]<br />
 <code>amd</code> [ <code>-nprvHS</code> ] [ <code>-a</code><i> mount_point</i> ] [ <code>-c</code><i> duration</i> ] [ <code>-d</code><i> domain</i> ] [ <code>-k</code><i> kernel-arch</i> ] [ <code>-l</code><i> logfile</i> ] [ <code>-o</code><i> op_sys_ver</i> ] [ <code>-t</code><i> interval.interval</i> ] [ <code>-w</code><i> interval</i> ] [ <code>-x</code><i> log-option</i> ] [ <code>-y</code><i> YP-domain</i> ] [ <code>-A</code><i> arch</i> ] [ <code>-C</code><i> cluster-name</i> ] [ <code>-D</code><i> option</i> ] [ <code>-F</code><i> conf_file</i> ] [ <code>-O</code><i> op_sys_name</i> ] [ <code>-T</code><i> tag</i> ] [ <i>directory</i> <i>mapname</i> [<i> -map-options </i>] ] &#8230;</p>
<h2>Description</h2>
<p><code>Amd</code> is a daemon that automatically mounts filesystems whenever a file or directory within that filesystem is accessed. Filesystems are automatically unmounted when they appear to have become quiescent. </p>
<p> <code>Amd</code> operates by attaching itself as an <font SIZE="-1">NFS</font> server to each of the specified <i>directories</i><code>.</code> Lookups within the specified directories are handled by <code>amd</code>, which uses the map defined by <i>mapname</i> to determine how to resolve the lookup. Generally, this will be a host name, some filesystem information and some mount options for the given filesystem. </p>
<p> In the first form depicted above, <code>amd</code> will print a short help string. In the second form, if no options are specified, or the <code>-F</code> is used, <code>amd</code> will read configuration parameters from the file <i>conf_file</i> which defaults to <code>/etc/amd.conf</code>. The last form is described below.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code><i> temporary-directory</i></p>
<dd>Specify an alternative location for the real mount points. The default is <code>/a</code>. </p>
<dt><code>-c</code><i> duration</i></p>
<dd>Specify a <i>duration</i>, in seconds, that a looked up name remains cached when not in use. The default is 5 minutes. </p>
<dt><code>-d</code><i> domain</i></p>
<dd>Specify the local domain name. If this option is not given the domain name is determined from the hostname. </p>
<dt><code>-k</code><i> kernel-arch</i></p>
<dd>Specifies the kernel architecture. This is used solely to set the ${karch} selector. </p>
<dt><code>-l</code><i> logfile</i></p>
<dd>Specify a logfile in which to record mount and unmount events. If <i>logfile</i> is the string <code>syslog</code> then the log messages will be sent to the system log daemon by <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3). The default syslog facility used is LOG_DAEMON. If you wish to change it, append its name to the log file name, delimited by a single colon. For example, if <i>logfile</i> is the string <code>syslog:local7</code> then <code>Amd</code> will log messages via <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3) using the LOG_LOCAL7 facility (if it exists on the system). </p>
<dt><code>-n</code></p>
<dd>Normalize hostnames. The name refereed to by ${rhost} is normalized relative to the host database before being used. The effect is to translate aliases into &#8220;official&#8221; names. </p>
<dt><code>-o</code><i> op_sys_ver</i></p>
<dd>Override the compiled-in version number of the operating system. Useful when the built in version is not desired for backward compatibility reasons. For example, if the build in version is &#8220;2.5.1&#8221;, you can override it to &#8220;5.5.1&#8221;, and use older maps that were written with the latter in mind. </p>
<dt><code>-p</code></p>
<dd>Print PID. Outputs the process-id of <code>amd</code> to standard output where it can be saved into a file. </p>
<dt><code>-r</code></p>
<dd>Restart existing mounts. <code>Amd</code> will scan the mount file table to determine which filesystems are currently mounted. Whenever one of these would have been auto-mounted, <code>amd</code> <i>inherits</i> it. </p>
<dt><code>-t</code><i> timeout.retransmit</i></p>
<dd>Specify the NFS timeout <i>interval</i>, in tenths of a second, between NFS/RPC retries (for UDP only). The default is 0.8 seconds. The second value alters the retransmit counter, which defaults to 11 retransmissions. Both of these values are used by the kernel to communicate with amd. Useful defaults are supplied if either or both values are missing. </p>
<p> Amd relies on the kernel RPC retransmit mechanism to trigger mount retries. The values of these parameters change the overall retry interval. Too long an interval gives poor interactive response; too short an interval causes excessive retries. </p>
<dt><code>-v</code></p>
<dd>Version. Displays version and configuration information on standard error. </p>
<dt><code>-w</code><i> interval</i></p>
<dd>Specify an <i>interval</i>, in seconds, between attempts to dismount filesystems that have exceeded their cached times. The default is 2 minutes. </p>
<dt><code>-x</code><i> options</i></p>
<dd>Specify run-time logging options. The options are a comma separated list chosen from: fatal, error, user, warn, info, map, stats, defaults, and all. Note that &quot;fatal&quot; and &quot;error&quot; are mandatory and cannot be turned off. </p>
<dt><code>-y</code><i> domain</i></p>
<dd>Specify an alternative NIS domain from which to fetch the NIS maps. The default is the system domain name. This option is ignored if NIS support is not available. </p>
<dt><code>-A</code><i> arch</i></p>
<dd>Specifies the OS architecture. This is used solely to set the ${arch} selector. </p>
<dt><code>-C</code><i> cluster-name</i></p>
<dd>Specify an alternative HP-UX cluster name to use. </p>
<dt><code>-D</code><i> option</i></p>
<dd>Select from a variety of debug options. Prefixing an option with the strings <code>no</code> reverses the effect of that option. Options are cumulative. The most useful option is <code>all</code>. Since <i>-D</i> is only used for debugging other options are not documented here: the current supported set of options is listed by the -v option and a fuller description is available in the program source. </p>
<dt><code>-F</code><i> conf_file</i></p>
<dd>Specify an amd configuration file to use. See <code><a href="/docs/linux/man/5-amd-conf/">amd.conf</a></code>(5) for description of this file&#8217;s format. This configuration file is used to specify any options in lieu of typing many of them on the command line. The <i>amd.conf</i> file includes directives for every command line option amd has, and many more that are only available via the configuration file facility. The configuration file specified by this option is processed after all other options had been processed, regardless of the actual location of this option on the command line. </p>
<dt><code>-H</code></p>
<dd>Print help and usage string. </p>
<dt><code>-O</code><i> op_sys_name</i></p>
<dd>Override the compiled-in name of the operating system. Useful when the built in name is not desired for backward compatibility reasons. For example, if the build in name is &#8220;sunos5&#8221;, you can override it to &#8220;sos5&#8221;, and use older maps which were written with the latter in mind. </p>
<dt><code>-S</code></p>
<dd>Do not lock the running executable pages of amd into memory. To improve amd&#8217;s performance, systems that support the <code><a href="/docs/linux/man/3-plock/">plock</a></code>(3) call, could lock the amd process into memory. This way there is less chance the operating system will schedule, page out, and swap the amd process as needed. This tends improves amd&#8217;s performance, at the cost of reserving the memory used by the amd process (making it unavailable for other processes). If this behavior is not desired, use the <code>-S</code> option. </p>
<dt><code>-T</code><i> tag</i></p>
<dd>Specify a tag to use with <code><a href="/docs/linux/man/5-amd-conf/">amd.conf</a></code>(5). All map entries tagged with <i>tag</i> will be processed. Map entries that are not tagged are always processed. Map entries that are tagged with a tag other than <i>tag</i> will not be processed. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/a</code></p>
<dd>directory under which filesystems are dynamically mounted</p>
<dt><code>/etc/amd.conf</code></p>
<dd>default configuration file</dl>
<h2>Caveats</h2>
<p>Some care may be required when creating a mount map. </p>
<p> Symbolic links on an NFS filesystem can be incredibly inefficient. In most implementations of NFS, their interpolations are not cached by the kernel and each time a symlink is encountered during a <i>lookuppn</i> translation it costs an RPC call to the NFS server. It would appear that a large improvement in real-time performance could be gained by adding a cache somewhere. Replacing symlinks with a suitable incarnation of the auto-mounter results in a large real-time speedup, but also causes a large number of process context switches. </p>
<p> A weird imagination is most useful to gain full advantage of all the features.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amq/">amq</a></code>(8), <code><a href="/docs/linux/man/1-domainname/">domainname</a></code>(1), <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). <code><a href="/docs/linux/man/5-amd-conf/">amd.conf</a></code>(5), <code><a href="/docs/linux/man/5-mtab/">mtab</a></code>(5), <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), </p>
<p> &#8220;am-utils&#8221; <code><a href="/docs/linux/man/1-info/">info</a></code>(1) entry. </p>
<p> <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). </p>
<p> <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i> </p>
<p> <i>Amd &#8211; The 4.4 BSD Automounter</i></p>
<h2>Authors</h2>
<p>Jan-Simon Pendry &lt;jsp [at] doc.ic.ac.uk&gt;, Department of Computing, Imperial College, London, UK. </p>
<p> Erez Zadok &lt;ezk [at] cs.sunysb.edu&gt;, Computer Science Department, Stony Brook University, Stony Brook, New York, USA. </p>
<p> Other authors and contributors to am-utils are listed in the <code>AUTHORS</code> file distributed with am-utils.</p>
