---
title: "nfstest-host(3)"
name: "nfstest-host"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nfstest-host/"
description: "nfstest.host – Host module"
---

<p>nfstest.host &#8211; Host module</p>
<h2>Description</h2>
<p>Provides a set of tools for running commands on the local host or a remote host, including a mechanism for running commands in the background. It provides methods for mounting and unmounting from an NFS server and a mechanism to simulate a network partition via the use of &#8216;iptables&#8217;. Currently, there is no mechanism to restore the iptables rules to their original state.</p>
<h2>Classes</h2>
<h3>class Host(baseobj.BaseObj)</h3>
<pre>Host object
Host() -&gt; New Host object
Usage:
 from nfstest.host import Host
 # Create host object for local host
 x = Host()
 # Create host object for remote host
 y = Host(host='192.168.0.11')
 # Run command to the local host
 x.run_cmd(&quot;ls -l&quot;)
 # Send command to the remote host and run it as root
 y.run_cmd(&quot;ls -l&quot;, sudo=True)
 # Run command in the background
 x.run_cmd(&quot;tcpdump&quot;, sudo=True, wait=False)
 ....
 ....
 # Stop command running in the background
 x.stop_cmd()
 # Mount volume using default options
 x.mount()
 # Unmount volume
 x.umount()
<code>Methods defined here:</code>
---------------------
<code>__del__(self)</code>
Destructor
Gracefully unmount volume and reset network.
<code>__init__(self, **kwargs)</code>
Constructor
Initialize object's private data.
<dl><dt><dd><dl><dt><code>host:</code>
<dd>Hostname or IP address [default: localhost]
<dt><code>user:</code>
<dd>User to log in to host [default: '']
<dt><code>server:</code>
<dd>NFS server name or IP address [default: None]
<dt><code>nfsversion:</code>
<dd>NFS version [default: 4.1]
<dt><code>proto:</code>
<dd>NFS protocol name [default: 'tcp']
<dt><code>port:</code>
<dd>NFS server port [default: 2049]
<dt><code>sec:</code>
<dd>Security flavor [default: 'sys']
<dt><code>export:</code>
<dd>Exported file system to mount [default: '/']
<dt><code>mtpoint:</code>
<dd>Mount point [default: '/mnt/t']
<dt><code>datadir:</code>
<dd>Data directory where files are created [default: '']
<dt><code>mtopts:</code>
<dd>Mount options [default: 'hard,rsize=4096,wsize=4096']
<dt><code>interface:</code>
<dd>Network device interface [default: 'eth0']
<dt><code>nomount:</code>
<dd>Debug option so the server is not actually mounted [default: False]
<dt><code>iptables:</code>
<dd>Iptables command [default: '/usr/sbin/iptables']
<dt><code>sudo:</code>
<dd>Sudo command [default: '/usr/bin/sudo']
</dl></dl>
<code>get_route(self, ipaddr)</code>
Get routing information for destination IP address
Returns a tuple: (gateway, device name, src IP address)
<code>mount(self, **kwargs)</code>
Mount the file system on the given mount point.
<dl><dt><dd><dl><dt><code>server:</code>
<dd>NFS server name or IP address [default: self.server]
<dt><code>nfsversion:</code>
<dd>NFS version [default: self.nfsversion]
<dt><code>proto:</code>
<dd>NFS protocol name [default: self.proto]
<dt><code>port:</code>
<dd>NFS server port [default: self.port]
<dt><code>sec:</code>
<dd>Security flavor [default: self.sec]
<dt><code>export:</code>
<dd>Exported file system to mount [default: self.export]
<dt><code>mtpoint:</code>
<dd>Mount point [default: self.mtpoint]
<dt><code>datadir:</code>
<dd>Data directory where files are created [default: self.datadir]
<dt><code>mtopts:</code>
<dd>Mount options [default: self.mtopts]
</dl></dl><dl><dt><dd>Return the mount point.
</dl>
<code>network_drop(self, ipaddr, port)</code>
Simulate a network drop by dropping all tcp packets going to the
given ipaddr and port using the iptables commands.
<code>network_reset(self)</code>
Reset the network by flushing all the chains in the table using
the iptables command.
<code>nfsstr(self, version=None)</code>
Return the NFS string for the given NFS version
<dl><dt><dd><dl><dt><code>version:</code>
<dd>NFS version, default is the object attribute nfsversion
</dl></dl>
<code>nfsvers(self, version=None)</code>
Return major and minor version for the given NFS version
<dl><dt><dd><dl><dt><code>version:</code>
<dd>NFS version, default is the object attribute nfsversion
</dl></dl>
<code>run_cmd(self, cmd, sudo=False, dlevel='DBG1', msg='', wait=True)</code>
Run the command to the remote machine using ssh.
There is no user authentication, so remote host must allow
ssh connection without any passwords for the user.
For a localhost the command is just executed and ssh is not used.
The object for the process of the command is stored in object
attribute 'self.process' to be used by methods wait_cmd() and
stop_cmd(). The standard output of the command is also stored
in the object attribute 'self.pstdout' while the standard error
output of the command is stored in 'self.pstderr'.
<dl><dt><dd><dl><dt><code>cmd:</code>
<dd>Command to execute
<dt><code>sudo:</code>
<dd>Run command using sudo if option is True
<dt><code>dlevel:</code>
<dd>Debug level for displaying the command to the user
<dt><code>msg:</code>
<dd>Prefix this message to the debug message to be displayed
<dt><code>wait:</code>
<dd>Wait for command to complete before returning
</dl></dl><dl><dt><dd>Return the standard output of the command and the return code or
exit status is stored in the object attribute 'self.returncode'.
</dl>
<code>stop_cmd(self, process=None, dlevel=None, msg='')</code>
Terminate command started by run_cmd() by calling wait_cmd()
with the 'terminate' option set to True.
<dl><dt><dd><dl><dt><code>process:</code>
<dd>The object for the process of the command to terminate,
or terminate all commands started by run_cmd() if this
option is not given
<dt><code>dlevel:</code>
<dd>Debug level for displaying the command to the user, default
is the level given by run_cmd()
<dt><code>msg:</code>
<dd>Prefix this message to the debug message to be displayed
</dl></dl><dl><dt><dd>Return the exit status of the last command
</dl>
<code>sudo_cmd(self, cmd)</code>
Prefix the SUDO command if effective user is not root.
<code>umount(self)</code>
Unmount the file system.
<code>wait_cmd(self, process=None, terminate=False, dlevel=None, msg='')</code>
Wait for command started by run_cmd() to finish.
<dl><dt><dd><dl><dt><code>process:</code>
<dd>The object for the process of the command to wait for,
or wait for all commands started by run_cmd() if this
option is not given
<dt><code>terminate:</code>
<dd>If True, send a signal to terminate the command or commands
and then wait for all commands to finish
<dt><code>dlevel:</code>
<dd>Debug level for displaying the command to the user, default
is the level given by run_cmd()
<dt><code>msg:</code>
<dd>Prefix this message to the debug message to be displayed
</dl></dl><dl><dt><dd>Return the exit status of the last command
</dl>
<code>Static methods defined here:</code>
----------------------------
<code>get_ip_address(host='', ipv6=False)</code>
Get IP address associated with the given host name.
This could be run as an instance or class method.</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
