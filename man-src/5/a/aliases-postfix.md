---
title: "aliases-postfix(5)"
name: "aliases-postfix"
section: "5"
letter: "a"
url: "/docs/linux/man/5-aliases-postfix/"
description: "aliases – Postfix local alias database format"
---

<p>aliases &#8211; Postfix local alias database format</p>
<h2>Synopsis</h2>
<p><code>newaliases</code></p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) table provides a system-wide mechanism to redirect mail for local recipients. The redirections are processed by the Postfix <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent. </p>
<p> Normally, the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) table is specified as a text file that serves as input to the <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) command. The result, an indexed file in <code>dbm</code> or <code>db</code> format, is used for fast lookup by the mail system. Execute the command <code>newaliases</code> in order to rebuild the indexed file after changing the Postfix alias database. </p>
<p> When the table is provided via other means such as NIS, LDAP or SQL, the same lookups are done as for ordinary indexed files. </p>
<p> Alternatively, the table can be provided as a regular-expression map where patterns are given as regular expressions. In this case, the lookups are done in a slightly different way as described below under &quot;REGULAR EXPRESSION TABLES&quot;. </p>
<p> Users can control delivery of their own mail by setting up <code>.forward</code> files in their home directory. Lines in per-user <code>.forward</code> files have the same syntax as the right-hand side of <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) entries. </p>
<p> The format of the alias database input file is as follows:</p>
<dl>
<dt>&bull;</p>
<dd>An alias definition has the form </p>
<pre> <i>name</i>: <i>value1</i>, <i>value2</i>, <i>...</i></pre>
<dt>&bull;</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>&bull;</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<p> The <i>name</i> is a local address (no domain part). Use double quotes when the name contains any special characters such as whitespace, `#&#8217;, `:&#8217;, or `@&#8217;. The <i>name</i> is folded to lowercase, in order to make database lookups case insensitive. </p>
<p> In addition, when an alias exists for <code>owner-</code><i>name</i>, delivery diagnostics are directed to that address, instead of to the originator of the message. This is typically used to direct delivery errors to the maintainer of a mailing list, who is in a better position to deal with mailing list delivery problems than the originator of the undelivered mail. </p>
<p> The <i>value</i> contains one or more of the following:</p>
<dl>
<dt><i>address</i></p>
<dd>Mail is forwarded to <i>address</i>, which is compatible with the RFC 822 standard.</p>
<dt><i>/file/name</i></p>
<dd>Mail is appended to <i>/file/name</i>. See <code><a href="/docs/linux/man/8-local/">local</a></code>(8) for details of delivery to file. Delivery is not limited to regular files. For example, to dispose of unwanted mail, deflect it to <code>/dev/null</code>.</p>
<dt>|<i>command</i></p>
<dd>Mail is piped into <i>command</i>. Commands that contain special characters, such as whitespace, should be enclosed between double quotes. See <code><a href="/docs/linux/man/8-local/">local</a></code>(8) for details of delivery to command. </p>
<p> When the command fails, a limited amount of command output is mailed back to the sender. The file <code>/usr/include/sysexits.h</code> defines the expected exit status codes. For example, use <code>&quot;|exit 67&quot;</code> to simulate a &quot;user unknown&quot; error, and <code>&quot;|exit 0&quot;</code> to implement an expensive black hole.</p>
<dt><code>:include:</code><i>/file/name</i></p>
<dd>Mail is sent to the destinations listed in the named file. Lines in <code>:include:</code> files have the same syntax as the right-hand side of alias entries. </p>
<p> A destination can be any destination that is described in this manual page. However, delivery to &quot;|<i>command</i>&quot; and <i>/file/name</i> is disallowed by default. To enable, edit the <code>allow_mail_to_commands</code> and <code>allow_mail_to_files</code> configuration parameters.</dl>
<h2>Address Extension</h2>
<p>When alias database search fails, and the recipient localpart contains the optional recipient delimiter (e.g., <i>user+foo</i>), the search is repeated for the unextended address (e.g., <i>user</i>). </p>
<p> The <code>propagate_unmatched_extensions</code> parameter controls whether an unmatched address extension (<i>+foo</i>) is propagated to the result of table lookup.</p>
<h2>Case Folding</h2>
<p>The <a href="/docs/linux/man/8-local/">local</a>(8) delivery agent always folds the search string to lowercase before database lookup.</p>
<h2>Regular Expression Tables</h2>
<p>This section describes how the table lookups change when the table is given in the form of regular expressions. For a description of regular expression lookup table syntax, see <code><a href="/docs/linux/man/5-regexp_table/">regexp_table</a></code>(5) or <code><a href="/docs/linux/man/5-pcre_table/">pcre_table</a></code>(5). NOTE: these formats do not use &quot;:&quot; at the end of a pattern. </p>
<p> Each regular expression is applied to the entire search string. Thus, a search string <i>user+foo</i> is not broken up into <i>user</i> and <i>foo</i>. </p>
<p> Regular expressions are applied in the order as specified in the table, until a regular expression is found that matches the search string. </p>
<p> Lookup results are the same as with indexed file lookups. For security reasons there is no support for <code>$1</code>, <code>$2</code> etc. substring interpolation.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent disallows regular expression substitution of $1 etc. in <code>alias_maps</code>, because that would open a security hole. </p>
<p> The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent will silently ignore requests to use the <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server within <code>alias_maps</code>. Instead it will open the table directly. Before Postfix version 2.2, the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent will terminate with a fatal error.</p>
<h2>Configuration Parameters</h2>
<p>The following <code>main.cf</code> parameters are especially relevant. The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>alias_database</code></p>
<dd>List of alias databases that are updated by the <code><a href="/docs/linux/man/1-newaliases/">newaliases</a></code>(1) command.</p>
<dt><code>alias_maps</code></p>
<dd>List of alias databases queried by the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent.</p>
<dt><code>allow_mail_to_commands</code></p>
<dd>Restrict the usage of mail delivery to external command.</p>
<dt><code>allow_mail_to_files</code></p>
<dd>Restrict the usage of mail delivery to external file.</p>
<dt><code>expand_owner_alias</code></p>
<dd>When delivering to an alias that has an <code>owner-</code> companion alias, set the envelope sender address to the right-hand side of the owner alias, instead using of the left-hand side address.</p>
<dt><code>propagate_unmatched_extensions</code></p>
<dd>A list of address rewriting or forwarding mechanisms that propagate an address extension from the original address to the result. Specify zero or more of <code>canonical</code>, <code>virtual</code>, <code>alias</code>, <code>forward</code>, <code>include</code>, or <code>generic</code>.</p>
<dt><code>owner_request_special</code></p>
<dd>Give special treatment to <code>owner-</code><i>listname</i> and <i>listname</i><code>-request</code> addresses.</p>
<dt><code>recipient_delimiter</code></p>
<dd>Delimiter that separates recipients from address extensions.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>frozen_delivered_to</code></p>
<dd>Update the <a href="/docs/linux/man/8-local/">local</a>(8) delivery agent&#8217;s Delivered-To: address (see prepend_delivered_header) only once, at the start of a delivery; do not update the Delivered-To: address while expanding aliases or .forward files.</dl>
<h2>Standards</h2>
<pre>RFC 822 (ARPA Internet Text Messages)</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-local/">local</a>(8), local delivery agent
<a href="//www.systutorials.com/docs/linux/man/1-newaliases/">newaliases</a>(1), create/update alias database
<a href="//www.systutorials.com/docs/linux/man/1-postalias/">postalias</a>(1), create/update alias database
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
