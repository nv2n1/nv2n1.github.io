---
title: "hlfsd(8)"
name: "hlfsd"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hlfsd/"
description: "hlfsd – home-link file system daemon"
---

<p>hlfsd &#8211; home-link file system daemon</p>
<h2>Synopsis</h2>
<p><code>hlfsd</code> [ <code>-fhnpvC</code> ] [ <code>-a</code><i> alt_dir</i> ] [ <code>-c</code><i> cache-interval</i> ] [ <code>-g</code><i> group</i> ] [ <code>-i</code><i> reload-interval</i> ] [ <code>-l</code><i> logfile</i> ] [ <code>-o</code><i> mount-options</i> ] [ <code>-x</code><i> log-options</i> ] [ <code>-D</code><i> debug-options</i> ] [ <code>-P</code><i> password-file</i> ] [ <i>linkname</i> [<i> subdir </i>] ]</p>
<h2>Description</h2>
<p><code>Hlfsd</code> is a daemon which implements a filesystem containing a symbolic link to subdirectory within a user&#8217;s home directory, depending on the user which accessed that link. It was primarily designed to redirect incoming mail to users&#8217; home directories, so that it can read from anywhere. </p>
<p> <code>Hlfsd</code> operates by mounting itself as an <font SIZE="-1">NFS</font> server for the directory containing <i>linkname</i>, which defaults to <code>/hlfs/home</code>. Lookups within that directory are handled by <code>hlfsd</code>, which uses the password map to determine how to resolve the lookup. The directory will be created if it doesn&#8217;t already exist. The symbolic link will be to the accessing user&#8217;s home directory, with <i>subdir</i> appended to it. If not specified, <i>subdir</i> defaults to <code>.hlfsdir</code>. This directory will also be created if it does not already exist. </p>
<p> A SIGTERM sent to <code>hlfsd</code> will cause it to shutdown. A SIGHUP will flush the internal caches, and reload the password map. It will also close and reopen the log file, to enable the original log file to be removed or rotated. A SIGUSR1 will cause it to dump its internal table of user IDs and home directories to the file <code>/usr/tmp/hlfsd.dump.XXXXXX</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code><i> alt_dir</i></p>
<dd>Alternate directory. The name of the directory to which the symbolic link returned by <code>hlfsd</code> will point, if it cannot access the home directory of the user. This defaults to <code>/var/hlfs</code>. This directory will be created if it doesn&#8217;t exist. It is expected that either users will read these files, or the system administrators will run a script to resend this &quot;lost mail&quot; to its owner.</p>
<dt><code>-c</code><i> cache-interval</i></p>
<dd>Caching interval. <code>Hlfsd</code> will cache the validity of home directories for this interval, in seconds. Entries which have been verified within the last <i>cache-interval</i> seconds will not be verified again, since the operation could be expensive, and the entries are most likely still valid. After the interval has expired, <code>hlfsd</code> will re-verify the validity of the user&#8217;s home directory, and reset the cache time-counter. The default value for <i>cache-interval</i> is 300 seconds (5 minutes).</p>
<dt><code>-f</code></p>
<dd>Force fast startup. This option tells <code>hlfsd</code> to skip startup-time consistency checks such as existence of mount directory, alternate spool directory, symlink to be hidden under the mount directory, their permissions and validity.</p>
<dt><code>-g</code><i> group</i></p>
<dd>Set the special group HLFS_GID to <i>group</i>. Programs such as <code>from</code> or <code>comsat</code>, which access the mailboxes of other users) must be setgid HLFS_GID to work properly. The default group is &quot;hlfs&quot;. If no group is provided, and there is no group &quot;hlfs&quot;, this feature is disabled.</p>
<dt><code>-h</code></p>
<dd>Help. Print a brief help message, and exit.</p>
<dt><code>-i</code><i> reload-interval</i></p>
<dd>Map-reloading interval. Each <i>reload-interval</i> seconds, <code>hlfsd</code> will reload the password map. <code>Hlfsd</code> needs the password map for the UIDs and home directory pathnames. <code>Hlfsd</code> schedules a SIGALRM to reload the password maps. A SIGHUP sent to <code>hlfsd</code> will force it to reload the maps immediately. The default value for <i>reload-interval</i> is 900 seconds (15 minutes.)</p>
<dt><code>-l</code><i> logfile</i></p>
<dd>Specify a log file to which <code>hlfsd</code> will record events. If <i>logfile</i> is the string <code>syslog</code> then the log messages will be sent to the system log daemon by <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3), using the LOG_DAEMON facility. This is also the default.</p>
<dt><code>-n</code></p>
<dd>No verify. <code>Hlfsd</code> will not verify the validity of the symbolic link it will be returning, or that the user&#8217;s home directory contains sufficient disk-space for spooling. This can speed up <code>hlfsd</code> at the cost of possibly returning symbolic links to home directories which are not currently accessible or are full. By default, <code>hlfsd</code> validates the symbolic-link in the background. The <code>-n</code> option overrides the meaning of the <code>-c</code> option, since no caching is necessary.</p>
<dt><code>-o</code><i> mount-options</i></p>
<dd>Mount options. Mount options which <code>hlfsd</code> will use to mount itself on top of <i>dirname.</i> By default, <i>mount-options</i> is set to &quot;ro&quot;. If the system supports symbolic-link caching, default options are set to &quot;ro,nocache&quot;.</p>
<dt><code>-p</code></p>
<dd>Print PID. Outputs the process-id of <code>hlfsd</code> to standard output where it can be saved into a file.</p>
<dt><code>-v</code></p>
<dd>Version. Displays version information to standard error.</p>
<dt><code>-x</code><i> log-options</i></p>
<dd>Specify run-time logging options. The options are a comma separated list chosen from: fatal, error, user, warn, info, map, stats, all.</p>
<dt><code>-C</code></p>
<dd>Force <code>hlfsd</code> to run on systems that cannot turn off the NFS attribute-cache. Use of this option on those systems is discouraged, as it may result in loss or mis-delivery of mail. The option is ignored on systems that can turn off the attribute-cache.</p>
<dt><code>-D</code><i> log-options</i></p>
<dd>Select from a variety of debugging options. Prefixing an option with the string <code>no</code> reverses the effect of that option. Options are cumulative. The most useful option is <code>all</code>. Since this option is only used for debugging other options are not documented here. A fuller description is available in the program source. A SIGUSR1 sent to <code>hlfsd</code> will cause it to dump its internal password map to the file <code>/usr/tmp/hlfsd.dump.XXXXXX</code>.</p>
<dt><code>-P</code><i> password-file</i></p>
<dd>Read the user-name, user-id, and home directory information from the file <i>password-file.</i> Normally, <code>hlfsd</code> will use <i><a href="/docs/linux/man/3-getpwent/">getpwent</a></i>(3) to read the password database. This option allows you to override the default database, and is useful if you want to map users&#8217; mail files to a directory other than their home directory. Only the username, uid, and home-directory fields of the file <i>password-file</i> are read and checked. All other fields are ignored. The file <i>password-file</i> must otherwise be compliant with Unix System 7 colon-delimited format <i><a href="/docs/linux/man/4-passwd/">passwd</a></i>(4).</dl>
<h2>Files</h2>
<dl>
<dt><code>/hlfs</code></p>
<dd>directory under which <code>hlfsd</code> mounts itself and manages the symbolic link <code>home</code>.</p>
<dt><code>.hlfsdir</code></p>
<dd>default sub-directory in the user&#8217;s home directory, to which the <code>home</code> symbolic link returned by <code>hlfsd</code> points.</p>
<dt><code>/var/hlfs</code></p>
<dd>directory to which <code>home</code> symbolic link returned by <code>hlfsd</code> points if it is unable to verify the that user&#8217;s home directory is accessible.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mail/">mail</a>(1),</code> <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/4-mnttab/">mnttab</a></code>(4), <code><a href="/docs/linux/man/4-passwd/">passwd</a></code>(4), <code><a href="/docs/linux/man/5-mtab/">mtab</a></code>(5), <code><a href="/docs/linux/man/8-amd/">amd</a></code>(8), <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8), <code><a href="/docs/linux/man/8-cron/">cron</a>(8),</code> <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8). </p>
<p> <i>HLFSD: Delivering Email to Your $HOME</i>, in <i>Proc. LISA-VII, The 7th Usenix System Administration Conference</i>, November 1993. </p>
<p> &#8220;am-utils&#8221; <code><a href="/docs/linux/man/1-info/">info</a></code>(1) entry. </p>
<p> <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). </p>
<p> <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i></p>
<h2>Authors</h2>
<p>Erez Zadok &lt;ezk [at] cs.sunysb.edu&gt;, Computer Science Department, Stony Brook University, Stony Brook, New York, USA. and Alexander Dupuy &lt;dupuy [at] smarts.com&gt;, System Management ARTS, White Plains, New York, USA. </p>
<p> Other authors and contributors to am-utils are listed in the <code>AUTHORS</code> file distributed with am-utils.</p>
