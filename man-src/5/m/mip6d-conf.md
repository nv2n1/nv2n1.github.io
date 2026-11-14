---
title: "mip6d-conf(5)"
name: "mip6d-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mip6d-conf/"
description: "mip6d.conf – UMIP Mobile IPv6 and NEMO Configuration file"
---

<p>mip6d.conf &#8211; UMIP Mobile IPv6 and NEMO Configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/mip6d.conf</code> </p>
<h2>Description</h2>
<p>UMIP Mobile IPv6 and NEMO daemon&#8217;s configuration file Below is a list of currently supported configuration options. All configuration lines are terminated with a semicolon. Sub-sections are enclosed in &#8216;{&#8216; and &#8216;}&#8217;. Optional parameters are designated with square brackets (you must omit them if you set the optional parameter). Strings are quoted with double quotes. Default value is given when available. Support for dynamic reload of the option through SIGHUP is also indicated. </p>
<h2>Common Options</h2>
<p>The file contains the following common definitions:</p>
<dl>
<dt><code>include </code>&quot;&lt;pattern&gt;&quot;</p>
<dd>Includes content from other files based on provided pattern. Usual shell wildcards are supported (&#8216;?&#8217;, &#8216;*&#8217;, &#8216;[&#8216;). See man (7) glob for details. The number of included files is virtually unlimited but only five levels of recursion are authorized to prevent loops. Note that if given pattern does not match any file, a simple warning is issued but parsing continues. Unlike most configuration statements, no &#8216;;&#8217; is expected after the pattern. </p>
<p> Example: include &quot;/etc/mip6d.conf.d/*.conf&quot; </p>
<dt><code>NodeConfig </code>CN | HA | MN<code>;</code></p>
<dd>Indicates if the daemon should run in Correspondent Node, Home Agent or Mobile Node mode. </p>
<p> Default: CN </p>
<p> Dynamic reload: not supported. Daemon must be restarted. </p>
<dt><code>DebugLevel </code>number<code>;</code></p>
<dd>Indicates the debug level of the daemon. If the value is greater than zero, the daemon will not detach from tty (i.e. debug messages will be printed on the controlling tty). </p>
<p> Default: 0 </p>
<p> Dynamic reload: partially supported. Cannot detach from tty afterwards. </p>
<dt><code>DebugLogFile </code>&quot;/path/to/log/file&quot;<code>;</code></p>
<dd>Indicates where debug logs should be stored. </p>
<p> Default: empty (output is redirected to stderr) </p>
<p> Dynamic reload: not supported. Daemon must be restarted. </p>
<dt><code>DoRouteOptimizationCN </code>boolean<code>;</code></p>
<dd>Indicates if a node should participate in route optimization with a Mobile Node, i.e. if it should accept a binding proposed by a peer. The value is used as the default binding policy value, if no <code>CnBindingPolicySet</code> have been defined for the proposed binding. </p>
<p> Default: enabled </p>
<p> Dynamic reload: supported but does not affect existing bindings. </p>
<dt>
<pre><dd><code>CnBindingPolicySet {</code>
<code> peer_hoa </code>[ local_addr ] <code>boolean</code>;
<code> ... </code>
<code>}</code></pre>
<p>The decision to accept a binding from a MN and participate in route optimization with it is governed on a global basis by <code>DoRouteOptimizationCN</code> parameter, i.e. which is used as the default binding policy value. </p>
<p> The <code>CnBindingPolicySet</code> section can be used to define specific binding policies for some given peers. In that context, each line is dedicated to a MN. The address (HoA) of the MN is given as first element of the line (i.e. <code>peer_hoa</code> ). The local address <code>local_addr</code> at which the Binding Update messages are expected to be received can be optionally specified as second argument (If we are acting as a MN, this will be one of our HoA). If it is not provided, the local address to which the BU from that MN are sent is not taken into account. The last argument <code>boolean</code> specifies if the node should perform route optimization with that peer. </p>
<p> Note that a MN must have at most a single entry defined in that section i.e. having more than one line starting with the same address is not allowed. </p>
<p> Default: by default, the set is empty and the default value provided by <code>DoRouteOptimizationCN</code> configuration parameter applies for all peers. </p>
<p> Dynamic reload: not supported. </p>
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
<code> Tunnel </code>boolean<code>;</code>
<code>}</code></pre>
<p>Specifies an interface and options associated with it. If no options are present, <code>Interface</code> can be terminated with semi-colon. This is used for home agent to specify which interfaces are used for HA operation. For the home agent to function properly, a Router Advertisement daemon (e.g. radvd) must broadcast advertisements with the Home Agent bit and Home Agent Information Option set on these interfaces. This option is also used by multihomed Mobile Nodes to define which interfaces are used by it. For MN and CN, it is posible to provide interfaces that are not already available when the daemon is started. Those will be used when available. </p>
<p> Dynamic reload: partially supported. Only new inet6 interfaces will use the new configuration. </p>
<p> <code>MnIfPreference</code> sets the interface preference value for an interface in a multi-homed Mobile Node. The most preferred interfaces have preference 1, the second most preferred have 2, etc. Values between 0 and 10 are allowed. A preference of zero means the interface will not be used. </p>
<p> The interface preference has a direct impact on the metric of default routes configured by the daemon from RA information. Note that if two interfaces with associated default routes have the same preference value, the routes will end up having the same metric, except if different default router preference (RFC 4191) values are provided in RA. In a sense, MnIfPreference value value is the primary selector for interface and default route selection and default router preference value provided in RA can then be used to break a tie. </p>
<p> Default: 10 </p>
<p> <code>IfType</code> overrides the default node behavior for this interface. If a MN doesn&#8217;t wish to use this interface for mobility, or a node doesn&#8217;t act as HA on this interface, the interface type should be set to CN. </p>
<p> Default: same as <code>NodeConfig</code> </p>
<p> <code>Tunnel</code> </p>
<p> When enabled, this flag explicitly marks the interface as a tunnel interface and modify the behavior of UMIP regarding the router discovery, address configuration and route addition steps for the interface. Those are expected to be done externally (manually or by another automatic process (for instance when using a Teredo interface). Note that the handling of routing via the interface is still partly handled by UMIP but leaves some latitude to the user or the automatic process that setup the interface. UMIP looks for default routes in the main table that use the interface as output device and replaces them by a default route with a proper preference. If a gateway was present for the route (there is one for 6to4, but none when miredo is used), it is kept in the new route. Other routes that are defined for the device (including other default routes in other tables) are left untouched. </p>
<p> Limitations and details: </p>
<p> 1) Tunnel interfaces are only allowed for MN and CN (not HA). </p>
<p> 2) They are never considered as home link (i.e. you will never be at home on a tunnel). </p>
<p> 3) Unlike for physical interfaces, link detection is not reliable for tunnel interfaces. If the tunnel interface state is directly dependent of some physical interface link status, that status must be monitored externally (i.e. not by UMIP) and reflected by having either the interface being set down/up or address being removed/added for UMIP to detect the change in interface configuration. </p>
<p> 4) An address must be configured on the interface for it to be selected. If no adress is available, UMIP will simply not consider the interface at all (even if it provides a default route). </p>
<p> 5) Routes that include specific sources are not considered by UMIP. </p>
<p> Example: </p>
<p> When using a teredo interface, the default route through the teredo device is found and its preference changed. Link local routes are kept unchanged. Address configuration is kept unmodified. </p>
<p> When using a 6to4 tunnel interface, a default route through the 6to4 device exists. It uses the 6to4 relay address (::192.88.99.1 anycast address or another specific one) as gateway. UMIP finds this default route and install a new default one with the same gateway but an updated metric. </p>
<p> Default: disabled </p>
<dt><code>UseMnHaIPsec </code>boolean<code>;</code></p>
<dd>Indicates if the MN-HA MIPv6 signalling should be protected with IPsec. </p>
<p> Default: enabled </p>
<p> Dynamic reload: not supported. </p>
<dt><code>KeyMngMobCapability </code>boolean<code>;</code></p>
<dd>If dynamic keying with MIPv6-aware IKE is used, this options should be enabled. It turns on the K-bit for binding updates and binding acknowledgements. </p>
<p> Default: disabled </p>
<p> Dynamic reload: supported. </p>
<dt>
<pre><dd><code>IPsecPolicySet {</code>
<code> HomeAgentAddress </code>address<code>;</code>
<code> HomeAddress </code>address/length<code>;</code>
<code> IPsecPolicy ...</code>
<code> ...</code>
<code>}</code></pre>
<p><code>IPsecPolicySet</code> is a set of policies to apply for matching packets. A policy set can contain multiple <code>HomeAddress</code> options, but only one <code>HomeAgentAddress</code> option. For home agent, home agent address field contains its own address, and home address fields may contain any number of mobile nodes for which the same policy applies. </p>
<p> Dynamic reload: supported. The sets can be changed, added or removed. Removing rules for established bindings may have unpredicted effects. </p>
<p> <code>IPsecPolicy</code> has the following format: </p>
<dt><code>IPsecPolicy </code>type <code>UseESP </code>number number<code>;</code></p>
<dd>Field <code>type </code> can be one of <code>HomeRegBinding</code> (for protecting BU/BH), <code>Mh</code> (for protecting all MH packets: BU, BA, BE), <code>MobPfxDisc</code> (for protecting MPS/MPA), <code>ICMP</code> (for protecting all ICMP packets, including MPS/MPA), <code>any</code> (for protecting all transport mode communication), <code>TunnelHomeTesting</code> (for protecting the HoTI/HoT messages), <code>TunnelMh</code> (for protecting all tunneled MH packets, including HoTI/HoT), or <code>TunnelPayload</code> (for protecting all tunneled packets including tunneled MH packets). </p>
<p> Currently only the ESP IPsec protocol is supported, but in the future AH and IPComp might also be available. The two remaining numeric fields are the IPsec reqid values, the first one used for MN &#8211; HA, the second one for HA &#8211; MN communication. If just one value is defined, the same reqid will be used in both directions. If no reqid is given, reqid will not be used. </p>
<p> If more that one IPsec transport mode or tunnel mode policy is defined between the MN and HA in each direction, reqid can be used to provide an unambiguous one-to-one mapping between IPsec policies and SAs. Otherwise the policies will just share a common SA. </p>
</dl>
<h2>Home Agent Specific Options</h2>
<p>The following definitions are ignored unless the node is configured as a HA: </p>
<dl>
<dt><code>HaMaxBindingLife </code>number<code>;</code></p>
<dd>Limits the maximum lifetime (in seconds) for Mobile Node home registrations. </p>
<p> Default: 262140 </p>
<p> Dynamic reload: partially supported. Only affects new bindings. </p>
<dt><code>SendMobPfxAdvs </code>boolean<code>;</code></p>
<dd>Controls whether home agent sends Mobile Prefix Advertisements to mobile nodes in foreign networks. </p>
<p> Default: enabled </p>
<p> Dynamic reload: partially supported. Only affects new bindings. </p>
<dt><code>SendUnsolMobPfxAdvs </code>boolean<code>;</code></p>
<dd>Controls whether home agent send unsolicited Mobile Prefix Advertisements to mobile nodes in foreign networks. </p>
<p> Default: enabled </p>
<p> Dynamic reload: partially supported. Only affects new bindings. </p>
<dt><code>MinMobPfxAdvInterval </code>number<code>;</code></p>
<dd>Sets a minimum interval (in seconds) for Mobile Prefix Advertisements. </p>
<p> Default: 600 </p>
<p> Dynamic reload: partially supported. Only affects new scheduled MPA. </p>
<dt><code>MaxMobPfxAdvInterval </code>number<code>;</code></p>
<dd>Sets a maximum interval (in seconds) for Mobile Prefix Advertisements. </p>
<p> Default: 86400 </p>
<p> Dynamic reload: Partially supported. Only affects new scheduled MPA. </p>
<dt><code>HaAcceptMobRtr </code>enabled | disabled<code>;</code></p>
<dd>Indicates if the HA accepts Mobile Router bindings. </p>
<p> Default: disabled </p>
<p> Dynamic reload: supported. </p>
<dt><code>HaServedPrefix </code>prefix/length<code>;</code></p>
<dd>Prefix is an IPv6 prefix and length is the prefix length. Defines the whole aggregated or extended prefix the HA serves. This option is only used for MR bindings and is only needed if the MRs derive their Home Addresses from their Mobile Network Prefixes, instead of one of the home link prefixes. </p>
<p> Dynamic reload: supported. </p>
<dt><code>BindingAclPolicy </code>address <code>[ MNP-list ] </code>allow | deny<code>;</code></p>
<dd>Defines if a MN is allowed to register with the HA or not. The home address of the MN is given in the address field. The mobile network prefixes belonging a NEMO Mobile Router are optionally listed in <code>MNP-list</code> for example: <code>(3ffe:2620:6:3::/64, 3ffe:2620:6:4::/64)</code> </p>
<p> Dynamic reload: partially supported. Does not affect existing bindings until they expire. </p>
<dt><code>DefaultBindingAclPolicy </code>allow | deny<code>;</code></p>
<dd>Defines the default policy if no matching BindingAclPolicy entry is found for a MN. </p>
<p> Default: allow </p>
<p> Dynamic reload: partially supported. Only affects new bindings. </p>
</dl>
<h2>Mobile Node Specific Options</h2>
<p>The following definitions are ignored unless the node is configured as a MN: </p>
<dl>
<dt><code>MnMaxHaBindingLife </code>number<code>;</code></p>
<dd>Limits the maximum lifetime (in seconds) for Mobile Node home registrations. </p>
<p> Default: 262140 </p>
<p> Dynamic reload: partially supported. Only affects new bindings. </p>
<dt><code>MnMaxCnBindingLife </code>number<code>;</code></p>
<dd>Limits the maximum lifetime (in seconds) for Mobile Node Correspondent Node registrations. </p>
<p> Default: 420 </p>
<p> Dynamic reload: partially supported. Only affects new bindings. </p>
<dt><code>MnDiscardHaParamProb </code>boolean<code>;</code></p>
<dd>Toggles if the Mobile Node should discard ICMPv6 Parameter Problem messages from its Home Agent. As the ICMPv6 error messages won&#8217;t normally be protected by IPsec, a malicious third party can quite easily impersonate the HA to the MN. Having the MN accept these messages therefore leaves it open to Denial of Service attacks, even though its home registration signalling is protected by IPsec. </p>
<p> Default: disabled </p>
<p> Dynamic reload: supported. </p>
<dt><code>MnResetDhaadAtHome </code>boolean<code>;</code></p>
<dd>If the MN uses DHAAD, then enabling this option will force UMIP to set the Home Agent Address to the unspecified address every time the MN returns home. As a consequence, the MN will run DHAAD every time it moves from home to a foreign network. If disabled, the HA address obtained from the very first DHAAD exchange will be remembered even if the MN returns home. </p>
<p> Default: disabled </p>
<p> Dynamic reload: supported. </p>
<dt><code>MnFlushAllAtHome </code>boolean<code>;</code></p>
<dd>Enabling this option allows the MN to flush all uncertain registrations upon returning home, instead of keeping trying to complete them from home until the retry counters expire. Also, this option forces the returning home procedure for valid registrations in the case the HA does not reply to DAD probe when returning home. </p>
<p> Default: disabled </p>
<p> Dynamic reload: supported. </p>
<dt><code>MnMaxCnConsecutiveResends </code>number<code>;</code></p>
<dd>By default, if the MN does not receives a BA from a CN, it resends the BU indefinitely. Setting this option to 1 or more allows to stop trying after the specified number. 1 resend is the minimum, as 0 is a reserved value to indicate that resend should be performed indefinitely. </p>
<p> Default: 0 (resend indefinitely) </p>
<p> Dynamic reload: supported. </p>
<dt><code>MnMaxHaConsecutiveResends </code>number<code>;</code></p>
<dd>By default, if the MN learnt the HA address through DHAAD and did not receive a BA from a HA after 5 retries, it invalidates the HA and tries to switch to another HA. This option allows to tune the number of retry before switching. Note that if DHAAD is not used, this option has no effect, and the MN retries sending the BU indefinitely. </p>
<p> Default: 5 </p>
<p> Dynamic reload: supported. </p>
<dt><code>SendMobPfxSols </code>boolean<code>;</code></p>
<dd>Controls whether mobile node sends Mobile Prefix Solicitations to the home network. </p>
<p> Default: enabled </p>
<p> Dynamic reload: supported. </p>
<dt><code>DoRouteOptimizationMN </code>boolean<code>;</code></p>
<dd>Indicates if the Mobile Node should initialize route optimization with Correspondent Nodes. </p>
<p> Default: enabled </p>
<p> Dynamic reload: partially supported, disabling is not supported. </p>
<dt><code>MnUseAllInterfaces </code>enabled | disabled<code>;</code></p>
<dd>Indicates if all interfaces should be used for mobility. The preference of these interfaces is always 1. Unless you use dynamically created and named network interfaces you should normally disable this option and use <code>Interface</code> options to explicitly list the used interfaces. </p>
<p> Default: disabled </p>
<p> Dynamic reload: same support as &quot;Interface&quot; directive. </p>
<dt><code>MobRtrUseExplicitMode </code>enabled | disabled<code>;</code></p>
<dd>Toggles between explicit or implicit mode home registrations in the MR. </p>
<p> Default: enabled </p>
<p> Dynamic reload: supported. </p>
<dt><code>UseCnBuAck </code>boolean<code>;</code></p>
<dd>Indicates if the Acknowledge bit should be set in Binding Updates sent to Correspondent Nodes. </p>
<p> Default: disabled </p>
<p> Dynamic reload: supported. </p>
<dt><code>InterfaceInitialInitDelay </code>decimal<code>;</code></p>
<dd>Defines the delay (in seconds) for initial interface configuration at startup before any movement decision occurs. </p>
<p> At startup, UMIP gathers information on interfaces available on the system. Then, for interfaces listed in the configuration, it either learn CoA (for those marked as <code>Tunnel</code>) or send RS to receive RA (asynchronously) and then configured CoA. </p>
<p> At startup, if the MN has multiple interfaces, UMIP may first select a CoA on a given interface and then change its mind and switch to another CoA. This may result in the emission of multiple useless BU. Additionally, when Dynamic Keying (IKE) is used for negotiating protection of traffic, a CoA change occurring during the initial negotiation only leads to additional delays. </p>
<p> By introducing an initial default delay at startup, that side effect is avoided. If your MN is configured to use only a single interface, or do not use IKE and startup delay matters, you may set the parameter to 0. </p>
<p> Default: 2.0 </p>
<p> Dynamic reload: not supported (only valid at daemon startup). </p>
<dt><code>MnRouterProbes </code>number<code>;</code></p>
<dd>Indicates how many times the MN should send Neighbor Unreachability Detection (NUD) probes to its old router after receiving a Router Advertisement (RA) from a new one. If the option is set to zero or the new router advertises a strictly higher default preference value than the old one (as defined in RFC 4191), the MN will move to the new router straight away. </p>
<p> Default: 0 </p>
<p> Dynamic reload: supported. </p>
<dt><code>MnRouterProbeTimeout </code>decimal<code>;</code></p>
<dd>Indicates how long (in seconds) the MN should wait for a reply during a access router Neighbor Unreachability Detection probe. If set, it overrides any default Neighbor Solicitation Retransmit Timer value greater than MnRouterProbeTimeout. For example, if the interface Retransmit Timer is 1 second, but MnRouterProbeTimeout is just 0.2 seconds, the MN will only wait 0.2 seconds for a Neighbor Advertisement before proceeding with the handoff. </p>
<p> Default: 0.0 </p>
<p> Dynamic reload: supported. </p>
<dt><code>InitialBindackTimeoutFirstReg </code>decimal<code>;</code></p>
<dd>Upon the first registration attempt, indicates how long (in seconds) the MN should wait before re-sending the Binding Update when no Binding Ack has been received. For subsequent registrations, you may set the <code>InitialBindackTimeoutReReg</code> option. </p>
<p> Default: 1.5 </p>
<p> Dynamic reload: partially supported. Only affects new bindings. </p>
<dt><code>InitialBindackTimeoutReReg </code>decimal<code>;</code></p>
<dd>Indicates how long (in seconds) the MN should wait before re-sending the Binding Update when no Binding Ack has been received. For the first registration attempt, you may set the <code>InitialBindackTimeoutFirstReg</code> option. </p>
<p> Default: 1.0 </p>
<p> Dynamic reload: partially supported. Does not affect existing bindings until they expire. </p>
<dt><code>InitialSolicitTimer </code>decimal<code>;</code></p>
<dd>Indicates how long (in seconds) the MN should wait before re-sending the initial Mobile Prefix Solitication message when no answers have been received. Option <code>SendMobPfxSols</code> must be enabled. </p>
<p> Default: 3.0 </p>
<p> Dynamic reload: not supported. </p>
<dt><code>OptimisticHandoff </code>enabled | disabled<code>;</code></p>
<dd>When a Mobile Node sends a Binding Update to the Home Agent, no Route Optimized or reverse tunneled traffic is sent until a Binding Acknowledgement is received. When enabled, this option allows the Mobile Node to assume that the binding was successful right after the BU has been sent, and does not wait for a positive acknowledgement before using RO or reverse tunneling. </p>
<p> Default: disabled </p>
<p> Dynamic reload: supported. </p>
<dt><code>NoHomeReturn </code>enabled | disabled<code>;</code></p>
<dd>When a MN returns Home, it usually deregisters its binding. Additionally, when IPsec is in use to protect data traffic, a MN also deinstall the IPsec Security Policies protecting data traffic. One problem with that expected behavior is that an insecure trigger (Home Link Detection mechanism, based on prefix announced in RA messages) is used for the removal of IPsec Security Policies for data traffic. </p>
<p> The <code>NoHomeReturn</code> option can be used to change that behavior. When enabled, the MN will never consider itself at home. That way, if IPsec is used to protect data traffic, associated Security Policies will never be removed. </p>
<p> Note that for the option to work when the MN really returns home (i.e. on the subnet where the Home Agent is defending MN&#8217;s HoA), the two following conditions must be met: </p>
<p> 1) The HoA of the MN must be different from the CoA the MN will automatically configure itself on its interface that connects to its home network, </p>
<p> 2) The interface that connects to the home subnet must not be the <code>MnHomeLink</code> interface (because the MN configures its HoA on that interface, which will in turn make DAD fail on the HA for the HoA). </p>
<p> Default: disabled </p>
<p> Dynamic reload: supported (for the next home return). </p>
<dt>
<pre><dd><code>MnHomeLink </code>name <code>{</code>
<code> HomeAddress </code>address/length <code>[ MNP-list ]</code>;
<code> HomeAgentAddress </code>address<code>;</code>
<code> MnRoPolicy ...</code>
<code> ...</code>
<code>}</code></pre>
<p>Each <code>MnHomeLink </code> definition has a name. This is the name (enclosed in double quotes) of the interface used for connecting to the physical home link. To set up multiple Home Addresses on the Mobile Node, you need to define multiple <code>MnHomeLink</code> structures. The interface names don&#8217;t have to be unique in these definitions. </p>
<p> Dynamic reload: not supported. The daemon has to be restarted for the changes in this directive to take effect. </p>
<p> All the home link specific definitions are detailed below: </p>
<dt><code>HomeAddress </code>address/length <code>[ MNP-list ]</code>;</p>
<dd>Address is an IPv6 address, and length the prefix length of the address, usually 64. The MNP-list contains the mobile network prefixes belonging to that particular NEMO Mobile Router. The MNP-list is optional and is of the same format as in <code>BindingAclPolicy.</code> This option must be included in a home link definition. </p>
<dt><code>HomeAgentAddress </code>address<code>;</code></p>
<dd>Address is the IPv6 address of the Mobile Node&#8217;s Home Agent. DHAAD is used if it is the unspecified address ::. </p>
<p> Default: :: </p>
<dt><code>IsMobRtr </code>enabled | disabled<code>;</code></p>
<dd>Defines if the MN is a NEMO MR. </p>
<p> Default: disabled </p>
<dt>The route optimization policies are of the form:</p>
<dd>
<dt><code>MnRoPolicy </code>address boolean<code>;</code></p>
<dd>Any number of these policies may be defined. If no policies are defined default behavior depends on the <code>DoRouteOptimizationMN</code> option. </p>
<p> The fields for a route optimization policy entry are as follows: <code>address</code> defines the Correspondent Node this policy applies to, if left undefined the uspecified address is used as a wildcard value <code>boolean</code> sets route optimization either enabled or disabled for packets matching this entry. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>A NEMO Home Agent example (without IPsec):</code></p>
<dd>
<pre>NodeConfig HA;
Interface &quot;eth0&quot;;
HaAcceptMobRtr enabled;
HaServedPrefix 3ffe:2620:6::/48;
DefaultBindingAclPolicy deny;
BindingAclPolicy 3ffe:2620:6:1::1234 (3ffe:2620:6:2::/64, 3ffe:2620:6:3::/64) allow;
BindingAclPolicy 3ffe:2620:6:1::1235 allow;
UseMnHaIPsec disabled;</pre>
<dt><code>A NEMO Mobile Router example (without IPsec):</code></p>
<dd>
<pre>NodeConfig MN;
DoRouteOptimizationCN disabled;
DoRouteOptimizationMN disabled;
Interface &quot;eth0&quot;;
MnRouterProbes 1;
MobRtrUseExplicitMode enabled;
MnHomeLink &quot;eth0&quot; {
 IsMobRtr enabled;
 HomeAgentAddress 3ffe:2620:6:1::1;
 HomeAddress 3ffe:2620:6:1::1234/64 (3ffe:2620:6:2::/64, 3ffe:2620:6:3::/64);
}
UseMnHaIPsec disabled;</pre>
<dt><code>A Correspondent Node example (without IPsec):</code></p>
<dd>
<pre>NodeConfig CN;
DoRouteOptimizationCN enabled;</pre>
<dt><code>A Home Agent example (with IPsec static keying):</code></p>
<dd>
<pre>NodeConfig HA;
Interface &quot;eth0&quot;;
BindingAclPolicy 3ffe:2620:6:1::1234 allow;
UseMnHaIPsec enabled;
IPsecPolicySet {
 HomeAgentAddress 3ffe:2620:6:1::1;
 HomeAddress 3ffe:2620:6:1::1234/64;
 # All MH packets (BU/BA/BERR)
 IPsecPolicy Mh UseESP 111 112;
 # All tunneled packets (HoTI/HoT, payload)
 IPsecPolicy TunnelPayload UseESP 113 114;
 # All ICMP packets (MPS/MPA, ICMPv6)
 IPsecPolicy ICMP UseESP 115 116;
}</pre>
<dt><code>A Mobile Node example (with IPsec static keying):</code></p>
<dd>
<pre>NodeConfig MN;
DoRouteOptimizationCN enabled;
# DoRouteOptimizationMN cannot be used 
# with TunnelPayload IPsecPolicy
DoRouteOptimizationMN disabled;
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
 # All MH packets (BU/BA/BERR)
 IPsecPolicy Mh UseESP 111 112;
 # All tunneled packets (HoTI/HoT, payload)
 IPsecPolicy TunnelPayload UseESP 113 114;
 # All ICMP packets (MPS/MPA, ICMPv6)
 IPsecPolicy ICMP UseESP 115 116;
}</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mip6d/">mip6d</a></code>(1), <code><a href="/docs/linux/man/7-mipv6/">mipv6</a></code>(7), RFC6275: Mobility Support in IPv6 RFC3776: Using IPsec to Protect Mobile IPv6 Signaling Between Mobile Nodes and Home Agents RFC4877: Mobile IPv6 Operation with IKEv2 and the Revised IPsec Architecture RFC3963: Network Mobility (NEMO) Basic Support Protocol </p>
