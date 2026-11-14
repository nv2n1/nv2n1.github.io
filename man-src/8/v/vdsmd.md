---
title: "vdsmd(8)"
name: "vdsmd"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vdsmd/"
description: "vdsmd – Virtual Desktops and Servers Manager @ENGINENAME@ host agent"
---

<p>vdsmd &#8211; Virtual Desktops and Servers Manager<br />
 @ENGINENAME@ host agent</p>
<h2>Synopsis</h2>
<p><code>service vdsmd start</code></p>
<h2>Description</h2>
<p>The <code>VDSM</code> service is required by a <code>@ENGINENAME@</code> to manage oVirt Nodes and Linux hosts. Currently, only Fedora and Red Hat Enterprise Linux are supported. VDSM manages and monitors the host&#8217;s storage, memory and networks as well as virtual machine creation, other host administration tasks, statistics gathering, and log collection. VDSM should be run as a daemon on each node managed by @ENGINENAME@. It answers XML-RPC calls from clients (mostly @ENGINENAME@). </p>
<h2>Hooks</h2>
<p>VDSM is extendible: it has hooks in strategic locations, where it executes external scripts. <code>Hooks API is new and is subject to future changes.</code> Currently-supported hooks have self-explanatory names:<br />
&nbsp;<wbr>before_vm_start, after_vm_start,<br />
&nbsp;<wbr>before_vm_cont, after_vm_cont,<br />
&nbsp;<wbr>before_vm_pause, after_vm_pause,<br />
&nbsp;<wbr>before_vm_hibernate, after_vm_hibernate,<br />
&nbsp;<wbr>before_vm_dehibernate, after_vm_dehibernate,<br />
&nbsp;<wbr>before_vm_migrate_source, after_vm_migrate_source,<br />
&nbsp;<wbr>before_vm_migrate_destination, after_vm_migrate_destination,<br />
&nbsp;<wbr>before_device_migrate_source, after_device_migrate_source,<br />
&nbsp;<wbr>before_device_migrate_destination, after_device_migrate_destination,<br />
&nbsp;<wbr>before_vm_destroy, after_vm_destroy,<br />
&nbsp;<wbr>before_vm_set_ticket, after_vm_set_ticket,<br />
&nbsp;<wbr>before_device_create, after_device_create,<br />
&nbsp;<wbr>before_device_destroy, after_device_destroy,<br />
&nbsp;<wbr>before_nic_hotplug, after_nic_hotplug, after_nic_hotplug_fail,<br />
&nbsp;<wbr>before_nic_hotunplug, after_nic_hotunplug, after_nic_hotunplug_fail,<br />
&nbsp;<wbr>before_update_device, after_update_device, after_update_device_fail,<br />
&nbsp;<wbr>before_disk_hotplug, after_disk_hotplug,<br />
&nbsp;<wbr>before_disk_hotunplug, after_disk_hotunplug,<br />
&nbsp;<wbr>before_vdsm_start, after_vdsm_stop,<br />
&nbsp;<wbr>before_network_setup, after_network_setup, after_network_setup_fail,<br />
&nbsp;<wbr>before_set_num_of_cpus, after_set_num_of_cpus,<br />
&nbsp;<wbr>before_get_vm_stats, after_get_vm_stats,<br />
&nbsp;<wbr>before_get_all_vm_stats, after_get_all_vm_stats,<br />
&nbsp;<wbr>before_get_caps, after_get_caps,<br />
&nbsp;<wbr>before_get_stats, after_get_stats,<br />
&nbsp;<wbr>after_hostdev_list_by_caps,<br />
&nbsp;<wbr>before_memory_hotplug, after_memory_hotplug,<br />
&nbsp;<wbr>before_ifcfg_write, after_ifcfg_write. </p>
<p> Each hook executes the scripts under <i>/usr/libexec/vdsm/hooks/&lt;hook-name&gt;/</i> in lexicographic order.</p>
<h3>Hook environment</h3>
<p>Each hook script (except before_vdsm_start, after_vdsm_stop, before_network_setup, after_network_setup and after_network_setup_fail, before_get_vm_stats, after_get_vm_stats, before_get_all_vm_stats, after_get_all_vm_stats, before_get_caps, after_get_caps, before_get_stats, after_get_stats, after_hostdev_list_by_caps, before_ifcfg_write and after_ifcfg_write) inherit the environment of the VDSM process, with an additional variable <code>_hook_domxml</code> which holds the path of libvirt&#8217;s <code>domain xml</code> representation of the relevant virtual machine. The uuid of the virtual machine may be deduced from that xml, but it is also available as the environment variable <code>vmId.</code> </p>
<p> The before_network_setup, after_network_setup, after_network_setup_fail, before_ifcfg_write and after_ifcfg_write hooks do also include an extra environment variable <code>_hook_json</code> which holds a pointer to a file with the network parameters that vdsm is setting up ( <code>request</code> ) , the request may be modified by the before_network_setup hook as thus affect the operation ultimately taken place by Vdsm. </p>
<p> The JSON format of this file for before_network_setup, after_network_setup and after_network_setup_fail has one section: request, this section contains networks, bondings and options, those parameters are specified in the setupNetworks VDSM API call. </p>
<pre>{&quot;request&quot;:
 {
 &quot;networks&quot;: {&quot;virtnet&quot;: {&quot;bonding&quot; : &quot;bond0&quot;, &quot;bridged&quot;: true, &quot;vlan&quot;:27}},
 &quot;bondings&quot;: {&quot;bond0&quot;: {&quot;nics&quot;:[&quot;eth1&quot;,&quot;eth2&quot;]}},
 &quot;options&quot;: {&quot;conectivityCheck&quot;:false}
 }
 }</pre>
<p>The JSON format of this file for before_ifcfg_write and after_ifcfg_write has the following parameters: ifcfg_file and config. </p>
<pre>{
 &quot;ifcfg_file&quot;: &quot;/etc/sysconfig/network-scripts/ifcfg-eth0&quot;,
 &quot;config&quot;: &quot;IPADDR=192.168.1.2ETMASK=255.255.255.0&quot;
 }</pre>
<p>Hooks that handle NIC hotplug, hotunplug and update device have the _hook_domxml variable but it contains the representation of the NIC rather than the VM. Hotplug/hotunplug disk hooks also have the _hook_dom_xml variable, which contains the drive definition (not the VM). All hook points that are device specific get the xml of the device instead of the entire VM. Such hooks are listed below. </p>
<p> On top of these, @ENGINENAME@ allows to set a collection of &quot;custom parameters&quot; for each virtual machine. Each of these parameters is provided to hooks as an environment variable. </p>
<p> before_migration_destination (and before_dehibernation) hooks currently receive the xml of the domain from the source host. The xml of the domain at the destination will differ in various details. </p>
<p> The environment of before_vm_set_ticket and after_vm_set_ticket hooks is augmented with a set of params passed by the caller of setVmTicket. </p>
<p> The environment of before_vm_dehibernate and after_vm_dehibernate hooks have FROM_SNAPSHOT variable set to True if the VM is being restored from a live snapshot. </p>
<p> The environment of hooks specific to devices:<br />
&nbsp;<wbr>before_nic_hotplug, after_nic_hotplug, after_nic_hotplug_fail,<br />
&nbsp;<wbr>before_nic_hotunplug, after_nic_hotunplug, after_nic_hotunplug_fail,<br />
&nbsp;<wbr>before_update_device, after_update_device, after_update_device_fail,<br />
&nbsp;<wbr>before_disk_hotplug, after_disk_hotplug,<br />
&nbsp;<wbr>before_disk_hotunplug, after_disk_hotunplug,<br />
&nbsp;<wbr>before_device_create, after_device_create,<br />
&nbsp;<wbr>before_device_destroy, after_device_destroy,<br />
&nbsp;<wbr>before_device_migrate_source, after_device_migrate_source,<br />
&nbsp;<wbr>before_device_migrate_destination, after_device_migrate_destination,<br />
&nbsp;<wbr>before_memory_hotplug, after_memory_hotplug. </p>
<p> Are all augmented by custom properties specific to those devices, sent by the caller of the hook. For example if before_nic_hotplug is called with custom: {qos: &#8216;0.5&#8217;, color: &#8216;red&#8217;} then qos and color will be directly available as environment variables when before_nic_hotplug is called. </p>
<p> before_get_vm_stats and before_get_all_vm_stats are called upon API request to get VM statistics, before getVmStats and getAllVmStats respectively. Those hooks do not receive any parameters. </p>
<p> after_get_vm_stats and after_get_all_vm_stats are called upon getVmStats and getAllVmStats respectively. Both receive a parameter in _hook_json containing a list of dictionaries of VM stats (in case of after_get_vm_stats the list will have a single element): </p>
<pre>[
 {&quot;vm_id&quot;: &quot;...&quot;, ... },
 {&quot;vm_id&quot;: &quot;...&quot;, ... },
 ...
]</pre>
<p>before_get_caps and after_get_caps are called before (and after) a getVdsCapabilities API request. after_get_caps receives the complete capabilities dictionary within _hook_json. </p>
<p> before_get_stats and after_get_stats are called before (and after) a getVdsStats API request. after_get_stats receives the complete host statistics dictionary within _hook_json.</p>
<h3>Hook execution</h3>
<p>before_vdsm_start and after_vdsm_stop scripts are executed as user <i>root.</i> All the other hooks are executed as user <i>vdsm.</i> </p>
<p> <code>before_vm_start</code> scripts may edit the domain xml file (pointed by <code>_hook_domxml</code> ) in order to change VDSM&#8217;s definition of a virtual machine before it reaches libvirt. As with all hooks, the China Store Rule applies &#8211; if you break something, you own it. Any script can mess up VDSM&#8217;s operation badly. In particular, you may never change the uuid of the domain, and should better know what you are doing if you remove a device from the domain. </p>
<p> before_vm_start and before_device_create may alter the vm start behavior by modifying the vm libvirt vm startup flags. The flag must be written to the /var/run/vdsm/hook/&lt;vm id&gt;/launchflags file, the required value being a decimal based on the libvirt virDomainCreateFlags enum values. </p>
<p> Standard error of hook scripts is collected into VDSM&#8217;s log, which may be used by scripts for debugging. </p>
<p> As a somewhat silly example, let us think of a script that warns when a domain with too much memory is started on a host: </p>
<pre> #!/bin/bash
 mem=`/usr/bin/xpath $_hook_domxml '/domain/memory/text()' 2&gt; /dev/null`
 if [ &quot;$mem&quot; -gt 1073741824 ]; then
 echo &quot;Domain with more than Gb!&quot; &gt;&amp;2
 fi
 exit 0</pre>
<h3>Hook return code</h3>
<p>Hook script must return one of the following return codes: </p>
<dl>
<dt><code>0</code></p>
<dd>the hook script ended successfully.</p>
<dt><code>1</code></p>
<dd>the hook script failed, other hooks should be processed.</p>
<dt><code>2</code></p>
<dd>the hook script failed, no further hooks should be processed.</p>
<dt><code>&gt;2</code></p>
<dd>reserved. </p>
<dt>If a before_&lt;action&gt; hook fails, the &lt;action&gt; would be aborted.</p>
<dd>However, before_vm_destroy&#8217;s failure does not abort destroy(). </p>
</dl>
<h2>Files</h2>
<dl>
<dt> <i>/etc/vdsm/vdsm.conf</i></p>
<dd>VDSM main configuration file. Use with great caution; some information about available variables and their meaning appear in <i>/usr/share/doc/vdsm-&lt;version&gt;/vdsm.conf.sample</i></p>
<dt> <i>/var/log/vdsm/vdsm.log</i></p>
<dd>Default log location for vdsm.</p>
<dt> <i>/usr/share/doc/vdsm-&lt;version&gt;/vdsm-api.html</i></p>
<dd>vdsm QAPI documentation.</p>
<dt> <i>/etc/pki/vdsm</i></p>
<dd>VDSM&#8217;s trust store: server key, certificate, and @ENGINENAME@ CA&#8217;s certificate.</p>
<dt> <i>/rhev/data-center</i></p>
<dd>VDSM&#8217;s image repository, or more exactly, links to NFS exports and iSCSI or FiberChannel devices which VDSM uses. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vdsclient/">vdsClient</a>(1)</code><br />
 <code><a rel="nofollow" href="http://www.ovirt.org/wiki/Category:Vdsm">http://www.ovirt.org/wiki/Category:Vdsm</a></code> </p>
<h2>Author</h2>
<p>VDSM was written by Ayal Baron, Barak Azulay, Cyril Plisko, Dan Kenigsberg, Doron Fediuck, Igor Lvovsky, Saggi Mizrahi, Shahar Frank, Simon Grinberg, and probably others.</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt; </p>
<h2>Copyright</h2>
<p>Copyright 2010-2013 Red Hat, Inc. License GPLv2: GNU GPL Version 2 &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.</p>
