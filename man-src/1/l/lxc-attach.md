---
title: "lxc-attach(1)"
name: "lxc-attach"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-attach/"
description: "lxc-attach – start a process inside a running container."
---

<h2>NAME</h2>
<p> lxc-attach &#8211; start a process inside a running container.</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-attach</code> {-n <i>name</i>} [-a <i>arch</i>] [-e] [-s <i>namespaces</i>] [-R] [&#8211;keep-env] [&#8211;clear-env] [&#8211; <i>command</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-attach</code> runs the specified <i>command</i> inside the container specified by <i>name</i>. The container has to be running already. </p>
<p> If no <i>command</i> is specified, the current default shell of the user running <code>lxc-attach</code> will be looked up inside the container and executed. This will fail if no such user exists inside the container or the container does not have a working nsswitch mechanism.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a, &#8211;arch </code><i>arch</i></p>
<dd> Specify the architecture which the kernel should appear to be running as to the command executed. This option will accept the same settings as the <code>lxc.arch</code> option in container configuration files, see <i><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></i>(5). By default, the current archictecture of the running container will be used.</p>
<dt><code>-e, &#8211;elevated-privileges </code><i>privileges</i></p>
<dd> Do not drop privileges when running <i>command</i> inside the container. If this option is specified, the new process will <i>not</i> be added to the container&#8217;s cgroup(s) and it will not drop its capabilities before executing. </p>
<p> You may specify privileges, in case you do not want to elevate all of them, as a pipe-separated list, e.g. <i>CGROUP|LSM</i>. Allowed values are <i>CGROUP</i>, <i>CAP</i> and <i>LSM</i> representing cgroup, capabilities and restriction privileges respectively. </p>
<p> <i>Warning:</i> This may leak privileges into the container if the command starts subprocesses that remain active after the main process that was attached is terminated. The (re-)starting of daemons inside the container is problematic, especially if the daemon starts a lot of subprocesses such as <code>cron</code> or <code>sshd</code>. <i>Use with great care.</i></p>
<dt><code>-s, &#8211;namespaces </code><i>namespaces</i></p>
<dd> Specify the namespaces to attach to, as a pipe-separated list, e.g. <i>NETWORK|IPC</i>. Allowed values are <i>MOUNT</i>, <i>PID</i>, <i>UTSNAME</i>, <i>IPC</i>, <i>USER </i>and <i>NETWORK</i>. This allows one to change the context of the process to e.g. the network namespace of the container while retaining the other namespaces as those of the host. </p>
<p> <i>Important:</i> This option implies <code>-e</code>.</p>
<dt><code>-R, &#8211;remount-sys-proc</code></p>
<dd> When using <code>-s</code> and the mount namespace is not included, this flag will cause <code>lxc-attach</code> to remount <i>/proc</i> and <i>/sys</i> to reflect the current other namespace contexts. </p>
<p> Please see the <i>Notes</i> section for more details. </p>
<p> This option will be ignored if one tries to attach to the mount namespace anyway.</p>
<dt><code>&#8211;keep-env</code></p>
<dd> Keep the current environment for attached programs. This is the current default behaviour (as of version 0.9), but is is likely to change in the future, since this may leak undesirable information into the container. If you rely on the environment being available for the attached program, please use this option to be future-proof. In addition to current environment variables, container=lxc will be set.</p>
<dt><code>&#8211;clear-env</code></p>
<dd> Clear the environment before attaching, so no undesired environment variables leak into the container. The variable container=lxc will be the only environment with which the attached program starts.</dl>
<h2>COMMON OPTIONS</h2>
<p> These options are common to most of lxc commands.</p>
<dl>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Print a longer usage message than normal.</p>
<dt><code>&#8211;usage</code></p>
<dd> Give the usage message</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> mute on</p>
<dt><code>-P, &#8211;lxcpath=</code><i>PATH</i></p>
<dd> Use an alternate container path. The default is /var/lib/lxc.</p>
<dt><code>-o, &#8211;logfile=</code><i>FILE</i></p>
<dd> Output to an alternate log <i>FILE</i>. The default is no log.</p>
<dt><code>-l, &#8211;logpriority=</code><i>LEVEL</i></p>
<dd> Set log priority to <i>LEVEL</i>. The default log priority is ERROR. Possible values are : FATAL, CRIT, WARN, ERROR, NOTICE, INFO, DEBUG. </p>
<p> Note that this option is setting the priority of the events log in the alternate log file. It do not have effect on the ERROR events log on stderr.</p>
<dt><code>-n, &#8211;name=</code><i>NAME</i></p>
<dd> Use container identifier <i>NAME</i>. The container identifier format is an alphanumeric string.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version number.</dl>
<h2>EXAMPLES</h2>
<p> To spawn a new shell running inside an existing container, use </p>
<pre>
          lxc-attach -n container
        
</pre>
<p> To restart the cron service of a running Debian container, use </p>
<pre>
          lxc-attach -n container -- /etc/init.d/cron restart
        
</pre>
<p> To deactivate the network link eth1 of a running container that does not have the NET_ADMIN capability, use either the <code>-e</code> option to use increased capabilities, assuming the <code>ip</code> tool is installed: </p>
<pre>
          lxc-attach -n container -e -- /sbin/ip link delete eth1
        
</pre>
<p> Or, alternatively, use the <code>-s</code> to use the tools installed on the host outside the container: </p>
<pre>
          lxc-attach -n container -s NETWORK -- /sbin/ip link delete eth1
        
</pre>
<h2>COMPATIBILITY</h2>
<p> Attaching completely (including the pid and mount namespaces) to a container requires a kernel of version 3.8 or higher, or a patched kernel, please see the lxc website for details. <code>lxc-attach</code> will fail in that case if used with an unpatched kernel of version 3.7 and prior. </p>
<p> Nevertheless, it will succeed on an unpatched kernel of version 3.0 or higher if the <code>-s</code> option is used to restrict the namespaces that the process is to be attached to to one or more of <i>NETWORK</i>, <i>IPC</i> and <i>UTSNAME</i>. </p>
<p> Attaching to user namespaces is supported by kernel 3.8 or higher with enabling user namespace.</p>
<h2>NOTES</h2>
<p> The Linux <i>/proc</i> and <i>/sys</i> filesystems contain information about some quantities that are affected by namespaces, such as the directories named after process ids in <i>/proc</i> or the network interface information in <i>/sys/class/net</i>. The namespace of the process mounting the pseudo-filesystems determines what information is shown, <i>not</i> the namespace of the process accessing <i>/proc</i> or <i>/sys</i>. </p>
<p> If one uses the <code>-s</code> option to only attach to the pid namespace of a container, but not its mount namespace (which will contain the <i>/proc</i> of the container and not the host), the contents of <code>/proc</code> will reflect that of the host and not the container. Analogously, the same issue occurs when reading the contents of <i>/sys/class/net</i> and attaching to just the network namespace. </p>
<p> To work around this problem, the <code>-R</code> flag provides the option to remount <i>/proc</i> and <i>/sys</i> in order for them to reflect the network/pid namespace context of the attached process. In order not to interfere with the host&#8217;s actual filesystem, the mount namespace will be unshared (like <code>lxc-unshare</code> does) before this is done, essentially giving the process a new mount namespace, which is identical to the hosts&#8217;s mount namespace except for the <i>/proc</i> and <i>/sys</i> filesystems.</p>
<h2>SECURITY</h2>
<p> The <code>-e</code> and <code>-s</code> options should be used with care, as it may break the isolation of the containers if used improperly.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
<h2>Index</h2>
