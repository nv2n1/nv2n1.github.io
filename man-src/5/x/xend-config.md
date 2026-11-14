---
title: "xend-config(5)"
name: "xend-config"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xend-config/"
description: "xend-config.sxp – Xen daemon configuration file"
---

<p>xend-config.sxp &#8211; Xen daemon configuration file</p>
<h2>Synopsis</h2>
<p>/etc/xen/xend-config.sxp</p>
<h2>Description</h2>
<p>The <i><a href="/docs/linux/man/1-xend/">xend</a></i>(1) program requires xend-config.sxp to specify operating parameters which determine the behavior of the daemon at runtime. </p>
<p> The parameters are specified in S-expression format. See the example configuration file in <i>/etc/xen/xend-config.sxp</i> for details.</p>
<h2>Options</h2>
<p>The following lists the daemon configuration parameters:</p>
<dl>
<dt><i>logfile</i></p>
<dd>The location of the file to record runtime log messages. Defaults to <i>/var/log/xen/xend.log</i>.</p>
<dt><i>loglevel</i></p>
<dd>Filters out messages below the specified level. Possible values are <font SIZE="-1">DEBUG</font>, <font SIZE="-1">INFO</font>, <font SIZE="-1">WARNING</font>, <font SIZE="-1">ERROR</font>, <font SIZE="-1">CRITICAL</font>. Defaults to <i></i><font SIZE="-1"><i>DEBUG</i></font><i></i>.</p>
<dt><i>xend-http-server</i></p>
<dd>A boolean value that tells xend whether or not to start the http stream socket management server. Defaults to <i>no</i>.</p>
<dt><i>xend-unix-server</i></p>
<dd>A boolean value that tells xend whether or not to start the unix domain socket management server. This is required for the <font SIZE="-1">CLI</font> tools to operate. Defaults to <i>yes</i>.</p>
<dt><i>xend-relocation-server</i></p>
<dd>A boolean value that tells xend whether or not to start the relocation server. This is required for cross-machine migrations. Defaults to <i>no</i>.</p>
<dt><i>xend-unix-path</i></p>
<dd>The location of the unix domain socket the xend-unix-server will use to communicate with the management tools. Defaults to <i>/var/lib/xend/xend-socket</i>.</p>
<dt><i>xend-port</i></p>
<dd>The port that will be used by the http management server. Defaults to <i>8000</i>.</p>
<dt><i>xend-relocation-port</i></p>
<dd>The port that will be used by the relocation server. Defaults to <i>8002</i>.</p>
<dt><i>xend-address</i></p>
<dd>The address to which the http management server will bind. Defaults to <i>&#8221;</i> which means &#8220;all interfaces&#8221;.</p>
<dt><i>xend-relocation-address</i></p>
<dd>The address to which the relocation server will bind. Defaults to <i>&#8221;</i> which means &#8220;all interfaces&#8221;.</p>
<dt><i>console-limit</i></p>
<dd>The kilobyte buffer limit that will be enforced by the console server. This limit is set per-domain, and is needed to prevent a single domain from overwhelming the console server with massive amounts of data. Defaults to <i>1024</i>.</p>
<dt><i>network-script</i></p>
<dd>The name of the script in <i>/etc/xen/scripts</i> that will be run to setup the networking environment. This can be any name, but in general is either <i>network-bridge</i> or <i>network-route</i>.</p>
<dt><i>vif-script</i></p>
<dd>The name of the script in <i>/etc/xen/scripts</i> that will be run to setup a virtual interface when it is created or destroyed. This needs to (in general) work in unison with the <i>network-script</i>.</p>
<dt><i>dom0-min-mem</i></p>
<dd>This specifies the minimum number of megabytes that will be reserved for Domain0. If this value is positive, Domain0 will be automatically ballooned down to this limit to make space for new domains. If this is set to 0, Domain0 will not be automatically ballooned.</p>
<dt><i>dom0-cpus</i></p>
<dd>This specifies the number of CPUs that Domain0 will be allowed to use. If the value is 0, all available CPUs will be used by Domain0.</p>
<dt><i>enable-dump</i></p>
<dd>A boolean value that tells xend whether or not core dumps of guest domains should be saved when a crash occurs. Defaults to <i>no</i>.</p>
<dt><i>external-migration-tool</i></p>
<dd>The name of an application or script that can handle external device migration, such as for example virtual <font SIZE="-1">TPM</font> migration. An example script is <i>/etc/xen/scripts/external-device-migrate</i>.</p>
<dt><i>device-create-timeout</i></p>
<dd>Integer value that tells xend how long it should wait for a new device to be created. Defaults to <i>100</i>.</p>
<dt><i>device-destroy-timeout</i></p>
<dd>Integer value that tells xend how long it should wait for a device to be destroyed. Defaults to <i>100</i>.</dl>
<h2>Examples</h2>
<p>An example configuration with relocation enabled for the local network: </p>
<pre> (xend-relocation-server yes)
 (xend-relocation-address 192.0.2.192)
 (network-script network-bridge)
 (vif-script vif-bridge)
 (dom0-min-mem 0)
 (dom0-cpus 0)</pre>
<h2>Caveats</h2>
<p>Note that relocation is currently unsecured and is very dangerous if left enabled. No authentication is performed, and very little sanity checking takes place. Enable at your own risk.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xend/">xend</a></code>(1)</p>
<h2>Author</h2>
<p>Dan Smith &lt;danms [at] us.ibm.com&gt;</p>
