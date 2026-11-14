---
title: "dhcp6s-conf(5)"
name: "dhcp6s-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dhcp6s-conf/"
description: "dhcp6s.conf – DHCPv6 server configuration file"
---

<p><code>dhcp6s.conf</code> &#8211; DHCPv6 server configuration file</p>
<h2>Synopsis</h2>
<p>/etc/wide-dhcpv6/dhcp6s.conf</p>
<h2>Description</h2>
<p>The file contains configuration information for KAME&#8217;s DHCPv6 server, <code>dhcp6s</code> The configuration file consists of a sequence of statements terminated by a semi-colon (`;&#8217;). Statements are composed of tokens separated by white space, which can be any combination of blanks, tabs and newlines. In some cases a set of statements is combined with a pair of brackets, which is regarded as a single token. Lines beginning with `#&#8217; are comments.</p>
<h2>Interface specification</h2>
<p>There are some statements that may or have to specify interface. Interfaces are specified in the form of &quot;name unit&quot;, such as <i>fxp0</i> and <i>gif1.</i></p>
<h2>Include statement</h2>
<p>An include statement specifies another configuration file to be included. The format of an include statement is as follows:</p>
<dl>
<dt> <code>include </code><i>&quot;filename&quot;</i></p>
<dd>
<dd>Where <i>&quot;filename&quot;</i> is the name (full path) of the file to be included.</dl>
<h2>Option statement</h2>
<p>An option statement specifies configuration parameters provided for every client. The format of the statement is as follows.</p>
<dl>
<dt> <code>option </code><i>option-name </i>[<i>option-value</i> ] ;</p>
<dd>
<dd>The following options can be specified in an option statement.</p>
<dl>
<dt> <code>domain-name-servers </code><i>dns-address </i>[<i>dns-addresses&#8230;</i> ]</p>
<dd>
<dd>provides DNS server address(es). Each <i>dns-address</i> must be a numeric IPv6 address. Multiple server addresses can also be specified by a sequence of these statements.</p>
<dt> <code>domain-name </code><i>&quot;dns-name&quot;</i></p>
<dd>
<dd>provides a domain name of a DNS search path. Multiple names in the path can be specified by a sequence of these statements.</p>
<dt> <code>ntp-servers </code><i>ntp-address </i>[<i>ntp-addresses&#8230;</i> ]</p>
<dd>
<dd>provides NTP server address(es). Each <i>ntp-address</i> must be a numeric IPv6 address. Multiple server addresses can also be specified by a sequence of these statements.</p>
<dt> <code>sip-server-address </code><i>sip-server-address </i>[<i>sip-server-addresses&#8230;</i> ]</p>
<dd>
<dd>provides SIP server address(es). Each <i>sip-server-address</i> must be a numeric IPv6 address. Multiple server addresses can also be specified by a sequence of these statements.</p>
<dt> <code>sip-server-domain-name </code><i>&quot;sip-server-domain-name&quot;</i></p>
<dd>
<dd>provides a domain name of a SIP server. Multiple names in the path can be specified by a sequence of these statements.</p>
<dt> <code>nis-server-address </code><i>nis-server-address </i>[<i>nis-server-addresses&#8230;</i> ]</p>
<dd>
<dd>provides NIS server address(es). Each <i>nis-server-address</i> must be a numeric IPv6 address. Multiple server addresses can also be specified by a sequence of these statements.</p>
<dt> <code>nis-domain-name </code><i>&quot;nis-domain-name&quot;</i></p>
<dd>
<dd>provides a NIS domain name. Multiple names in the path can be specified by a sequence of these statements.</p>
<dt> <code>nisp-server-address </code><i>nisp-server-address </i>[<i>nisp-server-addresses&#8230;</i> ]</p>
<dd>
<dd>provides NIS+ server address(es). Each <i>nisp-server-address</i> must be a numeric IPv6 address. Multiple server addresses can also be specified by a sequence of these statements.</p>
<dt> <code>nisp-domain-name </code><i>&quot;nisp-domain-name&quot;</i></p>
<dd>
<dd>provides a NIS+ domain name. Multiple names in the path can be specified by a sequence of these statements.</p>
<dt> <code>bcmcs-server-address </code><i>bcmcs-server-address </i>[<i>bcmcs-server-addresses&#8230;</i> ]</p>
<dd>
<dd>provides BCMCS server address(es). Each <i>bcmcs-server-address</i> must be a numeric IPv6 address. Multiple server addresses can also be specified by a sequence of these statements.</p>
<dt> <code>bcmcs-server-domain-name </code><i>&quot;bcmcs-server-domain-name&quot;</i></p>
<dd>
<dd>provides a domain name of a BCMCS server. Multiple names in the path can be specified by a sequence of these statements.</p>
<dt> <code>refreshtime </code><i>interval</i></p>
<dd>
<dd>specifies the refresh time of stateless information that does not have particular lease duration in seconds. This option is only applicable to stateless configuration by information-request and reply exchanges.</dl>
</dl>
<h2>Interface statement</h2>
<p>An interface statement specifies configuration parameters on the interface. The generic format of an interface statement is as follows:</p>
<dl>
<dt> <code>interface </code><i>interface</i> { <i>substatements</i> };</p>
<dd>
<dd>The followings are possible <i>substatements</i> in an interface statement.</p>
<dl>
<dt> <code>allow </code><i>allow-options</i> ;</p>
<dd>
<dd>This statement specifies DHCPv6 options accepted by the server. Currently only <i>rapid-commit</i> can be specified in an <code>allow</code> statement, which specifies the server to accept a rapid-commit option in solicit messages.</p>
<dt><code>preference </code><i>pref</i></p>
<dd>This statement sets the server&#8217;s preference value on the interface to the value <i>pref</i> The specified value will be contained in a preference option of advertise messages. The preference value must be a decimal integer and be between 0 and 255 (inclusive.)</p>
<dt><code>address-pool </code><i>pool pltime </i>[<i>vltime</i> ]</p>
<dd>This statement assigns an address pool <i>pool</i> to the interface. When receives a allocation request for an IA-NA, it assigns one IPv6 address from this pool. The specified pool name will be defined in a pool statement. Regarding the <i>pltime</i> and <i>vltime</i> , please see the explanation in the <i>prefix</i> substatement in host statement section.</dl>
</dl>
<h2>Host statement</h2>
<p>A host statement specifies configuration parameters for a particular client. The generic format of a host statement is as follows:</p>
<dl>
<dt> <code>host </code><i>name</i> { <i>substatements</i> };</p>
<dd><i>name</i></p>
<dd>is an arbitrary string. It does not affect server&#8217;s behavior but is provided for readability of log messages. Possible substatements are as follows.</p>
<dl>
<dt><code>duid </code><i>ID</i></p>
<dd>This statement defines the client&#8217;s DHCP unique identifier (DUID) <i>ID</i> is a colon-separated hexadecimal sequence where each separated part must be composed of two hexadecimal values. This statement is used to identify a particular host by the server and must be included in a host statement.</p>
<dt><code>prefix </code><i>ipv6-prefix pltime </i>[<i>vltime</i> ]</p>
<dd>This statement specifies an IPv6 prefix to be delegated to the client. <i>ipv6-prefix</i> is a string representing a valid IPv6 prefix (see the example below) <i>pltime</i> and <i>vltime</i> are preferred and valid lifetimes of the prefix, respectively. When the latter is omitted, it will be set to the same value of <i>pltime.</i> A positive decimal number or a special string <code>infinity</code> can be specified as a lifetime. A decimal number provides the lifetime in seconds, while <code>infinity</code> means the corresponding lifetime never expires. When both lifetimes are specified, <i>pltime</i> must not be larger than <i>vltime</i> Multiple prefixes can be specified, each of which is given by a single <code>prefix</code> statement. In that case, all or some of the specified prefixes will be delegated to the client, based on required parameters by the client.</p>
<dt><code>address </code><i>ipv6-address pltime </i>[<i>vltime</i> ]</p>
<dd>This statement specifies an IPv6 address to be assigned to the client. Everything is same as <i>prefix</i> option, except that you do not need specify prefix length.</p>
<dt><code>delayedkey </code><i>keyname</i></p>
<dd>This statement specifies a secret key shared with the client for the DHCPv6 delayed authentication protocol. <i>keyname</i> is a string that identifies a particular set of key parameters. A separate <code>keyinfo</code> statement for <i>keyname</i> must be provided in the configuration file. When this statement is specified and the client includes an authentication option for the delayed authentication protocol in a Solicit message, <code>dhcp6s</code> will perform the authentication protocol for succeeding message exchanges.</dl>
</dl>
<h2>Pool statement</h2>
<p>A pool statement specifies an address pool for a particular interface. The generic format of a pool statement is as follows:</p>
<dl>
<dt> <code>pool </code><i>name</i> { <i>substatements</i> };</p>
<dd><i>name</i></p>
<dd>is an arbitrary string. It does not affect server&#8217;s behavior but is provided for readability of log messages. Possible substatements are as follows.</p>
<dl>
<dt><code>range </code><i>min-addr </i><code>to </code><i>max-addr</i></p>
<dd>This substatement defines the range of addresses allocated for the pool, i.e. from <i>min-addr</i> to <i>max-addr.</i></dl>
</dl>
<h2>Keyinfo statement</h2>
<p>This statement defines a secret key shared with a client to authenticate DHCPv6 messages. The format and the description of this statement is provided in dhcp6c.conf5. One important difference in the server configuration is, however, the <i>keyname</i> is referred from a <code>host</code> statement as described above.</p>
<h2>Examples</h2>
<p>The followings are a sample configuration to provide a DNS server address for every client as well as to delegate a permanent IPv6 prefix 2001:db8:1111::/48 to a client whose DUID is 00:01:00:01:aa:bb. </p>
<pre>option domain-name-servers 2001:db8::35;
host kame {
 duid 00:01:00:01:aa:bb;
 prefix 2001:db8:1111::/48 infinity;
};</pre>
<p>If a shared secret should be configured in both the server and the client for DHCPv6 authentication, it would be specified in the configuration file as follows: </p>
<pre>keyinfo kame {
 realm &quot;kame.net&quot;;
 keyid 1;
 secret &quot;5pvW2g48OHPvkYMJSw0vZA==&quot;;
};</pre>
<p>And the <code>host</code> statement would be modified as follows: </p>
<pre>host kame {
 duid 00:01:00:01:aa:bb;
 prefix 2001:db8:1111::/48 infinity;
 delayedkey kame;
};</pre>
<h2>See Also</h2>
<p>dhcp6c.conf5 <a href="/docs/linux/man/8-dhcp6s/">dhcp6s</a>(8)</p>
<h2>History</h2>
<p>The configuration file first appeared in the WIDE/KAME IPv6 protocol stack kit.</p>
