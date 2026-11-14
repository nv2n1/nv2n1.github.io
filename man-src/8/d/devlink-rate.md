---
title: "devlink-rate(8)"
name: "devlink-rate"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-rate/"
description: "devlink-rate – devlink rate management"
---

<p>devlink-rate &#8211; devlink rate management</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

port function rate

{ COMMAND |

    help }

OPTIONS := {

    -j[son] | -p[retty] | -i[ec] }</code></pre>
<p> <code>devlink port function rate show</code> [ { <i>DEV/PORT_INDEX</i> | <i>DEV/NODE_NAME</i> } ]<br />
 <code>devlink port function rate set</code> { <i>DEV/PORT_INDEX</i> | <i>DEV/NODE_NAME</i> } [<code> tx_share </code><i>VALUE </i>] [<code> tx_max </code><i>VALUE </i>] [ {<code> parent </code><i>NODE_NAME </i>|<code> noparent </code>} ]<br />
 <code>devlink port function rate add </code><i>DEV/NODE_NAME</i> [<code> tx_share </code><i>VALUE </i>] [<code> tx_max </code><i>VALUE </i>] [ {<code> parent </code><i>NODE_NAME </i>|<code> noparent </code>} ]<br />
 <code>devlink port function rate del </code><i>DEV/NODE_NAME</i><br />
 <code>devlink port function rate help</code> </p>
<h2>Description</h2>
<h3>devlink port function rate show &#8211; display rate objects.</h3>
<p>Displays specified rate object or, if not specified, all rate objects. Rate object can be presented by one of the two types:</p>
<dl>
<dt><code>leaf</code></p>
<dd>Represents a single devlink port; created/destroyed by the driver and bound to the devlink port. As example, some driver may create leaf rate object for every devlink port associated with VF. Since leaf have 1to1 mapping to it&#8217;s devlink port, in user space it is referred as corresponding devlink port <i>DEV/PORT_INDEX</i>;</p>
<dt><code>node</code></p>
<dd>Represents a group of rate objects; created/deleted by the user (see command below) and bound to the devlink device rather then to the devlink port. In userspace it is referred as <i>DEV/NODE_NAME</i>, where node name can be any, except decimal number, to avoid collisions with leafs.</dl>
<p> Command output show rate object identifier, it&#8217;s type and rate values along with parent node name. Rate values printed in SI units which are more suitable to represent specific value. To print values in IEC units <code>-i</code> switch is used. JSON (<code>-j</code>) output always print rate values in bytes per second. Zero rate values means &quot;unlimited&quot; rates and ommited in output, as well as parent node name.</p>
<h3>devlink port function rate set &#8211; set rate object parameters.</h3>
<p>Allows set rate object&#8217;s parameters. If any parameter specified multiple times the last occurrence is used. <i>DEV/PORT_INDEX</i> &#8211; specifies devlink leaf rate object.<br />
 <i>DEV/NODE_NAME</i> &#8211; specifies devlink node rate object. <code>tx_share</code><i> VALUE</i> &#8211; specifies minimal tx rate value shared among all rate objects. If rate object is a part of some rate group, then this value shared with rate objects of this rate group. <code>tx_max</code><i> VALUE</i> &#8211; specifies maximum tx rate value.</p>
<dl>
<dt><i>VALUE</i></p>
<dd>These parameter accept a floating point number, possibly followed by either a unit (both SI and IEC units supported).</p>
<dl>
<dd>
<dl>
<dt>bit or a bare number</p>
<dd>Bits per second</p>
<dt>kbit</p>
<dd>Kilobits per second</p>
<dt>mbit</p>
<dd>Megabits per second</p>
<dt>gbit</p>
<dd>Gigabits per second</p>
<dt>tbit</p>
<dd>Terabits per second</p>
<dt>bps</p>
<dd>Bytes per second</p>
<dt>kbps</p>
<dd>Kilobytes per second</p>
<dt>mbps</p>
<dd>Megabytes per second</p>
<dt>gbps</p>
<dd>Gigabytes per second</p>
<dt>tbps</p>
<dd>Terabytes per second</dl>
<p> To specify in IEC units, replace the SI prefix (k-, m-, g-, t-) with IEC prefix (ki-, mi-, gi- and ti-) respectively. Input is case-insensitive.</dl>
</dl>
<p> <code>parent</code><i> NODE_NAME </i>| <code>noparent</code> &#8211; set rate object parent to existing node with name <i>NODE_NAME</i> or unset parent. Rate limits of the parent node applied to all it&#8217;s children. Actual behaviour is details of driver&#8217;s implementation. Setting parent to empty (&quot;&quot;) name due to the kernel logic threated as parent unset.</p>
<h3>devlink port function rate add &#8211; create node rate object with specified parameters.</h3>
<p>Creates rate object of type node and sets parameters. Parameters same as for the &quot;set&quot; command. <i>DEV/NODE_NAME</i> &#8211; specifies the devlink node rate object to create.</p>
<h3>devlink port function rate del &#8211; delete node rate object</h3>
<p>Delete specified devlink node rate object. Node can&#8217;t be deleted if there is any child, user must explicitly unset the parent. <i>DEV/NODE_NAME</i> &#8211; specifies devlink node rate object to delete.</p>
<h3>devlink port function rate help &#8211; display usage information</h3>
<p>Display devlink rate usage information </p>
<h2>Examples</h2>
<p><code>*</code> Display all rate objects:</p>
<dl>
<dd># devlink port function rate show<br />
 pci/0000:03:00.0/1 type leaf parent some_group<br />
 pci/0000:03:00.0/2 type leaf tx_share 12Mbit<br />
 pci/0000:03:00.0/some_group type node tx_share 1Gbps tx_max 5Gbps</dl>
<p> <code>*</code> Display leaf rate object bound to the 1st devlink port of the pci/0000:03:00.0 device:</p>
<dl>
<dd># devlink port function rate show pci/0000:03:00.0/1<br />
 pci/0000:03:00.0/1 type leaf
</dl>
<p> <code>*</code> Display leaf rate object rate values using IEC units:</p>
<dl>
<dd># devlink -i port function rate show pci/0000:03:00.0/2<br />
 pci/0000:03:00.0/2 type leaf 11718Kibit
</dl>
<p> <code>*</code> Display node rate object with name some_group of the pci/0000:03:00.0 device:</p>
<dl>
<dd># devlink port function rate show pci/0000:03:00.0/some_group<br />
 pci/0000:03:00.0/some_group type node
</dl>
<p> <code>*</code> Display pci/0000:03:00.0/2 leaf rate object as pretty JSON output:</p>
<dl>
<dd># devlink -jp port function rate show pci/0000:03:00.0/2<br />
 { </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;rate&quot;:&nbsp;{ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;pci/0000:03:00.0/2&quot;:&nbsp;{ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;type&quot;:&nbsp;&quot;leaf&quot;, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;tx_share&quot;: 1500000 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
 }</dl>
<p> <code>*</code> Create node rate object with name &quot;1st_group&quot; on pci/0000:03:00.0 device:</p>
<dl>
<dd># devlink port function rate add pci/0000:03:00.0/1st_group</dl>
<p> <code>*</code> Create node rate object with specified parameters:</p>
<dl>
<dd># devlink port function rate add pci/0000:03:00.0/2nd_group \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>tx_share 10Mbit tx_max 30Mbit parent 1st_group
</dl>
<p> <code>*</code> Set parameters to the specified leaf rate object:</p>
<dl>
<dd># devlink port function rate set pci/0000:03:00.0/1 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>tx_share 2Mbit tx_max 10Mbit
</dl>
<p> <code>*</code> Set leaf&#8217;s parent to &quot;1st_group&quot;:</p>
<dl>
<dd># devlink port function rate set pci/0000:03:00.0/1 parent 1st_group</dl>
<p> <code>*</code> Unset leaf&#8217;s parent:</p>
<dl>
<dd># devlink port function rate set pci/0000:03:00.0/1 noparent</dl>
<p> <code>*</code> Delete node rate object:</p>
<dl>
<dd># devlink port function rate del pci/0000:03:00.0/2nd_group</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-port/">devlink-port</a></code>(8) </p>
<h2>Author</h2>
<p>Dmytro Linkin &lt;dlinkin [at] nvidia.com&gt;</p>
