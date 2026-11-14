---
title: "hosted-engine(8)"
name: "hosted-engine"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hosted-engine/"
description: "hosted-engine – Tools for handling hosted engine"
---

<p>hosted-engine &#8211; Tools for handling hosted engine</p>
<h2>Synopsis</h2>
<p><code>hosted-engine</code> [&#8211;help] &lt;command&gt; [&lt;command-args&gt;] </p>
<h2>Description</h2>
<p>The <code>hosted-engine</code> command deploys a virtual machine that you can install oVirt Open Virtualization Manager on to. The Manager installation on your hosted-engine virtual machine can manage the host it is running on. The hosted-engine command can also be used to start, stop and access the hosted-engine virtual machine. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Show the help message and exit. </p>
<dt>The following commands are available:</p>
<dd>
<dt><code>&#8211;deploy [options]</code></p>
<dd>Run the ovirt-hosted-engine-setup command to deploy the hosted-engine virtual machine.</p>
<dt><code>&#8211;vm-start [&#8211;vm-conf=&lt;file&gt;]</code></p>
<dd>Start VM on this host. &#8211;vm-conf=&lt;file&gt; can be optionally used to load an alternative vm.conf file as a recovery action.</p>
<dt><code>&#8211;vm-start-paused</code></p>
<dd>Start VM on this host with qemu paused.</p>
<dt><code>&#8211;vm-shutdown</code></p>
<dd>Gracefully shutdown the VM on this host.</p>
<dt><code>&#8211;vm-poweroff</code></p>
<dd>Forcefully poweroff the VM on this host.</p>
<dt><code>&#8211;vm-status [&#8211;json]</code></p>
<dd>Show the VM status, in machine-readable format if &#8211;json is given.</p>
<dt><code>&#8211;add-console-password [&#8211;password=&lt;password&gt;]</code></p>
<dd>Create a temporary password for VNC/SPICE connections to the hosted-engine virtual machine.</p>
<dt><code>&#8211;console</code></p>
<dd>Open the configured console using virsh on localhost.</p>
<dt><code>&#8211;check-deployed</code></p>
<dd>Checks whether the hosted engine has been deployed.</p>
<dt><code>&#8211;check-liveliness</code></p>
<dd>Checks liveliness page of engine.</p>
<dt><code>&#8211;connect-storage</code></p>
<dd>Manually connect the storage domain to the local VDSM instance.</p>
<dt><code>&#8211;set-maintenance &#8211;mode=&lt;mode&gt;</code></p>
<dd>Set maintenance status to the specified mode:</p>
<dl>
<dd><code>global</code> &#8211; Allow the administrator to start/stop/modify the engine VM without any worry of interference from the HA agents.</dl>
<dl>
<dd><code>local</code> &#8211; Allow the administrator to maintain this host. Note that if you have only 2 nodes and one is in maintenance, there is only one host available to run the engine VM.</dl>
<dl>
<dd><code>none</code> &#8211; Resume HA functionality.</dl>
<dt><code>&#8211;clean_metadata [&#8211;force-cleanup] [&#8211;host-id=&lt;id&gt;]</code></p>
<dd>Remove host&#8217;s metadata from the global status database.</p>
<dt><code>&#8211;reinitialize-lockspace [&#8211;force]</code></p>
<dd>Reinitialize the sanlock lockspace file. This WIPES all locks.</p>
<dt><code>&#8211;upgrade-appliance</code></p>
<dd>Upgrade the engine appliance.</p>
<dt><code>&#8211;rollback-upgrade</code></p>
<dd>Rollback using a backup saved in a previous upgrade attempt. </p>
<dt>For additional information about a specific command try:</p>
<dd>hosted-engine &lt;command&gt; &#8211;help </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ovirt-hosted-engine-setup/">ovirt-hosted-engine-setup</a></code>(8) </p>
