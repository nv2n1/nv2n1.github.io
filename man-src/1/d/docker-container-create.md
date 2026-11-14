---
title: "docker-container-create(1)"
name: "docker-container-create"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-create/"
description: "docker-container-create – Create a new container"
---

<h2 class="name">NAME</h2>
<p> docker-container-create &#8211; Create a new container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container create [OPTIONS] IMAGE [COMMAND] [ARG&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Creates a writeable container layer over the specified image and prepares it for running the specified command. The container ID is then printed to STDOUT. This is similar to <code>docker run -d</code> except the container is never started. You can then use the <code>docker start </code> command to start the container at any point. </p>
<p> The initial status of the container created with <code>docker create</code> is &#8216;created&#8217;. </p>
<h3>OPTIONS</h3>
<p> The CONTAINER-DIR must be an absolute path such as /src/docs. The HOST-DIR can be an absolute path or a name value. A name value must start with an alphanumeric character, followed by a-z0-9, _ (underscore), . (period) or &#8211; (hyphen). An absolute path starts with a / (forward slash). </p>
<p> If you supply a HOST-DIR that is an absolute path, Docker bind-mounts to the path you specify. If you supply a name, Docker creates a named volume by that name. For example, you can specify either /foo or foo for a HOST-DIR value. If you supply the /foo value, Docker creates a bind mount. If you supply the foo specification, Docker creates a named volume. </p>
<p> You can specify multiple <code>-v</code> options to mount one or more mounts to a container. To use these same mounts in other containers, specify the <code>&#8211;volumes-from</code> option also. </p>
<p> You can supply additional options for each bind mount following an additional colon. A :ro or :rw suffix mounts a volume in read-only or read-write mode, respectively. By default, volumes are mounted in read-write mode.<br />
 You can also specify the consistency requirement for the mount, either :consistent (the default), :cached, or :delegated. Multiple options are separated by commas, e.g. :ro,cached. </p>
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
<p> To disable automatic copying of data from the container path to the volume, use the nocopy flag. The nocopy flag can be set on named volumes, and does not apply to bind mounts.. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;add-host</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add a custom host-to-IP mapping (host:ip)</p>
<p> <code>-a</code>, <code>&#8211;attach</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Attach to STDIN, STDOUT or STDERR</p>
<p> <code>&#8211;blkio-weight</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)</p>
<p> <code>&#8211;blkio-weight-device</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Block IO weight (relative device weight)</p>
<p> <code>&#8211;cap-add</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add Linux capabilities</p>
<p> <code>&#8211;cap-drop</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Drop Linux capabilities</p>
<p> <code>&#8211;cgroup-parent</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Optional parent cgroup for the container</p>
<p> <code>&#8211;cgroupns</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Cgroup namespace to use (host|private)</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default-cgroupns-mode option on the daemon&nbsp;(default) </p>
<p> <code>&#8211;cidfile</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Write the container ID to the file</p>
<p> <code>&#8211;cpu-count</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>CPU count (Windows only)</p>
<p> <code>&#8211;cpu-percent</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>CPU percent (Windows only)</p>
<p> <code>&#8211;cpu-period</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit CPU CFS (Completely Fair Scheduler) period</p>
<p> <code>&#8211;cpu-quota</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit CPU CFS (Completely Fair Scheduler) quota</p>
<p> <code>&#8211;cpu-rt-period</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit CPU real-time period in microseconds</p>
<p> <code>&#8211;cpu-rt-runtime</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit CPU real-time runtime in microseconds</p>
<p> <code>-c</code>, <code>&#8211;cpu-shares</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>CPU shares (relative weight)</p>
<p> <code>&#8211;cpus</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Number of CPUs</p>
<p> <code>&#8211;cpuset-cpus</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>CPUs in which to allow execution (0-3, 0,1)</p>
<p> <code>&#8211;cpuset-mems</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>MEMs in which to allow execution (0-3, 0,1)</p>
<p> <code>&#8211;device</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add a host device to the container</p>
<p> <code>&#8211;device-cgroup-rule</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add a rule to the cgroup allowed devices list</p>
<p> <code>&#8211;device-read-bps</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit read rate (bytes per second) from a device</p>
<p> <code>&#8211;device-read-iops</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit read rate (IO per second) from a device</p>
<p> <code>&#8211;device-write-bps</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit write rate (bytes per second) to a device</p>
<p> <code>&#8211;device-write-iops</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit write rate (IO per second) to a device</p>
<p> <code>&#8211;disable-content-trust</code>[=true] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Skip image verification</p>
<p> <code>&#8211;dns</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set custom DNS servers</p>
<p> <code>&#8211;dns-option</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set DNS options</p>
<p> <code>&#8211;dns-search</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set custom DNS search domains</p>
<p> <code>&#8211;domainname</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Container NIS domain name</p>
<p> <code>&#8211;entrypoint</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Overwrite the default ENTRYPOINT of the image</p>
<p> <code>-e</code>, <code>&#8211;env</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set environment variables</p>
<p> <code>&#8211;env-file</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Read in a file of environment variables</p>
<p> <code>&#8211;expose</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Expose a port or a range of ports</p>
<p> <code>&#8211;gpus</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>GPU devices to add to the container (&#8216;all&#8217; to pass all GPUs)</p>
<p> <code>&#8211;group-add</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add additional groups to join</p>
<p> <code>&#8211;health-cmd</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Command to run to check health</p>
<p> <code>&#8211;health-interval</code>=0s <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Time between running the check (ms|s|m|h) (default 0s)</p>
<p> <code>&#8211;health-retries</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Consecutive failures needed to report unhealthy</p>
<p> <code>&#8211;health-start-period</code>=0s <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Start period for the container to initialize before starting health-retries countdown (ms|s|m|h) (default 0s)</p>
<p> <code>&#8211;health-timeout</code>=0s <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Maximum time to allow one check to run (ms|s|m|h) (default 0s)</p>
<p> <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Print usage</p>
<p> <code>-h</code>, <code>&#8211;hostname</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Container host name</p>
<p> <code>&#8211;init</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Run an init inside the container that forwards signals and reaps processes</p>
<p> <code>-i</code>, <code>&#8211;interactive</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Keep STDIN open even if not attached</p>
<p> <code>&#8211;io-maxbandwidth</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Maximum IO bandwidth limit for the system drive (Windows only)</p>
<p> <code>&#8211;io-maxiops</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Maximum IOps limit for the system drive (Windows only)</p>
<p> <code>&#8211;ip</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>IPv4 address (e.g., 172.30.100.104)</p>
<p> <code>&#8211;ip6</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>IPv6 address (e.g., 2001:db8::33)</p>
<p> <code>&#8211;ipc</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>IPC mode to use</p>
<p> <code>&#8211;isolation</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Container isolation technology</p>
<p> <code>&#8211;kernel-memory</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Kernel memory limit</p>
<p> <code>-l</code>, <code>&#8211;label</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set meta data on a container</p>
<p> <code>&#8211;label-file</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Read in a line delimited file of labels</p>
<p> <code>&#8211;link</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add link to another container</p>
<p> <code>&#8211;link-local-ip</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Container IPv4/IPv6 link-local addresses</p>
<p> <code>&#8211;log-driver</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Logging driver for the container</p>
<p> <code>&#8211;log-opt</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Log driver options</p>
<p> <code>&#8211;mac-address</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Container MAC address (e.g., 92:d0:c6:0a:29:33)</p>
<p> <code>-m</code>, <code>&#8211;memory</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Memory limit</p>
<p> <code>&#8211;memory-reservation</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Memory soft limit</p>
<p> <code>&#8211;memory-swap</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Swap limit equal to memory plus swap: &#8216;-1&#8217; to enable unlimited swap</p>
<p> <code>&#8211;memory-swappiness</code>=-1 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Tune container memory swappiness (0 to 100)</p>
<p> <code>&#8211;mount</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Attach a filesystem mount to the container</p>
<p> <code>&#8211;name</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Assign a name to the container</p>
<p> <code>&#8211;network</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Connect a container to a network</p>
<p> <code>&#8211;network-alias</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add network-scoped alias for the container</p>
<p> <code>&#8211;no-healthcheck</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Disable any container-specified HEALTHCHECK</p>
<p> <code>&#8211;oom-kill-disable</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Disable OOM Killer</p>
<p> <code>&#8211;oom-score-adj</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Tune host&#8217;s OOM preferences (-1000 to 1000)</p>
<p> <code>&#8211;pid</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>PID namespace to use</p>
<p> <code>&#8211;pids-limit</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Tune container pids limit (set -1 for unlimited)</p>
<p> <code>&#8211;platform</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set platform if server is multi-platform capable</p>
<p> <code>&#8211;privileged</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Give extended privileges to this container</p>
<p> <code>-p</code>, <code>&#8211;publish</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Publish a container&#8217;s port(s) to the host</p>
<p> <code>-P</code>, <code>&#8211;publish-all</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Publish all exposed ports to random ports</p>
<p> <code>&#8211;pull</code>=&quot;missing&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pull image before creating (&quot;always&quot;|&quot;missing&quot;|&quot;never&quot;)</p>
<p> <code>&#8211;read-only</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Mount the container&#8217;s root filesystem as read only</p>
<p> <code>&#8211;restart</code>=&quot;no&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Restart policy to apply when a container exits</p>
<p> <code>&#8211;rm</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Automatically remove the container when it exits</p>
<p> <code>&#8211;runtime</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Runtime to use for this container</p>
<p> <code>&#8211;security-opt</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Security Options</p>
<p> <code>&#8211;shm-size</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Size of /dev/shm</p>
<p> <code>&#8211;stop-signal</code>=&quot;SIGTERM&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Signal to stop a container</p>
<p> <code>&#8211;stop-timeout</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Timeout (in seconds) to stop a container</p>
<p> <code>&#8211;storage-opt</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Storage driver options for the container</p>
<p> <code>&#8211;sysctl</code>=map[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Sysctl options</p>
<p> <code>&#8211;tmpfs</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Mount a tmpfs directory</p>
<p> <code>-t</code>, <code>&#8211;tty</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Allocate a pseudo-TTY</p>
<p> <code>&#8211;ulimit</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Ulimit options</p>
<p> <code>-u</code>, <code>&#8211;user</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Username or UID (format: [:])</p>
<p> <code>&#8211;userns</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>User namespace to use</p>
<p> <code>&#8211;uts</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>UTS namespace to use</p>
<p> <code>-v</code>, <code>&#8211;volume</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Bind mount a volume</p>
<p> <code>&#8211;volume-driver</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Optional volume driver for the container</p>
<p> <code>&#8211;volumes-from</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Mount volumes from the specified container(s)</p>
<p> <code>-w</code>, <code>&#8211;workdir</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Working directory inside the container</p>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre><code>
### Specify isolation technology for container (--isolation)
This option is useful in situations where you are running Docker containers on
Windows. The `--isolation=&lt;value&gt;` option sets a container's isolation
technology. On Linux, the only supported is the `default` option which uses
Linux namespaces. On Microsoft Windows, you can specify these values:
* `default`: Use the value specified by the Docker daemon's `--exec-opt` . If the `daemon` does not specify an isolation technology, Microsoft Windows uses `process` as its default value.
* `process`: Namespace isolation only.
* `hyperv`: Hyper-V hypervisor partition-based isolation.
Specifying the `--isolation` flag without a value is the same as setting `--isolation="default"`.
### Dealing with dynamically created devices (--device-cgroup-rule)
Devices available to a container are assigned at creation time. The
assigned devices will both be added to the cgroup.allow file and
created into the container once it is run. This poses a problem when
a new device needs to be added to running container.
One of the solution is to add a more permissive rule to a container
allowing it access to a wider range of devices. For example, supposing
our container needs access to a character device with major `42` and
any number of minor number (added as new devices appear), the
following rule would be added:
</code></pre>
</dl>
<p> docker create &#8211;device-cgroup-rule=&#8217;c 42:* rmw&#8217; -name my-container my-image </p>
<dl>
<dt>
<dd>
<pre>
Then, a user could ask `udev` to execute a script that would `docker exec my-container mknod newDevX c 42 &lt;minor&gt;`
the required device when it is added.
NOTE: initially present devices still need to be explicitly added to
the create/run command
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
