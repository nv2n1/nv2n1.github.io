---
title: "lxc(7)"
name: "lxc"
section: "7"
letter: "l"
url: "/docs/linux/man/7-lxc/"
description: "lxc – linux containers"
---

<p>lxc &#8211; linux containers</p>
<h2>Quick Start</h2>
<p>You are in a hurry, and you don&#8217;t want to read this man page. Ok, without warranty, here are the commands to launch a shell inside a container with a predefined configuration template, it may work. <code>/usr/bin/lxc-execute -n foo -f /usr/share/doc/lxc-1.0.11/examples/lxc-macvlan.conf /bin/bash</code></p>
<h2>Overview</h2>
<p>The container technology is actively being pushed into the mainstream linux kernel. It provides the resource management through the control groups aka process containers and resource isolation through the namespaces. </p>
<p> The linux containers, <code>lxc</code>, aims to use these new functionalities to provide a userspace container object which provides full resource isolation and resource control for an applications or a system. </p>
<p> The first objective of this project is to make the life easier for the kernel developers involved in the containers project and especially to continue working on the Checkpoint/Restart new features. The <code>lxc</code> is small enough to easily manage a container with simple command lines and complete enough to be used for other purposes.</p>
<h2>Requirements</h2>
<p>The <code>lxc</code> relies on a set of functionalities provided by the kernel which needs to be active. Depending of the missing functionalities the <code>lxc</code> will work with a restricted number of functionalities or will simply fail. </p>
<p> The following list gives the kernel features to be enabled in the kernel to have the full features container: </p>
<pre> * General setup
 * Control Group support
 -&gt; Namespace cgroup subsystem
 -&gt; Freezer cgroup subsystem
 -&gt; Cpuset support
 -&gt; Simple CPU accounting cgroup subsystem
 -&gt; Resource counters
 -&gt; Memory resource controllers for Control Groups
 * Group CPU scheduler
 -&gt; Basis for grouping tasks (Control Groups)
 * Namespaces support
 -&gt; UTS namespace
 -&gt; IPC namespace
 -&gt; User namespace
 -&gt; Pid namespace
 -&gt; Network namespace
 * Device Drivers
 * Character devices
 -&gt; Support multiple instances of devpts
 * Network device support
 -&gt; MAC-VLAN support
 -&gt; Virtual ethernet pair device
 * Networking
 * Networking options
 -&gt; 802.1d Ethernet Bridging
 * Security options
 -&gt; File POSIX Capabilities</pre>
<p>The kernel version &gt;= 2.6.32 shipped with the distros, will work with <code>lxc</code>, this one will have less functionalities but enough to be interesting. The helper script <code>lxc-checkconfig</code> will give you information about your kernel configuration. </p>
<p> The control group can be mounted anywhere, eg: <code>mount -t cgroup cgroup /cgroup</code>. It is however recommended to use cgmanager, cgroup-lite or systemd to mount the cgroup hierarchy under /sys/fs/cgroup.</p>
<h2>Functional Specification</h2>
<p>A container is an object isolating some resources of the host, for the application or system running in it. </p>
<p> The application / system will be launched inside a container specified by a configuration that is either initially created or passed as parameter of the starting commands. </p>
<p> How to run an application in a container ? </p>
<p> Before running an application, you should know what are the resources you want to isolate. The default configuration is to isolate the pids, the sysv ipc and the mount points. If you want to run a simple shell inside a container, a basic configuration is needed, especially if you want to share the rootfs. If you want to run an application like <code>sshd</code>, you should provide a new network stack and a new hostname. If you want to avoid conflicts with some files eg. <i>/var/run/httpd.pid</i>, you should remount <i>/var/run</i> with an empty directory. If you want to avoid the conflicts in all the cases, you can specify a rootfs for the container. The rootfs can be a directory tree, previously bind mounted with the initial rootfs, so you can still use your distro but with your own <i>/etc</i> and <i>/home</i> </p>
<p> Here is an example of directory tree for <code>sshd</code>: </p>
<pre>[root@lxc sshd]$ tree -d rootfs
 
rootfs 
|-- bin 
|-- dev 
| |-- pts
| `-- shm
| `-- network
|-- etc 
| `-- ssh
|-- lib 
|-- proc
|-- root
|-- sbin
|-- sys 
|-- usr 
`-- var 
 |-- empty
 | `-- sshd
 |-- lib
 | `-- empty
 | `-- sshd
 `-- run
 `-- sshd</pre>
<p>and the mount points file associated with it: </p>
<pre> [root@lxc sshd]$ cat fstab
 /lib /home/root/sshd/rootfs/lib none ro,bind 0 0
 /bin /home/root/sshd/rootfs/bin none ro,bind 0 0
 /usr /home/root/sshd/rootfs/usr none ro,bind 0 0
 /sbin /home/root/sshd/rootfs/sbin none ro,bind 0 0</pre>
<p>How to run a system in a container ? </p>
<p> Running a system inside a container is paradoxically easier than running an application. Why ? Because you don&#8217;t have to care about the resources to be isolated, everything need to be isolated, the other resources are specified as being isolated but without configuration because the container will set them up. eg. the ipv4 address will be setup by the system container init scripts. Here is an example of the mount points file: </p>
<pre> [root@lxc debian]$ cat fstab
 /dev /home/root/debian/rootfs/dev none bind 0 0
 /dev/pts /home/root/debian/rootfs/dev/pts none bind 0 0</pre>
<p>More information can be added to the container to facilitate the configuration. For example, make accessible from the container the resolv.conf file belonging to the host. </p>
<pre> /etc/resolv.conf /home/root/debian/rootfs/etc/resolv.conf none bind 0 0</pre>
<h3>Container Life Cycle</h3>
<p>When the container is created, it contains the configuration information. When a process is launched, the container will be starting and running. When the last process running inside the container exits, the container is stopped. </p>
<p> In case of failure when the container is initialized, it will pass through the aborting state. </p>
<pre> ---------
 | STOPPED |&lt;---------------
 --------- |
 | |
 start |
 | |
 V |
 ---------- |
 | STARTING |--error- |
 ---------- | |
 | | |
 V V |
 --------- ---------- |
 | RUNNING | | ABORTING | |
 --------- ---------- |
 | | |
 no process | |
 | | |
 V | |
 ---------- | |
 | STOPPING |&lt;------- |
 ---------- |
 | |
 ---------------------</pre>
<h3>Configuration</h3>
<p>The container is configured through a configuration file, the format of the configuration file is described in <i><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></i>(5)</p>
<h3>Creating / Destroying Container (Persistent Container)</h3>
<p>A persistent container object can be created via the <code>lxc-create</code> command. It takes a container name as parameter and optional configuration file and template. The name is used by the different commands to refer to this container. The <code>lxc-destroy</code> command will destroy the container object. </p>
<pre> lxc-create -n foo
 lxc-destroy -n foo</pre>
<h3>Volatile Container</h3>
<p>It is not mandatory to create a container object before to start it. The container can be directly started with a configuration file as parameter.</p>
<h3>Starting / Stopping Container</h3>
<p>When the container has been created, it is ready to run an application / system. This is the purpose of the <code>lxc-execute</code> and <code>lxc-start</code> commands. If the container was not created before starting the application, the container will use the configuration file passed as parameter to the command, and if there is no such parameter either, then it will use a default isolation. If the application is ended, the container will be stopped also, but if needed the <code>lxc-stop</code> command can be used to kill the still running application. </p>
<p> Running an application inside a container is not exactly the same thing as running a system. For this reason, there are two different commands to run an application into a container: </p>
<pre> lxc-execute -n foo [-f config] /bin/bash
 lxc-start -n foo [-f config] [/bin/bash]</pre>
<p><code>lxc-execute</code> command will run the specified command into the container via an intermediate process, <code>lxc-init</code>. This lxc-init after launching the specified command, will wait for its end and all other reparented processes. (to support daemons in the container). In other words, in the container, <code>lxc-init</code> has the pid 1 and the first process of the application has the pid 2. </p>
<p> <code>lxc-start</code> command will run directly the specified command into the container. The pid of the first process is 1. If no command is specified <code>lxc-start</code> will run <i>/sbin/init</i>. </p>
<p> To summarize, <code>lxc-execute</code> is for running an application and <code>lxc-start</code> is better suited for running a system. </p>
<p> If the application is no longer responding, is inaccessible or is not able to finish by itself, a wild <code>lxc-stop</code> command will kill all the processes in the container without pity. </p>
<pre> lxc-stop -n foo</pre>
<h3>Connect To An Available Tty</h3>
<p>If the container is configured with the ttys, it is possible to access it through them. It is up to the container to provide a set of available tty to be used by the following command. When the tty is lost, it is possible to reconnect it without login again. </p>
<pre> lxc-console -n foo -t 3</pre>
<h3>Freeze / Unfreeze Container</h3>
<p>Sometime, it is useful to stop all the processes belonging to a container, eg. for job scheduling. The commands: </p>
<pre> lxc-freeze -n foo</pre>
<p>will put all the processes in an uninteruptible state and </p>
<pre> lxc-unfreeze -n foo</pre>
<p>will resume them. </p>
<p> This feature is enabled if the cgroup freezer is enabled in the kernel.</p>
<h3>Getting Information About Container</h3>
<p>When there are a lot of containers, it is hard to follow what has been created or destroyed, what is running or what are the pids running into a specific container. For this reason, the following commands may be useful: </p>
<pre> lxc-ls
 lxc-info -n foo</pre>
<p><code>lxc-ls</code> lists the containers of the system. </p>
<p> <code>lxc-info</code> gives information for a specific container. </p>
<p> Here is an example on how the combination of these commands allows one to list all the containers and retrieve their state. </p>
<pre> for i in $(lxc-ls -1); do
 lxc-info -n $i
 done</pre>
<h3>Monitoring Container</h3>
<p>It is sometime useful to track the states of a container, for example to monitor it or just to wait for a specific state in a script. </p>
<p> <code>lxc-monitor</code> command will monitor one or several containers. The parameter of this command accept a regular expression for example: </p>
<pre> lxc-monitor -n &quot;foo|bar&quot;</pre>
<p>will monitor the states of containers named &#8216;foo&#8217; and &#8216;bar&#8217;, and: </p>
<pre> lxc-monitor -n &quot;.*&quot;</pre>
<p>will monitor all the containers. </p>
<p> For a container &#8216;foo&#8217; starting, doing some work and exiting, the output will be in the form: </p>
<pre> 'foo' changed state to [STARTING]
 'foo' changed state to [RUNNING]
 'foo' changed state to [STOPPING]
 'foo' changed state to [STOPPED]</pre>
<p><code>lxc-wait</code> command will wait for a specific state change and exit. This is useful for scripting to synchronize the launch of a container or the end. The parameter is an ORed combination of different states. The following example shows how to wait for a container if he went to the background. </p>
<pre> # launch lxc-wait in background
 lxc-wait -n foo -s STOPPED &amp;
 LXC_WAIT_PID=$!
 # this command goes in background
 lxc-execute -n foo mydaemon &amp;
 # block until the lxc-wait exits
 # and lxc-wait exits when the container
 # is STOPPED
 wait $LXC_WAIT_PID
 echo &quot;'foo' is finished&quot;</pre>
<h3>Setting The Control Group For Container</h3>
<p>The container is tied with the control groups, when a container is started a control group is created and associated with it. The control group properties can be read and modified when the container is running by using the lxc-cgroup command. </p>
<p> <code>lxc-cgroup</code> command is used to set or get a control group subsystem which is associated with a container. The subsystem name is handled by the user, the command won&#8217;t do any syntax checking on the subsystem name, if the subsystem name does not exists, the command will fail. </p>
<pre> lxc-cgroup -n foo cpuset.cpus</pre>
<p>will display the content of this subsystem. </p>
<pre> lxc-cgroup -n foo cpu.shares 512</pre>
<p>will set the subsystem to the specified value.</p>
<h2>Bugs</h2>
<p>The <code>lxc</code> is still in development, so the command syntax and the API can change. The version 1.0.0 will be the frozen version.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt;</p>
