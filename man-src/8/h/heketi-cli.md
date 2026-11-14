---
title: "heketi-cli(8)"
name: "heketi-cli"
section: "8"
letter: "h"
url: "/docs/linux/man/8-heketi-cli/"
description: "heketi-cli – Command line program for Heketi"
---

<p>heketi-cli &#8211; Command line program for Heketi</p>
<h2>Synopsis</h2>
<p><code>heketi-cli</code> [commands] [options]</p>
<h2>Description</h2>
<p>Command line program for Heketi</p>
<h2>Commands</h2>
<h3>Cluster Commands</h3>
<dl>
<dd><code>heketi-cli cluster create</code> Create a cluster<br />
&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli cluster create</dl>
<dl>
<dd><code>heketi-cli cluster delete &lt;CLUSTER-ID&gt;</code> Delete a cluster<br />
&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli cluster delete 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli cluster info &lt;CLUSTER-ID&gt;</code> Retrieves information about cluster </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli cluster info 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli cluster list</code> Lists the clusters managed by Heketi </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli cluster list </p>
</dl>
<h3>Device Commands</h3>
<dl>
<dd><code>heketi-cli device add &#8211;name=&lt;DEVICE-NAME&gt; &#8211;node=&lt;NODE-ID&gt;</code> Add new device to node to be managed by Heketi</p>
<dt><code> Options</code></p>
<dd></dl>
<p> <code> &#8211;name</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name of device to add </p>
<p> <code> &#8211;node</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Id of the node which has this device </p>
<p>&nbsp;<wbr><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Example</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli device add&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;name=/dev/sdb<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;node=3e098cb4407d7109806bb196d9e8f095 </p>
<dl>
<dd><code>heketi-cli device delete &lt;DEVICE-ID&gt;</code> Deletes a device from Heketi node </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli device delete 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli device disable &lt;DEVICE-ID&gt;</code> Disallow usage of a device by placing it offline </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli device disable 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli device enable &lt;DEVICE-ID&gt;</code> Allows device to go online </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli device enable 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli device info &lt;DEVICE-ID&gt;</code> Retrieves information about device </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli device info 886a86a868711bef83001 </p>
</dl>
<h3>Node Commands</h3>
<dl>
<dd><code>heketi-cli node add &#8211;zone=&lt;ZONE-NUMBER&gt; &#8211;cluster=&lt;CLUSTER-ID&gt; &#8211;management-host-name=&lt;MANAGEMENT-HOSTNAME&gt; &#8211;storage-host-name=&lt;STORAGE-HOSTNAME&gt;</code> Add new node to be managed by Heketi</p>
<dt><code> Options</code></p>
<dd></dl>
<p> <code> &#8211;cluster</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The cluster in which the node should reside </p>
<p> <code> &#8211;management-host-name</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Management host name </p>
<p> <code> &#8211;storage-host-name</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Storage host name </p>
<p> <code> &#8211;zone</code>=-1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The zone in which the node should reside </p>
<p>&nbsp;<wbr><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Example</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli node add&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;zone=3&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;cluster=3e098cb4407d7109806bb196d9e8f095&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;management-host-name=node1-manage.gluster.lab.com&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;storage-host-name=node1-storage.gluster.lab.com </p>
<dl>
<dd><code>heketi-cli node delete &lt;NODE-ID&gt;</code> Deletes a node from Heketi management </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli node delete 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli node disable &lt;NODE-ID&gt;</code> Disallow usage of a node by placing it offline </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli node disable 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli node enable &lt;NODE-ID&gt;</code> Allows node to go online </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli node enable 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli node info &lt;NODE-ID&gt;</code> Retrieves information about node </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli node info 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli node list</code> List all nodes in cluster </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli node list </p>
</dl>
<h3>Setup OpenShift/Kubernetes persistent storage for Heketi</h3>
<dl>
<dd><code>heketi-cli setup-openshift-heketi-storage</code> Creates a dedicated GlusterFS volume for Heketi. Once the volume is created, a Kubernetes/OpenShift list object is created to configure the volume.</p>
<dt><code> Options</code></p>
<dd></dl>
<p> <code> &#8211;listfile</code>=&quot;heketi-storage.json&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Filename to contain list of objects </p>
<p>&nbsp;<wbr><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Example</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli setup-openshift-heketi-storage</p>
<h3>Topology Commands</h3>
<dl>
<dd><code>heketi-cli topology load &#8211;json=&lt;JSON-FILENAME&gt;</code> Add devices to Heketi from a configuration file</p>
<dt><code> Options</code></p>
<dd></dl>
<p> <code> -j, &#8211;json</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Configuration containing devices, nodes, and clusters, in JSON format </p>
<p>&nbsp;<wbr><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Example</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli topology load &#8211;json=topo.json </p>
<dl>
<dd><code>heketi-cli topology info </code> Retreives information about the current Topology </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli topology info </p>
</dl>
<h3>Volume Commands</h3>
<dl>
<dd><code>heketi-cli volume create &#8211;cluster=&lt;CLUSTER-ID&gt; &#8211;disperse-data=&lt;DISPERSION-VALUE&gt; &#8211;durability=&lt;TYPE&gt; &#8211;name=&lt;VOLUME-NAME&gt; &#8211;redundancy=&lt;REDUNDENCY-VALUE&gt; &#8211;replica=&lt;REPLICA-VALUE&gt; &#8211;size=&lt;VOLUME-SIZE&gt; &#8211;snapshot-factor=&lt;SNAPSHOT-FACTOR-VALUE&gt;</code> Create a GlusterFS volume</p>
<dt><code> Options</code></p>
<dd></dl>
<p> <code> &#8211;clusters</code>=&quot;&quot; </p>
<dl>
<dd>
<pre> Optional: Comma separated list of cluster ids where this volume
 must be allocated. If omitted, Heketi will allocate the volume
 on any of the configured clusters which have the available space.
 Providing a set of clusters will ensure Heketi allocates storage
 for this volume only in the clusters specified.</pre>
</dl>
<p> <code> &#8211;disperse-data</code>=4 </p>
<dl>
<dd>
<pre> Optional: Dispersion value for durability type 'disperse'.
 Default is 4</pre>
</dl>
<p> <code> &#8211;durability</code>=&quot;replicate&quot; </p>
<dl>
<dd>
<pre> Optional: Durability type.
 Values are:
 none: No durability. Distributed volume only.
 replicate: (Default) Distributed-Replica volume.
 disperse: Distributed-Erasure Coded volume.</pre>
</dl>
<p> <code> &#8211;gid</code>=0 </p>
<dl>
<dd>
<pre> Optional: Initialize volume with the specified group id
 Default is 0</pre>
</dl>
<p> <code> &#8211;name</code>=&quot;&quot; </p>
<dl>
<dd>
<pre> Optional: Name of volume. Only set if really necessary</pre>
</dl>
<p> <code> &#8211;persistent-volume</code>[=false] </p>
<dl>
<dd>
<pre> Optional: Output to standard out a persistent volume JSON file for OpenShift or
 Kubernetes with the name provided.</pre>
</dl>
<p> <code> &#8211;persistent-volume-endpoint</code>=&quot;&quot; </p>
<dl>
<dd>
<pre> Optional: Endpoint name for the persistent volume</pre>
</dl>
<p> <code> &#8211;persistent-volume-file</code>=&quot;&quot; </p>
<dl>
<dd>
<pre> Optional: Create a persistent volume JSON file for OpenShift or
 Kubernetes with the name provided.</pre>
</dl>
<p> <code> &#8211;redundancy</code>=2 </p>
<dl>
<dd>
<pre> Optional: Redundancy value for durability type 'disperse'.
 Default is 2</pre>
</dl>
<p> <code> &#8211;replica</code>=3 </p>
<dl>
<dd>
<pre> Replica value for durability type 'replicate'.
 Default is 3</pre>
</dl>
<p> <code> &#8211;size</code>=-1 </p>
<dl>
<dd>
<pre> Size of volume in GB</pre>
</dl>
<p> <code> &#8211;snapshot-factor</code>=1 </p>
<dl>
<dd>
<pre> Optional: Amount of storage to allocate for snapshot support.
 Must be greater 1.0. For example if a 10TiB volume requires 5TiB of
 snapshot storage, then snapshot-factor would be set to 1.5. If the
 value is set to 1, then snapshots will not be enabled for this volume</pre>
</dl>
<p>&nbsp;<wbr><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Example</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Create a 100GB replica 3 volume:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume create &#8211;size=100<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Create a 100GB replica 3 volume specifying two specific clusters:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume create &#8211;size=100&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;clusters=0995098e1284ddccb46c7752d142c832,60d46d518074b13a04ce1022c8c7193c<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Create a 100GB replica 2 volume with 50GB of snapshot storage:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume create &#8211;size=100 &#8211;snapshot-factor=1.5 &#8211;replica=2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Create a 100GB distributed volume<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume create &#8211;size=100 &#8211;durability=none<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Create a 100GB erasure coded 4+2 volume with 25GB snapshot storage:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume create &#8211;size=100 &#8211;durability=disperse &#8211;snapshot-factor=1.25<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Create a 100GB erasure coded 8+3 volume with 25GB snapshot storage:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume create &#8211;size=100 &#8211;durability=disperse &#8211;snapshot-factor=1.25&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;disperse-data=8 &#8211;redundancy=3 </p>
<dl>
<dd><code>heketi-cli volume delete &lt;VOLUME-ID&gt;</code> Deletes the volume </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume delete 886a86a868711bef83001</dl>
<dl>
<dd><code>heketi-cli volume expand &#8211;expand-size=&lt;SIZE&gt; &#8211;volume=&lt;VOLUME-ID&gt;</code> Expand a volume</p>
<dt><code> Options</code></p>
<dd></dl>
<p> <code> &#8211;expand</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Amount in GB to add to the volume </p>
<p> <code> &#8211;volume</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Id of volume to expand </p>
<p> <code> Example</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Add 10GB to a volume<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume expand &#8211;volume=60d46d518074b13a04ce1022c8c7193c &#8211;expand-size=10 </p>
<dl>
<dd><code>heketi-cli volume info &lt;VOLUME-ID&gt;</code> Retrieves information about volume </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume info 886a86a868711bef83001 </p>
</dl>
<dl>
<dd><code>heketi-cli volume list</code> Lists the volumes managed by Heketi </p>
<p>&nbsp;<wbr><code>Example</code><br />
&nbsp;<wbr>$&nbsp;<wbr>heketi-cli volume list </p>
</dl>
<h2>Global Options</h2>
<p><code>&#8211;json</code>[=false] </p>
<dl>
<dd>
<pre>Print response as JSON</pre>
</dl>
<p> <code>&#8211;secret</code>=&quot;&quot; </p>
<dl>
<dd>
<pre>Secret key for specified user. Can also be
set using the environment variable HEKETI_CLI_KEY</pre>
</dl>
<p> <code>-s</code>, <code>&#8211;server</code>=&quot;&quot; </p>
<dl>
<dd>
<pre>Heketi server. Can also be set using the
environment variable HEKETI_CLI_SERVER</pre>
</dl>
<p> <code>&#8211;user</code>=&quot;&quot; </p>
<dl>
<dd>
<pre>Heketi user. Can also be set using the
environment variable HEKETI_CLI_USER</pre>
</dl>
<p> <code>-v</code>, <code>&#8211;version</code>[=false] </p>
<dl>
<dd>
<pre>Print version</pre>
</dl>
<h2>Example</h2>
<dl>
<dd>
<pre> $ export HEKETI_CLI_SERVER=<a rel="nofollow" href="http://localhost:8080">http://localhost:8080</a>
 $ heketi-cli volume list</pre>
</dl>
<h2>Copyright</h2>
<pre>Copyright (c) 2015 The heketi Authors</pre>
