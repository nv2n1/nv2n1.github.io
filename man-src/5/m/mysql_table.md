---
title: "mysql_table(5)"
name: "mysql_table"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mysql_table/"
description: "mysql_table – Postfix MySQL client configuration"
---

<p>mysql_table &#8211; Postfix MySQL client configuration</p>
<h2>Synopsis</h2>
<pre><code>postmap -q &quot;</code><i>string</i><code>&quot; mysql:/etc/postfix/filename</code>
<code>postmap -q - mysql:/etc/postfix/</code><i>filename</i> &lt;<i>inputfile</i></pre>
<h2>Description</h2>
<p>The Postfix mail system uses optional tables for address rewriting or mail routing. These tables are usually in <code>dbm</code> or <code>db</code> format. </p>
<p> Alternatively, lookup tables can be specified as MySQL databases. In order to use MySQL lookups, define a MySQL source as a lookup table in main.cf, for example: </p>
<pre> alias_maps = mysql:/etc/mysql-aliases.cf</pre>
<p>The file /etc/postfix/mysql-aliases.cf has the same format as the Postfix main.cf file, and can specify the parameters described below.</p>
<h2>Backwards Compatibility</h2>
<p>For compatibility with other Postfix lookup tables, MySQL parameters can also be defined in main.cf. In order to do that, specify as MySQL source a name that doesn&#8217;t begin with a slash or a dot. The MySQL parameters will then be accessible as the name you&#8217;ve given the source in its definition, an underscore, and the name of the parameter. For example, if the map is specified as &quot;mysql:<i>mysqlname</i>&quot;, the parameter &quot;hosts&quot; below would be defined in main.cf as &quot;<i>mysqlname</i>_hosts&quot;. </p>
<p> Note: with this form, the passwords for the MySQL sources are written in main.cf, which is normally world-readable. Support for this form will be removed in a future Postfix version. </p>
<p> Normally, the SQL query is specified via a single <code>query</code> parameter (described in more detail below). When this parameter is not specified in the map definition, Postfix reverts to an older interface, with the SQL query constructed from the <code>select_field</code>, <code>table</code>, <code>where_field</code> and <code>additional_conditions</code> parameters. The old interface will be gradually phased out. To migrate to the new interface set: </p>
<pre> <code>query</code> = SELECT [<i>select_field</i>]
 FROM [<i>table</i>]
 WHERE [<i>where_field</i>] = '%s'
 [<i>additional_conditions</i>]</pre>
<p>Insert the value, not the name, of each legacy parameter. Note that the <code>additional_conditions</code> parameter is optional and if not empty, will always start with <code>AND</code>.</p>
<h2>List Membership</h2>
<p>When using SQL to store lists such as $mynetworks, $mydestination, $relay_domains, $local_recipient_maps, etc., it is important to understand that the table must store each list member as a separate key. The table lookup verifies the *existence* of the key. See &quot;Postfix lists versus tables&quot; in the DATABASE_README document for a discussion. </p>
<p> Do NOT create tables that return the full list of domains in $mydestination or $relay_domains etc., or IP addresses in $mynetworks. </p>
<p> DO create tables with each matching item as a key and with an arbitrary value. With SQL databases it is not uncommon to return the key itself or a constant value.</p>
<h2>Mysql Parameters</h2>
<dl>
<dt><code>hosts</code></p>
<dd>The hosts that Postfix will try to connect to and query from. Specify <i>unix:</i> for UNIX domain sockets, <i>inet:</i> for TCP connections (default). Example: </p>
<pre> hosts = host1.some.domain host2.some.domain:port
 hosts = unix:/file/name</pre>
<p>The hosts are tried in random order, with all connections over UNIX domain sockets being tried before those over TCP. The connections are automatically closed after being idle for about 1 minute, and are re-opened as necessary. Postfix versions 2.0 and earlier do not randomize the host order. </p>
<p> NOTE: if you specify localhost as a hostname (even if you prefix it with <i>inet:</i>), MySQL will connect to the default UNIX domain socket. In order to instruct MySQL to connect to localhost over TCP you have to specify </p>
<pre> hosts = 127.0.0.1</pre>
<dt><code>user, password</code></p>
<dd>The user name and password to log into the mysql server. Example: </p>
<pre> user = someone
 password = some_password</pre>
<dt><code>dbname</code></p>
<dd>The database name on the servers. Example: </p>
<pre> dbname = customer_database</pre>
<dt><code>query</code></p>
<dd>The SQL query template used to search the database, where <code>%s</code> is a substitute for the address Postfix is trying to resolve, e.g. </p>
<pre> query = SELECT replacement FROM aliases WHERE mailbox = '%s'</pre>
<p>This parameter supports the following &#8216;%&#8217; expansions:</p>
<dl>
<dd>
<dl>
<dt><code>%%</code></p>
<dd>This is replaced by a literal &#8216;%&#8217; character.</p>
<dt><code>%s</code></p>
<dd>This is replaced by the input key. SQL quoting is used to make sure that the input key does not add unexpected metacharacters.</p>
<dt><code>%u</code></p>
<dd>When the input key is an address of the form user [at] domain, <code>%u</code> is replaced by the SQL quoted local part of the address. Otherwise, <code>%u</code> is replaced by the entire search string. If the localpart is empty, the query is suppressed and returns no results.</p>
<dt><code>%d</code></p>
<dd>When the input key is an address of the form user [at] domain, <code>%d</code> is replaced by the SQL quoted domain part of the address. Otherwise, the query is suppressed and returns no results.</p>
<dt><code>%[SUD]</code></p>
<dd>The upper-case equivalents of the above expansions behave in the <code>query</code> parameter identically to their lower-case counter-parts. With the <code>result_format</code> parameter (see below), they expand the input key rather than the result value.</p>
<dt><code>%[1-9]</code></p>
<dd>The patterns %1, %2, &#8230; %9 are replaced by the corresponding most significant component of the input key&#8217;s domain. If the input key is <i>user [at] mail.example.com</i>, then %1 is <code>com</code>, %2 is <code>example</code> and %3 is <code>mail</code>. If the input key is unqualified or does not have enough domain components to satisfy all the specified patterns, the query is suppressed and returns no results.</dl>
</dl>
<dd>The <code>domain</code> parameter described below limits the input keys to addresses in matching domains. When the <code>domain</code> parameter is non-empty, SQL queries for unqualified addresses or addresses in non-matching domains are suppressed and return no results. </p>
<p> This parameter is available with Postfix 2.2. In prior releases the SQL query was built from the separate parameters: <code>select_field</code>, <code>table</code>, <code>where_field</code> and <code>additional_conditions</code>. The mapping from the old parameters to the equivalent query is: </p>
<pre> SELECT [<code>select_field</code>]
 FROM [<code>table</code>]
 WHERE [<code>where_field</code>] = '%s'
 [<code>additional_conditions</code>]</pre>
<p>The &#8216;%s&#8217; in the <code>WHERE</code> clause expands to the escaped search string. With Postfix 2.2 these legacy parameters are used if the <code>query</code> parameter is not specified. </p>
<p> NOTE: DO NOT put quotes around the query parameter.</p>
<dt><code>result_format (default: %s</code>)</p>
<dd>Format template applied to result attributes. Most commonly used to append (or prepend) text to the result. This parameter supports the following &#8216;%&#8217; expansions:</p>
<dl>
<dd>
<dl>
<dt><code>%%</code></p>
<dd>This is replaced by a literal &#8216;%&#8217; character.</p>
<dt><code>%s</code></p>
<dd>This is replaced by the value of the result attribute. When result is empty it is skipped.</p>
<dt><code>%u</code></p>
<dd>When the result attribute value is an address of the form user [at] domain, <code>%u</code> is replaced by the local part of the address. When the result has an empty localpart it is skipped.</p>
<dt><code>%d</code></p>
<dd>When a result attribute value is an address of the form user [at] domain, <code>%d</code> is replaced by the domain part of the attribute value. When the result is unqualified it is skipped.</p>
<dt><code>%[SUD1-9]</code><code></p>
<dd>The upper-case and decimal digit expansions interpolate the parts of the input key rather than the result. Their behavior is identical to that described with query</code>, and in fact because the input key is known in advance, queries whose key does not contain all the information specified in the result template are suppressed and return no results.</dl>
</dl>
<dd>For example, using &quot;result_format = smtp:[%s]&quot; allows one to use a mailHost attribute as the basis of a <a href="/docs/linux/man/5-transport/">transport</a>(5) table. After applying the result format, multiple values are concatenated as comma separated strings. The expansion_limit and parameter explained below allows one to restrict the number of values in the result, which is especially useful for maps that must return at most one value. </p>
<p> The default value <code>%s</code> specifies that each result value should be used as is. </p>
<p> This parameter is available with Postfix 2.2 and later. </p>
<p> NOTE: DO NOT put quotes around the result format!</p>
<dt><code>domain (default: no domain list)</code></p>
<dd>This is a list of domain names, paths to files, or dictionaries. When specified, only fully qualified search keys with a *non-empty* localpart and a matching domain are eligible for lookup: &#8216;user&#8217; lookups, bare domain lookups and &quot;@domain&quot; lookups are not performed. This can significantly reduce the query load on the MySQL server. </p>
<pre> domain = postfix.org, hash:/etc/postfix/searchdomains</pre>
<p>It is best not to use SQL to store the domains eligible for SQL lookups. </p>
<p> This parameter is available with Postfix 2.2 and later. </p>
<p> NOTE: DO NOT define this parameter for <a href="/docs/linux/man/8-local/">local</a>(8) aliases, because the input keys are always unqualified.</p>
<dt><code>expansion_limit (default: 0)</code></p>
<dd>A limit on the total number of result elements returned (as a comma separated list) by a lookup against the map. A setting of zero disables the limit. Lookups fail with a temporary error if the limit is exceeded. Setting the limit to 1 ensures that lookups do not return multiple values.</dl>
<h2>Obsolete Query Interface</h2>
<p>This section describes an interface that is deprecated as of Postfix 2.2. It is replaced by the more general <code>query</code> interface described above. If the <code>query</code> parameter is defined, the legacy parameters described here ignored. Please migrate to the new interface as the legacy interface may be removed in a future release. </p>
<p> The following parameters can be used to fill in a SELECT template statement of the form: </p>
<pre> SELECT [<code>select_field</code>]
 FROM [<code>table</code>]
 WHERE [<code>where_field</code>] = '%s'
 [<code>additional_conditions</code>]</pre>
<p>The specifier %s is replaced by the search string, and is escaped so if it contains single quotes or other odd characters, it will not cause a parse error, or worse, a security problem.</p>
<dl>
<dt><code>select_field</code></p>
<dd>The SQL &quot;select&quot; parameter. Example: </p>
<pre> <code>select_field</code> = forw_addr</pre>
<dt><code>table</code></p>
<dd>The SQL &quot;select .. from&quot; table name. Example: </p>
<pre> <code>table</code> = mxaliases</pre>
<dt><code>where_field</code></p>
<dd>The SQL &quot;select .. where&quot; parameter. Example: </p>
<pre> <code>where_field</code> = alias</pre>
<dt><code>additional_conditions</code></p>
<dd>Additional conditions to the SQL query. Example: </p>
<pre> <code>additional_conditions</code> = AND status = 'paid'</pre>
</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table maintenance
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-ldap_table/">ldap_table</a>(5), LDAP lookup tables
<a href="//www.systutorials.com/docs/linux/man/5-pgsql_table/">pgsql_table</a>(5), PostgreSQL lookup tables
<a href="//www.systutorials.com/docs/linux/man/5-sqlite_table/">sqlite_table</a>(5), SQLite lookup tables</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview
MYSQL_README, Postfix MYSQL client guide</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<pre>MySQL support was introduced with Postfix version 1.0.</pre>
<h2>Author(S)</h2>
<pre>Original implementation by:
Scott Cotton, Joshua Marcus
IC Group, Inc.
Further enhancements by:
Liviu Daia
Institute of Mathematics of the Romanian Academy
P.O. BOX 1-764
RO-014700 Bucharest, ROMANIA</pre>
