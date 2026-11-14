---
title: "firewall-offline-cmd(1)"
name: "firewall-offline-cmd"
section: "1"
letter: "f"
url: "/docs/linux/man/1-firewall-offline-cmd/"
description: "firewall-offline-cmd – firewalld offline command line client"
---

<h2 class="name">NAME</h2>
<p> firewall-offline-cmd &#8211; firewalld offline command line client </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>firewall-offline-cmd</code> [OPTIONS&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>firewall-offline-cmd is an offline command line client of the firewalld daemon. It should be used only if the firewalld service is not running. For example to migrate from system-config-firewall/lokkit or in the install environment to configure firewall settings with kickstart. </p>
<p> Some lokkit options can not be automatically converted for firewalld, they will result in an error or warning message. This tool tries to convert as much as possible, but there are limitations for example with custom rules, modules and masquerading. </p>
<p> Check the firewall configuration after using this tool.</p>
<h2>OPTIONS</h2>
<p> If no options are given, configuration from <code>/etc/sysconfig/system-config-firewall</code> will be migrated. </p>
<p> For sequence options, this are the options that can be specified multiple times, the exit code is 0 if there is at least one item that succeded. The <i>ALREADY_ENABLED</i> (11), <i>NOT_ENABLED</i> (12) and also <i>ZONE_ALREADY_SET</i> (16) errors are treated as succeeded. If there are issues while parsing the items, then these are treated as warnings and will not change the result as long as there is a succeeded one. Without any succeeded item, the exit code will depend on the error codes. If there is exactly one error code, then this is used. If there are more than one then <i>UNKNOWN_ERROR</i> (254) will be used. </p>
<p> The following options are supported:</p>
<h3>General Options</h3>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints a short help text and exists.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints the version string of firewalld and exits.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Do not print status messages.</dl>
<h3>Status Options</h3>
<p> <code>&#8211;enabled</code></p>
<dl>
<dt>
<dd> Enable the firewall. This option is a default option and will activate the firewall if not already enabled as long as the option <code>&#8211;disabled</code> is not given.</dl>
<p> <code>&#8211;disabled</code></p>
<dl>
<dt>
<dd> Disable the firewall by disabling the firewalld service.</dl>
<h3>Lokkit Compatibility Options</h3>
<p> These options are nearly identical to the options of <code>lokkit</code>. </p>
<p> <code>&#8211;migrate-system-config-firewall=</code><i>file</i></p>
<dl>
<dt>
<dd> Migrate system-config-firewall configuration from the given file. No further</dl>
<p> <code>&#8211;addmodule</code>=<i>module</i></p>
<dl>
<dt>
<dd> This option will result in a warning message and will be ignored. </p>
<p> Handling of netfilter helpers has been merged into services completely. Adding or removing netfilter helpers outside of services is therefore not needed anymore. For more information on handling netfilter helpers in services, please have a look at <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> <code>&#8211;removemodule</code></p>
<dl>
<dt>
<dd> This option will result in a warning message and will be ignored. </p>
<p> Handling of netfilter helpers has been merged into services completely. Adding or removing netfilter helpers outside of services is therefore not needed anymore. For more information on handling netfilter helpers in services, please have a look at <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> <code>&#8211;remove-service</code>=<i>service</i></p>
<dl>
<dt>
<dd> Remove a service from the default zone. This option can be specified multiple times. </p>
<p> The service is one of the firewalld provided services. To get a list of the supported services, use <code>firewall-cmd &#8211;get-services</code>.</dl>
<p> <code>-s</code> <i>service</i>, <code>&#8211;service</code>=<i>service</i></p>
<dl>
<dt>
<dd> Add a service to the default zone. This option can be specified multiple times. </p>
<p> The service is one of the firewalld provided services. To get a list of the supported services, use <code>firewall-cmd &#8211;get-services</code>.</dl>
<p> <code>-p</code> <i>portid</i>[-<i>portid</i>]:<i>protocol</i>, <code>&#8211;port</code>=<i>portid</i>[-<i>portid</i>]:<i>protocol</i></p>
<dl>
<dt>
<dd> Add the port to the default zone. This option can be specified multiple times. </p>
<p> The port can either be a single port number or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>.</dl>
<p> <code>-t</code> <i>interface</i>, <code>&#8211;trust</code>=<i>interface</i></p>
<dl>
<dt>
<dd> This option will result in a warning message. </p>
<p> Mark an interface as trusted. This option can be specified multiple times. The interface will be bound to the trusted zone. </p>
<p> If the interface is used in a NetworkManager managed connection or if there is an ifcfg file for this interface, the zone will be changed to the zone defined in the configuration as soon as it gets activated. To change the zone of a connection use <code>nm-connection-editor</code> and set the zone to trusted, for an ifcfg file, use an editor and add &quot;ZONE=trusted&quot;. If the zone is not defined in the ifcfg file, the firewalld default zone will be used.</dl>
<p> <code>-m</code> <i>interface</i>, <code>&#8211;masq</code>=<i>interface</i></p>
<dl>
<dt>
<dd> This option will result in a warning message. </p>
<p> Masquerading will be enabled in the default zone. The interface argument will be ignored. This is for <i>IPv4</i> only.</dl>
<p> <code>&#8211;custom-rules</code>=[<i>type</i>:][<i>table</i>:]<i>filename</i></p>
<dl>
<dt>
<dd> This option will result in a warning message and will be ignored. </p>
<p> Custom rule files are not supported by firewalld.</dl>
<p> <code>&#8211;forward-port</code>=if=<i>interface</i>:port=<i>port</i>:proto=<i>protocol</i>[:toport=<i>destination port</i>:][:toaddr=<i>destination address</i>]</p>
<dl>
<dt>
<dd> This option will result in a warning message. </p>
<p> Add the <i>IPv4</i> forward port in the default zone. This option can be specified multiple times. </p>
<p> The port can either be a single port number <i>portid</i> or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>. The destination address is an IP address.</dl>
<p> <code>&#8211;block-icmp</code>=<i>icmptype</i></p>
<dl>
<dt>
<dd> This option will result in a warning message. </p>
<p> Add an ICMP block for <i>icmptype</i> in the default zone. This option can be specified multiple times. </p>
<p> The <i>icmptype</i> is the one of the icmp types firewalld supports. To get a listing of supported icmp types: <code>firewall-cmd &#8211;get-icmptypes</code></dl>
<h3>Log Denied Options</h3>
<p> <code>&#8211;get-log-denied</code></p>
<dl>
<dt>
<dd> Print the log denied setting.</dl>
<p> <code>&#8211;set-log-denied</code>=<i>value</i></p>
<dl>
<dt>
<dd> Add logging rules right before reject and drop rules in the INPUT, FORWARD and OUTPUT chains for the default rules and also final reject and drop rules in zones for the configured link-layer packet type. The possible values are: <i>all</i>, <i>unicast</i>, <i>broadcast</i>, <i>multicast</i> and <i>off</i>. The default setting is <i>off</i>, which disables the logging. </p>
<p> This is a runtime and permanent change and will also reload the firewall to be able to add the logging rules.</dl>
<h3>Automatic Helpers Options</h3>
<p> <code>&#8211;get-automatic-helpers</code></p>
<dl>
<dt>
<dd> Print the automatic helpers setting.</dl>
<p> <code>&#8211;set-automatic-helpers</code>=<i>value</i></p>
<dl>
<dt>
<dd> For the secure use of iptables and connection tracking helpers it is recommended to turn AutomaticHelpers off. But this might have side effects on other services using the netfilter helpers as the sysctl setting in <i>/proc/sys/net/netfilter/nf_conntrack_helper</i> will be changed. With the system setting, the default value set in the kernel or with sysctl will be used. Possible values are: <i>yes</i>, <i>no</i> and <i>system</i>. The default value is <i>system</i>. </p>
<p> This is a runtime and permanent change and will also reload the firewall to be able to make the helpers usable.</dl>
<h3>Zone Options</h3>
<p> <code>&#8211;get-default-zone</code></p>
<dl>
<dt>
<dd> Print default zone for connections and interfaces.</dl>
<p> <code>&#8211;set-default-zone</code>=<i>zone</i></p>
<dl>
<dt>
<dd> Set default zone for connections and interfaces where no zone has been selected. Setting the default zone changes the zone for the connections or interfaces, that are using the default zone.</dl>
<p> <code>&#8211;get-zones</code></p>
<dl>
<dt>
<dd> Print predefined zones as a space separated list.</dl>
<p> <code>&#8211;get-services</code></p>
<dl>
<dt>
<dd> Print predefined services as a space separated list.</dl>
<p> <code>&#8211;get-icmptypes</code></p>
<dl>
<dt>
<dd> Print predefined icmptypes as a space separated list.</dl>
<p> <code>&#8211;get-zone-of-interface</code>=<i>interface</i></p>
<dl>
<dt>
<dd> Print the name of the zone the <i>interface</i> is bound to or <i>no zone</i>.</dl>
<p> <code>&#8211;get-zone-of-source</code>=<i>source</i>[/<i>mask</i>]|<i>MAC</i>|ipset:<i>ipset</i></p>
<dl>
<dt>
<dd> Print the name of the zone the source is bound to or <i>no zone</i>.</dl>
<p> <code>&#8211;info-zone=</code><i>zone</i></p>
<dl>
<dt>
<dd> Print information about the zone <i>zone</i>. The output format is: </p>
<dl>
<dt>
<dd>
<pre>
<i>zone</i>
  interfaces: <i>interface1</i> ..
  sources: <i>source1</i> ..
  services: <i>service1</i> ..
  ports: <i>port1</i> ..
  protocols: <i>protocol1</i> ..
  forward-ports:
        <i>forward-port1</i>
        ..
  source-ports: <i>source-port1</i> ..
  icmp-blocks: <i>icmp-type1</i> ..
  rich rules:
        <i>rich-rule1</i>
        ..
              
</pre>
</dl>
</dl>
<p> <code>&#8211;list-all-zones</code></p>
<dl>
<dt>
<dd> List everything added for or enabled in all zones. The output format is: </p>
<dl>
<dt>
<dd>
<pre>
<i>zone1</i>
  interfaces: <i>interface1</i> ..
  sources: <i>source1</i> ..
  services: <i>service1</i> ..
  ports: <i>port1</i> ..
  protocols: <i>protocol1</i> ..
  forward-ports:
        <i>forward-port1</i>
        ..
  source-ports: <i>source-port1</i> ..
  icmp-blocks: <i>icmp-type1</i> ..
  rich rules:
        <i>rich-rule1</i>
        ..
..
              
</pre>
</dl>
</dl>
<p> <code>&#8211;new-zone</code>=<i>zone</i></p>
<dl>
<dt>
<dd> Add a new permanent zone.</dl>
<p> <code>&#8211;new-zone-from-file</code>=<i>filename</i> [<code>&#8211;name</code>=<i>zone</i>]</p>
<dl>
<dt>
<dd> Add a new permanent zone from a prepared zone file with an optional name override.</dl>
<p> <code>&#8211;path-zone=</code><i>zone</i></p>
<dl>
<dt>
<dd> Print path of the zone configuration file.</dl>
<p> <code>&#8211;delete-zone</code>=<i>zone</i></p>
<dl>
<dt>
<dd> Delete an existing permanent zone.</dl>
<p> <code>&#8211;zone</code>=<i>zone</i> <code>&#8211;set-description</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set new description to zone</dl>
<p> <code>&#8211;zone</code>=<i>zone</i> <code>&#8211;get-description</code></p>
<dl>
<dt>
<dd> Print description for zone</dl>
<p> <code>&#8211;zone</code>=<i>zone</i> <code>&#8211;set-short</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set short description to zone</dl>
<p> <code>&#8211;zone</code>=<i>zone</i> <code>&#8211;get-short</code></p>
<dl>
<dt>
<dd> Print short description for zone</dl>
<p> <code>&#8211;zone</code>=<i>zone</i> <code>&#8211;get-target</code></p>
<dl>
<dt>
<dd> Get the target of a permanent zone.</dl>
<p> <code>&#8211;zone</code>=<i>zone</i> <code>&#8211;set-target</code>=<i>zone</i></p>
<dl>
<dt>
<dd> Set the target of a permanent zone.</dl>
<h3>Options to Adapt and Query Zones</h3>
<p> Options in this section affect only one particular zone. If used with <code>&#8211;zone</code>=<i>zone</i> option, they affect the zone <i>zone</i>. If the option is omitted, they affect default zone (see <code>&#8211;get-default-zone</code>). </p>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-all</code></p>
<dl>
<dt>
<dd> List everything added for or enabled in <i>zone</i>. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-services</code></p>
<dl>
<dt>
<dd> List services added for <i>zone</i> as a space separated list. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-service</code>=<i>service</i></p>
<dl>
<dt>
<dd> Add a service for <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times. </p>
<p> The service is one of the firewalld provided services. To get a list of the supported services, use <code>firewall-cmd &#8211;get-services</code>.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-service-from-zone</code>=<i>service</i></p>
<dl>
<dt>
<dd> Remove a service from <i>zone</i>. This option can be specified multiple times. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-service</code>=<i>service</i></p>
<dl>
<dt>
<dd> Return whether <i>service</i> has been added for <i>zone</i>. If zone is omitted, default zone will be used. Returns 0 if true, 1 otherwise.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-ports</code></p>
<dl>
<dt>
<dd> List ports added for <i>zone</i> as a space separated list. A port is of the form <i>portid</i>[-<i>portid</i>]/<i>protocol</i>, it can be either a port and protocol pair or a port range with a protocol. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Add the port for <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times. </p>
<p> The port can either be a single port number or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Remove the port from <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Return whether the port has been added for <i>zone</i>. If zone is omitted, default zone will be used. Returns 0 if true, 1 otherwise.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-protocols</code></p>
<dl>
<dt>
<dd> List protocols added for <i>zone</i> as a space separated list. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-protocol</code>=<i>protocol</i></p>
<dl>
<dt>
<dd> Add the protocol for <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times. If a timeout is supplied, the rule will be active for the specified amount of time and will be removed automatically afterwards. <i>timeval</i> is either a number (of seconds) or number followed by one of characters <i>s</i> (seconds), <i>m</i> (minutes), <i>h</i> (hours), for example <i>20m</i> or <i>1h</i>. </p>
<p> The protocol can be any protocol supported by the system. Please have a look at <i>/etc/protocols</i> for supported protocols.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-protcol</code>=<i>protocol</i></p>
<dl>
<dt>
<dd> Remove the protocol from <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-protocol</code>=<i>protocol</i></p>
<dl>
<dt>
<dd> Return whether the protocol has been added for <i>zone</i>. If zone is omitted, default zone will be used. Returns 0 if true, 1 otherwise.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-icmp-blocks</code></p>
<dl>
<dt>
<dd> List Internet Control Message Protocol (ICMP) type blocks added for <i>zone</i> as a space separated list. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-icmp-block</code>=<i>icmptype</i></p>
<dl>
<dt>
<dd> Add an ICMP block for <i>icmptype</i> for <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times. </p>
<p> The <i>icmptype</i> is the one of the icmp types firewalld supports. To get a listing of supported icmp types: <code>firewall-cmd &#8211;get-icmptypes</code></dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-icmp-block</code>=<i>icmptype</i></p>
<dl>
<dt>
<dd> Remove the ICMP block for <i>icmptype</i> from <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-icmp-block</code>=<i>icmptype</i></p>
<dl>
<dt>
<dd> Return whether an ICMP block for <i>icmptype</i> has been added for <i>zone</i>. If zone is omitted, default zone will be used. Returns 0 if true, 1 otherwise.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-forward-ports</code></p>
<dl>
<dt>
<dd> List <i>IPv4</i> forward ports added for <i>zone</i> as a space separated list. If zone is omitted, default zone will be used. </p>
<p> For <i>IPv6</i> forward ports, please use the rich language.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-forward-port</code>=port=<i>portid</i>[-<i>portid</i>]:proto=<i>protocol</i>[:toport=<i>portid</i>[-<i>portid</i>]][:toaddr=<i>address</i>[/<i>mask</i>]]</p>
<dl>
<dt>
<dd> Add the <i>IPv4</i> forward port for <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times. </p>
<p> The port can either be a single port number <i>portid</i> or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>. The destination address is a simple IP address. </p>
<p> For <i>IPv6</i> forward ports, please use the rich language.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-forward-port</code>=port=<i>portid</i>[-<i>portid</i>]:proto=<i>protocol</i>[:toport=<i>portid</i>[-<i>portid</i>]][:toaddr=<i>address</i>[/<i>mask</i>]]</p>
<dl>
<dt>
<dd> Remove the <i>IPv4</i> forward port from <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times. </p>
<p> For <i>IPv6</i> forward ports, please use the rich language.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-forward-port</code>=port=<i>portid</i>[-<i>portid</i>]:proto=<i>protocol</i>[:toport=<i>portid</i>[-<i>portid</i>]][:toaddr=<i>address</i>[/<i>mask</i>]]</p>
<dl>
<dt>
<dd> Return whether the <i>IPv4</i> forward port has been added for <i>zone</i>. If zone is omitted, default zone will be used. Returns 0 if true, 1 otherwise. </p>
<p> For <i>IPv6</i> forward ports, please use the rich language.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-source-ports</code></p>
<dl>
<dt>
<dd> List source ports added for <i>zone</i> as a space separated list. A port is of the form <i>portid</i>[-<i>portid</i>]/<i>protocol</i>. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-source-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Add the source port for <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times. If a timeout is supplied, the rule will be active for the specified amount of time and will be removed automatically afterwards. </p>
<p> The port can either be a single port number or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-source-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Remove the source port from <i>zone</i>. If zone is omitted, default zone will be used. This option can be specified multiple times.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-source-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Return whether the source port has been added for <i>zone</i>. If zone is omitted, default zone will be used. Returns 0 if true, 1 otherwise.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-masquerade</code></p>
<dl>
<dt>
<dd> Enable <i>IPv4</i> masquerade for <i>zone</i>. If zone is omitted, default zone will be used. Masquerading is useful if the machine is a router and machines connected over an interface in another zone should be able to use the first connection. </p>
<p> For <i>IPv6</i> masquerading, please use the rich language.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-masquerade</code></p>
<dl>
<dt>
<dd> Disable <i>IPv4</i> masquerade for <i>zone</i>. If zone is omitted, default zone will be used. </p>
<p> For <i>IPv6</i> masquerading, please use the rich language.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-masquerade</code></p>
<dl>
<dt>
<dd> Return whether <i>IPv4</i> masquerading has been enabled for <i>zone</i>. If zone is omitted, default zone will be used. Returns 0 if true, 1 otherwise. </p>
<p> For <i>IPv6</i> masquerading, please use the rich language.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-rich-rules</code></p>
<dl>
<dt>
<dd> List rich language rules added for <i>zone</i> as a newline separated list. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-rich-rule</code>=&#8217;<i>rule</i>&#8216;</p>
<dl>
<dt>
<dd> Add rich language rule &#8216;<i>rule</i>&#8216; for <i>zone</i>. This option can be specified multiple times. If zone is omitted, default zone will be used. </p>
<p> For the rich language rule syntax, please have a look at <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5).</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-rich-rule</code>=&#8217;<i>rule</i>&#8216;</p>
<dl>
<dt>
<dd> Remove rich language rule &#8216;<i>rule</i>&#8216; from <i>zone</i>. This option can be specified multiple times. If zone is omitted, default zone will be used. </p>
<p> For the rich language rule syntax, please have a look at <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5).</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-rich-rule</code>=&#8217;<i>rule</i>&#8216;</p>
<dl>
<dt>
<dd> Return whether a rich language rule &#8216;<i>rule</i>&#8216; has been added for <i>zone</i>. If zone is omitted, default zone will be used. Returns 0 if true, 1 otherwise. </p>
<p> For the rich language rule syntax, please have a look at <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5).</dl>
<h3>Options to Handle Bindings of Interfaces</h3>
<p> Binding an interface to a zone means that this zone settings are used to restrict traffic via the interface. </p>
<p> Options in this section affect only one particular zone. If used with <code>&#8211;zone</code>=<i>zone</i> option, they affect the zone <i>zone</i>. If the option is omitted, they affect default zone (see <code>&#8211;get-default-zone</code>). </p>
<p> For a list of predefined zones use <code>firewall-cmd &#8211;get-zones</code>. </p>
<p> An interface name is a string up to 16 characters long, that may not contain <code>&#8216; &#8216;</code>, <code>&#8216;/&#8217;</code>, <code>&#8216;!&#8217;</code> and <code>&#8216;*&#8217;</code>. </p>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-interfaces</code></p>
<dl>
<dt>
<dd> List interfaces that are bound to zone <i>zone</i> as a space separated list. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-interface</code>=<i>interface</i></p>
<dl>
<dt>
<dd> Bind interface <i>interface</i> to zone <i>zone</i>. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;change-interface</code>=<i>interface</i></p>
<dl>
<dt>
<dd> Change zone the interface <i>interface</i> is bound to to zone <i>zone</i>. If zone is omitted, default zone will be used. If old and new zone are the same, the call will be ignored without an error. If the interface has not been bound to a zone before, it will behave like <code>&#8211;add-interface</code>.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-interface</code>=<i>interface</i></p>
<dl>
<dt>
<dd> Query whether interface <i>interface</i> is bound to zone <i>zone</i>. Returns 0 if true, 1 otherwise.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-interface</code>=<i>interface</i></p>
<dl>
<dt>
<dd> Remove binding of interface <i>interface</i> from zone <i>zone</i>. If zone is omitted, default zone will be used.</dl>
<h3>Options to Handle Bindings of Sources</h3>
<p> Binding a source to a zone means that this zone settings will be used to restrict traffic from this source. </p>
<p> A source address or address range is either an IP address or a network IP address with a mask for IPv4 or IPv6 or a MAC address or an ipset with the ipset: prefix. For IPv4, the mask can be a network mask or a plain number. For IPv6 the mask is a plain number. The use of host names is not supported. </p>
<p> Options in this section affect only one particular zone. If used with <code>&#8211;zone</code>=<i>zone</i> option, they affect the zone <i>zone</i>. If the option is omitted, they affect default zone (see <code>&#8211;get-default-zone</code>). </p>
<p> For a list of predefined zones use <code>firewall-cmd &#8211;get-zones</code>. </p>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;list-sources</code></p>
<dl>
<dt>
<dd> List sources that are bound to zone <i>zone</i> as a space separated list. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;add-source</code>=<i>source</i>[/<i>mask</i>]|<i>MAC</i>|ipset:<i>ipset</i></p>
<dl>
<dt>
<dd> Bind the source to zone <i>zone</i>. If zone is omitted, default zone will be used.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;change-source</code>=<i>source</i>[/<i>mask</i>]|<i>MAC</i>|ipset:<i>ipset</i></p>
<dl>
<dt>
<dd> Change zone the source is bound to to zone <i>zone</i>. If zone is omitted, default zone will be used. If old and new zone are the same, the call will be ignored without an error. If the source has not been bound to a zone before, it will behave like <code>&#8211;add-source</code>.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;query-source</code>=<i>source</i>[/<i>mask</i>]|<i>MAC</i>|ipset:<i>ipset</i></p>
<dl>
<dt>
<dd> Query whether the source is bound to the zone <i>zone</i>. Returns 0 if true, 1 otherwise.</dl>
<p> [<code>&#8211;zone</code>=<i>zone</i>] <code>&#8211;remove-source</code>=<i>source</i>[/<i>mask</i>]|<i>MAC</i>|ipset:<i>ipset</i></p>
<dl>
<dt>
<dd> Remove binding of the source from zone <i>zone</i>. If zone is omitted, default zone will be used.</dl>
<h3>IPSet Options</h3>
<p> <code>&#8211;new-ipset</code>=<i>ipset</i> <code>&#8211;type</code>=<i>ipset type</i> [<code>&#8211;option</code>=<i>ipset option</i>[=<i>value</i>]]</p>
<dl>
<dt>
<dd> Add a new permanent ipset with specifying the type and optional options.</dl>
<p> <code>&#8211;new-ipset-from-file</code>=<i>filename</i> [<code>&#8211;name</code>=<i>ipset</i>]</p>
<dl>
<dt>
<dd> Add a new permanent ipset from a prepared ipset file with an optional name override.</dl>
<p> <code>&#8211;delete-ipset</code>=<i>ipset</i></p>
<dl>
<dt>
<dd> Delete an existing permanent ipset.</dl>
<p> <code>&#8211;info-ipset=</code><i>ipset</i></p>
<dl>
<dt>
<dd> Print information about the ipset <i>ipset</i>. The output format is: </p>
<dl>
<dt>
<dd>
<pre>
<i>ipset</i>
  type: <i>type</i>
  options: <i>option1[=value1]</i> ..
  entries: <i>entry1</i> ..
              
</pre>
</dl>
</dl>
<p> <code>&#8211;get-ipsets</code></p>
<dl>
<dt>
<dd> Print predefined ipsets as a space separated list.</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;add-entry</code>=<i>entry</i></p>
<dl>
<dt>
<dd> Add a new entry to the ipset.</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;remove-entry</code>=<i>entry</i></p>
<dl>
<dt>
<dd> Remove an entry from the ipset.</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;query-entry</code>=<i>entry</i></p>
<dl>
<dt>
<dd> Return whether the entry has been added to an ipset. Returns 0 if true, 1 otherwise.</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;get-entries</code></p>
<dl>
<dt>
<dd> List all entries of the ipset.</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;add-entries-from-file</code>=<i>filename</i></p>
<dl>
<dt>
<dd> Add a new entries to the ipset from the file. For all entries that are listed in the file but already in the ipset, a warning will be printed. </p>
<p> The file should contain an entry per line. Lines starting with an hash or semicolon are ignored. Also empty lines.</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;remove-entries-from-file</code>=<i>filename</i></p>
<dl>
<dt>
<dd> Remove existing entries from the ipset from the file. For all entries that are listed in the file but not in the ipset, a warning will be printed. </p>
<p> The file should contain an entry per line. Lines starting with an hash or semicolon are ignored. Also empty lines.</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;set-description</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set new description to ipset</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;get-description</code></p>
<dl>
<dt>
<dd> Print description for ipset</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;set-short</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set new short description to ipset</dl>
<p> <code>&#8211;ipset</code>=<i>ipset</i> <code>&#8211;get-short</code></p>
<dl>
<dt>
<dd> Print short description for ipset</dl>
<p> <code>&#8211;path-ipset=</code><i>ipset</i></p>
<dl>
<dt>
<dd> Print path of the ipset configuration file.</dl>
<h3>Service Options</h3>
<p> <code>&#8211;info-service=</code><i>service</i></p>
<dl>
<dt>
<dd> Print information about the service <i>service</i>. The output format is: </p>
<dl>
<dt>
<dd>
<pre>
<i>service</i>
  ports: <i>port1</i> ..
  protocols: <i>protocol1</i> ..
  source-ports: <i>source-port1</i> ..
  modules: <i>module1</i> ..
  destination: <i>ipv1</i>:<i>address1</i> ..
              
</pre>
</dl>
</dl>
<p> <code>&#8211;new-service</code>=<i>service</i></p>
<dl>
<dt>
<dd> Add a new permanent service.</dl>
<p> <code>&#8211;new-service-from-file</code>=<i>filename</i> [<code>&#8211;name</code>=<i>service</i>]</p>
<dl>
<dt>
<dd> Add a new permanent service from a prepared service file with an optional name override.</dl>
<p> <code>&#8211;delete-service</code>=<i>service</i></p>
<dl>
<dt>
<dd> Delete an existing permanent service.</dl>
<p> <code>&#8211;path-service=</code><i>service</i></p>
<dl>
<dt>
<dd> Print path of the service configuration file.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;set-description</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set new description to service</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;get-description</code></p>
<dl>
<dt>
<dd> Print description for service</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;set-short</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set short description to service</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;get-short</code></p>
<dl>
<dt>
<dd> Print short description for service</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;add-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Add a new port to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;remove-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Remove a port from the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;query-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Return wether the port has been added to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;get-ports</code></p>
<dl>
<dt>
<dd> List ports added to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;add-protocol</code>=<i>protocol</i></p>
<dl>
<dt>
<dd> Add a new protocol to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;remove-protocol</code>=<i>protocol</i></p>
<dl>
<dt>
<dd> Remove a protocol from the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;query-protocol</code>=<i>protocol</i></p>
<dl>
<dt>
<dd> Return wether the protocol has been added to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;get-protocols</code></p>
<dl>
<dt>
<dd> List protocols added to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;add-source-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Add a new source port to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;remove-source-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Remove a source port from the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;query-source-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Return wether the source port has been added to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;get-source-ports</code></p>
<dl>
<dt>
<dd> List source ports added to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;add-module</code>=<i>module</i></p>
<dl>
<dt>
<dd> Add a new module to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;remove-module</code>=<i>module</i></p>
<dl>
<dt>
<dd> Remove a module from the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;query-module</code>=<i>module</i></p>
<dl>
<dt>
<dd> Return wether the module has been added to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;get-modules</code></p>
<dl>
<dt>
<dd> List modules added to the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;set-destination</code>=<i>ipv</i>:<i>address</i>[/<i>mask</i>]</p>
<dl>
<dt>
<dd> Set destination for ipv to address[/mask] in the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;remove-destination</code>=<i>ipv</i></p>
<dl>
<dt>
<dd> Remove the destination for ipv from the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;query-destination</code>=<i>ipv</i>:<i>address</i>[/<i>mask</i>]</p>
<dl>
<dt>
<dd> Return wether the destination ipv to address[/mask] has been set in the permanent service.</dl>
<p> <code>&#8211;service</code>=<i>service</i> <code>&#8211;get-destinations</code></p>
<dl>
<dt>
<dd> List destinations added to the permanent service.</dl>
<h3>Helper Options</h3>
<p> Options in this section affect only one particular helper. </p>
<p> <code>&#8211;info-helper=</code><i>helper</i></p>
<dl>
<dt>
<dd> Print information about the helper <i>helper</i>. The output format is: </p>
<dl>
<dt>
<dd>
<pre>
<i>helper</i>
  family: <i>family</i>
  module: <i>module</i>
  ports: <i>port1</i> ..
              
</pre>
</dl>
</dl>
<p> The following options are only usable in the permanent configuration. </p>
<p> <code>&#8211;new-helper</code>=<i>helper</i> <code>&#8211;module</code>=<i>nf_conntrack_module</i> [<code>&#8211;family</code>=<i>ipv4</i>|<i>ipv6</i>]</p>
<dl>
<dt>
<dd> Add a new permanent helper with module and optionally family defined.</dl>
<p> <code>&#8211;new-helper-from-file</code>=<i>filename</i> [<code>&#8211;name</code>=<i>helper</i>]</p>
<dl>
<dt>
<dd> Add a new permanent helper from a prepared helper file with an optional name override.</dl>
<p> <code>&#8211;delete-helper</code>=<i>helper</i></p>
<dl>
<dt>
<dd> Delete an existing permanent helper.</dl>
<p> <code>&#8211;load-helper-defaults</code>=<i>helper</i></p>
<dl>
<dt>
<dd> Load helper default settings or report NO_DEFAULTS error.</dl>
<p> <code>&#8211;path-helper=</code><i>helper</i></p>
<dl>
<dt>
<dd> Print path of the helper configuration file.</dl>
<p> <code>&#8211;get-helpers</code></p>
<dl>
<dt>
<dd> Print predefined helpers as a space separated list.</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;set-description</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set new description to helper</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;get-description</code></p>
<dl>
<dt>
<dd> Print description for helper</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;set-short</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set short description to helper</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;get-short</code></p>
<dl>
<dt>
<dd> Print short description for helper</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;add-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Add a new port to the permanent helper.</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;remove-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Remove a port from the permanent helper.</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;query-port</code>=<i>portid</i>[-<i>portid</i>]/<i>protocol</i></p>
<dl>
<dt>
<dd> Return wether the port has been added to the permanent helper.</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;get-ports</code></p>
<dl>
<dt>
<dd> List ports added to the permanent helper.</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;set-module</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set module description for helper</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;get-module</code></p>
<dl>
<dt>
<dd> Print module description for helper</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;set-family</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set family description for helper</dl>
<p> <code>&#8211;helper</code>=<i>helper</i> <code>&#8211;get-family</code></p>
<dl>
<dt>
<dd> Print family description of helper</dl>
<h3>Internet Control Message Protocol (ICMP) type Options</h3>
<p> <code>&#8211;info-icmptype=</code><i>icmptype</i></p>
<dl>
<dt>
<dd> Print information about the icmptype <i>icmptype</i>. The output format is: </p>
<dl>
<dt>
<dd>
<pre>
<i>icmptype</i>
  destination: <i>ipv1</i> ..
              
</pre>
</dl>
</dl>
<p> <code>&#8211;new-icmptype</code>=<i>icmptype</i></p>
<dl>
<dt>
<dd> Add a new permanent icmptype.</dl>
<p> <code>&#8211;new-icmptype-from-file</code>=<i>filename</i> [<code>&#8211;name</code>=<i>icmptype</i>]</p>
<dl>
<dt>
<dd> Add a new permanent icmptype from a prepared icmptype file with an optional name override.</dl>
<p> <code>&#8211;delete-icmptype</code>=<i>icmptype</i></p>
<dl>
<dt>
<dd> Delete an existing permanent icmptype.</dl>
<p> <code>&#8211;icmptype</code>=<i>icmptype</i> <code>&#8211;set-description</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set new description to icmptype</dl>
<p> <code>&#8211;icmptype</code>=<i>icmptype</i> <code>&#8211;get-description</code></p>
<dl>
<dt>
<dd> Print description for icmptype</dl>
<p> <code>&#8211;icmptype</code>=<i>icmptype</i> <code>&#8211;set-short</code>=<i>description</i></p>
<dl>
<dt>
<dd> Set short description to icmptype</dl>
<p> <code>&#8211;icmptype</code>=<i>icmptype</i> <code>&#8211;get-short</code></p>
<dl>
<dt>
<dd> Print short description for icmptype</dl>
<p> <code>&#8211;icmptype</code>=<i>icmptype</i> <code>&#8211;add-destination</code>=<i>ipv</i></p>
<dl>
<dt>
<dd> Enable destination for ipv in permanent icmptype. ipv is one of <i>ipv4</i> or <i>ipv6</i>.</dl>
<p> <code>&#8211;icmptype</code>=<i>icmptype</i> <code>&#8211;remove-destination</code>=<i>ipv</i></p>
<dl>
<dt>
<dd> Disable destination for ipv in permanent icmptype. ipv is one of <i>ipv4</i> or <i>ipv6</i>.</dl>
<p> <code>&#8211;icmptype</code>=<i>icmptype</i> <code>&#8211;query-destination</code>=<i>ipv</i></p>
<dl>
<dt>
<dd> Return whether destination for ipv is enabled in permanent icmptype. ipv is one of <i>ipv4</i> or <i>ipv6</i>.</dl>
<p> <code>&#8211;icmptype</code>=<i>icmptype</i> <code>&#8211;get-destinations</code></p>
<dl>
<dt>
<dd> List destinations in permanent icmptype.</dl>
<p> <code>&#8211;path-icmptype=</code><i>icmptype</i></p>
<dl>
<dt>
<dd> Print path of the icmptype configuration file.</dl>
<h3>Direct Options</h3>
<p> The direct options give a more direct access to the firewall. These options require user to know basic iptables concepts, i.e. <i>table</i> (filter/mangle/nat/&#8230;), <i>chain</i> (INPUT/OUTPUT/FORWARD/&#8230;), <i>commands</i> (-A/-D/-I/&#8230;), <i>parameters</i> (-p/-s/-d/-j/&#8230;) and <i>targets</i> (ACCEPT/DROP/REJECT/&#8230;). </p>
<p> Direct options should be used only as a last resort when it&#8217;s not possible to use for example <code>&#8211;add-service</code>=<i>service</i> or <code>&#8211;add-rich-rule</code>=&#8217;<i>rule</i>&#8216;. </p>
<p> The first argument of each option has to be <i>ipv4</i> or <i>ipv6</i> or <i>eb</i>. With <i>ipv4</i> it will be for IPv4 (<code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8)), with <i>ipv6</i> for IPv6 (<code><a href="/docs/linux/man/8-ip6tables/">ip6tables</a></code>(8)) and with <i>eb</i> for ethernet bridges (<code><a href="/docs/linux/man/8-ebtables/">ebtables</a></code>(8)). </p>
<p> <code>&#8211;direct</code> <code>&#8211;get-all-chains</code></p>
<dl>
<dt>
<dd> Get all chains added to all tables. </p>
<p> This option concerns only chains previously added with <code>&#8211;direct &#8211;add-chain</code>.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;get-chains</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>table</i></p>
<dl>
<dt>
<dd> Get all chains added to table <i>table</i> as a space separated list. </p>
<p> This option concerns only chains previously added with <code>&#8211;direct &#8211;add-chain</code>.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;add-chain</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>table</i> <i>chain</i></p>
<dl>
<dt>
<dd> Add a new chain with name <i>chain</i> to table <i>table</i>. </p>
<p> There already exist basic chains to use with direct options, for example <i>INPUT_direct</i> chain (see <i>iptables-save | grep direct</i> output for all of them). These chains are jumped into before chains for zones, i.e. every rule put into <i>INPUT_direct</i> will be checked before rules in zones.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;remove-chain</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>table</i> <i>chain</i></p>
<dl>
<dt>
<dd> Remove the chain with name <i>chain</i> from table <i>table</i>.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;query-chain</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>table</i> <i>chain</i></p>
<dl>
<dt>
<dd> Return whether a chain with name <i>chain</i> exists in table <i>table</i>. Returns 0 if true, 1 otherwise. </p>
<p> This option concerns only chains previously added with <code>&#8211;direct &#8211;add-chain</code>.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;get-all-rules</code></p>
<dl>
<dt>
<dd> Get all rules added to all chains in all tables as a newline separated list of the priority and arguments.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;get-rules</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>table</i> <i>chain</i></p>
<dl>
<dt>
<dd> Get all rules added to chain <i>chain</i> in table <i>table</i> as a newline separated list of the priority and arguments.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;add-rule</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>table</i> <i>chain</i> <i>priority</i> <i>args</i></p>
<dl>
<dt>
<dd> Add a rule with the arguments <i>args</i> to chain <i>chain</i> in table <i>table</i> with priority <i>priority</i>. </p>
<p> The <i>priority</i> is used to order rules. Priority 0 means add rule on top of the chain, with a higher priority the rule will be added further down. Rules with the same priority are on the same level and the order of these rules is not fixed and may change. If you want to make sure that a rule will be added after another one, use a low priority for the first and a higher for the following.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;remove-rule</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>table</i> <i>chain</i> <i>priority</i> <i>args</i></p>
<dl>
<dt>
<dd> Remove a rule with <i>priority</i> and the arguments <i>args</i> from chain <i>chain</i> in table <i>table</i>.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;remove-rules</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>table</i> <i>chain</i></p>
<dl>
<dt>
<dd> Remove all rules in the chain with name <i>chain</i> exists in table <i>table</i>. </p>
<p> This option concerns only rules previously added with <code>&#8211;direct &#8211;add-rule</code> in this chain.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;query-rule</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>table</i> <i>chain</i> <i>priority</i> <i>args</i></p>
<dl>
<dt>
<dd> Return whether a rule with <i>priority</i> and the arguments <i>args</i> exists in chain <i>chain</i> in table <i>table</i>. Returns 0 if true, 1 otherwise.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;get-all-passthroughs</code></p>
<dl>
<dt>
<dd> Get all permanent passthrough as a newline separated list of the ipv value and arguments.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;get-passthroughs</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> }</p>
<dl>
<dt>
<dd> Get all permanent passthrough rules for the ipv value as a newline separated list of the priority and arguments.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;add-passthrough</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>args</i></p>
<dl>
<dt>
<dd> Add a permanent passthrough rule with the arguments <i>args</i> for the ipv value.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;remove-passthrough</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>args</i></p>
<dl>
<dt>
<dd> Remove a permanent passthrough rule with the arguments <i>args</i> for the ipv value.</dl>
<p> <code>&#8211;direct</code> <code>&#8211;query-passthrough</code> { <i>ipv4</i> | <i>ipv6</i> | <i>eb</i> } <i>args</i></p>
<dl>
<dt>
<dd> Return whether a permanent passthrough rule with the arguments <i>args</i> exists for the ipv value. Returns 0 if true, 1 otherwise.</dl>
<h3>Lockdown Options</h3>
<p> Local applications or services are able to change the firewall configuration if they are running as root (example: libvirt) or are authenticated using PolicyKit. With this feature administrators can lock the firewall configuration so that only applications on lockdown whitelist are able to request firewall changes. </p>
<p> The lockdown access check limits D-Bus methods that are changing firewall rules. Query, list and get methods are not limited. </p>
<p> The lockdown feature is a very light version of user and application policies for firewalld and is turned off by default. </p>
<p> <code>&#8211;lockdown-on</code></p>
<dl>
<dt>
<dd> Enable lockdown. Be careful &#8211; if firewall-cmd is not on lockdown whitelist when you enable lockdown you won&#8217;t be able to disable it again with firewall-cmd, you would need to edit firewalld.conf.</dl>
<p> <code>&#8211;lockdown-off</code></p>
<dl>
<dt>
<dd> Disable lockdown.</dl>
<p> <code>&#8211;query-lockdown</code></p>
<dl>
<dt>
<dd> Query whether lockdown is enabled. Returns 0 if lockdown is enabled, 1 otherwise.</dl>
<h3>Lockdown Whitelist Options</h3>
<p> The lockdown whitelist can contain <i>commands</i>, <i>contexts</i>, <i>users</i> and <i>user ids</i>. </p>
<p> If a command entry on the whitelist ends with an asterisk &#8216;*&#8217;, then all command lines starting with the command will match. If the &#8216;*&#8217; is not there the absolute command inclusive arguments must match. </p>
<p> Commands for user root and others is not always the same. Example: As root <code>/bin/firewall-cmd</code> is used, as a normal user <code>/usr/bin/firewall-cmd</code> is be used on Fedora. </p>
<p> The context is the security (SELinux) context of a running application or service. To get the context of a running application use <code>ps -e &#8211;context</code>. </p>
<p> <code>Warning:</code> If the context is unconfined, then this will open access for more than the desired application. </p>
<p> The lockdown whitelist entries are checked in the following order:</p>
<dl>
<dt>
<dd> 1. <i>context</i></dl>
<dl>
<dt>
<dd> 2. <i>uid</i></dl>
<dl>
<dt>
<dd> 3. <i>user</i></dl>
<dl>
<dt>
<dd> 4. <i>command</i></dl>
<p> <code>&#8211;list-lockdown-whitelist-commands</code></p>
<dl>
<dt>
<dd> List all command lines that are on the whitelist.</dl>
<p> <code>&#8211;add-lockdown-whitelist-command</code>=<i>command</i></p>
<dl>
<dt>
<dd> Add the <i>command</i> to the whitelist.</dl>
<p> <code>&#8211;remove-lockdown-whitelist-command</code>=<i>command</i></p>
<dl>
<dt>
<dd> Remove the <i>command</i> from the whitelist.</dl>
<p> <code>&#8211;query-lockdown-whitelist-command</code>=<i>command</i></p>
<dl>
<dt>
<dd> Query whether the <i>command</i> is on the whitelist. Returns 0 if true, 1 otherwise.</dl>
<p> <code>&#8211;list-lockdown-whitelist-contexts</code></p>
<dl>
<dt>
<dd> List all contexts that are on the whitelist.</dl>
<p> <code>&#8211;add-lockdown-whitelist-context</code>=<i>context</i></p>
<dl>
<dt>
<dd> Add the context <i>context</i> to the whitelist.</dl>
<p> <code>&#8211;remove-lockdown-whitelist-context</code>=<i>context</i></p>
<dl>
<dt>
<dd> Remove the <i>context</i> from the whitelist.</dl>
<p> <code>&#8211;query-lockdown-whitelist-context</code>=<i>context</i></p>
<dl>
<dt>
<dd> Query whether the <i>context</i> is on the whitelist. Returns 0 if true, 1 otherwise.</dl>
<p> <code>&#8211;list-lockdown-whitelist-uids</code></p>
<dl>
<dt>
<dd> List all user ids that are on the whitelist.</dl>
<p> <code>&#8211;add-lockdown-whitelist-uid</code>=<i>uid</i></p>
<dl>
<dt>
<dd> Add the user id <i>uid</i> to the whitelist.</dl>
<p> <code>&#8211;remove-lockdown-whitelist-uid</code>=<i>uid</i></p>
<dl>
<dt>
<dd> Remove the user id <i>uid</i> from the whitelist.</dl>
<p> <code>&#8211;query-lockdown-whitelist-uid</code>=<i>uid</i></p>
<dl>
<dt>
<dd> Query whether the user id <i>uid</i> is on the whitelist. Returns 0 if true, 1 otherwise.</dl>
<p> <code>&#8211;list-lockdown-whitelist-users</code></p>
<dl>
<dt>
<dd> List all user names that are on the whitelist.</dl>
<p> <code>&#8211;add-lockdown-whitelist-user</code>=<i>user</i></p>
<dl>
<dt>
<dd> Add the user name <i>user</i> to the whitelist.</dl>
<p> <code>&#8211;remove-lockdown-whitelist-user</code>=<i>user</i></p>
<dl>
<dt>
<dd> Remove the user name <i>user</i> from the whitelist.</dl>
<p> <code>&#8211;query-lockdown-whitelist-user</code>=<i>user</i></p>
<dl>
<dt>
<dd> Query whether the user name <i>user</i> is on the whitelist. Returns 0 if true, 1 otherwise.</dl>
<h3>Policy Options</h3>
<p> <code>&#8211;policy-server</code></p>
<dl>
<dt>
<dd> Change Polkit actions to &#8216;server&#8217; (more restricted)</dl>
<p> <code>&#8211;policy-desktop</code></p>
<dl>
<dt>
<dd> Change Polkit actions to &#8216;desktop&#8217; (less restricted)</dl>
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
