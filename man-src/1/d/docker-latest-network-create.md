---
title: "docker-latest-network-create(1)"
name: "docker-latest-network-create"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-network-create/"
description: "docker-network-create – create a new network"
---

<h2 class="name">NAME</h2>
<p> docker-network-create &#8211; create a new network </p>
<h2>SYNOPSIS</h2>
<p> <code>docker network create</code> [<code>&#8211;aux-address</code>=<i>map[]</i>] [<code>-d</code>|<code>&#8211;driver</code>=<i>DRIVER</i>] [<code>&#8211;gateway</code>=<i>[]</i>] [<code>&#8211;help</code>] [<code>&#8211;internal</code>] [<code>&#8211;ip-range</code>=<i>[]</i>] [<code>&#8211;ipam-driver</code>=<i>default</i>] [<code>&#8211;ipam-opt</code>=<i>map[]</i>] [<code>&#8211;ipv6</code>] [<code>&#8211;label</code>[=<i>[]</i>]] [<code>-o</code>|<code>&#8211;opt</code>=<i>map[]</i>] [<code>&#8211;subnet</code>=<i>[]</i>] NETWORK-NAME </p>
<h2>DESCRIPTION</h2>
<p> Creates a new network. The DRIVER accepts bridge or overlay which are the built-in network drivers. If you have installed a third party or your own custom network driver you can specify that DRIVER here also. If you don&#8217;t specify the &#8211;driver option, the command automatically creates a bridge network for you. When you install Docker Engine it creates a bridge network automatically. This network corresponds to the docker0 bridge that Engine has traditionally relied on. When launch a new container with docker run it automatically connects to this bridge network. You cannot remove this default bridge network but you can create new ones using the network create command. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network create -d bridge my-bridge-network
</pre>
</dl>
<p> Bridge networks are isolated networks on a single Engine installation. If you want to create a network that spans multiple Docker hosts each running an Engine, you must create an overlay network. Unlike bridge networks overlay networks require some pre-existing conditions before you can create one. These conditions are:</p>
<dl>
<dt>step]</p>
<dd>
<p> item Access to a key-value store. Engine supports Consul, Etcd, and Zookeeper (Distributed store) key-value stores. item A cluster of hosts with connectivity to the key-value store. item A properly configured Engine daemon on each host in the cluster.</dl>
<p> The dockerd options that support the overlay network are:</p>
<dl>
<dt>step]</p>
<dd>
<p> item &#8211;cluster-store item &#8211;cluster-store-opt item &#8211;cluster-advertise</dl>
<p> To read more about these options and how to configure them, see &lt;<a rel="nofollow" href="https://docs.docker.com/engine/userguide/networking/get-started-overlay/">https://docs.docker.com/engine/userguide/networking/get-started-overlay/</a>&gt;. </p>
<p> It is also a good idea, though not required, that you install Docker Swarm on to manage the cluster that makes up your network. Swarm provides sophisticated discovery and server management that can assist your implementation. </p>
<p> Once you have prepared the overlay network prerequisites you simply choose a Docker host in the cluster and issue the following to create the network: </p>
<dl>
<dt>
<dd>
<pre>
$ docker network create -d overlay my-multihost-network
</pre>
</dl>
<p> Network names must be unique. The Docker daemon attempts to identify naming conflicts but this is not guaranteed. It is the user&#8217;s responsibility to avoid name conflicts. </p>
<h2>Connect containers</h2>
<p> When you start a container use the &#8211;net flag to connect it to a network. This adds the busybox container to the mynet network. </p>
<dl>
<dt>
<dd>
<pre>
$ docker run -itd --net=mynet busybox
</pre>
</dl>
<p> If you want to add a container to a network after the container is already running use the docker network connect subcommand. </p>
<p> You can connect multiple containers to the same network. Once connected, the containers can communicate using only another container&#8217;s IP address or name. For overlay networks or custom plugins that support multi-host connectivity, containers connected to the same multi-host network but launched from different Engines can also communicate in this way. </p>
<p> You can disconnect a container from a network using the docker network disconnect command. </p>
<h2>Specifying advanced options</h2>
<p> When you create a network, Engine creates a non-overlapping subnetwork for the network by default. This subnetwork is not a subdivision of an existing network. It is purely for ip-addressing purposes. You can override this default and specify subnetwork values directly using the &#8211;subnet option. On a bridge network you can only create a single subnet: </p>
<dl>
<dt>
<dd>
<pre>
$ docker network create -d bridge --subnet=192.168.0.0/16 br0
</pre>
</dl>
<p> Additionally, you also specify the &#8211;gateway &#8211;ip-range and &#8211;aux-address options. </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker network create-- driver = bridge-- subnet = 172.28.0.0 / 16 --ip - range = 172.28.5.0 / 24 --gateway = 172.28.5.254 br0
</code></pre>
</dl>
<p> If you omit the &#8211;gateway flag the Engine selects one for you from inside a preferred pool. For overlay networks and for network driver plugins that support it you can create multiple subnetworks. </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker network create - d overlay-- subnet = 192.168.0.0 / 16 --subnet = 192.170.0.0 / 16 --gateway = 192.168.0.100 \ 
  --gateway = 192.170.0.100 --ip - range = 192.168.1.0 / 24 --aux - address = "my-router=192.168.1.5" --aux - address = "my-switch=192.168.1.6" --aux - address = "my-printer=192.170.1.5" --aux - address = "my-nas=192.170.1.6" my - multihost - network
</code></pre>
</dl>
<p> Be sure that your subnetworks do not overlap. If they do, the network create fails and Engine returns an error. </p>
<h3>Network internal mode</h3>
<p> By default, when you connect a container to an overlay network, Docker also connects a bridge network to it to provide external connectivity. If you want to create an externally isolated overlay network, you can specify the &#8211;internal option. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;aux-address</code>=map[]<br />
&nbsp;<wbr>&nbsp;<wbr>Auxiliary IPv4 or IPv6 addresses used by network driver </p>
<p> <code>-d</code>, <code>&#8211;driver</code>=<i>DRIVER</i><br />
&nbsp;<wbr>&nbsp;<wbr>Driver to manage the Network bridge or overlay. The default is bridge. </p>
<p> <code>&#8211;gateway</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>IPv4 or IPv6 Gateway for the master subnet </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage </p>
<p> <code>&#8211;internal</code><br />
&nbsp;<wbr>&nbsp;<wbr>Restrict external access to the network </p>
<p> <code>&#8211;ip-range</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>Allocate container ip from a sub-range </p>
<p> <code>&#8211;ipam-driver</code>=<i>default</i><br />
&nbsp;<wbr>&nbsp;<wbr>IP Address Management Driver </p>
<p> <code>&#8211;ipam-opt</code>=map[]<br />
&nbsp;<wbr>&nbsp;<wbr>Set custom IPAM driver options </p>
<p> <code>&#8211;ipv6</code><br />
&nbsp;<wbr>&nbsp;<wbr>Enable IPv6 networking </p>
<p> <code>&#8211;label</code>=<i>label</i><br />
Set metadata for a network </p>
<p> <code>-o</code>, <code>&#8211;opt</code>=map[]<br />
&nbsp;<wbr>&nbsp;<wbr>Set custom driver options </p>
<p> <code>&#8211;subnet</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>Subnet in CIDR format that represents a network segment </p>
<h2>HISTORY</h2>
<p> OCT 2015, created by Mary Anthony &lt;mary [at] docker.com&gt; </p>
<h2>Index</h2>
