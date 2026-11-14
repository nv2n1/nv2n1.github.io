---
title: "docker-network-connect(1)"
name: "docker-network-connect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-network-connect/"
description: "docker-network-connect – Connect a container to a network"
---

<h2 class="name">NAME</h2>
<p> docker-network-connect &#8211; Connect a container to a network </p>
<h2>SYNOPSIS</h2>
<p> <code>docker network connect [OPTIONS] NETWORK CONTAINER</code> </p>
<h2>DESCRIPTION</h2>
<p> Connects a container to a network. You can connect a container by name or by ID. Once connected, the container can communicate with other containers in the same network. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network connect multi-host-network container1
</pre>
</dl>
<p> You can also use the docker run &#8211;network=&lt;network-name&gt; option to start a container and immediately connect it to a network. </p>
<dl>
<dt>
<dd>
<pre>
$ docker run -itd --network=multi-host-network --ip 172.20.88.22 --ip6 2001:db8::8822 busybox
</pre>
</dl>
<p> You can pause, restart, and stop containers that are connected to a network. A container connects to its configured networks when it runs. </p>
<p> If specified, the container&#8217;s IP address(es) is reapplied when a stopped container is restarted. If the IP address is no longer available, the container fails to start. One way to guarantee that the IP address is available is to specify an &#8211;ip-range when creating the network, and choose the static IP address(es) from outside that range. This ensures that the IP address is not given to another container while this container is not on the network. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network create --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 multi-host-network
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
$ docker network connect --ip 172.20.128.2 multi-host-network container2
</pre>
</dl>
<p> To verify the container is connected, use the docker network inspect command. Use docker network disconnect to remove a container from the network. </p>
<p> Once connected in network, containers can communicate using only another container&#8217;s IP address or name. For overlay networks or custom plugins that support multi-host connectivity, containers connected to the same multi-host network but launched from different Engines can also communicate in this way. </p>
<p> You can connect a container to one or more networks. The networks need not be the same type. For example, you can connect a single container bridge and overlay networks. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;alias</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add network-scoped alias for the container</p>
<p> <code>&#8211;driver-opt</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>driver options for the network</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for connect</p>
<p> <code>&#8211;ip</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>IPv4 address (e.g., 172.30.100.104)</p>
<p> <code>&#8211;ip6</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>IPv6 address (e.g., 2001:db8::33)</p>
<p> <code>&#8211;link</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add link to another container</p>
<p> <code>&#8211;link-local-ip</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Add a link-local address for the container</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-network/">docker-network</a>(1)</code> </p>
<h2>Index</h2>
