---
title: "transport(5)"
name: "transport"
section: "5"
letter: "t"
url: "/docs/linux/man/5-transport/"
description: "transport – Postfix transport table format"
---

<p>transport &#8211; Postfix transport table format</p>
<h2>Synopsis</h2>
<pre><code>postmap /etc/postfix/transport</code>
<code>postmap -q &quot;</code><i>string</i><code>&quot; /etc/postfix/transport</code>
<code>postmap -q - /etc/postfix/transport &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The optional <code><a href="/docs/linux/man/5-transport/">transport</a></code>(5) table specifies a mapping from email addresses to message delivery transports and next-hop destinations. Message delivery transports such as <code>local</code> or <code>smtp</code> are defined in the <code>master.cf</code> file, and next-hop destinations are typically hosts or domain names. The table is searched by the <code><a href="/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a></code>(8) daemon. </p>
<p> This mapping overrides the default <i>transport</i>:<i>nexthop</i> selection that is built into Postfix:</p>
<dl>
<dt><code>local_transport (default: local:$myhostname)</code></p>
<dd>This is the default for final delivery to domains listed with <code>mydestination</code>, and for [<i>ipaddress</i>] destinations that match <code>$inet_interfaces</code> or <code>$proxy_interfaces</code>. The default <i>nexthop</i> destination is the MTA hostname.</p>
<dt><code>virtual_transport (default: virtual:)</code></p>
<dd>This is the default for final delivery to domains listed with <code>virtual_mailbox_domains</code>. The default <i>nexthop</i> destination is the recipient domain.</p>
<dt><code>relay_transport (default: relay:)</code></p>
<dd>This is the default for remote delivery to domains listed with <code>relay_domains</code>. In order of decreasing precedence, the <i>nexthop</i> destination is taken from <code>relay_transport</code>, <code>sender_dependent_relayhost_maps</code>, <code>relayhost</code>, or from the recipient domain.</p>
<dt><code>default_transport (default: smtp:)</code></p>
<dd>This is the default for remote delivery to other destinations. In order of decreasing precedence, the <i>nexthop</i> destination is taken from <code>sender_dependent_default_transport_maps, default_transport</code>, <code>sender_dependent_relayhost_maps</code>, <code>relayhost</code>, or from the recipient domain.</dl>
<p> Normally, the <code><a href="/docs/linux/man/5-transport/">transport</a></code>(5) table is specified as a text file that serves as input to the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command. The result, an indexed file in <code>dbm</code> or <code>db</code> format, is used for fast searching by the mail system. Execute the command &quot;<code>postmap /etc/postfix/transport</code>&quot; to rebuild an indexed file after changing the corresponding transport table. </p>
<p> When the table is provided via other means such as NIS, LDAP or SQL, the same lookups are done as for ordinary indexed files. </p>
<p> Alternatively, the table can be provided as a regular-expression map where patterns are given as regular expressions, or lookups can be directed to TCP-based server. In those case, the lookups are done in a slightly different way as described below under &quot;REGULAR EXPRESSION TABLES&quot; or &quot;TCP-BASED TABLES&quot;.</p>
<h2>Case Folding</h2>
<p>The search string is folded to lowercase before database lookup. As of Postfix 2.3, the search string is not case folded with database types such as regexp: or pcre: whose lookup fields can match both upper and lower case.</p>
<h2>Table Format</h2>
<p>The input format for the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command is as follows:</p>
<dl>
<dt><i>pattern result</i></p>
<dd>When <i>pattern</i> matches the recipient address or domain, use the corresponding <i>result</i>.</p>
<dt>blank lines and comments</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>multi-line text</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<p> The <i>pattern</i> specifies an email address, a domain name, or a domain name hierarchy, as described in section &quot;TABLE LOOKUP&quot;. </p>
<p> The <i>result</i> is of the form <i>transport:nexthop</i> and specifies how or where to deliver mail. This is described in section &quot;RESULT FORMAT&quot;.</p>
<h2>Table Search Order</h2>
<p>With lookups from indexed files such as DB or DBM, or from networked tables such as NIS, LDAP or SQL, patterns are tried in the order as listed below:</p>
<dl>
<dt><i>user+extension [at] domain transport</i>:<i>nexthop</i></p>
<dd>Deliver mail for <i>user+extension [at] domain</i> through <i>transport</i> to <i>nexthop</i>.</p>
<dt><i>user [at] domain transport</i>:<i>nexthop</i></p>
<dd>Deliver mail for <i>user [at] domain</i> through <i>transport</i> to <i>nexthop</i>.</p>
<dt><i>domain transport</i>:<i>nexthop</i></p>
<dd>Deliver mail for <i>domain</i> through <i>transport</i> to <i>nexthop</i>.</p>
<dt><i>.domain transport</i>:<i>nexthop</i></p>
<dd>Deliver mail for any subdomain of <i>domain</i> through <i>transport</i> to <i>nexthop</i>. This applies only when the string <code>transport_maps</code> is not listed in the <code>parent_domain_matches_subdomains</code> configuration setting. Otherwise, a domain name matches itself and its subdomains.</p>
<dt><code>*</code><i> transport</i>:<i>nexthop</i></p>
<dd>The special pattern <code>*</code> represents any address (i.e. it functions as the wild-card pattern, and is unique to Postfix transport tables).</dl>
<p> Note 1: the null recipient address is looked up as <code>$empty_address_recipient</code>@<code>$myhostname</code> (default: mailer-daemon [at] hostname). </p>
<p> Note 2: <i>user [at] domain</i> or <i>user+extension [at] domain</i> lookup is available in Postfix 2.0 and later.</p>
<h2>Result Format</h2>
<p>The lookup result is of the form <i>transport</i><code>:</code><i>nexthop</i>. The <i>transport</i> field specifies a mail delivery transport such as <code>smtp</code> or <code>local</code>. The <i>nexthop</i> field specifies where and how to deliver mail. </p>
<p> The transport field specifies the name of a mail delivery transport (the first name of a mail delivery service entry in the Postfix <code>master.cf</code> file). </p>
<p> The interpretation of the nexthop field is transport dependent. In the case of SMTP, specify a service on a non-default port as <i>host</i>:<i>service</i>, and disable MX (mail exchanger) DNS lookups with [<i>host</i>] or [<i>host</i>]:<i>port</i>. The [] form is required when you specify an IP address instead of a hostname. </p>
<p> A null <i>transport</i> and null <i>nexthop</i> result means &quot;do not change&quot;: use the delivery transport and nexthop information that would be used when the entire transport table did not exist. </p>
<p> A non-null <i>transport</i> field with a null <i>nexthop</i> field resets the nexthop information to the recipient domain. </p>
<p> A null <i>transport</i> field with non-null <i>nexthop</i> field does not modify the transport information.</p>
<h2>Examples</h2>
<p>In order to deliver internal mail directly, while using a mail relay for all other mail, specify a null entry for internal destinations (do not change the delivery transport or the nexthop information) and specify a wildcard for all other destinations. </p>
<pre> <code>my.domain :</code>
 <code>.my.domain :</code>
 <code>* smtp:outbound-relay.my.domain</code></pre>
<p>In order to send mail for <code>example.com</code> and its subdomains via the <code>uucp</code> transport to the UUCP host named <code>example</code>: </p>
<pre> <code>example.com uucp:example</code>
 <code>.example.com uucp:example</code></pre>
<p>When no nexthop host name is specified, the destination domain name is used instead. For example, the following directs mail for <i>user</i>@<code>example.com</code> via the <code>slow</code> transport to a mail exchanger for <code>example.com</code>. The <code>slow</code> transport could be configured to run at most one delivery process at a time: </p>
<pre> <code>example.com slow:</code></pre>
<p>When no transport is specified, Postfix uses the transport that matches the address domain class (see DESCRIPTION above). The following sends all mail for <code>example.com</code> and its subdomains to host <code>gateway.example.com</code>: </p>
<pre> <code>example.com :[gateway.example.com]</code>
 <code>.example.com :[gateway.example.com]</code></pre>
<p>In the above example, the [] suppress MX lookups. This prevents mail routing loops when your machine is primary MX host for <code>example.com</code>. </p>
<p> In the case of delivery via SMTP, one may specify <i>hostname</i>:<i>service</i> instead of just a host: </p>
<pre> <code>example.com smtp:bar.example:2025</code></pre>
<p>This directs mail for <i>user</i>@<code>example.com</code> to host <code>bar.example</code> port <code>2025</code>. Instead of a numerical port a symbolic name may be used. Specify [] around the hostname if MX lookups must be disabled. </p>
<p> The error mailer can be used to bounce mail: </p>
<pre> <code>.example.com error:mail for *.example.com is not deliverable</code></pre>
<p>This causes all mail for <i>user</i>@<i>anything</i><code>.example.com</code> to be bounced.</p>
<h2>Regular Expression Tables</h2>
<p>This section describes how the table lookups change when the table is given in the form of regular expressions. For a description of regular expression lookup table syntax, see <code><a href="/docs/linux/man/5-regexp_table/">regexp_table</a></code>(5) or <code><a href="/docs/linux/man/5-pcre_table/">pcre_table</a></code>(5). </p>
<p> Each pattern is a regular expression that is applied to the entire address being looked up. Thus, <i>some.domain.hierarchy</i> is not looked up via its parent domains, nor is <i>user+foo [at] domain</i> looked up as <i>user [at] domain</i>. </p>
<p> Patterns are applied in the order as specified in the table, until a pattern is found that matches the search string. </p>
<p> The <code><a href="/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a></code>(8) server disallows regular expression substitution of $1 etc. in regular expression lookup tables, because that could open a security hole (Postfix version 2.3 and later).</p>
<h2>Tcp-Based Tables</h2>
<p>This section describes how the table lookups change when lookups are directed to a TCP-based server. For a description of the TCP client/server lookup protocol, see <code><a href="/docs/linux/man/5-tcp_table/">tcp_table</a></code>(5). This feature is not available up to and including Postfix version 2.4. </p>
<p> Each lookup operation uses the entire recipient address once. Thus, <i>some.domain.hierarchy</i> is not looked up via its parent domains, nor is <i>user+foo [at] domain</i> looked up as <i>user [at] domain</i>. </p>
<p> Results are the same as with indexed file lookups.</p>
<h2>Configuration Parameters</h2>
<p>The following <code>main.cf</code> parameters are especially relevant. The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>empty_address_recipient</code></p>
<dd>The address that is looked up instead of the null sender address.</p>
<dt><code>parent_domain_matches_subdomains</code></p>
<dd>List of Postfix features that use <i>domain.tld</i> patterns to match <i>sub.domain.tld</i> (as opposed to requiring <i>.domain.tld</i> patterns).</p>
<dt><code>transport_maps</code></p>
<dd>List of transport lookup tables.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a>(8), rewrite and resolve addresses
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), master.cf file format
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>ADDRESS_REWRITING_README, address rewriting guide
DATABASE_README, Postfix lookup table overview
FILTER_README, external content filter</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
