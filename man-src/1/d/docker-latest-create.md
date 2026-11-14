---
title: "docker-latest-create(1)"
name: "docker-latest-create"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-create/"
description: "docker-create – Create a new container"
---

<h2 class="name">NAME</h2>
<p> docker-create &#8211; Create a new container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker create</code> [<code>-a</code>|<code>&#8211;attach</code>[=<i>[]</i>]] [<code>&#8211;add-host</code>[=<i>[]</i>]] [<code>&#8211;blkio-weight</code>[=<i>[BLKIO-WEIGHT]</i>]] [<code>&#8211;blkio-weight-device</code>[=<i>[]</i>]] [<code>&#8211;cpu-shares</code>[=<i>0</i>]] [<code>&#8211;cap-add</code>[=<i>[]</i>]] [<code>&#8211;cap-drop</code>[=<i>[]</i>]] [<code>&#8211;cgroup-parent</code>[=<i>CGROUP-PATH</i>]] [<code>&#8211;cidfile</code>[=<i>CIDFILE</i>]] [<code>&#8211;cpu-period</code>[=<i>0</i>]] [<code>&#8211;cpu-quota</code>[=<i>0</i>]] [<code>&#8211;cpuset-cpus</code>[=<i>CPUSET-CPUS</i>]] [<code>&#8211;cpuset-mems</code>[=<i>CPUSET-MEMS</i>]] [<code>&#8211;device</code>[=<i>[]</i>]] [<code>&#8211;device-read-bps</code>[=<i>[]</i>]] [<code>&#8211;device-read-iops</code>[=<i>[]</i>]] [<code>&#8211;device-write-bps</code>[=<i>[]</i>]] [<code>&#8211;device-write-iops</code>[=<i>[]</i>]] [<code>&#8211;dns</code>[=<i>[]</i>]] [<code>&#8211;dns-search</code>[=<i>[]</i>]] [<code>&#8211;dns-opt</code>[=<i>[]</i>]] [<code>-e</code>|<code>&#8211;env</code>[=<i>[]</i>]] [<code>&#8211;entrypoint</code>[=<i>ENTRYPOINT</i>]] [<code>&#8211;env-file</code>[=<i>[]</i>]] [<code>&#8211;expose</code>[=<i>[]</i>]] [<code>&#8211;group-add</code>[=<i>[]</i>]] [<code>-h</code>|<code>&#8211;hostname</code>[=<i>HOSTNAME</i>]] [<code>&#8211;help</code>] [<code>-i</code>|<code>&#8211;interactive</code>] [<code>&#8211;ip</code>[=<i>IPv4-ADDRESS</i>]] [<code>&#8211;ip6</code>[=<i>IPv6-ADDRESS</i>]] [<code>&#8211;ipc</code>[=<i>IPC</i>]] [<code>&#8211;isolation</code>[=<i>default</i>]] [<code>&#8211;kernel-memory</code>[=<i>KERNEL-MEMORY</i>]] [<code>-l</code>|<code>&#8211;label</code>[=<i>[]</i>]] [<code>&#8211;label-file</code>[=<i>[]</i>]] [<code>&#8211;link</code>[=<i>[]</i>]] [<code>&#8211;link-local-ip</code>[=<i>[]</i>]] [<code>&#8211;log-driver</code>[=<i>[]</i>]] [<code>&#8211;log-opt</code>[=<i>[]</i>]] [<code>-m</code>|<code>&#8211;memory</code>[=<i>MEMORY</i>]] [<code>&#8211;mac-address</code>[=<i>MAC-ADDRESS</i>]] [<code>&#8211;memory-reservation</code>[=<i>MEMORY-RESERVATION</i>]] [<code>&#8211;memory-swap</code>[=<i>LIMIT</i>]] [<code>&#8211;memory-swappiness</code>[=<i>MEMORY-SWAPPINESS</i>]] [<code>&#8211;name</code>[=<i>NAME</i>]] [<code>&#8211;network-alias</code>[=<i>[]</i>]] [<code>&#8211;network</code>[=<i>&quot;bridge&quot;</i>]] [<code>&#8211;oom-kill-disable</code>] [<code>&#8211;oom-score-adj</code>[=<i>0</i>]] [<code>-P</code>|<code>&#8211;publish-all</code>] [<code>-p</code>|<code>&#8211;publish</code>[=<i>[]</i>]] [<code>&#8211;pid</code>[=<i>[PID]</i>]] [<code>&#8211;userns</code>[=<i>[]</i>]] [<code>&#8211;pids-limit</code>[=<i>PIDS_LIMIT</i>]] [<code>&#8211;privileged</code>] [<code>&#8211;read-only</code>] [<code>&#8211;restart</code>[=<i>RESTART</i>]] [<code>&#8211;security-opt</code>[=<i>[]</i>]] [<code>&#8211;storage-opt</code>[=<i>[]</i>]] [<code>&#8211;stop-signal</code>[=<i>SIGNAL</i>]] [<code>&#8211;shm-size</code>[=<i>[]</i>]] [<code>&#8211;sysctl</code>[=<i>[]</i>]] [<code>-t</code>|<code>&#8211;tty</code>] [<code>&#8211;tmpfs</code>[=<i>[CONTAINER-DIR[:&lt;OPTIONS&gt;]</i>]] [<code>-u</code>|<code>&#8211;user</code>[=<i>USER</i>]] [<code>&#8211;ulimit</code>[=<i>[]</i>]] [<code>&#8211;uts</code>[=<i>[]</i>]] [<code>-v</code>|<code>&#8211;volume</code>[=<i>[[HOST-DIR:]CONTAINER-DIR[:OPTIONS]]</i>]] [<code>&#8211;volume-driver</code>[=<i>DRIVER</i>]] [<code>&#8211;volumes-from</code>[=<i>[]</i>]] [<code>-w</code>|<code>&#8211;workdir</code>[=<i>WORKDIR</i>]] IMAGE [COMMAND] [ARG&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Creates a writeable container layer over the specified image and prepares it for running the specified command. The container ID is then printed to STDOUT. This is similar to <code>docker run -d</code> except the container is never started. You can then use the <code>docker start &lt;container_id&gt;</code> command to start the container at any point. </p>
<p> The initial status of the container created with <code>docker create</code> is &#8216;created&#8217;. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;attach</code>=[]<br />
Attach to STDIN, STDOUT or STDERR. </p>
<p> <code>&#8211;add-host</code>=[]<br />
Add a custom host-to-IP mapping&nbsp;<wbr>(host:ip) </p>
<p> <code>&#8211;blkio-weight</code>=<i>0</i><br />
Block IO weight&nbsp;<wbr>(relative weight)&nbsp;<wbr>accepts a weight value between 10 and 1000. </p>
<p> <code>&#8211;blkio-weight-device</code>=[]<br />
Block IO weight&nbsp;<wbr>(relative device weight, format: DEVICE_NAME:WEIGHT). </p>
<p> <code>&#8211;cpu-shares</code>=<i>0</i><br />
CPU shares&nbsp;<wbr>(relative weight) </p>
<p> <code>&#8211;cap-add</code>=[]<br />
Add Linux capabilities </p>
<p> <code>&#8211;cap-drop</code>=[]<br />
Drop Linux capabilities </p>
<p> <code>&#8211;cgroup-parent</code>=&quot;&quot;<br />
Path to cgroups under which the cgroup for the container will be created. If the path is not absolute, the path is considered to be relative to the cgroups path of the init process. Cgroups will be created if they do not already exist. </p>
<p> <code>&#8211;cidfile</code>=&quot;&quot;<br />
Write the container ID to the file </p>
<p> <code>&#8211;cpu-period</code>=<i>0</i><br />
&nbsp;<wbr>Limit the CPU CFS&nbsp;<wbr>(Completely Fair Scheduler)&nbsp;<wbr>period </p>
<p> <code>&#8211;cpuset-cpus</code>=&quot;&quot;<br />
CPUs in which to allow execution&nbsp;<wbr>(0-3, 0,1) </p>
<p> <code>&#8211;cpuset-mems</code>=&quot;&quot;<br />
Memory nodes&nbsp;<wbr>(MEMs)&nbsp;<wbr>in which to allow execution&nbsp;<wbr>(0-3, 0,1). Only effective on NUMA systems. </p>
<p> If you have four memory nodes on your system (0-3), use &#8211;cpuset-mems=0,1 then processes in your Docker container will only use memory from the first two memory nodes. </p>
<p> <code>&#8211;cpu-quota</code>=<i>0</i><br />
Limit the CPU CFS&nbsp;<wbr>(Completely Fair Scheduler)&nbsp;<wbr>quota </p>
<p> <code>&#8211;device</code>=[]<br />
Add a host device to the container&nbsp;<wbr>(e.g. &#8211;device=/dev/sdc:/dev/xvdc:rwm) </p>
<p> <code>&#8211;device-read-bps</code>=[]<br />
&nbsp;<wbr>Limit read rate&nbsp;<wbr>(bytes per second)&nbsp;<wbr>from a device&nbsp;<wbr>(e.g. &#8211;device-read-bps=/dev/sda:1mb) </p>
<p> <code>&#8211;device-read-iops</code>=[]<br />
&nbsp;<wbr>Limit read rate&nbsp;<wbr>(IO per second)&nbsp;<wbr>from a device&nbsp;<wbr>(e.g. &#8211;device-read-iops=/dev/sda:1000) </p>
<p> <code>&#8211;device-write-bps</code>=[]<br />
&nbsp;<wbr>Limit write rate&nbsp;<wbr>(bytes per second)&nbsp;<wbr>to a device&nbsp;<wbr>(e.g. &#8211;device-write-bps=/dev/sda:1mb) </p>
<p> <code>&#8211;device-write-iops</code>=[]<br />
&nbsp;<wbr>Limit write rate&nbsp;<wbr>(IO per second)&nbsp;<wbr>to a device&nbsp;<wbr>(e.g. &#8211;device-write-iops=/dev/sda:1000) </p>
<p> <code>&#8211;dns</code>=[]<br />
Set custom DNS servers </p>
<p> <code>&#8211;dns-opt</code>=[]<br />
Set custom DNS options </p>
<p> <code>&#8211;dns-search</code>=[]<br />
Set custom DNS search domains&nbsp;<wbr>(Use &#8211;dns-search=. if you don&#8217;t wish to set the search domain) </p>
<p> <code>-e</code>, <code>&#8211;env</code>=[]<br />
Set environment variables </p>
<p> <code>&#8211;entrypoint</code>=&quot;&quot;<br />
Overwrite the default ENTRYPOINT of the image </p>
<p> <code>&#8211;env-file</code>=[]<br />
Read in a line-delimited file of environment variables </p>
<p> <code>&#8211;expose</code>=[]<br />
Expose a port or a range of ports&nbsp;<wbr>(e.g. &#8211;expose=3300-3310)&nbsp;<wbr>from the container without publishing it to your host </p>
<p> <code>&#8211;group-add</code>=[]<br />
Add additional groups to run as </p>
<p> <code>-h</code>, <code>&#8211;hostname</code>=&quot;&quot;<br />
Container host name </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-i</code>, <code>&#8211;interactive</code>=<i>true</i>|<i>false</i><br />
Keep STDIN open even if not attached. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;ip</code>=&quot;&quot;<br />
Sets the container&#8217;s interface IPv4 address&nbsp;<wbr>(e.g. 172.23.0.9) </p>
<p> It can only be used in conjunction with <code>&#8211;net</code> for user-defined networks </p>
<p> <code>&#8211;ip6</code>=&quot;&quot;<br />
Sets the container&#8217;s interface IPv6 address&nbsp;<wbr>(e.g. 2001:db8::1b99) </p>
<p> It can only be used in conjunction with <code>&#8211;net</code> for user-defined networks </p>
<p> <code>&#8211;ipc</code>=&quot;&quot;<br />
Default is to create a private IPC namespace&nbsp;<wbr>(POSIX SysV IPC)&nbsp;<wbr>for the container<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;container:&lt;name|id&gt;&#8217;: reuses another container shared memory, semaphores and message queues<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;host&#8217;: use the host shared memory,semaphores and message queues inside the container.&nbsp;<wbr>&nbsp;<wbr>Note: the host mode gives the container full access to local shared memory and is therefore considered insecure. </p>
<p> <code>&#8211;isolation</code>=&quot;<i>default</i>&quot;<br />
Isolation specifies the type of isolation technology used by containers. Note that the default on Windows server is process, and the default on Windows client is hyperv. Linux only supports default. </p>
<p> <code>&#8211;kernel-memory</code>=&quot;&quot;<br />
Kernel memory limit&nbsp;<wbr>(format:&nbsp;<wbr>&lt;number&gt;[&lt;unit&gt;], where unit&nbsp;<wbr>=&nbsp;<wbr>b, k, m or g) </p>
<p> Constrains the kernel memory available to a container. If a limit of 0 is specified (not using &#8211;kernel-memory), the container&#8217;s kernel memory is not limited. If you specify a limit, it may be rounded up to a multiple of the operating system&#8217;s page size and the value can be very large, millions of trillions. </p>
<p> <code>-l</code>, <code>&#8211;label</code>=[]<br />
Adds metadata to a container&nbsp;<wbr>(e.g., &#8211;label=com.example.key=value) </p>
<p> <code>&#8211;label-file</code>=[]<br />
Read labels from a file. Delimit each label with an EOL. </p>
<p> <code>&#8211;link</code>=[]<br />
Add link to another container in the form of&nbsp;<wbr>&lt;name or id&gt;:alias or just<br />
&lt;name or id&gt;&nbsp;<wbr>in which case the alias will match the name. </p>
<p> <code>&#8211;link-local-ip</code>=[]<br />
Add one or more link-local IPv4/IPv6 addresses to the container&#8217;s interface </p>
<p> <code>&#8211;log-driver</code>=&quot;<i>json-file</i>|<i>syslog</i>|<i>journald</i>|<i>gelf</i>|<i>fluentd</i>|<i>awslogs</i>|<i>splunk</i>|<i>etwlogs</i>|<i>gcplogs</i>|<i>none</i>&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>Logging driver for the container. Default is defined by daemon &#8211;log-driver flag.<br />
&nbsp;<wbr>&nbsp;<wbr><code>Warning</code>: the docker logs command works only for the json-file and<br />
&nbsp;<wbr>&nbsp;<wbr>journald logging drivers. </p>
<p> <code>&#8211;log-opt</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>Logging driver specific options. </p>
<p> <code>-m</code>, <code>&#8211;memory</code>=&quot;&quot;<br />
Memory limit&nbsp;<wbr>(format:&nbsp;<wbr>&lt;number&gt;[&lt;unit&gt;], where unit&nbsp;<wbr>=&nbsp;<wbr>b, k, m or g) </p>
<p> Allows you to constrain the memory available to a container. If the host supports swap memory, then the <code>-m</code> memory setting can be larger than physical RAM. If a limit of 0 is specified (not using <code>-m</code>), the container&#8217;s memory is not limited. The actual limit may be rounded up to a multiple of the operating system&#8217;s page size (the value would be very large, that&#8217;s millions of trillions). </p>
<p> <code>&#8211;mac-address</code>=&quot;&quot;<br />
Container MAC address&nbsp;<wbr>(e.g. 92:d0:c6:0a:29:33) </p>
<p> <code>&#8211;memory-reservation</code>=&quot;&quot;<br />
Memory soft limit&nbsp;<wbr>(format:&nbsp;<wbr>&lt;number&gt;[&lt;unit&gt;], where unit&nbsp;<wbr>=&nbsp;<wbr>b, k, m or g) </p>
<p> After setting memory reservation, when the system detects memory contention or low memory, containers are forced to restrict their consumption to their reservation. So you should always set the value below <code>&#8211;memory</code>, otherwise the hard limit will take precedence. By default, memory reservation will be the same as memory limit. </p>
<p> <code>&#8211;memory-swap</code>=&quot;LIMIT&quot;<br />
A limit value equal to memory plus swap. Must be used with the&nbsp;<wbr>&nbsp;<wbr><code>-m</code> (<code>&#8211;memory</code>) flag. The swap LIMIT should always be larger than <code>-m</code> (<code>&#8211;memory</code>) value. </p>
<p> The format of LIMIT is &lt;number&gt;[&lt;unit&gt;]. Unit can be b (bytes), k (kilobytes), m (megabytes), or g (gigabytes). If you don&#8217;t specify a unit, b is used. Set LIMIT to -1 to enable unlimited swap. </p>
<p> <code>&#8211;memory-swappiness</code>=&quot;&quot;<br />
Tune a container&#8217;s memory swappiness behavior. Accepts an integer between 0 and 100. </p>
<p> <code>&#8211;name</code>=&quot;&quot;<br />
Assign a name to the container </p>
<p> <code>&#8211;net</code>=&quot;<i>bridge</i>&quot;<br />
Set the Network mode for the container<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;bridge&#8217;: create a network stack on the default Docker bridge<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;none&#8217;: no networking<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;container:&lt;name|id&gt;&#8217;: reuse another container&#8217;s network stack<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;host&#8217;: use the Docker host network stack.&nbsp;<wbr>&nbsp;<wbr>Note: the host mode gives the container full access to local system services such as D-bus and is therefore considered insecure.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;&lt;network-name&gt;|&lt;network-id&gt;&#8217;: connect to a user-defined network </p>
<p> <code>&#8211;network-alias</code>=[]<br />
Add network-scoped alias for the container </p>
<p> <code>&#8211;oom-kill-disable</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>Whether to disable OOM Killer for the container or not. </p>
<p> <code>&#8211;oom-score-adj</code>=&quot;&quot;<br />
&nbsp;<wbr>Tune the host&#8217;s OOM preferences for containers&nbsp;<wbr>(accepts -1000 to 1000) </p>
<p> <code>-P</code>, <code>&#8211;publish-all</code>=<i>true</i>|<i>false</i><br />
Publish all exposed ports to random ports on the host interfaces. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>-p</code>, <code>&#8211;publish</code>=[]<br />
Publish a container&#8217;s port, or a range of ports, to the host<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>format: ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort | containerPort<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Both hostPort and containerPort can be specified as a range of ports.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>When specifying ranges for both, the number of container ports in the range must match the number of host ports in the range.&nbsp;<wbr>(e.g., -p 1234-1236:1234-1236/tcp)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(use&nbsp;<wbr>&#8216;docker port&#8217;&nbsp;<wbr>to see the actual mapping) </p>
<p> <code>&#8211;pid</code>=&quot;&quot;<br />
Set the PID mode for the container<br />
Default is to create a private PID namespace for the container<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;container:&lt;name|id&gt;&#8217;: join another container&#8217;s PID namespace<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;host&#8217;: use the host&#8217;s PID namespace for the container. Note: the host mode gives the container full access to local PID and is therefore considered insecure. </p>
<p> <code>&#8211;userns</code>=&quot;&quot;<br />
Set the usernamespace mode for the container when userns-remap option is enabled.<br />
&nbsp;<wbr>&nbsp;<wbr><code>host</code>: use the host usernamespace and enable all privileged options&nbsp;<wbr>(e.g., pid=host or &#8211;privileged). </p>
<p> <code>&#8211;pids-limit</code>=&quot;&quot;<br />
Tune the container&#8217;s pids limit. Set -1 to have unlimited pids for the container. </p>
<p> <code>&#8211;privileged</code>=<i>true</i>|<i>false</i><br />
Give extended privileges to this container. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;read-only</code>=<i>true</i>|<i>false</i><br />
Mount the container&#8217;s root filesystem as read only. </p>
<p> <code>&#8211;restart</code>=&quot;<i>no</i>&quot;<br />
Restart policy to apply when a container exits&nbsp;<wbr>(no, on-failure[:max-retry], always, unless-stopped). </p>
<p> <code>&#8211;shm-size</code>=&quot;&quot;<br />
Size of&nbsp;<wbr>/dev/shm. The format is&nbsp;<wbr>&lt;number&gt;&lt;unit&gt;. number must be greater than 0.<br />
Unit is optional and can be b&nbsp;<wbr>(bytes), k&nbsp;<wbr>(kilobytes), m&nbsp;<wbr>(megabytes), or g&nbsp;<wbr>(gigabytes). If you omit the unit, the system uses bytes.<br />
If you omit the size entirely, the system uses 64m. </p>
<p> <code>&#8211;security-opt</code>=[]<br />
Security Options </p>
<p> &quot;label:user:USER&quot; : Set the label user for the container<br />
&nbsp;<wbr>&quot;label:role:ROLE&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Set the label role for the container<br />
&nbsp;<wbr>&quot;label:type:TYPE&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Set the label type for the container<br />
&nbsp;<wbr>&quot;label:level:LEVEL&quot;&nbsp;<wbr>: Set the label level for the container<br />
&nbsp;<wbr>&quot;label:disable&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Turn off label confinement for the container<br />
&nbsp;<wbr>&quot;no-new-privileges&quot;&nbsp;<wbr>: Disable container processes from gaining additional privileges<br />
&nbsp;<wbr>&quot;seccomp:unconfined&quot;&nbsp;<wbr>: Turn off seccomp confinement for the container<br />
&nbsp;<wbr>&quot;seccomp:profile.json :&nbsp;<wbr>&nbsp;<wbr>White listed syscalls seccomp Json file to be used as a seccomp filter </p>
<p> <code>&#8211;storage-opt</code>=[]<br />
Storage driver options per container </p>
<p> $ docker create -it &#8211;storage-opt size=120G fedora /bin/bash </p>
<p> This (size) will allow to set the container rootfs size to 120G at creation time. User cannot pass a size less than the Default BaseFS Size.<br />
This option is only available for the devicemapper, btrfs, and zfs graph drivers. </p>
<p> <code>&#8211;stop-signal</code>=<i>SIGTERM</i><br />
&nbsp;<wbr>&nbsp;<wbr>Signal to stop a container. Default is SIGTERM. </p>
<p> <code>&#8211;sysctl</code>=SYSCTL<br />
&nbsp;<wbr>&nbsp;<wbr>Configure namespaced kernel parameters at runtime </p>
<p> IPC Namespace &#8211; current sysctls allowed: </p>
<p> kernel.msgmax, kernel.msgmnb, kernel.msgmni, kernel.sem, kernel.shmall, kernel.shmmax, kernel.shmmni, kernel.shm_rmid_forced<br />
&nbsp;<wbr>&nbsp;<wbr>Sysctls beginning with fs.mqueue.* </p>
<p> Note: if you use &#8211;ipc=host using these sysctls will not be allowed. </p>
<p> Network Namespace &#8211; current sysctls allowed:<br />
Sysctls beginning with net.* </p>
<p> Note: if you use &#8211;net=host using these sysctls will not be allowed. </p>
<p> <code>-t</code>, <code>&#8211;tty</code>=<i>true</i>|<i>false</i><br />
Allocate a pseudo-TTY. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;tmpfs</code>=[] Create a tmpfs mount </p>
<p> Mount a temporary filesystem (tmpfs) mount into a container, for example: </p>
<p> $ docker run -d &#8211;tmpfs /tmp:rw,size=787448k,mode=1777 my_image </p>
<p> This command mounts a tmpfs at /tmp within the container. The supported mount options are the same as the Linux default mount flags. If you do not specify any options, the systems uses the following options: rw,noexec,nosuid,nodev,size=65536k. </p>
<p> <code>-u</code>, <code>&#8211;user</code>=&quot;&quot;<br />
Username or UID </p>
<p> <code>&#8211;ulimit</code>=[]<br />
Ulimit options </p>
<p> <code>&#8211;uts</code>=<i>host</i><br />
Set the UTS mode for the container<br />
&nbsp;<wbr>&nbsp;<wbr><code>host</code>: use the host&#8217;s UTS namespace inside the container.<br />
&nbsp;<wbr>&nbsp;<wbr>Note: the host mode gives the container access to changing the host&#8217;s hostname and is therefore considered insecure. </p>
<p> <code>-v</code>|<code>&#8211;volume</code>[=<i>[[HOST-DIR:]CONTAINER-DIR[:OPTIONS]]</i>]<br />
Create a bind mount. If you specify, -v&nbsp;<wbr>/HOST-DIR:/CONTAINER-DIR, Docker<br />
bind mounts&nbsp;<wbr>/HOST-DIR in the host to&nbsp;<wbr>/CONTAINER-DIR in the Docker<br />
container. If&nbsp;<wbr>&#8216;HOST-DIR&#8217;&nbsp;<wbr>is omitted,&nbsp;<wbr>&nbsp;<wbr>Docker automatically creates the new<br />
volume on the host.&nbsp;<wbr>&nbsp;<wbr>The OPTIONS are a comma delimited list and can be:</p>
<dl>
<dt>step]</p>
<dd>
<p> item [rw|ro] item [z|Z] item [[r]shared|[r]slave|[r]private]</dl>
<p> The CONTAINER-DIR must be an absolute path such as /src/docs. The HOST-DIR can be an absolute path or a name value. A name value must start with an alphanumeric character, followed by a-z0-9, _ (underscore), . (period) or &#8211; (hyphen). An absolute path starts with a / (forward slash). </p>
<p> If you supply a HOST-DIR that is an absolute path, Docker bind-mounts to the path you specify. If you supply a name, Docker creates a named volume by that name. For example, you can specify either /foo or foo for a HOST-DIR value. If you supply the /foo value, Docker creates a bind-mount. If you supply the foo specification, Docker creates a named volume. </p>
<p> You can specify multiple <code>-v</code> options to mount one or more mounts to a container. To use these same mounts in other containers, specify the <code>&#8211;volumes-from</code> option also. </p>
<p> You can add :ro or :rw suffix to a volume to mount it read-only or read-write mode, respectively. By default, the volumes are mounted read-write. See examples. </p>
<p> Labeling systems like SELinux require that proper labels are placed on volume content mounted into a container. Without a label, the security system might prevent the processes running inside the container from using the content. By default, Docker does not change the labels set by the OS. </p>
<p> To change a label in the container context, you can add either of two suffixes :z or :Z to the volume mount. These suffixes tell Docker to relabel file objects on the shared volumes. The z option tells Docker that two containers share the volume content. As a result, Docker labels the content with a shared content label. Shared volume labels allow all containers to read/write content. The Z option tells Docker to label the content with a private unshared label. Only the current container can use a private volume. </p>
<p> By default bind mounted volumes are private. That means any mounts done inside container will not be visible on host and vice-a-versa. One can change this behavior by specifying a volume mount propagation property. Making a volume shared mounts done under that volume inside container will be visible on host and vice-a-versa. Making a volume slave enables only one way mount propagation and that is mounts done on host under that volume will be visible inside container but not the other way around. </p>
<p> To control mount propagation property of volume one can use :[r]shared, :[r]slave or :[r]private propagation flag. Propagation property can be specified only for bind mounted volumes and not for internal volumes or named volumes. For mount propagation to work source mount point (mount point where source dir is mounted on) has to have right propagation properties. For shared volumes, source mount point has to be shared. And for slave volumes, source mount has to be either shared or slave. </p>
<p> Use df &lt;source-dir&gt; to figure out the source mount and then use findmnt -o TARGET,PROPAGATION &lt;source-mount-dir&gt; to figure out propagation properties of source mount. If findmnt utility is not available, then one can look at mount entry for source mount point in /proc/self/mountinfo. Look at optional fields and see if any propagaion properties are specified. shared:X means mount is shared, master:X means mount is slave and if nothing is there that means mount is private. </p>
<p> To change propagation properties of a mount point use mount command. For example, if one wants to bind mount source directory /foo one can do mount &#8211;bind /foo /foo and mount &#8211;make-private &#8211;make-shared /foo. This will convert /foo into a shared mount point. Alternatively one can directly change propagation properties of source mount. Say / is source mount for /foo, then use mount &#8211;make-shared / to convert / into a shared mount. </p>
<dl>
<dt>
<dd>
<p> <code>Note</code>: When using systemd to manage the Docker daemon&#8217;s start and stop, in the systemd unit file there is an option to control mount propagation for the Docker daemon itself, called MountFlags. The value of this setting may cause Docker to not see mount propagation changes made on the mount point. For example, if this value is slave, you may not be able to use the shared or rshared propagation on a volume.</dl>
<p> To disable automatic copying of data from the container path to the volume, use the nocopy flag. The nocopy flag can be set on bind mounts and named volumes. </p>
<p> <code>&#8211;volume-driver</code>=&quot;&quot;<br />
Container&#8217;s volume driver. This driver creates volumes specified either from<br />
a Dockerfile&#8217;s VOLUME instruction or from the docker run -v flag.<br />
See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-volume-create/">docker-volume-create</a>(1)</code>&nbsp;<wbr>for full details. </p>
<p> <code>&#8211;volumes-from</code>=[]<br />
Mount volumes from the specified container(s) </p>
<p> <code>-w</code>, <code>&#8211;workdir</code>=&quot;&quot;<br />
Working directory inside the container </p>
<h2>EXAMPLES</h2>
<h2>Specify isolation technology for container (&#8211;isolation)</h2>
<p> This option is useful in situations where you are running Docker containers on Windows. The &#8211;isolation=&lt;value&gt; option sets a container&#8217;s isolation technology. On Linux, the only supported is the default option which uses Linux namespaces. On Microsoft Windows, you can specify these values:</p>
<dl>
<dt>step]</p>
<dd>
<p> item default: Use the value specified by the Docker daemon&#8217;s &#8211;exec-opt . If the daemon does not specify an isolation technology, Microsoft Windows uses process as its default value. item process: Namespace isolation only. item hyperv: Hyper-V hypervisor partition-based isolation.</dl>
<p> Specifying the &#8211;isolation flag without a value is the same as setting &#8211;isolation=&quot;default&quot;. </p>
<h2>HISTORY</h2>
<p> August 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; September 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; November 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
