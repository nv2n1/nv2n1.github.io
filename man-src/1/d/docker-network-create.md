---
title: "docker-network-create(1)"
name: "docker-network-create"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-network-create/"
description: "docker-network-create – Create a network"
---

<h2 class="name">NAME</h2>
<p> docker-network-create &#8211; Create a network </p>
<h2>SYNOPSIS</h2>
<p> <code>docker network create [OPTIONS] NETWORK</code> </p>
<h2>DESCRIPTION</h2>
<p> Creates a new network. The DRIVER accepts bridge or overlay which are the built-in network drivers. If you have installed a third party or your own custom network driver you can specify that DRIVER here also. If you don&#8217;t specify the &#8211;driver option, the command automatically creates a bridge network for you. When you install Docker Engine it creates a bridge network automatically. This network corresponds to the docker0 bridge that Engine has traditionally relied on. When you launch a new container with docker run it automatically connects to this bridge network. You cannot remove this default bridge network but you can create new ones using the network create command. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network create -d bridge my-bridge-network
</pre>
</dl>
<p> Bridge networks are isolated networks on a single Engine installation. If you want to create a network that spans multiple Docker hosts each running an Engine, you must create an overlay network. Unlike bridge networks overlay networks require some pre-existing conditions before you can create one. These conditions are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Access to a key-value store. Engine supports Consul, Etcd, and Zookeeper (Distributed store) key-value stores.</p>
<dt>&bull;</p>
<dd> A cluster of hosts with connectivity to the key-value store.</p>
<dt>&bull;</p>
<dd> A properly configured Engine daemon on each host in the cluster. </p>
</dl>
</dl>
<p> The dockerd options that support the overlay network are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> &#8211;cluster-store</p>
<dt>&bull;</p>
<dd> &#8211;cluster-store-opt</p>
<dt>&bull;</p>
<dd> &#8211;cluster-advertise </p>
</dl>
</dl>
<p> To read more about these options and how to configure them, see &quot;<i>Get started with multi-host network</i>&quot; &lt;<a rel="nofollow" href="https://docs.docker.com/engine/userguide/networking/get-started-overlay/">https://docs.docker.com/engine/userguide/networking/get-started-overlay/</a>&gt;. </p>
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
<p> When you start a container use the &#8211;network flag to connect it to a network. This adds the busybox container to the mynet network. </p>
<dl>
<dt>
<dd>
<pre>
$ docker run -itd --network=mynet busybox
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
<p>$ docker network create &#8211; d overlay&#8211; subnet = 192.168.0.0 / 16 &#8211;subnet = 192.170.0.0 / 16 &#8211;gateway = 192.168.0.100 \<br />
  &#8211;gateway = 192.170.0.100 &#8211;ip &#8211; range = 192.168.1.0 / 24 &#8211;aux &#8211; address = &#8220;my-router=192.168.1.5&#8221; &#8211;aux &#8211; address = &#8220;my-switch=192.168.1.6&#8221; &#8211;aux &#8211; address = &#8220;my-printer=192.170.1.5&#8221; &#8211;aux &#8211; address = &#8220;my-nas=192.170.1.6&#8221; my &#8211; multihost &#8211; network
</dl>
<p> Be sure that your subnetworks do not overlap. If they do, the network create fails and Engine returns an error. </p>
<h3>Network internal mode</h3>
<p> By default, when you connect a container to an overlay network, Docker also connects a bridge network to it to provide external connectivity. If you want to create an externally isolated overlay network, you can specify the &#8211;internal option. </p>
<h3>Network ingress mode</h3>
<p> You can create the network which will be used to provide the routing-mesh in the swarm cluster. You do so by specifying &#8211;ingress when creating the network. Only one ingress network can be created at the time. The network can be removed only if no services depend on it. Any option available when creating an overlay network is also available when creating the ingress network, besides the &#8211;attachable option. </p>
<dl>
<dt>
<dd>
<p>$ docker network create &#8211; d overlay&#8211; subnet = 10.11.0.0 / 16 &#8211;ingress&#8211; opt com.docker.network.mtu = 9216 &#8211;opt encrypted = true my &#8211; ingress &#8211; network
</dl>
<h3>Run services on predefined networks</h3>
<p> You can create services on the predefined docker networks bridge and host. </p>
<dl>
<dt>
<dd>
<pre>
$ docker service create --name my-service \
  --network host \
  --replicas 2 \
  busybox top
</pre>
</dl>
<h3>Swarm networks with local scope drivers</h3>
<p> You can create a swarm network with local scope network drivers. You do so by promoting the network scope to swarm during the creation of the network. You will then be able to use this network when creating services. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network create -d bridge \
  --scope swarm \
  --attachable \
  swarm-network
</pre>
</dl>
<p> For network drivers which provide connectivity across hosts (ex. macvlan), if node specific configurations are needed in order to plumb the network on each host, you will supply that configuration via a configuration only network. When you create the swarm scoped network, you will then specify the name of the network which contains the configuration. </p>
<dl>
<dt>
<dd>
<pre><code>
node1$ docker network create-- config - only-- subnet 192.168.100.0 / 24 --gateway 192.168.100.115 mv - config node2$ docker network create-- config - only-- subnet 192.168.200.0 / 24 --gateway 192.168.200.202 mv - config node1$ docker network create - d macvlan-- scope swarm-- config - from mv - config-- attachable swarm - network
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;attachable</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Enable manual container attachment</p>
<p> <code>&#8211;aux-address</code>=map[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Auxiliary IPv4 or IPv6 addresses used by Network driver</p>
<p> <code>&#8211;config-from</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>The network from which to copy the configuration</p>
<p> <code>&#8211;config-only</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Create a configuration only network</p>
<p> <code>-d</code>, <code>&#8211;driver</code>=&quot;bridge&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Driver to manage the Network</p>
<p> <code>&#8211;gateway</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>IPv4 or IPv6 Gateway for the master subnet</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for create</p>
<p> <code>&#8211;ingress</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Create swarm routing-mesh network</p>
<p> <code>&#8211;internal</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Restrict external access to the network</p>
<p> <code>&#8211;ip-range</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Allocate container ip from a sub-range</p>
<p> <code>&#8211;ipam-driver</code>=&quot;default&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>IP Address Management Driver</p>
<p> <code>&#8211;ipam-opt</code>=map[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set IPAM driver specific options</p>
<p> <code>&#8211;ipv6</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Enable IPv6 networking</p>
<p> <code>&#8211;label</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set metadata on a network</p>
<p> <code>-o</code>, <code>&#8211;opt</code>=map[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set driver specific options</p>
<p> <code>&#8211;scope</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Control the network&#8217;s scope</p>
<p> <code>&#8211;subnet</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Subnet in CIDR format that represents a network segment</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-network/">docker-network</a>(1)</code> </p>
<h2>Index</h2>
