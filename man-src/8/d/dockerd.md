---
title: "dockerd(8)"
name: "dockerd"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dockerd/"
description: "dockerd – Enable daemon mode"
---

<p>dockerd &#8211; Enable daemon mode </p>
<h2>Synopsis</h2>
<p><code>dockerd</code> [<code>&#8211;add-runtime</code>[=<i>[]</i>]] [<code>&#8211;allow-nondistributable-artifacts</code>[=<i>[]</i>]] [<code>&#8211;api-cors-header</code>=[=<i>API-CORS-HEADER</i>]] [<code>&#8211;authorization-plugin</code>[=<i>[]</i>]] [<code>-b</code>|<code>&#8211;bridge</code>[=<i>BRIDGE</i>]] [<code>&#8211;bip</code>[=<i>BIP</i>]] [<code>&#8211;cgroup-parent</code>[=<i>[]</i>]] [<code>&#8211;cluster-store</code>[=<i>[]</i>]] [<code>&#8211;cluster-advertise</code>[=<i>[]</i>]] [<code>&#8211;cluster-store-opt</code>[=<i>map[]</i>]] [<code>&#8211;config-file</code>[=<i>/etc/docker/daemon.json</i>]] [<code>&#8211;containerd</code>[=<i>SOCKET-PATH</i>]] [<code>&#8211;data-root</code>[=<i>/var/lib/docker</i>]] [<code>-D</code>|<code>&#8211;debug</code>] [<code>&#8211;default-cgroupns-mode</code>[=<i>host</i>]] [<code>&#8211;default-gateway</code>[=<i>DEFAULT-GATEWAY</i>]] [<code>&#8211;default-gateway-v6</code>[=<i>DEFAULT-GATEWAY-V6</i>]] [<code>&#8211;default-address-pool</code>[=<i>DEFAULT-ADDRESS-POOL</i>]] [<code>&#8211;default-runtime</code>[=<i>runc</i>]] [<code>&#8211;default-ipc-mode</code>=<i>MODE</i>] [<code>&#8211;default-shm-size</code>[=<i>64MiB</i>]] [<code>&#8211;default-ulimit</code>[=<i>[]</i>]] [<code>&#8211;dns</code>[=<i>[]</i>]] [<code>&#8211;dns-opt</code>[=<i>[]</i>]] [<code>&#8211;dns-search</code>[=<i>[]</i>]] [<code>&#8211;exec-opt</code>[=<i>[]</i>]] [<code>&#8211;exec-root</code>[=<i>/var/run/docker</i>]] [<code>&#8211;experimental</code>[=<i>false</i>]] [<code>&#8211;fixed-cidr</code>[=<i>FIXED-CIDR</i>]] [<code>&#8211;fixed-cidr-v6</code>[=<i>FIXED-CIDR-V6</i>]] [<code>-G</code>|<code>&#8211;group</code>[=<i>docker</i>]] [<code>-H</code>|<code>&#8211;host</code>[=<i>[]</i>]] [<code>&#8211;help</code>] [<code>&#8211;icc</code>[=<i>true</i>]] [<code>&#8211;init</code>[=<i>false</i>]] [<code>&#8211;init-path</code>[=<i>&quot;&quot;</i>]] [<code>&#8211;insecure-registry</code>[=<i>[]</i>]] [<code>&#8211;ip</code>[=<i>0.0.0.0</i>]] [<code>&#8211;ip-forward</code>[=<i>true</i>]] [<code>&#8211;ip-masq</code>[=<i>true</i>]] [<code>&#8211;iptables</code>[=<i>true</i>]] [<code>&#8211;ipv6</code>] [<code>&#8211;isolation</code>[=<i>default</i>]] [<code>-l</code>|<code>&#8211;log-level</code>[=<i>info</i>]] [<code>&#8211;label</code>[=<i>[]</i>]] [<code>&#8211;live-restore</code>[=<i>false</i>]] [<code>&#8211;log-driver</code>[=<i>json-file</i>]] [<code>&#8211;log-opt</code>[=<i>map[]</i>]] [<code>&#8211;mtu</code>[=<i>0</i>]] [<code>&#8211;max-concurrent-downloads</code>[=<i>3</i>]] [<code>&#8211;max-concurrent-uploads</code>[=<i>5</i>]] [<code>&#8211;max-download-attempts</code>[=<i>5</i>]] [<code>&#8211;node-generic-resources</code>[=<i>[]</i>]] [<code>-p</code>|<code>&#8211;pidfile</code>[=<i>/var/run/docker.pid</i>]] [<code>&#8211;raw-logs</code>] [<code>&#8211;registry-mirror</code>[=<i>[]</i>]] [<code>-s</code>|<code>&#8211;storage-driver</code>[=<i>STORAGE-DRIVER</i>]] [<code>&#8211;seccomp-profile</code>[=<i>SECCOMP-PROFILE-PATH</i>]] [<code>&#8211;selinux-enabled</code>] [<code>&#8211;shutdown-timeout</code>[=<i>15</i>]] [<code>&#8211;storage-opt</code>[=<i>[]</i>]] [<code>&#8211;swarm-default-advertise-addr</code>[=<i>IP|INTERFACE</i>]] [<code>&#8211;tls</code>] [<code>&#8211;tlscacert</code>[=<i>~/.docker/ca.pem</i>]] [<code>&#8211;tlscert</code>[=<i>~/.docker/cert.pem</i>]] [<code>&#8211;tlskey</code>[=<i>~/.docker/key.pem</i>]] [<code>&#8211;tlsverify</code>] [<code>&#8211;userland-proxy</code>[=<i>true</i>]] [<code>&#8211;userland-proxy-path</code>[=<i>&quot;&quot;</i>]] [<code>&#8211;userns-remap</code>[=<i>default</i>]] </p>
<h2>Description</h2>
<p><code>dockerd</code> is used for starting the Docker daemon (i.e., to command the daemon to manage images, containers etc). So <code>dockerd</code> is a server, as a daemon. To run the Docker daemon you can specify <code>dockerd</code>. You can check the daemon options using <code>dockerd &#8211;help</code>. Daemon options should be specified after the <code>dockerd</code> keyword in the following format. <code>dockerd [OPTIONS]</code> </p>
<h2>Options</h2>
<p><code>&#8211;add-runtime</code>=[]<br />
&nbsp;<wbr>&nbsp;Runtimes can be registered with the daemon either via the configuration file or using the &#8211;add-runtime command line argument. </p>
<p> The following is an example adding 2 runtimes via the configuration: </p>
<dl>
<dd>
<pre>{
 &quot;default-runtime&quot;: &quot;runc&quot;,
 &quot;runtimes&quot;: {
 &quot;runc&quot;: {
 &quot;path&quot;: &quot;runc&quot;
 },
 &quot;custom&quot;: {
 &quot;path&quot;: &quot;/usr/local/bin/my-runc-replacement&quot;,
 &quot;runtimeArgs&quot;: [
 &quot;--debug&quot;
 ]
 }
 }
}</pre>
</dl>
<p> This is the same example via the command line: </p>
<dl>
<dd>
<pre>$ sudo dockerd --add-runtime runc=runc --add-runtime custom=/usr/local/bin/my-runc-replacement</pre>
</dl>
<p> <code>Note</code>: defining runtime arguments via the command line is not supported. </p>
<p> <code>&#8211;allow-nondistributable-artifacts</code>=[]<br />
&nbsp;<wbr>&nbsp;Push nondistributable artifacts to the specified registries. </p>
<p> List can contain elements with CIDR notation to specify a whole subnet. </p>
<p> This option is useful when pushing images containing nondistributable<br />
&nbsp;<wbr>&nbsp;artifacts to a registry on an air-gapped network so hosts on that network can<br />
&nbsp;<wbr>&nbsp;pull the images without connecting to another server. </p>
<p> <code>Warning</code>: Nondistributable artifacts typically have restrictions on how<br />
&nbsp;<wbr>&nbsp;and where they can be distributed and shared. Only use this feature to push<br />
&nbsp;<wbr>&nbsp;artifacts to private registries and ensure that you are in compliance with<br />
&nbsp;<wbr>&nbsp;any terms that cover redistributing nondistributable artifacts. </p>
<p> <code>&#8211;api-cors-header</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Set CORS headers in the Engine API. Default is cors disabled. Give urls like<br />
&nbsp;<wbr>&nbsp;&quot;<a rel="nofollow" href="http://foo,">http://foo,</a>&nbsp;<a rel="nofollow" href="http://bar,">http://bar,</a>&nbsp;&#8230;&quot;. Give&nbsp;&quot;*&quot;&nbsp;to allow all. </p>
<p> <code>&#8211;authorization-plugin</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Set authorization plugins to load </p>
<p> <code>-b</code>, <code>&#8211;bridge</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Attach containers to a pre-existing network bridge;&nbsp;use&nbsp;&#8216;none&#8217;&nbsp;to disable<br />
&nbsp;<wbr>&nbsp;container networking </p>
<p> <code>&#8211;bip</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Use the provided CIDR notation address for the dynamically created bridge<br />
&nbsp;<wbr>&nbsp;(docker0);&nbsp;Mutually exclusive of -b </p>
<p> <code>&#8211;cgroup-parent</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Set parent cgroup for all containers. Default is&nbsp;&quot;/docker&quot;&nbsp;for fs cgroup<br />
&nbsp;<wbr>&nbsp;driver and&nbsp;&quot;system.slice&quot;&nbsp;for systemd cgroup driver. </p>
<p> <code>&#8211;cluster-store</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;URL of the distributed storage backend </p>
<p> <code>&#8211;cluster-advertise</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Specifies the&nbsp;&#8216;host:port&#8217;&nbsp;or interface:port combination that this<br />
&nbsp;<wbr>&nbsp;particular daemon instance should use when advertising itself to the cluster.<br />
&nbsp;<wbr>&nbsp;The daemon is reached through this value. </p>
<p> <code>&#8211;cluster-store-opt</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Specifies options for the Key/Value store. </p>
<p> <code>&#8211;config-file</code>=&quot;/etc/docker/daemon.json&quot;<br />
&nbsp;<wbr>&nbsp;Specifies the JSON file path to load the configuration from. </p>
<p> <code>&#8211;containerd</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Path to containerd socket. </p>
<p> <code>&#8211;data-root</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Path to the directory used to store persisted Docker data such as<br />
&nbsp;<wbr>&nbsp;configuration for resources, swarm cluster state, and filesystem data for<br />
&nbsp;<wbr>&nbsp;images, containers, and local volumes. Default is&nbsp;/var/lib/docker. </p>
<p> <code>-D</code>, <code>&#8211;debug</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Enable debug mode. Default is false. </p>
<p> <code>&#8211;default-cgroupns-mode</code>=&quot;<code>host</code>|<code>private</code>&quot;<br />
&nbsp;<wbr>&nbsp;Set the default cgroup namespace mode for newly created containers. The argument<br />
&nbsp;<wbr>&nbsp;can either be&nbsp;<code>host</code>&nbsp;or&nbsp;<code>private</code>. If unset, this defaults to host on cgroup v1, private on cgroup v2. </p>
<p> <code>&#8211;default-gateway</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;IPv4 address of the container default gateway;&nbsp;this address must be part of<br />
&nbsp;<wbr>&nbsp;the bridge subnet&nbsp;(which is defined by -b or &#8211;bip) </p>
<p> <code>&#8211;default-gateway-v6</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;IPv6 address of the container default gateway </p>
<p> <code>&#8211;default-address-pool</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Default address pool from which IPAM driver selects a subnet for the networks.<br />
&nbsp;<wbr>&nbsp;Example: base=172.30.0.0/16,size=24 will set the default<br />
&nbsp;<wbr>&nbsp;address pools for the selected scope networks to&nbsp;{172.30.[0-255].0/24} </p>
<p> <code>&#8211;default-runtime</code>=&quot;runc&quot;<br />
&nbsp;<wbr>&nbsp;Set default runtime if there&#8217;re more than one specified by &#8211;add-runtime. </p>
<p> <code>&#8211;default-ipc-mode</code>=&quot;<code>private</code>|<code>shareable</code>&quot;<br />
&nbsp;<wbr>&nbsp;Set the default IPC mode for newly created containers. The argument<br />
&nbsp;<wbr>&nbsp;can either be&nbsp;<code>private</code>&nbsp;or&nbsp;<code>shareable</code>. </p>
<p> <code>&#8211;default-shm-size</code>=<i>64MiB</i><br />
&nbsp;<wbr>&nbsp;Set the daemon-wide default shm size for containers. Default is 64MiB. </p>
<p> <code>&#8211;default-ulimit</code>=[]<br />
&nbsp;<wbr>&nbsp;Default ulimits for containers. </p>
<p> <code>&#8211;dns</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Force Docker to use specific DNS servers </p>
<p> <code>&#8211;dns-opt</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;DNS options to use. </p>
<p> <code>&#8211;dns-search</code>=[]<br />
&nbsp;<wbr>&nbsp;DNS search domains to use. </p>
<p> <code>&#8211;exec-opt</code>=[]<br />
&nbsp;<wbr>&nbsp;Set runtime execution options. See RUNTIME EXECUTION OPTIONS. </p>
<p> <code>&#8211;exec-root</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Path to use as the root of the Docker execution state files. Default is<br />
&nbsp;<wbr>&nbsp;/var/run/docker. </p>
<p> <code>&#8211;experimental</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Enable the daemon experimental features. </p>
<p> <code>&#8211;fixed-cidr</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;IPv4 subnet for fixed IPs&nbsp;(e.g., 10.20.0.0/16);&nbsp;this subnet must be nested in<br />
&nbsp;<wbr>&nbsp;the bridge subnet&nbsp;(which is defined by -b or &#8211;bip). </p>
<p> <code>&#8211;fixed-cidr-v6</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;IPv6 subnet for global IPv6 addresses&nbsp;(e.g., 2a00:1450::/64) </p>
<p> <code>-G</code>, <code>&#8211;group</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Group to assign the unix socket specified by -H when running in daemon mode.<br />
&nbsp;<wbr>&nbsp;use&nbsp;&#8221;&nbsp;(the empty string)&nbsp;to disable setting of a group. Default is docker. </p>
<p> <code>-H</code>, <code>&#8211;host</code>=[<i><a href="unix:///var/run/docker.sock">unix:///var/run/docker.sock</a></i>]: <a href="tcp://[host:port]">tcp://[host:port]</a> to bind or <a href="unix://[/path/to/socket]">unix://[/path/to/socket]</a> to use.<br />
&nbsp;<wbr>&nbsp;The socket(s)&nbsp;to bind to in daemon mode specified using one or more<br />
&nbsp;<wbr>&nbsp;<a href="tcp://host:port,">tcp://host:port,</a>&nbsp;<a href="unix:///path/to/socket,">unix:///path/to/socket,</a>&nbsp;fd://*&nbsp;or fd://socketfd. </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;Print usage statement </p>
<p> <code>&#8211;icc</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Allow unrestricted inter-container and Docker daemon host communication. If<br />
&nbsp;<wbr>&nbsp;disabled, containers can still be linked together using the&nbsp;<code>&#8211;link</code>&nbsp;option<br />
&nbsp;<wbr>&nbsp;(see&nbsp;<code><a href="/docs/linux/man/1-docker-run/">docker-run</a>(1)</code>). Default is true. </p>
<p> <code>&#8211;init</code><br />
&nbsp;<wbr>&nbsp;Run an init process inside containers for signal forwarding and process<br />
&nbsp;<wbr>&nbsp;reaping. </p>
<p> <code>&#8211;init-path</code><br />
&nbsp;<wbr>&nbsp;Path to the docker-init binary. </p>
<p> <code>&#8211;insecure-registry</code>=[]<br />
&nbsp;<wbr>&nbsp;Enable insecure registry communication, i.e., enable un-encrypted and/or<br />
&nbsp;<wbr>&nbsp;untrusted communication. </p>
<p> List of insecure registries can contain an element with CIDR notation to<br />
&nbsp;<wbr>&nbsp;specify a whole subnet. Insecure registries accept HTTP and/or accept HTTPS<br />
&nbsp;<wbr>&nbsp;with certificates from unknown CAs. </p>
<p> Enabling &#8211;insecure-registry is useful when running a local registry.<br />
&nbsp;<wbr>&nbsp;However, because its use creates security vulnerabilities it should ONLY be<br />
&nbsp;<wbr>&nbsp;enabled for testing purposes.&nbsp;<wbr>&nbsp;For increased security, users should add their<br />
&nbsp;<wbr>&nbsp;CA to their system&#8217;s list of trusted CAs instead of using<br />
&nbsp;<wbr>&nbsp;&#8211;insecure-registry. </p>
<p> <code>&#8211;ip</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Default IP address to use when binding container ports. Default is 0.0.0.0. </p>
<p> <code>&#8211;ip-forward</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Enables IP forwarding on the Docker host. The default is true. This flag<br />
&nbsp;<wbr>&nbsp;interacts with the IP forwarding setting on your host system&#8217;s kernel. If<br />
&nbsp;<wbr>&nbsp;your system has IP forwarding disabled, this setting enables it. If your<br />
&nbsp;<wbr>&nbsp;system has IP forwarding enabled, setting this flag to &#8211;ip-forward=false<br />
&nbsp;<wbr>&nbsp;has no effect. </p>
<p> This setting will also enable IPv6 forwarding if you have both<br />
&nbsp;<wbr>&nbsp;&#8211;ip-forward=true and &#8211;fixed-cidr-v6 set. Note that this may reject<br />
&nbsp;<wbr>&nbsp;Router Advertisements and interfere with the host&#8217;s existing IPv6<br />
&nbsp;<wbr>&nbsp;configuration. For more information, please consult the documentation about<br />
&nbsp;<wbr>&nbsp;&quot;Advanced Networking &#8211; IPv6&quot;. </p>
<p> <code>&#8211;ip-masq</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Enable IP masquerading for bridge&#8217;s IP range. Default is true. </p>
<p> <code>&#8211;iptables</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Enable Docker&#8217;s addition of iptables rules. Default is true. </p>
<p> <code>&#8211;ipv6</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Enable IPv6 support. Default is false. Docker will create an IPv6-enabled<br />
&nbsp;<wbr>&nbsp;bridge with address fe80::1 which will allow you to create IPv6-enabled<br />
&nbsp;<wbr>&nbsp;containers. Use together with &#8211;fixed-cidr-v6 to provide globally routable<br />
&nbsp;<wbr>&nbsp;IPv6 addresses. IPv6 forwarding will be enabled if not used with<br />
&nbsp;<wbr>&nbsp;&#8211;ip-forward=false. This may collide with your host&#8217;s current IPv6<br />
&nbsp;<wbr>&nbsp;settings. For more information please consult the documentation about<br />
&nbsp;<wbr>&nbsp;&quot;Advanced Networking &#8211; IPv6&quot;. </p>
<p> <code>&#8211;isolation</code>=&quot;<i>default</i>&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Isolation specifies the type of isolation technology used by containers.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Note that the default on Windows server is process, and the default on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Windows client is hyperv. Linux only supports default. </p>
<p> <code>-l</code>, <code>&#8211;log-level</code>=&quot;<i>debug</i>|<i>info</i>|<i>warn</i>|<i>error</i>|<i>fatal</i>&quot;<br />
&nbsp;<wbr>&nbsp;Set the logging level. Default is info. </p>
<p> <code>&#8211;label</code>=&quot;[]&quot;<br />
&nbsp;<wbr>&nbsp;Set key=value labels to the daemon&nbsp;(displayed in docker info) </p>
<p> <code>&#8211;live-restore</code>=<i>false</i><br />
&nbsp;<wbr>&nbsp;Enable live restore of running containers when the daemon starts so that they<br />
&nbsp;<wbr>&nbsp;are not restarted. This option is applicable only for docker daemon running<br />
&nbsp;<wbr>&nbsp;on Linux host. </p>
<p> <code>&#8211;log-driver</code>=&quot;<i>json-file</i>|<i>syslog</i>|<i>journald</i>|<i>gelf</i>|<i>fluentd</i>|<i>awslogs</i>|<i>splunk</i>|<i>etwlogs</i>|<i>gcplogs</i>|<i>none</i>&quot;<br />
&nbsp;<wbr>&nbsp;Default driver for container logs. Default is json-file.<br />
&nbsp;<wbr>&nbsp;<code>Warning</code>: docker logs command works only for json-file logging driver. </p>
<p> <code>&#8211;log-opt</code>=[]<br />
&nbsp;<wbr>&nbsp;Logging driver specific options. </p>
<p> <code>&#8211;mtu</code>=<i>0</i><br />
&nbsp;<wbr>&nbsp;Set the containers network mtu. Default is 0. </p>
<p> <code>&#8211;max-concurrent-downloads</code>=<i>3</i><br />
&nbsp;<wbr>&nbsp;Set the max concurrent downloads for each pull. Default is 3. </p>
<p> <code>&#8211;max-concurrent-uploads</code>=<i>5</i><br />
&nbsp;<wbr>&nbsp;Set the max concurrent uploads for each push. Default is 5. </p>
<p> <code>&#8211;max-download-attempts</code>=<i>5</i><br />
&nbsp;<wbr>&nbsp;Set the max download attempts for each pull. Default is 5. </p>
<p> <code>&#8211;node-generic-resources</code>=<i>[]</i><br />
&nbsp;<wbr>&nbsp;Advertise user-defined resource. Default is&nbsp;[].<br />
&nbsp;<wbr>&nbsp;Use this if your swarm cluster has some nodes with custom<br />
&nbsp;<wbr>&nbsp;resources&nbsp;(e.g: NVIDIA GPU, SSD, &#8230;)&nbsp;and you need your services to land on<br />
&nbsp;<wbr>&nbsp;nodes advertising these resources.<br />
&nbsp;<wbr>&nbsp;Usage example: &#8211;node-generic-resources&nbsp;&quot;NVIDIA-GPU=UUID1&quot;<br />
&nbsp;<wbr>&nbsp;&#8211;node-generic-resources&nbsp;&quot;NVIDIA-GPU=UUID2&quot; </p>
<p> <code>-p</code>, <code>&#8211;pidfile</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Path to use for daemon PID file. Default is&nbsp;/var/run/docker.pid </p>
<p> <code>&#8211;raw-logs</code><br />
&nbsp;<wbr>&nbsp;Output daemon logs in full timestamp format without ANSI coloring. If this<br />
&nbsp;<wbr>&nbsp;flag is not set, the daemon outputs condensed, colorized logs if a terminal<br />
&nbsp;<wbr>&nbsp;is detected, or full&nbsp;(&quot;raw&quot;)&nbsp;output otherwise. </p>
<p> <code>&#8211;registry-mirror</code>=<i>://</i><br />
&nbsp;<wbr>&nbsp;Prepend a registry mirror to be used for image pulls. May be specified<br />
&nbsp;<wbr>&nbsp;multiple times. </p>
<p> <code>-s</code>, <code>&#8211;storage-driver</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Force the Docker runtime to use a specific storage driver. </p>
<p> <code>&#8211;seccomp-profile</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Path to seccomp profile. </p>
<p> <code>&#8211;selinux-enabled</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Enable selinux support. Default is false. </p>
<p> <code>&#8211;shutdown-timeout</code>=<i>15</i><br />
&nbsp;<wbr>&nbsp;Set the shutdown timeout value in seconds. Default is 15. </p>
<p> <code>&#8211;storage-opt</code>=[]<br />
&nbsp;<wbr>&nbsp;Set storage driver options. See STORAGE DRIVER OPTIONS. </p>
<p> <code>&#8211;swarm-default-advertise-addr</code>=<i>IP|INTERFACE</i><br />
&nbsp;<wbr>&nbsp;Set default address or interface for swarm to advertise as its<br />
&nbsp;<wbr>&nbsp;externally-reachable address to other cluster members. This can be a<br />
&nbsp;<wbr>&nbsp;hostname, an IP address, or an interface such as eth0. A port cannot be<br />
&nbsp;<wbr>&nbsp;specified with this option. </p>
<p> <code>&#8211;tls</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Use TLS;&nbsp;implied by &#8211;tlsverify. Default is false. </p>
<p> <code>&#8211;tlscacert</code>=<i>~/.docker/ca.pem</i><br />
&nbsp;<wbr>&nbsp;Trust certs signed only by this CA. </p>
<p> <code>&#8211;tlscert</code>=<i>~/.docker/cert.pem</i><br />
&nbsp;<wbr>&nbsp;Path to TLS certificate file. </p>
<p> <code>&#8211;tlskey</code>=<i>~/.docker/key.pem</i><br />
&nbsp;<wbr>&nbsp;Path to TLS key file. </p>
<p> <code>&#8211;tlsverify</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Use TLS and verify the remote&nbsp;(daemon: verify client, client: verify daemon).<br />
&nbsp;<wbr>&nbsp;Default is false. </p>
<p> <code>&#8211;userland-proxy</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Rely on a userland proxy implementation for inter-container and<br />
&nbsp;<wbr>&nbsp;outside-to-container loopback communications. Default is true. </p>
<p> <code>&#8211;userland-proxy-path</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Path to the userland proxy binary. </p>
<p> <code>&#8211;userns-remap</code>=<i>default</i>|<i>uid:gid</i>|<i>user:group</i>|<i>user</i>|<i>uid</i><br />
&nbsp;<wbr>&nbsp;Enable user namespaces for containers on the daemon. Specifying&nbsp;&quot;default&quot;<br />
&nbsp;<wbr>&nbsp;will cause a new user and group to be created to handle UID and GID range<br />
&nbsp;<wbr>&nbsp;remapping for the user namespace mappings used for contained processes.<br />
&nbsp;<wbr>&nbsp;Specifying a user&nbsp;(or uid)&nbsp;and optionally a group&nbsp;(or gid)&nbsp;will cause the<br />
&nbsp;<wbr>&nbsp;daemon to lookup the user and group&#8217;s subordinate ID ranges for use as the<br />
&nbsp;<wbr>&nbsp;user namespace mappings for contained processes.</p>
<h2>Storage Driver Options</h2>
<p>Docker uses storage backends (known as &quot;graphdrivers&quot; in the Docker internals) to create writable containers from images. Many of these backends use operating system level technologies and can be configured. </p>
<p> Specify options to the storage backend with <code>&#8211;storage-opt</code> flags. The backends that currently take options are <i>devicemapper</i>, <i>zfs</i> and <i>btrfs</i>. Options for <i>devicemapper</i> are prefixed with <i>dm</i>, options for <i>zfs</i> start with <i>zfs</i> and options for <i>btrfs</i> start with <i>btrfs</i>. </p>
<p> Specifically for devicemapper, the default is a &quot;loopback&quot; model which requires no pre-configuration, but is extremely inefficient. Do not use it in production. </p>
<p> To make the best use of Docker with the devicemapper backend, you must have a recent version of LVM. Use lvm to create a thin pool; for more information see man lvmthin. Then, use &#8211;storage-opt dm.thinpooldev to tell the Docker engine to use that pool for allocating images and container snapshots.</p>
<h2>Devicemapper options</h2>
<h3>dm.thinpooldev</h3>
<p>Specifies a custom block storage device to use for the thin pool. </p>
<p> If using a block device for device mapper storage, it is best to use lvm to create and manage the thin-pool volume. This volume is then handed to Docker to exclusively create snapshot volumes needed for images and containers. </p>
<p> Managing the thin-pool outside of Engine makes for the most feature-rich method of having Docker utilize device mapper thin provisioning as the backing storage for Docker containers. The highlights of the lvm-based thin-pool management feature include: automatic or interactive thin-pool resize support, dynamically changing thin-pool features, automatic thinp metadata checking when lvm activates the thin-pool, etc. </p>
<p> As a fallback if no thin pool is provided, loopback files are created. Loopback is very slow, but can be used without any pre-configuration of storage. It is strongly recommended that you do not use loopback in production. Ensure your Engine daemon has a &#8211;storage-opt dm.thinpooldev argument provided. </p>
<p> Example use: </p>
<p> $ dockerd \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;storage-opt dm.thinpooldev=/dev/mapper/thin-pool</p>
<h3>dm.directlvm_device</h3>
<p>As an alternative to manually creating a thin pool as above, Docker can automatically configure a block device for you. </p>
<p> Example use: </p>
<p> $ dockerd \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;storage-opt dm.directlvm_device=/dev/xvdf</p>
<h3>dm.thinp_percent</h3>
<p>Sets the percentage of passed in block device to use for storage.</p>
<h3>Example:</h3>
<p>$ sudo dockerd \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;storage-opt dm.thinp_percent=95</p>
<h3>dm.thinp_metapercent</h3>
<p>Sets the percentage of the passed in block device to use for metadata storage.</p>
<h3>Example:</h3>
<p>$ sudo dockerd \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;storage-opt dm.thinp_metapercent=1</p>
<h3>dm.thinp_autoextend_threshold</h3>
<p>Sets the value of the percentage of space used before lvm attempts to autoextend the available space [100 = disabled]</p>
<h3>Example:</h3>
<p>$ sudo dockerd \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;storage-opt dm.thinp_autoextend_threshold=80</p>
<h3>dm.thinp_autoextend_percent</h3>
<p>Sets the value percentage value to increase the thin pool by when lvm attempts to autoextend the available space [100 = disabled]</p>
<h3>Example:</h3>
<p>$ sudo dockerd \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;storage-opt dm.thinp_autoextend_percent=20</p>
<h3>dm.basesize</h3>
<p>Specifies the size to use when creating the base device, which limits the size of images and containers. The default value is 10G. Note, thin devices are inherently &quot;sparse&quot;, so a 10G device which is mostly empty doesn&#8217;t use 10 GB of space on the pool. However, the filesystem will use more space for base images the larger the device is. </p>
<p> The base device size can be increased at daemon restart which will allow all future images and containers (based on those new images) to be of the new base device size. </p>
<p> Example use: dockerd &#8211;storage-opt dm.basesize=50G </p>
<p> This will increase the base device size to 50G. The Docker daemon will throw an error if existing base device size is larger than 50G. A user can use this option to expand the base device size however shrinking is not permitted. </p>
<p> This value affects the system-wide &quot;base&quot; empty filesystem that may already be initialized and inherited by pulled images. Typically, a change to this value requires additional steps to take effect: </p>
<dl>
<dd>
<pre> $ sudo service docker stop
 $ sudo rm -rf /var/lib/docker
 $ sudo service docker start</pre>
</dl>
<p> Example use: dockerd &#8211;storage-opt dm.basesize=20G</p>
<h3>dm.fs</h3>
<p>Specifies the filesystem type to use for the base device. The supported options are ext4 and xfs. The default is ext4. </p>
<p> Example use: dockerd &#8211;storage-opt dm.fs=xfs</p>
<h3>dm.mkfsarg</h3>
<p>Specifies extra mkfs arguments to be used when creating the base device. </p>
<p> Example use: dockerd &#8211;storage-opt &quot;dm.mkfsarg=-O ^has_journal&quot;</p>
<h3>dm.mountopt</h3>
<p>Specifies extra mount options used when mounting the thin devices. </p>
<p> Example use: dockerd &#8211;storage-opt dm.mountopt=nodiscard</p>
<h3>dm.use_deferred_removal</h3>
<p>Enables use of deferred device removal if libdm and the kernel driver support the mechanism. </p>
<p> Deferred device removal means that if device is busy when devices are being removed/deactivated, then a deferred removal is scheduled on device. And devices automatically go away when last user of the device exits. </p>
<p> For example, when a container exits, its associated thin device is removed. If that device has leaked into some other mount namespace and can&#8217;t be removed, the container exit still succeeds and this option causes the system to schedule the device for deferred removal. It does not wait in a loop trying to remove a busy device. </p>
<p> Example use: dockerd &#8211;storage-opt dm.use_deferred_removal=true</p>
<h3>dm.use_deferred_deletion</h3>
<p>Enables use of deferred device deletion for thin pool devices. By default, thin pool device deletion is synchronous. Before a container is deleted, the Docker daemon removes any associated devices. If the storage driver can not remove a device, the container deletion fails and daemon returns. </p>
<p> Error deleting container: Error response from daemon: Cannot destroy container </p>
<p> To avoid this failure, enable both deferred device deletion and deferred device removal on the daemon. </p>
<p> dockerd &#8211;storage-opt dm.use_deferred_deletion=true &#8211;storage-opt dm.use_deferred_removal=true </p>
<p> With these two options enabled, if a device is busy when the driver is deleting a container, the driver marks the device as deleted. Later, when the device isn&#8217;t in use, the driver deletes it. </p>
<p> In general it should be safe to enable this option by default. It will help when unintentional leaking of mount point happens across multiple mount namespaces.</p>
<h3>dm.loopdatasize</h3>
<p><code>Note</code>: This option configures devicemapper loopback, which should not be used in production. </p>
<p> Specifies the size to use when creating the loopback file for the &quot;data&quot; device which is used for the thin pool. The default size is 100G. The file is sparse, so it will not initially take up this much space. </p>
<p> Example use: dockerd &#8211;storage-opt dm.loopdatasize=200G</p>
<h3>dm.loopmetadatasize</h3>
<p><code>Note</code>: This option configures devicemapper loopback, which should not be used in production. </p>
<p> Specifies the size to use when creating the loopback file for the &quot;metadata&quot; device which is used for the thin pool. The default size is 2G. The file is sparse, so it will not initially take up this much space. </p>
<p> Example use: dockerd &#8211;storage-opt dm.loopmetadatasize=4G</p>
<h3>dm.datadev</h3>
<p>(Deprecated, use dm.thinpooldev) </p>
<p> Specifies a custom blockdevice to use for data for a Docker-managed thin pool. It is better to use dm.thinpooldev &#8211; see the documentation for it above for discussion of the advantages.</p>
<h3>dm.metadatadev</h3>
<p>(Deprecated, use dm.thinpooldev) </p>
<p> Specifies a custom blockdevice to use for metadata for a Docker-managed thin pool. See dm.datadev for why this is deprecated.</p>
<h3>dm.blocksize</h3>
<p>Specifies a custom blocksize to use for the thin pool. The default blocksize is 64K. </p>
<p> Example use: dockerd &#8211;storage-opt dm.blocksize=512K</p>
<h3>dm.blkdiscard</h3>
<p>Enables or disables the use of blkdiscard when removing devicemapper devices. This is disabled by default due to the additional latency, but as a special case with loopback devices it will be enabled, in order to re-sparsify the loopback file on image/container removal. </p>
<p> Disabling this on loopback can lead to <i>much</i> faster container removal times, but it also prevents the space used in /var/lib/docker directory from being returned to the system for other use when containers are removed. </p>
<p> Example use: dockerd &#8211;storage-opt dm.blkdiscard=false</p>
<h3>dm.override_udev_sync_check</h3>
<p>By default, the devicemapper backend attempts to synchronize with the udev device manager for the Linux kernel. This option allows disabling that synchronization, to continue even though the configuration may be buggy. </p>
<p> To view the udev sync support of a Docker daemon that is using the devicemapper driver, run: </p>
<dl>
<dd>
<pre> $ docker info
 [...]
 Udev Sync Supported: true
 [...]</pre>
</dl>
<p> When udev sync support is true, then devicemapper and udev can coordinate the activation and deactivation of devices for containers. </p>
<p> When udev sync support is false, a race condition occurs between the devicemapper and udev during create and cleanup. The race condition results in errors and failures. (For information on these failures, see docker#4036 &lt;<a rel="nofollow" href="https://github.com/docker/docker/issues/4036">https://github.com/docker/docker/issues/4036</a>&gt;) </p>
<p> To allow the docker daemon to start, regardless of whether udev sync is false, set dm.override_udev_sync_check to true: </p>
<dl>
<dd>
<pre> $ dockerd --storage-opt dm.override_udev_sync_check=true</pre>
</dl>
<p> When this value is true, the driver continues and simply warns you the errors are happening. </p>
<p> <code>Note</code>: The ideal is to pursue a docker daemon and environment that does support synchronizing with udev. For further discussion on this topic, see docker#4036 &lt;<a rel="nofollow" href="https://github.com/docker/docker/issues/4036">https://github.com/docker/docker/issues/4036</a>&gt;. Otherwise, set this flag for migrating existing Docker daemons to a daemon with a supported environment.</p>
<h3>dm.min_free_space</h3>
<p>Specifies the min free space percent in a thin pool require for new device creation to succeed. This check applies to both free data space as well as free metadata space. Valid values are from 0% &#8211; 99%. Value 0% disables free space checking logic. If user does not specify a value for this option, the Engine uses a default value of 10%. </p>
<p> Whenever a new a thin pool device is created (during docker pull or during container creation), the Engine checks if the minimum free space is available. If the space is unavailable, then device creation fails and any relevant docker operation fails. </p>
<p> To recover from this error, you must create more free space in the thin pool to recover from the error. You can create free space by deleting some images and containers from tge thin pool. You can also add more storage to the thin pool. </p>
<p> To add more space to an LVM (logical volume management) thin pool, just add more storage to the group container thin pool; this should automatically resolve any errors. If your configuration uses loop devices, then stop the Engine daemon, grow the size of loop files and restart the daemon to resolve the issue. </p>
<p> Example use:: dockerd &#8211;storage-opt dm.min_free_space=10%</p>
<h3>dm.xfs_nospace_max_retries</h3>
<p>Specifies the maximum number of retries XFS should attempt to complete IO when ENOSPC (no space) error is returned by underlying storage device. </p>
<p> By default XFS retries infinitely for IO to finish and this can result in unkillable process. To change this behavior one can set xfs_nospace_max_retries to say 0 and XFS will not retry IO after getting ENOSPC and will shutdown filesystem. </p>
<p> Example use: </p>
<dl>
<dd>
<pre>$ sudo dockerd --storage-opt dm.xfs_nospace_max_retries=0</pre>
</dl>
<h3>dm.libdm_log_level</h3>
<p>Specifies the maxmimum libdm log level that will be forwarded to the dockerd log (as specified by &#8211;log-level). This option is primarily intended for debugging problems involving libdm. Using values other than the defaults may cause false-positive warnings to be logged. </p>
<p> Values specified must fall within the range of valid libdm log levels. At the time of writing, the following is the list of libdm log levels as well as their corresponding levels when output by dockerd. </p>
<table BORDER>
<tr VALIGN=top>
<td>libdm Level</td>
<td>Value</td>
<td>&#8211;log-level
</td>
</tr>
<tr VALIGN=top>
<td>_LOG_FATAL</td>
<td>2</td>
<td>error
</td>
</tr>
<tr VALIGN=top>
<td>_LOG_ERR</td>
<td>3</td>
<td>error
</td>
</tr>
<tr VALIGN=top>
<td>_LOG_WARN</td>
<td>4</td>
<td>warn
</td>
</tr>
<tr VALIGN=top>
<td>_LOG_NOTICE</td>
<td>5</td>
<td>info
</td>
</tr>
<tr VALIGN=top>
<td>_LOG_INFO</td>
<td>6</td>
<td>info
</td>
</tr>
<tr VALIGN=top>
<td>_LOG_DEBUG</td>
<td>7</td>
<td>debug
</td>
</tr>
</table>
<p> Example use: </p>
<dl>
<dd>
<pre>$ sudo dockerd \
 --log-level debug \
 --storage-opt dm.libdm_log_level=7</pre>
</dl>
<h2>ZFS options</h2>
<h3>zfs.fsname</h3>
<p>Set zfs filesystem under which docker will create its own datasets. By default docker will pick up the zfs filesystem where docker graph (/var/lib/docker) is located. </p>
<p> Example use: dockerd -s zfs &#8211;storage-opt zfs.fsname=zroot/docker</p>
<h2>Btrfs options</h2>
<h3>btrfs.min_space</h3>
<p>Specifies the minimum size to use when creating the subvolume which is used for containers. If user uses disk quota for btrfs when creating or running a container with <code>&#8211;storage-opt size</code> option, docker should ensure the <code>size</code> cannot be smaller than <code>btrfs.min_space</code>. </p>
<p> Example use: docker daemon -s btrfs &#8211;storage-opt btrfs.min_space=10G</p>
<h2>Cluster Store Options</h2>
<p>The daemon uses libkv to advertise the node within the cluster. Some Key/Value backends support mutual TLS, and the client TLS settings used by the daemon can be configured using the <code>&#8211;cluster-store-opt</code> flag, specifying the paths to PEM encoded files.</p>
<h3>kv.cacertfile</h3>
<p>Specifies the path to a local file with PEM encoded CA certificates to trust</p>
<h3>kv.certfile</h3>
<p>Specifies the path to a local file with a PEM encoded certificate. This certificate is used as the client cert for communication with the Key/Value store.</p>
<h3>kv.keyfile</h3>
<p>Specifies the path to a local file with a PEM encoded private key. This private key is used as the client key for communication with the Key/Value store.</p>
<h2>Access authorization</h2>
<p>Docker&#8217;s access authorization can be extended by authorization plugins that your organization can purchase or build themselves. You can install one or more authorization plugins when you start the Docker daemon using the &#8211;authorization-plugin=PLUGIN_ID option. </p>
<dl>
<dd>
<pre>dockerd --authorization-plugin=plugin1 --authorization-plugin=plugin2,...</pre>
</dl>
<p> The PLUGIN_ID value is either the plugin&#8217;s name or a path to its specification file. The plugin&#8217;s implementation determines whether you can specify a name or path. Consult with your Docker administrator to get information about the plugins available to you. </p>
<p> Once a plugin is installed, requests made to the daemon through the command line or Docker&#8217;s Engine API are allowed or denied by the plugin. If you have multiple plugins installed, each plugin, in order, must allow the request for it to complete. </p>
<p> For information about how to create an authorization plugin, see access authorization plugin &lt;<a rel="nofollow" href="https://docs.docker.com/engine/extend/plugins_authorization/">https://docs.docker.com/engine/extend/plugins_authorization/</a>&gt; section in the Docker extend section of this documentation.</p>
<h2>Runtime Execution Options</h2>
<p>You can configure the runtime using options specified with the &#8211;exec-opt flag. All the flag&#8217;s options have the native prefix. A single native.cgroupdriver option is available. </p>
<p> The native.cgroupdriver option specifies the management of the container&#8217;s cgroups. You can only specify cgroupfs or systemd. If you specify systemd and it is not available, the system errors out. If you omit the native.cgroupdriver option,cgroupfs is used on cgroup v1 hosts, systemd is used on cgroup v2 hosts with systemd available. </p>
<p> This example sets the cgroupdriver to systemd: </p>
<dl>
<dd>
<pre>$ sudo dockerd --exec-opt native.cgroupdriver=systemd</pre>
</dl>
<p> Setting this option applies to all containers the daemon launches.</p>
<h2>History</h2>
<p>Sept 2015, Originally compiled by Shishir Mahajan shishir.mahajan [at] redhat.com &lt;mailto:shishir.mahajan [at] redhat.com&gt; based on docker.com source material and internal work.</p>
