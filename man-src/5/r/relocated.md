---
title: "relocated(5)"
name: "relocated"
section: "5"
letter: "r"
url: "/docs/linux/man/5-relocated/"
description: "relocated – Postfix relocated table format"
---

<p>relocated &#8211; Postfix relocated table format</p>
<h2>Synopsis</h2>
<pre><code>postmap /etc/postfix/relocated</code></pre>
<h2>Description</h2>
<p>The optional <code><a href="/docs/linux/man/5-relocated/">relocated</a></code>(5) table provides the information that is used in &quot;user has moved to <i>new_location</i>&quot; bounce messages. </p>
<p> Normally, the <code><a href="/docs/linux/man/5-relocated/">relocated</a></code>(5) table is specified as a text file that serves as input to the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command. The result, an indexed file in <code>dbm</code> or <code>db</code> format, is used for fast searching by the mail system. Execute the command &quot;<code>postmap /etc/postfix/relocated</code>&quot; to rebuild an indexed file after changing the corresponding relocated table. </p>
<p> When the table is provided via other means such as NIS, LDAP or SQL, the same lookups are done as for ordinary indexed files. </p>
<p> Alternatively, the table can be provided as a regular-expression map where patterns are given as regular expressions, or lookups can be directed to TCP-based server. In those case, the lookups are done in a slightly different way as described below under &quot;REGULAR EXPRESSION TABLES&quot; or &quot;TCP-BASED TABLES&quot;. </p>
<p> Table lookups are case insensitive.</p>
<h2>Case Folding</h2>
<p>The search string is folded to lowercase before database lookup. As of Postfix 2.3, the search string is not case folded with database types such as regexp: or pcre: whose lookup fields can match both upper and lower case.</p>
<h2>Table Format</h2>
<p>The input format for the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command is as follows:</p>
<dl>
<dt>&bull;</p>
<dd>An entry has one of the following form: </p>
<pre> <i>pattern new_location</i></pre>
<p>Where <i>new_location</i> specifies contact information such as an email address, or perhaps a street address or telephone number.</p>
<dt>&bull;</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>&bull;</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<h2>Table Search Order</h2>
<p>With lookups from indexed files such as DB or DBM, or from networked tables such as NIS, LDAP or SQL, patterns are tried in the order as listed below:</p>
<dl>
<dt><i>user</i>@<i>domain</i></p>
<dd>Matches <i>user</i>@<i>domain</i>. This form has precedence over all other forms.</p>
<dt><i>user</i></p>
<dd>Matches <i>user</i>@<i>site</i> when <i>site</i> is $<code>myorigin</code>, when <i>site</i> is listed in $<code>mydestination</code>, or when <i>site</i> is listed in $<code>inet_interfaces</code> or $<code>proxy_interfaces</code>.</p>
<dt>@<i>domain</i></p>
<dd>Matches other addresses in <i>domain</i>. This form has the lowest precedence.</dl>
<h2>Address Extension</h2>
<p>When a mail address localpart contains the optional recipient delimiter (e.g., <i>user+foo</i>@<i>domain</i>), the lookup order becomes: <i>user+foo</i>@<i>domain</i>, <i>user</i>@<i>domain</i>, <i>user+foo</i>, <i>user</i>, and @<i>domain</i>.</p>
<h2>Regular Expression Tables</h2>
<p>This section describes how the table lookups change when the table is given in the form of regular expressions or when lookups are directed to a TCP-based server. For a description of regular expression lookup table syntax, see <code><a href="/docs/linux/man/5-regexp_table/">regexp_table</a></code>(5) or <code><a href="/docs/linux/man/5-pcre_table/">pcre_table</a></code>(5). For a description of the TCP client/server table lookup protocol, see <code><a href="/docs/linux/man/5-tcp_table/">tcp_table</a></code>(5). This feature is not available up to and including Postfix version 2.4. </p>
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
<dt><code>relocated_maps</code></p>
<dd>List of lookup tables for relocated users or sites.</dl>
<p> Other parameters of interest:</p>
<dl>
<dt><code>inet_interfaces</code></p>
<dd>The network interface addresses that this system receives mail on. You need to stop and start Postfix when this parameter changes.</p>
<dt><code>mydestination</code></p>
<dd>List of domains that this mail system considers local.</p>
<dt><code>myorigin</code></p>
<dd>The domain that is appended to locally-posted mail.</p>
<dt><code>proxy_interfaces</code></p>
<dd>Other interfaces that this machine receives mail on by way of a proxy agent or network address translator.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a>(8), address resolver
<a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters</pre>
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
