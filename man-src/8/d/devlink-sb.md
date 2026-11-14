---
title: "devlink-sb(8)"
name: "devlink-sb"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-sb/"
description: "devlink-sb – devlink shared buffer configuration"
---

<p>devlink-sb &#8211; devlink shared buffer configuration</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

sb

{ COMMAND |

    help }

OPTIONS := {

    -V[ersion] |
    -n[no-nice-names] }</code></pre>
<p> <code>devlink sb show </code> [ <i>DEV</i> [ <code>sb</code> <i>SB_INDEX</i> ] ]<br />
 <code>devlink sb pool show </code> [ <i>DEV</i> [ <code>sb</code> <i>SB_INDEX</i> ]<br />
 <code>pool</code> <i>POOL_INDEX</i> ] </p>
<pre><code>devlink sb pool set DEV

[ sb

SB_INDEX ]


pool POOL_INDEX


size POOL_SIZE


thtype { static | dynamic }</code></pre>
<p> <code>devlink sb port pool show </code> [ <i>DEV/PORT_INDEX</i> [ <code>sb</code> <i>SB_INDEX</i> ]<br />
 <code>pool</code> <i>POOL_INDEX</i> ]<br />
 <code>devlink sb port pool set </code><i>DEV/PORT_INDEX</i> [ <code>sb</code> <i>SB_INDEX</i> ]<br />
 <code>pool</code><i> POOL_INDEX </i><br />
 <code>th</code><i> THRESHOLD </i><br />
 <code>devlink sb tc bind show </code> [ <i>DEV/PORT_INDEX</i> [ <code>sb</code> <i>SB_INDEX</i> ]<br />
 <code>tc</code><i> TC_INDEX </i><br />
 <code>type</code> { <code>ingress</code> | <code>egress</code> } ]<br />
 <code>devlink sb tc bind set </code><i>DEV/PORT_INDEX</i> [ <code>sb</code> <i>SB_INDEX</i> ]<br />
 <code>tc</code><i> TC_INDEX </i><br />
 <code>type</code> { <code>ingress</code> | <code>egress</code> }<br />
 <code>pool</code><i> POOL_INDEX </i><br />
 <code>th</code><i> THRESHOLD </i><br />
 <code>devlink sb occupancy show </code> { <i>DEV</i> | <i>DEV/PORT_INDEX</i> } [ <code>sb</code> <i>SB_INDEX</i> ]<br />
 <code>devlink sb occupancy snapshot </code> <i>DEV</i> [ <code>sb</code> <i>SB_INDEX</i> ]<br />
 <code>devlink sb occupancy clearmax </code> <i>DEV</i> [ <code>sb</code> <i>SB_INDEX</i> ]<br />
 <code>devlink sb help</code> </p>
<h2>Description</h2>
<h3>devlink sb show &#8211; display available shared buffers and their attributes</h3>
<p><i>DEV</i> &#8211; specifies the devlink device to show shared buffers. If this argument is omitted all shared buffers of all devices are listed. <i>SB_INDEX</i> &#8211; specifies the shared buffer. If this argument is omitted shared buffer with index 0 is selected. Behaviour of this argument it the same for every command.</p>
<h3>devlink sb pool show &#8211; display available pools and their attributes</h3>
<p><i>DEV</i> &#8211; specifies the devlink device to show pools. If this argument is omitted all pools of all devices are listed. Display available pools listing their <code>type, size, thtype</code> and <code>cell_size. cell_size</code> is the allocation granularity of memory within the shared buffer. Drivers may round up, round down or reject <code>size</code> passed to the set command if it is not multiple of <code>cell_size.</code></p>
<h3>devlink sb pool set &#8211; set attributes of pool</h3>
<p><i>DEV</i> &#8211; specifies the devlink device to set pool.</p>
<dl>
<dt><code>size</code><i> POOL_SIZE</i></p>
<dd>size of the pool in Bytes.</p>
<dt><code>thtype</code> { <code>static</code> | <code>dynamic</code> }</p>
<dd>pool threshold type. <i>static</i> &#8211; Threshold values for the pool will be passed in Bytes. <i>dynamic</i> &#8211; Threshold values (&quot;to_alpha&quot;) for the pool will be used to compute alpha parameter according to formula:<br />
 alpha = 2 ^ (to_alpha &#8211; 10) The range of the passed value is between 0 to 20. The computed alpha is used to determine the maximum usage of the flow:<br />
 max_usage = alpha / (1 + alpha) * Free_Buffer</dl>
<h3>devlink sb port pool show &#8211; display port-pool combinations and threshold for each</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port.</p>
<dl>
<dt><code>pool</code><i> POOL_INDEX</i></p>
<dd>pool index.</dl>
<h3>devlink sb port pool set &#8211; set port-pool threshold</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port.</p>
<dl>
<dt><code>pool</code><i> POOL_INDEX</i></p>
<dd>pool index.</p>
<dt><code>th</code><i> THRESHOLD</i></p>
<dd>threshold value. Type of the value is either Bytes or &quot;to_alpha&quot;, depends on <code>thtype</code> set for the pool.</dl>
<h3>devlink sb tc bind show &#8211; display port-TC to pool bindings and threshold for each</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port.</p>
<dl>
<dt><code>tc</code><i> TC_INDEX</i></p>
<dd>index of either ingress or egress TC, usually in range 0 to 8 (depends on device).</p>
<dt><code>type</code> { <code>ingress</code> | <code>egress</code> }</p>
<dd>TC type.</dl>
<h3>devlink sb tc bind set &#8211; set port-TC to pool binding with specified threshold</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port.</p>
<dl>
<dt><code>tc</code><i> TC_INDEX</i></p>
<dd>index of either ingress or egress TC, usually in range 0 to 8 (depends on device).</p>
<dt><code>type</code> { <code>ingress</code> | <code>egress</code> }</p>
<dd>TC type.</p>
<dt><code>pool</code><i> POOL_INDEX</i></p>
<dd>index of pool to bind this to.</p>
<dt><code>th</code><i> THRESHOLD</i></p>
<dd>threshold value. Type of the value is either Bytes or &quot;to_alpha&quot;, depends on <code>thtype</code> set for the pool.</dl>
<h3>devlink sb occupancy show &#8211; display shared buffer occupancy values for device or port</h3>
<p>This command is used to browse shared buffer occupancy values. Values are showed for every port-pool combination as well as for all port-TC combinations (with pool this port-TC is bound to). Format of value is:<br />
 current_value/max_value Note that before showing values, one has to issue <code>occupancy snapshot</code> command first. <i>DEV</i> &#8211; specifies the devlink device to show occupancy values for. <i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port to show occupancy values for.</p>
<h3>devlink sb occupancy snapshot &#8211; take occupancy snapshot of shared buffer for device</h3>
<p>This command is used to take a snapshot of shared buffer occupancy values. After that, the values can be showed using <code>occupancy show</code> command. <i>DEV</i> &#8211; specifies the devlink device to take occupancy snapshot on.</p>
<h3>devlink sb occupancy clearmax &#8211; clear occupancy watermarks of shared buffer for device</h3>
<p>This command is used to reset maximal occupancy values reached for whole device. Note that before browsing reset values, one has to issue <code>occupancy snapshot</code> command. <i>DEV</i> &#8211; specifies the devlink device to clear occupancy watermarks on. </p>
<h2>Examples</h2>
<p>devlink sb show</p>
<dl>
<dd>List available share buffers.</dl>
<p> devlink sb pool show</p>
<dl>
<dd>List available pools and their config.</dl>
<p> devlink sb port pool show pci/0000:03:00.0/1 pool 0</p>
<dl>
<dd>Show port-pool setup for specified port and pool.</dl>
<p> sudo devlink sb port pool set pci/0000:03:00.0/1 pool 0 th 15</p>
<dl>
<dd>Change threshold for port specified port and pool.</dl>
<p> devlink sb tc bind show pci/0000:03:00.0/1 tc 0 type ingress</p>
<dl>
<dd>Show pool binding and threshold for specified port and TC.</dl>
<p> sudo devlink sb tc bind set pci/0000:03:00.0/1 tc 0 type ingress pool 0 th 9</p>
<dl>
<dd>Set pool binding and threshold for specified port and TC.</dl>
<p> sudo devlink sb occupancy snapshot pci/0000:03:00.0</p>
<dl>
<dd>Make a snapshot of occupancy of shared buffer for specified devlink device.</dl>
<p> devlink sb occupancy show pci/0000:03:00.0/1</p>
<dl>
<dd>Show occupancy for specified port from the snapshot.</dl>
<p> sudo devlink sb occupancy clearmax pci/0000:03:00.0</p>
<dl>
<dd>Clear watermarks for shared buffer of specified devlink device.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-dev/">devlink-dev</a></code>(8), <code><a href="/docs/linux/man/8-devlink-port/">devlink-port</a></code>(8), <code><a href="/docs/linux/man/8-devlink-monitor/">devlink-monitor</a></code>(8), </p>
<h2>Author</h2>
<p>Jiri Pirko &lt;jiri [at] mellanox.com&gt;</p>
