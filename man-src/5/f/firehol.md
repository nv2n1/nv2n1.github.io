---
title: "firehol(5)"
name: "firehol"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firehol/"
description: "firehol.conf – Configuration file for firehol(1)"
---

<p>firehol.conf &#8211; Configuration file for <a href="/docs/linux/man/1-firehol/">firehol</a>(1)</p>
<h2>Description</h2>
<p><i>firehol.conf</i> is the configuration file for <i><a href="/docs/linux/man/1-firehol/">firehol</a></i>(1), which creates an iptables firewall from the simple rules in this file. </p>
<p> This file is parsed as a <i><a href="/docs/linux/man/1-bash/">bash</a></i>(1) script, so it&#8217;s no problem to use variables or complex bashisms.</p>
<h2>Commands</h2>
<h2>interface &lt;real interface&gt; &lt;name&gt; [optional rule parameters]</h2>
<dl>
<dd>The interface command creates a firewall for protecting the host the firewall is running, from the given interface. The default interface policy is drop, so that if no subcommands are given, the firewall will just drop all incoming and outgoing traffic using this interface. </dd>
<p> <i>Parameters</i></p>
<dl>
<dt>* real interface</dt>
<dd>This is the interface name as shown by ip link show. Generally anything iptables accepts, including the pattern character + (the plus sign), is valid. The plus sign after some text will match all interfaces that start with this text. It is allowed to use more than one interfaces separated by spaces, but all of them should be given within one quoted argument. Example:</dd>
<dl>
<dd>
</dd><dl>
<dd>interface &#8220;eth0 eth1 ppp0&#8221; myname</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<dt>* name</dt>
<dd>This is a name for this interface. Generally you should use short names (10 characters max) without spaces or other symbols. You should not use the same name more than once in FireHOL primary commands.</dd>
<dt>* optional rule parameters</dt>
<dd>This is a set of rules that allow further restriction of the traffic that gets matched for this interface. See section <code>Optional Rules Parameters</code> for more information. Examples:</dd>
<dl>
<dd>
</dd><dl>
<dd>interface eth0 intranet src 10.0.0.0/16 </dd>
<p> interface eth0 internet src not &#8220;$UNROUTABLE_IPS&#8221; (note: UNROUTABLE_IPS is a variable defined by FireHOL that includes all IPs that should not be routable by the Internet).</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
</dl>
<dl>
<dd></dd></dl>
<h2>router &lt;name&gt; [optional rule parameters]</h2>
<dl>
<dd>The router command creates a firewall for the traffic passing through the host running the firewall. The only acceptable policy on all router commands is return and therefore the policy subcommand cannot be used on routers. This means that no packets are dropped in a router. Packets not matched by any router command will be dropped at the end of the firewall. </dd>
<p> <i>Parameters</i></p>
<dl>
<dt>* name</dt>
<dd>This is a name for this router. The same restrictions of interface names apply here too.</dd>
<dt>* optional rule parameters</dt>
<dd>This is a set of rules that allow further restriction of the traffic that gets matched for this router. See section <code>Optional Rules Parameters</code> for more information.</dd></dl>
</dl>
<dl>
<dd><i>Description</i> </dd>
<dl>
<dd>Router statements produce similar iptables commands the interface statements produce. For each router statement an in_<i>name</i> and an out_<i>name</i> chain are produced to match the traffic in both directions of the router. </dd>
<p> To match some client or server traffic the administrator has to specify the input/output interface or the source/destination of the request. All inface/outface, src/dst optional rule parameters can be given either on the router statement in which case will be applied to all subcommands for this router, or on each subcommand within a router. Both are valid. </p>
<p> For example: </p>
<dl>
<dd>router mylan inface ppp+ outface eth0<br/>
&nbsp;<wbr>&nbsp;<wbr>server http accept<br/>
&nbsp;<wbr>&nbsp;<wbr>client smtp accept</dd></dl>
</dl>
<dl>
<dd>The above says: Define a router that matches all requests that originate from some PPP interface and go out to eth0. There is an HTTP server in eth0 that client from the PPP interfaces are allowed to reach. Clients on eth0 are allowed to get SMTP traffic from the PPP interfaces. </dd>
<p> While: </p>
<dl>
<dd>router mylan<br/>
&nbsp;<wbr>&nbsp;<wbr>server http accept inface ppp+&nbsp;<wbr>outface eth0<br/>
&nbsp;<wbr>&nbsp;<wbr>server smtp accept inface eth0 outface ppp+</dd></dl>
</dl>
<dl>
<dd>The above says: Define a router that matches any kind of forwarded traffic. For HTTP traffic the clients are on a PPP interface and the servers on eth0. For SMTP traffic the clients are on a eth0 interface and the servers o a PPP interface. </dd>
<p> Please note that in the second example the SMTP traffic is matched again with a server subcommand, not a client (as in the first example). </p>
<p> The client subcommand reverses all the optional rules that are applied indirectly to it. Indirect rule parameters are those that are inherited from the parent command (router in this case). To make it simple, for FireHOL a client is: &#8220;a server with all the implicit optional rule parameters reversed&#8221;. </p>
<p> So, in the first example, the client simply flipped the inface and outface rules defined at the router and became an SMTP server. In the second example there is nothing to be flipped, so server and client are exactly the same. </p>
<p> I suggest to use client subcommands in routers only if you have inface/outface or src/dst in the router statements. If you are building routers like the second example, don&#8217;t use client, it is confusing. </p>
<p> Older versions of FireHOL did not allow server and client subcommands in routers. Only the route subcommand was allowed. Today, route is just an alias for server and can be used only in routers, not interfaces. </p>
<p> Any number of router statements can exist. Since the policy is RETURN on all of them, any traffic not matched by a router will continue to be checked against the second.</dl>
</dl>
<dl>
<dd></dd></dl>
<h2>Subcommands</h2>
<p>Subcommands must be given within Primary commands.</p>
<h2>policy &lt;action&gt;</h2>
<dl>
<dd>The policy subcommand defines the default policy for an interface. </dd>
<p> This directive accepts all the actions specified in the section <code>Actions</code>. </p>
<p> The policy of routers cannot be changed and is always RETURN.</dl>
<h2>protection [reverse] &lt;type&gt;</h2>
<dl>
<dd>The protection subcommand sets a number of protection rules on an interface. </dd>
<p> In router configurations, protections are setup on inface. </p>
<p> <i>Parameters</i></p>
<dl>
<dt>reverse</dt>
<dd>The reverse keyword will make the protections setup on outface.</dd>
<dt>type</dt>
<dd>One of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt>strong, full or all</dt>
<dd>Turns on all known protections</dd>
<dt>fragments</dt>
<dd>Drops all packet fragments. Please note that most probably this rule will never match anything since iptables reconstructs all packets automatically, before the iptables firewall rules are processed, when its connection tracker is running.</dd>
<dt>new-tcp-w/o-syn</dt>
<dd>Drops all TCP packets that initiate a socket but have no the SYN bit set.</dd>
<dt>syn-floods [requests/sec [burst]]</dt>
<dd>Allows only a certain amount of new TCP connections per second. The optional two arguments [requests/sec] and [burst] are used by this rule in order to provide control on the number of connections to be allowed. The default is 100 connections per second that can match 50 (it was 4 in v1.38 and before) packets initially (this is implemented using the limit module of iptables: see man iptables for more). Note that this rule applies to all connections attempted regardless of their final result (rejected, dropped, established, etc). Therefore it might not be a good idea to set it too low.</dd>
<dt>icmp-floods [requests/sec [burst]]</dt>
<dd>Allows only a certain amount of ICMP echo requests per second. The optional two arguments [requests/sec] and [burst] are used by this rule in order to provide control on the number of connections to be allowed. The default is 100 connections per second that can match 50 (it was 4 in v1.38 and before) packets initially (this is implemented using the limit module of iptables: see man iptables for more).</dd>
<dt>malformed-xmas</dt>
<dd>Drops all TCP packets that have all TCP flags set.</dd>
<dt>malformed-null</dt>
<dd>Drops all TCP packets that have all TCP flags unset.</dd>
<dt>malformed-bad</dt>
<dd>Drops all TCP packets that have illegal combinations of TCP flags set.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
</dl>
<dl>
<dd></dd></dl>
<h2>server &lt;service&gt; &lt;action&gt; [optional rule parameters]</h2>
<dl>
<dd>The server subcommand defines a server of a service. For FireHOL a server is the destination of a request, and even if this is more complex for multi-socket services, for FireHOL a server always accepts requests. </dd>
<p> The optional rule parameters given to the parent primary command (interface or router) are inherited by the server as they have been given. </p>
<p> This subcommand can be used on both interfaces and routers. </p>
<p> <i>Parameters</i></p>
<dl>
<dt>service</dt>
<dd>This is one of the supported service names. The command accepts more than one services in the same argument if they are separated by space and quoted as a single argument. Example:</dd>
<dl>
<dd>
</dd><dl>
<dd>server smtp accept </dd>
<p> server &#8220;smtp pop3 imap&#8221; accept</dl>
</dl>
<dl>
<dd></dd></dl>
<dt>action</dt>
<dd>This tells FireHOL what to do with the traffic matching this rule. </dd>
<p> FireHOL supports the actions defined in the section <code>Actions</code>.</p>
<dt>optional rule parameters</dt>
<dd>This is a set of rules that allow further restriction of the traffic that gets matched by this rule. See section <code>Optional Rules Parameters</code> for more information. Examples:</dd>
<dl>
<dd>
</dd><dl>
<dd>server smtp accept src 1.2.3.4 </dd>
<p> server smtp accept log &#8220;its mail&#8221; src 1.2.3.4</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
</dl>
<dl>
<dd></dd></dl>
<h2>client &lt;service&gt; &lt;action&gt; [optional rule parameters]</h2>
<dl>
<dd>The client subcommand defines a client of a service. For FireHOL a client is the source of a request. FireHOL follows this simple rule even on multi-socket complex protocols, so that for FireHOL a client always sends requests. The parameters are exactly the same with the server subcommand. </dd>
<p> The optional rule parameters given to the parent primary command (interface or router) are inherited by the client, but they are reversed. For an explanation of this please refer to the documentation of the router primary command. </p>
<p> This subcommand can be used on both interfaces and routers.</dl>
<h2>route &lt;service&gt; &lt;action&gt; [optional rule parameters]</h2>
<dl>
<dd>The route subcommand is an alias for the server command that can be used only on routers, not interfaces.</dd></dl>
<h2>Helper commands</h2>
<h2>version &lt;number&gt;</h2>
<dl>
<dd>The version command states the FireHOL release the configuration file was created for. In case the configuration file is newer than FireHOL, FireHOL will deny to run it. </dd>
<p> This command is here to allow you or anyone else design and distribute FireHOL configuration files, while ensuring that the correct FireHOL version is going to run them. </p>
<p> The FireHOL release is increased every time the format of the configuration file and the internals of FireHOL are changed. </p>
<p> Since FireHOL v1.67 version is not required to be present in every configuration file.</dl>
<h2>iptables &lt;arguments&gt;</h2>
<dl>
<dd>The iptables command passes all its arguments to the real iptables command, during run-time. </dd>
<p> You should not use /sbin/iptables directly to alter a FireHOL firewall in its configurations. If you do, your commands will be run before FireHOL activates its firewall and while the previous firewall is still running. Also, since FireHOL will delete all previous firewall rules in order to activate the new firewall, any changes you will make, will be deleted too. </p>
<p> Always use the iptables directive to hook iptables commands in a FireHOL firewall. Nothing else.</dl>
<h2>masquerade [reverse | interface] [optional rule parameters]</h2>
<dl>
<dd>Masquerading is a special from of SNAT (Source NAT) that changes the source of requests when they go out and replaces their original source when replies come in. This way a Linux box can become an internet router for a LAN of clients having unroutable IP addresses. Masquerading takes care to re-map IP addresses and ports as required. </dd>
<p> Masquerading is &#8220;expensive&#8221; compared to SNAT because it checks the IP address of the ougoing interface every time for every packet, and therefore it is suggested that if you connect to the internet with a static IP address, to prefer SNAT. </p>
<p> The masquerade helper sets up masquerading on the output of a network interface (not the interface command, but a real network interface). </p>
<p> If the masquerade command is placed within an interface command, its network interface[s] will be used. </p>
<p> If the masquerade command is placed within a router command that has an outface defined, then the outface network interface[s] will be used. </p>
<p> If placed within a router command but the keyword reverse is specified and the router command has an inface defined, then the inface network interface[s] will be used. </p>
<p> If placed outside and before all primary commands, an interface (or list of space separated interfaces, within double quotes) can be specified on the masquerade command. </p>
<p> In all cases, masquerade will setup itself on the output of the given interface[s]. </p>
<p> Please note that if masquerade is used within some interface or router, it does not respect the optional rule parameters given to this interface or router command. Masquerade uses only its own optional rule parameters. </p>
<p> inface and outface should not be given as parameters to masquerade (inface because iptables does not support this in the POSTROUTING chain, and outface because it will be overwritten by the interface(s) mentioned above). </p>
<p> Finally, the masquerade helper will turn on FIREHOL_NAT and instruct the kernel to do packet forwarding (like the router commands do). </p>
<p> Examples: </p>
<dl>
<dd>Before the first interface or router:<br/>
&nbsp;<wbr>&nbsp;<wbr>masquerade eth0 src 10.0.0.0/8 dst not 10.0.0.0/8 </dd>
<p> Within an interface rule to masquerade on the output of this interface:<br/>
&nbsp;<wbr>&nbsp;<wbr>masquerade </p>
<p> Within a router rule to masquerade on the output of the router&#8217;s inface:<br/>
&nbsp;<wbr>&nbsp;<wbr>masquerade reverse</dl>
</dl>
<dl>
<dd></dd></dl>
<h2>transparent_squid &lt;port&gt; &lt;user&gt; [optional rule parameters]</h2>
<dl>
<dd>The transparent_squid helper sets up trasparent caching for HTTP traffic. The squid proxy is assumed to be running on the firewall host at port <i>port</i> (<i>port</i> defaults to squid), with the credentials of the local user <i>user</i> (<i>user</i> defaults to squid). </dd>
<p> The transparent_squid helper can be used for two kinds of traffic:</p>
<dl>
<dt>* Incoming HTTP traffic</dt>
<dd>Incoming HTTP traffic, which is either targeted to the firewall host or passing through the firewall host. </dd>
<p> The optional rule parameters can be used to specify which kind of incoming traffic to be catched (by using inface, src, dst, etc &#8212; outface should not be used here, because the rules generated are placed before the routing decision and therefore the outgoing interface is not yet known). </p>
<p> If no optional rule parameters are given, then the transparent cache will be setup on all network interfaces for all HTTP traffic (use this with care since you are risking to serve requests from the internet using your squid).</p>
<dt>* Locally HTTP traffic</dt>
<dd>Locally generated HTTP traffic except traffic generated by processes running as user <i>user</i>. The optional rule parameters inface, outface and src are ignored for this type of traffic. </dd>
<p> This kind of matching makes it possible to support transparent caching for WEB browsers running on the firewall host, as far as they do not run as the user excluded. More than one users can be specified by space-separating and enclosing them in double quotes. </p>
<p> This rule can be disabled by specifing as user the empty string: &quot;&quot;</dl>
</dl>
<dl>
<dd>Examples: </dd>
<dl>
<dd>transparent_squid 3128 squid inface eth0 src 10.0.0.0/8 </dd>
<p> transparent_squid 8080 &#8220;squid privoxy root bin&#8221; inface not &#8220;ppp+ ipsec+&#8221; dst not &#8220;a.not.proxied.server&#8221;</dl>
</dl>
<dl>
<dd></dd></dl>
<h2>nat &lt;type&gt; &lt;target&gt; [optional rule parameters]</h2>
<dl>
<dd>The nat helper sets up a NAT rule for routed traffic. </dd>
<p> The type parameter can be:</p>
<dl>
<dt>to-source</dt>
<dd>Defines a Source NAT (created in NAT/POSTROUTING). </dd>
<p> The <i>target</i> in this case is the source address to be set in packets matching the optional rule parameters (if no optional rule parameters, all forwarded traffic will be matched). <i>target</i> accepts all &#8211;to-source values iptables accepts (see iptables -j SNAT &#8211;help). Multiple &#8211;to-source values can be given, if separated by space and quoted as a single argument. </p>
<p> inface should not be used in SNAT, because iptables does provide this information at this point.</p>
<dt>to-destination</dt>
<dd>Defines a Destination NAT (created in NAT/PREROUTING). </dd>
<p> The <i>target</i> in this case is the destination address to be set in packets matching the optional rule parameters (if no optional rule parameters, all forwarded traffic will be matched). <i>target</i> accepts all &#8211;to-destination values iptables accepts (see iptables -j DNAT &#8211;help). Multiple &#8211;to-destination values can be given, if separated by space and quoted as a single argument. </p>
<p> outface should not be used in DNAT, because iptables does provide this information at this point.</p>
<dt>redirect-to</dt>
<dd>Catches traffic comming in and send it to the local machine (created in NAT/PREROUTING). </dd>
<p> The <i>target</i> in this case is a port or a range of ports (XXX-YYY) that packets matching the rule will be redirected to (if no optional rule parameters are given, all incomming traffic will be matched). <i>target</i> accepts all &#8211;to-ports values iptables accepts (see iptables -j REDIRECT &#8211;help). </p>
<p> outface should not be used in REDIRECT, because iptables does provide this information at this point.</dl>
</dl>
<dl>
<dd>Please understand that the optional rule parameters are used only to limit the traffic to be matched. Consider these examples:</dd>
<dl>
<dt>Sends to 1.1.1.1 all traffic comming in or passing trhough the firewall host:</dt>
<dd>nat to-destination 1.1.1.1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt>Redirects to 1.1.1.1 all traffic comming in or passing through, and going to 2.2.2.2:</dt>
<dd>
<pre> nat to-destination 1.1.1.1 dst 2.2.2.2</pre>
</dd><dt>Redirects to 1.1.1.1 all TCP traffic comming in or passing through and going to 2.2.2.2:</dt>
<dd>
<pre> nat to-destination 1.1.1.1 proto tcp dst 2.2.2.2</pre>
</dd><dt>Redirects to 1.1.1.1 all traffic comming in or passing through and going to 2.2.2.2 to port tcp/25:</dt>
<dd>
<pre> nat to-destination 1.1.1.1 proto tcp dport 25 dst 2.2.2.2</pre>
</dd></dl>
</dl>
<dl>
<dd>More examples: </dd>
<dl>
<dd>nat to-source 1.1.1.1 outface eth0 src 2.2.2.2 dst 3.3.3.3 </dd>
<p> nat to-destination 4.4.4.4 inface eth0 src 5.5.5.5 dst 6.6.6.6 </p>
<p> nat redirect-to 8080 inface eth0 src 2.2.2.0/24 proto tcp dport 80</dl>
</dl>
<dl>
<dd></dd></dl>
<h2>snat [to] &lt;target&gt; [optional rule parameters]</h2>
<dl>
<dd>The snat helper sets up a Source NAT rule for routed traffic, by calling nat to-source <i>target</i> [optional rule parameters] </dd>
<p> See the nat helper. </p>
<p> Example: </p>
<dl>
<dd>snat to 1.1.1.1 outface eth0 src 2.2.2.2 dst 3.3.3.3</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<h2>dnat [to] &lt;target&gt; [optional rule parameters]</h2>
<dl>
<dd>The dnat helper sets up a Destination NAT rule for routed traffic, by calling nat to-destination <i>target</i> [optional rule parameters] </dd>
<p> See the nat helper. </p>
<p> Example: </p>
<dl>
<dd>dnat to 1.1.1.1 inface eth0 src 2.2.2.2 dst 3.3.3.3</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<h2>redirect [to] &lt;target&gt; [optional rule parameters]</h2>
<dl>
<dd>The redirect helper catches all incomming traffic matching the optional rule parameters given and redirects it to ports on the local host, by calling nat redirect-to <i>target</i> [optional rule parameters] </dd>
<p> See the nat helper. </p>
<p> Example: </p>
<dl>
<dd>nat redirect-to 8080 inface eth0 src 2.2.2.0/24 proto tcp dport 80</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<h2>Actions</h2>
<p>Actions are the actions to be taken on services and traffic described by other commands and functions. Please note that normally, FireHOL will pass-through to the generated iptables statements all the possible actions iptables accepts, but only the ones defined here can be used with lower case letters and currently it will be impossible to pass arguments to some unknown action. Also, keep in mind that the iptables action LOG is a FireHOL optional rule parameter (see log and loglimit) that can be defined together with one of the following actions and FireHOL will actually produce multiple iptables statements to achieve both the logging and the action.</p>
<h2>accept</h2>
<dl>
<dd>accept allows the traffic matching the rules to reach its destination. </dd>
<p> Example: </p>
<dl>
<dd>server smtp accept, to allow SMTP requests and their replies to flow.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<h2>reject [with message]</h2>
<dl>
<dd>reject discards the matching traffic but sends a rejecting message back to the sender. </dd>
<p> with is used to offer control on the message to be returned to the sender. with accepts all the arguments the &#8211;reject-with iptables expression accepts. For an updated list of these messages type iptables -j REJECT &#8211;help. </p>
<p> Examples: </p>
<dl>
<dd>policy reject with host-unreach </dd>
<p> server ident reject with tcp-reset </p>
<p> UNMATCHED_INPUT_POLICY=&#8220;reject with host-prohib&#8221;</dl>
</dl>
<dl>
<dd></dd></dl>
<h2>drop</h2>
<dl>
<dd>drop silently discards the matching traffic. The fact that the traffic is silently discarded makes the sender timeout in order to conclude that it is not possible to use the wanted service. </dd>
<p> Example: </p>
<dl>
<dd>server smtp drop, to silently discard SMTP requests and their replies.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<h2>deny</h2>
<dl>
<dd>deny is just an alias for drop, made for those who are used to ipchains terminology. </dd>
<p> Example: </p>
<dl>
<dd>server smtp deny, to silently discard SMTP requests and their replies.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<h2>return</h2>
<dl>
<dd>return will return the flow of processing to the parent of the current command. Currently, it has meaning to specify the action return only as a policy to some interface. </dd>
<p> Example:</p>
<dl>
<dt>policy return</dt>
<dd>Traffic not matched by any rule within an interface continues traveling through the firewall and is possibly matched by other interfaces bellow.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<h2>mirror</h2>
<dl>
<dd><i>mirror</i> will return the traffic to the wanted port, back to the sending host. Use this with care, and only if you understand what you doing. Keep also in mind that FireHOL will apply this action to both requests and replies comming in or passing through, and will replace it with REJECT for traffic generated by the local host.</dd></dl>
<h2>redirect [to-port port]</h2>
<dl>
<dd><i>redirect</i> is used internally by FireHOL Helper Commands to redirect traffic to ports on the local host. Unless you are a developer, you will never need to use this directly.</dd></dl>
<h2>Optional Rule Parameters</h2>
<p>Optional rule parameters are accepted by many commands to narrow the match they do by default. The parameters described bellow are all that FireHOL supports. You should check the documentation of each command to find which parameters should not be used with it. Normally, all FireHOL commands are designed so that if you specify a parameters that is also used internally, the internal one will overwrite the one given in the configuration file. In such a case, FireHOL will present you a warning with the old and the new value. </p>
<p> Not all parameters should be used in all cases. For example <i>sport</i> and <i>dport</i> should not be used in normal server and client commands since such ports are internally defined by the services themselves. In any case, FireHOL will complain about optional rule parameters that should not be used in certain commands.</p>
<h2>src [not] &lt;host&gt;</h2>
<dl>
<dd><i>src</i> defines the source IP address of the REQUEST. If <i>src</i> is defined on a server statement it matches the source of the request which is the remote host, while if it is defined on a client statement it matches again the source of the request, but this time it is the local host. Focus on the REQUEST!!! Forget the reply. </dd>
<p> <i>Parameters</i></p>
<dl>
<dt>not</dt>
<dd>Optional argument that reverses the match. When defined, the rule will match all hosts except the ones defined. Example:<br/>
&nbsp;<wbr>&nbsp;<wbr>server smtp accept src not 1.2.3.4</dd>
<dt><i>host</i></dt>
<dd>An IP address, a hostname, or a subnet. Multiple hosts/networks can be defined if separated by space and quoted as a single argument. Examples:<br/>
&nbsp;<wbr>&nbsp;<wbr>server smtp accept src 1.2.3.4<br/>
&nbsp;<wbr>&nbsp;<wbr>server smtp accept src not&nbsp;<wbr>&#8220;1.2.3.0/24 5.6.7.8 badhost.example.com&#8221;&nbsp;<wbr></dd></dl>
</dl>
<dl>
<dd></dd></dl>
<h2>dst [not] &lt;host&gt;</h2>
<dl>
<dd><i>dst</i> defines the destination of the REQUEST. If dst is defined on a server statement it matches the destination of the request which is the local host, while if it is defined on a client statement it matches again the destination of the request, but this time it is the remote host. Focus on the REQUEST!!! Forget the reply. </dd>
<p> <i>dst</i> accepts the same parameters as src.</dl>
<h2>inface [not] &lt;interface&gt;</h2>
<dl>
<dd><i>inface</i> defines the interface the REQUEST is received via. inface cannot be used in interface commands. </dd>
<p> <i>Parameters</i></p>
<dl>
<dt>not</dt>
<dd>An optional argument that reverses the match. When defined, the rule will match all interfaces except the ones defined. Example:<br/>
&nbsp;<wbr>&nbsp;<wbr>server smtp accept inface not eth0</dd>
<dt><i>interface</i></dt>
<dd>if an interface name in the same format the interface command accepts. Multiple interfaces can be defined if separated by space and quoted as a single argument. Examples:<br/>
&nbsp;<wbr>&nbsp;<wbr>server smtp accept inface not eth0<br/>
&nbsp;<wbr>&nbsp;<wbr>server smtp accept inface not&nbsp;<wbr>&#8220;eth0 eth1&#8221;</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<h2>outface [not] &lt;interface&gt;</h2>
<dl>
<dd><i>outface</i> defines the interface the REQUEST is send via. outface cannot be used in interface commands. </dd>
<p> <i>outface</i> accepts the same parameters as inface.</dl>
<h2>custom &lt;parameters&gt;</h2>
<dl>
<dd><i>custom</i> passes its arguments to the generated iptables commands. </dd>
<p> It is required to quote all the parameters given to custom. If the parameters include a space character between some text that is required to be given to iptables as one argument, it is required to escape another set of quotes in order. Another way is to use double quotes externally and single quotes internally. </p>
<p> Examples: </p>
<pre> server smtp accept custom &quot;--some-iptables-option and_its_value&quot;</pre>
<pre> server smtp accept custom &quot;--some-iptables-option 'one_value another_value'</pre>
</dl>
<h2>log &lt;some text&gt; [level a_level]</h2>
<dl>
<dd><i>log</i> will log the matching packets to syslog. Note that this is not an action (in iptables it is). FireHOL will actually produce multiple iptables commands to accomplish both the action for the rule and the logging. You can control how logging works, by altering the variables FIREHOL_LOG_OPTIONS and FIREHOL_LOG_LEVEL. You can also change the level of just one rule by using the level argument of the log parameter. </dd>
<p> FireHOL logs traffic, exactly the same way iptables does. Many users have complained about packet logs appearing at their console. To avoid this you will have to:</p>
<dl>
<dt>* setup klogd to log only more important traffic</dt>
<dd>
</dd><dt>* change FIREHOL_LOG_LEVEL to log at a not so important log-level</dt>
<dd></dd></dl>
</dl>
<dl>
<dd>Actually klogd&#8217;s -c option and iptables&#8217; &#8211;log-level option are the same thing (iptables accepts also the numeric values klogd accepts). If iptables logs at a higher priority than klogd is configured to use, then your packets will appear in the console too.</dd></dl>
<h2>loglimit &lt;some text&gt;</h2>
<dl>
<dd><i>loglimit</i> is the same with log but limits the frequency of logging according to the setting of FIREHOL_LOG_FREQUENCY and FIREHOL_LOG_BURST.</dd></dl>
<h2>proto [not] &lt;protocol&gt;</h2>
<dl>
<dd><i>proto</i> sets the required protocol for the traffic. This command accepts anything iptables accepts as protocols.</dd></dl>
<h2>limit &lt;frequency&gt; &lt;burst&gt;</h2>
<dl>
<dd><i>limit</i> will limit the match in both directions of the traffic (request and reply). This is used internally by FireHOL and its effects has not been tested in the high level configuration file directives.</dd></dl>
<h2>sport &lt;port&gt;</h2>
<dl>
<dd><i>sport</i> defines the source port of a request. It accepts port names, port numbers, port ranges (FROM:TO) and multiple ports (or ranges) seperated by spaces and quoted as a single argument. This parameter should not be used in normal services definitions (client and server commands) or interface and router definitions, unless you really understand what you are doing.</dd></dl>
<h2>dport &lt;port&gt;</h2>
<dl>
<dd><i>dport</i> defines the destination port of a request. It accepts port names, port numbers, port ranges (FROM:TO) and multiple ports (or ranges) seperated by spaces and quoted as a single argument. This parameter should not be used in normal services definitions (client and server commands) or interface and router definitions, unless you really understand what you are doing.</dd></dl>
<h2>uid [not] &lt;user&gt; =head2 user [not] &lt;user&gt;</h2>
<dl>
<dd><i>uid</i> or <i>user</i> define the operating system user sending this traffic. The parameter can be a username, a user number or a list of these two, seperated by spaces and quoted as a single argument. </dd>
<p> This parameter can be used only in services (client and server commands) defined within interfaces, not routers. FireHOL is &#8220;smart&#8221; enough to apply this parameter only to traffic send by the localhost, i.e. the replies of servers and requests of clients. It is not possible, and FireHOL will simply ignore this parameter, on traffic coming in or passign through the firewall host. </p>
<p> Example 1: </p>
<pre> client &quot;pop3 imap&quot; accept user not &quot;user1 user2 user3&quot; dst mymailer.example.com</pre>
</dl>
<dl>
<dd>The above will allow local users except user1, user2 and user3 to use POP3 and IMAP services on mymailer.example.com. You can use this, for example, to allow only a few of the local users use the fetchmail program to fetch their mail from the mail server. </dd>
<p> Example 2: </p>
<pre> server http accept user apache</pre>
</dl>
<dl>
<dd>The above will allow all HTTP to reach the local http server, but only if the web server is running as user apache the replies will be send back to the HTTP client.</dd></dl>
<h2>gid &lt;group&gt; =head2 group &lt;group&gt;</h2>
<dl>
<dd><i>gid</i> or <i>group</i> define the operating system user group sending this traffic. The parameter can be a group name, a group number or a list of these two, seperated by spaces and quoted as a single argument. </dd>
<p> This parameter can be used only in services (client and server commands) defined within interfaces, not routers. FireHOL is &#8220;smart&#8221; enough to apply this parameter only to traffic send by the localhost, i.e. the replies of servers and requests of clients. It is not possible, and FireHOL will simply ignore this parameter, on traffic coming in or passing through the firewall host.</dl>
<h2>pid &lt;process&gt; =head2 process &lt;process&gt;</h2>
<dl>
<dd><i>pid</i> or <i>process</i> define the operating system process ID (or PID) sending this traffic. The parameter can be a PID or a list of PIDs, seperated by spaces and quoted as a single argument. </dd>
<p> This parameter can be used only in services (client and server commands) defined within interfaces, not routers. FireHOL is &#8220;smart&#8221; enough to apply this parameter only to traffic send by the localhost, i.e. the replies of servers and requests of clients. It is not possible, and FireHOL will simply ignore this parameter, on traffic coming in or passign through the firewall host.</dl>
<h2>sid &lt;session&gt; =head2 session &lt;session&gt;</h2>
<dl>
<dd><i>sid</i> or <i>session</i> define the operating system session ID of the process sending this traffic (The session ID of a process is the process group ID of the session leader). The parameter can be a list of such IDs, seperated by spaces and quoted as a single argument. </dd>
<p> This parameter can be used only in services (client and server commands) defined within interfaces, not routers. FireHOL is &#8220;smart&#8221; enough to apply this parameter only to traffic send by the localhost, i.e. the replies of servers and requests of clients. It is not possible, and FireHOL will simply ignore this parameter, on traffic coming in or passign through the firewall host.</dl>
<h2>Variables that control FireHOL</h2>
<h2>DEFAULT_INTERFACE_POLICY</h2>
<dl>
<dd><i></i><i>DEFAULT_INTERFACE_POLICY</i><i></i> controls the default action to be taken on traffic not matched by any rule within an interface. Actually, this is a global setting for what policy does for an interface. </dd>
<p> All packets that reach the end of an interface are logged only if the action is not return or accept. You can control the frequency of this logging by altering the frequency loglimit uses. </p>
<pre> Default: DEFAULT_INTERFACE_POLICY=&quot;DROP&quot;</pre>
<pre> Example: DEFAULT_INTERFACE_POLICY=&quot;REJECT&quot;</pre>
</dl>
<h2>UNMATCHED_INPUT_POLICY</h2>
<h2>UNMATCHED_OUTPUT_POLICY</h2>
<h2>UNMATCHED_FORWARD_POLICY</h2>
<dl>
<dd><i></i><i>UNMATCHED_INPUT_POLICY</i><i></i> controls the default action to be taken for incoming traffic not matched by any interface command. </dd>
<p> <i></i><i>UNMATCHED_OUTPUT_POLICY</i><i></i> controls the default action to be taken for outgoing traffic not matched by any interface command. </p>
<p> <i></i><i>UNMATCHED_FORWARD_POLICY</i><i></i> controls the default action to be taken for forwarded traffic not matched by any router command. </p>
<p> All variables accept all the Actions FireHOL supports. </p>
<p> All packets that reach the end of firewall in all three chains are logged (always, regardless of these settings). You can control the frequency of this logging by altering the frequency loglimit uses. </p>
<pre> Default: UNMATCHED_INPUT_POLICY=&quot;DROP&quot;</pre>
<pre> Default: UNMATCHED_OUTPUT_POLICY=&quot;DROP&quot;</pre>
<pre> Default: UNMATCHED_FORWARD_POLICY=&quot;DROP&quot;</pre>
<pre> Example: UNMATCHED_INPUT_POLICY=&quot;REJECT&quot;</pre>
<pre> Example: UNMATCHED_OUTPUT_POLICY=&quot;REJECT&quot;</pre>
<pre> Example: UNMATCHED_FORWARD_POLICY=&quot;REJECT&quot;</pre>
</dl>
<h2>FIREHOL_LOG_LEVEL =head2 FIREHOL_LOG_OPTIONS =head2 FIREHOL_LOG_FREQUENCY =head2 FIREHOL_LOG_BURST</h2>
<dl>
<dd><i></i><i>FIREHOL_LOG_LEVEL</i><i></i> controls the level at which iptables will log things to the syslog. For a description of the possible values supported and for per-rule control of log level, see the log optional rule parameter. </dd>
<p> <i></i><i>FIREHOL_LOG_OPTIONS</i><i></i> controls the way iptables will log things to the syslog. The value of this variable is passed as is to iptables, so use exact iptables parameters. </p>
<p> <i></i><i>FIREHOL_LOG_FREQUENCY</i><i></i> and <i></i><i>FIREHOL_LOG_BURST</i><i></i> (added in v1.39 of FireHOL) control the frequency at each each logging rule will write packets to the syslog. FIREHOL_LOG_FREQUENCY is set to the maximum average frequency and FIREHOL_LOG_BURST specifies the maximum initial number of packets to match. </p>
<pre> Default: FIREHOL_LOG_OPTIONS=&quot;--log-level warning&quot;</pre>
<pre> Default: FIREHOL_LOG_FREQUENCY=&quot;1/second&quot;</pre>
<pre> Default: FIREHOL_LOG_BURST=&quot;5&quot;</pre>
<pre> Example: FIREHOL_LOG_OPTIONS=&quot;--log-level info --log-tcp-options --log-ip-options&quot;</pre>
<pre> Example: FIREHOL_LOG_FREQUENCY=&quot;30/minute&quot;</pre>
<pre> Example: FIREHOL_LOG_BURST=&quot;2&quot;</pre>
<p>To see the available iptables log options, run <tt>&quot;/sbin/iptables -j LOG --help&quot;</tt> To see what iptables accepts as frequencies and bursts, run <tt>&quot;/sbin/iptables -m limit --help&quot;</tt> </p>
<p> You can also check man iptables.</dl>
<h2>DEFAULT_CLIENT_PORTS</h2>
<dl>
<dd><i></i><i>DEFAULT_CLIENT_PORTS</i><i></i> controls the port range to be used when a remote client is specified. For localhost clients, FireHOL finds the exact client ports by querying the kernel options. </dd>
<pre> Default: 1000:65535</pre>
<pre> Example: DEFAULT_CLIENT_PORTS=&quot;0:65535&quot;</pre>
</dl>
<h2>FIREHOL_NAT</h2>
<dl>
<dd>If <i></i><i>FIREHOL_NAT</i><i></i> is set to 1, FireHOL will load NAT kernel modules for those services that they are require such. FireHOL sets this to 1 automatically if you use the Helper Commands that do NAT. </dd>
<pre> Default: FIREHOL_NAT=&quot;0&quot;</pre>
<pre> Example: FIREHOL_NAT=&quot;1&quot;</pre>
</dl>
<h2>FIREHOL_AUTOSAVE</h2>
<dl>
<dd>FIREHOL_AUTOSAVE controls the file that will be created when FireHOL is called with the save command line argument. If this variable is empty (the default), FireHOL will try to detect where to save the file. Currently, the RedHat way (/etc/sysconfig/iptables) and the Debian way (/var/lib/iptables/autosave) are automatically detected (in the order given here) based on the existance of the directory this file should be created in. </dd>
<p> Default: FIREHOL_AUTOSAVE=&quot;&#8220; Example: FIREHOL_AUTOSAVE=&#8221;/tmp/firehol-saved.txt&quot;</dl>
<h2>Variables that FireHOL offers</h2>
<h2>RESERVED_IPS</h2>
<dl>
<dd>This variable includes all the IP addresses defined as IANA &#8211; Reserved by IANA. </dd>
<pre> Example: interface eth0 internet src not &quot;${RESERVED_IPS}&quot;</pre>
</dl>
<h2>PRIVATE_IPS</h2>
<dl>
<dd>This variable includes all the IP addresses defined as Private or Test by RFC 3330. </dd>
<pre> Example: interface eth0 internet src not &quot;${PRIVATE_IPS}&quot;</pre>
</dl>
<h2>UNROUTABLE_IPS</h2>
<dl>
<dd>This variable is both <i></i><i>RESERVED_IPS</i><i></i> and <i></i><i>PRIVATE_IPS</i><i></i> together. I suggest to use this variable on interfaces and routers accepting Internet traffic. </dd>
<pre> Example: interface eth0 internet src not &quot;${UNROUTABLE_IPS}&quot;</pre>
</dl>
<h2>Files</h2>
<p><i>/etc/firehol/firehol.conf</i></p>
<h2>Author</h2>
<p>firehol written by Costa Tsaousis &lt;costa [at] tsaousis.gr&gt;. </p>
<p> Man page written by Marc Brockschmidt &lt;&lt;marc [at] marcbrockschmidt.de&gt;.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-firehol/">firehol</a></i>(1), <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8), <i><a href="/docs/linux/man/1-bash/">bash</a></i>(1) </p>
