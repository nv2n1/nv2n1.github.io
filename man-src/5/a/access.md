---
title: "access(5)"
name: "access"
section: "5"
letter: "a"
url: "/docs/linux/man/5-access/"
description: "access – Postfix SMTP server access table"
---

<p>access &#8211; Postfix SMTP server access table</p>
<h2>Synopsis</h2>
<pre><code>postmap /etc/postfix/access</code>
<code>postmap -q &quot;</code><i>string</i><code>&quot; /etc/postfix/access</code>
<code>postmap -q - /etc/postfix/access &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>This document describes access control on remote SMTP client information: host names, network addresses, and envelope sender or recipient addresses; it is implemented by the Postfix SMTP server. See <code><a href="/docs/linux/man/5-header_checks/">header_checks</a></code>(5) or <code><a href="/docs/linux/man/5-body_checks/">body_checks</a></code>(5) for access control on the content of email messages. </p>
<p> Normally, the <code><a href="/docs/linux/man/5-access/">access</a></code>(5) table is specified as a text file that serves as input to the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command. The result, an indexed file in <code>dbm</code> or <code>db</code> format, is used for fast searching by the mail system. Execute the command &quot;<code>postmap /etc/postfix/access</code>&quot; to rebuild an indexed file after changing the corresponding text file. </p>
<p> When the table is provided via other means such as NIS, LDAP or SQL, the same lookups are done as for ordinary indexed files. </p>
<p> Alternatively, the table can be provided as a regular-expression map where patterns are given as regular expressions, or lookups can be directed to TCP-based server. In those cases, the lookups are done in a slightly different way as described below under &quot;REGULAR EXPRESSION TABLES&quot; or &quot;TCP-BASED TABLES&quot;.</p>
<h2>Case Folding</h2>
<p>The search string is folded to lowercase before database lookup. As of Postfix 2.3, the search string is not case folded with database types such as regexp: or pcre: whose lookup fields can match both upper and lower case.</p>
<h2>Table Format</h2>
<p>The input format for the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command is as follows:</p>
<dl>
<dt><i>pattern action</i></p>
<dd>When <i>pattern</i> matches a mail address, domain or host address, perform the corresponding <i>action</i>.</p>
<dt>blank lines and comments</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>multi-line text</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<h2>Email Address Patterns</h2>
<p>With lookups from indexed files such as DB or DBM, or from networked tables such as NIS, LDAP or SQL, patterns are tried in the order as listed below:</p>
<dl>
<dt><i>user</i>@<i>domain</i></p>
<dd>Matches the specified mail address.</p>
<dt><i>domain.tld</i></p>
<dd>Matches <i>domain.tld</i> as the domain part of an email address. </p>
<p> The pattern <i>domain.tld</i> also matches subdomains, but only when the string <code>smtpd_access_maps</code> is listed in the Postfix <code>parent_domain_matches_subdomains</code> configuration setting.</p>
<dt><i>.domain.tld</i></p>
<dd>Matches subdomains of <i>domain.tld</i>, but only when the string <code>smtpd_access_maps</code> is not listed in the Postfix <code>parent_domain_matches_subdomains</code> configuration setting.</p>
<dt><i>user</i>@</p>
<dd>Matches all mail addresses with the specified user part.</dl>
<p> Note: lookup of the null sender address is not possible with some types of lookup table. By default, Postfix uses <code>&lt;&gt;</code> as the lookup key for such addresses. The value is specified with the <code>smtpd_null_access_lookup_key</code> parameter in the Postfix <code>main.cf</code> file.</p>
<h2>Email Address Extension</h2>
<p>When a mail address localpart contains the optional recipient delimiter (e.g., <i>user+foo</i>@<i>domain</i>), the lookup order becomes: <i>user+foo</i>@<i>domain</i>, <i>user</i>@<i>domain</i>, <i>domain</i>, <i>user+foo</i>@, and <i>user</i>@.</p>
<h2>Host Name/Address Patterns</h2>
<p>With lookups from indexed files such as DB or DBM, or from networked tables such as NIS, LDAP or SQL, the following lookup patterns are examined in the order as listed:</p>
<dl>
<dt><i>domain.tld</i></p>
<dd>Matches <i>domain.tld</i>. </p>
<p> The pattern <i>domain.tld</i> also matches subdomains, but only when the string <code>smtpd_access_maps</code> is listed in the Postfix <code>parent_domain_matches_subdomains</code> configuration setting.</p>
<dt><i>.domain.tld</i></p>
<dd>Matches subdomains of <i>domain.tld</i>, but only when the string <code>smtpd_access_maps</code> is not listed in the Postfix <code>parent_domain_matches_subdomains</code> configuration setting.</p>
<dt><i>net.work.addr.ess</i></p>
<dd>
<dt><i>net.work.addr</i></p>
<dd>
<dt><i>net.work</i></p>
<dd>
<dt><i>net</i></p>
<dd>Matches the specified IPv4 host address or subnetwork. An IPv4 host address is a sequence of four decimal octets separated by &quot;.&quot;. </p>
<p> Subnetworks are matched by repeatedly truncating the last &quot;.octet&quot; from the remote IPv4 host address string until a match is found in the access table, or until further truncation is not possible. </p>
<p> NOTE 1: The access map lookup key must be in canonical form: do not specify unnecessary null characters, and do not enclose network address information with &quot;[]&quot; characters. </p>
<p> NOTE 2: use the <code>cidr</code> lookup table type to specify network/netmask patterns. See <code><a href="/docs/linux/man/5-cidr_table/">cidr_table</a></code>(5) for details.</p>
<dt><i>net:work:addr:ess</i></p>
<dd>
<dt><i>net:work:addr</i></p>
<dd>
<dt><i>net:work</i></p>
<dd>
<dt><i>net</i></p>
<dd>Matches the specified IPv6 host address or subnetwork. An IPv6 host address is a sequence of three to eight hexadecimal octet pairs separated by &quot;:&quot;. </p>
<p> Subnetworks are matched by repeatedly truncating the last &quot;:octetpair&quot; from the remote IPv6 host address string until a match is found in the access table, or until further truncation is not possible. </p>
<p> NOTE 1: the truncation and comparison are done with the string representation of the IPv6 host address. Thus, not all the &quot;:&quot; subnetworks will be tried. </p>
<p> NOTE 2: The access map lookup key must be in canonical form: do not specify unnecessary null characters, and do not enclose network address information with &quot;[]&quot; characters. </p>
<p> NOTE 3: use the <code>cidr</code> lookup table type to specify network/netmask patterns. See <code><a href="/docs/linux/man/5-cidr_table/">cidr_table</a></code>(5) for details. </p>
<p> IPv6 support is available in Postfix 2.2 and later.</dl>
<h2>Accept Actions</h2>
<dl>
<dt><code>OK</code></p>
<dd>Accept the address etc. that matches the pattern.</p>
<dt><i>all-numerical</i></p>
<dd>An all-numerical result is treated as OK. This format is generated by address-based relay authorization schemes such as pop-before-smtp.</dl>
<p> For other accept actions, see &quot;OTHER ACTIONS&quot; below.</p>
<h2>Reject Actions</h2>
<p>Postfix version 2.3 and later support enhanced status codes as defined in RFC 3463. When no code is specified at the beginning of the <i>text</i> below, Postfix inserts a default enhanced status code of &quot;5.7.1&quot; in the case of reject actions, and &quot;4.7.1&quot; in the case of defer actions. See &quot;ENHANCED STATUS CODES&quot; below.</p>
<dl>
<dt><code>4</code><i>NN text</i></p>
<dd>
<dt><code>5</code><i>NN text</i></p>
<dd>Reject the address etc. that matches the pattern, and respond with the numerical three-digit code and text. <code>4</code><i>NN</i> means &quot;try again later&quot;, while <code>5</code><i>NN</i> means &quot;do not try again&quot;. </p>
<p> The following responses have special meaning for the Postfix SMTP server:</p>
<dl>
<dd>
<dl>
<dt><code>421 </code><i>text</i> (Postfix 2.3 and later)</p>
<dd>
<dt><code>521 </code><i>text</i> (Postfix 2.6 and later)</p>
<dd>After responding with the numerical three-digit code and text, disconnect immediately from the SMTP client. This frees up SMTP server resources so that they can be made available to another SMTP client.</p>
<dd>Note: The &quot;521&quot; response should be used only with botnets and other malware where interoperability is of no concern. The &quot;send 521 and disconnect&quot; behavior is NOT defined in the SMTP standard.</dl>
</dl>
<dt><code>REJECT </code><i>optional text&#8230;</i></p>
<dd>Reject the address etc. that matches the pattern. Reply with &quot;<code>$access_map_reject_code </code><i>optional text&#8230;</i>&quot; when the optional text is specified, otherwise reply with a generic error response message.</p>
<dt><code>DEFER </code><i>optional text&#8230;</i></p>
<dd>Reject the address etc. that matches the pattern. Reply with &quot;<code>$access_map_defer_code </code><i>optional text&#8230;</i>&quot; when the optional text is specified, otherwise reply with a generic error response message. </p>
<p> This feature is available in Postfix 2.6 and later.</p>
<dt><code>DEFER_IF_REJECT </code><i>optional text&#8230;</i></p>
<dd>Defer the request if some later restriction would result in a REJECT action. Reply with &quot;<code>$access_map_defer_code 4.7.1 </code><i>optional text&#8230;</i>&quot; when the optional text is specified, otherwise reply with a generic error response message. </p>
<p> Prior to Postfix 2.6, the SMTP reply code is 450. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<dt><code>DEFER_IF_PERMIT </code><i>optional text&#8230;</i></p>
<dd>Defer the request if some later restriction would result in a an explicit or implicit PERMIT action. Reply with &quot;<code>$access_map_defer_code 4.7.1 </code><i> optional text&#8230;</i>&quot; when the optional text is specified, otherwise reply with a generic error response message. </p>
<p> Prior to Postfix 2.6, the SMTP reply code is 450. </p>
<p> This feature is available in Postfix 2.1 and later.</dl>
<p> For other reject actions, see &quot;OTHER ACTIONS&quot; below.</p>
<h2>Other Actions</h2>
<dl>
<dt><i>restriction&#8230;</i></p>
<dd>Apply the named UCE restriction(s) (<code>permit</code>, <code>reject</code>, <code>reject_unauth_destination</code>, and so on).</p>
<dt><code>BCC </code><i>user [at] domain</i></p>
<dd>Send one copy of the message to the specified recipient. </p>
<p> If multiple BCC actions are specified within the same SMTP MAIL transaction, with Postfix 3.0 only the last action will be used. </p>
<p> This feature is available in Postfix 3.0 and later.</p>
<dt><code>DISCARD </code><i>optional text&#8230;</i></p>
<dd>Claim successful delivery and silently discard the message. Log the optional text if specified, otherwise log a generic message. </p>
<p> Note: this action currently affects all recipients of the message. To discard only one recipient without discarding the entire message, use the <a href="/docs/linux/man/5-transport/">transport</a>(5) table to direct mail to the <a href="/docs/linux/man/8-discard/">discard</a>(8) service. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<dt><code>DUNNO</code></p>
<dd>Pretend that the lookup key was not found. This prevents Postfix from trying substrings of the lookup key (such as a subdomain name, or a network address subnetwork). </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<dt><code>FILTER </code><i>transport:destination</i></p>
<dd>After the message is queued, send the entire message through the specified external content filter. The <i>transport</i> name specifies the first field of a mail delivery agent definition in master.cf; the syntax of the next-hop <i>destination</i> is described in the manual page of the corresponding delivery agent. More information about external content filters is in the Postfix FILTER_README file. </p>
<p> Note 1: do not use $<i>number</i> regular expression substitutions for <i>transport</i> or <i>destination</i> unless you know that the information has a trusted origin. </p>
<p> Note 2: this action overrides the main.cf <code>content_filter</code> setting, and affects all recipients of the message. In the case that multiple <code>FILTER</code> actions fire, only the last one is executed. </p>
<p> Note 3: the purpose of the FILTER command is to override message routing. To override the recipient&#8217;s <i>transport</i> but not the next-hop <i>destination</i>, specify an empty filter <i>destination</i> (Postfix 2.7 and later), or specify a <i>transport:destination</i> that delivers through a different Postfix instance (Postfix 2.6 and earlier). Other options are using the recipient-dependent <code>transport_maps</code> or the sender-dependent <code>sender_dependent_default_transport_maps</code> features. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<dt><code>HOLD </code><i>optional text&#8230;</i></p>
<dd>Place the message on the <code>hold</code> queue, where it will sit until someone either deletes it or releases it for delivery. Log the optional text if specified, otherwise log a generic message. </p>
<p> Mail that is placed on hold can be examined with the <code><a href="/docs/linux/man/1-postcat/">postcat</a></code>(1) command, and can be destroyed or released with the <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) command. </p>
<p> Note: use &quot;<code>postsuper -r</code>&quot; to release mail that was kept on hold for a significant fraction of <code>$maximal_queue_lifetime</code> or <code>$bounce_queue_lifetime</code>, or longer. Use &quot;<code>postsuper -H</code>&quot; only for mail that will not expire within a few delivery attempts. </p>
<p> Note: this action currently affects all recipients of the message. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<dt><code>PREPEND </code><i>headername: headervalue</i></p>
<dd>Prepend the specified message header to the message. When more than one PREPEND action executes, the first prepended header appears before the second etc. prepended header. </p>
<p> Note: this action must execute before the message content is received; it cannot execute in the context of <code>smtpd_end_of_data_restrictions</code>. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<dt><code>REDIRECT </code><i>user [at] domain</i></p>
<dd>After the message is queued, send the message to the specified address instead of the intended recipient(s). When multiple <code>REDIRECT</code> actions fire, only the last one takes effect. </p>
<p> Note: this action overrides the FILTER action, and currently overrides all recipients of the message. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<dt><code>INFO </code><i>optional text&#8230;</i></p>
<dd>Log an informational record with the optional text, together with client information and if available, with helo, sender, recipient and protocol information. </p>
<p> This feature is available in Postfix 3.0 and later.</p>
<dt><code>WARN </code><i>optional text&#8230;</i></p>
<dd>Log a warning with the optional text, together with client information and if available, with helo, sender, recipient and protocol information. </p>
<p> This feature is available in Postfix 2.1 and later.</dl>
<h2>Enhanced Status Codes</h2>
<p>Postfix version 2.3 and later support enhanced status codes as defined in RFC 3463. When an enhanced status code is specified in an access table, it is subject to modification. The following transformations are needed when the same access table is used for client, helo, sender, or recipient access restrictions; they happen regardless of whether Postfix replies to a MAIL FROM, RCPT TO or other SMTP command.</p>
<dl>
<dt>&bull;</p>
<dd>When a sender address matches a REJECT action, the Postfix SMTP server will transform a recipient DSN status (e.g., 4.1.1-4.1.6) into the corresponding sender DSN status, and vice versa.</p>
<dt>&bull;</p>
<dd>When non-address information matches a REJECT action (such as the HELO command argument or the client hostname/address), the Postfix SMTP server will transform a sender or recipient DSN status into a generic non-address DSN status (e.g., 4.0.0).</dl>
<h2>Regular Expression Tables</h2>
<p>This section describes how the table lookups change when the table is given in the form of regular expressions. For a description of regular expression lookup table syntax, see <code><a href="/docs/linux/man/5-regexp_table/">regexp_table</a></code>(5) or <code><a href="/docs/linux/man/5-pcre_table/">pcre_table</a></code>(5). </p>
<p> Each pattern is a regular expression that is applied to the entire string being looked up. Depending on the application, that string is an entire client hostname, an entire client IP address, or an entire mail address. Thus, no parent domain or parent network search is done, <i>user [at] domain</i> mail addresses are not broken up into their <i>user@</i> and <i>domain</i> constituent parts, nor is <i>user+foo</i> broken up into <i>user</i> and <i>foo</i>. </p>
<p> Patterns are applied in the order as specified in the table, until a pattern is found that matches the search string. </p>
<p> Actions are the same as with indexed file lookups, with the additional feature that parenthesized substrings from the pattern can be interpolated as <code>$1</code>, <code>$2</code> and so on.</p>
<h2>Tcp-Based Tables</h2>
<p>This section describes how the table lookups change when lookups are directed to a TCP-based server. For a description of the TCP client/server lookup protocol, see <code><a href="/docs/linux/man/5-tcp_table/">tcp_table</a></code>(5). This feature is not available up to and including Postfix version 2.4. </p>
<p> Each lookup operation uses the entire query string once. Depending on the application, that string is an entire client hostname, an entire client IP address, or an entire mail address. Thus, no parent domain or parent network search is done, <i>user [at] domain</i> mail addresses are not broken up into their <i>user@</i> and <i>domain</i> constituent parts, nor is <i>user+foo</i> broken up into <i>user</i> and <i>foo</i>. </p>
<p> Actions are the same as with indexed file lookups.</p>
<h2>Example</h2>
<p>The following example uses an indexed file, so that the order of table entries does not matter. The example permits access by the client at address 1.2.3.4 but rejects all other clients in 1.2.3.0/24. Instead of <code>hash</code> lookup tables, some systems use <code>dbm</code>. Use the command &quot;<code>postconf -m</code>&quot; to find out what lookup tables Postfix supports on your system. </p>
<pre>/etc/postfix/main.cf:
 smtpd_client_restrictions =
 check_client_access hash:/etc/postfix/access
/etc/postfix/access:
 1.2.3 REJECT
 1.2.3.4 OK</pre>
<p>Execute the command &quot;<code>postmap /etc/postfix/access</code>&quot; after editing the file.</p>
<h2>Bugs</h2>
<p>The table format does not understand quoting conventions.</p>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), SMTP server
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-transport/">transport</a>(5), transport:nexthop syntax</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>SMTPD_ACCESS_README, built-in SMTP server access control
DATABASE_README, Postfix lookup table overview</pre>
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
