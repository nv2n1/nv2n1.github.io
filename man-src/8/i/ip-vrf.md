---
title: "ip-vrf(8)"
name: "ip-vrf"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-vrf/"
description: "ip-vrf – run a command against a vrf"
---

<p>ip-vrf &#8211; run a command against a vrf</p>
<h2>Synopsis</h2>
<pre><code>ip

vrf

{ COMMAND |

    help }
</code></pre>
<p> <code>ip vrf show</code> [ <i>NAME</i> ]<br />
 <code>ip vrf identify</code> [ <i>PID</i> ]<br />
 <code>ip vrf pids</code> <i>NAME</i><br />
 <code>ip vrf exec </code> [ <i>NAME</i> ] <i>command</i>&#8230; </p>
<h2>Description</h2>
<p>A VRF provides traffic isolation at layer 3 for routing, similar to how a VLAN is used to isolate traffic at layer 2. Fundamentally, a VRF is a separate routing table. Network devices are associated with a VRF by enslaving the device to the VRF. At that point network addresses assigned to the device are local to the VRF with host and connected routes moved to the table associated with the VRF. A process can specify a VRF using several APIs &#8212; binding the socket to the VRF device using SO_BINDTODEVICE, setting the VRF association using IP_UNICAST_IF or IPV6_UNICAST_IF, or specifying the VRF for a specific message using IP_PKTINFO or IPV6_PKTINFO. By default a process is not bound to any VRF. An association can be set explicitly by making the program use one of the APIs mentioned above or implicitly using a helper to set SO_BINDTODEVICE for all IPv4 and IPv6 sockets (AF_INET and AF_INET6) when the socket is created. This ip-vrf command is a helper to run a command against a specific VRF with the VRF association inherited parent to child.</p>
<dl>
<dt><code>ip vrf show [ NAME ] &#8211; Show all configured VRF</code></p>
<dd>This command lists all VRF and their corresponding table ids. If NAME is given, then only that VRF and table id is shown. The latter command is useful for scripting where the table id for a VRF is needed.</p>
<dt><code>ip vrf exec [ NAME ] cmd &#8230; &#8211; Run cmd against the named VRF</code></p>
<dd>This command allows applications that are VRF unaware to be run against a VRF other than the default VRF (main table). A command can be run against the default VRF by passing the &quot;default&quot; as the VRF name. This is useful if the current shell is associated with another VRF (e.g, Management VRF). This command requires the system to be booted with cgroup v2 (e.g. with systemd, add systemd.unified_cgroup_hierarchy=1 to the kernel command line). This command also requires to be ran as root or with the CAP_SYS_ADMIN, CAP_NET_ADMIN and CAP_DAC_OVERRIDE capabilities. If built with libcap and if capabilities are added to the ip binary program via setcap, the program will drop them as the first thing when invoked, unless the command is vrf exec.<br />
 NOTE: capabilities will NOT be dropped if CAP_NET_ADMIN is set to INHERITABLE to avoid breaking programs with ambient capabilities that call ip. Do not set the INHERITABLE flag on the ip binary itself.</p>
<dt><code>ip vrf identify [PID] &#8211; Report VRF association for process</code></p>
<dd>This command shows the VRF association of the specified process. If PID is not specified then the id of the current process is used.</p>
<dt><code>ip vrf pids NAME &#8211; Report processes associated with the named VRF</code></p>
<dd>This command shows all process ids that are associated with the given VRF. </p>
<h2>Caveats</h2>
<p>This command requires a kernel compiled with CGROUPS and CGROUP_BPF enabled. </p>
<p> The VRF helper *only* affects network layer sockets.</p>
<h2>Examples</h2>
<p>ip vrf exec red ssh 10.100.1.254</p>
<dl>
<dd>Executes ssh to 10.100.1.254 against the VRF red table.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-ip-link/">ip-link</a></code>(8), <code><a href="/docs/linux/man/8-ip-address/">ip-address</a></code>(8), <code><a href="/docs/linux/man/8-ip-route/">ip-route</a></code>(8), <code><a href="/docs/linux/man/8-ip-neighbor/">ip-neighbor</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by David Ahern</p>
