---
title: "mip6d(5)"
name: "mip6d"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mip6d/"
description: "mip6d.conf – MIPL Mobile IPv6 Configuration file"
---

<p>mip6d.conf &#8211; MIPL Mobile IPv6 Configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/mip6d.conf</code> </p>
<h2>Description</h2>
<p>MIPL Mobile IPv6 daemon&#8217;s configuration file Below is a list of currently supported configuration options. All configuration lines are terminated with a semicolon. Sub-sections are enclosed in &#8216;{&#8216; and &#8216;}&#8217;. Strings are quoted with double quotes. </p>
<h2>Common Options</h2>
<p>The file contains the following common definitions:</p>
<dl>
<dt><code>NodeConfig </code>CN | HA | MN<code>;</code></p>
<dd>Indicates if the daemon should run in Correspondent Node, Home Agent or Mobile Node mode. </p>
<p> Default: CN </p>
<dt><code>DebugLevel </code>number<code>;</code></p>
<dd>Indicates the debug level of the daemon. If the value is greater than zero, the daemon will not detach from tty (i.e. debug messages will be printed on the controlling tty). </p>
<p> Default: 0 </p>
<dt><code>DoRouteOptimizationCN </code>boolean<code>;</code></p>
<dd>Indicates if a node should participate in route optimization with a Mobile Node. </p>
<p> Default: enabled </p>
<dt><code>NonVolatileBindingCache </code>boolean<code>;</code></p>
<dd>This option is currently ignored. Binding cache is always stored in volatile memory, and is not retained between shutdown and startup. </p>
</dl>
<h2>Options Common To Home Agent And Mobile Node</h2>
<dl>
<dt>These options are used both in the Home Agent and Mobile Node:</p>
<dd>
<dt><code>Interface </code>name<code>;</code></p>
<dd>
<dt>
<pre><dd><code>Interface </code>name<code> {</code>
<code> MnIfPreference </code>number<code>;</code>
<code> IfType </code>CN | HA | MN<code>;</code>
<code>}</code></pre>
<p>Specifies an interface and options associated with it. If no options are present, <code>Interface</code> can be terminated with semi-colon. This is used for home agent to specify which interfaces are used for HA operation. For the home agent to function properly, a Router Advertisement daemon (e.g. radvd) must broadcast advertisements with the Home Agent bit and Home Agent Information Option set on these interfaces. This option is also used by multihomed Mobile Nodes to define which interfaces are used by it. </p>
<p> <code>MnIfPreference</code> sets the interface preference value for an interface in a multi-homed Mobile Node. The most preferred intefaces have preference 1, the second most preferred have 2, etc. A preference of zero means the interface will not be used. </p>
<p> Default: 5 </p>
<p> <code>IfType</code> overrides the default node behavior for this interface. If a MN doesn&#8217;t wish to use this inteface for mobility, or a node doesn&#8217;t act as HA on this interface, the interface type should be set to CN. </p>
<p> Default: same as <code>NodeConfig</code> </p>
<dt><code>UseMnHaIPsec </code>boolean<code>;</code></p>
<dd>Indicates if the MN-HA MIPv6 signalling should be protected with IPsec. </p>
<p> Default: enabled </p>
<dt><code>KeyMngMobCapability </code>boolean<code>;</code></p>
<dd>If dynamic keying with MIPv6-aware IKE is used, this options should be enabled. It turns on the K-bit for binding updates and binding acknowledgements. </p>
<p> Default: disabled </p>
<dt>
<pre><dd><code>IPsecPolicySet {</code>
<code> HomeAgentAddress </code>address<code>;</code>
<code> HomeAddress </code>address/length<code>;</code>
<code> IPsecPolicy ...</code>
<code> ...</code>
<code>}</code></pre>
<p><code>IPsecPolicySet</code> is a set of policies to apply for matching packets. A policy set can contain multiple <code>HomeAddress</code> options, but only one <code>HomeAgentAddress</code> option. For home agent, home agent address field contains its own address, and home address fields may contain any number of mobile nodes for which the same policy applies. </p>
<p> <code>IPsecPolicy</code> has the following format: </p>
<dt><code>IPsecPolicy </code>type <code>UseESP</code>number number<code>;</code></p>
<dd>Field <code>type </code> can be one of HomeRegBinding, Mh, MobPfxDisc, ICMP, any, TunnelMh, TunnelHomeTesting, or TunnelPayload. The any option protects all transport mode communication between the MN and HA. Currently only the ESP IPsec protocol is supported, but in the future AH and IPComp might also be available. The two remaining numeric fields are the IPsec reqid values, the first one used for MN &#8211; HA, the second one for HA &#8211; MN communication. If just one value is defined, the same reqid will be used in both directions. If no reqid is given, reqid will not be used. </p>
<p> If more that one IPsec transport mode or tunnel mode policy is defined between the MN and HA in each direction, reqid can be used to provide an unambiguous one-to-one mapping between IPsec policies and SAs. Otherwise the policies will just share a common SA. </p>
</dl>
<h2>Home Agent Specific Options</h2>
<p>The following definitions are ignored unless the node is configured as a HA: </p>
<dl>
<dt><code>HaMaxBindingLife </code>number<code>;</code></p>
<dd>Limits the maximum lifetime (in seconds) for Mobile Node home registrations. </p>
<p> Default: 262140 </p>
<dt><code>SendMobPfxAdvs </code>boolean<code>;</code></p>
<dd>Controls whether home agent sends Mobile Prefix Advertisements to mobile nodes in foreign networks. </p>
<dt><code>SendUnsolMobPfxAdvs </code>boolean<code>;</code></p>
<dd>Controls whether home agent send unsolicited Mobile Prefix Advertisements to mobile nodes in foreign networks. </p>
<dt><code>MinMobPfxAdvInterval </code>number<code>;</code></p>
<dd>Sets a minimum interval (in seconds) for Mobile Prefix Advertisements. </p>
<p> Default: 600 </p>
<dt><code>MaxMobPfxAdvInterval </code>number<code>;</code></p>
<dd>Sets a maximum interval (in seconds) for Mobile Prefix Advertisements. </p>
<p> Default: 86400 </p>
<dt><code>BindingAclPolicy </code>address <code>allow | deny</code></p>
<dd>Defines if a MN is allowed to register with the HA or not. The MN home address of the MN is given in the address field.&quot; </p>
<dt><code>DefaultBindingAclPolicy allow | deny</code></p>
<dd>Defines the default policy if no matching BindingAclPolicy entry is found for a MN. </p>
<p> Default: allow </p>
</dl>
<h2>Mobile Node Specific Options</h2>
<p>The following definitions are ignored unless the node is configured as a MN: </p>
<dl>
<dt><code>MnMaxHaBindingLife </code>number<code>;</code></p>
<dd>Limits the maximum lifetime (in seconds) for Mobile Node home registrations. </p>
<p> Default: 262140 </p>
<dt><code>MnMaxCnBindingLife </code>number<code>;</code></p>
<dd>Limits the maximum lifetime (in seconds) for Mobile Node Correspondent Node registrations. </p>
<p> Default: 420 </p>
<dt><code>MnDiscardHaParamProb </code>boolean<code>;</code></p>
<dd>Toggles if the Mobile Node should discard ICMPv6 Parameter Problem messages from its Home Agent. As the ICMPv6 error messages won&#8217;t normally be protected by IPsec, a malicious third party can quite easily impersonate the HA to the MN. Having the MN accept these messages therefore leaves it open to Denial of Service attacks, even though its home registration signalling is protected by IPsec. </p>
<p> Default: disabled </p>
<dt><code>SendMobPfxSols </code>boolean<code>;</code></p>
<dd>Controls whether mobile node sends Mobile Prefix Solicitations to the home network. </p>
<dt><code>DoRouteOptimizationMN </code>boolean<code>;</code></p>
<dd>Indicates if the Mobile Node should initialize route optimization with Corresponent Nodes. </p>
<p> Default: enabled </p>
<dt><code>MnUseAllInterfaces enabled | disabled</code></p>
<dd>Indicates if all interfaces should be used for mobility. The preference of these interfaces is always 1. Unless you use dynamically created and named network interfaces you should normally disable this option and use <code>Interface</code> options to explicitly list the used interfaces. </p>
<p> Default: disabled </p>
<dt><code>UseCnBuAck </code>boolean<code>;</code></p>
<dd>Indicates if the Acknowledge bit should be set in Binding Updates sent to Corresponent Nodes. </p>
<p> Default: disabled </p>
<dt><code>MnRouterProbes </code>number<code>;</code></p>
<dd>Indicates how many times the MN should send Neighbor Unreachability Detection probes to its old router after receiving a Router Advertisement from a new one. If the option is set to zero, the MN will move to the new router straight away. </p>
<p> Default: 0 </p>
<dt><code>MnRouterProbeTimeout </code>decimal<code>;</code></p>
<dd>Indicates how long (in seconds) the MN should wait for a reply during a access router Neighbor Unreachability Detection probe. If set, it overrides any default Neighbor Solicitation Retransmit Timer value greater than MnRouterProbeTimeout. For example, if the interface Retransmit Timer is 1 second, but MnRouterProbeTimeout is just 0.2 seconds, the MN will only wait 0.2 seconds for a Neighbor Advertisement before proceeding with the handoff. </p>
<p> Default: 0 </p>
<dt><code>OptimisticHandoff enabled | disabled</code></p>
<dd>When a Mobile Node sends a Binding Update to the Home Agent, no Route Optimized or reverse tunneled traffic is sent until a Binding Acknowledgement is received. When enabled, this option allows the Mobile Node to assume that the binding was successful right after the BU has been sent, and does not wait for a positive acknowledgement before using RO or reverse tunneling. </p>
<p> Default: disabled; </p>
<dt>
<pre><dd><code>MnHomeLink </code>name <code>{</code>
<code> HomeAddress </code>address/length<code>;</code>
<code> HomeAgentAddress </code>address<code>;</code>
<code> MnRoPolicy ...</code>
<code> ...</code>
<code>}</code></pre>
<p>Each <code>MnHomeLink </code> definition has a name. This is the name (enclosed in double quotes) of the interface used for connecting to the physical home link. To set up multiple Home Addresses on the Mobile Node, you need to define multiple <code>MnHomeLink</code> structures. The interface names don&#8217;t have to be unique in these definitions. All the home link specific definitions are detailed below: </p>
<dt><code>HomeAddress </code>address/length<code>;</code></p>
<dd>Address is an IPv6 address, and length the prefix length of the address, usually 64. This option must be included in a home link definition. </p>
<dt><code>HomeAgentAddress </code>address<code>;</code></p>
<dd>Address is the IPv6 address of the Mobile Node&#8217;s Home Agent. DHAAD is used if it is the unspecified address ::. </p>
<p> Default: :: </p>
<dt>The route optimization policies are of the form:</p>
<dd>
<dt><code>MnRoPolicy </code>address boolean<code>;</code></p>
<dd>Any number of these policies may be defined. If no policies are defined default behavior depends on the <code>DoRouteOptimizationMN</code> option. </p>
<p> The fields for a route optimization policy entry are as follows: <code>address</code> defines the Correspondent Node this policy applies to, if left undefined the uspecified address is used as a wildcard value <code>boolean</code> sets route optimization either enabled or disabled for packets matching this entry. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>A Correspondent Node example:</code></p>
<dd>
<pre>NodeConfig CN;
DoRouteOptimizationCN enabled;</pre>
<dt><code>A Home Agent example:</code></p>
<dd>
<pre>NodeConfig HA;
Interface &quot;eth0&quot;;
Interface &quot;eth1&quot;;
UseMnHaIPsec enabled;
IPsecPolicySet {
 HomeAgentAddress 3ffe:2620:6:1::1;
 HomeAddress 3ffe:2620:6:1::1234/64;
 HomeAddress 3ffe:2620:6:1::1235/64;
 IPsecPolicy HomeRegBinding UseESP;
 IPsecPolicy TunnelMh UseESP;
}</pre>
<dt><code>A Mobile Node example:</code></p>
<dd>
<pre>NodeConfig MN;
DoRouteOptimizationCN enabled;
DoRouteOptimizationMN enabled;
UseCnBuAck enabled;
MnHomeLink &quot;eth0&quot; {
 HomeAgentAddress 3ffe:2620:6:1::1;
 HomeAddress 3ffe:2620:6:1::1234/64;
 # address opt.
 #MnRoPolicy 3ffe:2060:6:1::3 enabled;
 #MnRoPolicy disabled;
}
UseMnHaIPsec enabled;
IPsecPolicySet {
 HomeAgentAddress 3ffe:2620:6:1::1;
 HomeAddress 3ffe:2620:6:1::1234/64;
 IPsecPolicy HomeRegBinding UseESP;
 IPsecPolicy TunnelMh UseESP;
}</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mip6d/">mip6d</a></code>(1), <code><a href="/docs/linux/man/7-mipv6/">mipv6</a></code>(7), RFC3775: Mobility Support in IPv6, RFC3776: Using IPsec to Protect Mobile IPv6 Signaling Between Mobile Nodes and Home Agents </p>
