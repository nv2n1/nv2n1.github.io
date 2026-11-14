---
title: "canonical(5)"
name: "canonical"
section: "5"
letter: "c"
url: "/docs/linux/man/5-canonical/"
description: "canonical – Postfix canonical table format"
---

<p>canonical &#8211; Postfix canonical table format</p>
<h2>Synopsis</h2>
<pre><code>postmap /etc/postfix/canonical</code>
<code>postmap -q &quot;</code><i>string</i><code>&quot; /etc/postfix/canonical</code>
<code>postmap -q - /etc/postfix/canonical &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The optional <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5) table specifies an address mapping for local and non-local addresses. The mapping is used by the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon, before mail is stored into the queue. The address mapping is recursive. </p>
<p> Normally, the <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5) table is specified as a text file that serves as input to the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command. The result, an indexed file in <code>dbm</code> or <code>db</code> format, is used for fast searching by the mail system. Execute the command &quot;<code>postmap /etc/postfix/canonical</code>&quot; to rebuild an indexed file after changing the corresponding text file. </p>
<p> When the table is provided via other means such as NIS, LDAP or SQL, the same lookups are done as for ordinary indexed files. </p>
<p> Alternatively, the table can be provided as a regular-expression map where patterns are given as regular expressions, or lookups can be directed to TCP-based server. In those cases, the lookups are done in a slightly different way as described below under &quot;REGULAR EXPRESSION TABLES&quot; or &quot;TCP-BASED TABLES&quot;. </p>
<p> By default the <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5) mapping affects both message header addresses (i.e. addresses that appear inside messages) and message envelope addresses (for example, the addresses that are used in SMTP protocol commands). This is controlled with the <code>canonical_classes</code> parameter. </p>
<p> NOTE: Postfix versions 2.2 and later rewrite message headers from remote SMTP clients only if the client matches the local_header_rewrite_clients parameter, or if the remote_header_rewrite_domain configuration parameter specifies a non-empty value. To get the behavior before Postfix 2.2, specify &quot;local_header_rewrite_clients = static:all&quot;. </p>
<p> Typically, one would use the <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5) table to replace login names by <i>Firstname.Lastname</i>, or to clean up addresses produced by legacy mail systems. </p>
<p> The <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5) mapping is not to be confused with <i>virtual alias</i> support or with local aliasing. To change the destination but not the headers, use the <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) or <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) map instead.</p>
<h2>Case Folding</h2>
<p>The search string is folded to lowercase before database lookup. As of Postfix 2.3, the search string is not case folded with database types such as regexp: or pcre: whose lookup fields can match both upper and lower case.</p>
<h2>Table Format</h2>
<p>The input format for the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command is as follows:</p>
<dl>
<dt><i>pattern address</i></p>
<dd>When <i>pattern</i> matches a mail address, replace it by the corresponding <i>address</i>.</p>
<dt>blank lines and comments</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>multi-line text</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<h2>Table Search Order</h2>
<p>With lookups from indexed files such as DB or DBM, or from networked tables such as NIS, LDAP or SQL, each <i>user</i>@<i>domain</i> query produces a sequence of query patterns as described below. </p>
<p> Each query pattern is sent to each specified lookup table before trying the next query pattern, until a match is found.</p>
<dl>
<dt><i>user</i>@<i>domain address</i></p>
<dd>Replace <i>user</i>@<i>domain</i> by <i>address</i>. This form has the highest precedence. </p>
<p> This is useful to clean up addresses produced by legacy mail systems. It can also be used to produce <i>Firstname.Lastname</i> style addresses, but see below for a simpler solution.</p>
<dt><i>user address</i></p>
<dd>Replace <i>user</i>@<i>site</i> by <i>address</i> when <i>site</i> is equal to $<code>myorigin</code>, when <i>site</i> is listed in $<code>mydestination</code>, or when it is listed in $<code>inet_interfaces</code> or $<code>proxy_interfaces</code>. </p>
<p> This form is useful for replacing login names by <i>Firstname.Lastname</i>.</p>
<dt>@<i>domain address</i></p>
<dd>Replace other addresses in <i>domain</i> by <i>address</i>. This form has the lowest precedence. </p>
<p> Note: @<i>domain</i> is a wild-card. When this form is applied to recipient addresses, the Postfix SMTP server accepts mail for any recipient in <i>domain</i>, regardless of whether that recipient exists. This may turn your mail system into a backscatter source: Postfix first accepts mail for non-existent recipients and then tries to return that mail as &quot;undeliverable&quot; to the often forged sender address. </p>
<p> To avoid backscatter with mail for a wild-card domain, replace the wild-card mapping with explicit 1:1 mappings, or add a reject_unverified_recipient restriction for that domain: </p>
<pre> smtpd_recipient_restrictions =
 ...
 reject_unauth_destination
 check_recipient_access
 inline:{example.com=reject_unverified_recipient}
 unverified_recipient_reject_code = 550</pre>
<p>In the above example, Postfix may contact a remote server if the recipient is rewritten to a remote address.</dl>
<h2>Result Address Rewriting</h2>
<p>The lookup result is subject to address rewriting:</p>
<dl>
<dt>&bull;</p>
<dd>When the result has the form @<i>otherdomain</i>, the result becomes the same <i>user</i> in <i>otherdomain</i>.</p>
<dt>&bull;</p>
<dd>When &quot;<code>append_at_myorigin=yes</code>&quot;, append &quot;<code>@$myorigin</code>&quot; to addresses without &quot;@domain&quot;.</p>
<dt>&bull;</p>
<dd>When &quot;<code>append_dot_mydomain=yes</code>&quot;, append &quot;<code>.$mydomain</code>&quot; to addresses without &quot;.domain&quot;.</dl>
<h2>Address Extension</h2>
<p>When a mail address localpart contains the optional recipient delimiter (e.g., <i>user+foo</i>@<i>domain</i>), the lookup order becomes: <i>user+foo</i>@<i>domain</i>, <i>user</i>@<i>domain</i>, <i>user+foo</i>, <i>user</i>, and @<i>domain</i>. </p>
<p> The <code>propagate_unmatched_extensions</code> parameter controls whether an unmatched address extension (<i>+foo</i>) is propagated to the result of table lookup.</p>
<h2>Regular Expression Tables</h2>
<p>This section describes how the table lookups change when the table is given in the form of regular expressions. For a description of regular expression lookup table syntax, see <code><a href="/docs/linux/man/5-regexp_table/">regexp_table</a></code>(5) or <code><a href="/docs/linux/man/5-pcre_table/">pcre_table</a></code>(5). </p>
<p> Each pattern is a regular expression that is applied to the entire address being looked up. Thus, <i>user [at] domain</i> mail addresses are not broken up into their <i>user</i> and <i>@domain</i> constituent parts, nor is <i>user+foo</i> broken up into <i>user</i> and <i>foo</i>. </p>
<p> Patterns are applied in the order as specified in the table, until a pattern is found that matches the search string. </p>
<p> Results are the same as with indexed file lookups, with the additional feature that parenthesized substrings from the pattern can be interpolated as <code>$1</code>, <code>$2</code> and so on.</p>
<h2>Tcp-Based Tables</h2>
<p>This section describes how the table lookups change when lookups are directed to a TCP-based server. For a description of the TCP client/server lookup protocol, see <code><a href="/docs/linux/man/5-tcp_table/">tcp_table</a></code>(5). This feature is not available up to and including Postfix version 2.4. </p>
<p> Each lookup operation uses the entire address once. Thus, <i>user [at] domain</i> mail addresses are not broken up into their <i>user</i> and <i>@domain</i> constituent parts, nor is <i>user+foo</i> broken up into <i>user</i> and <i>foo</i>. </p>
<p> Results are the same as with indexed file lookups.</p>
<h2>Bugs</h2>
<p>The table format does not understand quoting conventions.</p>
<h2>Configuration Parameters</h2>
<p>The following <code>main.cf</code> parameters are especially relevant. The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>canonical_classes (envelope_sender, envelope_recipient, header_sender, header_recipient)</code></p>
<dd>What addresses are subject to canonical_maps address mapping.</p>
<dt><code>canonical_maps (empty)</code></p>
<dd>Optional address mapping lookup tables for message headers and envelopes.</p>
<dt><code>recipient_canonical_maps (empty)</code></p>
<dd>Optional address mapping lookup tables for envelope and header recipient addresses.</p>
<dt><code>sender_canonical_maps (empty)</code></p>
<dd>Optional address mapping lookup tables for envelope and header sender addresses.</p>
<dt><code>propagate_unmatched_extensions (canonical, virtual)</code></p>
<dd>What address lookup tables copy an address extension from the lookup key to the lookup result.</dl>
<p> Other parameters of interest:</p>
<dl>
<dt><code>inet_interfaces (all)</code></p>
<dd>The network interface addresses that this mail system receives mail on.</p>
<dt><code>local_header_rewrite_clients (permit_inet_interfaces)</code></p>
<dd>Rewrite message header addresses in mail from these clients and update incomplete addresses with the domain name in $myorigin or $mydomain; either don&#8217;t rewrite message headers from other clients at all, or rewrite message headers and update incomplete addresses with the domain specified in the remote_header_rewrite_domain parameter.</p>
<dt><code>proxy_interfaces (empty)</code></p>
<dd>The network interface addresses that this mail system receives mail on by way of a proxy or network address translation unit.</p>
<dt><code>masquerade_classes (envelope_sender, header_sender, header_recipient)</code></p>
<dd>What addresses are subject to address masquerading.</p>
<dt><code>masquerade_domains (empty)</code></p>
<dd>Optional list of domains whose subdomain structure will be stripped off in email addresses.</p>
<dt><code>masquerade_exceptions (empty)</code></p>
<dd>Optional list of user names that are not subjected to address masquerading, even when their address matches $masquerade_domains.</p>
<dt><code>mydestination ($myhostname, localhost.$mydomain, localhost)</code></p>
<dd>The list of domains that are delivered via the $local_transport mail delivery transport.</p>
<dt><code>myorigin ($myhostname)</code></p>
<dd>The domain name that locally-posted mail appears to come from, and that locally posted mail is delivered to.</p>
<dt><code>owner_request_special (yes)</code></p>
<dd>Enable special treatment for owner-<i>listname</i> entries in the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) file, and don&#8217;t split owner-<i>listname</i> and <i>listname</i>-request address localparts when the recipient_delimiter is set to &quot;-&quot;.</p>
<dt><code>remote_header_rewrite_domain (empty)</code></p>
<dd>Don&#8217;t rewrite message headers from remote clients at all when this parameter is empty; otherwise, rewrite message headers and append the specified domain name to incomplete addresses.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-cleanup/">cleanup</a>(8), canonicalize and enqueue mail
<a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-virtual/">virtual</a>(5), virtual aliasing</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview
ADDRESS_REWRITING_README, address rewriting guide</pre>
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
