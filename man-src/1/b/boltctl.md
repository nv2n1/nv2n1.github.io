---
title: "boltctl(1)"
name: "boltctl"
section: "1"
letter: "b"
url: "/docs/linux/man/1-boltctl/"
description: "boltctl – control the thunderbolt device manager"
---

<h2 class="name">NAME</h2>
<p> boltctl &#8211; control the thunderbolt device manager </p>
<h2>SYNOPSIS</h2>
<pre>
<code>boltctl</code> <i>authorize</i> <i>DEVICE</i>
<code>boltctl</code> <i>config</i>
<code>boltctl</code> <i>domains</i>
<code>boltctl</code> <i>enroll</i> <i>DEVICE</i>
<code>boltctl</code> <i>forget</i> <i>DEVICE</i>
<code>boltctl</code> <i>info</i> <i>DEVICE</i>
<code>boltctl</code> <i>list</i>
<code>boltctl</code> <i>monitor</i>
<code>boltctl</code> <i>power</i>
</pre>
<h2>DESCRIPTION</h2>
<p> <i>boltctl</i> is the command line interface to interact with <i>boltd</i>, the system daemon that manages Thunderbolt 3(TM) devices. It can be used to query the state of devices as well as manage them. </p>
<p> Devices can be globally identified via their unique identifier (uuid). All commands that take a <i>DEVICE</i> identifier expect this unique id. </p>
<p> If no command is given, it is equivalent to <i>boltctl list</i>.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version information and exit.</dl>
<p> <code>-U | &#8211;uuid {</code><i>full</i><code> | </code><i>short</i><code> | </code><i>alias</i><code> | N}</code></p>
<dl>
<dt>
<dd> Control how UUIDs are printed. Since they are somewhat sensitive data it is not advisable to share them publicly in full length. Instead <i>short</i> or <i>alias</i> can and should be used when sharing the output of <i>boltctl</i>. </p>
<p> <i>full</i></p>
<dl>
<dt>
<dd> Print all UUIDs in full length.</dl>
<p> <i>short</i></p>
<dl>
<dt>
<dd> Truncate all UUIDs so only the first 13 characters are printed.</dl>
<p> <i>alias</i></p>
<dl>
<dt>
<dd> All UUIDs are replaced by a random string that is derived from the UUID, therefore the devices can be uniquely identified without revealing the original UUID.</dl>
<p> N</p>
<dl>
<dt>
<dd> If a integer <i>N</i> is specified, all UUIDs are truncated to only show up to <i>N</i>.</dl>
</dl>
<h2>COMMANDS</h2>
<h3>authorize [-F | &#8211;first-time] <i>DEVICE</i></h3>
<p> Authorize a currently unauthorized device identified via its unique id (uuid) <i>DEVICE</i>. If a key is stored in the database it will be used, given the security level of the domain supports secure device connection. Use <i>boltctl list</i> to find out the uuid of a device. </p>
<p> <code>-F | &#8211;first-time</code></p>
<dl>
<dt>
<dd> Normally, when attempting to authorize an already authorized device <code>boltctl</code> will do nothing and return a successful status code. When using this option, the attempt will fail and result in a negative exit code if the device is already authorized.</dl>
<h3>config &#8211;describe [global|domain|device]</h3>
<p> List global, domain, or all (if nothing is specified) properties. The format is 3 columns: permission, name, description. Permission indicates if the property is only readable or can also be written.</p>
<h3>config <i>KEY</i> [<i>VALUE</i>]</h3>
<p> Get or set, if <i>VALUE</i> is specified, a global property.</p>
<h3>config <i>&lt;domain|device&gt;.KEY</i> <i>TARGET</i> [<i>VALUE</i>]</h3>
<p> Get or set, if <i>VALUE</i> is specified, a domain or device property, where <i>TARGET</i> is the unique id of the domain or the device.</p>
<h3>domains [-v | &#8211;verbose]</h3>
<p> List all currently active Thunderbolt domains. A Thunderbolt domain represents the Thunderbolt controller hardware. There will be one domain (and host device) for each Thunderbolt controller present in the system. The <i>security</i> property shows the security level of the controller. If <i>iommu</i> support is active (see the <code>boltd</code> man page) it will be indicated by a <i>+iommu</i> suffix for &quot;secure&quot; or &quot;user&quot; mode, or just plain <i>iommu</i> in case the security level is &quot;none&quot; (sl0). <i>bootacl</i> shows the used and total slots of the boot access control list (BootACL) and the content of all non-empty entries. NB: if BootACL is unsupported it will show 0 for both (0/0). The <i>online</i> property shows if the thunderbolt controller is currently powered by the firmware. <code>NB</code>: if the controller is currently offline the BootACL list will reflect what <i>boltd</i> estimates the list will look like once the controller is back online and local changes have been synchronized to the controller. This might not be accurate if the list was modified in the meantime, e.g. from a different installation or OS.</p>
<h3>enroll [&#8211;policy <i>policy</i>] <i>DEVICE</i></h3>
<p> Authorize and record the device with the unique id <i>DEVICE</i> in the database. If the domain supports secure connection a new key will be generated and stored in the database alongside the device name and vendor name. The key, if created, will be used in the future to securely authorize the device. </p>
<p> <code>&#8211;policy {</code><i>default</i><code> | </code><i>auto</i><code> | </code><i>manual</i><code>}</code></p>
<dl>
<dt>
<dd> Specify the policy to be used for the newly enrolled device. </p>
<p> <i>default</i></p>
<dl>
<dt>
<dd> Use the global default policy of the daemon; this can be changed, but is normally also <i>auto</i>.</dl>
<p> <i>auto</i></p>
<dl>
<dt>
<dd> Automatically authorize this device whenever it is connected.</dl>
<p> <i>manual</i></p>
<dl>
<dt>
<dd> Do <code>not</code> automatically authorize the device; instead require manual authorization via <code>boltctl authorize</code>.</dl>
</dl>
<h3>forget <i>DEVICE</i></h3>
<p> Remove the information about the device with the unique id <i>DEVICE</i> from the database. This includes the key, if one was previously generated. If you pass <i>&#8211;all</i> instead of the <i>DEVICE</i> all devices are removed instead of just one.</p>
<h3>info <i>DEVICE</i></h3>
<p> Display information about the device with the unique id <i>DEVICE</i>.</p>
<h3>list [-a | &#8211;all]</h3>
<p> List and print information about all connected and stored devices. </p>
<p> <code>-a | &#8211;all</code></p>
<dl>
<dt>
<dd> Normally, the only the device type that will be shown is peripherals. Therefore the device that represents the host itself will be omitted. Using this option will instead include all device types in the list.</dl>
<h3>monitor</h3>
<p> Listen for and show changes in connected devices.</p>
<h3>power [-t | &#8211;timeout <i>seconds</i>] [-q | &#8211;query]</h3>
<p> Power up the Thunderbolt controller. If the Thunderbolt controller is not in &quot;native enumeration mode&quot; it can be completely powered down by the host firmware/BIOS. On supported systems there is an interface to &quot;force&quot; power the thunderbolt controller. If supported this command will request the daemon to do so. The daemon will keep track of all client requests and will release the force power override when the last request is released. </p>
<p> <code>-t | &#8211;timeout </code><i>seconds</i></p>
<dl>
<dt>
<dd> Release the force power request after the specified amount of <i>seconds</i> and exit.</dl>
<p> <code>-q | &#8211;query</code></p>
<dl>
<dt>
<dd> Query the current force power status of the daemon.</dl>
<h2>AUTHOR</h2>
<p> Written by Christian Kellner &lt;ckellner [at] redhat.com&gt;. </p>
<h2>Index</h2>
<dt><a href="#lbAR">AUTHOR</a></p>
<dd></dl>
