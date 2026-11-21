---
title: "python-networkmanager(1)"
name: "python-networkmanager"
section: "1"
letter: "p"
url: "/docs/linux/man/1-python-networkmanager/"
description: "python-networkmanager – python-networkmanager Documentation"
---

<h2>NAME</h2>
<p> python-networkmanager &#8211; python-networkmanager Documentation </p>
<p> NetworkManager provides a detailed and capable D-Bus interface on the system bus. You can use this interface to query NetworkManager about the overall state of the network and details of network devices like current IP addresses or DHCP options, and to activate and deactivate network connections. </p>
<p> python-networkmanager takes this D-Bus interface and wraps D-Bus interfaces in classes and D-Bus properties in python properties. It also provides a command-line utility to inspect the configuration and (de-)activate connections.</p>
<h2>THE NETWORKMANAGER MODULE</h2>
<p> All the code is contained in one module: <i>NetworkManager</i>. Using it is as simple as you think it is: </p>
<pre>
&gt;&gt;&gt; import NetworkManager
&gt;&gt;&gt; NetworkManager.NetworkManager.Version
'1.2.0'
</pre>
<p> NetworkManager exposes a lot of information via D-Bus and also allows full control of network settings. The full D-Bus API can be found on <i>NetworkManager project website</i>. All interfaces listed there have been wrapped in classes as listed below. With a few exceptions, they behave exactly like the D-Bus methods. These exceptions are for convenience and limited to this list:</p>
<dl>
<dt>&bull;</dt>
<dd> IP addresses are returned as strings of the form <code>1.2.3.4</code> instead of network byte ordered integers.</dd>
<dt>&bull;</dt>
<dd> Route metrics are returned in host byte order, so you can use them as integers.</dd>
<dt>&bull;</dt>
<dd> Mac addresses and BSSIDs are always returned as strings of the form <code>00:11:22:33:44:55</code> instead of byte sequences.</dd>
<dt>&bull;</dt>
<dd> Wireless SSID&#8217;s are returned as strings instead of byte sequences. They will be decoded as UTF-8 data, so using any other encoding for your SSID will result in errors.</dd>
<dt><code>class NetworkManager.NMDbusInterface</code></dt>
<dd>
<p> This is the base class for all interface wrappers. It adds a few useful features to standard D-Bus interfaces:</p>
</dd><dt>&bull;</dt>
<dd> All D-Bus properties are exposed as python properties</dd>
<dt>&bull;</dt>
<dd> Return values are automatically converted to python basic types (so no more <code>dbus.String</code>, but simple <code>str</code> (python 3) or <code>unicode</code> (python 2))</dd>
<dt>&bull;</dt>
<dd> Object paths in return values are automatically replaced with proxy objects, so you don&#8217;t need to do that manually</dd>
<dt>&bull;</dt>
<dd> &#8230;and vice versa when sending</dd>
<dt>&bull;</dt>
<dd> And also when receiving signals</dd>
<dt><code>NetworkManager.const(prefix, value)</code></dt>
<dd>
<p> Many of NetworkManagers D-Bus methods expect or return numeric constants, for which there are enums in the C source code. These constants, such as <code>NM_STATE_CONNECTED_GLOBAL</code>, can all be found in the <i>NetworkManager</i> module as well. The <i>const()</i> function can help you translate them to text. For example: </p>
<pre>
&gt;&gt;&gt; NetworkManager.const('state', 40)
'connecting'
&gt;&gt;&gt; NetworkManager.const('device_type', 2)
'wifi'
</pre>
</dd></dl>
<h2>LIST OF CLASSES</h2>
<dl>
<dt><code>class NetworkManager.NetworkManager</code></dt>
<dd>
<p> This class represents the <code>org.freedesktop.NetworkManager</code> interface. Note that <i>NetworkManager.NetworkManager</i> actually is the singleton instance of this class.</p>
</dd><dt><code>NetworkManager.auto_reconnect()</code></dt>
<dd>
<p> Call this method to automatically update D-Bus paths and reconnect signals when NetworkManager restarts.</p>
</dd><dt><code>class NetworkManager.Settings</code></dt>
<dd>
<p> This class represents the <code>org.freedesktop.NetworkManager.Settings</code> interface. Note that <i>NetworkManager.Settings</i> actually is the singleton instance of this class.</p>
</dd><dt><code>class NetworkManager.Connection</code></dt>
<dd>
<p> This class represents the <code>org.freedesktop.NetworkManager.Settings.Connection</code> interface.</p>
</dd><dt><code>class NetworkManager.ActiveConnection</code></dt>
<dd>
<p> This class represents the <code>org.freedesktop.NetworkManager.Connection.Active</code> interface.</p>
</dd><dt><code>class NetworkManager.AccessPoint</code></dt>
<dd>
<p> This class represents the <code>org.freedesktop.NetworkManager.AccessPoint</code> interface.</p>
</dd><dt><code>class NetworkManager.Device</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Adsl</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Bluetooth</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Bond</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Bridge</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Generic</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Infiniband</code></dt>
<dd>
</dd><dt><code>class NetworkManager.IPTunnel</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Macvlan</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Modem</code></dt>
<dd>
</dd><dt><code>class NetworkManager.OlpcMesh</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Team</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Tun</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Veth</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Vlan</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Vxlan</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Wimax</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Wired</code></dt>
<dd>
</dd><dt><code>class NetworkManager.Wireless</code></dt>
<dd>
<p> These classes represent D-Bus interfaces for various types of hardware. Note that methods such as <code>NetworkManager.GetDevices()</code> will only return <i>Device</i> instances. To get the hardware-specific class, you can call the <code>Device.SpecificDevice()</code> method. </p>
<pre><code>
&gt;&gt;&gt; [(dev.Interface, dev.SpecificDevice().__class__.__name__)
...  for dev in NetworkManager.NetworkManager.GetDevices()]
[('eth0', 'Wired'), ('wlan0', 'Wireless'), ('wwan0', 'Modem')]
</code></pre>
</dd><dt><code>class NetworkManager.IP4Config</code></dt>
<dd>
</dd><dt><code>class NetworkManager.IP6Config</code></dt>
<dd>
</dd><dt><code>class NetworkManager.DHCP4Config</code></dt>
<dd>
</dd><dt><code>class NetworkManager.DHCP6Config</code></dt>
<dd>
<p> These classes represent the various IP configuration interfaces.</p>
</dd><dt><code>class NetworkManager.AgentManager</code></dt>
<dd>
</dd><dt><code>class NetworkManager.SecretAgent</code></dt>
<dd>
<p> Classes that can be used to handle and store secrets. Note that these are not for querying NetworkManager&#8217;s exisiting secret stores. For that the <code>GetSecrets()</code> method of the <i>Connection</i> class can be used.</p>
</dd><dt><code>class NetworkManager.VPNConnection</code></dt>
<dd>
<p> This class represents the <code>org.freedesktop.NetworkManager.VPN.Connection</code> interface.</p>
</dd><dt><code>class NetworkManager.VPNPlugin</code></dt>
<dd>
<p> A class that can be used to query VPN plugins.</dd></dl>
<h2>AUTHOR</h2>
<p> Dennis Kaarsemaker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2016, Dennis Kaarsemaker </p>
