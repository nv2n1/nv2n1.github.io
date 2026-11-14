---
title: "dhcp6c-conf(5)"
name: "dhcp6c-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dhcp6c-conf/"
description: "dhcp6c.conf – DHCPv6 client configuration file"
---

<p><code>dhcp6c.conf</code> &#8211; DHCPv6 client configuration file</p>
<h2>Synopsis</h2>
<p>/etc/wide-dhcpv6/dhcp6c.conf</p>
<h2>Description</h2>
<p>The file contains configuration information for KAME&#8217;s DHCPv6 client, <code>dhcp6c</code> The configuration file consists of a sequence of statements terminated by a semi-colon (`;&#8217;). Statements are composed of tokens separated by white space, which can be any combination of blanks, tabs and newlines. In some cases a set of statements is combined with a pair of brackets, which is regarded as a single token. Lines beginning with `#&#8217; are comments.</p>
<h2>Interface specification</h2>
<p>There are some statements that may or have to specify interface. Interfaces are specified in the form of &quot;name unit&quot;, such as <i>fxp0</i> and <i>gif1.</i></p>
<h2>DHCPv6 options</h2>
<p>Some configuration statements take the description of a DHCPv6 option as an argument. The followings are the format and description of available DHCPv6 options.</p>
<dl>
<dt> <code>domain-name-servers</code></p>
<dd>
<dd>means a Domain Name Server option.</p>
<dt> <code>domain-name</code></p>
<dd>
<dd>means a domain name option.</p>
<dt> <code>ntp-servers</code></p>
<dd>
<dd>means an NTP server option. As of this writing, the option type for this option is not officially assigned. <code>dhcp6c</code> will reject this option unless it is explicitly built to accept the option.</p>
<dt> <code>sip-server-address</code></p>
<dd>
<dd>means a SIP Server address option.</p>
<dt> <code>sip-server-domain-name</code></p>
<dd>
<dd>means a SIP server domain name option.</p>
<dt> <code>nis-server-address</code></p>
<dd>
<dd>means a NIS Server address option.</p>
<dt> <code>nis-domain-name</code></p>
<dd>
<dd>means a NIS domain name option.</p>
<dt> <code>nisp-server-address</code></p>
<dd>
<dd>means a NIS+ Server address option.</p>
<dt> <code>nisp-domain-name</code></p>
<dd>
<dd>means a NIS+ domain name option.</p>
<dt> <code>bcmcs-server-address</code></p>
<dd>
<dd>means a BCMCS Server address option.</p>
<dt> <code>bcmcs-server-domain-name</code></p>
<dd>
<dd>means a BCMCS server domain name option.</p>
<dt><code>ia-pd </code><i>ID</i></p>
<dd>means an IA_PD (Identity Association for Prefix Delegation) option. <i>ID</i> is a decimal number of the IAID (see below about identity associations)</p>
<dt><code>ia-na </code><i>ID</i></p>
<dd>means an IA_PD (Identity Association for Non-temporary Addresses) option. <i>ID</i> is a decimal number of the IAID (see below about identity associations)</p>
<dt><code>rapid-commit</code></p>
<dd>means a rapid-commit option.</p>
<dt><code>authentication </code><i>authname</i></p>
<dd>means an authentication option. <i>authname</i> is a string specifying parameters of the authentication protocol. An <code>authentication</code> statement for <i>authname</i> must be provided.</dl>
<h2>Interface statement</h2>
<p>An interface statement specifies configuration parameters on the interface. The generic format of an interface statement is as follows:</p>
<dl>
<dt> <code>interface </code><i>interface</i> { <i>substatements</i> };</p>
<dd>
<dd>The followings are possible <i>substatements</i> in an interface statement.</p>
<dl>
<dt> <code>send </code><i>send-options</i> ;</p>
<dd>
<dd>This statement specifies DHCPv6 options to be sent to the server(s). Some options can only appear in particular messages according to the specification, in which case the appearance of the options is limited to be compliant with the specification. </p>
<p> <i>send-options</i> is a comma-separated list of options, each of which should be specified as described above. Multiple <code>send</code> statements can also be specified, in which case all the specified options will be sent. </p>
<p> When <code>rapid-commit</code> is specified, <code>dhcp6c</code> will include a rapid-commit option in solicit messages and wait for an immediate reply instead of advertisements. </p>
<p> When <code>ia-pd</code> is specified, <code>dhcp6c</code> will initiate prefix delegation as a requesting router by including an IA_PD option with the specified <i>ID</i> in solicit messages. </p>
<p> When <code>ia-na</code> is specified, <code>dhcp6c</code> will initiate stateful address assignment by including an IA_NA option with the specified <i>ID</i> in solicit messages. </p>
<p> In either case, a corresponding identity association statement must exist with the same <i>ID</i></p>
<dt><code>request </code><i>request-options</i></p>
<dd>This statement specifies DHCPv6 options to be included in an option-request option. <i>request-options</i> is a comma-separated list of options, which can consist of the following options.</p>
<dl>
<dt> <code>domain-name-servers</code></p>
<dd>
<dd>requests a list of Domain Name Server addresses.</p>
<dt> <code>domain-name</code></p>
<dd>
<dd>requests a DNS search path.</p>
<dt> <code>ntp-servers</code></p>
<dd>
<dd>requests a list of NTP server addresses. As of this writing, the option type for this option is not officially assigned. <code>dhcp6c</code> will reject this option unless it is explicitly built to accept the option.</p>
<dt> <code>sip-server-address</code></p>
<dd>
<dd>requests a list of SIP server addresses.</p>
<dt> <code>sip-domain-name</code></p>
<dd>
<dd>requests a SIP server domain name.</p>
<dt> <code>nis-server-address</code></p>
<dd>
<dd>requests a list of NIS server addresses.</p>
<dt> <code>nis-domain-name</code></p>
<dd>
<dd>requests a NIS domain name.</p>
<dt> <code>nisp-server-address</code></p>
<dd>
<dd>requests a list of NIS+ server addresses.</p>
<dt> <code>nisp-domain-name</code></p>
<dd>
<dd>requests a NIS+ domain name.</p>
<dt> <code>bcmcs-server-address</code></p>
<dd>
<dd>requests a list of BCMCS server addresses.</p>
<dt> <code>bcmcs-domain-name</code></p>
<dd>
<dd>requests a BCMCS domain name.</p>
<dt> <code>refreshtime</code></p>
<dd>
<dd>means an information refresh time option. This can only be specified when sent with information-request messages; <code>dhcp6c</code> will ignore this option for other messages.</dl>
<p> Multiple <code>request</code> statements can also be specified, in which case all the specified options will be requested.</p>
<dt><code>information-only</code></p>
<dd>This statement specifies <code>dhcp6c</code> to only exchange informational configuration parameters with servers. A list of DNS server addresses is an example of such parameters. This statement is useful when the client does not need stateful configuration parameters such as IPv6 addresses or prefixes.</p>
<dt><code>script </code><i>&quot;script-name&quot;</i></p>
<dd>This statement specifies a path to script invoked by <code>dhcp6c</code> on a certain condition including when the daemon receives a reply message. <i>script-name</i> must be the absolute path from root to the script file, be a regular file, and be created by the same owner who runs the daemon.</dl>
</dl>
<h2>Profile statement</h2>
<p>Some setups may require to configure an interface independently from its name. Profiles are available for this particular purpose. They follow the same syntax as an interface statement except they can be arbitrarily named. It is then possible to choose which profile to use for a given interface on the command line.</p>
<h2>Identity association statement</h2>
<p>Identity association (IA) is a key notion of DHCPv6. An IA is uniquely identified in a client by a pair of IA type and IA identifier (IAID) An IA is associated with configuration information dependent on the IA type. </p>
<p> An identity association statement defines a single IA with some client-side configuration parameters. Its format is as follows:</p>
<dl>
<dt> <code>id-assoc </code><i>type </i>[<i>ID</i> ] { <i>substatements</i> };</p>
<dd><i>type</i></p>
<dd>is a string for the type of this IA. The current implementation supports `<code>na</code> &#8216; (non-temporary address allocation) `<code>pd</code> &#8216; </p>
<p> (prefix delegation) for the IA type. <i>ID</i> is a decimal number of IAID. If omitted, the value 0 will be used by default. <i>substatements</i> is a sequence of statements that specifies configuration parameters for this IA. Each statement may or may not be specific to the type of IA. </p>
<p> The followings are possible <i>substatements</i> for an IA of type <code>na</code></p>
<dl>
<dt> <code>address </code><i>ipv6-address pltime </i>[<i>vltime</i> ]</p>
<dd>
<dd>specifies an address and related parameters that the client wants to be allocated. Multiple addresses can be specified, each of which is described as a separate <code>address</code> substatement. <code>dhcp6c</code> will include all the addresses (and related parameters) in Solicit messages, as an IA_NA prefix option encapsulated in the corresponding IA_NA option. Note, however, that the server may or may not respect the specified prefix parameters. For parameters of the <code>address</code> substatement, see dhcp6s.conf5.</dl>
<p> The followings are possible <i>substatements</i> for an IA of type <code>pd</code></p>
<dl>
<dt> <i>prefix_interface_statement</i></p>
<dd>
<dd>specifies the client&#8217;s local configuration of how delegated prefixes should be used (see below)</p>
<dt><code>prefix </code><i>ipv6-prefix pltime </i>[<i>vltime</i> ]</p>
<dd>specifies a prefix and related parameters that the client wants to be delegated. Multiple prefixes can be specified, each of which is described as a separate <code>prefix</code> substatement. <code>dhcp6c</code> will include all the prefixes (and related parameters) in Solicit messages, as an IA_PD prefix option encapsulated in the corresponding IA_PD option. Note, however, that the server may or may not respect the specified prefix parameters. For parameters of the <code>prefix</code> substatement, see dhcp6s.conf5.</dl>
</dl>
<h2>Prefix interface statement</h2>
<p>A prefix interface statement specifies configuration parameters of prefixes on local interfaces that are derived from delegated prefixes. A prefix interface statement can only appear as a substatement of an identity association statement with the type <code>pd</code> The generic format of an interface statement is as follows:</p>
<dl>
<dt> <code>prefix-interface </code><i>interface</i> { <i>substatements</i> };</p>
<dd>
<dd>When an IPv6 prefix is delegated from a DHCPv6 server, <code>dhcp6c</code> will assign a prefix on the <i>interface</i> unless the interface receives the DHCPv6 message that contains the prefix with the delegated prefix and the parameters provided in <i>substatements</i> Possible substatements are as follows:</p>
<dl>
<dt> <code>sla-id </code><i>ID</i> ;</p>
<dd>
<dd>This statement specifies the identifier value of the site-level aggregator (SLA) on the interface. <i>ID</i> must be a decimal integer which fits in the length of SLA IDs (see below) For example, if <i>ID</i> is 1 and the client is delegated an IPv6 prefix 2001:db8:ffff::/48, <code>dhcp6c</code> will combine the two values into a single IPv6 prefix, 2001:db8:ffff:1::/64, and will configure the prefix on the specified <i>interface</i></p>
<dt> <code>sla-len </code><i>length</i> ;</p>
<dd>
<dd>This statement specifies the length of the SLA ID in bits. <i>length</i> must be a decimal number between 0 and 128. If the length is not specified by this statement, the default value 16 will be used.</p>
<dt> <code>ifid </code><i>ID</i> ;</p>
<dd>
<dd>This statement specifies the interface id. <i>ID</i> must be a decimal integer. It will be combined with the delegated prefix and the sla-id to form a complete interface address. The default is to use the EUI-64 address of the <i>interface</i></dl>
</dl>
<h2>Authentication statement</h2>
<p>An authentication statement defines a set of authentication parameters used in DHCPv6 exchanges with the server(s). The format of an authentication statement is as follows:</p>
<dl>
<dt> <code>authentication </code><i>authname</i> { <i>substatements</i> };</p>
<dd><i>authname</i></p>
<dd>is a string which is unique among all authentication statements in the configuration file. It will specify a particular set of authentication parameters when <code>authentication</code> option is specified in the <code>interface</code> statement. Possible substatements of the <code>authentication</code> statement are as follows:</p>
<dl>
<dt> <code>protocol </code><i>authprotocol</i> ;</p>
<dd>
<dd>specifies the authentication protocol. Currently, the only available protocol as <i>authprotocol</i> is <code>delayed</code> which means the DHCPv6 delayed authentication protocol.</p>
<dt> <code>algorithm </code><i>authalgorithm</i> ;</p>
<dd>
<dd>specifies the algorithm for this authentication. Currently, the only available algorithm is HMAC-MD5, which can be specified as one of the followings: <code>hmac-md5</code> <code>HMAC-MD5</code> <code>hmacmd5</code> or <code>HMACMD5</code> This substatement can be omitted. In this case, HMAC-MD5 will be used as the algorithm.</p>
<dt> <code>rdm </code><i>replay-detection-method</i> ;</p>
<dd>
<dd>specifies the replay protection method for this authentication. Currently, the only available method is <code>monocounter</code> which means the use of a monotonically increasing counter. If this method is specified, <code>dhcp6c</code> will use an NTP-format timestamp when it authenticates the message. This substatement can be omitted, in which case <code>monocounter</code> will be used as the method.</dl>
</dl>
<h2>Keyinfo statement</h2>
<p>A keyinfo statement defines a secret key shared with the server(s) to authenticate DHCPv6 messages. The format of a keyinfo statement is as follows:</p>
<dl>
<dt> <code>keyinfo </code><i>keyname</i> { <i>substatements</i> };</p>
<dd><i>keyname</i></p>
<dd>is an arbitrary string. It does not affect client&#8217;s behavior but is provided for readability of log messages. Possible substatements of the <code>keyinfo</code> statement are as follows:</p>
<dl>
<dt> <code>realm </code><i>&quot;realmname&quot;</i> ;</p>
<dd>
<dd>specifies the DHCP realm. <i>realmname</i> is an arbitrary string, but is typically expected to be a domain name like &quot;kame.net&quot; .</p>
<dt> <code>keyid </code><i>ID</i> ;</p>
<dd>
<dd>specifies the key identifier, <i>ID</i> as a decimal number. A secret key is uniquely identified within the client by the DHCP realm and the key identifier.</p>
<dt> <code>secret </code><i>&quot;secret-value&quot;</i> ;</p>
<dd>
<dd>specifies the shared secret of this key. <i>&quot;secret-value&quot;</i> is a base-64 encoded string of the secret.</p>
<dt> <code>expire </code><i>&quot;expiration-time&quot;</i> ;</p>
<dd>
<dd>specifies the expiration time of this key. <i>&quot;expiration-time&quot;</i> should be formatted in one of the followings: <i>yyyy-mm-dd HH:MM</i> <i>mm-dd HH:MM</i> or <i>HH:MM</i> where <i>yyyy</i> is the year with century (e.g., 2004), <i>mm</i> is the month, <i>dd</i> is the day of the month, <i>HH</i> is the hour of 24-hour clock, and <i>MM</i> is the minute, each of which is given as a decimal number. Additionally, a special keyword <code>forever</code> can be specified as <i>expiration-time</i> which means the key has an infinite lifetime and never expires. This substatement can be omitted, in which case <code>forever</code> will be used by default.</dl>
</dl>
<h2>Examples</h2>
<p>The followings are a sample configuration to be delegated an IPv6 prefix from an upstream service provider. With this configuration <code>dhcp6c</code> will send solicit messages containing an IA_PD option, with an IAID 0, on to an upstream PPP link, <i>ppp0</i> After receiving some prefixes from a server, <code>dhcp6c</code> will then configure derived IPv6 prefixes with the SLA ID 1 on a local ethernet interface, <i>ne0</i> Note that the IAID for the <code>id-assoc</code> statement is 0 according to the default. </p>
<pre>interface ppp0 {
 send ia-pd 0;
};
id-assoc pd {
 prefix-interface ne0 {
 sla-id 1;
 };
};</pre>
<p>If a shared secret should be configured in both the client and the server for DHCPv6 authentication, it would be specified in the configuration file as follows: </p>
<pre>keyinfo kame-key {
 realm &quot;kame.net&quot;;
 keyid 1;
 secret &quot;5pvW2g48OHPvkYMJSw0vZA==&quot;;
};</pre>
<p>One easy way of generating a new secret in the base64 format is to execute the <a href="/docs/linux/man/1-openssl/">openssl</a>(1) command (when available) as follows, </p>
<pre>% openssl rand -base64 16</pre>
<p>and copy the output to the <code>dhcp6c.conf</code> file. </p>
<p> To include an authentication option for DHCPv6 authentication, the <code>interface</code> statement should be modified and an <code>authentication</code> statement should be added as follows: </p>
<pre>interface ppp0 {
 send ia-pd 0;
 send authentication kame;
};
authentication kame {
 protocol delayed;
};</pre>
<pre>interface fxp0 {
 send ia-na 0;
};</pre>
<h2>See Also</h2>
<p>dhcp6s.conf5 <a href="/docs/linux/man/8-dhcp6c/">dhcp6c</a>(8)</p>
<h2>History</h2>
<p>The configuration file first appeared in the WIDE/KAME IPv6 protocol stack kit.</p>
