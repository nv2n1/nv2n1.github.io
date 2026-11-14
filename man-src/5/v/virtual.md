---
title: "virtual(5)"
name: "virtual"
section: "5"
letter: "v"
url: "/docs/linux/man/5-virtual/"
description: "virtual – Postfix virtual alias table format"
---

<p>virtual &#8211; Postfix virtual alias table format</p>
<h2>Synopsis</h2>
<pre><code>postmap /etc/postfix/virtual</code>
<code>postmap -q &quot;</code><i>string</i><code>&quot; /etc/postfix/virtual</code>
<code>postmap -q - /etc/postfix/virtual &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The optional <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) alias table rewrites recipient addresses for all local, all virtual, and all remote mail destinations. This is unlike the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) table which is used only for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery. Virtual aliasing is recursive, and is implemented by the Postfix <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon before mail is queued. </p>
<p> The main applications of virtual aliasing are:</p>
<dl>
<dt>&bull;</p>
<dd>To redirect mail for one address to one or more addresses.</p>
<dt>&bull;</p>
<dd>To implement virtual alias domains where all addresses are aliased to addresses in other domains. </p>
<p> Virtual alias domains are not to be confused with the virtual mailbox domains that are implemented with the Postfix <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) mail delivery agent. With virtual mailbox domains, each recipient address can have its own mailbox.</dl>
<p> Virtual aliasing is applied only to recipient envelope addresses, and does not affect message headers. Use <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5) mapping to rewrite header and envelope addresses in general. </p>
<p> Normally, the <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) alias table is specified as a text file that serves as input to the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command. The result, an indexed file in <code>dbm</code> or <code>db</code> format, is used for fast searching by the mail system. Execute the command &quot;<code>postmap /etc/postfix/virtual</code>&quot; to rebuild an indexed file after changing the corresponding text file. </p>
<p> When the table is provided via other means such as NIS, LDAP or SQL, the same lookups are done as for ordinary indexed files. </p>
<p> Alternatively, the table can be provided as a regular-expression map where patterns are given as regular expressions, or lookups can be directed to TCP-based server. In those case, the lookups are done in a slightly different way as described below under &quot;REGULAR EXPRESSION TABLES&quot; or &quot;TCP-BASED TABLES&quot;.</p>
<h2>Case Folding</h2>
<p>The search string is folded to lowercase before database lookup. As of Postfix 2.3, the search string is not case folded with database types such as regexp: or pcre: whose lookup fields can match both upper and lower case.</p>
<h2>Table Format</h2>
<p>The input format for the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command is as follows:</p>
<dl>
<dt><i>pattern address, address, &#8230;</i></p>
<dd>When <i>pattern</i> matches a mail address, replace it by the corresponding <i>address</i>.</p>
<dt>blank lines and comments</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>multi-line text</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<h2>Table Search Order</h2>
<p>With lookups from indexed files such as DB or DBM, or from networked tables such as NIS, LDAP or SQL, each <i>user</i>@<i>domain</i> query produces a sequence of query patterns as described below. </p>
<p> Each query pattern is sent to each specified lookup table before trying the next query pattern, until a match is found.</p>
<dl>
<dt><i>user</i>@<i>domain address, address, &#8230;</i></p>
<dd>Redirect mail for <i>user</i>@<i>domain</i> to <i>address</i>. This form has the highest precedence.</p>
<dt><i>user address, address, &#8230;</i></p>
<dd>Redirect mail for <i>user</i>@<i>site</i> to <i>address</i> when <i>site</i> is equal to $<code>myorigin</code>, when <i>site</i> is listed in $<code>mydestination</code>, or when it is listed in $<code>inet_interfaces</code> or $<code>proxy_interfaces</code>. </p>
<p> This functionality overlaps with functionality of the local <i><a href="/docs/linux/man/5-aliases/">aliases</a></i>(5) database. The difference is that <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) mapping can be applied to non-local addresses.</p>
<dt>@<i>domain address, address, &#8230;</i></p>
<dd>Redirect mail for other users in <i>domain</i> to <i>address</i>. This form has the lowest precedence. </p>
<p> Note: @<i>domain</i> is a wild-card. With this form, the Postfix SMTP server accepts mail for any recipient in <i>domain</i>, regardless of whether that recipient exists. This may turn your mail system into a backscatter source: Postfix first accepts mail for non-existent recipients and then tries to return that mail as &quot;undeliverable&quot; to the often forged sender address. </p>
<p> To avoid backscatter with mail for a wild-card domain, replace the wild-card mapping with explicit 1:1 mappings, or add a reject_unverified_recipient restriction for that domain: </p>
<pre> smtpd_recipient_restrictions =
 ...
 reject_unauth_destination
 check_recipient_access
 inline:{example.com=reject_unverified_recipient}
 unverified_recipient_reject_code = 550</pre>
<p>In the above example, Postfix may contact a remote server if the recipient is aliased to a remote address.</dl>
<h2>Result Address Rewriting</h2>
<p>The lookup result is subject to address rewriting:</p>
<dl>
<dt>&bull;</p>
<dd>When the result has the form @<i>otherdomain</i>, the result becomes the same <i>user</i> in <i>otherdomain</i>. This works only for the first address in a multi-address lookup result.</p>
<dt>&bull;</p>
<dd>When &quot;<code>append_at_myorigin=yes</code>&quot;, append &quot;<code>@$myorigin</code>&quot; to addresses without &quot;@domain&quot;.</p>
<dt>&bull;</p>
<dd>When &quot;<code>append_dot_mydomain=yes</code>&quot;, append &quot;<code>.$mydomain</code>&quot; to addresses without &quot;.domain&quot;.</dl>
<h2>Address Extension</h2>
<p>When a mail address localpart contains the optional recipient delimiter (e.g., <i>user+foo</i>@<i>domain</i>), the lookup order becomes: <i>user+foo</i>@<i>domain</i>, <i>user</i>@<i>domain</i>, <i>user+foo</i>, <i>user</i>, and @<i>domain</i>. </p>
<p> The <code>propagate_unmatched_extensions</code> parameter controls whether an unmatched address extension (<i>+foo</i>) is propagated to the result of table lookup.</p>
<h2>Virtual Alias Domains</h2>
<p>Besides virtual aliases, the virtual alias table can also be used to implement virtual alias domains. With a virtual alias domain, all recipient addresses are aliased to addresses in other domains. </p>
<p> Virtual alias domains are not to be confused with the virtual mailbox domains that are implemented with the Postfix <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) mail delivery agent. With virtual mailbox domains, each recipient address can have its own mailbox. </p>
<p> With a virtual alias domain, the virtual domain has its own user name space. Local (i.e. non-virtual) usernames are not visible in a virtual alias domain. In particular, local <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) and local mailing lists are not visible as <i>localname [at] virtual-alias.domain</i>. </p>
<p> Support for a virtual alias domain looks like: </p>
<pre>/etc/postfix/main.cf:
 virtual_alias_maps = hash:/etc/postfix/virtual</pre>
<p>Note: some systems use <code>dbm</code> databases instead of <code>hash</code>. See the output from &quot;<code>postconf -m</code>&quot; for available database types. </p>
<pre>/etc/postfix/virtual:
 <i>virtual-alias.domain anything</i> (right-hand content does not matter)
 <i>postmaster [at] virtual-alias.domain postmaster</i>
 <i>user1 [at] virtual-alias.domain address1</i>
 <i>user2 [at] virtual-alias.domain address2, address3</i></pre>
<p>The <i>virtual-alias.domain anything</i> entry is required for a virtual alias domain. <code>Without this entry, mail is rejected with &quot;relay access denied&quot;, or bounces with &quot;mail loops back to myself&quot;.</code> </p>
<p> Do not specify virtual alias domain names in the <code>main.cf mydestination</code> or <code>relay_domains</code> configuration parameters. </p>
<p> With a virtual alias domain, the Postfix SMTP server accepts mail for <i>known-user [at] virtual-alias.domain</i>, and rejects mail for <i>unknown-user</i>@<i>virtual-alias.domain</i> as undeliverable. </p>
<p> Instead of specifying the virtual alias domain name via the <code>virtual_alias_maps</code> table, you may also specify it via the <code>main.cf virtual_alias_domains</code> configuration parameter. This latter parameter uses the same syntax as the <code>main.cf mydestination</code> configuration parameter.</p>
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
<p>The following <code>main.cf</code> parameters are especially relevant to this topic. See the Postfix <code>main.cf</code> file for syntax details and for default values. Use the &quot;<code>postfix reload</code>&quot; command after a configuration change.</p>
<dl>
<dt><code>virtual_alias_maps ($virtual_maps)</code></p>
<dd>Optional lookup tables that alias specific mail addresses or domains to other local or remote address.</p>
<dt><code>virtual_alias_domains ($virtual_alias_maps)</code></p>
<dd>Postfix is final destination for the specified list of virtual alias domains, that is, domains for which all addresses are aliased to addresses in other local or remote domains.</p>
<dt><code>propagate_unmatched_extensions (canonical, virtual)</code></p>
<dd>What address lookup tables copy an address extension from the lookup key to the lookup result.</dl>
<p> Other parameters of interest:</p>
<dl>
<dt><code>inet_interfaces (all)</code></p>
<dd>The network interface addresses that this mail system receives mail on.</p>
<dt><code>mydestination ($myhostname, localhost.$mydomain, localhost)</code></p>
<dd>The list of domains that are delivered via the $local_transport mail delivery transport.</p>
<dt><code>myorigin ($myhostname)</code></p>
<dd>The domain name that locally-posted mail appears to come from, and that locally posted mail is delivered to.</p>
<dt><code>owner_request_special (yes)</code></p>
<dd>Enable special treatment for owner-<i>listname</i> entries in the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) file, and don&#8217;t split owner-<i>listname</i> and <i>listname</i>-request address localparts when the recipient_delimiter is set to &quot;-&quot;.</p>
<dt><code>proxy_interfaces (empty)</code></p>
<dd>The network interface addresses that this mail system receives mail on by way of a proxy or network address translation unit.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-cleanup/">cleanup</a>(8), canonicalize and enqueue mail
<a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-canonical/">canonical</a>(5), canonical address mapping</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>ADDRESS_REWRITING_README, address rewriting guide
DATABASE_README, Postfix lookup table overview
VIRTUAL_README, domain hosting guide</pre>
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
