---
title: "isnsadm(8)"
name: "isnsadm"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isnsadm/"
description: "isnsadm – iSNS client utility"
---

<p>isnsadm &#8211; iSNS client utility</p>
<h2>Synopsis</h2>
<p><code>isnsadm</code> [<i>options&#8230;</i>] &#8211;register<i> object&#8230;</i> <code>isnsadm</code> [<code>&#8230;</code>] &#8211;query<i> attr</i>[=<i>value</i>] <code>isnsadm</code> [<code>&#8230;</code>] &#8211;deregister<i> attr=value</i> <code>isnsadm</code> [<code>&#8230;</code>] &#8211;list<i> type attr=value</i> <code>isnsadm</code> [<code>&#8230;</code>] &#8211;dd-register<i> attr=value</i> <code>isnsadm</code> [<code>&#8230;</code>] &#8211;enroll<i> client-name attr=value</i> <code>isnsadm</code> [<code>&#8230;</code>] &#8211;edit-policy<i> attr=value</i> </p>
<h2>Description</h2>
<p><code>Isnsadm</code> is a command line utility for interacting with an iSNS server. It operates in one of several modes, which are mutually exclusive. Currently, <code>isnsadm</code> supports registration, query, and deregistration.</p>
<h2>Options</h2>
<p>By default, <code>isnsadm</code> will take most of its settings from the configuration file <code>/etc/isns/isnsadm.conf</code>, with the exception of the following options:</p>
<dl>
<dt><code>&#8211;config</code><i> filename</i>, <code>-c</code><i> filename</i></p>
<dd>This option overrides the default configuration file.</p>
<dt><code>&#8211;debug</code><i> facility</i>, <code>-d</code><i> facility</i></p>
<dd>enables debugging. Valid facilities are</dl>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>socket</code></td>
<td>network send/receive</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>auth</code></td>
<td>authentication and security related information</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>message</code></td>
<td>iSNS protocol layer</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>state</code></td>
<td>database state</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>scn</code></td>
<td>SCN (state change notification) messages</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>esi</code></td>
<td>ESI (entity status inquiry) messages</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>all</code></td>
<td>all of the above</td>
<td ALIGN=right>
</td>
</tr>
</table>
</table>
<p></center> </p>
<dl>
<dt><code>&#8211;local</code></p>
<dd>makes <code>isnsadm</code> use a Local (aka Unix) socket when talking to the iSNS server. This can be used by the administrator to perform management tasks, such as enrolling new clients, editing access control and so on. Local mode is only available to the super user.</p>
<dt><code>&#8211;control</code></p>
<dd>makes <code>isnsadm</code> assume the identity of a control node. Control nodes are special in that they have more rights in accessing and modifying the database than normal storage nodes have.</dl>
<p> When using this option, <code>isnsadm</code> will use the source name and DSA key specified by the <code>Control.SourceName</code> and <code>Control.AuthKeyFile</code> configuration options, respectively. </p>
<dl>
<dt><code>&#8211;key</code><i> attr</i><code>=</code><i>value</i></p>
<dd>This option is recognized in registration mode only, and lets you specify an object key. For a more detailed explanation, refer to section <code>Registration mode</code>.</p>
<dt><code>&#8211;keyfile=</code><i>filename</i></p>
<dd>When creating a policy for a new iSNS client, <code>isnsadm</code> is able to generate a DSA key for the client. The public part of the key is stored in a policy object in the iSNS server&#8217;s database, whereas the private portion is stored in the file specified by the <code>keyfile</code> option. <code></p>
<dt>&#8211;help</code></p>
<dd>This will print a help message and exit.</dl>
<h3>Built-in help</h3>
<p><code>Isnsadm</code> has built-in help functions. When invoked with <code>&#8211;help</code>, it will print a general help message showing all supported command modes, and exit. Specific help on an individual command mode is available by invoking that mode with a single argument of <code>help</code>, like this: </p>
<p> <code>isnsadm &#8211;register help</code> </p>
<p> This will print a help message describing how to use this command mode, followed by a list of attributes this command supports and a help text describing the attribute.</p>
<h3>Supported attributes</h3>
<p>Most command modes take a list of attributes as arguments on the command line. The naming and syntax of these attributes as the same for all commands modes, however certain modes support only a limited set of attributes. </p>
<p> Attributes are usually given as <i>name</i><code>=</code><i>value</i> pairs. Where empty (or NIL) attributes are supported, the attribute name by itself can be given. </p>
<p> The syntax of attribute <i>value</i> depends on the attribute type. For strings and numeric values, no special conventions apply, but bitfields have a special syntax described below. </p>
<p> The attribute name is usually preceded by the object type it applies to (such as <code>entity</code>), followed by a hyphen and the name itself. However, where the context clearly determines a specific object type, the prefix can be omitted. For instance, when editing a policy object using <code>&#8211;edit-policy</code>, it is acceptable to use <code>node-type</code> as shorthand for <code>policy-node-type</code>. </p>
<p> Likewise, in a query command, it is not permitted to mix attributes from different object types. Thus, the first attribute of a query string establishes a type context, so that the following two invocations are equivalent: </p>
<p> <code>isnsadm &#8211;query pg-name=iqn.com.foo pg-addr=10.1.1.1 pg-port=860/tcp</code><br />
 <code>isnsadm &#8211;query pg-name=iqn.com.foo addr=10.1.1.1 port=860/tcp</code> </p>
<p> <code>Isnsadm</code> currently supports the following attributes: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><i>Context</i></td>
<td><i>Attribute</i></td>
<td><i>iSNS tag</i></td>
<td><i>Aliases</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2>Network Entity</td>
<td><code>entity-id</code></td>
<td ALIGN=right>1</td>
<td><code>eid</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>entity-prot</code></td>
<td ALIGN=right>2</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>entity-index</code></td>
<td ALIGN=right>7</td>
<td></td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2>iSCSI Storage Node</td>
<td><code>iscsi-name</code></td>
<td ALIGN=right>32</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>iscsi-node-type</code></td>
<td ALIGN=right>33</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>iscsi-alias</code></td>
<td ALIGN=right>34</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>iscsi-idx</code></td>
<td ALIGN=right>36</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>iscsi-authmethod</code></td>
<td ALIGN=right>42</td>
<td></td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2>Portal</td>
<td><code>portal-addr</code></td>
<td ALIGN=right>16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>portal-port</code></td>
<td ALIGN=right>17</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>portal-name</code></td>
<td ALIGN=right>18</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>portal-esi-port</code></td>
<td ALIGN=right>20</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>portal-esi-interval</code></td>
<td ALIGN=right>21</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>portal-idx</code></td>
<td ALIGN=right>22</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>portal-scn-port</code></td>
<td ALIGN=right>23</td>
<td></td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2>Portal Group</td>
<td><code>portal-group-index</code></td>
<td ALIGN=right>52</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pg-name</code></td>
<td ALIGN=right>48</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>pg-addr</code></td>
<td ALIGN=right>49</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>pg-port</code></td>
<td ALIGN=right>50</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>pg-tag</code></td>
<td ALIGN=right>51</td>
<td><code>pgt</code></td>
</tr>
<tr VALIGN=top>
<td><code>pg-idx</code></td>
<td ALIGN=right>52</td>
<td></td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2>Discovery Domain</td>
<td><code>dd-id</code></td>
<td ALIGN=right>2065</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>dd-name</code></td>
<td ALIGN=right>2066</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>dd-member-iscsi-idx</code></td>
<td ALIGN=right>2067</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>dd-member-name</code></td>
<td ALIGN=right>2068</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>dd-member-fc-name</code></td>
<td ALIGN=right>2069</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>dd-member-portal-idx</code></td>
<td ALIGN=right>2070</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>dd-member-addr</code></td>
<td ALIGN=right>2071</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>dd-member-port</code></td>
<td ALIGN=right>2072</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>dd-features</code></td>
<td ALIGN=right>2078</td>
<td></td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2>Policy Object</td>
<td><code>policy-name</code></td>
<td ALIGN=right>&#8211;</td>
<td><code>spi</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>policy-key</code></td>
<td ALIGN=right>&#8211;</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>policy-entity</code></td>
<td ALIGN=right>&#8211;</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>policy-node-type</code></td>
<td ALIGN=right>&#8211;</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>policy-object-type</code></td>
<td ALIGN=right>&#8211;</td>
<td></td>
</tr>
<tr VALIGN=top>
<td><code>policy-functions</code></td>
<td ALIGN=right>&#8211;</td>
<td></td>
</tr>
</table>
</table>
<p></center></p>
<h3>Portal attributes</h3>
<p>Portal information is conveyed by two separate attributes in iSNS; an address attribute holding the IP address, and a TCP/UDP port attribute holding the port number and an indication of the protocol to be used (TCP or UDP). </p>
<p> When parsing a TCP/UDP port, Open-iSNS will expect a port number, optionally followed by a slash and the protocol. Port names such as &quot;iscsi-target&quot; are not supported. </p>
<p> As a convenience, <code>isnsadm</code> supports a notation representing a portal as one pseudo-attribute. Separating address and port by a colon. Thus, the following two are equivalent, with the latter being the shorthand representation of the former: </p>
<p> <code>addr=</code><i>&lt;address&gt;</i><code> port=</code><i>&lt;port&gt;</i><code>[/</code><i>protocol</i><code>]</code><i></i>. <code>portal=</code><i>&lt;adress&gt;</i><code>:</code><i>port</i><code>[/</code><i>protocol</i><code>]</code> </p>
<p> This notation can be used in any context where an <code>addr</code>/<code>port</code> attribute pair can appear, and may be prefixed by a type name, as in <code>pg-portal=&#8230;</code>. </p>
<p> When using literal IPv6 addresses, the address has to be surrounded by square brackets, otherwise the embedded colons would create ambiguity: <code>portal=[2001:5c0:0:2::24]:860/tcp</code></p>
<h3>Bitfield attributes</h3>
<p>Some iSNS attributes are words representing a bit field. <code>Isnsadm</code> displays and parses these attributes in human-readable form rather than using the numerical value. The names of the bit values are displayed by built-in help facilities. When specifying a bitfield attribute on the command line, you can combine them using the plus (<code>+</code>) or comma (<code>,</code>) character, like this: </p>
<p> <code>node-type=control+initiator</code></p>
<h3>Registration mode</h3>
<p>Registration mode is selected by using the <code>&#8211;register</code> option, followed by a list of one or more objects to register with the iSNS server. By default, this will create a network entity for the client (if none exists), and place the new objects inside it. Usually, you register all objects for a network entity in one operation, rather than each one separately. </p>
<p> Each object is specified as a type, optionally followed by a comma-separated list of attributes, such as this: </p>
<p> <code>target=iqn.2005-01.org.open-iscsi.foo:disk1,alias=disk1</code> </p>
<p> The following object types are currently supported:</p>
<dl>
<dt><code>entity=</code><i>name</i></p>
<dd>Tells the server to group all objects in the specified Network Entity container object. Normally, the iSNS server will automatically assign an entity name that is in line with its policies, and there is no need to specify it explicitly.</p>
<dt><code>initiator[=</code><i>name</i><code>]</code></p>
<dd>This will register an iSCSI storage node of type initiator. By default, the name is set to the iSNS source name.</p>
<dd>This can be followed by any number of iSCSI storage node attributes.</p>
<dt><code>target[=</code><i>name</i><code>]</code></p>
<dd>This will register an iSCSI storage node of type target. By default, the name is set to the iSNS source name.</p>
<dd>This object accepts the same set of attributes as <code>initiator</code>.</p>
<dt><code>control[=</code><i>name</i><code>]</code></p>
<dd>This will register an iSCSI storage node of type control. By default, the name is set to the iSNS source name. Only management nodes should be registered as control nodes, as this gives a node complete control over the iSNS database.</p>
<dd>This object accepts the same set of attributes as <code>initiator</code>.</p>
<dt><code>portal=[</code><i>address:port/proto</i><code>]</code></p>
<dd>This will register a portal using the given address, port and protocol triple. If the triple is omitted, <code>isnsadm</code> will use the client host&#8217;s IP address. If the portal is preceded by an initiator registration (on the command line), the port defaults to 860/tcp; if it is preceded by a target registration, the port defaults to 3260/tcp. For multi-homed hosts, the choice of address is implementation dependant.</p>
<dd>This can be followed by any number of portal attributes.</p>
<dt><code>pg</code></p>
<dd>This will register a portal group joining the preceding portal and node. Portal groups can be used to describe the preferred portals for a given node; please refer to RFC 4711 for details.</p>
<dd>This can be followed by any number of portal group attributes. The attribute list must specify a portal group tag (PGT) via the <code>pgt</code> attribute.</dl>
<p> There are two additional command line options of interest, which are used exclusively with Registration mode. One is <code>&#8211;replace</code>. Normally, registration mode will <i>add</i> new objects to the network entity associated with the client host. If you specify <code>&#8211;replace</code> on the command line, the server will wipe the network entity completely, and remove all portals and storage nodes it contained. Then it will create a new network entity, and place the portals and storage nodes provided by the caller inside. </p>
<p> In addition, it is possible to replace just parts of a network entity. This is achieved by using the command line option <code>&#8211;key</code> to specify the object that should be replaced. </p>
<p> For instance, assume a network entity contains the portal <code>10.1.1.1:860</code>, and the client&#8217;s network address changed to <code>10.2.7.7</code>. Then the following command will atomically update the database, replacing just the portal without touching the registered storage nodes: </p>
<p> <code> isnsadm &#8211;replace &#8211;key portal=10.1.1.1:860 portal=10.2.7.7:860</code> </p>
<p> The <code>&#8211;key</code> option recognizes only a subset of the usual attributes:</p>
<dl>
<dd>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><i>Object type</i></td>
<td><i>Syntax</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Entity</code></td>
<td><code>eid=<i>identifier</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Portal</code></td>
<td><code>portal=<i>address</i>:port</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>iSCSI Node</code></td>
<td><code>iscsi-name=<i>name</i></code>
</td>
</tr>
</table>
</table>
</dl>
<p> To get a list of supported attributes, invoke <code>isnsadm &#8211;register help</code>.</p>
<h3>Query mode</h3>
<p>Query mode is selected by using the <code>&#8211;query</code> option. A query consists of a list of <code>attr</code>=<i></i>value pairs. All attributes must belong to the same object type, i.e. queries that mix a Network Entity attribute with e.g. a Portal attribute will be rejected. </p>
<p> It is also possible to specify an attribute name without value (i.e. just <code>attr</code>), which will will match any object that has such an attribute, regardless of its value. This is useful when you want to query for all objects of a given type. </p>
<p> To obtain a list of supported attributes, invoke <code>isnsadm &#8211;query help</code>.</p>
<h3>List Mode</h3>
<p>In this mode, <code>isnsadm</code> will display all objects of a given type, optionally restricted to those matching certain attribute values. </p>
<p> The arguments to list mode are a <i>type name</i>, optionally followed by one or more <i>attr</i><code>=</code><i>value</i> pairs. Only attributes pertaining to the given type are permitted; for instance, if you specify a type name of <code>portals</code>, only portal attributes are permitted. </p>
<p> Possible type names are: <code>entities</code>, <code>nodes</code>, <code>portals</code>, <code>dds</code>, <code>ddsets</code>, <code>portal-groups</code>, and <code>policies</code>. </p>
<p> Additional information is available via <code>isnsadm &#8211;list help</code>.</p>
<h3>Deregistration mode</h3>
<p>In this mode, you can deregister objects previously registered. Only the node which registered an entity in the first place is permitted to remove it, or any of its child objects. (Control nodes are not bound by this restriction). </p>
<p> In deregistration mode, the argument list consists of a list of <i>attr</i><code>=</code><i>value</i> pairs. Deregistration supports the same set of attributes as query mode.</p>
<h3>Discovery Domain Registration</h3>
<p>This mode, allows to register a discovery domain or to add new members to an existing discovery domain. Again, attributes are specified as a list of <i>attr</i><code>=</code><i>value</i> pairs. Only discovery domain attributes are recognized. </p>
<p> Note, in order to add members to an existing domain, you must specify the domain&#8217;s numeric ID. The domain&#8217;s symbolic name is not a valid handle when referring to a discovery domain.</p>
<h3>Client Enrollment</h3>
<p>This mode only works when the server recognizes the client as having control node capabilities, which is possible in two ways:</p>
<dl>
<dt>Invoke</p>
<dd><code>isnsadm &#8211;local</code> as super user on the host <code>isnsd</code> is running on. The <code>&#8211;local</code> options tells it to communicate with the server through the local control socket.</p>
<dt>Invoke</p>
<dd><code>isnsadm &#8211;control</code>, which tells it to assume the identity of a control node. When given this option, <code>isnsadm</code> will use the source name and DSA key specified by the <code>Control.SourceName</code> and <code>Control.AuthKeyFile</code> configuration options, respectively. The server must be configured to grant this identity control node status.</dl>
<p> To enroll a client, use the <code>&#8211;enroll</code> option, followed by the (source) name of the client to enroll. This string will be used as the name of the security policy the client will use to identify itself. </p>
<p> This is followed by a list of attribute/value pairs, where the following set of attributes is supported: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><i>Attribute</i></td>
<td><i>Description</i></td>
<td><i>Aliases</i></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>name</code></td>
<td>Policy Name</td>
<td ALIGN=right>spi</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>key</code></td>
<td>Client&#8217;s DSA public key</td>
<td ALIGN=right></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>entity</code></td>
<td>Assigned Entity Identifier</td>
<td ALIGN=right></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>node-type</code></td>
<td>Permitted node type(s)</td>
<td ALIGN=right></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>node-name</code></td>
<td>Permitted node name(s)</td>
<td ALIGN=right></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>functions</code></td>
<td>Bitmap of permitted functions</td>
<td ALIGN=right></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>object-type</code></td>
<td>Object access mask</td>
<td ALIGN=right></td>
<td>
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The <code>key</code> attribute is used to specify the DSA public key that the server should use to authenticate messages from this client. You can either provide a file name; in which case <code>isnsadm</code> will try to read the PEM encoded public key from that file. If no <code>key</code> attribute is given, or when using <code>key=gen</code>, <code>isnsadm</code> will generate a DSA key. The private portion of the newly generated key will be stored in the file specified by <code>&#8211;keyfile=</code><i>filename</i>. </p>
<p> The <code>object-type</code> attribute is used to specify which object types the client is permitted to access. This is a comma separated list of <i>type</i><code>:</code><i>perm</i> pairs, where <i>type</i> can be any of <code>entity</code>, <code>iscsi-node</code>, <code>portal</code>, <code>portal-group</code>, <code>dd</code>, <code>ddset</code>, and <code>policy</code>. The permissions can be either <code>rw</code>, or <code>r</code>. </p>
<p> The <code>functions</code> attribute can be used to restrict which functions the client is permitted to invoke. This is a bitfield, using the standard function names from RFC 4171, such as <code>DevAttrReg</code>, <code>DevAttrQry</code>, etc. </p>
<p> For a description of the open-isns security model and policies, please refer to the <code><a href="/docs/linux/man/5-isns_config/">isns_config</a></code>(5) manual page. </p>
<p> <code>Important note</code>: In order to generate a DSA key, you have to have a set of DSA parameters installed. By default, <code>isnsadm</code> expects to find them in <code>/etc/isns/dsa.params</code>. These parameters are created by calling <code>isnsd &#8211;init</code> once on the server machine. Alternatively, you can use the following command: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> openssl dsaparam 1024 -out /etc/isns/dsa.params </p>
<p> where 1024 is the chosen DSA key size, in bits.</p>
<h2>Examples</h2>
<p>If you want to use Open-iSNS in authenticated mode, you first need to initialize the server&#8217;s DSA key and DSA parameters. This can be done conveniently by using </p>
<p> <code>isnsd &#8211;init</code> </p>
<p> This will create the server&#8217;s private and public key, and place them in <code>/etc/isns/auth_key</code> and <code>auth_key.pub</code>, respectively. </p>
<p> The following command will create a policy object for a node named <code>isns.control ,</code> and grant it control privileges: </p>
<p> <code>isnsadm &#8211;local &#8211;keyfile=control.key</code> <code>&#8211;enroll isns.control \</code><br />
 <code> node-type=ALL functions=ALL object-type=ALL</code> </p>
<p> In the process of entrolling the client, this will generate a DSA key pair, and place the private key portion in the file <code>control.key</code>. This file must be installed as <code>/etc/isns/control.key</code> on the host you wish to use as an iSNS management station. </p>
<p> Next, you need to create a storage node object for the management station: </p>
<p> <code>isnsadm &#8211;local &#8211;register control</code> </p>
<p> On the management station, you can then enroll additional hosts: </p>
<p> <code>isnsadm &#8211;control &#8211;keyfile=somehost.key</code> <code>&#8211;enroll iqn.2005-01.org.open-iscsi.somehost \</code><br />
 <code> node-type=target+initiator</code> </p>
<p> Again, this will generate a DSA key pair and store the private key portion in auth_key. Note the use of the <code>&#8211;control</code> option that tells <code>isnsadm</code> to use the identity of the control node instead of the default key and source name. </p>
<p> You then need to copy <code>somehost.key</code> to the client host and install it as <code>/etc/isns/auth_key</code>. Likewise, the server&#8217;s public key (which resides in <code>/etc/isns/auth_key.pub</code> on the server) needs to be copied to the client machine, and placed in <code>/etc/isns/server_key.pub</code>. </p>
<p> By default, when a client registers a storage node (be it initiator or target) with iSNS, the client will not be able to see any other storage nodes. In order for targets to be visible to a given initiator, you need to create so-called Discovery Domains (or DDs for short). </p>
<p> Currently, domain membership operations require administrator privilege. Future extensions may allow iSNS clients to add themselves to one or more DDs upon registration. </p>
<p> To create a discovery domain, and add nodes to it, you can use </p>
<p> <code>isnsadm &#8211;control &#8211;dd-register dd-name=mydomain \</code><br />
 <code> member-name=iqn.org.bozo.client iqn.org.bozo.jbod &#8230;</code> </p>
<p> In order to add members to an existing DD, you have to specify the numeric domain ID &#8211; using the DD name is not sufficient, unfortunately (this is a requirement of the RFC, not an implementation issue): </p>
<p> <code>isnsadm &#8211;control &#8211;dd-register dd-id=42 \</code><br />
 <code> member-name=iqn.com.foo member-name=iqn.com.bar</code> </p>
<p> The DD ID can be obtained by doing a query for the DD name: </p>
<p> <code>isnsadm &#8211;control &#8211;query dd-name=mydomain</code> </p>
<p> In management mode, you can also register and deregister nodes and portals manually, in case you want to fix up an inconsisteny in the database. For instance, this will register a node and portal on a host named client.bozo.org: </p>
<p> <code>isnsadm &#8211;control &#8211;register entity=client.bozo.org \</code><br />
 <code> initiator=iqn.org.bozo.client portal=191.168.7.1:860</code> </p>
<p> Note that this registration explicitly specifies the network entity in which to place the new objects. If you omit this, the new objects will be placed in an entity named <code>CONTROL</code>, which is decidedly not what you want.</p>
<h2>See Also</h2>
<p>RFC 4171, <code><a href="/docs/linux/man/8-isnsd/">isnsd</a></code>(8), <code><a href="/docs/linux/man/5-isns_config/">isns_config</a></code>(5).</p>
<h2>Authors</h2>
<p>Olaf Kirch &lt;olaf.kirch [at] oracle.com&gt;</p>
