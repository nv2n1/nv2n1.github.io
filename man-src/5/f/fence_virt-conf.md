---
title: "fence_virt-conf(5)"
name: "fence_virt-conf"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fence_virt-conf/"
description: "fence_virt.conf – configuration file for fence_virtd"
---

<p>fence_virt.conf &#8211; configuration file for fence_virtd</p>
<h2>Description</h2>
<p>The fence_virt.conf file contains configuration information for fence_virtd, a fencing request routing daemon for clusters of virtual machines. The file is tree-structured. There are parent/child relationships and sibling relationships between the nodes. </p>
<pre><code>foo {
    bar {
        baz = &quot;1&quot;;
    }
}</code></pre>
<p> There are three primary sections of fence_virt.conf. </p>
<h2>Sections</h2>
<h3>fence_virtd</h3>
<p>This section contains global information about how fence_virtd is to operate. The most important pieces of information are as follows: </p>
<dl>
<dt><code>listener</code></dt>
<dd>the listener plugin for receiving fencing requests from clients </dd>
<dt><code>backend</code></dt>
<dd>the plugin to be used to carry out fencing requests </dd>
<dt><code>foreground</code></dt>
<dd>do not fork into the background. </dd>
<dt><code>wait_for_init</code></dt>
<dd>wait for the frontend and backends to become available rather than giving up immediately. This replaces wait_for_backend in 0.2.x. </dd>
<dt><code>module_path</code></dt>
<dd>the module path to search for plugins </dd>
</dl>
<h3>listeners</h3>
<p>This section contains listener-specific configuration information; see the section about listeners below.</p>
<h3>backends</h3>
<p>This section contains listener-specific configuration information; see the section about listeners below.</p>
<h3>groups</h3>
<p>This section contains static maps of which virtual machines may fence which other virtual machines; see the section about groups below.</p>
<h2>Listeners</h2>
<p>There are various listeners available for fence_virtd, each one handles decoding and authentication of a given fencing request. The following configuration blocks belong in the <code>listeners</code> section of fence_virt.conf</p>
<h3>multicast</h3>
<dl>
<dt><code>key_file</code></dt>
<dd>the shared key file to use (default: /etc/cluster/fence_xvm.key). </dd>
<dt><code>hash</code></dt>
<dd>the weakest hashing algorithm allowed for client requests. Clients may send packets with stronger hashes than the one specified, but not weaker ones. (default: sha256, but could be sha1, sha512, or none) </dd>
<dt><code>auth</code></dt>
<dd>the hashing algorithm to use for the simplistic challenge-response authentication (default: sha256, but could be sha1, sha512, or none) </dd>
<dt><code>family</code></dt>
<dd>the IP family to use (default: ipv4, but may be ipv6) </dd>
<dt><code>address</code></dt>
<dd>the multicast address to listen on (default: 225.0.0.12) </dd>
<dt><code>port</code></dt>
<dd>the multicast port to listen on (default: 1229) </dd>
<dt><code>interface</code></dt>
<dd>interface to listen on. By default, fence_virtd listens on all interfaces. However, this causes problems in some environments where the host computer is used as a gateway. </dd>
</dl>
<h3>serial</h3>
<p>The serial listener plugin utilizes libvirt&#8217;s serial (or VMChannel) mapping to listen for requests. When using the serial listener, it is necessary to add a serial port (preferably pointing to /dev/ttyS1) or a channel (preferrably pointing to 10.0.2.179:1229) to the libvirt domain description. Note that only type <code>unix</code> , mode <code>bind</code> serial ports and channels are supported. Example libvirt XML: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;<code>serial</code>&nbsp;<wbr>type=&#8217;unix&#8217;&gt;<br/>
&nbsp;<wbr>&lt;source mode=&#8217;bind&#8217;&nbsp;<wbr>path=&#8217;/sandbox/guests/fence_socket_molly&#8217;/&gt;<br/>
&nbsp;<wbr>&lt;target port=&#8217;1&#8217;/&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>&lt;/serial&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>&lt;<code>channel</code>&nbsp;<wbr>type=&#8217;unix&#8217;&gt;<br/>
&nbsp;<wbr>&lt;source mode=&#8217;bind&#8217;&nbsp;<wbr>path=&#8217;/sandbox/guests/fence_molly_vmchannel&#8217;/&gt;<br/>
&nbsp;<wbr>&lt;target type=&#8217;guestfwd&#8217;&nbsp;<wbr>address=&#8217;10.0.2.179&#8242;&nbsp;<wbr>port=&#8217;1229&#8217;/&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>&lt;/channel&gt; </p>
<dl>
<dt><code>uri</code></dt>
<dd>the URI to use when connecting to libvirt by the serial plugin. </dd>
<dt><code>path</code></dt>
<dd>The same directory that is defined for the domain serial port path (From example above: /sandbox/guests). Sockets must reside in this directory in order to be considered valid. This can be used to prevent fence_virtd from using the wrong sockets. </dd>
<dt><code>mode</code></dt>
<dd>This selects the type of sockets to register. Valid values are &quot;serial&quot; (default) and &quot;vmchannel&quot;. </dd>
</dl>
<h3>tcp</h3>
<p>The tcp plugin was designed to be used with vios-proxy. vios-proxy uses a virtio-serial channel to proxy TCP connections between guests and a host. In order to use the tcp plugin, vios-proxy-host must be running on all the physical cluster nodes, and vios-proxy-guest must be running on all guest cluster nodes. Prior to running vios-proxy-host or vios-proxy-guest, the virtio-serial channel and host sockets must be configured for all guest domains. Example libvirt XML: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;<code>controller</code>&nbsp;<wbr>type=&#8217;virtio-serial&#8217;&nbsp;<wbr>index=&#8217;0&#8242;&gt;<br/>
&nbsp;<wbr>&lt;address type=&#8217;pci&#8217;&nbsp;<wbr>domain=&#8217;0x0000&#8242;&nbsp;<wbr>bus=&#8217;0x00&#8242;&nbsp;<wbr>slot=&#8217;0x08&#8242;&nbsp;<wbr>function=&#8217;0x0&#8217;/&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>&lt;/controller&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;<code>channel</code>&nbsp;<wbr>type=&#8217;unix&#8217;&gt;<br/>
&nbsp;<wbr>&lt;source mode=&#8217;bind&#8217;&nbsp;<wbr>path=&#8217;/sandbox/fence_virt/guests/fence_socket_guest1&#8242;&nbsp;<wbr>id=&#8217;guest1&#8217;/&gt;<br/>
&nbsp;<wbr>&lt;target type=&#8217;virtio&#8217;&nbsp;<wbr>name=&#8217;org.redhat.fencevirt.node.1&#8217;/&gt;<br/>
&nbsp;<wbr>&lt;address type=&#8217;virtio-serial&#8217;&nbsp;<wbr>controller=&#8217;0&#8242;&nbsp;<wbr>bus=&#8217;0&#8242;&nbsp;<wbr>port=&#8217;1&#8217;/&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>&lt;/channel&gt; </p>
<dl>
<dt><code>key_file</code></dt>
<dd>the shared key file to use (default: /etc/cluster/fence_xvm.key). </dd>
<dt><code>hash</code></dt>
<dd>the hashing algorithm to use for packet signing (default: sha256, but could be sha1, sha512, or none) </dd>
<dt><code>auth</code></dt>
<dd>the hashing algorithm to use for the simplistic challenge-response authentication (default: sha256, but could be sha1, sha512, or none) </dd>
<dt><code>family</code></dt>
<dd>the IP family to use (default: ipv4, but may be ipv6) </dd>
<dt><code>address</code></dt>
<dd>the IP address to listen on (default: 127.0.0.1) </dd>
<dt><code>port</code></dt>
<dd>the TCP port to listen on (default: 1229) </dd>
</dl>
<h2>Backends</h2>
<p>There are various backends available for fence_virtd, each one handles routing a fencing request to a hypervisor or management tool. The following configuration blocks belong in the <code>backends</code> section of fence_virt.conf</p>
<h3>libvirt</h3>
<p>The libvirt plugin is the simplest plugin. It is used in environments where routing fencing requests between multiple hosts is not required, for example by a user running a cluster of virtual machines on a single desktop computer. </p>
<dl>
<dt><code>uri</code></dt>
<dd>the URI to use when connecting to libvirt. </dd>
</dl>
<h3>libvirt-qmf</h3>
<p>The libvirt-qmf plugin acts as a QMFv2 Console to the libvirt-qmf daemon in order to route fencing requests over AMQP to the appropriate computer. </p>
<dl>
<dt><code>host</code></dt>
<dd>host or IP address of qpid broker. Defaults to 127.0.0.1. </dd>
<dt><code>port</code></dt>
<dd>IP port of qpid broker. Defaults to 5672. </dd>
<dt><code>username</code></dt>
<dd>Username for GSSAPI, if configured. </dd>
<dt><code>service</code></dt>
<dd>Qpid service to connect to. </dd>
<dt><code>gssapi</code></dt>
<dd>If set to 1, have fence_virtd use GSSAPI for authentication when communicating with the Qpid broker. Default is 0 (off). </dd>
</dl>
<h3>checkpoint</h3>
<p>The checkpoint plugin uses CMAN, CPG, and OpenAIS checkpoints to track virtual machines and route fencing requests to the appropriate computer. </p>
<dl>
<dt><code>uri</code></dt>
<dd>the URI to use when connecting to libvirt by the checkpoint plugin. </dd>
<dt><code>name_mode</code></dt>
<dd>The checkpoint plugin, in order to retain compatibility with fence_xvm, stores virtual machines in a certain way in the OpenAIS checkpoints. The default was to use &#8216;name&#8217; when using fence_xvm and fence_xvmd, and so this is still the default. However, it is strongly recommended to use &#8216;uuid&#8217; instead of &#8216;name&#8217; in all cluster environments involving more than one physical host in order to avoid the potential for name collisions. </dd>
</dl>
<h2>Groups</h2>
<p>Fence_virtd supports static maps which allow grouping of VMs. The groups are arbitrary and are checked at fence time. Any member of a group may fence any other member. Hosts may be assigned to multiple groups if desired.</p>
<h3>group</h3>
<p>This defines a group. </p>
<dl>
<dt><code>uuid</code></dt>
<dd>defines UUID as a member of a group. </dd>
<dt><code>ip</code></dt>
<dd>defines an IP which is allowed to send fencing requests for members of this group (e.g. for multicast). It is highly recommended that this be used in conjunction with a key file. </dd>
</dl>
<h2>Example</h2>
<p>fence_virtd {<br/>
    listener = &quot;multicast&quot;;<br/>
    backend = &quot;checkpoint&quot;;</p>
<p>}<br/>
&nbsp;<wbr>#&nbsp;<wbr>this is the listeners section </p>
<pre><code>listeners {
    multicast {
        key_file = &quot;/etc/cluster/fence_xvm.key&quot;;
    }
}
backends {
    libvirt {
        uri = &quot;qemu:///system&quot;;
    }
}
groups {
    group {
        ip = &quot;192.168.1.1&quot;;
        uuid = &quot;44179d3f-6c63-474f-a212-20c8b4b25b16&quot;;
        uuid = &quot;1ce02c4b-dfa1-42cb-b5b1-f0b1091ece60&quot;;
    }
}
</code></pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence_virtd/">fence_virtd</a>(8), <a href="/docs/linux/man/8-fence_virt/">fence_virt</a>(8), <a href="/docs/linux/man/8-fence_xvm/">fence_xvm</a>(8), fence(8) </p>
