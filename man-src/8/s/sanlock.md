---
title: "sanlock(8)"
name: "sanlock"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sanlock/"
description: "sanlock – shared storage lock manager"
---

<p>sanlock &#8211; shared storage lock manager</p>
<h2>Synopsis</h2>
<p><code>sanlock</code> [COMMAND] [ACTION] &#8230; </p>
<h2>Description</h2>
<p>sanlock is a lock manager built on shared storage. Hosts with access to the storage can perform locking. An application running on the hosts is given a small amount of space on the shared block device or file, and uses sanlock for its own application-specific synchronization. Internally, the sanlock daemon manages locks using two disk-based lease algorithms: delta leases and paxos leases.</p>
<dl>
<dt>&bull;</p>
<dd><i>delta leases</i> are slow to acquire and demand regular i/o to shared storage. sanlock only uses them internally to hold a lease on its &quot;host_id&quot; (an integer host identifier from 1-2000). They prevent two hosts from using the same host identifier. The delta lease renewals also indicate if a host is alive. (&quot;Light-Weight Leases for Storage-Centric Coordination&quot;, Chockler and Malkhi.)</p>
<dt>&bull;</p>
<dd><i>paxos leases</i> are fast to acquire and sanlock makes them available to applications as general purpose resource leases. The disk paxos algorithm uses host_id&#8217;s internally to represent different hosts, and the owner of a paxos lease. delta leases provide unique host_id&#8217;s for implementing paxos leases, and delta lease renewals serve as a proxy for paxos lease renewal. (&quot;Disk Paxos&quot;, Eli Gafni and Leslie Lamport.)  Externally, the sanlock daemon exposes a locking interface through libsanlock in terms of &quot;lockspaces&quot; and &quot;resources&quot;. A lockspace is a locking context that an application creates for itself on shared storage. When the application on each host is started, it &quot;joins&quot; the lockspace. It can then create &quot;resources&quot; on the shared storage. Each resource represents an application-specific entity. The application can acquire and release leases on resources. To use sanlock from an application:</p>
<dl>
<dt>&bull;</p>
<dd>Allocate shared storage for an application, e.g. a shared LUN or LV from a SAN, or files from NFS.</p>
<dt>&bull;</p>
<dd>Provide the storage to the application.</p>
<dt>&bull;</p>
<dd>The application uses this storage with libsanlock to create a lockspace and resources for itself.</p>
<dt>&bull;</p>
<dd>The application joins the lockspace when it starts.</p>
<dt>&bull;</p>
<dd>The application acquires and releases leases on resources.  How lockspaces and resources translate to delta leases and paxos leases within sanlock: <i>Lockspaces</i></p>
<dl>
<dt>&bull;</p>
<dd>A lockspace is based on delta leases held by each host using the lockspace.</p>
<dt>&bull;</p>
<dd>A lockspace is a series of 2000 delta leases on disk, and requires 1MB of storage.</p>
<dt>&bull;</p>
<dd>A lockspace can support up to 2000 concurrent hosts using it, each using a different delta lease.</p>
<dt>&bull;</p>
<dd>Applications can i) create, ii) join and iii) leave a lockspace, which corresponds to i) initializing the set of delta leases on disk, ii) acquiring one of the delta leases and iii) releasing the delta lease.</p>
<dt>&bull;</p>
<dd>When a lockspace is created, a unique lockspace name and disk location is provided by the application.</p>
<dt>&bull;</p>
<dd>When a lockspace is created/initialized, sanlock formats the sequence of 2000 on-disk delta lease structures on the file or disk, e.g. /mnt/leasefile (NFS) or /dev/vg/lv (SAN).</p>
<dt>&bull;</p>
<dd>The 2000 individual delta leases in a lockspace are identified by number: 1,2,3,&#8230;,2000.</p>
<dt>&bull;</p>
<dd>Each delta lease is a 512 byte sector in the 1MB lockspace, offset by its number, e.g. delta lease 1 is offset 0, delta lease 2 is offset 512, delta lease 2000 is offset 1023488.</p>
<dt>&bull;</p>
<dd>When an application joins a lockspace, it must specify the lockspace name, the lockspace location on shared disk/file, and the local host&#8217;s host_id. sanlock then acquires the delta lease corresponding to the host_id, e.g. joining the lockspace with host_id 1 acquires delta lease 1.</p>
<dt>&bull;</p>
<dd>The terms delta lease, lockspace lease, and host_id lease are used interchangably.</p>
<dt>&bull;</p>
<dd>sanlock acquires a delta lease by writing the host&#8217;s unique name to the delta lease disk sector, reading it back after a delay, and verifying it is the same.</p>
<dt>&bull;</p>
<dd>If a unique host name is not specified, sanlock generates a uuid to use as the host&#8217;s name. The delta lease algorithm depends on hosts using unique names.</p>
<dt>&bull;</p>
<dd>The application on each host should be configured with a unique host_id, where the host_id is an integer 1-2000.</p>
<dt>&bull;</p>
<dd>If hosts are misconfigured and have the same host_id, the delta lease algorithm is designed to detect this conflict, and only one host will be able to acquire the delta lease for that host_id.</p>
<dt>&bull;</p>
<dd>A delta lease ensures that a lockspace host_id is being used by a single host with the unique name specified in the delta lease.</p>
<dt>&bull;</p>
<dd>Resolving delta lease conflicts is slow, because the algorithm is based on waiting and watching for some time for other hosts to write to the same delta lease sector. If multiple hosts try to use the same delta lease, the delay is increased substantially. So, it is best to configure applications to use unique host_id&#8217;s that will not conflict.</p>
<dt>&bull;</p>
<dd>After sanlock acquires a delta lease, the lease must be renewed until the application leaves the lockspace (which corresponds to releasing the delta lease on the host_id.)</p>
<dt>&bull;</p>
<dd>sanlock renews delta leases every 20 seconds (by default) by writing a new timestamp into the delta lease sector.</p>
<dt>&bull;</p>
<dd>When a host acquires a delta lease in a lockspace, it can be referred to as &quot;joining&quot; the lockspace. Once it has joined the lockspace, it can use resources associated with the lockspace.  <i>Resources</i></p>
<dl>
<dt>&bull;</p>
<dd>A lockspace is a context for resources that can be locked and unlocked by an application.</p>
<dt>&bull;</p>
<dd>sanlock uses paxos leases to implement leases on resources. The terms paxos lease and resource lease are used interchangably.</p>
<dt>&bull;</p>
<dd>A paxos lease exists on shared storage and requires 1MB of space. It contains a unique resource name and the name of the lockspace.</p>
<dt>&bull;</p>
<dd>An application assigns its own meaning to a sanlock resource and the leases on it. A sanlock resource could represent some shared object like a file, or some unique role among the hosts.</p>
<dt>&bull;</p>
<dd>Resource leases are associated with a specific lockspace and can only be used by hosts that have joined that lockspace (they are holding a delta lease on a host_id in that lockspace.)</p>
<dt>&bull;</p>
<dd>An application must keep track of the disk locations of its lockspaces and resources. sanlock does not maintain any persistent index or directory of lockspaces or resources that have been created by applications, so applications need to remember where they have placed their own leases (which files or disks and offsets).</p>
<dt>&bull;</p>
<dd>sanlock does not renew paxos leases directly (although it could). Instead, the renewal of a host&#8217;s delta lease represents the renewal of all that host&#8217;s paxos leases in the associated lockspace. In effect, many paxos lease renewals are factored out into one delta lease renewal. This reduces i/o when many paxos leases are used.</p>
<dt>&bull;</p>
<dd>The disk paxos algorithm allows multiple hosts to all attempt to acquire the same paxos lease at once, and will produce a single winner/owner of the resource lease. (Shared resource leases are also possible in addition to the default exclusive leases.)</p>
<dt>&bull;</p>
<dd>The disk paxos algorithm involves a specific sequence of reading and writing the sectors of the paxos lease disk area. Each host has a dedicated 512 byte sector in the paxos lease disk area where it writes its own &quot;ballot&quot;, and each host reads the entire disk area to see the ballots of other hosts. The first sector of the disk area is the &quot;leader record&quot; that holds the result of the last paxos ballot. The winner of the paxos ballot writes the result of the ballot to the leader record (the winner of the ballot may have selected another contending host as the owner of the paxos lease.)</p>
<dt>&bull;</p>
<dd>After a paxos lease is acquired, no further i/o is done in the paxos lease disk area.</p>
<dt>&bull;</p>
<dd>Releasing the paxos lease involves writing a single sector to clear the current owner in the leader record.</p>
<dt>&bull;</p>
<dd>If a host holding a paxos lease fails, the disk area of the paxos lease still indicates that the paxos lease is owned by the failed host. If another host attempts to acquire the paxos lease, and finds the lease is held by another host_id, it will check the delta lease of that host_id. If the delta lease of the host_id is being renewed, then the paxos lease is owned and cannot be acquired. If the delta lease of the owner&#8217;s host_id has expired, then the paxos lease is expired and can be taken (by going through the paxos lease algorithm.)</p>
<dt>&bull;</p>
<dd>The &quot;interaction&quot; or &quot;awareness&quot; between hosts of each other is limited to the case where they attempt to acquire the same paxos lease, and need to check if the referenced delta lease has expired or not.</p>
<dt>&bull;</p>
<dd>When hosts do not attempt to lock the same resources concurrently, there is no host interaction or awareness. The state or actions of one host have no effect on others.</p>
<dt>&bull;</p>
<dd>To speed up checking delta lease expiration (in the case of a paxos lease conflict), sanlock keeps track of past renewals of other delta leases in the lockspace.  <i>Expiration</i></p>
<dl>
<dt>&bull;</p>
<dd>If a host fails to renew its delta lease, e.g. it looses access to the storage, its delta lease will eventually expire and another host will be able to take over any resource leases held by the host. sanlock must ensure that the application on two different hosts is not holding and using the same lease concurrently.</p>
<dt>&bull;</p>
<dd>When sanlock has failed to renew a delta lease for a period of time, it will begin taking measures to stop local processes (applications) from using any resource leases associated with the expiring lockspace delta lease. sanlock enters this &quot;recovery mode&quot; well ahead of the time when another host could take over the locally owned leases. sanlock must have sufficient time to stop all local processes that are using the expiring leases.</p>
<dt>&bull;</p>
<dd>sanlock uses three methods to stop local processes that are using expiring leases: 1. Graceful shutdown. sanlock will execute a &quot;graceful shutdown&quot; program that the application previously specified for this case. The shutdown program tells the application to shut down because its leases are expiring. The application must respond by stopping its activities and releasing its leases (or exit). If an application does not specify a graceful shutdown program, sanlock sends SIGTERM to the process instead. The process must release its leases or exit in a prescribed amount of time (see -g), or sanlock proceeds to the next method of stopping. 2. Forced shutdown. sanlock will send SIGKILL to processes using the expiring leases. The processes have a fixed amount of time to exit after receiving SIGKILL. If any do not exit in this time, sanlock will proceed to the next method. 3. Host reset. sanlock will trigger the host&#8217;s watchdog device to forcibly reset it. sanlock carefully manages the timing of the watchdog device so that it fires shortly before any other host could take over the resource leases held by local processes.  <i>Failures</i> If a process holding resource leases fails or exits without releasing its leases, sanlock will release the leases for it automatically (unless persistent resource leases were used.) If the sanlock daemon cannot renew a lockspace delta lease for a specific period of time (see Expiration), sanlock will enter &quot;recovery mode&quot; where it attempts to stop and/or kill any processes holding resource leases in the expiring lockspace. If the processes do not exit in time, sanlock will force the host to be reset using the local watchdog device. If the sanlock daemon crashes or hangs, it will not renew the expiry time of the per-lockspace connections it had to the wdmd daemon. This will lead to the expiration of the local watchdog device, and the host will be reset. <i>Watchdog</i> sanlock uses the <a href="/docs/linux/man/8-wdmd/">wdmd</a>(8) daemon to access /dev/watchdog. wdmd multiplexes multiple timeouts onto the single watchdog timer. This is required because delta leases for each lockspace are renewed and expire independently. sanlock maintains a wdmd connection for each lockspace delta lease being renewed. Each connection has an expiry time for some seconds in the future. After each successful delta lease renewal, the expiry time is renewed for the associated wdmd connection. If wdmd finds any connection expired, it will not renew the /dev/watchdog timer. Given enough successive failed renewals, the watchdog device will fire and reset the host. (Given the multiplexing nature of wdmd, shorter overlapping renewal failures from multiple lockspaces could cause spurious watchdog firing.) The direct link between delta lease renewals and watchdog renewals provides a predictable watchdog firing time based on delta lease renewal timestamps that are visible from other hosts. sanlock knows the time the watchdog on another host has fired based on the delta lease time. Furthermore, if the watchdog device on another host fails to fire when it should, the continuation of delta lease renewals from the other host will make this evident and prevent leases from being taken from the failed host. If sanlock is able to stop/kill all processing using an expiring lockspace, the associated wdmd connection for that lockspace is removed. The expired wdmd connection will no longer block /dev/watchdog renewals, and the host should avoid being reset. <i>Storage</i> On devices with 512 byte sectors, lockspaces and resources are 1MB in size. On devices with 4096 byte sectors, lockspaces and resources are 8MB in size. sanlock uses 512 byte sectors when shared files are used in place of shared block devices. Offsets of leases or resources must be multiples of 1MB/8MB according to the sector size. Using sanlock on shared block devices that do host based mirroring or replication is not likely to work correctly. When using sanlock on shared files, all sanlock io should go to one file server. <i>Example</i> This is an example of creating and using lockspaces and resources from the command line. (Most applications would use sanlock through libsanlock rather than through the command line.)</p>
<dl>
<dt>1.</p>
<dd>Allocate shared storage for sanlock leases. This example assumes 512 byte sectors on the device, in which case the lockspace needs 1MB and each resource needs 1MB. </p>
<pre># vgcreate vg /dev/sdb
# lvcreate -n leases -L 1GB vg</pre>
<dt>2.</p>
<dd>Start sanlock on all hosts. The -w 0 disables use of the watchdog for testing. </p>
<pre># sanlock daemon -w 0</pre>
<dt>3.</p>
<dd>Start a dummy application on all hosts. This sanlock command registers with sanlock, then execs the sleep command which inherits the registered fd. The sleep process acts as the dummy application. Because the sleep process is registered with sanlock, leases can be acquired for it. </p>
<pre># sanlock client command -c /bin/sleep 600 &amp;</pre>
<dt>4.</p>
<dd>Create a lockspace for the application (from one host). The lockspace is named &quot;test&quot;. </p>
<pre># sanlock client init -s test:0:/dev/test/leases:0</pre>
<dt>5.</p>
<dd>Join the lockspace for the application. Use a unique host_id on each host. </p>
<pre>host1:
# sanlock client add_lockspace -s test:1/dev/vg/leases:0
host2:
# sanlock client add_lockspace -s test:2/dev/vg/leases:0</pre>
<dt>6.</p>
<dd>Create two resources for the application (from one host). The resources are named &quot;RA&quot; and &quot;RB&quot;. Offsets are used on the same device as the lockspace. Different LVs or files could also be used. </p>
<pre># sanlock client init -r test:RA:/dev/vg/leases:1048576
# sanlock client init -r test:RB:/dev/vg/leases:2097152</pre>
<dt>7.</p>
<dd>Acquire resource leases for the application on host1. Acquire an exclusive lease (the default) on the first resource, and a shared lease (SH) on the second resource. </p>
<pre># export P=`pidof sleep`
# sanlock client acquire -r test:RA:/dev/vg/leases:1048576 -p $P
# sanlock client acquire -r test:RB:/dev/vg/leases:2097152:SH -p $P</pre>
<dt>8.</p>
<dd>Acquire resource leases for the application on host2. Acquiring the exclusive lease on the first resource will fail because it is held by host1. Acquiring the shared lease on the second resource will succeed. </p>
<pre># export P=`pidof sleep`
# sanlock client acquire -r test:RA:/dev/vg/leases:1048576 -p $P
# sanlock client acquire -r test:RB:/dev/vg/leases:2097152:SH -p $P</pre>
<dt>9.</p>
<dd>Release resource leases for the application on both hosts. The sleep pid could also be killed, which will result in the sanlock daemon releasing its leases when it exits. </p>
<pre># sanlock client release -r test:RA:/dev/vg/leases:1048576 -p $P
# sanlock client release -r test:RB:/dev/vg/leases:2097152 -p $P</pre>
<dt>10.</p>
<dd>Leave the lockspace for the application. </p>
<pre>host1:
# sanlock client rem_lockspace -s test:1/dev/vg/leases:0
host2:
# sanlock client rem_lockspace -s test:2/dev/vg/leases:0</pre>
<dt>11.</p>
<dd>Stop sanlock on all hosts. </p>
<pre># sanlock shutdown</pre>
<h2>Options</h2>
<p>COMMAND can be one of three primary top level choices </p>
<p> <code>sanlock daemon</code> start daemon<br />
 <code>sanlock client</code> send request to daemon (default command if none given)<br />
 <code>sanlock direct</code> access storage directly (no coordination with daemon)</p>
<h3>Daemon Command</h3>
<p><code>sanlock daemon</code> [options] </p>
<p> <code>-D</code> no fork and print all logging to stderr </p>
<p> <code>-Q</code> 0|1 quiet error messages for common lock contention </p>
<p> <code>-R</code> 0|1 renewal debugging, log debug info for each renewal </p>
<p> <code>-L</code><i> pri</i> write logging at priority level and up to logfile (-1 none) </p>
<p> <code>-S</code><i> pri</i> write logging at priority level and up to syslog (-1 none) </p>
<p> <code>-U</code><i> uid</i> user id </p>
<p> <code>-G</code><i> gid</i> group id </p>
<p> <code>-t</code><i> num</i> max worker threads </p>
<p> <code>-g</code><i> sec</i> seconds for graceful recovery </p>
<p> <code>-w</code> 0|1 use watchdog through wdmd </p>
<p> <code>-h</code> 0|1 use high priority (RR) scheduling </p>
<p> <code>-l</code><i> num</i> use mlockall (0 none, 1 current, 2 current and future) </p>
<p> <code>-b</code><i> sec</i> seconds a host id bit will remain set in delta lease bitmap </p>
<p> <code>-e</code><i> str</i> local host name used in delta leases</p>
<h3>Client Command</h3>
<p><code>sanlock client</code> <i>action</i> [options] </p>
<p> <code>sanlock client status</code> </p>
<p> Print processes, lockspaces, and resources being managed by the sanlock daemon. Add -D to show extra internal daemon status for debugging. Add -o p to show resources by pid, or -o s to show resources by lockspace. </p>
<p> <code>sanlock client host_status</code> </p>
<p> Print state of host_id delta leases read during the last renewal. State of all lockspaces is shown (use -s to select one). Add -D to show extra internal daemon status for debugging. </p>
<p> <code>sanlock client gets</code> </p>
<p> Print lockspaces being managed by the sanlock daemon. The LOCKSPACE string will be followed by ADD or REM if the lockspace is currently being added or removed. Add -h 1 to also show hosts in each lockspace. </p>
<p> <code>sanlock client renewal -s</code> LOCKSPACE </p>
<p> Print a history of renewals with timing details. </p>
<p> <code>sanlock client log_dump</code> </p>
<p> Print the sanlock daemon internal debug log. </p>
<p> <code>sanlock client shutdown</code> </p>
<p> Ask the sanlock daemon to exit. Without the force option (-f 0), the command will be ignored if any lockspaces exist. With the force option (-f 1), any registered processes will be killed, their resource leases released, and lockspaces removed. With the wait option (-w 1), the command will wait for a result from the daemon indicating that it has shut down and is exiting, or cannot shut down because lockspaces exist (command fails). </p>
<p> <code>sanlock client init -s</code> LOCKSPACE </p>
<p> Tell the sanlock daemon to initialize a lockspace on disk. The -o option can be used to specify the io timeout to be written in the host_id leases. (Also see sanlock direct init.) </p>
<p> <code>sanlock client init -r</code> RESOURCE </p>
<p> Tell the sanlock daemon to initialize a resource lease on disk. (Also see sanlock direct init.) </p>
<p> <code>sanlock client read -s</code> LOCKSPACE </p>
<p> Tell the sanlock daemon to read a lockspace from disk. Only the LOCKSPACE path and offset are required. If host_id is zero, the first record at offset (host_id 1) is used. The complete LOCKSPACE and io timeout are printed. </p>
<p> <code>sanlock client read -r</code> RESOURCE </p>
<p> Tell the sanlock daemon to read a resource lease from disk. Only the RESOURCE path and offset are required. The complete RESOURCE is printed. (Also see sanlock direct read_leader.) </p>
<p> <code>sanlock client align -s</code> LOCKSPACE </p>
<p> Tell the sanlock daemon to report the required lease alignment for a storage path. Only path is used from the LOCKSPACE argument. </p>
<p> <code>sanlock client add_lockspace -s</code> LOCKSPACE </p>
<p> Tell the sanlock daemon to acquire the specified host_id in the lockspace. This will allow resources to be acquired in the lockspace. The -o option can be used to specify the io timeout of the acquiring host, and will be written in the host_id lease. </p>
<p> <code>sanlock client inq_lockspace -s</code> LOCKSPACE </p>
<p> Inquire about the state of the lockspace in the sanlock daemon, whether it is being added or removed, or is joined. </p>
<p> <code>sanlock client rem_lockspace -s</code> LOCKSPACE </p>
<p> Tell the sanlock daemon to release the specified host_id in the lockspace. Any processes holding resource leases in this lockspace will be killed, and the resource leases not released. </p>
<p> <code>sanlock client command -r</code> RESOURCE <code>-c</code> <i>path</i> <i>args</i> </p>
<p> Register with the sanlock daemon, acquire the specified resource lease, and exec the command at path with args. When the command exits, the sanlock daemon will release the lease. -c must be the final option. </p>
<p> <code>sanlock client acquire -r</code> RESOURCE <code>-p</code> <i>pid</i><br />
 <code>sanlock client release -r</code> RESOURCE <code>-p</code> <i>pid</i> </p>
<p> Tell the sanlock daemon to acquire or release the specified resource lease for the given pid. The pid must be registered with the sanlock daemon. acquire can optionally take a versioned RESOURCE string RESOURCE:lver, where lver is the version of the lease that must be acquired, or fail. </p>
<p> <code>sanlock client convert -r</code> RESOURCE <code>-p</code> <i>pid</i> </p>
<p> Tell the sanlock daemon to convert the mode of the specified resource lease for the given pid. If the existing mode is exclusive (default), the mode of the lease can be converted to shared with RESOURCE:SH. If the existing mode is shared, the mode of the lease can be converted to exclusive with RESOURCE (no :SH suffix). </p>
<p> <code>sanlock client inquire -p</code><i> pid</i> </p>
<p> Print the resource leases held the given pid. The format is a versioned RESOURCE string &quot;RESOURCE:lver&quot; where lver is the version of the lease held. </p>
<p> <code>sanlock client request -r</code> RESOURCE <code>-f</code> <i>force_mode</i> </p>
<p> Request the owner of a resource do something specified by force_mode. A versioned RESOURCE:lver string must be used with a greater version than is presently held. Zero lver and force_mode clears the request. </p>
<p> <code>sanlock client examine -r</code> RESOURCE </p>
<p> Examine the request record for the currently held resource lease and carry out the action specified by the requested force_mode. </p>
<p> <code>sanlock client examine -s</code> LOCKSPACE </p>
<p> Examine requests for all resource leases currently held in the named lockspace. Only lockspace_name is used from the LOCKSPACE argument. </p>
<p> <code>sanlock client set_event -s</code> LOCKSPACE <code>-i</code> <i>host_id</i> <code>-g</code> <i>gen</i> <code>-e</code> <i>num</i> <code>-d</code> <i>num</i> </p>
<p> Set an event for another host. When the sanlock daemon next renews its delta lease for the lockspace it will: set the bit for the host_id in its bitmap, and set the generation, event and data values in its own delta lease. An application that has registered for events from this lockspace on the destination host will get the event that has been set when the destination sees the event during its next delta lease renewal. </p>
<p> <code>sanlock client set_config -s</code> LOCKSPACE </p>
<p> Set a configuration value for a lockspace. Only lockspace_name is used from the LOCKSPACE argument. The USED flag has the same effect on a lockspace as a process holding a resource lease that will not exit. The USED_BY_ORPHANS flag means that an orphan resource lease will have the same effect as the USED.<br />
 -u 0|1 Set (1) or clear (0) the USED flag.<br />
 -O 0|1 Set (1) or clear (0) the USED_BY_ORPHANS flag.</p>
<h3>Direct Command</h3>
<p><code>sanlock direct</code> <i>action</i> [options] </p>
<p> <code>-o</code><i> sec</i> io timeout in seconds </p>
<p> <code>sanlock direct init -s</code> LOCKSPACE<br />
 <code>sanlock direct init -r</code> RESOURCE </p>
<p> Initialize storage for 2000 host_id (delta) leases for the given lockspace, or initialize storage for one resource (paxos) lease. Both options require 1MB of space. The host_id in the LOCKSPACE string is not relevant to initialization, so the value is ignored. (The default of 2000 host_ids can be changed for special cases using the -n num_hosts and -m max_hosts options.) With -s, the -o option specifies the io timeout to be written in the host_id leases. </p>
<p> <code>sanlock direct read_leader -s</code> LOCKSPACE<br />
 <code>sanlock direct read_leader -r</code> RESOURCE </p>
<p> Read a leader record from disk and print the fields. The leader record is the single sector of a delta lease, or the first sector of a paxos lease. </p>
<p> <code>sanlock direct dump</code><i> path</i>[<code>:</code><i>offset</i>] </p>
<p> Read disk sectors and print leader records for delta or paxos leases. Add -f 1 to print the request record values for paxos leases, and host_ids set in delta lease bitmaps.</p>
<h3>LOCKSPACE option string</h3>
<p><code>-s</code> <i>lockspace_name</i>:<i>host_id</i>:<i>path</i>:<i>offset</i> </p>
<p> <i>lockspace_name</i> name of lockspace<br />
 <i>host_id</i> local host identifier in lockspace<br />
 <i>path</i> path to storage reserved for leases<br />
 <i>offset</i> offset on path (bytes)</p>
<h3>RESOURCE option string</h3>
<p><code>-r</code> <i>lockspace_name</i>:<i>resource_name</i>:<i>path</i>:<i>offset</i> </p>
<p> <i>lockspace_name</i> name of lockspace<br />
 <i>resource_name</i> name of resource<br />
 <i>path</i> path to storage reserved for leases<br />
 <i>offset</i> offset on path (bytes)</p>
<h3>RESOURCE option string with suffix</h3>
<p><code>-r</code> <i>lockspace_name</i>:<i>resource_name</i>:<i>path</i>:<i>offset</i>:<i>lver</i> </p>
<p> <i>lver</i> leader version </p>
<p> <code>-r</code> <i>lockspace_name</i>:<i>resource_name</i>:<i>path</i>:<i>offset</i>:SH </p>
<p> SH indicates shared mode</p>
<h3>Defaults</h3>
<p><code>sanlock help</code> shows the default values for the options above. </p>
<p> <code>sanlock version</code> shows the build version.</p>
<h2>Other</h2>
<h3>Request/Examine</h3>
<p>The first part of making a request for a resource is writing the request record of the resource (the sector following the leader record). To make a successful request:</p>
<dl>
<dt>&bull;</p>
<dd>RESOURCE:lver must be greater than the lver presently held by the other host. This implies the leader record must be read to discover the lver, prior to making a request.</p>
<dt>&bull;</p>
<dd>RESOURCE:lver must be greater than or equal to the lver presently written to the request record. Two hosts may write a new request at the same time for the same lver, in which case both would succeed, but the force_mode from the last would win.</p>
<dt>&bull;</p>
<dd>The force_mode must be greater than zero.</p>
<dt>&bull;</p>
<dd>To unconditionally clear the request record (set both lver and force_mode to 0), make request with RESOURCE:0 and force_mode 0. </p>
</dl>
<p> The owner of the requested resource will not know of the request unless it is explicitly told to examine its resources via the &quot;examine&quot; api/command, or otherwise notfied. </p>
<p> The second part of making a request is notifying the resource lease owner that it should examine the request records of its resource leases. The notification will cause the lease owner to automatically run the equivalent of &quot;sanlock client examine -s LOCKSPACE&quot; for the lockspace of the requested resource. </p>
<p> The notification is made using a bitmap in each host_id delta lease. Each bit represents each of the possible host_ids (1-2000). If host A wants to notify host B to examine its resources, A sets the bit in its own bitmap that corresponds to the host_id of B. When B next renews its delta lease, it reads the delta leases for all hosts and checks each bitmap to see if its own host_id has been set. It finds the bit for its own host_id set in A&#8217;s bitmap, and examines its resource request records. (The bit remains set in A&#8217;s bitmap for set_bitmap_seconds.) </p>
<p> <i>force_mode</i> determines the action the resource lease owner should take: </p>
<dl>
<dt>&bull;</p>
<dd>FORCE (1): kill the process holding the resource lease. When the process has exited, the resource lease will be released, and can then be acquired by anyone. The kill signal is SIGKILL (or SIGTERM if SIGKILL is restricted.) </p>
<dt>&bull;</p>
<dd>GRACEFUL (2): run the program configured by sanlock_killpath against the process holding the resource lease. If no killpath is defined, then FORCE is used. </p>
</dl>
<h3>Persistent and orphan resource leases</h3>
<p>A resource lease can be acquired with the PERSISTENT flag (-P 1). If the process holding the lease exits, the lease will not be released, but kept on an orphan list. Another local process can acquire an orphan lease using the ORPHAN flag (-O 1), or release the orphan lease using the ORPHAN flag (-O 1). All orphan leases can be released by setting the lockspace name (-s lockspace_name) with no resource name.</p>
<h2>Internals</h2>
<h3>Disk Format</h3>
<dl>
<dt>&bull;</p>
<dd>This example uses 512 byte sectors.</p>
<dt>&bull;</p>
<dd>Each lockspace is 1MB. It holds 2000 delta_leases, one per sector, supporting up to 2000 hosts.</p>
<dt>&bull;</p>
<dd>Each paxos_lease is 1MB. It is used as a lease for one resource.</p>
<dt>&bull;</p>
<dd>The leader_record structure is used differently by each lease type.</p>
<dt>&bull;</p>
<dd>To display all leader_record fields, see sanlock direct read_leader.</p>
<dt>&bull;</p>
<dd>A lockspace is often followed on disk by the paxos_leases used within that lockspace, but this layout is not required.</p>
<dt>&bull;</p>
<dd>The request_record and host_id bitmap are used for requests/events.</p>
<dt>&bull;</p>
<dd>The mode_block contains the SHARED flag indicating a lease is held in the shared mode.</p>
<dt>&bull;</p>
<dd>In a lockspace, the host using host_id N writes to a single delta_lease in sector N-1. No other hosts write to this sector. All hosts read all lockspace sectors when renewing their own delta_lease, and are able to monitor renewals of all delta_leases.</p>
<dt>&bull;</p>
<dd>In a paxos_lease, each host has a dedicated sector it writes to, containing its own paxos_dblock and mode_block structures. Its sector is based on its host_id; host_id 1 writes to the dblock/mode_block in sector 2 of the paxos_lease.</p>
<dt>&bull;</p>
<dd>The paxos_dblock structures are used by the paxos_lease algorithm, and the result is written to the leader_record. </p>
</dl>
<p> <code>0x000000 lockspace foo:0:/path:0</code> </p>
<p> (There is no representation on disk of the lockspace in general, only the sequence of specific delta_leases which collectively represent the lockspace.) </p>
<p> <code>delta_lease foo:1:/path:0</code> </p>
<pre>0x000 0 leader_record (sector 0, for host_id 1)
 magic: 0x12212010 
 space_name: foo
 resource_name: host uuid/name
 ...
 host_id bitmap (leader_record + 256)</pre>
<p><code>delta_lease foo:2:/path:0</code> </p>
<pre>0x200 512 leader_record (sector 1, for host_id 2)
 magic: 0x12212010
 space_name: foo
 resource_name: host uuid/name
 ...
 host_id bitmap (leader_record + 256)</pre>
<p><code>delta_lease foo:3:/path:0</code> </p>
<pre>0x400 1024 leader_record (sector 2, for host_id 3)
 magic: 0x12212010
 space_name: foo
 resource_name: host uuid/name
 ...
 host_id bitmap (leader_record + 256)</pre>
<p><code>delta_lease foo:2000:/path:0</code> </p>
<pre>0xF9E00 leader_record (sector 1999, for host_id 2000)
 magic: 0x12212010
 space_name: foo
 resource_name: host uuid/name
 ...
 host_id bitmap (leader_record + 256)</pre>
<p><code>0x100000 paxos_lease foo:example1:/path:1048576</code> </p>
<pre>0x000 0 leader_record (sector 0)
 magic: 0x06152010
 space_name: foo
 resource_name: example1
0x200 512 request_record (sector 1)
 magic: 0x08292011
0x400 1024 paxos_dblock (sector 2, for host_id 1)
0x480 1152 mode_block (paxos_dblock + 128)
0x600 1536 paxos_dblock (sector 3, for host_id 2)
0x680 1664 mode_block (paxos_dblock + 128)
0x800 2048 paxos_dblock (sector 4, for host_id 3)
0x880 2176 mode_block (paxos_dblock + 128)
0xFA200 paxos_dblock (sector 2001, for host_id 2000)
0xFA280 mode_block (paxos_dblock + 128)</pre>
<p><code>0x200000 paxos_lease foo:example2:/path:2097152</code> </p>
<pre>0x000 0 leader_record (sector 0)
 magic: 0x06152010
 space_name: foo
 resource_name: example2
0x200 512 request_record (sector 1)
 magic: 0x08292011
0x400 1024 paxos_dblock (sector 2, for host_id 1)
0x480 1152 mode_block (paxos_dblock + 128)
0x600 1536 paxos_dblock (sector 3, for host_id 2)
0x680 1664 mode_block (paxos_dblock + 128)
0x800 2048 paxos_dblock (sector 4, for host_id 3)
0x880 2176 mode_block (paxos_dblock + 128)
0xFA200 paxos_dblock (sector 2001, for host_id 2000)
0xFA280 mode_block (paxos_dblock + 128)</pre>
<h3>Lease ownership</h3>
<p>Not shown in the leader_record structures above are the owner_id, owner_generation and timestamp fields. These are the fields that define the lease owner. </p>
<p> The delta_lease at sector N for host_id N+1 has leader_record.owner_id N+1. The leader_record.owner_generation is incremented each time the delta_lease is acquired. When a delta_lease is acquired, the leader_record.timestamp field is set to the time of the host and the leader_record.resource_name is set to the unique name of the host. When the host renews the delta_lease, it writes a new leader_record.timestamp. When a host releases a delta_lease, it writes zero to leader_record.timestamp. </p>
<p> When a host acquires a paxos_lease, it uses the host_id/generation value from the delta_lease it holds in the lockspace. It uses this host_id/generation to identify itself in the paxos_dblock when running the paxos algorithm. The result of the algorithm is the winning host_id/generation &#8211; the new owner of the paxos_lease. The winning host_id/generation are written to the paxos_lease leader_record.owner_id and leader_record.owner_generation fields and leader_record.timestamp is set. When a host releases a paxos_lease, it sets leader_record.timestamp to 0. </p>
<p> When a paxos_lease is free (leader_record.timestamp is 0), multiple hosts may attempt to acquire it. The paxos algorithm, using the paxos_dblock structures, will select only one of the hosts as the new owner, and that owner is written in the leader_record. The paxos_lease will no longer be free (non-zero timestamp). Other hosts will see this and will not attempt to acquire the paxos_lease until it is free again. </p>
<p> If a paxos_lease is owned (non-zero timestamp), but the owner has not renewed its delta_lease for a specific length of time, then the owner value in the paxos_lease becomes expired, and other hosts will use the paxos algorithm to acquire the paxos_lease, and set a new owner.</p>
<h2>Files</h2>
<p>/etc/sanlock/sanlock.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wdmd/">wdmd</a></code>(8) </p>
