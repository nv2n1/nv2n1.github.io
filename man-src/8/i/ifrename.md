---
title: "ifrename(8)"
name: "ifrename"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifrename/"
description: "ifrename – rename network interfaces based on various static criteria"
---

<p>ifrename &#8211; rename network interfaces based on various static criteria</p>
<h2>Synopsis</h2>
<p><code>ifrename [-c configfile] [-p] [-d] [-u] [-v] [-V] [-D]</code><br />
 <code>ifrename [-c configfile] [-i interface] [-n newname]</code></p>
<h2>Description</h2>
<p><code>Ifrename </code> is a tool allowing you to assign a consistent name to each of your network interface. </p>
<p> By default, interface names are dynamic, and each network interface is assigned the first available name (<i>eth0</i>, <i>eth1</i>&#8230;). The order network interfaces are created may vary. For built-in interfaces, the kernel boot time enumeration may vary. For removable interface, the user may plug them in any order. </p>
<p> <code>Ifrename</code> allow the user to decide what name a network interface will have. <code>Ifrename </code> can use a variety of <i>selectors</i> to specify how interface names match the network interfaces on the system, the most common selector is the interface <i>MAC address</i>. </p>
<p> <code>Ifrename</code> must be run before interfaces are brought up, which is why it&#8217;s mostly useful in various scripts (init, hotplug) but is seldom used directly by the user. By default, <code>ifrename </code> renames all present system interfaces using mappings defined in <i>/etc/iftab</i>.</p>
<h2>Parameters</h2>
<dl>
<dt><code>-c </code><i>configfile</i></p>
<dd>Set the configuration file to be used (by default <i>/etc/iftab</i>). The configuration file define the mapping between selectors and interface names, and is described in <i><a href="/docs/linux/man/5-iftab/">iftab</a></i>(5).<br />
 If <i>configfile</i> is &quot;-&quot;, the configuration is read from stdin.</p>
<dt><code>-p</code></p>
<dd>Probe (load) kernel modules before renaming interfaces. By default <code>ifrename </code> only check interfaces already loaded, and doesn&#8217;t auto-load the required kernel modules. This option enables smooth integration with system not loading modules before calling <code>ifrename</code>.</p>
<dt><code>-d</code></p>
<dd>Enable various <code>Debian</code> specific hacks. Combined with <code>-p</code>, only modules for interfaces specified in <i>/etc/network/interface</i> are loaded.</p>
<dt><code>-i </code><i>interface</i></p>
<dd>Only rename the specified <i>interface </i> as opposed to all interfaces on the system. The new interface name is printed.</p>
<dt><code>-n </code><i>newname</i></p>
<dd>When used with <i>-i</i>, specify the new name of the interface. The list of mappings from the configuration file is bypassed, the interface specified with <i>-i</i> is renamed directly to <i>newname</i>. The new name may be a wildcard containing a single &#8216;*&#8217;.<br />
 When used without <i>-i</i>, rename interfaces by using only mappings that would rename them to <i>newname</i>. The new name may not be a wildcard. This use of ifrename is discouraged, because inefficient (<i>-n</i> without <i>-i</i>). All the interfaces of the system need to be processed at each invocation, therefore in most case it is not faster than just letting ifrename renaming all of them (without both <i>-n</i> and <i>-i</i>).</p>
<dt><code>-t</code></p>
<dd>Enable name takeover support. This allow interface name swapping between two or more interfaces.<br />
 Takeover enable an interface to &#8216;steal&#8217; the name of another interface. This works only with kernel 2.6.X and if the other interface is down. Consequently, this is not compatible with Hotplug. The other interface is assigned a random name, but may be renamed later with &#8216;ifrename&#8217;.<br />
 The number of takeovers is limited to avoid circular loops, and therefore some complex multi-way name swapping situations may not be fully processed.<br />
 In any case, name swapping and the use of this feature is discouraged, and you are invited to choose unique and unambiguous names for your interfaces&#8230;</p>
<dt><code>-u</code></p>
<dd>Enable <i>udev</i> output mode. This enables proper integration of <code>ifrename</code> in the <i>udev</i> framework, <code><a href="/docs/linux/man/8-udevd/">udevd</a></code>(8) will use <code>ifrename</code> to assign interface names present in <i>/etc/iftab</i>. In this mode the output of ifrename can be parsed directly by <code><a href="/docs/linux/man/8-udevd/">udevd</a></code>(8) as an IMPORT action. This requires <i>udev</i> version 107 or later.</p>
<dt><code>-D</code></p>
<dd>Dry-run mode. Ifrename won&#8217;t change any interface, it will only print new interface name, if applicable, and return.<br />
 In dry-run mode, interface name wildcards are not resolved. New interface name is printed, even if it is the same as the old name.<br />
 Be also aware that some selectors can only be read by root, for example those based on <code>ethtool</code>), and will fail silently if run by a normal user. In other words, dry-run mode under a standard user may not give the expected result.</p>
<dt><code>-V</code></p>
<dd>Verbose mode. Ifrename will display internal results of parsing its configuration file and querying the interfaces selectors. Combined with the <i>dry-run</i> option, this is a good way to debug complex configurations or trivial problems.</dl>
<h2>Author</h2>
<p>Jean Tourrilhes &#8211; jt [at] hpl.hp.com</p>
<h2>Files</h2>
<p><i>/etc/iftab</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/5-iftab/">iftab</a></code>(5). </p>
