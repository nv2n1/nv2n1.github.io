---
title: "plotnetcfg-json(5)"
name: "plotnetcfg-json"
section: "5"
letter: "p"
url: "/docs/linux/man/5-plotnetcfg-json/"
description: "plotnetcfg – json output format"
---

<p>plotnetcfg &#8211; json output format</p>
<h2>Description</h2>
<h3>Root object fields</h3>
<dl>
<dt>format</p>
<dd><i>(number)</i> Currently 1. Will be increased if incompatible changes are introduced. A tool parsing the json output should refuse any format it&#8217;s not aware of. Note that adding of new fields is not considered to be an incompatible change.</p>
<dt>version</p>
<dd><i>(string)</i> Plotnetcfg version.</p>
<dt>date</p>
<dd><i>(string)</i> Time and date when the data were gathered, in <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) format.</p>
<dt>namespaces</p>
<dd><i>(array)</i> Array of name space objects. The first one is always the root name space.</dl>
<h3>Name space object fields</h3>
<dl>
<dt>name</p>
<dd><i>(string)</i> Name of the name space suitable for user consumption. This in general cannot be used for machine consumption, e.g. switching to the name space. The root name space has an empty name.</p>
<dt>interfaces</p>
<dd><i>(array)</i> Array of interface objects.</p>
<dt>warnings</p>
<dd><i>(array)</i> If present, an array of strings. Contains error messages encountered when gathering data in the given name space.</dl>
<h3>Interface object fields</h3>
<dl>
<dt>id</p>
<dd><i>(string)</i> Unique identifier of the interface. This is an arbitrary opaque string and the consumer should not make any assumption of its contents (apart of not containing null characters). It should not be displayed to the user, the sole purpose of this field is linking to other interfaces. The identifier is globally unique, it is safe to assume that interfaces with the same name in different name spaces have a different id.</p>
<dt>name</p>
<dd><i>(string)</i> User visible name of the interface. Usually (but not always) the name of the corresponding Linux interface. This is not unique between name spaces.</p>
<dt>driver</p>
<dd><i>(string)</i> The kernel module (driver) behind the interface. May be empty in some specific cases.</p>
<dt>info</p>
<dd><i>(array)</i> Array of strings. Contains additional information about the interface, formatted. An example is tunnel endpoints. The exact content is dependent on the type of the interface.</p>
<dt>addresses</p>
<dd><i>(array)</i> Array of address objects.</p>
<dt>mtu</p>
<dd><i>(number)</i> Interface MTU.</p>
<dt>type</p>
<dd><i>(string)</i></p>
<dl>
<dd>&quot;device&quot;: normal interface. Most interfaces are of this type. &quot;internal&quot;: this interface is not backed up by a Linux interface. Can be often found with Open vSwitch. Further types are possible with future plotnetcfg versions. Adding them will not be considered a format change.</dl>
<dt>state</p>
<dd><i>(string)</i></p>
<dl>
<dd>&quot;down&quot;: the interface is administratively disabled. &quot;up&quot;: the interface is up and operating. &quot;up_no_link&quot;: the interface is up but has no link. &quot;none&quot;: state cannot be determined or is not applicable to this kind of interface. More states are possible to be added in future plotnetcfg versions. Adding them will not be considered a format change.</dl>
<dt>warning</p>
<dd><i>(bool)</i> There was a problem gathering data about this interface. Details are in the name space warnings field. The purpose of this flag is for visual representation of this interface as not having complete data available. Not present if there was no error.</p>
<dt>parent</p>
<dd><i>(object)</i> The parent interface, as a connection object. Not present if there&#8217;s no parent.</p>
<dt>children</p>
<dd><i>(array)</i> Array of children interfaces, as connection objects. Not present if there are no children.</p>
<dt>peer</p>
<dd><i>(object)</i> The peer interface, as a connection object. Not present if there&#8217;s no peer.</dl>
<h3>Connection object fields</h3>
<dl>
<dt>info</p>
<dd><i>(array)</i> Array of strings. Contains additional information about the connection between the two interfaces, formatted. May be an empty array.</p>
<dt>target</p>
<dd><i>(string)</i> Id of the interface that is being linked to.</dl>
<h3>Address object fields</h3>
<dl>
<dt>family</p>
<dd><i>(string)</i> Currently only &quot;INET&quot; or &quot;INET6&quot;. More types will be added in the future (without considering it a format change).</p>
<dt>address</p>
<dd><i>(string)</i> Address formatted for user consumption. May include net mask. This field should be generally machine parseable.</p>
<dt>peer</p>
<dd><i>(object)</i> If present, the peer address corresponding to this address. It&#8217;s of the address object type but cannot contain futher peer field. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-plotnetcfg/">plotnetcfg</a></code>(8) </p>
<h2>Author</h2>
<p><code>plotnetcfg</code> was written and is maintained by Jiri Benc &lt;jbenc [at] redhat.com&gt;.</p>
