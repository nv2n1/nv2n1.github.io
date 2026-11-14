---
title: "fuser(1)"
name: "fuser"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fuser/"
description: "fuser – identify processes using files or sockets"
---

<h2 class="name">NAME</h2>
<p> fuser &#8211; identify processes using files or sockets </p>
<h2>SYNOPSIS</h2>
<p> <code>fuser</code> [<code>-fuv</code>] [<code>-a</code>|<code>-s</code>] [<code>-4</code>|<code>-6</code>] [<code>-c</code>|<code>-m</code>|<code>-n</code> <i>space</i>] [<code>&nbsp;-k</code> [<code>-i</code>] [<code>-M</code>] [<code>-w</code>] [<code>&#8211;</code><i>SIGNAL</i>] ] <i>name</i> &#8230;<br />
 <code>fuser -l</code><br />
 <code>fuser -V</code></p>
<h2>DESCRIPTION</h2>
<p> <code>fuser</code> displays the PIDs of processes using the specified files or file systems. In the default display mode, each file name is followed by a letter denoting the type of access: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c</code></p>
<dd> current directory.</p>
<dt><code>e</code></p>
<dd> executable being run.</p>
<dt><code>f</code></p>
<dd> open file. <code>f</code> is omitted in default display mode.</p>
<dt><code>F</code></p>
<dd> open file for writing. <code>F</code> is omitted in default display mode.</p>
<dt><code>r</code></p>
<dd> root directory.</p>
<dt><code>m</code></p>
<dd> mmap&#8217;ed file or shared library.</p>
<dt><code>.</code></p>
<dd> Placeholder, omitted in default display mode.</dl>
</dl>
<p> <code>fuser</code> returns a non-zero return code if none of the specified files is accessed or in case of a fatal error. If at least one access has been found, <code>fuser</code> returns zero. </p>
<p> In order to look up processes using TCP and UDP sockets, the corresponding name space has to be selected with the <code>-n</code> option. By default <code>fuser</code> will look in both IPv6 and IPv4 sockets. To change the default behavior, use the <code>-4</code> and <code>-6</code> options. The socket(s) can be specified by the local and remote port, and the remote address. All fields are optional, but commas in front of missing fields must be present: </p>
<p> [<i>lcl_port</i>][,[<i>rmt_host</i>][,[<i>rmt_port</i>]]] </p>
<p> Either symbolic or numeric values can be used for IP addresses and port numbers. </p>
<p> <code>fuser</code> outputs only the PIDs to stdout, everything else is sent to stderr.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> Show all files specified on the command line. By default, only files that are accessed by at least one process are shown.</p>
<dt><code>-c</code></p>
<dd> Same as <code>-m</code> option, used for POSIX compatibility.</p>
<dt><code>-f</code></p>
<dd> Silently ignored, used for POSIX compatibility.</p>
<dt><code>-k</code>, &#8211;kill</p>
<dd> Kill processes accessing the file. Unless changed with <code>&#8211;</code><i>SIGNAL/</i>, SIGKILL is sent. An <code>fuser</code> process never kills itself, but may kill other <code>fuser</code> processes. The effective user ID of the process executing <code>fuser</code> is set to its real user ID before attempting to kill.</p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask the user for confirmation before killing a process. This option is silently ignored if <code>-k</code> is not present too.</p>
<dt><code>-I</code>, <code>&#8211;inode</code></p>
<dd> For the name space <code>file</code> let all comparisons be based on the inodes of the specified file(s) and never on the file names even on network based file systems.</p>
<dt><code>-l</code>, <code>&#8211;list-signals</code></p>
<dd> List all known signal names.</p>
<dt><code>-m</code><i> NAME</i>, <code>&#8211;mount </code><i>NAME</i></p>
<dd> <i>NAME</i> specifies a file on a mounted file system or a block device that is mounted. All processes accessing files on that file system are listed. If a directory is specified, it is automatically changed to <i>NAME</i>/ to use any file system that might be mounted on that directory.</p>
<dt><code>-M</code>, <code>&#8211;ismountpoint</code></p>
<dd> Request will be fulfilled only if <i>NAME</i> specifies a mountpoint. This is an invaluable seat belt which prevents you from killing the machine if <i>NAME</i> happens to not be a filesystem.</p>
<dt><code>-w</code></p>
<dd> Kill only processes which have write access. This option is silently ignored if <code>-k</code> is not present too.</p>
<dt><code>-n</code><i> NAMESPACE</i>, <code>&#8211;namespace </code><i>NAMESPACE</i></p>
<dd> Select a different name space. The name spaces <code>file</code> (file names, the default), <code>udp</code> (local UDP ports), and <code>tcp</code> (local TCP ports) are supported. For ports, either the port number or the symbolic name can be specified. If there is no ambiguity, the shortcut notation <i>name</i><code>/</code><i>space</i> (e.g., <i>80</i><code>/</code><i>tcp</i>) can be used.</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> Silent operation. <code>-u</code> and <code>-v</code> are ignored in this mode. <code>-a</code> must not be used with <code>-s</code>.</p>
<dt><code>&#8211;</code><i>SIGNAL</i></p>
<dd> Use the specified signal instead of SIGKILL when killing processes. Signals can be specified either by name (e.g., <code>-HUP</code>) or by number (e.g., <code>-1</code>). This option is silently ignored if the <code>-k</code> option is not used.</p>
<dt><code>-u</code>, <code>&#8211;user</code></p>
<dd> Append the user name of the process owner to each PID.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode. Processes are shown in a <code>ps</code>-like style. The fields PID, USER and COMMAND are similar to <code>ps</code>. ACCESS shows how the process accesses the file. Verbose mode will also show when a particular file is being accessed as a mount point, knfs export or swap file. In this case <code>kernel</code> is shown instead of the PID.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>-4</code>, <code>&#8211;ipv4</code></p>
<dd> Search only for IPv4 sockets. This option must not be used with the <code>-6</code> option and only has an effect with the tcp and udp namespaces.</p>
<dt><code>-6</code>, <code>&#8211;ipv6</code></p>
<dd> Search only for IPv6 sockets. This option must not be used with the <code>-4</code> option and only has an effect with the tcp and udp namespaces.</p>
<dt><code>&#8211;</code></p>
<dd> Reset all options and set the signal back to SIGKILL.</dl>
<h2>FILES</h2>
<dl>
<dt>/proc</p>
<dd> location of the proc file system</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>fuser -km /home</code></p>
<dd> kills all processes accessing the file system /home in any way.</p>
<dt><code>if fuser -s /dev/ttyS1; then :; else </code><i>command</i><code>; fi</code></p>
<dd> invokes <i>command</i> if no other process is using /dev/ttyS1.</p>
<dt><code>fuser telnet/tcp</code></p>
<dd> shows all processes at the (local) TELNET port.</dl>
<h2>RESTRICTIONS</h2>
<p> Processes accessing the same file or file system several times in the same way are only shown once. </p>
<p> If the same object is specified several times on the command line, some of those entries may be ignored. </p>
<p> <code>fuser</code> may only be able to gather partial information unless run with privileges. As a consequence, files opened by processes belonging to other users may not be listed and executables may be classified as mapped only. </p>
<p> <code>fuser</code> cannot report on any processes that it doesn&#8217;t have permission to look at the file descriptor table for. The most common time this problem occurs is when looking for TCP or UDP sockets when running <code>fuser</code> as a non-root user. In this case <code>fuser</code> will report no access. </p>
<p> Installing <code>fuser</code> SUID root will avoid problems associated with partial information, but may be undesirable for security and privacy reasons. </p>
<p> <code>udp</code> and <code>tcp</code> name spaces, and UNIX domain sockets can&#8217;t be searched with kernels older than 1.3.78. </p>
<p> Accesses by the kernel are only shown with the <code>-v</code> option. </p>
<p> The <code>-k</code> option only works on processes. If the user is the kernel, <code>fuser</code> will print an advice, but take no action beyond that.</p>
<h2>BUGS</h2>
<p> <code>fuser -m /dev/sgX</code> will show (or kill with the <code>-k</code> flag) all processes, even if you don&#8217;t have that device configured. There may be other devices it does this for too. </p>
<p> The mount <code>-m</code> option will match any file within the same device as the specified file, use the <code>-M</code> option as well if you mean to specify only the mount point.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/1-killall/">killall</a></code>(1), <code><a href="/docs/linux/man/8-lsof/">lsof</a></code>(8), <code><a href="/docs/linux/man/1-pkill/">pkill</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2). </p>
<h2>Index</h2>
