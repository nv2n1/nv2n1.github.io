---
title: "firewalld(1)"
name: "firewalld"
section: "1"
letter: "f"
url: "/docs/linux/man/1-firewalld/"
description: "firewalld – Dynamic Firewall Manager"
---

<h2 class="name">NAME</h2>
<p> firewalld &#8211; Dynamic Firewall Manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>firewalld </code><code>[OPTIONS&#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<dd>firewalld provides a dynamically managed firewall with support for network/firewall zones to define the trust level of network connections or interfaces. It has support for IPv4, IPv6 firewall settings and for ethernet bridges and has a separation of runtime and permanent configuration options. It also supports an interface for services or applications to add firewall rules directly.</p>
<h2>OPTIONS</h2>
<p> These are the command line options of firewalld: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints a short help text and exists.</dl>
<p> <code>&#8211;debug</code>[=<i>level</i>]</p>
<dl>
<dt>
<dd> Set the debug level for firewalld to <i>level</i>. The range of the debug level is 1 (lowest level) to 10 (highest level). The debug output will be written to the firewalld log file <i>/var/log/firewalld</i>.</dl>
<p> <code>&#8211;debug-gc</code></p>
<dl>
<dt>
<dd> Print garbage collector leak information. The collector runs every 10 seconds and if there are leaks, it prints information about the leaks.</dl>
<p> <code>&#8211;nofork</code></p>
<dl>
<dt>
<dd> Turn off daemon forking. Force firewalld to run as a foreground process instead of as a daemon in the background.</dl>
<p> <code>&#8211;nopid</code></p>
<dl>
<dt>
<dd> Disable writing pid file. By default the program will write a pid file. If the program is invoked with this option it will not check for an existing server process.</dl>
<h2>CONCEPTS</h2>
<p> firewalld has a D-Bus interface for firewall configuration of services and applications. It also has a command line client for the user. Services or applications already using D-Bus can request changes to the firewall with the D-Bus interface directly. For more information on the firewalld D-Bus interface, please have a look at <code><a href="/docs/linux/man/5-firewalld-dbus/">firewalld.dbus</a></code>(5). </p>
<p> firewalld provides support for zones, predefined services and ICMP types and has a separation of runtime and permanent configuration options. Permanent configuration is loaded from XML files in <i>/usr/lib/firewalld</i> or <i>/etc/firewalld</i> (see the section called &#8220;DIRECTORIES&#8221;). </p>
<p> If NetworkManager is not in use and firewalld gets started after the network is already up, the connections and manually created interfaces are not bound to the zone specified in the ifcfg file. The interfaces will automatically be handled by the default zone. firewalld will also not get notified about network device renames. All this also applies to interfaces that are not controlled by NetworkManager if <i>NM_CONTROLLED=no</i> is set. </p>
<p> You can add these interfaces to a zone with <code>firewall-cmd [&#8211;permanent] &#8211;zone=</code><i>zone</i><code> &#8211;add-interface=</code><i>interface</i>. If there is a /etc/sysconfig/network-scripts/ifcfg-<i>interface</i> file, firewalld tries to change the ZONE=<i>zone</i> setting in this file. </p>
<p> If firewalld gets reloaded, it will restore the interface bindings that were in place before reloading to keep interface bindings stable in the case of NetworkManager uncontrolled interfaces. This mechanism is not possible in the case of a firewalld service restart. </p>
<p> It is essential to keep the ZONE= setting in the ifcfg file consistent to the binding in firewalld in the case of NetworkManager uncontrolled interfaces.</p>
<h3>Zones</h3>
<p> A network or firewall zone defines the trust level of the interface used for a connection. There are several pre-defined zones provided by firewalld. Zone configuration options and generic information about zones are described in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5)</p>
<h3>Services</h3>
<p> A service can be a list of local ports, protocols and destinations and additionally also a list of firewall helper modules automatically loaded if a service is enabled. Service configuration options and generic information about services are described in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). The use of predefined services makes it easier for the user to enable and disable access to a service.</p>
<h3>ICMP types</h3>
<p> The Internet Control Message Protocol (ICMP) is used to exchange information and also error messages in the Internet Protocol (IP). ICMP types can be used in firewalld to limit the exchange of these messages. For more information, please have a look at <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<h3>Runtime configuration</h3>
<p> Runtime configuration is the actual active configuration and is not permanent. After reload/restart of the service or a system reboot, runtime settings will be gone if they haven&#8217;t been also in permanent configuration.</p>
<h3>Permanent configuration</h3>
<p> The permanent configuration is stored in config files and will be loaded and become new runtime configuration with every machine boot or service reload/restart.</p>
<h3>Direct interface</h3>
<p> The direct interface is mainly used by services or applications to add specific firewall rules. It requires basic knowledge of <a href="/docs/linux/man/6-ip/">ip</a>(6)tables concepts (tables, chains, commands, parameters, targets).</p>
<h2>DIRECTORIES</h2>
<p> firewalld supports two configuration directories:</p>
<h3>Default/Fallback configuration in <i>/usr/lib/firewalld</i></h3>
<p> This directory contains the default and fallback configuration provided by firewalld for icmptypes, services and zones. The files provided with the firewalld package should not get changed and the changes are gone with an update of the firewalld package. Additional <code>icmptypes</code>, <code>services</code> and <code>zones</code> can be provided with packages or by creating files.</p>
<h3>System configuration settings in <i>/etc/firewalld</i></h3>
<p> The system or user configuration stored here is either created by the system administrator or by customization with the configuration interface of firewalld or by hand. The files will overload the default configuration files. </p>
<p> To manually change settings of pre-defined icmptypes, zones or services, copy the file from the default configuration directory to the corresponding directory in the system configuration directory and change it accordingly. </p>
<p> For more information on icmptypes, please have a look at the <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5) man page, for services at <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5) and for zones at <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<h2>SIGNALS</h2>
<p> Currently only SIGHUP is supported.</p>
<h3>SIGHUP</h3>
<p> Reloads the complete firewall configuration. You can also use <code>firewall-cmd &#8211;reload</code>. All runtime configuration settings will be restored. Permanent configuration will change according to options defined in the configuration files.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-firewall-applet/">firewall-applet</a></code>(1), <code><a href="/docs/linux/man/1-firewalld/">firewalld</a></code>(1), <code><a href="/docs/linux/man/1-firewall-cmd/">firewall-cmd</a></code>(1), <code><a href="/docs/linux/man/1-firewall-config/">firewall-config</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-conf/">firewalld.conf</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-dbus/">firewalld.dbus</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5), <code><a href="/docs/linux/man/1-firewall-offline-cmd/">firewall-offline-cmd</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zones/">firewalld.zones</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5)</p>
<h2>NOTES</h2>
<p> firewalld home page:</p>
<dl>
<dt>
<dd> m[blue]<code><a rel="nofollow" href="http://www.firewalld.org">http://www.firewalld.org</a></code>m[]</dl>
<p> More documentation with examples:</p>
<dl>
<dt>
<dd> m[blue]<code><a rel="nofollow" href="http://fedoraproject.org/wiki/FirewallD">http://fedoraproject.org/wiki/FirewallD</a></code>m[]</dl>
<h2>AUTHORS</h2>
<p> <code>Thomas Woerner</code> &lt;twoerner [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<p> <code>Jiri Popelka</code> &lt;jpopelka [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<h2>Index</h2>
<dt><a href="#lbAP">SIGNALS</a></p>
<dd>
<dt><a href="#lbAR">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAS">NOTES</a></p>
<dd>
<dt><a href="#lbAT">AUTHORS</a></p>
<dd></dl>
