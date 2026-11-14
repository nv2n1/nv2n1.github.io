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
<dt><code>-f</code></p>
<dd>Foreground mode (do not fork)</p>
<dt><code>-d</code></p>
<dd>Enable debugging output. The more times you specify this parameter, the more debugging output you will receive.</p>
<dt><code>-i</code> <i>family</i></p>
<dd>IP family to use (auto, ipv4, or ipv6; default = auto)</p>
<dt><code>-a</code> <i>address</i></p>
<dd>Multicast address to listen on (default=225.0.0.12 for ipv4, ff02::3:1 for ipv6)</p>
<dt><code>-p</code> <i>port</i></p>
<dd>Port to use (default=1229)</p>
<dt><code>-I</code> <i>interface</i></p>
<dd>Network interface to listen on, e.g. eth0.</p>
<dt><code>-C</code> <i>auth</i></p>
<dd>Authentication type (none, sha1, sha256, sha512; default=sha256). This controls the authentication mechanism used to authenticate clients. The three SHA hashes use a key which must be shared between both the virtual machines and the host machine or cluster. The three SHA authentication mechanisms use a simple bidirectional challenge-response based on pseudo- random number generation and a shared private key.</p>
<dt><code>-c</code> <i>hash</i></p>
<dd>Packet hash type (none, sha1, sha256, sha512; default=sha256). This controls the hashing mechanism used to authenticate fencing requests. The three SHA hashes use a key which must be shared between both the virtual machines and the host machine or cluster.</p>
<dt><code>-k</code> <i>key_file</i></p>
<dd>Use the specified key file for packet hashing / SHA authentication. When both the hash type and the authentication type are set to &quot;none&quot;, this parameter is ignored.</p>
<dt><code>-u</code></p>
<dd>Fence by UUID instead of virtual machine name.</p>
<dt><code>-?</code></p>
<dd>Print out a help message describing available options, then exit.</p>
<dt><code>-h</code></p>
<dd>Print out a help message describing available options, then exit.</p>
<dt><code>-X</code></p>
<dd>Do not connect to CCS for configuration; only use command line parameters. CCS configuration parameters override command line parameters (because they are cluster-wide), so if you need to override a configuration option contained in CCS, you must specify this parameter.</p>
<dt><code>-L</code></p>
<dd>Local-only / non-cluster mode. When used with -X, this this option prevents fence_xvmd from operating as a clustered service, obviating the need to configure/run CMAN on the host domain.</p>
<dt><code>-U</code> <i>uri</i></p>
<dd>Force use of the specified URI for connecting to the hypervisor.</p>
<dt><code>-V</code></p>
<dd>Print out a version message, then exit. </p>
</dl>
<h2>Ccs Parameters</h2>
<p>CCS options are simply attributes of the &lt;fence_xvmd&gt; tag, a child of the &lt;cluster&gt; tag in /etc/cluster/cluster.conf.</p>
<dl>
<dt><i>debug=&quot;1&quot;</i></p>
<dd>Same as the -d option. Specify numbers &gt;1 for more debugging information.</p>
<dt><i>family=&quot;param&quot;</i></p>
<dd>Same as the -i option.</p>
<dt><i>multicast_address=&quot;param&quot;</i></p>
<dd>Same as the -a option.</p>
<dt><i>port=&quot;param&quot;</i></p>
<dd>Same as the -p option.</p>
<dt><i>auth=&quot;param&quot;</i></p>
<dd>Same as the -C option.</p>
<dt><i>hash=&quot;param&quot;</i></p>
<dd>Same as the -c option.</p>
<dt><i>key_file=&quot;param&quot;</i></p>
<dd>Same as the -k option.</p>
<dt><i>use_uuid=&quot;1&quot;</i></p>
<dd>Same as the -u option.</p>
<dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence/">fence</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8), <a href="/docs/linux/man/8-fence_xvm/">fence_xvm</a>(8) </p>
