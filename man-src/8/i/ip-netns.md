---
title: "ip-netns(8)"
name: "ip-netns"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-netns/"
description: "ip-netns – process network namespace management"
---

<p>ip-netns &#8211; process network namespace management</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ]

netns

{ COMMAND |

    help }</code></pre>
<p> <code>ip netns</code> [ <code>list</code> ]<br />
 <code>ip netns add</code> <i>NETNSNAME</i><br />
 <code>ip netns attach</code> <i>NETNSNAME PID</i><br />
 <code>ip [-all] netns del</code> [ <i>NETNSNAME</i> ]<br />
 <code>ip netns set</code> <i>NETNSNAME NETNSID</i> </p>
<pre><code>NETNSID := auto | POSITIVE-INT</code></pre>
<p> <code>ip netns identify</code> [ <i>PID</i> ]<br />
 <code>ip netns pids</code> <i>NETNSNAME</i><br />
 <code>ip [-all] netns exec </code> [ <i>NETNSNAME</i> ] <i>command</i>&#8230;<br />
 <code>ip netns monitor</code><br />
 <code>ip netns list-id</code> [ target-nsid <i>POSITIVE-INT</i> ] [ nsid <i>POSITIVE-INT</i> ] </p>
<h2>Description</h2>
<p>A network namespace is logically another copy of the network stack, with its own routes, firewall rules, and network devices. By default a process inherits its network namespace from its parent. Initially all the processes share the same default network namespace from the init process. By convention a named network namespace is an object at <code>/run/netns/</code>NAME that can be opened. The file descriptor resulting from opening <code>/run/netns/</code>NAME refers to the specified network namespace. Holding that file descriptor open keeps the network namespace alive. The file descriptor can be used with the <code><a href="/docs/linux/man/2-setns/">setns</a>(2)</code> system call to change the network namespace associated with a task. For applications that are aware of network namespaces, the convention is to look for global network configuration files first in <code>/etc/netns/</code>NAME<code>/</code> then in <code>/etc/.</code> For example, if you want a different version of <code>/etc/resolv.conf</code> for a network namespace used to isolate your vpn you would name it <code>/etc/netns/myvpn/resolv.conf.</code> <code>ip netns exec</code> automates handling of this configuration, file convention for network namespace unaware applications, by creating a mount namespace and bind mounting all of the per network namespace configure files into their traditional location in /etc.</p>
<dl>
<dt><code>ip netns list &#8211; show all of the named network namespaces</code></p>
<dd>This command displays all of the network namespaces in /run/netns</p>
<dt><code>ip netns add NAME &#8211; create a new named network namespace</code></p>
<dd>If NAME is available in /run/netns this command creates a new network namespace and assigns NAME.</p>
<dt><code>ip netns attach NAME PID &#8211; create a new named network namespace</code></p>
<dd>If NAME is available in /run/netns this command attaches the network namespace of the process PID to NAME as if it were created with ip netns.</p>
<dt><code>ip [-all] netns delete [ NAME ] &#8211; delete the name of a network namespace(s)</code></p>
<dd>If NAME is present in /run/netns it is umounted and the mount point is removed. If this is the last user of the network namespace the network namespace will be freed and all physical devices will be moved to the default one, otherwise the network namespace persists until it has no more users. ip netns delete may fail if the mount point is in use in another mount namespace. If <code>-all</code> option was specified then all the network namespace names will be removed. It is possible to lose the physical device when it was moved to netns and then this netns was deleted with a running process:</p>
<dl>
<dd>$ ip netns add net0</dl>
<dl>
<dd>$ ip link set dev eth0 netns net0</dl>
<dl>
<dd>$ ip netns exec net0 SOME_PROCESS_IN_BACKGROUND</dl>
<dl>
<dd>$ ip netns del net0</dl>
<dl>
<dd>and eth0 will appear in the default netns only after SOME_PROCESS_IN_BACKGROUND will exit or will be killed. To prevent this the processes running in net0 should be killed before deleting the netns:</dl>
<dl>
<dd>$ ip netns pids net0 | xargs kill</dl>
<dl>
<dd>$ ip netns del net0</dl>
<dt><code>ip netns set NAME NETNSID &#8211; assign an id to a peer network namespace</code></p>
<dd>This command assigns a id to a peer network namespace. This id is valid only in the current network namespace. If the keyword &quot;auto&quot; is specified an available nsid will be chosen. This id will be used by the kernel in some netlink messages. If no id is assigned when the kernel needs it, it will be automatically assigned by the kernel. Once it is assigned, it&#8217;s not possible to change it.</p>
<dt><code>ip netns identify [PID] &#8211; Report network namespaces names for process</code></p>
<dd>This command walks through /run/netns and finds all the network namespace names for network namespace of the specified process, if PID is not specified then the current process will be used.</p>
<dt><code>ip netns pids NAME &#8211; Report processes in the named network namespace</code></p>
<dd>This command walks through proc and finds all of the process who have the named network namespace as their primary network namespace.</p>
<dt><code>ip [-all] netns exec [ NAME ] cmd &#8230; &#8211; Run cmd in the named network namespace</code></p>
<dd>This command allows applications that are network namespace unaware to be run in something other than the default network namespace with all of the configuration for the specified network namespace appearing in the customary global locations. A network namespace and bind mounts are used to move files from their network namespace specific location to their default locations without affecting other processes. If <code>-all</code> option was specified then <code>cmd</code> will be executed synchronously on the each named network namespace even if <code>cmd</code> fails on some of them. Network namespace name is printed on each <code>cmd</code> executing.</p>
<dt><code>ip netns monitor &#8211; Report as network namespace names are added and deleted</code></p>
<dd>This command watches network namespace name addition and deletion events and prints a line for each event it sees.</p>
<dt><code>ip netns list-id [target-nsid POSITIVE-INT] [nsid POSITIVE-INT] &#8211; list network namespace ids (nsid)</code></p>
<dd>Network namespace ids are used to identify a peer network namespace. This command displays nsids of the current network namespace and provides the corresponding iproute2 netns name (from /run/netns) if any. The <code>target-nsid</code> option enables to display nsids of the specified network namespace instead of the current network namespace. This <code>target-nsid</code> is a nsid from the current network namespace. The <code>nsid</code> option enables to display only this nsid. It is a nsid from the current network namespace. In combination with the <code>target-nsid</code> option, it enables to convert a specific nsid from the current network namespace to a nsid of the <code>target-nsid</code> network namespace. </p>
<h2>Examples</h2>
<p>ip netns list</p>
<dl>
<dd>Shows the list of current named network namespaces</dl>
<p> ip netns add vpn</p>
<dl>
<dd>Creates a network namespace and names it vpn</dl>
<p> ip netns exec vpn ip link set lo up</p>
<dl>
<dd>Bring up the loopback interface in the vpn network namespace.</dl>
<p> ip netns add foo<br />
 ip netns add bar<br />
 ip netns set foo 12<br />
 ip netns set bar 13<br />
 ip -n foo netns set foo 22<br />
 ip -n foo netns set bar 23<br />
 ip -n bar netns set foo 32<br />
 ip -n bar netns set bar 33<br />
 ip netns list-id target-nsid 12</p>
<dl>
<dd>Shows the list of nsids from the network namespace foo.</dl>
<p> ip netns list-id target-nsid 12 nsid 13</p>
<dl>
<dd>Get nsid of bar from the network namespace foo (result is 23).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Eric W. Biederman<br />
 Manpage revised by Nicolas Dichtel &lt;nicolas.dichtel [at] 6wind.com&gt;</p>
