---
title: "docker-run(1)"
name: "docker-run"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-run/"
description: "docker-run – Run a command in a new container"
---

<h2 class="name">NAME</h2>
<p> docker-run &#8211; Run a command in a new container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker run</code> [<code>-a</code>|<code>&#8211;attach</code>[=<i>[]</i>]] [<code>&#8211;add-host</code>[=<i>[]</i>]] [<code>&#8211;blkio-weight</code>[=<i>[BLKIO-WEIGHT]</i>]] [<code>&#8211;blkio-weight-device</code>[=<i>[]</i>]] [<code>&#8211;cpu-shares</code>[=<i>0</i>]] [<code>&#8211;cap-add</code>[=<i>[]</i>]] [<code>&#8211;cap-drop</code>[=<i>[]</i>]] [<code>&#8211;cgroupns</code>[=<i>[]</i>]] [<code>&#8211;cgroup-parent</code>[=<i>CGROUP-PATH</i>]] [<code>&#8211;cidfile</code>[=<i>CIDFILE</i>]] [<code>&#8211;cpu-count</code>[=<i>0</i>]] [<code>&#8211;cpu-percent</code>[=<i>0</i>]] [<code>&#8211;cpu-period</code>[=<i>0</i>]] [<code>&#8211;cpu-quota</code>[=<i>0</i>]] [<code>&#8211;cpu-rt-period</code>[=<i>0</i>]] [<code>&#8211;cpu-rt-runtime</code>[=<i>0</i>]] [<code>&#8211;cpus</code>[=<i>0.0</i>]] [<code>&#8211;cpuset-cpus</code>[=<i>CPUSET-CPUS</i>]] [<code>&#8211;cpuset-mems</code>[=<i>CPUSET-MEMS</i>]] [<code>-d</code>|<code>&#8211;detach</code>] [<code>&#8211;detach-keys</code>[=<i>[]</i>]] [<code>&#8211;device</code>[=<i>[]</i>]] [<code>&#8211;device-cgroup-rule</code>[=<i>[]</i>]] [<code>&#8211;device-read-bps</code>[=<i>[]</i>]] [<code>&#8211;device-read-iops</code>[=<i>[]</i>]] [<code>&#8211;device-write-bps</code>[=<i>[]</i>]] [<code>&#8211;device-write-iops</code>[=<i>[]</i>]] [<code>&#8211;dns</code>[=<i>[]</i>]] [<code>&#8211;dns-option</code>[=<i>[]</i>]] [<code>&#8211;dns-search</code>[=<i>[]</i>]] [<code>&#8211;domainname</code>[=<i>DOMAINNAME</i>]] [<code>-e</code>|<code>&#8211;env</code>[=<i>[]</i>]] [<code>&#8211;entrypoint</code>[=<i>ENTRYPOINT</i>]] [<code>&#8211;env-file</code>[=<i>[]</i>]] [<code>&#8211;expose</code>[=<i>[]</i>]] [<code>&#8211;group-add</code>[=<i>[]</i>]] [<code>-h</code>|<code>&#8211;hostname</code>[=<i>HOSTNAME</i>]] [<code>&#8211;help</code>] [<code>&#8211;init</code>] [<code>-i</code>|<code>&#8211;interactive</code>] [<code>&#8211;ip</code>[=<i>IPv4-ADDRESS</i>]] [<code>&#8211;ip6</code>[=<i>IPv6-ADDRESS</i>]] [<code>&#8211;ipc</code>[=<i>IPC</i>]] [<code>&#8211;isolation</code>[=<i>default</i>]] [<code>&#8211;kernel-memory</code>[=<i>KERNEL-MEMORY</i>]] [<code>-l</code>|<code>&#8211;label</code>[=<i>[]</i>]] [<code>&#8211;label-file</code>[=<i>[]</i>]] [<code>&#8211;link</code>[=<i>[]</i>]] [<code>&#8211;link-local-ip</code>[=<i>[]</i>]] [<code>&#8211;log-driver</code>[=<i>[]</i>]] [<code>&#8211;log-opt</code>[=<i>[]</i>]] [<code>-m</code>|<code>&#8211;memory</code>[=<i>MEMORY</i>]] [<code>&#8211;mac-address</code>[=<i>MAC-ADDRESS</i>]] [<code>&#8211;memory-reservation</code>[=<i>MEMORY-RESERVATION</i>]] [<code>&#8211;memory-swap</code>[=<i>LIMIT</i>]] [<code>&#8211;memory-swappiness</code>[=<i>MEMORY-SWAPPINESS</i>]] [<code>&#8211;mount</code>[=<i>[MOUNT]</i>]] [<code>&#8211;name</code>[=<i>NAME</i>]] [<code>&#8211;network-alias</code>[=<i>[]</i>]] [<code>&#8211;network</code>[=<i>&quot;bridge&quot;</i>]] [<code>&#8211;oom-kill-disable</code>] [<code>&#8211;oom-score-adj</code>[=<i>0</i>]] [<code>-P</code>|<code>&#8211;publish-all</code>] [<code>-p</code>|<code>&#8211;publish</code>[=<i>[]</i>]] [<code>&#8211;pid</code>[=<i>[PID]</i>]] [<code>&#8211;userns</code>[=<i>[]</i>]] [<code>&#8211;pids-limit</code>[=<i>PIDS_LIMIT</i>]] [<code>&#8211;privileged</code>] [<code>&#8211;read-only</code>] [<code>&#8211;restart</code>[=<i>RESTART</i>]] [<code>&#8211;rm</code>] [<code>&#8211;security-opt</code>[=<i>[]</i>]] [<code>&#8211;storage-opt</code>[=<i>[]</i>]] [<code>&#8211;stop-signal</code>[=<i>SIGNAL</i>]] [<code>&#8211;stop-timeout</code>[=<i>TIMEOUT</i>]] [<code>&#8211;shm-size</code>[=<i>[]</i>]] [<code>&#8211;sig-proxy</code>[=<i>true</i>]] [<code>&#8211;sysctl</code>[=<i>[]</i>]] [<code>-t</code>|<code>&#8211;tty</code>] [<code>&#8211;tmpfs</code>[=<i>[CONTAINER-DIR[:OPTIONS]</i>]] [<code>-u</code>|<code>&#8211;user</code>[=<i>USER</i>]] [<code>&#8211;ulimit</code>[=<i>[]</i>]] [<code>&#8211;uts</code>[=<i>[]</i>]] [<code>-v</code>|<code>&#8211;volume</code>[=<i>[[HOST-DIR:]CONTAINER-DIR[:OPTIONS]]</i>]] [<code>&#8211;volume-driver</code>[=<i>DRIVER</i>]] [<code>&#8211;volumes-from</code>[=<i>[]</i>]] [<code>-w</code>|<code>&#8211;workdir</code>[=<i>WORKDIR</i>]] IMAGE [COMMAND] [ARG&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Run a process in a new container. <code>docker run</code> starts a process with its own file system, its own networking, and its own isolated process tree. The IMAGE which starts the process may define defaults related to the process that will be run in the container, the networking to expose, and more, but <code>docker run</code> gives final control to the operator or administrator who starts the container from the image. For that reason <code>docker run</code> has more options than any other Docker command. </p>
<p> If the IMAGE is not already loaded then <code>docker run</code> will pull the IMAGE, and all image dependencies, from the repository in the same way running <code>docker pull</code> IMAGE, before it starts the container from that image. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;attach</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Attach to STDIN, STDOUT or STDERR. </p>
<p> In foreground mode (the default when <code>-d</code> is not specified), <code>docker run</code> can start the process in the container and attach the console to the process&#8217;s standard input, output, and standard error. It can even pretend to be a TTY (this is what most commandline executables expect) and pass along signals. The <code>-a</code> option can be set for each of stdin, stdout, and stderr. </p>
<p> <code>&#8211;add-host</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Add a custom host-to-IP mapping&nbsp;(host:ip) </p>
<p> Add a line to /etc/hosts. The format is hostname:ip. The <code>&#8211;add-host</code> option can be set multiple times. </p>
<p> <code>&#8211;blkio-weight</code>=<i>0</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Block IO weight&nbsp;(relative weight)&nbsp;accepts a weight value between 10 and 1000. </p>
<p> <code>&#8211;blkio-weight-device</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Block IO weight&nbsp;(relative device weight, format: DEVICE_NAME:WEIGHT). </p>
<p> <code>&#8211;cpu-shares</code>=<i>0</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;CPU shares&nbsp;(relative weight) </p>
<p> By default, all containers get the same proportion of CPU cycles. This proportion can be modified by changing the container&#8217;s CPU share weighting relative to the weighting of all other running containers. </p>
<p> To modify the proportion from the default of 1024, use the <code>&#8211;cpu-shares</code> flag to set the weighting to 2 or higher. </p>
<p> The proportion will only apply when CPU-intensive processes are running. When tasks in one container are idle, other containers can use the left-over CPU time. The actual amount of CPU time will vary depending on the number of containers running on the system. </p>
<p> For example, consider three containers, one has a cpu-share of 1024 and two others have a cpu-share setting of 512. When processes in all three containers attempt to use 100% of CPU, the first container would receive 50% of the total CPU time. If you add a fourth container with a cpu-share of 1024, the first container only gets 33% of the CPU. The remaining containers receive 16.5%, 16.5% and 33% of the CPU. </p>
<p> On a multi-core system, the shares of CPU time are distributed over all CPU cores. Even if a container is limited to less than 100% of CPU time, it can use 100% of each individual CPU core. </p>
<p> For example, consider a system with more than three cores. If you start one container <code>{C0}</code> with <code>-c=512</code> running one process, and another container <code>{C1}</code> with <code>-c=1024</code> running two processes, this can result in the following division of CPU shares: </p>
<dl>
<dt>
<dd>
<pre><code>
PID container CPU CPU share 100
{
    C0
}
0 100 % of CPU0 101
{
    C1
}
1 100 % of CPU1 102
{
    C1
}
2 100 % of CPU2
</code></pre>
</dl>
<p> <code>&#8211;cap-add</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Add Linux capabilities </p>
<p> <code>&#8211;cap-drop</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Drop Linux capabilities </p>
<p> <code>&#8211;cgroupns</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set the cgroup namespace mode for the container.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>host</code>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;run the container in the host&#8217;s cgroup namespace<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>private</code>: run the container in its own private cgroup namespace<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&quot;&quot;</code>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(unset)&nbsp;use the daemon&#8217;s default configuration&nbsp;(<code>host</code>&nbsp;on cgroup v1,&nbsp;<code>private</code>&nbsp;on cgroup v2) </p>
<p> <code>&#8211;cgroup-parent</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Path to cgroups under which the cgroup for the container will be created. If the path is not absolute, the path is considered to be relative to the cgroups path of the init process. Cgroups will be created if they do not already exist. </p>
<p> <code>&#8211;cidfile</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Write the container ID to the file </p>
<p> <code>&#8211;cpu-count</code>=<i>0</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit the number of CPUs available for execution by the container. </p>
<dl>
<dt>
<dd>
<pre>
On Windows Server containers, this is approximated as a percentage of total CPU usage.
On Windows Server containers, the processor resource controls are mutually exclusive, the order of precedence is CPUCount first, then CPUShares, and CPUPercent last.
</pre>
</dl>
<p> <code>&#8211;cpu-percent</code>=<i>0</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit the percentage of CPU available for execution by a container running on a Windows daemon. </p>
<dl>
<dt>
<dd>
<pre>
On Windows Server containers, the processor resource controls are mutually exclusive, the order of precedence is CPUCount first, then CPUShares, and CPUPercent last.
</pre>
</dl>
<p> <code>&#8211;cpu-period</code>=<i>0</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit the CPU CFS&nbsp;(Completely Fair Scheduler)&nbsp;period </p>
<p> Limit the container&#8217;s CPU usage. This flag tell the kernel to restrict the container&#8217;s CPU usage to the period you specify. </p>
<p> <code>&#8211;cpuset-cpus</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;CPUs in which to allow execution&nbsp;(0-3, 0,1) </p>
<p> <code>&#8211;cpuset-mems</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Memory nodes&nbsp;(MEMs)&nbsp;in which to allow execution&nbsp;(0-3, 0,1). Only effective on NUMA systems. </p>
<p> If you have four memory nodes on your system (0-3), use &#8211;cpuset-mems=0,1 then processes in your Docker container will only use memory from the first two memory nodes. </p>
<p> <code>&#8211;cpu-quota</code>=<i>0</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit the CPU CFS&nbsp;(Completely Fair Scheduler)&nbsp;quota </p>
<p> Limit the container&#8217;s CPU usage. By default, containers run with the full CPU resource. This flag tell the kernel to restrict the container&#8217;s CPU usage to the quota you specify. </p>
<p> <code>&#8211;cpu-rt-period</code>=0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit the CPU real-time period in microseconds </p>
<p> Limit the container&#8217;s Real Time CPU usage. This flag tell the kernel to restrict the container&#8217;s Real Time CPU usage to the period you specify. </p>
<p> <code>&#8211;cpu-rt-runtime</code>=0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit the CPU real-time runtime in microseconds </p>
<p> Limit the containers Real Time CPU usage. This flag tells the kernel to limit the amount of time in a given CPU period Real Time tasks may consume. Ex:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Period of 1,000,000us and Runtime of 950,000us means that this container could consume 95%&nbsp;of available CPU and leave the remaining 5%&nbsp;to normal priority tasks. </p>
<p> The sum of all runtimes across containers cannot exceed the amount allotted to the parent cgroup. </p>
<p> <code>&#8211;cpus</code>=0.0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number of CPUs. The default is&nbsp;<i>0.0</i>&nbsp;which means no limit. </p>
<p> <code>-d</code>, <code>&#8211;detach</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Detached mode: run the container in the background and print the new container ID. The default is&nbsp;<i>false</i>. </p>
<p> At any time you can run <code>docker ps</code> in the other shell to view a list of the running containers. You can reattach to a detached container with <code>docker attach</code>. </p>
<p> When attached in the tty mode, you can detach from the container (and leave it running) using a configurable key sequence. The default sequence is CTRL-p CTRL-q. You configure the key sequence using the <code>&#8211;detach-keys</code> option or a configuration file. See <code><a href="/docs/linux/man/5-config-json/">config-json</a>(5)</code> for documentation on using a configuration file. </p>
<p> <code>&#8211;detach-keys</code>=<i>key</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Override the key sequence for detaching a container;&nbsp;<i>key</i>&nbsp;is a single character from the&nbsp;[a-Z]&nbsp;range, or&nbsp;<code>ctrl</code>&#8211;<i>value</i>, where&nbsp;<i>value</i>&nbsp;is one of:&nbsp;<code>a-z</code>,&nbsp;<code>@</code>,&nbsp;<code>^</code>,&nbsp;<code>[</code>,&nbsp;<code>,</code>, or&nbsp;<code>_</code>. </p>
<p> <code>&#8211;device</code>=<i>onhost</i>:<i>incontainer</i>[:<i>mode</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Add a host device&nbsp;<i>onhost</i>&nbsp;to the container under the&nbsp;<i>incontainer</i>&nbsp;name. Optional <i>mode</i> parameter can be used to specify device permissions, it is a combination of <code>r</code> (for read), <code>w</code> (for write), and <code>m</code> (for <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2)). </p>
<p> For example, <code>&#8211;device=/dev/sdc:/dev/xvdc:rwm</code> will give a container all permissions for the host device <code>/dev/sdc</code>, seen as <code>/dev/xvdc</code> inside the container. </p>
<p> <code>&#8211;device-cgroup-rule</code>=&quot;<i>type</i> <i>major</i>:<i>minor</i> <i>mode</i>&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Add a rule to the cgroup allowed devices list. The rule is expected to be in the format specified in the Linux kernel documentation&nbsp;(Documentation/cgroup-v1/devices.txt):<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;&nbsp;<i>type</i>:&nbsp;<code>a</code>&nbsp;(all),&nbsp;<code>c</code>&nbsp;(char), or&nbsp;<code>b</code>&nbsp;(block);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;&nbsp;<i>major</i>&nbsp;and&nbsp;<i>minor</i>: either a number, or&nbsp;<code>*</code>&nbsp;for all;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;&nbsp;<i>mode</i>: a composition of&nbsp;<code>r</code>&nbsp;(read),&nbsp;<code>w</code>&nbsp;(write), and&nbsp;<code>m</code>&nbsp;(<code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2)). </p>
<p> Example: <code>&#8211;device-cgroup-rule &quot;c 1:3 mr&quot;</code>: allow for a character device idendified by <code>1:3</code> to be created and read. </p>
<p> <code>&#8211;device-read-bps</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit read rate from a device&nbsp;(e.g. &#8211;device-read-bps=/dev/sda:1mb) </p>
<p> <code>&#8211;device-read-iops</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit read rate from a device&nbsp;(e.g. &#8211;device-read-iops=/dev/sda:1000) </p>
<p> <code>&#8211;device-write-bps</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit write rate to a device&nbsp;(e.g. &#8211;device-write-bps=/dev/sda:1mb) </p>
<p> <code>&#8211;device-write-iops</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Limit write rate to a device&nbsp;(e.g. &#8211;device-write-iops=/dev/sda:1000) </p>
<p> <code>&#8211;dns-search</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set custom DNS search domains&nbsp;(Use &#8211;dns-search=. if you don&#8217;t wish to set the search domain) </p>
<p> <code>&#8211;dns-option</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set custom DNS options </p>
<p> <code>&#8211;dns</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set custom DNS servers </p>
<p> This option can be used to override the DNS configuration passed to the container. Typically this is necessary when the host DNS configuration is invalid for the container (e.g., 127.0.0.1). When this is the case the <code>&#8211;dns</code> flags is necessary for every run. </p>
<p> <code>&#8211;domainname</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Container NIS domain name </p>
<p> Sets the container&#8217;s NIS domain name (see also <code><a href="/docs/linux/man/2-setdomainname/">setdomainname</a>(2)</code>) that is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;available inside the container. </p>
<p> <code>-e</code>, <code>&#8211;env</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set environment variables </p>
<p> This option allows you to specify arbitrary environment variables that are available for the process that will be launched inside of the container. </p>
<p> <code>&#8211;entrypoint</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Overwrite the default ENTRYPOINT of the image </p>
<p> This option allows you to overwrite the default entrypoint of the image that is set in the Dockerfile. The ENTRYPOINT of an image is similar to a COMMAND because it specifies what executable to run when the container starts, but it is (purposely) more difficult to override. The ENTRYPOINT gives a container its default nature or behavior, so that when you set an ENTRYPOINT you can run the container as if it were that binary, complete with default options, and you can pass in more options via the COMMAND. But, sometimes an operator may want to run something else inside the container, so you can override the default ENTRYPOINT at runtime by using a <code>&#8211;entrypoint</code> and a string to specify the new ENTRYPOINT. </p>
<p> <code>&#8211;env-file</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Read in a line delimited file of environment variables </p>
<p> <code>&#8211;expose</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Expose a port, or a range of ports&nbsp;(e.g. &#8211;expose=3300-3310)&nbsp;informs Docker that the container listens on the specified network ports at runtime. Docker uses this information to interconnect containers using links and to set up port redirection on the host system. </p>
<p> <code>&#8211;group-add</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Add additional groups to run as </p>
<p> <code>-h</code>, <code>&#8211;hostname</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Container host name </p>
<p> Sets the container host name that is available inside the container. </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Print usage statement </p>
<p> <code>&#8211;init</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Run an init inside the container that forwards signals and reaps processes </p>
<p> <code>-i</code>, <code>&#8211;interactive</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Keep STDIN open even if not attached. The default is&nbsp;<i>false</i>. </p>
<p> When set to true, keep stdin open even if not attached. </p>
<p> <code>&#8211;ip</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sets the container&#8217;s interface IPv4 address&nbsp;(e.g., 172.23.0.9) </p>
<p> It can only be used in conjunction with <code>&#8211;network</code> for user-defined networks </p>
<p> <code>&#8211;ip6</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sets the container&#8217;s interface IPv6 address&nbsp;(e.g., 2001:db8::1b99) </p>
<p> It can only be used in conjunction with <code>&#8211;network</code> for user-defined networks </p>
<p> <code>&#8211;ipc</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sets the IPC mode for the container. The following values are accepted: </p>
<table BORDER>
<tr VALIGN=top>
<td>Value</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>(empty)</td>
<td>Use daemon&#8217;s default.
</td>
</tr>
<tr VALIGN=top>
<td><code>none</code></td>
<td> Own private IPC namespace, with /dev/shm not mounted.
</td>
</tr>
<tr VALIGN=top>
<td><code>private</code></td>
<td>Own private IPC namespace.
</td>
</tr>
<tr VALIGN=top>
<td><code>shareable</code></td>
<td> Own private IPC namespace, with a possibility to share it with other containers.
</td>
</tr>
<tr VALIGN=top>
<td><code>container:</code><i>name-or-ID</i></td>
<td> Join another (&quot;shareable&quot;) container&#8217;s IPC namespace.
</td>
</tr>
<tr VALIGN=top>
<td><code>host</code></td>
<td> Use the host system&#8217;s IPC namespace.
</td>
</tr>
</table>
<p> If not specified, daemon default is used, which can either be <code>private</code> or <code>shareable</code>, depending on the daemon version and configuration. </p>
<p> <code>&#8211;isolation</code>=&quot;<i>default</i>&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Isolation specifies the type of isolation technology used by containers. Note that the default on Windows server is process, and the default on Windows client is hyperv. Linux only supports default. </p>
<p> <code>-l</code>, <code>&#8211;label</code> <i>key</i>=<i>value</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set metadata on the container&nbsp;(for example,&nbsp;<code>&#8211;label com.example.key=value</code>). </p>
<p> <code>&#8211;kernel-memory</code>=<i>number</i>[<i>S</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Kernel memory limit;&nbsp;<i>S</i>&nbsp;is an optional suffix which can be one of&nbsp;<code>b</code>,&nbsp;<code>k</code>,&nbsp;<code>m</code>, or&nbsp;<code>g</code>. </p>
<p> Constrains the kernel memory available to a container. If a limit of 0 is specified (not using <code>&#8211;kernel-memory</code>), the container&#8217;s kernel memory is not limited. If you specify a limit, it may be rounded up to a multiple of the operating system&#8217;s page size and the value can be very large, millions of trillions. </p>
<p> <code>&#8211;label-file</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Read in a line delimited file of labels </p>
<p> <code>&#8211;link</code>=<i>name-or-id</i>[:<i>alias</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Add link to another container. </p>
<p> If the operator uses <code>&#8211;link</code> when starting the new client container, then the client container can access the exposed port via a private networking interface. Docker will set some environment variables in the client container to help indicate which interface and port to use. </p>
<p> <code>&#8211;link-local-ip</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Add one or more link-local IPv4/IPv6 addresses to the container&#8217;s interface </p>
<p> <code>&#8211;log-driver</code>=&quot;<i>json-file</i>|<i>syslog</i>|<i>journald</i>|<i>gelf</i>|<i>fluentd</i>|<i>awslogs</i>|<i>splunk</i>|<i>etwlogs</i>|<i>gcplogs</i>|<i>none</i>&quot;<br />
&nbsp;<wbr>&nbsp;Logging driver for the container. Default is defined by daemon&nbsp;<code>&#8211;log-driver</code>&nbsp;flag.<br />
&nbsp;<wbr>&nbsp;<code>Warning</code>: the docker logs command works only for the json-file and<br />
&nbsp;<wbr>&nbsp;journald logging drivers. </p>
<p> <code>&#8211;log-opt</code>=[]<br />
&nbsp;<wbr>&nbsp;Logging driver specific options. </p>
<p> <code>-m</code>, <code>&#8211;memory</code>=<i>number</i>[*S]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Memory limit;&nbsp;<i>S</i>&nbsp;is an optional suffix which can be one of&nbsp;<code>b</code>,&nbsp;<code>k</code>,&nbsp;<code>m</code>, or&nbsp;<code>g</code>. </p>
<p> Allows you to constrain the memory available to a container. If the host supports swap memory, then the <code>-m</code> memory setting can be larger than physical RAM. If a limit of 0 is specified (not using <code>-m</code>), the container&#8217;s memory is not limited. The actual limit may be rounded up to a multiple of the operating system&#8217;s page size (the value would be very large, that&#8217;s millions of trillions). </p>
<p> <code>&#8211;memory-reservation</code>=<i>number</i>[*S]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Memory soft limit;&nbsp;<i>S</i>&nbsp;is an optional suffix which can be one of&nbsp;<code>b</code>,&nbsp;<code>k</code>,&nbsp;<code>m</code>, or&nbsp;<code>g</code>. </p>
<p> After setting memory reservation, when the system detects memory contention or low memory, containers are forced to restrict their consumption to their reservation. So you should always set the value below <code>&#8211;memory</code>, otherwise the hard limit will take precedence. By default, memory reservation will be the same as memory limit. </p>
<p> <code>&#8211;memory-swap</code>=<i>number</i>[<i>S</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Combined memory plus swap limit;&nbsp;<i>S</i>&nbsp;is an optional suffix which can be one of&nbsp;<code>b</code>,&nbsp;<code>k</code>,&nbsp;<code>m</code>, or&nbsp;<code>g</code>. </p>
<p> This option can only be used together with <code>&#8211;memory</code>. The argument should always be larger than that of <code>&#8211;memory</code>. Default is double the value of <code>&#8211;memory</code>. Set to <code>-1</code> to enable unlimited swap. </p>
<p> <code>&#8211;mac-address</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Container MAC address&nbsp;(e.g.,&nbsp;<code>92:d0:c6:0a:29:33</code>) </p>
<p> Remember that the MAC address in an Ethernet network must be unique. The IPv6 link-local address will be based on the device&#8217;s MAC address according to RFC4862. </p>
<p> <code>&#8211;mount</code> <code>type=</code><i>TYPE</i>,<i>TYPE-SPECIFIC-OPTION</i>[,&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Attach a filesystem mount to the container </p>
<p> Current supported mount TYPES are bind, volume, and tmpfs. </p>
<p> e.g. </p>
<p> type=bind,source=/path/on/host,destination=/path/in/container </p>
<p> type=volume,source=my-volume,destination=/path/in/container,volume-label=&quot;color=red&quot;,volume-label=&quot;shape=round&quot; </p>
<p> type=tmpfs,tmpfs-size=512M,destination=/path/in/container </p>
<p> Common Options: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> src, source: mount source spec for bind and volume. Mandatory for bind.</p>
<dt>&bull;</p>
<dd> dst, destination, target: mount destination spec.</p>
<dt>&bull;</p>
<dd> ro, readonly: true or false (default). </p>
</dl>
</dl>
<p> <code>Note</code>: setting readonly for a bind mount does not make its submounts<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;read-only on the current Linux implementation. See also bind-nonrecursive. </p>
<p> Options specific to bind: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> bind-propagation: shared, slave, private, rshared, rslave, or rprivate(default). See also <a href="/docs/linux/man/2-mount/">mount</a>(2).</p>
<dt>&bull;</p>
<dd> consistency: consistent(default), cached, or delegated. Currently, only effective for Docker for Mac.</p>
<dt>&bull;</p>
<dd> bind-nonrecursive: true or false (default). If set to true, submounts are not recursively bind-mounted. This option is useful for readonly bind mount. </p>
</dl>
</dl>
<p> Options specific to volume: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> volume-driver: Name of the volume-driver plugin.</p>
<dt>&bull;</p>
<dd> volume-label: Custom metadata.</p>
<dt>&bull;</p>
<dd> volume-nocopy: true(default) or false. If set to false, the Engine copies existing files and directories under the mount-path into the volume, allowing the host to access them.</p>
<dt>&bull;</p>
<dd> volume-opt: specific to a given volume driver. </p>
</dl>
</dl>
<p> Options specific to tmpfs: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> tmpfs-size: Size of the tmpfs mount in bytes. Unlimited by default in Linux.</p>
<dt>&bull;</p>
<dd> tmpfs-mode: File mode of the tmpfs in octal. (e.g. 700 or 0700.) Defaults to 1777 in Linux. </p>
</dl>
</dl>
<p> <code>&#8211;name</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Assign a name to the container </p>
<p> The operator can identify a container in three ways: </p>
<table BORDER>
<tr VALIGN=top>
<td>Identifier type</td>
<td>Example value
</td>
</tr>
<tr VALIGN=top>
<td>UUID long identifier</td>
<td> &quot;f78375b1c487e03c9438c729345e54db9d20cfa2ac1fc3494b6eb60872e74778&quot;
</td>
</tr>
<tr VALIGN=top>
<td>UUID short identifier</td>
<td>&quot;f78375b1c487&quot;
</td>
</tr>
<tr VALIGN=top>
<td>Name</td>
<td>&quot;evil_ptolemy&quot;
</td>
</tr>
</table>
<p> The UUID identifiers come from the Docker daemon, and if a name is not assigned to the container with <code>&#8211;name</code> then the daemon will also generate a random string name. The name is useful when defining links (see <code>&#8211;link</code>) (or any other place you need to identify a container). This works for both background and foreground Docker containers. </p>
<p> <code>&#8211;network</code>=<i>type</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set the Network mode for the container. Supported values are: </p>
<table BORDER>
<tr VALIGN=top>
<td>Value</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td><code>none</code></td>
<td> No networking in the container.
</td>
</tr>
<tr VALIGN=top>
<td><code>bridge</code></td>
<td> Connect the container to the default Docker bridge via veth interfaces.
</td>
</tr>
<tr VALIGN=top>
<td><code>host</code></td>
<td> Use the host&#8217;s network stack inside the container.
</td>
</tr>
<tr VALIGN=top>
<td><code>container:</code><i>name</i>|<i>id</i></td>
<td> Use the network stack of another container, specified via its <i>name</i> or <i>id</i>.
</td>
</tr>
<tr VALIGN=top>
<td><i>network-name</i>|<i>network-id</i></td>
<td> Connects the container to a user created network (using docker network create command)
</td>
</tr>
</table>
<p> Default is <code>bridge</code>. </p>
<p> <code>&#8211;network-alias</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Add network-scoped alias for the container </p>
<p> <code>&#8211;oom-kill-disable</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Whether to disable OOM Killer for the container or not. </p>
<p> <code>&#8211;oom-score-adj</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Tune the host&#8217;s OOM preferences for containers&nbsp;(accepts -1000 to 1000) </p>
<p> <code>-P</code>, <code>&#8211;publish-all</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Publish all exposed ports to random ports on the host interfaces. The default is&nbsp;<i>false</i>. </p>
<p> When set to true publish all exposed ports to the host interfaces. The default is false. If the operator uses -P (or -p) then Docker will make the exposed port accessible on the host and the ports will be available to any client that can reach the host. When using -P, Docker will bind any exposed port to a random port on the host within an <i>ephemeral port range</i> defined by /proc/sys/net/ipv4/ip_local_port_range. To find the mapping between the host ports and the exposed ports, use docker <a href="/docs/linux/man/1-port/">port</a>(1). </p>
<p> <code>-p</code>, <code>&#8211;publish</code> <i>ip</i>:[<i>hostPort</i>]:<i>containerPort</i> | [<i>hostPort</i>:]<i>containerPort</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Publish a container&#8217;s port, or range of ports, to the host. </p>
<p> Both <i>hostPort</i> and <i>containerPort</i> can be specified as a range. When specifying ranges for both, the number of ports in ranges should be equal. </p>
<p> Examples: <code>-p 1234-1236:1222-1224</code>, <code>-p 127.0.0.1:$HOSTPORT:$CONTAINERPORT</code>. </p>
<p> Use docker <a href="/docs/linux/man/1-port/">port</a>(1) to see the actual mapping, e.g. docker port CONTAINER $CONTAINERPORT. </p>
<p> <code>&#8211;pid</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set the PID mode for the container<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Default is to create a private PID namespace for the container<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;container:&#8217;: join another container&#8217;s PID namespace<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;host&#8217;: use the host&#8217;s PID namespace for the container. Note: the host mode gives the container full access to local PID and is therefore considered insecure. </p>
<p> <code>&#8211;userns</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set the usernamespace mode for the container when userns-remap option is enabled.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>host</code>: use the host usernamespace and enable all privileged options&nbsp;(e.g., pid=host or &#8211;privileged). </p>
<p> <code>&#8211;pids-limit</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Tune the container&#8217;s pids&nbsp;(process IDs)&nbsp;limit. Set to -1 to have unlimited pids for the container. </p>
<p> <code>&#8211;uts</code>=<i>type</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set the UTS mode for the container. The only possible&nbsp;<i>type</i>&nbsp;is&nbsp;<code>host</code>, meaning to use the host&#8217;s UTS namespace inside the container.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Note: the host mode gives the container access to changing the host&#8217;s hostname and is therefore considered insecure. </p>
<p> <code>&#8211;privileged</code> [<code>true</code>|<code>false</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Give extended privileges to this container. A&nbsp;&quot;privileged&quot;&nbsp;container is given access to all devices. </p>
<p> When the operator executes <code>docker run &#8211;privileged</code>, Docker will enable access to all devices on the host as well as set some configuration in AppArmor to allow the container nearly all the same access to the host as processes running outside of a container on the host. </p>
<p> <code>&#8211;read-only</code>=<code>true</code>|<code>false</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mount the container&#8217;s root filesystem as read only. </p>
<p> By default a container will have its root filesystem writable allowing processes to write files anywhere. By specifying the &#8211;read-only flag the container will have its root filesystem mounted as read only prohibiting any writes. </p>
<p> <code>&#8211;restart</code> <i>policy</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Restart policy to apply when a container exits. Supported values are: </p>
<table BORDER>
<tr VALIGN=top>
<td>Policy</td>
<td>Result
</td>
</tr>
<tr VALIGN=top>
<td><code>no</code></td>
<td> Do not automatically restart the container when it exits.
</td>
</tr>
<tr VALIGN=top>
<td><code>on-failure</code>[:<i>max-retries</i>]</td>
<td> Restart only if the container exits with a non-zero exit status. Optionally, limit the number of restart retries the Docker daemon attempts.
</td>
</tr>
<tr VALIGN=top>
<td><code>always</code></td>
<td> Always restart the container regardless of the exit status. When you specify always, the Docker daemon will try to restart the container indefinitely. The container will also always start on daemon startup, regardless of the current state of the container.
</td>
</tr>
<tr VALIGN=top>
<td><code>unless-stopped</code></td>
<td> Always restart the container regardless of the exit status, but do not start it on daemon startup if the container has been put to a stopped state before.
</td>
</tr>
</table>
<p> Default is <code>no</code>. </p>
<p> <code>&#8211;rm</code> <code>true</code>|<code>false</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Automatically remove the container when it exits. The default is&nbsp;<code>false</code>.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;rm flag can work together with -d, and auto-removal will be done on daemon side. Note that it&#8217;s incompatible with any restart policy other than none. </p>
<p> <code>&#8211;security-opt</code> <i>value</i>[,&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Security Options for the container. The following options can be given: </p>
<dl>
<dt>
<dd>
<p>&#8220;label=user:USER&#8221;   : Set the label user for the container<br />
&#8220;label=role:ROLE&#8221;   : Set the label role for the container<br />
&#8220;label=type:TYPE&#8221;   : Set the label type for the container<br />
&#8220;label=level:LEVEL&#8221; : Set the label level for the container<br />
&#8220;label=disable&#8221;     : Turn off label confinement for the container<br />
&#8220;no-new-privileges&#8221; : Disable container processes from gaining additional privileges<br />
&#8220;seccomp=unconfined&#8221; : Turn off seccomp confinement for the container<br />
&#8220;seccomp=profile.json :  White listed syscalls seccomp Json file to be used as a seccomp filter<br />
&#8220;apparmor=unconfined&#8221; : Turn off apparmor confinement for the container<br />
&#8220;apparmor=your-profile&#8221; : Set the apparmor confinement profile for the container
</dl>
<p> <code>&#8211;storage-opt</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Storage driver options per container </p>
<p> $ docker run -it &#8211;storage-opt size=120G fedora /bin/bash </p>
<p> This (size) will allow to set the container rootfs size to 120G at creation time.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;This option is only available for the devicemapper, btrfs, overlay2&nbsp;<wbr>&nbsp;and zfs graph drivers.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;For the devicemapper, btrfs and zfs storage drivers, user cannot pass a size less than the Default BaseFS Size.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;For the overlay2 storage driver, the size option is only available if the backing fs is xfs and mounted with the pquota mount option.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Under these conditions, user can pass any size less than the backing fs size. </p>
<p> <code>&#8211;stop-signal</code>=<i>SIGTERM</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Signal to stop the container. Default is SIGTERM. </p>
<p> The &#8211;stop-signal flag sets the system call signal that will be sent to the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;container to exit. This signal can be a signal name in the format SIG&lt;NAME&gt;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;for instance SIGKILL, or an unsigned number that matches a position in the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;kernel&#8217;s syscall table, for instance 9. </p>
<p> <code>&#8211;stop-timeout</code><br />
&nbsp;<wbr>&nbsp;Timeout&nbsp;(in seconds)&nbsp;to stop a container, or&nbsp;<code>-1</code>&nbsp;to disable timeout. </p>
<p> The &#8211;stop-timeout flag sets the number of seconds to wait for the container<br />
&nbsp;<wbr>&nbsp;to stop after sending the pre-defined&nbsp;(see &#8211;stop-signal)&nbsp;system call signal.<br />
&nbsp;<wbr>&nbsp;If the container does not exit after the timeout elapses, it is forcibly killed<br />
&nbsp;<wbr>&nbsp;with a SIGKILL signal. </p>
<p> If &#8211;stop-timeout is set to <code>-1</code>, no timeout is applied, and the daemon will<br />
&nbsp;<wbr>&nbsp;wait indefinitely for the container to exit. </p>
<p> The default is determined by the daemon, and 10 seconds for Linux containers,<br />
&nbsp;<wbr>&nbsp;and 30 seconds for Windows containers. </p>
<p> <code>&#8211;shm-size</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Size of&nbsp;/dev/shm. The format is&nbsp;&lt;number&gt;&lt;unit&gt;.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;number must be greater than 0.&nbsp;<wbr>&nbsp;Unit is optional and can be b&nbsp;(bytes), k&nbsp;(kilobytes), m(megabytes), or g&nbsp;(gigabytes).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;If you omit the unit, the system uses bytes. If you omit the size entirely, the system uses 64m. </p>
<p> <code>&#8211;sysctl</code>=SYSCTL<br />
&nbsp;<wbr>&nbsp;Configure namespaced kernel parameters at runtime </p>
<p> IPC Namespace &#8211; current sysctls allowed: </p>
<p> kernel.msgmax, kernel.msgmnb, kernel.msgmni, kernel.sem, kernel.shmall, kernel.shmmax, kernel.shmmni, kernel.shm_rmid_forced<br />
&nbsp;<wbr>&nbsp;Sysctls beginning with fs.mqueue.* </p>
<p> If you use the &#8211;ipc=host option these sysctls will not be allowed. </p>
<p> Network Namespace &#8211; current sysctls allowed:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sysctls beginning with net.* </p>
<p> If you use the &#8211;network=host option these sysctls will not be allowed. </p>
<p> <code>&#8211;sig-proxy</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Proxy received signals to the process&nbsp;(non-TTY mode only). SIGCHLD, SIGSTOP, and SIGKILL are not proxied. The default is&nbsp;<i>true</i>. </p>
<p> <code>&#8211;memory-swappiness</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Tune a container&#8217;s memory swappiness behavior. Accepts an integer between 0 and 100. </p>
<p> <code>-t</code>, <code>&#8211;tty</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Allocate a pseudo-TTY. The default is&nbsp;<i>false</i>. </p>
<p> When set to true Docker can allocate a pseudo-tty and attach to the standard input of any container. This can be used, for example, to run a throwaway interactive shell. The default is false. </p>
<p> The <code>-t</code> option is incompatible with a redirection of the docker client standard input. </p>
<p> <code>&#8211;tmpfs</code>=[] Create a tmpfs mount </p>
<p> Mount a temporary filesystem (tmpfs) mount into a container, for example: </p>
<p> $ docker run -d &#8211;tmpfs /tmp:rw,size=787448k,mode=1777 my_image </p>
<p> This command mounts a tmpfs at /tmp within the container. The supported mount options are the same as the Linux default mount flags. If you do not specify any options, the systems uses the following options: rw,noexec,nosuid,nodev,size=65536k. </p>
<p> See also &#8211;mount, which is the successor of &#8211;tmpfs and &#8211;volume.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Even though there is no plan to deprecate &#8211;tmpfs, usage of &#8211;mount is recommended. </p>
<p> <code>-u</code>, <code>&#8211;user</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sets the username or UID used and optionally the groupname or GID for the specified command. </p>
<p> The followings examples are all valid:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;user&nbsp;[user | user:group | uid | uid:gid | user:gid | uid:group&nbsp;] </p>
<p> Without this argument the command will be run as root in the container. </p>
<p> <code>&#8211;ulimit</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Ulimit options </p>
<p> <code>-v</code>|<code>&#8211;volume</code>[=<i>[[HOST-DIR:]CONTAINER-DIR[:OPTIONS]]</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Create a bind mount. If you specify, -v&nbsp;/HOST-DIR:/CONTAINER-DIR, Docker<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;bind mounts&nbsp;/HOST-DIR in the host to&nbsp;/CONTAINER-DIR in the Docker<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;container. If&nbsp;&#8216;HOST-DIR&#8217;&nbsp;is omitted,&nbsp;<wbr>&nbsp;Docker automatically creates the new<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;volume on the host.&nbsp;<wbr>&nbsp;The OPTIONS are a comma delimited list and can be: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> [rw|ro]</p>
<dt>&bull;</p>
<dd> [z|Z]</p>
<dt>&bull;</p>
<dd> [[r]shared|[r]slave|[r]private]</p>
<dt>&bull;</p>
<dd> [delegated|cached|consistent]</p>
<dt>&bull;</p>
<dd> [nocopy] </p>
</dl>
</dl>
<p> The CONTAINER-DIR must be an absolute path such as /src/docs. The HOST-DIR can be an absolute path or a name value. A name value must start with an alphanumeric character, followed by a-z0-9, _ (underscore), . (period) or &#8211; (hyphen). An absolute path starts with a / (forward slash). </p>
<p> If you supply a HOST-DIR that is an absolute path, Docker bind-mounts to the path you specify. If you supply a name, Docker creates a named volume by that name. For example, you can specify either /foo or foo for a HOST-DIR value. If you supply the /foo value, Docker creates a bind mount. If you supply the foo specification, Docker creates a named volume. </p>
<p> You can specify multiple <code>-v</code> options to mount one or more mounts to a container. To use these same mounts in other containers, specify the <code>&#8211;volumes-from</code> option also. </p>
<p> You can supply additional options for each bind mount following an additional colon. A :ro or :rw suffix mounts a volume in read-only or read-write mode, respectively. By default, volumes are mounted in read-write mode. You can also specify the consistency requirement for the mount, either :consistent (the default), :cached, or :delegated. Multiple options are separated by commas, e.g. :ro,cached. </p>
<p> Labeling systems like SELinux require that proper labels are placed on volume content mounted into a container. Without a label, the security system might prevent the processes running inside the container from using the content. By default, Docker does not change the labels set by the OS. </p>
<p> To change a label in the container context, you can add either of two suffixes :z or :Z to the volume mount. These suffixes tell Docker to relabel file objects on the shared volumes. The z option tells Docker that two containers share the volume content. As a result, Docker labels the content with a shared content label. Shared volume labels allow all containers to read/write content. The Z option tells Docker to label the content with a private unshared label. Only the current container can use a private volume. </p>
<p> By default bind mounted volumes are private. That means any mounts done inside container will not be visible on host and vice-a-versa. One can change this behavior by specifying a volume mount propagation property. Making a volume shared mounts done under that volume inside container will be visible on host and vice-a-versa. Making a volume slave enables only one way mount propagation and that is mounts done on host under that volume will be visible inside container but not the other way around. </p>
<p> To control mount propagation property of volume one can use :[r]shared, :[r]slave or :[r]private propagation flag. Propagation property can be specified only for bind mounted volumes and not for internal volumes or named volumes. For mount propagation to work source mount point (mount point where source dir is mounted on) has to have right propagation properties. For shared volumes, source mount point has to be shared. And for slave volumes, source mount has to be either shared or slave. </p>
<p> Use df &lt;source-dir&gt; to figure out the source mount and then use findmnt -o TARGET,PROPAGATION &lt;source-mount-dir&gt; to figure out propagation properties of source mount. If findmnt utility is not available, then one can look at mount entry for source mount point in /proc/self/mountinfo. Look at optional fields and see if any propagation properties are specified. shared:X means mount is shared, master:X means mount is slave and if nothing is there that means mount is private. </p>
<p> To change propagation properties of a mount point use mount command. For example, if one wants to bind mount source directory /foo one can do mount &#8211;bind /foo /foo and mount &#8211;make-private &#8211;make-shared /foo. This will convert /foo into a shared mount point. Alternatively one can directly change propagation properties of source mount. Say / is source mount for /foo, then use mount &#8211;make-shared / to convert / into a shared mount. </p>
<dl>
<dt>
<dd>
<p> <code>Note</code>: When using systemd to manage the Docker daemon&#8217;s start and stop, in the systemd unit file there is an option to control mount propagation for the Docker daemon itself, called MountFlags. The value of this setting may cause Docker to not see mount propagation changes made on the mount point. For example, if this value is slave, you may not be able to use the shared or rshared propagation on a volume. </p>
</dl>
<p> To disable automatic copying of data from the container path to the volume, use the nocopy flag. The nocopy flag can be set on bind mounts and named volumes. </p>
<p> See also &#8211;mount, which is the successor of &#8211;tmpfs and &#8211;volume. Even though there is no plan to deprecate &#8211;volume, usage of &#8211;mount is recommended. </p>
<p> <code>&#8211;volume-driver</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Container&#8217;s volume driver. This driver creates volumes specified either from<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;a Dockerfile&#8217;s VOLUME instruction or from the docker run -v flag.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;See&nbsp;<code><a href="/docs/linux/man/1-docker-volume-create/">docker-volume-create</a>(1)</code>&nbsp;for full details. </p>
<p> <code>&#8211;volumes-from</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mount volumes from the specified container(s) </p>
<p> Mounts already mounted volumes from a source container onto another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;container. You must supply the source&#8217;s container-id. To share<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;a volume, use the&nbsp;<code>&#8211;volumes-from</code>&nbsp;option when running<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;the target container. You can share volumes even if the source container<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;is not running. </p>
<p> By default, Docker mounts the volumes in the same mode (read-write or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;read-only)&nbsp;as it is mounted in the source container. Optionally, you<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;can change this by suffixing the container-id with either the :ro or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;:rw keyword. </p>
<p> If the location of the volume from the source container overlaps with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;data residing on a target container, then the volume hides<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;that data on the target. </p>
<p> <code>-w</code>, <code>&#8211;workdir</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Working directory inside the container </p>
<p> The default working directory for running binaries within a container is the root directory (/). The developer can set a different default with the Dockerfile WORKDIR instruction. The operator can override the working directory by using the <code>-w</code> option. </p>
<h2>Exit Status</h2>
<p> The exit code from docker run gives information about why the container failed to run or why it exited. When docker run exits with a non-zero code, the exit codes follow the chroot standard, see below: </p>
<p> <i>125</i> if the error is with Docker daemon <i>itself</i> </p>
<dl>
<dt>
<dd>
<p>$ docker run&#8211; foo busybox;<br />
echo $ ?<br />
#flag provided but not defined : &#8211;foo<br />
       See &#8216;docker run &#8211;help&#8217;.125
</dl>
<p> <i>126</i> if the <i>contained command</i> cannot be invoked </p>
<dl>
<dt>
<dd>
<pre>
$ docker run busybox /etc; echo $?
# exec: &quot;/etc&quot;: permission denied
  docker: Error response from daemon: Contained command could not be invoked
  126
</pre>
</dl>
<p> <i>127</i> if the <i>contained command</i> cannot be found </p>
<dl>
<dt>
<dd>
<pre>
$ docker run busybox foo; echo $?
# exec: &quot;foo&quot;: executable file not found in $PATH
  docker: Error response from daemon: Contained command not found or does not exist
  127
</pre>
</dl>
<p> <i>Exit code</i> of <i>contained command</i> otherwise </p>
<dl>
<dt>
<dd>
<pre>
$ docker run busybox /bin/sh -c 'exit 3' 
# 3
</pre>
</dl>
<h2>EXAMPLES</h2>
<h2>Running container in read-only mode</h2>
<p> During container image development, containers often need to write to the image content. Installing packages into /usr, for example. In production, applications seldom need to write to the image. Container applications write to volumes if they need to write to file systems at all. Applications can be made more secure by running them in read-only mode using the &#8211;read-only switch. This protects the containers image from modification. Read only containers may still need to write temporary data. The best way to handle this is to mount tmpfs directories on /run and /tmp. </p>
<dl>
<dt>
<dd>
<pre>
# docker run --read-only --tmpfs /run --tmpfs /tmp -i -t fedora /bin/bash
</pre>
</dl>
<h2>Exposing log messages from the container to the host&#8217;s log</h2>
<p> If you want messages that are logged in your container to show up in the host&#8217;s syslog/journal then you should bind mount the /dev/log directory as follows. </p>
<dl>
<dt>
<dd>
<pre>
# docker run -v /dev/log:/dev/log -i -t fedora /bin/bash
</pre>
</dl>
<p> From inside the container you can test this by sending a message to the log. </p>
<dl>
<dt>
<dd>
<pre>
(bash)# logger &quot;Hello from my container&quot;
</pre>
</dl>
<p> Then exit and check the journal. </p>
<dl>
<dt>
<dd>
<pre>
# exit
# journalctl -b | grep Hello
</pre>
</dl>
<p> This should list the message sent to logger. </p>
<h2>Attaching to one or more from STDIN, STDOUT, STDERR</h2>
<p> If you do not specify -a then Docker will attach everything (stdin,stdout,stderr) you&#8217;d like to connect instead, as in: </p>
<dl>
<dt>
<dd>
<pre>
# docker run -a stdin -a stdout -i -t fedora /bin/bash
</pre>
</dl>
<h2>Sharing IPC between containers</h2>
<p> Using shm_server.c available here: <a rel="nofollow" href="https://www.cs.cf.ac.uk/Dave/C/node27.html">https://www.cs.cf.ac.uk/Dave/C/node27.html</a> </p>
<p> Testing &#8211;ipc=host mode: </p>
<p> Host shows a shared memory segment with 7 pids attached, happens to be from httpd: </p>
<dl>
<dt>
<dd>
<p>$ sudo ipcs &#8211; m&#8211; &#8212; &#8211;Shared Memory Segments&#8211; &#8212; &#8212; &#8211;key shmid owner perms bytes nattch status 0x01128e25 0 root 600 1000 7
</dl>
<p> Now run a regular container, and it correctly does NOT see the shared memory segment from the host: </p>
<dl>
<dt>
<dd>
<p>$ docker run &#8211; it shm ipcs &#8211; m&#8211; &#8212; &#8211;Shared Memory Segments&#8211; &#8212; &#8212; &#8211;key shmid owner perms bytes nattch status
</dl>
<p> Run a container with the new &#8211;ipc=host option, and it now sees the shared memory segment from the host httpd: </p>
<dl>
<dt>
<dd>
<p>$ docker run &#8211; it&#8211; ipc = host shm ipcs &#8211; m&#8211; &#8212; &#8211;Shared Memory Segments&#8211; &#8212; &#8212; &#8211;key shmid owner perms bytes nattch status 0x01128e25 0 root 600 1000 7
</dl>
<p> Testing &#8211;ipc=container:CONTAINERID mode: </p>
<p> Start a container with a program to create a shared memory segment: </p>
<dl>
<dt>
<dd>
<p>$ docker run &#8211; it shm bash $ sudo shm / shm_server &amp;$ sudo ipcs &#8211; m&#8211; &#8212; &#8211;Shared Memory Segments&#8211; &#8212; &#8212; &#8211;key shmid owner perms bytes nattch status 0x0000162e 0 root 666 27 1
</dl>
<p> Create a 2nd container correctly shows no shared memory segment from 1st container: </p>
<dl>
<dt>
<dd>
<p>$ docker run shm ipcs &#8211; m&#8211; &#8212; &#8211;Shared Memory Segments&#8211; &#8212; &#8212; &#8211;key shmid owner perms bytes nattch status
</dl>
<p> Create a 3rd container using the new &#8211;ipc=container:CONTAINERID option, now it shows the shared memory segment from the first: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker run - it-- ipc = container : ed735b2264ac shm ipcs - m $ sudo ipcs - m-- -- --Shared Memory Segments-- -- -- --key shmid owner perms bytes nattch status 0x0000162e 0 root 666 27 1
</code></pre>
</dl>
<h2>Linking Containers</h2>
<dl>
<dt>
<dd>
<p> <code>Note</code>: This section describes linking between containers on the default (bridge) network, also known as &quot;legacy links&quot;. Using &#8211;link on user-defined networks uses the DNS-based discovery, which does not add entries to /etc/hosts, and does not set environment variables for discovery. </p>
</dl>
<p> The link feature allows multiple containers to communicate with each other. For example, a container whose Dockerfile has exposed port 80 can be run and named as follows: </p>
<dl>
<dt>
<dd>
<pre>
# docker run --name=link-test -d -i -t fedora/httpd
</pre>
</dl>
<p> A second container, in this case called linker, can communicate with the httpd container, named link-test, by running with the <code>&#8211;link=:</code> </p>
<dl>
<dt>
<dd>
<pre>
# docker run -t -i --link=link-test:lt --name=linker fedora /bin/bash
</pre>
</dl>
<p> Now the container linker is linked to container link-test with the alias lt. Running the <code>env</code> command in the linker container shows environment variables<br />
&nbsp;with the LT&nbsp;(alias)&nbsp;context&nbsp;(<code>LT_</code>) </p>
<dl>
<dt>
<dd>
<pre>
# env
HOSTNAME=668231cb0978
TERM=xterm
LT_PORT_80_TCP=<a href="tcp://172.17.0.3:80">tcp://172.17.0.3:80</a>
LT_PORT_80_TCP_PORT=80
LT_PORT_80_TCP_PROTO=tcp
LT_PORT=<a href="tcp://172.17.0.3:80">tcp://172.17.0.3:80</a>
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/
LT_NAME=/linker/lt
SHLVL=1
HOME=/
LT_PORT_80_TCP_ADDR=172.17.0.3
_=/usr/bin/env
</pre>
</dl>
<p> When linking two containers Docker will use the exposed ports of the container to create a secure tunnel for the parent to access. </p>
<p> If a container is connected to the default bridge network and linked with other containers, then the container&#8217;s /etc/hosts file is updated with the linked container&#8217;s name. </p>
<dl>
<dt>
<dd>
<p> <code>Note</code> Since Docker may live update the container&#8217;s /etc/hosts file, there may be situations when processes inside the container can end up reading an empty or incomplete /etc/hosts file. In most cases, retrying the read again should fix the problem. </p>
</dl>
<h2>Mapping Ports for External Usage</h2>
<p> The exposed port of an application can be mapped to a host port using the <code>-p</code> flag. For example, an httpd port 80 can be mapped to the host port 8080 using the following: </p>
<dl>
<dt>
<dd>
<pre>
# docker run -p 8080:80 -d -i -t fedora/httpd
</pre>
</dl>
<h2>Creating and Mounting a Data Volume Container</h2>
<p> Many applications require the sharing of persistent data across several containers. Docker allows you to create a Data Volume Container that other containers can mount from. For example, create a named container that contains directories /var/volume1 and /tmp/volume2. The image will need to contain these directories so a couple of RUN mkdir instructions might be required for you fedora-data image: </p>
<dl>
<dt>
<dd>
<pre>
# docker run --name=data -v /var/volume1 -v /tmp/volume2 -i -t fedora-data true
# docker run --volumes-from=data --name=fedora-container1 -i -t fedora bash
</pre>
</dl>
<p> Multiple &#8211;volumes-from parameters will bring together multiple data volumes from multiple containers. And it&#8217;s possible to mount the volumes that came from the DATA container in yet another container via the fedora-container1 intermediary container, allowing to abstract the actual data source from users of that data: </p>
<dl>
<dt>
<dd>
<pre>
# docker run --volumes-from=fedora-container1 --name=fedora-container2 -i -t fedora bash
</pre>
</dl>
<h2>Mounting External Volumes</h2>
<p> To mount a host directory as a container volume, specify the absolute path to the directory and the absolute path for the container directory separated by a colon: </p>
<dl>
<dt>
<dd>
<pre>
# docker run -v /var/db:/data1 -i -t fedora bash
</pre>
</dl>
<p> When using SELinux, be aware that the host has no knowledge of container SELinux policy. Therefore, in the above example, if SELinux policy is enforced, the /var/db directory is not writable to the container. A &quot;Permission Denied&quot; message will occur and an avc: message in the host&#8217;s syslog. </p>
<p> To work around this, at time of writing this man page, the following command needs to be run in order for the proper SELinux policy type label to be attached to the host directory: </p>
<dl>
<dt>
<dd>
<pre>
# chcon -Rt svirt_sandbox_file_t /var/db
</pre>
</dl>
<p> Now, writing to the /data1 volume in the container will be allowed and the changes will also be reflected on the host in /var/db. </p>
<h2>Using alternative security labeling</h2>
<p> You can override the default labeling scheme for each container by specifying the &#8211;security-opt flag. For example, you can specify the MCS/MLS level, a requirement for MLS systems. Specifying the level in the following command allows you to share the same content between containers. </p>
<dl>
<dt>
<dd>
<pre>
# docker run --security-opt label=level:s0:c100,c200 -i -t fedora bash
</pre>
</dl>
<p> An MLS example might be: </p>
<dl>
<dt>
<dd>
<pre>
# docker run --security-opt label=level:TopSecret -i -t rhel7 bash
</pre>
</dl>
<p> To disable the security labeling for this container versus running with the &#8211;permissive flag, use the following command: </p>
<dl>
<dt>
<dd>
<pre>
# docker run --security-opt label=disable -i -t fedora bash
</pre>
</dl>
<p> If you want a tighter security policy on the processes within a container, you can specify an alternate type for the container. You could run a container that is only allowed to listen on Apache ports by executing the following command: </p>
<dl>
<dt>
<dd>
<pre>
# docker run --security-opt label=type:svirt_apache_t -i -t centos bash
</pre>
</dl>
<p> Note: </p>
<p> You would have to write policy defining a svirt_apache_t type. </p>
<h2>Setting device weight</h2>
<p> If you want to set /dev/sda device weight to 200, you can specify the device weight by &#8211;blkio-weight-device flag. Use the following command: </p>
<dl>
<dt>
<dd>
<pre>
# docker run -it --blkio-weight-device &quot;/dev/sda:200&quot; ubuntu
</pre>
</dl>
<h2>Specify isolation technology for container (&#8211;isolation)</h2>
<p> This option is useful in situations where you are running Docker containers on Microsoft Windows. The &#8211;isolation &lt;value&gt; option sets a container&#8217;s isolation technology. On Linux, the only supported is the default option which uses Linux namespaces. These two commands are equivalent on Linux: </p>
<dl>
<dt>
<dd>
<pre>
$ docker run -d busybox top
$ docker run -d --isolation default busybox top
</pre>
</dl>
<p> On Microsoft Windows, can take any of these values: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> default: Use the value specified by the Docker daemon&#8217;s &#8211;exec-opt . If the daemon does not specify an isolation technology, Microsoft Windows uses process as its default value.</p>
<dt>&bull;</p>
<dd> process: Namespace isolation only.</p>
<dt>&bull;</p>
<dd> hyperv: Hyper-V hypervisor partition-based isolation. </p>
</dl>
</dl>
<p> In practice, when running on Microsoft Windows without a daemon option set, these two commands are equivalent: </p>
<dl>
<dt>
<dd>
<pre>
$ docker run -d --isolation default busybox top
$ docker run -d --isolation process busybox top
</pre>
</dl>
<p> If you have set the &#8211;exec-opt isolation=hyperv option on the Docker daemon, any of these commands also result in hyperv isolation: </p>
<dl>
<dt>
<dd>
<pre>
$ docker run -d --isolation default busybox top
$ docker run -d --isolation hyperv busybox top
</pre>
</dl>
<h2>Setting Namespaced Kernel Parameters (Sysctls)</h2>
<p> The &#8211;sysctl sets namespaced kernel parameters (sysctls) in the container. For example, to turn on IP forwarding in the containers network namespace, run this command: </p>
<dl>
<dt>
<dd>
<pre>
$ docker run --sysctl net.ipv4.ip_forward=1 someimage
</pre>
</dl>
<p> Note: </p>
<p> Not all sysctls are namespaced. Docker does not support changing sysctls inside of a container that also modify the host system. As the kernel evolves we expect to see more sysctls become namespaced. </p>
<p> See the definition of the &#8211;sysctl option above for the current list of supported sysctls. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit SvenDowideit [at] home.org.au &lt;mailto:SvenDowideit [at] home.org.au&gt; July 2014, updated by Sven Dowideit SvenDowideit [at] home.org.au &lt;mailto:SvenDowideit [at] home.org.au&gt; November 2015, updated by Sally O&#8217;Malley somalley [at] redhat.com &lt;mailto:somalley [at] redhat.com&gt; </p>
<h2>Index</h2>
