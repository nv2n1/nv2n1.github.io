---
title: "lxc-unshare(1)"
name: "lxc-unshare"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-unshare/"
description: "lxc-unshare – Run a task in a new set of namespaces."
---

<h2>NAME</h2>
<p> lxc-unshare &#8211; Run a task in a new set of namespaces.</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-unshare</code> {-s <i>namespaces</i>} [-u <i>user</i>] [-H <i>hostname</i>] [-i <i>ifname</i>] [-d] [-M] {command}</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-unshare</code> can be used to run a task in a cloned set of namespaces. This command is mainly provided for testing purposes. Despite its name, it always uses clone rather than unshare to create the new task with fresh namespaces. Apart from testing kernel regressions this should make no difference.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s </code><i>namespaces</i></p>
<dd> Specify the namespaces to attach to, as a pipe-separated list, e.g. <i>NETWORK|IPC</i>. Allowed values are <i>MOUNT</i>, <i>PID</i>, <i>UTSNAME</i>, <i>IPC</i>, <i>USER </i>and <i>NETWORK</i>. This allows one to change the context of the process to e.g. the network namespace of the container while retaining the other namespaces as those of the host. (The pipe symbol needs to be escaped, e.g. <i>MOUNT\|PID</i> or quoted, e.g. <i>&quot;MOUNT|PID&quot;</i>.)</p>
<dt><code>-u </code><i>user</i></p>
<dd> Specify a userid which the new task should become.</p>
<dt><code>-H </code><i>hostname</i></p>
<dd> Set the hostname in the new container. Only allowed if the UTSNAME namespace is set.</p>
<dt><code>-i </code><i>interfacename</i></p>
<dd> Move the named interface into the container. Only allowed if the NETWORK namespace is set. You may specify this argument multiple times to move multiple interfaces into container.</p>
<dt><code>-d</code></p>
<dd> Daemonize (do not wait for the container to exit before exiting)</p>
<dt><code>-M</code></p>
<dd> Mount default filesystems (/proc /dev/shm and /dev/mqueue) in the container. Only allowed if MOUNT namespace is set.</dl>
<h2>EXAMPLES</h2>
<p> To spawn a new shell with its own UTS (hostname) namespace, </p>
<pre>
          lxc-unshare -s UTSNAME /bin/bash
        
</pre>
<p> If the hostname is changed in that shell, the change will not be reflected on the host. </p>
<p> To spawn a shell in a new network, pid, and mount namespace, </p>
<pre>
          lxc-unshare -s &quot;NETWORK|PID|MOUNT&quot; /bin/bash
        
</pre>
<p> The resulting shell will have pid 1 and will see no network interfaces. After re-mounting /proc in that shell, </p>
<pre>
          mount -t proc proc /proc
        
</pre>
<p> ps output will show there are no other processes in the namespace. </p>
<p> To spawn a shell in a new network, pid, mount, and hostname namespace. </p>
<pre>
          lxc-unshare -s &quot;NETWORK|PID|MOUNT|UTSNAME&quot; -M -H slave -i veth1 /bin/bash
        
</pre>
<p> The resulting shell will have pid 1 and will see two network interfaces (lo and veth1). The hostname will be &quot;slave&quot; and /proc will have been remounted. ps output will show there are no other processes in the namespace.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
<h2>Index</h2>
