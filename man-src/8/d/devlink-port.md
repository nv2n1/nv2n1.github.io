---
title: "devlink-port(8)"
name: "devlink-port"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-port/"
description: "devlink-port – devlink port configuration"
---

<p>devlink-port &#8211; devlink port configuration</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

port

{ COMMAND |

    help }

OPTIONS := {

    -V[ersion] |
    -n[no-nice-names] }</code></pre>
<p> <code>devlink port set </code> <i>DEV/PORT_INDEX</i> [ <code>type</code> { <code>eth</code> | <code>ib</code> | <code>auto</code> } ]<br />
 <code>devlink port split </code> <i>DEV/PORT_INDEX</i> <code>count</code> <i>COUNT</i><br />
 <code>devlink port unsplit </code> <i>DEV/PORT_INDEX</i><br />
 <code>devlink port show</code> [ <i>DEV/PORT_INDEX</i> ] devlink port health</p>
<p>{ show | recover | diagnose | dump | set }<br />
 <code>devlink port add</code> { <i>DEV | DEV/PORT_INDEX</i> } [ <code>flavour</code> <i>FLAVOUR</i> ] [ <code>pfnum</code> <i>PFNUMBER</i> ] [ <code>sfnum</code> <i>SFNUMBER</i> ] [ <code>controller</code> <i>CNUM</i> ] </p>
<p> <code>devlink port del</code> <i>DEV/PORT_INDEX</i><br />
 <code>devlink port function set </code> <i>DEV/PORT_INDEX</i> [ <code>hw_addr </code> ADDR ] [ <code>state</code> { <code>active</code> | <code>inactive</code> } ] </p>
<pre><code>devlink port function rate

{ show | set | add | del | help }
devlink dev param set

DEV/PORT_INDEX

name

PARAMETER

value

VALUE

cmode { runtime | driverinit | permanent }</code></pre>
<p> <code>devlink dev param show</code> [ <i>DEV/PORT_INDEX</i> <code>name</code> <i>PARAMETER</i> ]<br />
 <code>devlink port help</code> </p>
<h2>Description</h2>
<h3>devlink port set &#8211; change devlink port attributes</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port to operate on. Format is: BUS_NAME/BUS_ADDRESS/PORT_INDEX</p>
<dl>
<dt><code>type</code> { <code>eth</code> | <code>ib</code> | <code>auto</code> }</p>
<dd>set port type <i>eth</i> &#8211; Ethernet <i>ib</i> &#8211; Infiniband <i>auto</i> &#8211; autoselect</dl>
<h3>devlink port split &#8211; split devlink port into more</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port to operate on.</p>
<dl>
<dt><code>count</code><i> COUNT</i></p>
<dd>number of ports to split to.</dl>
<h3>devlink port unsplit &#8211; unsplit previously split devlink port</h3>
<p>Could be performed on any split port of the same split group. <i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port to operate on.</p>
<h3>devlink port show &#8211; display devlink port attributes</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port to show. If this argument is omitted all ports are listed.</p>
<h3>devlink port health &#8211; devlink health reporting and recovery</h3>
<p>Is an alias for <code><a href="/docs/linux/man/8-devlink-health/">devlink-health</a></code>(8).</p>
<h3>devlink port add &#8211; add a devlink port</h3>
<p><i>DEV</i> &#8211; specifies the devlink device to operate on. or <i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port index to use for the requested new port. This is optional. When omitted, driver allocates unique port index.</p>
<dl>
<dt><code>flavour</code> { <code>pcipf</code> | <code>pcisf</code> }</p>
<dd>set port flavour <i>pcipf</i> &#8211; PCI PF port <i>pcisf</i> &#8211; PCI SF port</p>
<dt><code>pfnum</code><i> PFNUMBER </i></p>
<dd>Specifies PCI pfnumber to use on which a SF device to create</p>
<dt><code>sfnum</code><i> SFNUMBER </i></p>
<dd>Specifies sfnumber to assign to the device of the SF. This field is optional for those devices which supports auto assignment of the SF number.</p>
<dt><code>controller</code><i> CNUM </i></p>
<dd>Specifies controller number for which the SF port is created. This field is optional. It is used only when SF port is created for the external controller.
</dl>
<h3>devlink port function set &#8211; Set the port function attribute(s).</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port to operate on.</p>
<dl>
<dt><code>hw_addr</code><i> ADDR</i></p>
<dd>Hardware address of the function to set. This is a Ethernet MAC address when port type is Ethernet.</p>
<dt><code>state</code> { <code>active</code> | <code>inactive</code> }</p>
<dd>New state of the function to change to. <i>active</i> &#8211; Once configuration of the function is done, activate the function. <i>inactive</i> &#8211; To inactivate the function and its device(s), set to inactive.
</dl>
<h3>devlink port del &#8211; delete a devlink port</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port to delete.</p>
<h3>devlink port param set &#8211; set new value to devlink port configuration parameter</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port to operate on.</p>
<dl>
<dt><code>name</code><i> PARAMETER</i></p>
<dd>Specify parameter name to set.</p>
<dt><code>value</code><i> VALUE</i></p>
<dd>New value to set.</p>
<dt><code>cmode</code> { <code>runtime</code> | <code>driverinit</code> | <code>permanent</code> }</p>
<dd>Configuration mode in which the new value is set. <i>runtime</i> &#8211; Set new value while driver is running. This configuration mode doesn&#8217;t require any reset to apply the new value. <i>driverinit</i> &#8211; Set new value which will be applied during driver initialization. This configuration mode requires restart driver by devlink reload command to apply the new value. <i>permanent</i> &#8211; New value is written to device&#8217;s non-volatile memory. This configuration mode requires hard reset to apply the new value.</dl>
<h3>devlink port param show &#8211; display devlink port supported configuration parameters attributes</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port to operate on. <code>name</code> <i>PARAMETER</i> Specify parameter name to show. If this argument, as well as port index, are omitted &#8211; all parameters supported by devlink device ports are listed.</p>
<h3>devlink port function rate &#8211; manage devlink rate objects</h3>
<p>Is an alias for <code><a href="/docs/linux/man/8-devlink-rate/">devlink-rate</a></code>(8). </p>
<h2>Examples</h2>
<p>devlink port show</p>
<dl>
<dd>Shows the state of all devlink ports on the system.</dl>
<p> devlink port show pci/0000:01:00.0/1</p>
<dl>
<dd>Shows the state of specified devlink port.</dl>
<p> devlink port set pci/0000:01:00.0/1 type eth</p>
<dl>
<dd>Set type of specified devlink port to Ethernet.</dl>
<p> devlink port split pci/0000:01:00.0/1 count 4</p>
<dl>
<dd>Split the specified devlink port into four ports.</dl>
<p> devlink port unsplit pci/0000:01:00.0/1</p>
<dl>
<dd>Unplit the specified previously split devlink port.</dl>
<p> devlink port health show</p>
<dl>
<dd>Shows status and configuration of all supported reporters registered on all devlink ports.</dl>
<p> devlink port health show pci/0000:01:00.0/1 reporter tx</p>
<dl>
<dd>Shows status and configuration of tx reporter registered on pci/0000:01:00.0/1 devlink port.</dl>
<p> devlink port add pci/0000:06:00.0 flavour pcisf pfnum 0 sfnum 88</p>
<dl>
<dd>Add a devlink port of flavour PCI SF on PCI PF having number 0 with SF number 88. To make use of the function an example sequence is to add a port, configure the function attribute and activate the function. Once function usage is completed, inactivate the function and finally delete the port. When there is desire to reuse the port without deletion, it can be reconfigured and activated again when function is in inactive state and function&#8217;s operational state is detached.</dl>
<p> devlink port del pci/0000:06:00.0/1</p>
<dl>
<dd>Delete previously created devlink port. It is recommended to first deactivate the function if the function supports state management.</dl>
<p> devlink port function set pci/0000:01:00.0/1 hw_addr 00:00:00:11:22:33</p>
<dl>
<dd>Configure hardware address of the PCI function represented by devlink port. If the port supports change in function state, hardware address must be configured before activating the function.</dl>
<p> devlink port function set pci/0000:01:00.0/1 state active</p>
<dl>
<dd>Activate the function. This will initiate the function enumeration and driver loading.</dl>
<p> devlink port function set pci/0000:01:00.0/1 state inactive</p>
<dl>
<dd>Deactivate the function. This will initiate the function teardown which results in driver unload and device removal.</dl>
<p> devlink port function set pci/0000:01:00.0/1 hw_addr 00:00:00:11:22:33 state active</p>
<dl>
<dd>Configure hardware address and also active the function. When a function is activated together with other configuration in a single command, all the configuration is applied first before changing the state to active.</dl>
<p> devlink dev param show</p>
<dl>
<dd>Shows (dumps) all the port parameters across all the devices registered in the devlink.</dl>
<p> devlink dev param set pci/0000:01:00.0/1 name internal_error_reset value true cmode runtime</p>
<dl>
<dd>Sets the parameter internal_error_reset of specified devlink port (#1) to true.</dl>
<p> devlink port add pci/0000:06:00.0 flavour pcisf pfnum 0 sfnum 88 controller 1</p>
<dl>
<dd>Add a devlink port of flavour PCI SF on controller 1 which has PCI PF of number 0 with SF number 88. To make use of the function an example sequence is to add a port, configure the function attribute and activate the function. Once the function usage is completed, deactivate the function and finally delete the port. When there is desire to reuse the port without deletion, it can be reconfigured and activated again when function is in inactive state and function&#8217;s operational state is detached.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-dev/">devlink-dev</a></code>(8), <code><a href="/docs/linux/man/8-devlink-sb/">devlink-sb</a></code>(8), <code><a href="/docs/linux/man/8-devlink-monitor/">devlink-monitor</a></code>(8), <code><a href="/docs/linux/man/8-devlink-health/">devlink-health</a></code>(8), </p>
<h2>Author</h2>
<p>Jiri Pirko &lt;jiri [at] mellanox.com&gt;</p>
