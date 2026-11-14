---
title: "sge_st(8)"
name: "sge_st"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sge_st/"
description: "util/sgeST/sge_st – Grid Engine Service Tags Support control command"
---

<p>util/sgeST/sge_st &#8211; Grid Engine Service Tags Support control command</p>
<h2>Synopsis</h2>
<p><code>sge_st</code> <code>enable |</code> <code>disable |</code> <code>register |</code> <code>unregister |</code> <code>check |</code> <code>enabled |</code> <code>supported |</code> <code>help</code></p>
<h2>Description</h2>
<p><i>sge_st </i> controls the Grid Engine support for Service Tags. A Service Tag support improve the monitoring of usages of the Grid Engine.</p>
<h2>Options</h2>
<dl>
<dt><code>enable</code></p>
<dd>Enables the Service Tags support for Grid Engine. If the Service Tags packages are installed on the host, the presence of the product instance service tag is checked in every start of the qmaster daemon. </p>
<dt><code>disable</code></p>
<dd>Disables the Service Tags support for Grid Engine. </p>
<dt><code>register</code></p>
<dd>Create the product instance service tag. </p>
<dt><code>unregister</code></p>
<dd>Remove the product instance service tag. </p>
<dt><code>check</code></p>
<dd>Checks the status of the product instance service tag. If not registered, the option returns &quot;unregistered&quot;. If registered, the option returns &quot;registered:&lt;product_instance_urn&gt;&quot; </p>
<dt><code>enabled</code></p>
<dd>Check the status of the service tags support. If the service tags are enabled by Grid Engine administrator, the option returns &quot;true&quot;, otherwise &quot;false&quot;. </p>
<dt><code>supported</code></p>
<dd>Checks if the Service Tags are supported on this host. This option validates the presence of the Service Tags packages on the host and checks if they are correctly installed. If Service Tags are supported on this host, the option return a word &quot;true&quot;, otherwise &quot;false&quot;. </p>
</dl>
<h2>The Service Tags Support</h2>
<p>Service Tags enables automatic discovery of systems, software and services. A service tag uniquely identifies each tagged asset, and allows the asset information to be shared over a local network in a standard XML format. </p>
<p> The Grid Engine can create a service tag for one cluster installation. A service tag entry is stored in the Service Tag registry. Each service tag has an unique instance identifier which is generated when the record is added to the registry. This identifier is used as the key when accessing the record. </p>
<p> The discoverer and listener services installed together with Service Tags on a host. They provide a way to discover a service tags via the network. The discoverer is a UDP-based application which exists to provide information about the listener. The listener is a TCP-based application which provides a way to gather service tag and associated environmental information. </p>
<p> The discoverer service is used by operating system upgrade or register tools to send the service tags data to SUN. There is no other way, how to propagate the collected data to SUN than through the registration tool. The data to be send can be inspected and accepted. The Service Tags Data is going to be analyzed.</p>
<h2>Environmental Variables</h2>
<dl>
<dt><code>GE_ROOT</code></p>
<dd>Specifies the location of the Grid Engine standard configuration files.</p>
<dt><code>GE_CELL</code></p>
<dd>If set, specifies the default Grid Engine cell. To address a Grid Engine cell</dl>
<h2>Restrictions</h2>
<p><i>sge_st</i> The command must be called with Grid Engine admin rights or root permissions.</p>
<h2>Files</h2>
<p><code>sge_st creates a st.enabled file in GE_CELL
