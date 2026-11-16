---
title: "fence_xvmd(8)"
name: "fence_xvmd"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_xvmd/"
description: "fence_xvmd – Libvirt-based, general purpose fencing host for virtual machines."
---

<p>fence_xvmd &#8211; Libvirt-based, general purpose fencing host for virtual machines.</p>
<h2>Synopsis</h2>
<p><code>fence_xvmd</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_xvmd is an I/O Fencing host which resides on bare metal machines and is used in conjunction with the fence_xvm fencing agent. Together, these two programs can be used to fence can be used machines which are part of a cluster. If the virtual machines are backed by clustered storage or the virtual machines may be migrated to other physical machines, all physical machines in question must also be a part of their own CMAN/OpenAIS based cluster. Furthermore, the bare metal cluster is required to have fencing configured if virtual machine recovery is expected to be automatic. fence_xvmd accepts options on the command line and from cluster.conf </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></dt>
<dd>Foreground mode (do not fork)</dd>
<dt><code>-d</code></dt>
<dd>Enable debugging output. The more times you specify this parameter, the more debugging output you will receive.</dd>
<dt><code>-i</code> <i>family</i></dt>
<dd>IP family to use (auto, ipv4, or ipv6; default = auto)</dd>
<dt><code>-a</code> <i>address</i></dt>
<dd>Multicast address to listen on (default=225.0.0.12 for ipv4, ff02::3:1 for ipv6)</dd>
<dt><code>-p</code> <i>port</i></dt>
<dd>Port to use (default=1229)</dd>
<dt><code>-I</code> <i>interface</i></dt>
<dd>Network interface to listen on, e.g. eth0.</dd>
<dt><code>-C</code> <i>auth</i></dt>
<dd>Authentication type (none, sha1, sha256, sha512; default=sha256). This controls the authentication mechanism used to authenticate clients. The three SHA hashes use a key which must be shared between both the virtual machines and the host machine or cluster. The three SHA authentication mechanisms use a simple bidirectional challenge-response based on pseudo- random number generation and a shared private key.</dd>
<dt><code>-c</code> <i>hash</i></dt>
<dd>Packet hash type (none, sha1, sha256, sha512; default=sha256). This controls the hashing mechanism used to authenticate fencing requests. The three SHA hashes use a key which must be shared between both the virtual machines and the host machine or cluster.</dd>
<dt><code>-k</code> <i>key_file</i></dt>
<dd>Use the specified key file for packet hashing / SHA authentication. When both the hash type and the authentication type are set to &quot;none&quot;, this parameter is ignored.</dd>
<dt><code>-u</code></dt>
<dd>Fence by UUID instead of virtual machine name.</dd>
<dt><code>-?</code></dt>
<dd>Print out a help message describing available options, then exit.</dd>
<dt><code>-h</code></dt>
<dd>Print out a help message describing available options, then exit.</dd>
<dt><code>-X</code></dt>
<dd>Do not connect to CCS for configuration; only use command line parameters. CCS configuration parameters override command line parameters (because they are cluster-wide), so if you need to override a configuration option contained in CCS, you must specify this parameter.</dd>
<dt><code>-L</code></dt>
<dd>Local-only / non-cluster mode. When used with -X, this this option prevents fence_xvmd from operating as a clustered service, obviating the need to configure/run CMAN on the host domain.</dd>
<dt><code>-U</code> <i>uri</i></dt>
<dd>Force use of the specified URI for connecting to the hypervisor.</dd>
<dt><code>-V</code></dt>
<dd>Print out a version message, then exit. </dd>
</dl>
<h2>Ccs Parameters</h2>
<p>CCS options are simply attributes of the &lt;fence_xvmd&gt; tag, a child of the &lt;cluster&gt; tag in /etc/cluster/cluster.conf.</p>
<dl>
<dt><i>debug=&quot;1&quot;</i></dt>
<dd>Same as the -d option. Specify numbers &gt;1 for more debugging information.</dd>
<dt><i>family=&quot;param&quot;</i></dt>
<dd>Same as the -i option.</dd>
<dt><i>multicast_address=&quot;param&quot;</i></dt>
<dd>Same as the -a option.</dd>
<dt><i>port=&quot;param&quot;</i></dt>
<dd>Same as the -p option.</dd>
<dt><i>auth=&quot;param&quot;</i></dt>
<dd>Same as the -C option.</dd>
<dt><i>hash=&quot;param&quot;</i></dt>
<dd>Same as the -c option.</dd>
<dt><i>key_file=&quot;param&quot;</i></dt>
<dd>Same as the -k option.</dd>
<dt><i>use_uuid=&quot;1&quot;</i></dt>
<dd>Same as the -u option.</dd>
<dd></dd></dl>
<h2>See Also</h2>
<p>fence(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8), <a href="/docs/linux/man/8-fence_xvm/">fence_xvm</a>(8) </p>
