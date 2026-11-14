---
title: "unshare(1)"
name: "unshare"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unshare/"
description: "unshare – run program in new namespaces"
---

<h2 class="name">NAME</h2>
<p> unshare &#8211; run program in new namespaces </p>
<h2>SYNOPSIS</h2>
<p> <code>unshare</code> [options] [<i>program</i> [<i>arguments</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>unshare</code> command creates new namespaces (as specified by the command-line options described below) and then executes the specified <i>program</i>. If <i>program</i> is not given, then &quot;${SHELL}&quot; is run (default: <i>/bin/sh</i>). </p>
<p> By default, a new namespace persists only as long as it has member processes. A new namespace can be made persistent even when it has no member processes by bind mounting /proc/<i>pid</i>/ns/<i>type</i> files to a filesystem path. A namespace that has been made persistent in this way can subsequently be entered with <code><a href="/docs/linux/man/1-nsenter/">nsenter</a></code>(1) even after the <i>program</i> terminates (except PID namespaces where a permanently running init process is required). Once a persistent namespace is no longer needed, it can be unpersisted by using <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) to remove the bind mount. See the EXAMPLES section for more details. </p>
<p> <code>unshare</code> since util-linux version 2.36 uses <i>/proc/[pid]/ns/pid_for_children</i> and <i>/proc/[pid]/ns/time_for_children</i> files for persistent PID and TIME namespaces. This change requires Linux kernel 4.17 or newer. </p>
<p> The following types of namespaces can be created with <code>unshare</code>: </p>
<p> <code>mount namespace</code></p>
<dl>
<dt>
<dd> Mounting and unmounting filesystems will not affect the rest of the system, except for filesystems which are explicitly marked as shared (with <code>mount &#8211;make-shared</code>; see <i>/proc/self/mountinfo</i> or <code>findmnt -o+PROPAGATION</code> for the <code>shared</code> flags). For further details, see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7). </p>
<p> <code>unshare</code> since util-linux version 2.27 automatically sets propagation to <code>private</code> in a new mount namespace to make sure that the new namespace is really unshared. It&#8217;s possible to disable this feature with option <code>&#8211;propagation unchanged</code>. Note that <code>private</code> is the kernel default.</dl>
<p> <code>UTS namespace</code></p>
<dl>
<dt>
<dd> Setting hostname or domainname will not affect the rest of the system. For further details, see <code><a href="/docs/linux/man/7-uts_namespaces/">uts_namespaces</a></code>(7).</dl>
<p> <code>IPC namespace</code></p>
<dl>
<dt>
<dd> The process will have an independent namespace for POSIX message queues as well as System V message queues, semaphore sets and shared memory segments. For further details, see <code><a href="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></code>(7).</dl>
<p> <code>network namespace</code></p>
<dl>
<dt>
<dd> The process will have independent IPv4 and IPv6 stacks, IP routing tables, firewall rules, the <i>/proc/net</i> and <i>/sys/class/net</i> directory trees, sockets, etc. For further details, see <code><a href="/docs/linux/man/7-network_namespaces/">network_namespaces</a></code>(7).</dl>
<p> <code>PID namespace</code></p>
<dl>
<dt>
<dd> Children will have a distinct set of PID-to-process mappings from their parent. For further details, see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7).</dl>
<p> <code>cgroup namespace</code></p>
<dl>
<dt>
<dd> The process will have a virtualized view of <i>/proc/self/cgroup</i>, and new cgroup mounts will be rooted at the namespace cgroup root. For further details, see <code><a href="/docs/linux/man/7-cgroup_namespaces/">cgroup_namespaces</a></code>(7).</dl>
<p> <code>user namespace</code></p>
<dl>
<dt>
<dd> The process will have a distinct set of UIDs, GIDs and capabilities. For further details, see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</dl>
<p> <code>time namespace</code></p>
<dl>
<dt>
<dd> The process can have a distinct view of <code>CLOCK_MONOTONIC</code> and/or <code>CLOCK_BOOTTIME</code> which can be changed using <i>/proc/self/timens_offsets</i>. For further details, see <code><a href="/docs/linux/man/7-time_namespaces/">time_namespaces</a></code>(7).</dl>
<h2>OPTIONS</h2>
<p> <code>-i</code>, <code>&#8211;ipc</code>[<code>=</code><i>file</i>]</p>
<dl>
<dt>
<dd> Unshare the IPC namespace. If <i>file</i> is specified, then a persistent namespace is created by a bind mount.</dl>
<p> <code>-m</code>, <code>&#8211;mount</code>[<code>=</code><i>file</i>]</p>
<dl>
<dt>
<dd> Unshare the mount namespace. If <i>file</i> is specified, then a persistent namespace is created by a bind mount. Note that <i>file</i> must be located on a mount whose propagation type is not <code>shared</code> (or an error results). Use the command <code>findmnt -o+PROPAGATION</code> when not sure about the current setting. See also the examples below.</dl>
<p> <code>-n</code>, <code>&#8211;net</code>[<code>=</code><i>file</i>]</p>
<dl>
<dt>
<dd> Unshare the network namespace. If <i>file</i> is specified, then a persistent namespace is created by a bind mount.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code>[<code>=</code><i>file</i>]</p>
<dl>
<dt>
<dd> Unshare the PID namespace. If <i>file</i> is specified, then a persistent namespace is created by a bind mount. (Creation of a persistent PID namespace will fail if the <code>&#8211;fork</code> option is not also specified.) </p>
<p> See also the <code>&#8211;fork</code> and <code>&#8211;mount-proc</code> options.</dl>
<p> <code>-u</code>, <code>&#8211;uts</code>[<code>=</code><i>file</i>]</p>
<dl>
<dt>
<dd> Unshare the UTS namespace. If <i>file</i> is specified, then a persistent namespace is created by a bind mount.</dl>
<p> <code>-U</code>, <code>&#8211;user</code>[<code>=</code><i>file</i>]</p>
<dl>
<dt>
<dd> Unshare the user namespace. If <i>file</i> is specified, then a persistent namespace is created by a bind mount.</dl>
<p> <code>-C</code>, <code>&#8211;cgroup</code>[<code>=</code><i>file</i>]</p>
<dl>
<dt>
<dd> Unshare the cgroup namespace. If <i>file</i> is specified, then persistent namespace is created by bind mount.</dl>
<p> <code>-T</code>, <code>&#8211;time</code>[<code>=</code><i>file</i>]</p>
<dl>
<dt>
<dd> Unshare the time namespace. If <i>file</i> is specified, then a persistent namespace is created by a bind mount. The <code>&#8211;monotonic</code> and <code>&#8211;boottime</code> options can be used to specify the corresponding offset in the time namespace.</dl>
<p> <code>-f</code>, <code>&#8211;fork</code></p>
<dl>
<dt>
<dd> Fork the specified <i>program</i> as a child process of <code>unshare</code> rather than running it directly. This is useful when creating a new PID namespace. Note that when <code>unshare</code> is waiting for the child process, then it ignores <code>SIGINT</code> and <code>SIGTERM</code> and does not forward any signals to the child. It is necessary to send signals to the child process.</dl>
<p> <code>&#8211;keep-caps</code></p>
<dl>
<dt>
<dd> When the <code>&#8211;user</code> option is given, ensure that capabilities granted in the user namespace are preserved in the child process.</dl>
<p> <code>&#8211;kill-child</code>[<code>=</code><i>signame</i>]</p>
<dl>
<dt>
<dd> When <code>unshare</code> terminates, have <i>signame</i> be sent to the forked child process. Combined with <code>&#8211;pid</code> this allows for an easy and reliable killing of the entire process tree below <code>unshare</code>. If not given, <i>signame</i> defaults to <code>SIGKILL</code>. This option implies <code>&#8211;fork</code>.</dl>
<p> <code>&#8211;mount-proc</code>[<code>=</code><i>mountpoint</i>]</p>
<dl>
<dt>
<dd> Just before running the program, mount the proc filesystem at <i>mountpoint</i> (default is <i>/proc</i>). This is useful when creating a new PID namespace. It also implies creating a new mount namespace since the <i>/proc</i> mount would otherwise mess up existing programs on the system. The new proc filesystem is explicitly mounted as private (with <code>MS_PRIVATE</code>|<code>MS_REC</code>).</dl>
<p> <code>&#8211;map-user=</code><i>uid|name</i></p>
<dl>
<dt>
<dd> Run the program only after the current effective user ID has been mapped to <i>uid</i>. If this option is specified multiple times, the last occurrence takes precedence. This option implies <code>&#8211;user</code>.</dl>
<p> <code>&#8211;map-group=</code><i>gid|name</i></p>
<dl>
<dt>
<dd> Run the program only after the current effective group ID has been mapped to <i>gid</i>. If this option is specified multiple times, the last occurrence takes precedence. This option implies <code>&#8211;setgroups=deny</code> and <code>&#8211;user</code>.</dl>
<p> <code>-r</code>, <code>&#8211;map-root-user</code></p>
<dl>
<dt>
<dd> Run the program only after the current effective user and group IDs have been mapped to the superuser UID and GID in the newly created user namespace. This makes it possible to conveniently gain capabilities needed to manage various aspects of the newly created namespaces (such as configuring interfaces in the network namespace or mounting filesystems in the mount namespace) even when run unprivileged. As a mere convenience feature, it does not support more sophisticated use cases, such as mapping multiple ranges of UIDs and GIDs. This option implies <code>&#8211;setgroups=deny</code> and <code>&#8211;user</code>. This option is equivalent to <code>&#8211;map-user=0 &#8211;map-group=0</code>.</dl>
<p> <code>-c</code>, <code>&#8211;map-current-user</code></p>
<dl>
<dt>
<dd> Run the program only after the current effective user and group IDs have been mapped to the same UID and GID in the newly created user namespace. This option implies <code>&#8211;setgroups=deny</code> and <code>&#8211;user</code>. This option is equivalent to <code>&#8211;map-user=$(id -ru) &#8211;map-group=$(id -rg)</code>.</dl>
<p> <code>&#8211;propagation private</code>|<code>shared</code>|<code>slave</code>|<code>unchanged</code></p>
<dl>
<dt>
<dd> Recursively set the mount propagation flag in the new mount namespace. The default is to set the propagation to <i>private</i>. It is possible to disable this feature with the argument <code>unchanged</code>. The option is silently ignored when the mount namespace (<code>&#8211;mount</code>) is not requested.</dl>
<p> <code>&#8211;setgroups allow</code>|<code>deny</code></p>
<dl>
<dt>
<dd> Allow or deny the <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) system call in a user namespace. </p>
<p> To be able to call <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2), the calling process must at least have <code>CAP_SETGID</code>. But since Linux 3.19 a further restriction applies: the kernel gives permission to call <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) only after the GID map (<code>/proc/</code><i>pid</i>*/gid_map*) has been set. The GID map is writable by root when <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) is enabled (i.e., <code>allow</code>, the default), and the GID map becomes writable by unprivileged processes when <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) is permanently disabled (with <code>deny</code>).</dl>
<p> <code>-R</code>, <code>&#8211;root=</code><i>dir</i></p>
<dl>
<dt>
<dd> run the command with root directory set to <i>dir</i>.</dl>
<p> <code>-w</code>, <code>&#8211;wd=</code><i>dir</i></p>
<dl>
<dt>
<dd> change working directory to <i>dir</i>.</dl>
<p> <code>-S</code>, <code>&#8211;setuid</code> <i>uid</i></p>
<dl>
<dt>
<dd> Set the user ID which will be used in the entered namespace.</dl>
<p> <code>-G</code>, <code>&#8211;setgid</code> <i>gid</i></p>
<dl>
<dt>
<dd> Set the group ID which will be used in the entered namespace and drop supplementary groups.</dl>
<p> <code>&#8211;monotonic</code> <i>offset</i></p>
<dl>
<dt>
<dd> Set the offset of <code>CLOCK_MONOTONIC</code> which will be used in the entered time namespace. This option requires unsharing a time namespace with <code>&#8211;time</code>.</dl>
<p> <code>&#8211;boottime</code> <i>offset</i></p>
<dl>
<dt>
<dd> Set the offset of <code>CLOCK_BOOTTIME</code> which will be used in the entered time namespace. This option requires unsharing a time namespace with <code>&#8211;time</code>.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>NOTES</h2>
<p> The proc and sysfs filesystems mounting as root in a user namespace have to be restricted so that a less privileged user can not get more access to sensitive files that a more privileged user made unavailable. In short the rule for proc and sysfs is as close to a bind mount as possible.</p>
<h2>EXAMPLES</h2>
<p> The following command creates a PID namespace, using <code>&#8211;fork</code> to ensure that the executed command is performed in a child process that (being the first process in the namespace) has PID 1. The <code>&#8211;mount-proc</code> option ensures that a new mount namespace is also simultaneously created and that a new <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) filesystem is mounted that contains information corresponding to the new PID namespace. When the <code>readlink</code> command terminates, the new namespaces are automatically torn down. </p>
<dl>
<dt>
<dd>
<pre>
# unshare --fork --pid --mount-proc readlink /proc/self
1
</pre>
</dl>
<p> As an unprivileged user, create a new user namespace where the user&#8217;s credentials are mapped to the root IDs inside the namespace: </p>
<dl>
<dt>
<dd>
<pre><code>
$ id - u;
id - g 1000 1000 $ unshare-- user-- map - root - user sh - c ''whoami;
cat / proc / self / uid_map / proc / self / gid_map'' root 0 1000 1 0 1000 1
</code></pre>
</dl>
<p> The first of the following commands creates a new persistent UTS namespace and modifies the hostname as seen in that namespace. The namespace is then entered with <code><a href="/docs/linux/man/1-nsenter/">nsenter</a></code>(1) in order to display the modified hostname; this step demonstrates that the UTS namespace continues to exist even though the namespace had no member processes after the <code>unshare</code> command terminated. The namespace is then destroyed by removing the bind mount. </p>
<dl>
<dt>
<dd>
<pre>
# touch /root/uts-ns
# unshare --uts=/root/uts-ns hostname FOO
# nsenter --uts=/root/uts-ns hostname
FOO
# umount /root/uts-ns
</pre>
</dl>
<p> The following commands establish a persistent mount namespace referenced by the bind mount <i>/root/namespaces/mnt</i>. In order to ensure that the creation of that bind mount succeeds, the parent directory (<i>/root/namespaces</i>) is made a bind mount whose propagation type is not <code>shared</code>. </p>
<dl>
<dt>
<dd>
<pre>
# mount --bind /root/namespaces /root/namespaces
# mount --make-private /root/namespaces
# touch /root/namespaces/mnt
# unshare --mount=/root/namespaces/mnt
</pre>
</dl>
<p> The following commands demonstrate the use of the <code>&#8211;kill-child</code> option when creating a PID namespace, in order to ensure that when <code>unshare</code> is killed, all of the processes within the PID namespace are killed. </p>
<dl>
<dt>
<dd>
#set + m #Don&#8217;t print job status messages<br />
#unshare&#8211; pid&#8211; fork&#8211; mount &#8211; proc&#8211; kill &#8211; child&#8211; bash&#8211; norc &#8211; c &#8221;(sleep 555 &amp;)&amp;&amp;(ps a &amp;)&amp;&amp;sleep 999&#8221; &amp;<br />
[1] 53456<br />
#PID TTY STAT TIME COMMAND<br />
        1 pts /<br />
        3 S +<br />
    0 : 00 sleep 999 3 pts / 3 S + 0 : 00 sleep 555 5 pts / 3 R + 0 : 00 ps a<br />
#ps h &#8211; o &#8216;comm&#8217; $ !#Show that background job is unshare(1)<br />
                                                                      unshare<br />
#kill $ !#Kill unshare(1)<br />
#pidof sleep
</dl>
<p> The <code><a href="/docs/linux/man/1-pidof/">pidof</a></code>(1) command prints no output, because the <code>sleep</code> processes have been killed. More precisely, when the <code>sleep</code> process that has PID 1 in the namespace (i.e., the namespace&#8217;s init process) was killed, this caused all other processes in the namespace to be killed. By contrast, a similar series of commands where the <code>&#8211;kill-child</code> option is not used shows that when <code>unshare</code> terminates, the processes in the PID namespace are not killed: </p>
<dl>
<dt>
<dd>
<pre><code>
#unshare-- pid-- fork-- mount - proc-- bash-- norc - c ''(sleep 555 &amp;)&amp;&amp;(ps a &amp;)&amp;&amp;sleep 999'' &amp;
[1] 53479
#PID TTY STAT TIME COMMAND
        1 pts /
        3 S +
    0 : 00 sleep 999 3 pts / 3 S + 0 : 00 sleep 555 5 pts / 3 R + 0 : 00 ps a
#kill $ !
#pidof sleep
    53482 53480
</code></pre>
</dl>
<p> The following example demonstrates the creation of a time namespace where the boottime clock is set to a point several years in the past: </p>
<dl>
<dt>
<dd>
<pre>
# uptime -p             # Show uptime in initial time namespace
up 21 hours, 30 minutes
# unshare --time --fork --boottime 300000000 uptime -p
up 9 years, 28 weeks, 1 day, 2 hours, 50 minutes
</pre>
</dl>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>unshare</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
