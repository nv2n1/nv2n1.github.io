---
title: "generic(5)"
name: "generic"
section: "5"
letter: "g"
url: "/docs/linux/man/5-generic/"
description: "generic – Postfix generic table format"
---

<p>generic &#8211; Postfix generic table format</p>
<h2>Synopsis</h2>
<pre><code>postmap /etc/postfix/generic</code>
<code>postmap -q &quot;</code><i>string</i><code>&quot; /etc/postfix/generic</code>
<code>postmap -q - /etc/postfix/generic &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The optional <code><a href="/docs/linux/man/5-generic/">generic</a></code>(5) table specifies an address mapping that applies when mail is delivered. This is the opposite of <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5) mapping, which applies when mail is received. </p>
<p> Typically, one would use the <code><a href="/docs/linux/man/5-generic/">generic</a></code>(5) table on a system that does not have a valid Internet domain name and that uses something like <i>localdomain.local</i> instead. The <code><a href="/docs/linux/man/5-generic/">generic</a></code>(5) table is then used by the <code><a href="/docs/linux/man/8-smtp/">smtp</a></code>(8) client to transform local mail addresses into valid Internet mail addresses when mail has to be sent across the Internet. See the EXAMPLE section at the end of this document. </p>
<p> The <code><a href="/docs/linux/man/5-generic/">generic</a></code>(5) mapping affects both message header addresses (i.e. addresses that appear inside messages) and message envelope addresses (for example, the addresses that are used in SMTP protocol commands). </p>
<p> Normally, the <code><a href="/docs/linux/man/5-generic/">generic</a></code>(5) table is specified as a text file that serves as input to the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command. The result, an indexed file in <code>dbm</code> or <code>db</code> format, is used for fast searching by the mail system. Execute the command &quot;<code>postmap /etc/postfix/generic</code>&quot; to rebuild an indexed file after changing the corresponding text file. </p>
<p> When the table is provided via other means such as NIS, LDAP or SQL, the same lookups are done as for ordinary indexed files. </p>
<p> Alternatively, the table can be provided as a regular-expression map where patterns are given as regular expressions, or lookups can be directed to TCP-based server. In those case, the lookups are done in a slightly different way as described below under &quot;REGULAR EXPRESSION TABLES&quot; or &quot;TCP-BASED TABLES&quot;.</p>
<h2>Case Folding</h2>
<p>The search string is folded to lowercase before database lookup. As of Postfix 2.3, the search string is not case folded with database types such as regexp: or pcre: whose lookup fields can match both upper and lower case.</p>
<h2>Table Format</h2>
<p>The input format for the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command is as follows:</p>
<dl>
<dt><i>pattern result</i></p>
<dd>When <i>pattern</i> matches a mail address, replace it by the corresponding <i>result</i>.</p>
<dt>blank lines and comments</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>multi-line text</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<h2>Table Search Order</h2>
<p>With lookups from indexed files such as DB or DBM, or from networked tables such as NIS, LDAP or SQL, each <i>user</i>@<i>domain</i> query produces a sequence of query patterns as described below. </p>
<p> Each query pattern is sent to each specified lookup table before trying the next query pattern, until a match is found.</p>
<dl>
<dt><i>user</i>@<i>domain address</i></p>
<dd>Replace <i>user</i>@<i>domain</i> by <i>address</i>. This form has the highest precedence.</p>
<dt><i>user address</i></p>
<dd>Replace <i>user</i>@<i>site</i> by <i>address</i> when <i>site</i> is equal to $<code>myorigin</code>, when <i>site</i> is listed in $<code>mydestination</code>, or when it is listed in $<code>inet_interfaces</code> or $<code>proxy_interfaces</code>.</p>
<dt>@<i>domain address</i></p>
<dd>Replace other addresses in <i>domain</i> by <i>address</i>. This form has the lowest precedence.</dl>
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
<h2>Example</h2>
<p>The following shows a generic mapping with an indexed file. When mail is sent to a remote host via SMTP, this replaces <i>his [at] localdomain.local</i> by his ISP mail address, replaces <i>her [at] localdomain.local</i> by her ISP mail address, and replaces other local addresses by his ISP account, with an address extension of <i>+local</i> (this example assumes that the ISP supports &quot;+&quot; style address extensions). </p>
<pre>/etc/postfix/main.cf:
 smtp_generic_maps = hash:/etc/postfix/generic
/etc/postfix/generic:
 his [at] localdomain.local hisaccount [at] hisisp.example
 her [at] localdomain.local heraccount [at] herisp.example
 @localdomain.local hisaccount+local [at] hisisp.example</pre>
<p>Execute the command &quot;<code>postmap /etc/postfix/generic</code>&quot; whenever the table is changed. Instead of <code>hash</code>, some systems use <code>dbm</code> database files. To find out what tables your system supports use the command &quot;<code>postconf -m</code>&quot;.</p>
<h2>Bugs</h2>
<p>The table format does not understand quoting conventions.</p>
<h2>Configuration Parameters</h2>
<p>The following <code>main.cf</code> parameters are especially relevant. The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>smtp_generic_maps</code></p>
<dd>Address mapping lookup table for envelope and header sender and recipient addresses while delivering mail via SMTP.</p>
<dt><code>propagate_unmatched_extensions</code></p>
<dd>A list of address rewriting or forwarding mechanisms that propagate an address extension from the original address to the result. Specify zero or more of <code>canonical</code>, <code>virtual</code>, <code>alias</code>, <code>forward</code>, <code>include</code>, or <code>generic</code>.</dl>
<p> Other parameters of interest:</p>
<dl>
<dt><code>inet_interfaces</code></p>
<dd>The network interface addresses that this system receives mail on. You need to stop and start Postfix when this parameter changes.</p>
<dt><code>proxy_interfaces</code></p>
<dd>Other interfaces that this machine receives mail on by way of a proxy agent or network address translator.</p>
<dt><code>mydestination</code></p>
<dd>List of domains that this mail system considers local.</p>
<dt><code>myorigin</code></p>
<dd>The domain that is appended to locally-posted mail.</p>
<dt><code>owner_request_special</code></p>
<dd>Give special treatment to <code>owner-</code><i>xxx</i> and <i>xxx</i><code>-request</code> addresses.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/8-smtp/">smtp</a>(8), Postfix SMTP client</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>ADDRESS_REWRITING_README, address rewriting guide
DATABASE_README, Postfix lookup table overview
STANDARD_CONFIGURATION_README, configuration examples</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>A genericstable feature appears in the Sendmail MTA. </p>
<p> This feature is available in Postfix 2.2 and later.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
