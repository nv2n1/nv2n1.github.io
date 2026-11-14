---
title: "interfaces(5)"
name: "interfaces"
section: "5"
letter: "i"
url: "/docs/linux/man/5-interfaces/"
description: "/etc/network/interfaces – network interface configuration for ifup and ifdown"
---

<p>/etc/network/interfaces &#8211; network interface configuration for ifup and ifdown</p>
<h2>Description</h2>
<p>/etc/network/interfaces contains network interface configuration information for the <code><a href="/docs/linux/man/8-ifup/">ifup</a></code>(8) and <code><a href="/docs/linux/man/8-ifdown/">ifdown</a></code>(8) commands. This is where you configure how your system is connected to the network.</p>
<h2>Example</h2>
<p>The following example configures two network interfaces: eth0 is brought up at boot, and uses DHCP for IPv4 and SLAAC for IPv6, whereas eth1 is brought up whenever the network hardware is detected, and is configured with static IPv4 and IPv6 addresses.</p>
<dl>
<dd>
<pre>auto eth0
allow-hotplug eth1
iface eth0 inet dhcp
iface eth0 inet6 auto
iface eth1 inet static
 address 192.168.1.2/24
 gateway 192.168.1.1
iface eth1 inet6 static
 address fec0:0:0:1::2/64
 gateway fec0:0:0:1::1</pre>
</dl>
<h2>File Format</h2>
<p>Lines starting with `#&#8217; are ignored. Note that end-of-line comments are NOT supported, comments must be on a line of their own. </p>
<p> A line may be extended across multiple lines by making the last character a backslash. </p>
<p> The file consists of zero or more &quot;iface&quot;, &quot;mapping&quot;, &quot;auto&quot;, &quot;allow-&quot;, &quot;rename&quot;, &quot;source&quot; and &quot;source-directory&quot; stanzas. These will be described in more detail in the following sections.</p>
<h2>Interface Selection</h2>
<p>Lines beginning with the word &quot;auto&quot; are used to identify the physical interfaces to be brought up when <code>ifup</code> is run with the <code>-a</code> option. (This option is also used by the system boot scripts, so interfaces marked &quot;auto&quot; are brought up at boot time.) Physical interface names should follow the word &quot;auto&quot; on the same line. There can be multiple &quot;auto&quot; stanzas. <code>ifup</code> brings the named interfaces up in the order listed. </p>
<p> Lines beginning with &quot;allow-&quot; are used to identify interfaces that should be brought up automatically by various subsystems. This may be done using a command such as &quot;ifup &#8211;allow=hotplug eth0 eth1&quot;, which will only bring up eth0 or eth1 if it is listed in an &quot;allow-hotplug&quot; line. Note that &quot;allow-auto&quot; and &quot;auto&quot; are synonyms. (Interfaces marked &quot;allow-hotplug&quot; are brought up when udev detects them. This can either be during boot if the interface is already present, or at a later time, for example when plugging in a USB network card. Please note that this does not have anything to do with detecting a network cable being plugged in.) </p>
<p> Lines beginning with &quot;no-auto-down&quot; are used to identify interfaces that should not be brought down by the command &quot;ifdown -a&quot;. Its main use is to prevent an interface from being brought down during system shutdown time, for example if the root filesystem is a network filesystem and the interface should stay up until the very end. Note that you can still bring down the interface by specifying the interface name explicitly. </p>
<p> Lines beginning with &quot;no-scripts&quot; are used to identify interfaces for which scripts in <i>/etc/network/if-*.d/</i> should not be run when those interfaces are brought up or down. he above will match eth0 and eth1, and will bring up both interfaces using the &quot;iface eth&quot; stanza.</p>
<h2>Interface Renaming</h2>
<p>Lines beginning with &quot;rename&quot; are used to rename interfaces. It takes one or more arguments in the form of &quot;CUR=NEW&quot;, where CUR is the name of an existing interface, and NEW is the new name. This becomes very powerful when combined with pattern matching for the CUR interface. </p>
<p> Interfaces are renamed whenever &quot;ifup&quot; is called. Renaming logically happens before anything else is done. So if an interface is started with the name &quot;foo&quot;, and it has to be renamed to &quot;bar&quot; and brought up at boot time, then one should use the following /etc/network/interfaces file: </p>
<dl>
<dd>
<pre>rename foo=bar
auto bar
iface bar ...</pre>
</dl>
<p> However, if the interface is not renamed yet, it is possible to use both &quot;ifup foo&quot; and &quot;ifup bar&quot;. The former command will then automatically be converted to the latter. This is mainly useful when ifup is called automatically whenever an interface is hotplugged. </p>
<p> Interface renaming only works if the operating system supports it, if an interface is not renamed to another existing interface, and may require that the interface that is to be renamed has not been brought up yet. If ifup tries to rename an interface and it fails, it will exit with an error.</p>
<h2>Including Other Files</h2>
<p>Lines beginning with &quot;source&quot; are used to include stanzas from other files, so configuration can be split into many files. The word &quot;source&quot; is followed by the path of file to be sourced. Shell wildcards can be used. (See <code><a href="/docs/linux/man/3-wordexp/">wordexp</a></code>(3) for details.) </p>
<p> Similarly, &quot;source-directory&quot; keyword is used to source multiple files at once, without specifying them individually or using shell globs. Additionally, when &quot;source-directory&quot; is used, names of the files are checked to match the following regular expression: <i>^[a-zA-Z0-9_-]+$</i>. In other words, the names must consist entirely of ASCII upper- and lower-case letters, ASCII digits, ASCII underscores, and ASCII minus-hyphens. In the directory path, shell wildcards may be used as well. </p>
<p> When sourcing files or directories, if a path doesn&#8217;t have a leading slash, it&#8217;s considered relative to the directory containing the file in which the keyword is placed. In the example above, if the file is located at <i>/etc/network/interfaces</i>, paths to the included files are understood to be under <i>/etc/network</i>. </p>
<p> By default, on a freshly installed Debian system, the interfaces file includes a line to source files in the <i>/etc/network/interfaces.d</i> directory.</p>
<h2>Mappings</h2>
<p>Stanzas beginning with the word &quot;mapping&quot; are used to determine how a logical interface name is chosen for a physical interface that is to be brought up. The first line of a mapping stanza consists of the word &quot;mapping&quot; followed by a pattern in shell glob syntax. Each mapping stanza must contain a <code>script</code> definition. The named script is run with the physical interface name as its argument and with the contents of all following &quot;map&quot; lines (<code>without</code> the leading &quot;map&quot;) in the stanza provided to it on its standard input. The script must print a string on its standard output before exiting. See <i>/usr/share/doc/ifupdown/examples</i> for examples of what the script must print. </p>
<p> Mapping a name consists of searching the remaining mapping patterns and running the script corresponding to the first match; the script outputs the name to which the original is mapped. </p>
<p> <code>ifup</code> is normally given a physical interface name as its first non-option argument. <code>ifup</code> also uses this name as the initial logical name for the interface unless it is accompanied by a suffix of the form <i>=LOGICAL</i>, in which case ifup chooses <i>LOGICAL</i> as the initial logical name for the interface. It then maps this name, possibly more than once according to successive mapping specifications, until no further mappings are possible. If the resulting name is the name of some defined logical interface then <code>ifup</code> attempts to bring up the physical interface as that logical interface. Otherwise <code>ifup</code> exits with an error.</p>
<h2>Interface Definitions</h2>
<p>Stanzas defining logical interfaces start with a line consisting of the word &quot;iface&quot; followed by the name of the logical interface. In simple configurations without mapping stanzas this name should simply be the name of the physical interface to which it is to be applied. (The default mapping script is, in effect, the <code>echo</code> command.) The interface name is followed by the name of the address family that the interface uses. This will be &quot;inet&quot; for TCP/IP networking, but there is also some support for IPX networking (&quot;ipx&quot;), and IPv6 networking (&quot;inet6&quot;). Following that is the name of the method used to configure the interface. </p>
<p> Additional options can be given on subsequent lines in the stanza. Which options are available depends on the family and method, as described below. Additional options can be made available by other Debian packages. For example, the wireless-tools package makes available a number of options prefixed with &quot;wireless-&quot; which can be used to configure the interface using <code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8)<code>.</code> (See <code><a href="/docs/linux/man/7-wireless/">wireless</a></code>(7) for details.) A list of packages providing additional options is mentioned in the section &quot;OPTIONS PROVIDED BY OTHER PACKAGE&quot;. </p>
<p> Options are usually indented for clarity (as in the example above) but are not required to be. </p>
<p> Multiple &quot;iface&quot; stanzas can be given for the same interface, in which case all of the configured addresses and options for that interface will be applied when bringing up that interface. This is useful to configure both IPv4 and IPv6 addresses on the same interface (although if no inet6 stanza is present, the kernel will normally still perform stateless address autoconfiguration if there is an IPv6 route advertisement daemon on the network). It can also be used to configure multiple addresses of the same type on a single interface.</p>
<h2>Interface Templates</h2>
<p>It is possible to define interface definition templates and extend them using the <code>inherits</code> keyword: </p>
<dl>
<dd>
<pre>iface ethernet inet static
 mtu 1500
 hwaddress 11:22:33:44:55:66
iface eth0 inet static inherits ethernet
 address 192.168.1.2/24</pre>
</dl>
<p> This may be useful to separate link-level settings shared by multiple interfaces from, for example, IP address settings specific to every interface.</p>
<h2>Pattern Matching Interfaces</h2>
<p>It is possible to use patterns to match one or more real interfaces. These patterns can currently appear in lines beginning with &quot;auto&quot;, &quot;allow-&quot;, &quot;rename&quot; and on the command line. A pattern has the following format (see below for exceptions for GNU/Hurd): </p>
<dl>
<dd>
<pre>[VARIABLE]/VALUE[/[OPTIONS]][=LOGICAL]</pre>
</dl>
<p> If no VARIABLE is given, this pattern will match interface names against the given VALUE. VALUE can contain wildcard patterns such as ? and *, see the <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3) function. When <code>ifup</code> or <code>ifdown</code> is run, patterns are replaces by all real interfaces that are currently known to the operating system kernel and whose names match the pattern. For example, given the following line: </p>
<dl>
<dd>
<pre>auto /eth*</pre>
</dl>
<p> If the kernel knows about the interfaces with names lo, eth0 and eth1, then the above line is then interpreted as: </p>
<dl>
<dd>
<pre>auto eth0 eth1</pre>
</dl>
<p> Note that there must still be valid &quot;iface&quot; stanzas for each matching interface. However, it is possible to combine a pattern with a mapping to a logical interface, like so: </p>
<dl>
<dd>
<pre>auto /eth*=eth
iface eth inet dhcp</pre>
</dl>
<p> Valid variable names are &quot;mac&quot;, in which case value is matched against the interface&#8217;s MAC address. On Linux, the variable name can also be any filename in /sys/class/net/&lt;iface&gt;/, in which case the value is matched against the contents of the corresponding file. </p>
<p> The OPTIONS field currently only supports a number. If given, only the n-th interface that has a matching value will actually be used, where n is the number given, starting at 1. So /eth*/1 will match the first interface whose name starts with eth. </p>
<p> On GNU/Hurd, interface names start with /dev/, and this obviously clashes with the format for patterns. To ensure an interface name like /dev/eth0 does not get interpreted as a pattern, any pattern that starts with /dev/ is ignored, and instead interpreted as a literal interface name. To make a pattern that matches interface names on GNU/Hurd, use something like: </p>
<dl>
<dd>
<pre>auto /?dev?eth*=eth
iface eth inet dhcp</pre>
</dl>
<h2>Vlan Interfaces</h2>
<p>To ease the configuration of VLAN interfaces, interfaces having <code>.</code> (full stop character) in the name are configured as 802.1q tagged virtual LAN interface. For example, interface <code>eth0.1</code> is a virtual interface with VLAN ID 1 having <code>eth0</code> as its parent interface. </p>
<p> VLAN interfaces are mostly treated as independent interfaces. As such, a VLAN interface is normally not automatically brought up when its parent interface is brought up. The exception is when ifup is called with the &#8211;allow option, in which case all VLAN interfaces that are in the same allow class as the parent interface are brought up together with the parent interface. For example: </p>
<dl>
<dd>
<pre>allow-hotplug eth0 eth0.1
iface eth0 inet static
 address ...
iface eth0.1 inet static
 address ...
iface eth0.2 inet static
 address ...</pre>
</dl>
<p> In the above example, when &quot;ifup &#8211;allow hotplug eth0&quot; is called (either manually or because udev triggers this when a network device is hotplugged), the interface eth0 and the VLAN interface eth0.1 are brought up, but eth0.2 is not. </p>
<p> Keep in mind that pattern matching will only match interfaces the kernel knows about, so it is not possible to specify &quot;auto /eth0.*&quot; and have all VLAN interfaces for eth0 be brought up at boot time. Another way to ensure that a VLAN interface is brought up automatically when the parent interface is brought up, is to use a recursive call to ifup, like so: </p>
<dl>
<dd>
<pre>iface eth0 inet manual
 up ifup eth0.3
iface eth0.3 inet static
 address ...</pre>
</dl>
<p> Note that there is no need to add an explicit call to ifdown, since VLAN interfaces are automatically brought down whenever their parent interfaces are brought down.</p>
<h2>Iface Options</h2>
<p>The following &quot;command&quot; options are available for every family and method. Each of these options can be given multiple times in a single stanza, in which case the commands are executed in the order in which they appear in the stanza. (You can ensure a command never fails by suffixing them with &quot;|| true&quot;.)</p>
<dl>
<dt><code>pre-up</code><i> command</i></p>
<dd>Run <i>command</i> before bringing the interface up. If this command fails then <code>ifup</code> aborts, refraining from marking the interface as configured, prints an error message, and exits with status 0. This behavior may change in the future.</p>
<dt><code>up</code><i> command</i></p>
<dd>
<dt><code>post-up</code><i> command</i></p>
<dd>Run <i>command</i> after bringing the interface up. If this command fails then <code>ifup</code> aborts, refraining from marking the interface as configured (even though it has really been configured), prints an error message, and exits with status 0. This behavior may change in the future.</p>
<dt><code>down</code><i> command</i></p>
<dd>
<dt><code>pre-down</code><i> command</i></p>
<dd>Run <i>command</i> before taking the interface down. If this command fails then <code>ifdown</code> aborts, marks the interface as deconfigured (even though it has not really been deconfigured), and exits with status 0. This behavior may change in the future.</p>
<dt><code>post-down</code><i> command</i></p>
<dd>Run <i>command</i> after taking the interface down. If this command fails then <code>ifdown</code> aborts, marks the interface as deconfigured, and exits with status 0. This behavior may change in the future.</p>
<dt><code>description</code><i> name</i></p>
<dd>Alias interface by <i>name</i></dl>
<h2>Hook Scripts</h2>
<p>There are four directories in which scripts can be placed which will always be run for any interface during certain phases of ifup and ifdown commands. These are:</p>
<dl>
<dt><i>/etc/network/if-pre-up.d/</i></p>
<dd>Scripts in this directory are run before bringing the interface up.</p>
<dt><i>/etc/network/if-up.d/</i></p>
<dd>Scripts in this directory are run after bringing the interface up.</p>
<dt><i>/etc/network/if-down.d/</i></p>
<dd>Scripts in this directory are run before bringing the interface down.</p>
<dt><i>/etc/network/if-post-down.d/</i></p>
<dd>Scripts in this directory are run after bringing the interface down.</dl>
<p> The scripts in which are run (with no arguments) using <code><a href="/docs/linux/man/8-run-parts/">run-parts</a></code>(8) after the corresponding <code>pre-up</code>, <code>up</code>, <code>down</code> and <code>post-down</code> options in the <i>/etc/network/interfaces</i> file itself have been processed. Please note that as <code>post-up</code> and <code>pre-down</code> are aliases, no files in the corresponding directories are processed. Please use <i>if-up.d</i> and <i>if-down.d</i> directories instead.</p>
<h2>Environment Variables</h2>
<p>All hook scripts, and the commands executed by <code>pre-up</code>, <code>up</code>, <code>post-up</code>, <code>pre-down</code>, <code>down</code> and <code>post-down</code> have access to the following environment variables:</p>
<dl>
<dt><code>IFACE</code></p>
<dd>The physical name of the interface being processed, or &quot;&#8211;all&quot; (see below).</p>
<dt><code>LOGICAL</code></p>
<dd>The logical name of the interface being processed, or &quot;auto&quot; (see below).</p>
<dt><code>ADDRFAM</code></p>
<dd>The address family of the interface, or &quot;meta&quot; (see below).</p>
<dt><code>METHOD</code></p>
<dd>The method of the interface (e.g., <i>static</i>), or &quot;none&quot; (see below).</p>
<dt><code>CLASS</code></p>
<dd>The class of interfaces being processed. This is a copy of the value given to the <code>&#8211;allow</code> option when running ifup or ifdown, otherwise it is set to &quot;auto&quot; when the <code>&#8211;all</code> option is used.</p>
<dt><code>CLASS</code></p>
<dd>The class of interfaces being processed. This is a copy of the value given to the <code>&#8211;allow</code> option when running ifup or ifdown, otherwise it is set to &quot;auto&quot; when the <code>&#8211;all</code> option is used.</p>
<dt><code>MODE</code></p>
<dd><i>start</i> if run from ifup, <i>stop</i> if run from ifdown.</p>
<dt><code>PHASE</code></p>
<dd>As per MODE, but with finer granularity, distinguishing the <i>pre-up</i>, <i>post-up</i>, <i>pre-down</i> and <i>post-down</i> phases.</p>
<dt><code>VERBOSITY</code></p>
<dd>Indicates whether <code>&#8211;verbose</code> was used; set to 1 if so, 0 if not.</p>
<dt><code>PATH</code></p>
<dd>The command search path: <i>/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin</i></dl>
<p> Additionally, all options given in an interface definition stanza are exported to the environment in upper case with &quot;IF_&quot; prepended and with hyphens converted to underscores and non-alphanumeric characters discarded. </p>
<p> When ifupdown is being called with the <code>&#8211;all</code> option, before doing anything to interfaces, it calls all the hook scripts (<i>pre-up</i> or <i>down</i>) with <code>IFACE</code> set to &quot;&#8211;all&quot;, <code>LOGICAL</code> set to the current value of &#8211;allow parameter (or &quot;auto&quot; if it&#8217;s not set), <code>ADDRFAM</code>=&quot;meta&quot; and <code>METHOD</code>=&quot;none&quot;. After all the interfaces have been brought up or taken down, the appropriate scripts (<i>up</i> or <i>post-down</i>) are executed.</p>
<h2>Concurrency And Parallel Execution</h2>
<p>Ifupdown uses per-interface locking to ensure that concurrent ifup and ifdown calls to the same interface are run in serial. However, calls to different interfaces will be able to run in parallel. It is therefore important that any hook scripts and <i>pre-up</i>, <i>up</i>, <i>down</i> and <i>post-down</i> commands are written with the possibility of parallel execution in mind. </p>
<p> It is allowed to recursively call <code>ifup</code> and <code>ifdown</code> from hook scripts and interface commands, as long as these calls refer to a different interface than the one that is already being (de)configured. Loops are detected and will result in the call failing instead of a deadlock, although it is best if one does not rely on that.</p>
<h2>Options Provided By Other Packages</h2>
<p>This manual page documents the configuration options provided by the ifupdown package. However, other packages can make other options available for use in /etc/network/interfaces. Here is a list of packages that provide such extensions: </p>
<p> arping, avahi-autoipd, avahi-daemon, bind9, bridge-utils, clamav-freshclam, controlaula, epoptes-client, ethtool, guidedog, hostap-utils, hostapd, htpdate, ifenslave, ifmetric, ifupdown-extra, ifupdown-multi, ifupdown-scripts-zg2, initscripts, isatapd, linux-wlan-ng, lprng, macchanger, miredo, nslcd, ntpdate, openntpd, openresolv, openssh-server, openvpn, openvswitch-switch, postfix, resolvconf, sendmail-base, shorewall-init, slrn, slrnpull, tinc, ucarp, uml-utilities, uruk, vde2, vlan, vzctl, whereami, wide-dhcpv6-client, wireless-tools, wpasupplicant. </p>
<p> Please consult the documentation of those packages for information about how they extend ifupdown.</p>
<h2>Inet Address Family</h2>
<p>This section documents the methods available in the inet address family.</p>
<h3>The loopback Method</h3>
<p>This method may be used to define the IPv4 loopback interface. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt>(No options)</p>
<dd></dl>
</dl>
<h3>The static Method</h3>
<p>This method may be used to define Ethernet interfaces with statically allocated IPv4 addresses. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>address</code><i> address </i></p>
<dd>Address (dotted quad/netmask) <code>required</code></p>
<dt><code>netmask</code><i> mask </i></p>
<dd>Netmask (dotted quad or number of bits) <code>deprecated</code></p>
<dt><code>broadcast</code><i> broadcast_address</i></p>
<dd>Broadcast address (dotted quad, + or -) <code>deprecated</code>. Default value: &quot;+&quot;</p>
<dt><code>metric</code><i> metric </i></p>
<dd>Routing metric for default gateway (integer)</p>
<dt><code>gateway</code><i> address </i></p>
<dd>Default gateway (dotted quad)</p>
<dt><code>pointopoint</code><i> address </i></p>
<dd>Address of other end point (dotted quad). Note the spelling of &quot;point-to&quot;.</p>
<dt><code>hwaddress</code><i> address </i></p>
<dd>Link local address or &quot;random&quot;.</p>
<dt><code>mtu</code><i> size </i></p>
<dd>MTU size</p>
<dt><code>scope</code></p>
<dd>Address validity scope. Possible values: global, link, host</dl>
</dl>
<h3>The manual Method</h3>
<p>This method may be used to define interfaces for which no configuration is done by default. Such interfaces can be configured manually by means of <code>up</code> and <code>down</code> commands or /etc/network/if-*.d scripts. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>hwaddress</code><i> address </i></p>
<dd>Link local address or &quot;random&quot;.</p>
<dt><code>mtu</code><i> size </i></p>
<dd>MTU size</dl>
</dl>
<h3>The dhcp Method</h3>
<p>This method may be used to obtain an address via DHCP with any of the tools: dhclient, pump, udhcpc, dhcpcd. (They have been listed in their order of precedence.) If you have a complicated DHCP setup you should note that some of these clients use their own configuration files and do not obtain their configuration information via <code>ifup</code>. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>hostname</code><i> hostname </i></p>
<dd>Hostname to be requested (pump, dhcpcd, udhcpc)</p>
<dt><code>metric</code><i> metric </i></p>
<dd>Metric for added routes (dhclient)</p>
<dt><code>leasehours</code><i> leasehours </i></p>
<dd>Preferred lease time in hours (pump)</p>
<dt><code>leasetime</code><i> leasetime </i></p>
<dd>Preferred lease time in seconds (dhcpcd)</p>
<dt><code>vendor</code><i> vendor </i></p>
<dd>Vendor class identifier (dhcpcd)</p>
<dt><code>client</code><i> client </i></p>
<dd>Client identifier (dhcpcd)</p>
<dt><code>hwaddress</code><i> address </i></p>
<dd>Hardware address.</dl>
</dl>
<h3>The bootp Method</h3>
<p>This method may be used to obtain an address via bootp. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>bootfile</code><i> file </i></p>
<dd>Tell the server to use <i>file</i> as the bootfile.</p>
<dt><code>server</code><i> address</i></p>
<dd>Use the IP address <i>address</i> to communicate with the server.</p>
<dt><code>hwaddr</code><i> addr </i></p>
<dd>Use <i>addr</i> as the hardware address instead of whatever it really is.</dl>
</dl>
<h3>The tunnel Method</h3>
<p>This method is used to create GRE or IPIP tunnels. You need to have the <code>ip</code> binary from the <code>iproute</code> package. For GRE tunnels, you will need to load the ip_gre module and the ipip module for IPIP tunnels. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>address</code><i> address </i></p>
<dd>Local address (dotted quad) <code>required</code></p>
<dt><code>mode</code><i> type </i></p>
<dd>Tunnel type (either GRE or IPIP) <code>required</code></p>
<dt><code>endpoint</code><i> address </i></p>
<dd>Address of other tunnel endpoint <code>required</code></p>
<dt><code>dstaddr</code><i> address </i></p>
<dd>Remote address (remote address inside tunnel)</p>
<dt><code>local</code><i> address </i></p>
<dd>Address of the local endpoint</p>
<dt><code>metric</code><i> metric </i></p>
<dd>Routing metric for default gateway (integer)</p>
<dt><code>gateway</code><i> address </i></p>
<dd>Default gateway</p>
<dt><code>ttl</code><i> time </i></p>
<dd>TTL setting</p>
<dt><code>mtu</code><i> size </i></p>
<dd>MTU size</dl>
</dl>
<h3>The ppp Method</h3>
<p>This method uses pon/poff to configure a PPP interface. See those commands for details. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>provider</code><i> name </i></p>
<dd>Use <i>name</i> as the provider (from /etc/ppp/peers).</p>
<dt><code>unit</code><i> number </i></p>
<dd>Use <i>number</i> as the ppp unit number.</p>
<dt><code>options</code><i> string</i></p>
<dd>Pass <i>string</i> as additional options to pon.</dl>
</dl>
<h3>The wvdial Method</h3>
<p>This method uses wvdial to configure a PPP interface. See that command for more details. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>provider</code><i> name </i></p>
<dd>Use <i>name</i> as the provider (from /etc/wvdial.conf).</dl>
</dl>
<h3>The ipv4ll Method</h3>
<p>This method uses avahi-autoipd to configure an interface with an IPv4 Link-Layer address (169.254.0.0/16 family). This method is also known as APIPA or IPAC, and often colloquially referred to as &quot;Zeroconf address&quot;. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt>(No options)</p>
<dd></dl>
</dl>
<h2>Ipx Address Family</h2>
<p>This section documents the methods available in the ipx address family.</p>
<h3>The static Method</h3>
<p>This method may be used to setup an IPX interface. It requires the <i>ipx_interface</i> command. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>frame</code><i> type </i></p>
<dd><i>type</i> of Ethernet frames to use (e.g. <code>802.2</code>)</p>
<dt><code>netnum</code><i> id </i></p>
<dd>Network number</dl>
</dl>
<h3>The dynamic Method</h3>
<p>This method may be used to setup an IPX interface dynamically. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>frame</code><i> type </i></p>
<dd><i>type</i> of Ethernet frames to use (e.g. <code>802.2</code>)</dl>
</dl>
<h2>Inet6 Address Family</h2>
<p>This section documents the methods available in the inet6 address family.</p>
<h3>The auto Method</h3>
<p>This method may be used to define interfaces with automatically assigned IPv6 addresses. Using this method on its own doesn&#8217;t mean that RDNSS options will be applied, too. To make this happen, <code>rdnssd</code> daemon must be installed, properly configured and running. If stateless DHCPv6 support is turned on, then additional network configuration parameters such as DNS and NTP servers will be retrieved from a DHCP server. Please note that on ifdown, the lease is not currently released (a known bug). </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>privext</code><i> int </i></p>
<dd>Privacy extensions (RFC4941) (0=off, 1=assign, 2=prefer)</p>
<dt><code>accept_ra</code><i> int </i></p>
<dd>Accept router advertisements (0=off, 1=on, 2=on+forwarding). Default value: &quot;2&quot;</p>
<dt><code>dhcp</code><i> int </i></p>
<dd>Use stateless DHCPv6 (0=off, 1=on)</p>
<dt><code>request_prefix</code><i> int </i></p>
<dd>Request a prefix through DHCPv6 Prefix Delegation (0=off, 1=on). Default value: &quot;0&quot;</p>
<dt><code>ll-attempts</code></p>
<dd>Number of attempts to wait for a link-local address. Default value: &quot;60&quot;</p>
<dt><code>ll-interval</code></p>
<dd>Link-local address polling interval in seconds. Default value: &quot;0.1&quot;</dl>
</dl>
<h3>The loopback Method</h3>
<p>This method may be used to define the IPv6 loopback interface. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt>(No options)</p>
<dd></dl>
</dl>
<h3>The static Method</h3>
<p>This method may be used to define interfaces with statically assigned IPv6 addresses. By default, stateless autoconfiguration is disabled for this interface. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>address</code><i> address </i></p>
<dd>Address (colon delimited/netmask) <code>required</code></p>
<dt><code>netmask</code><i> mask </i></p>
<dd>Netmask (number of bits, eg 64) <code>deprecated</code></p>
<dt><code>metric</code><i> metric </i></p>
<dd>Routing metric for default gateway (integer)</p>
<dt><code>gateway</code><i> address </i></p>
<dd>Default gateway (colon delimited)</p>
<dt><code>media</code><i> type </i></p>
<dd>Medium type, driver dependent</p>
<dt><code>hwaddress</code><i> address </i></p>
<dd>Hardware address or &quot;random&quot;</p>
<dt><code>mtu</code><i> size </i></p>
<dd>MTU size</p>
<dt><code>accept_ra</code><i> int </i></p>
<dd>Accept router advertisements (0=off, 1=on, 2=on+forwarding)</p>
<dt><code>autoconf</code><i> int </i></p>
<dd>Perform stateless autoconfiguration (0=off, 1=on). Default value: &quot;0&quot;</p>
<dt><code>privext</code><i> int </i></p>
<dd>Privacy extensions (RFC3041) (0=off, 1=assign, 2=prefer)</p>
<dt><code>scope</code></p>
<dd>Address validity scope. Possible values: global, site, link, host</p>
<dt><code>preferred-lifetime</code><i> int</i></p>
<dd>Time that address remains preferred</p>
<dt><code>dad-attempts</code></p>
<dd>Number of attempts to settle DAD (0 to disable DAD). Default value: &quot;60&quot;</p>
<dt><code>dad-interval</code></p>
<dd>DAD state polling interval in seconds. Default value: &quot;0.1&quot;</dl>
</dl>
<h3>The manual Method</h3>
<p>This method may be used to define interfaces for which no configuration is done by default. Such interfaces can be configured manually by means of <code>up</code> and <code>down</code> commands or /etc/network/if-*.d scripts. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>hwaddress</code><i> address </i></p>
<dd>Hardware address or &quot;random&quot;</p>
<dt><code>mtu</code><i> size </i></p>
<dd>MTU size</dl>
</dl>
<h3>The dhcp Method</h3>
<p>This method may be used to obtain network interface configuration via stateful DHCPv6 with dhclient. In stateful DHCPv6, the DHCP server is responsible for assigning addresses to clients. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>hwaddress</code><i> address </i></p>
<dd>Hardware address or &quot;random&quot;</p>
<dt><code>accept_ra</code><i> int </i></p>
<dd>Accept router advertisements (0=off, 1=on, 2=on+forwarding). Default value: &quot;1&quot;</p>
<dt><code>autoconf</code><i> int </i></p>
<dd>Perform stateless autoconfiguration (0=off, 1=on)</p>
<dt><code>request_prefix</code><i> int </i></p>
<dd>Request a prefix through DHCPv6 Prefix Delegation (0=off, 1=on). Default value: &quot;0&quot;</p>
<dt><code>ll-attempts</code></p>
<dd>Number of attempts to wait for a link-local address. Default value: &quot;60&quot;</p>
<dt><code>ll-interval</code></p>
<dd>Link-local address polling interval in seconds. Default value: &quot;0.1&quot;</dl>
</dl>
<h3>The v4tunnel Method</h3>
<p>This method may be used to setup an IPv6-over-IPv4 tunnel. It requires the <code>ip</code> command from the <code>iproute</code> package. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>address</code><i> address </i></p>
<dd>Address (colon delimited/netmask) <code>required</code></p>
<dt><code>netmask</code><i> mask </i></p>
<dd>Netmask (number of bits, eg 64) <code>deprecated</code></p>
<dt><code>endpoint</code><i> address </i></p>
<dd>Address of other tunnel endpoint (IPv4 dotted quad) <code>required</code></p>
<dt><code>local</code><i> address </i></p>
<dd>Address of the local endpoint (IPv4 dotted quad)</p>
<dt><code>metric</code><i> metric </i></p>
<dd>Routing metric for default gateway (integer)</p>
<dt><code>gateway</code><i> address </i></p>
<dd>Default gateway (colon delimited)</p>
<dt><code>ttl</code><i> time </i></p>
<dd>TTL setting</p>
<dt><code>mtu</code><i> size </i></p>
<dd>MTU size</p>
<dt><code>preferred-lifetime</code><i> int</i></p>
<dd>Time that address remains preferred</dl>
</dl>
<h3>The 6to4 Method</h3>
<p>This method may be used to setup an 6to4 tunnel. It requires the <code>ip</code> command from the <code>iproute</code> package. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>local</code><i> address </i></p>
<dd>Address of the local endpoint (IPv4 dotted quad) <code>required</code></p>
<dt><code>metric</code><i> metric </i></p>
<dd>Routing metric for default gateway (integer)</p>
<dt><code>ttl</code><i> time </i></p>
<dd>TTL setting</p>
<dt><code>mtu</code><i> size </i></p>
<dd>MTU size</p>
<dt><code>preferred-lifetime</code><i> int</i></p>
<dd>Time that address remains preferred</dl>
</dl>
<h2>Can Address Family</h2>
<p>This section documents the methods available in the can address family.</p>
<h3>The static Method</h3>
<p>This method may be used to setup an Controller Area Network (CAN) interface. It requires the the <code>ip</code> command from the <code>iproute</code> package. </p>
<p> <code>Options</code></p>
<dl>
<dd>
<dl>
<dt><code>bitrate</code><i> bitrate<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></i></p>
<dd>bitrate (1..1000000) <code>required</code></p>
<dt><code>samplepoint</code><i> samplepoint</i></p>
<dd>sample point (0.000..0.999)</p>
<dt><code>loopback</code><i> loopback<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></i></p>
<dd>loop back CAN Messages (on|off)</p>
<dt><code>listenonly</code><i> listenonly</i></p>
<dd>listen only mode (on|off)</p>
<dt><code>triple</code><i> triple<tt>&nbsp;<wbr>&nbsp;</tt></i></p>
<dd>activate triple sampling (on|off)</p>
<dt><code>oneshot</code><i> oneshot<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></i></p>
<dd>one shot mode (on|off)</p>
<dt><code>berr</code><i> berr<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></i></p>
<dd>activate berr reporting (on|off)
</dl>
</dl>
<h2>Known Bugs/Limitations</h2>
<p>The <code>ifup</code> and <code>ifdown</code> programs work with so-called &quot;physical&quot; interface names. These names are assigned to hardware by the kernel. Unfortunately it can happen that the kernel assigns different physical interface names to the same hardware at different times; for example, what was called &quot;eth0&quot; last time you booted is now called &quot;eth1&quot; and vice versa. This creates a problem if you want to configure the interfaces appropriately. A way to deal with this problem is to use mapping scripts that choose logical interface names according to the properties of the interface hardware. See the <code>get-mac-address.sh</code> script in the examples directory for an example of such a mapping script. See also Debian bug #101728.</p>
<h2>Author</h2>
<p>The ifupdown suite was written by Anthony Towns &lt;aj [at] azure.humbug.org.au&gt;. This manpage was contributed by Joey Hess &lt;joey [at] kitenet.net&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ifup/">ifup</a></code>(8), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-run-parts/">run-parts</a></code>(8), <code><a href="/docs/linux/man/8-resolvconf/">resolvconf</a></code>(8). For advice on configuring this package read the <code>Network Configuration</code> chapter of the <i>Debian Reference</i> manual, available at <i><a rel="nofollow" href="http://www.debian.org/doc/manuals/debian-reference/ch05.en.html">http://www.debian.org/doc/manuals/debian-reference/ch05.en.html</a></i> or in the <code>debian-reference-en</code> package. Examples of how to set up interfaces can be found in <code>/usr/share/doc/ifupdown/examples/network-interfaces.gz</code>. </p>
