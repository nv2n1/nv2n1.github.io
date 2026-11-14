---
title: "fcoemon(8)"
name: "fcoemon"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fcoemon/"
description: "fcoemon – Open-FCoE service daemon"
---

<p>fcoemon &#8211; Open-FCoE service daemon</p>
<h2>Synopsis</h2>
<p><code>fcoemon</code> [-f|&#8211;foreground] [-l|&#8211;legacy] [-d|&#8211;debug] [-s|&#8211;syslog] </p>
<p> <code>fcoemon</code> -h|&#8211;help </p>
<p> <code>fcoemon</code> -v|&#8211;version</p>
<h2>Description</h2>
<p>The <code>fcoemon</code> daemon is the core component of the <i>Open-FCoE</i> management service. </p>
<p> The primary function of <code>fcoemon</code> is to control FCoE instances. <code>fcoemon</code> will create, destroy, reset, enable and disable FCoE instances based on system configuration, administrative commands, and runtime events. </p>
<p> On startup, <code>fcoemon</code> will create FCoE instances defined by the configuration files (see <i>FILES</i> section below). Since FCoE typically relies on the Data Center Bridging (DCB) capabilities of an Ethernet interface, <code>fcoemon</code> establishes a connection with the LLDP daemon <code>lldpad</code> to query the status of the DCB features on relevant Ethernet interfaces and receive DCB configuration change events. </p>
<p> During runtime, <code>fcoemon</code> will monitor network and <code>lldpad</code> events for the relevant Ethernet interfaces and perform appropriate actions (create, destroy, enable, disable) on the FCoE instances. <code>fcoemon</code> also provides a client interface via which the <code>fcoeadm</code> utility is able to issue commands. </p>
<p> Installation of the <i>fcoe-utils</i> package will set up an <i>fcoe</i> service which will control the execution of the <code>fcoemon</code> daemon.</p>
<h2>Options</h2>
<p><code>-f</code>, <code>&#8211;foreground</code></p>
<dl>
<dd>Run <code>fcoemon</code> in the foreground.</dl>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dd>Enable debugging messages.</dl>
<p> <code>-l</code>, <code>&#8211;legacy</code></p>
<dl>
<dd>Force fcoemon to use the legacy /sys/module/libfcoe/parameters/ interface. The default is to use the newer /sys/bus/fcoe/ interfaces if they are available.</dl>
<p> <code>-s</code>, <code>&#8211;syslog</code></p>
<dl>
<dd>Use syslogd for logging. The default behavior is to log to stdout and stderr.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Show help message with basic usage instructions</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dd>Show the version of the <code>fcoemon</code> command.</dl>
<h2>Terminology</h2>
<p><i>DCB</i></p>
<dl>
<dd>Data Center Bridging A set of Ethernet enhancement standards developed by the IEEE 802.1 Working Group.</dl>
<p> &nbsp;<wbr></p>
<dl>
<dd>See <a rel="nofollow" href="http://www.ieee802.org/1/pages/dcbridges.html">http://www.ieee802.org/1/pages/dcbridges.html</a> for more information.</dl>
<p> <i>DCBX</i></p>
<dl>
<dd>DCB Capabilities Exchange Protocol, implemented by the DCB module of <code>lldpad</code>. DCBX exchanges DCB capabilities and configuration with a link partner as a series of values transferred using the Link Layer Discovery Protocol (LLDP).</dl>
<p> <i>PFC</i></p>
<dl>
<dd>Priority-based Flow Control, a <i>DCB</i> feature.</dl>
<p> <i>App:FCoE</i></p>
<dl>
<dd>The FCoE instance of application specific parameters in DCBX.</dl>
<h2>Criteria Used For Controlling The Fcoe Instance</h2>
<p><code>fcoemon</code> uses two information sources for determining when to create an FCoE instance: the state of the network interface, which may be a VLAN interface, and, if required for the FCoE instance, the state of the DCB configuration on the physical Ethernet interface. </p>
<p> First of all, the network interface must be &quot;up&quot; for the FCoE instance to be created. Secondly, if the FCoE configuration indicates that DCB is required, then the following criteria must be satisfied before the FCoE interface is created: </p>
<dl>
<dd>&bull; DCB is enabled on the Ethernet interface.</dl>
<dl>
<dd>&bull; The PFC DCB feature is enabled and operational.</dl>
<dl>
<dd>&bull; The App:FCoE DCB feature is enabled and operational.</dl>
<dl>
<dd>&bull; The priority indicated by the App:FCoE feature is also enabled for PFC.</dl>
<p> Once the FCoE instance is created by <code>fcoemon</code>, it will only be destroyed under the following conditions: </p>
<dl>
<dd>&bull; The driver for the Ethernet interface is unloaded.</dl>
<dl>
<dd>&bull; A user administratively destroys the FCoE instance using <code>fcoeadm</code>.</dl>
<dl>
<dd>&bull; The <code>fcoemon</code> daemon is terminated.</dl>
<p> If DCB is required for the FCoE instance, and the DCB settings change after the interface is created, the following criteria are used to disable the FCoE instance: </p>
<dl>
<dd>&bull; DCB is disabled on the Ethernet interface.</dl>
<dl>
<dd>&bull; The App:FCoE DCB feature is not enabled.</dl>
<dl>
<dd>&bull; The App:FCoE and PFC features are operational AND the priority indicated by App:FCoE is not enabled for PFC.</dl>
<p> Otherwise, the FCoE instance will always remain enabled.</p>
<h2>Configuration</h2>
<p>Once the <i>fcoe-utils</i> and <code>lldpad</code> packages have been installed and the corresponding services are running, there are a few simple configuration steps required to get an FCoE instance up and running. The following assumes that DCB will be required for the interface. </p>
<dl>
<dd>&bull; Ensure that the configuration on the peer device (e.g. FCoE capable switch) has the necessary configurations (VLANs, DCB, DCBX).</dl>
<dl>
<dd>&bull; Configure any needed VLAN interfaces on the local system.</dl>
<dl>
<dd>&bull; Create and configure <i>/etc/fcoe/cfg-&lt;ifname&gt;</i> files for the network interfaces over which FCoE instances need to be created. See the <i>FILES</i> sections for details. Note that <i>ifname</i> may be for a VLAN interface.</dl>
<dl>
<dd>&bull; Restart the <code>fcoe</code> service (i.e. <code>fcoemon</code>).</dl>
<dl>
<dd>&bull; The default DCB configuration of an Ethernet interface managed by <code>lldpad</code> requires the following configuration using <code>dcbtool</code>. </p>
<dl>
<dd>
<pre>dcbtool sc ethX dcb on &lt;-- enable DCB on the interface
dcbtool sc ethX app:fcoe e:1 &lt;-- enable App:FCoE on the interface</pre>
</dl>
</dl>
<p> These steps only need to be done one time. Note that if other DCB configuration changes have been made with <code>dcbtool</code>, then additional changes may need to be made in order to satisfy the DCB criteria for creating an FCoE instance. Consult <code>dcbtool</code> for details. </p>
<p> Once these configuration steps have been performed, use <code>fcoeadm</code> to query the status of the FCoE instances.</p>
<h2>Files</h2>
<h3>/etc/fcoe/config</h3>
<p>This is the primary configuration file for the <code>fcoe</code> system service. The default options in this file are: <code>DEBUG=&quot;no&quot;</code> and <code>USE_SYSLOG=&quot;yes&quot;</code>. The former is used to enable debugging messages from the fcoe service script and <code>fcoemon</code> (via the <code>&#8211;debug</code> option). The latter is to indicate if the log messages are to be output to the system log (via the <code>&#8211;syslog</code> option). <code>SUPPORTED_DRIVERS</code> is the list of drivers to automatically load during fcoe service start. Any changes to this file will require a restart of the <code>fcoe</code> service.</p>
<h3>/etc/sysconfig/fcoe</h3>
<p>On systemd-enabled systems, this is the primary configuration file used for the <code>fcoe</code> system service. Add <code>&#8211;debug</code> to <code>FCOEMON_OPTS</code> to enable debug log messages. Any changes to this file will require a restart of the <code>fcoe</code> service.</p>
<h3>/etc/fcoe/cfg-&lt;ifname&gt;</h3>
<p>These files are read by <code>fcoemon</code> on initialization. They are used to indicate which Ethernet or VLAN interfaces should have FCoE instances created. The option values in this file normally are: <code>FCOE_ENABLE=&quot;yes&quot;</code>, <code>DCB_REQUIRED=&quot;yes&quot;</code>, and <code>AUTO_VLAN=&quot;yes&quot;</code>, though if the variable values are omitted, they default to &quot;no&quot;. </p>
<p> <i>FCOE_ENABLE</i></p>
<dl>
<dd>is used to enable/disable creation of the FCoE instance. If FCoE_ENABLE is set to &quot;no&quot;, then the other configuration values have no effect.</dl>
<p> <i>DCB_REQUIRED</i></p>
<dl>
<dd>indicates if the DCB service is required on the Ethernet interface.</dl>
<p> <i>AUTO_VLAN</i></p>
<dl>
<dd>indicates if VLAN discovery should be performed. If AUTO_VLAN is set to &quot;yes&quot;, then once the link configuration has been validated, <code>fcoemon</code> will run run the FIP VLAN discovery protocol on the Ethernet interface. Network interfaces for any discovered FCoE VLANs will be automatically created, if they are not already configured, and FCoE instances will be created on the VLAN interfaces. If the network interface specified by the filename is already a VLAN interface, the AUTO_VLAN setting is ignored.</dl>
<p> <i>MODE</i></p>
<dl>
<dd>indicates whether operation will be in fabric or vn2vn mode. The default is fabric.</dl>
<p> <i>FIP_RESP</i></p>
<dl>
<dd>indicates whether a FIP responder should be activated on this device to support VLAN discovery in a vn2vn environment. The default is &quot;no&quot;. Often this will be used on a vn2vn node also serving as a target. When using this option, the AUTO_VLAN should not be set and the supported VLANs should have configuration files supplied, constituting a static VLAN configuration that provides the information for the FIP responder to return. This should be set on a base device, which should probably have FCOE_ENABLE set to &quot;no&quot; since presumably FCoE operation will be on the configured VLANs.</dl>
<p> Note that the attached Ethernet peer device (e.g. FCoE capable switch port) must have compatible settings For DCB and FCoE to function properly.</p>
<h3>/etc/init.d/fcoe</h3>
<p>This is the <code>fcoe</code> system service script. This script is invoked by the init process or by the service command to start and stop the <code>fcoemon</code>. On systemd-enabled systems, <code>fcoemon</code> is controlled via the <code>fcoe.service</code> unit.</p>
<h2>Vlan Naming Conventions</h2>
<p>If a new VLAN device is created (see the description of the <i>AUTO_VLAN</i> setting above), it will have the name <i>dev</i>.<i>vlan</i>-fcoe; where <i>dev</i> is the name of the Ethernet parent device and <i>vlan</i> is the discovered VLAN ID number.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fcoeadm/">fcoeadm</a></code>(8) <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8) <code><a href="/docs/linux/man/8-dcbtool/">dcbtool</a></code>(8)</p>
<h2>Support</h2>
<p><code>fcoemon</code> is part of the <i>fcoe-utils</i> package, maintained through the <i>Open-FCoE</i> project. Resources for both developers and users can be found at the <i>Open-FCoE</i> website <a rel="nofollow" href="http://open-fcoe.org/">http://open-fcoe.org/</a></p>
