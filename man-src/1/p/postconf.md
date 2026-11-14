---
title: "postconf(1)"
name: "postconf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postconf/"
description: "postconf – Postfix configuration utility"
---

<h2 class="name">NAME</h2>
<p> postconf &#8211; Postfix configuration utility </p>
<h2>SYNOPSIS</h2>
<p> <code>Managing main.cf:</code> </p>
<p> <code>postconf</code> [<code>-dfhHnopvx</code>] [<code>-c </code><i>config_dir</i>] [<code>-C </code><i>class,&#8230;</i>] [<i>parameter &#8230;</i>] </p>
<p> <code>postconf</code> [<code>-epv</code>] [<code>-c </code><i>config_dir</i>] <i>parameter</i><code>=</code><i>value &#8230;</i> </p>
<p> <code>postconf</code> <code>-#</code> [<code>-pv</code>] [<code>-c </code><i>config_dir</i>] <i>parameter &#8230;</i> </p>
<p> <code>postconf</code> <code>-X</code> [<code>-pv</code>] [<code>-c </code><i>config_dir</i>] <i>parameter &#8230;</i> </p>
<p> <code>Managing master.cf service entries:</code> </p>
<p> <code>postconf</code> <code>-M</code> [<code>-fovx</code>] [<code>-c </code><i>config_dir</i>] [<i>service</i>[<code>/</code><i>type</i>]<i> &#8230;</i>] </p>
<p> <code>postconf</code> <code>-M</code> [<code>-ev</code>] [<code>-c </code><i>config_dir</i>] <i>service</i><code>/</code><i>type</i><code>=</code><i>value &#8230;</i> </p>
<p> <code>postconf</code> <code>-M#</code> [<code>-v</code>] [<code>-c </code><i>config_dir</i>] <i>service</i><code>/</code><i>type &#8230;</i> </p>
<p> <code>postconf</code> <code>-MX</code> [<code>-v</code>] [<code>-c </code><i>config_dir</i>] <i>service</i><code>/</code><i>type &#8230;</i> </p>
<p> <code>Managing master.cf service fields:</code> </p>
<p> <code>postconf</code> <code>-F</code> [<code>-fhHovx</code>] [<code>-c </code><i>config_dir</i>] [<i>service</i>[<code>/</code><i>type</i>[<code>/</code><i>field</i>]]<i> &#8230;</i>] </p>
<p> <code>postconf</code> <code>-F</code> [<code>-ev</code>] [<code>-c </code><i>config_dir</i>] <i>service</i><code>/</code><i>type</i><code>/</code><i>field</i><code>=</code><i>value &#8230;</i> </p>
<p> <code>Managing master.cf service parameters:</code> </p>
<p> <code>postconf</code> <code>-P</code> [<code>-fhHovx</code>] [<code>-c </code><i>config_dir</i>] [<i>service</i>[<code>/</code><i>type</i>[<code>/</code><i>parameter</i>]]<i> &#8230;</i>] </p>
<p> <code>postconf</code> <code>-P</code> [<code>-ev</code>] [<code>-c </code><i>config_dir</i>] <i>service</i><code>/</code><i>type</i><code>/</code><i>parameter</i><code>=</code><i>value &#8230;</i> </p>
<p> <code>postconf</code> <code>-PX</code> [<code>-v</code>] [<code>-c </code><i>config_dir</i>] <i>service</i><code>/</code><i>type</i><code>/</code><i>parameter &#8230;</i> </p>
<p> <code>Managing bounce message templates:</code> </p>
<p> <code>postconf</code> <code>-b</code> [<code>-v</code>] [<code>-c </code><i>config_dir</i>] [<i>template_file</i>] </p>
<p> <code>postconf</code> <code>-t</code> [<code>-v</code>] [<code>-c </code><i>config_dir</i>] [<i>template_file</i>] </p>
<p> <code>Managing TLS features:</code> </p>
<p> <code>postconf</code> <code>-T </code><i>mode</i> [<code>-v</code>] [<code>-c </code><i>config_dir</i>] </p>
<p> <code>Managing other configuration:</code> </p>
<p> <code>postconf</code> <code>-a</code>|<code>-A</code>|<code>-l</code>|<code>-m</code> [<code>-v</code>] [<code>-c </code><i>config_dir</i>]</p>
<h2>DESCRIPTION</h2>
<p> By default, the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command displays the values of <code>main.cf</code> configuration parameters, and warns about possible mis-typed parameter names (Postfix 2.9 and later). The command can also change <code>main.cf</code> configuration parameter values, or display other configuration information about the Postfix mail system. </p>
<p> Options:</p>
<dl>
<dt><code>-a</code></p>
<dd> List the available SASL plug-in types for the Postfix SMTP server. The plug-in type is selected with the <code>smtpd_sasl_type</code> configuration parameter by specifying one of the names listed below.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cyrus</code></p>
<dd> This server plug-in is available when Postfix is built with Cyrus SASL support.</p>
<dt><code>dovecot</code></p>
<dd> This server plug-in uses the Dovecot authentication server, and is available when Postfix is built with any form of SASL support.</dl>
</dl>
<dt>
<dd> This feature is available with Postfix 2.3 and later.</p>
<dt><code>-A</code></p>
<dd> List the available SASL plug-in types for the Postfix SMTP client. The plug-in type is selected with the <code>smtp_sasl_type</code> or <code>lmtp_sasl_type</code> configuration parameters by specifying one of the names listed below.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cyrus</code></p>
<dd> This client plug-in is available when Postfix is built with Cyrus SASL support.</dl>
</dl>
<dt>
<dd> This feature is available with Postfix 2.3 and later.</p>
<dt><code>-b</code> [<i>template_file</i>]</p>
<dd> Display the message text that appears at the beginning of delivery status notification (DSN) messages, expanding $<code>name</code> expressions with actual values as described in <code><a href="/docs/linux/man/5-bounce/">bounce</a></code>(5). </p>
<p> To override the <code>bounce_template_file</code> parameter setting, specify a template file name at the end of the &quot;<code>postconf -b</code>&quot; command line. Specify an empty file name to display built-in templates (in shell language: &quot;&quot;). </p>
<p> This feature is available with Postfix 2.3 and later.</p>
<dt><code>-c </code><i>config_dir</i></p>
<dd> The <code>main.cf</code> configuration file is in the named directory instead of the default configuration directory.</p>
<dt><code>-C </code><i>class,&#8230;</i></p>
<dd> When displaying <code>main.cf</code> parameters, select only parameters from the specified class(es):</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>builtin</code></p>
<dd> Parameters with built-in names.</p>
<dt><code>service</code></p>
<dd> Parameters with service-defined names (the first field of a <code>master.cf</code> entry plus a Postfix-defined suffix).</p>
<dt><code>user</code></p>
<dd> Parameters with user-defined names.</p>
<dt><code>all</code></p>
<dd> All the above classes.</dl>
</dl>
<dt>
<dd> The default is as if &quot;<code>-C all</code>&quot; is specified. </p>
<p> This feature is available with Postfix 2.9 and later.</p>
<dt><code>-d</code></p>
<dd> Print <code>main.cf</code> default parameter settings instead of actual settings. Specify <code>-df</code> to fold long lines for human readability (Postfix 2.9 and later).</p>
<dt><code>-e</code></p>
<dd> Edit the <code>main.cf</code> configuration file, and update parameter settings with the &quot;<i>name=value</i>&quot; pairs on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. </p>
<p> With <code>-M</code>, edit the <code>master.cf</code> configuration file, and replace one or more service entries with new values as specified with &quot;<i>service/type=value</i>&quot; on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. </p>
<p> With <code>-F</code>, edit the <code>master.cf</code> configuration file, and replace one or more service fields with new values as specified with &quot;<i>service/type/field=value</i>&quot; on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. Currently, the &quot;command&quot; field contains the command name and command arguments. this may change in the near future, so that the &quot;command&quot; field contains only the command name, and a new &quot;arguments&quot; pseudofield contains the command arguments. </p>
<p> With <code>-P</code>, edit the <code>master.cf</code> configuration file, and add or update one or more service parameter settings (-o parameter=value settings) with new values as specified with &quot;<i>service/type/parameter=value</i>&quot; on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. </p>
<p> In all cases the file is copied to a temporary file then renamed into place. Specify quotes to protect special characters and whitespace on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. </p>
<p> The <code>-e</code> option is no longer needed with Postfix version 2.8 and later.</p>
<dt><code>-f</code></p>
<dd> Fold long lines when printing <code>main.cf</code> or <code>master.cf</code> configuration file entries, for human readability. </p>
<p> This feature is available with Postfix 2.9 and later.</p>
<dt><code>-F</code></p>
<dd> Show <code>master.cf</code> per-entry field settings (by default all services and all fields), formatted as &quot;<i>service/type/field=value</i>&quot;, one per line. Specify <code>-Ff</code> to fold long lines. </p>
<p> Specify one or more &quot;<i>service/type/field</i>&quot; instances on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line to limit the output to fields of interest. Trailing parameter name or service type fields that are omitted will be handled as &quot;*&quot; wildcard fields. </p>
<p> This feature is available with Postfix 2.11 and later.</p>
<dt><code>-h</code></p>
<dd> Show parameter or attribute values without the &quot;<i>name</i> = &quot; label that normally precedes the value.</p>
<dt><code>-H</code></p>
<dd> Show parameter or attribute names without the &quot; = <i>value</i>&quot; that normally follows the name. </p>
<p> This feature is available with Postfix 3.1 and later.</p>
<dt><code>-l</code></p>
<dd> List the names of all supported mailbox locking methods. Postfix supports the following methods:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>flock</code></p>
<dd> A kernel-based advisory locking method for local files only. This locking method is available on systems with a BSD compatible library.</p>
<dt><code>fcntl</code></p>
<dd> A kernel-based advisory locking method for local and remote files.</p>
<dt><code>dotlock</code></p>
<dd> An application-level locking method. An application locks a file named <i>filename</i> by creating a file named <i>filename</i><code>.lock</code>. The application is expected to remove its own lock file, as well as stale lock files that were left behind after abnormal program termination.</dl>
</dl>
<dt><code>-m</code></p>
<dd> List the names of all supported lookup table types. In Postfix configuration files, lookup tables are specified as <i>type</i><code>:</code><i>name</i>, where <i>type</i> is one of the types listed below. The table <i>name</i> syntax depends on the lookup table type as described in the DATABASE_README document.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>btree</code></p>
<dd> A sorted, balanced tree structure. Available on systems with support for Berkeley DB databases.</p>
<dt><code>cdb</code></p>
<dd> A read-optimized structure with no support for incremental updates. Available on systems with support for CDB databases. </p>
<p> This feature is available with Postfix 2.2 and later.</p>
<dt><code>cidr</code></p>
<dd> A table that associates values with Classless Inter-Domain Routing (CIDR) patterns. This is described in <code><a href="/docs/linux/man/5-cidr_table/">cidr_table</a></code>(5). </p>
<p> This feature is available with Postfix 2.2 and later.</p>
<dt><code>dbm</code></p>
<dd> An indexed file type based on hashing. Available on systems with support for DBM databases.</p>
<dt><code>environ</code></p>
<dd> The UNIX process environment array. The lookup key is the environment variable name; the table name is ignored. Originally implemented for testing, someone may find this useful someday.</p>
<dt><code>fail</code></p>
<dd> A table that reliably fails all requests. The lookup table name is used for logging. This table exists to simplify Postfix error tests. </p>
<p> This feature is available with Postfix 2.9 and later.</p>
<dt><code>hash</code></p>
<dd> An indexed file type based on hashing. Available on systems with support for Berkeley DB databases.</p>
<dt><code>inline</code> (read-only)</p>
<dd> A non-shared, in-memory lookup table. Example: &quot;<code>inline:{ </code><i>key</i><code>=</code><i>value</i><code>, { </code><i>key</i><code> = </code><i>text with whitespace or comma</i><code> }}</code>&quot;. Key-value pairs are separated by whitespace or comma; with a key-value pair inside &quot;<code>{}</code>&quot;, whitespace is ignored after the opening &quot;<code>{</code>&quot;, around the &quot;<code>=</code>&quot; between key and value, and before the closing &quot;<code>}</code>&quot;. Inline tables eliminate the need to create a database file for just a few fixed elements. See also the <i>static:</i> map type. </p>
<p> This feature is available with Postfix 3.0 and later.</p>
<dt><code>internal</code></p>
<dd> A non-shared, in-memory hash table. Its content are lost when a process terminates.</p>
<dt><code>lmdb</code></p>
<dd> OpenLDAP LMDB database (a memory-mapped, persistent file). Available on systems with support for LMDB databases. This is described in <code><a href="/docs/linux/man/5-lmdb_table/">lmdb_table</a></code>(5). </p>
<p> This feature is available with Postfix 2.11 and later.</p>
<dt><code>ldap</code> (read-only)</p>
<dd> LDAP database client. This is described in <code><a href="/docs/linux/man/5-ldap_table/">ldap_table</a></code>(5).</p>
<dt><code>memcache</code></p>
<dd> Memcache database client. This is described in <code><a href="/docs/linux/man/5-memcache_table/">memcache_table</a></code>(5). </p>
<p> This feature is available with Postfix 2.9 and later.</p>
<dt><code>mysql</code> (read-only)</p>
<dd> MySQL database client. Available on systems with support for MySQL databases. This is described in <code><a href="/docs/linux/man/5-mysql_table/">mysql_table</a></code>(5).</p>
<dt><code>pcre</code> (read-only)</p>
<dd> A lookup table based on Perl Compatible Regular Expressions. The file format is described in <code><a href="/docs/linux/man/5-pcre_table/">pcre_table</a></code>(5).</p>
<dt><code>pgsql</code> (read-only)</p>
<dd> PostgreSQL database client. This is described in <code><a href="/docs/linux/man/5-pgsql_table/">pgsql_table</a></code>(5). </p>
<p> This feature is available with Postfix 2.1 and later.</p>
<dt><code>pipemap</code> (read-only)</p>
<dd> A lookup table that constructs a pipeline of tables. Example: &quot;<code>pipemap:{</code><i>type_1:name_1, &#8230;, type_n:name_n</i><code>}</code>&quot;. Each &quot;pipemap:&quot; query is given to the first table. Each lookup result becomes the query for the next table in the pipeline, and the last table produces the final result. When any table lookup produces no result, the pipeline produces no result. The first and last characters of the &quot;pipemap:&quot; table name must be &quot;<code>{</code>&quot; and &quot;<code>}</code>&quot;. Within these, individual maps are separated with comma or whitespace. </p>
<p> This feature is available with Postfix 3.0 and later.</p>
<dt><code>proxy</code></p>
<dd> Postfix <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) client for shared access to Postfix databases. The table name syntax is <i>type</i><code>:</code><i>name</i>. </p>
<p> This feature is available with Postfix 2.0 and later.</p>
<dt><code>randmap</code> (read-only)</p>
<dd> An in-memory table that performs random selection. Example: &quot;<code>randmap:{</code><i>result_1, &#8230;, result_n</i><code>}</code>&quot;. Each table query returns a random choice from the specified results. The first and last characters of the &quot;randmap:&quot; table name must be &quot;<code>{</code>&quot; and &quot;<code>}</code>&quot;. Within these, individual results are separated with comma or whitespace. To give a specific result more weight, specify it multiple times. </p>
<p> This feature is available with Postfix 3.0 and later.</p>
<dt><code>regexp</code> (read-only)</p>
<dd> A lookup table based on regular expressions. The file format is described in <code><a href="/docs/linux/man/5-regexp_table/">regexp_table</a></code>(5).</p>
<dt><code>sdbm</code></p>
<dd> An indexed file type based on hashing. Available on systems with support for SDBM databases. </p>
<p> This feature is available with Postfix 2.2 and later.</p>
<dt><code>socketmap</code> (read-only)</p>
<dd> Sendmail-style socketmap client. The table name is <code>inet</code>:<i>host</i>:<i>port</i>:<i>name</i> for a TCP/IP server, or <code>unix</code>:<i>pathname</i>:<i>name</i> for a UNIX-domain server. This is described in <code><a href="/docs/linux/man/5-socketmap_table/">socketmap_table</a></code>(5). </p>
<p> This feature is available with Postfix 2.10 and later.</p>
<dt><code>sqlite</code> (read-only)</p>
<dd> SQLite database. This is described in <code><a href="/docs/linux/man/5-sqlite_table/">sqlite_table</a></code>(5). </p>
<p> This feature is available with Postfix 2.8 and later.</p>
<dt><code>static</code> (read-only)</p>
<dd> A table that always returns its name as lookup result. For example, <code>static:foobar</code> always returns the string <code>foobar</code> as lookup result. Specify &quot;<code>static:{ </code><i>text with whitespace</i><code> }</code>&quot; when the result contains whitespace; this form ignores whitespace after the opening &quot;<code>{</code>&quot; and before the closing &quot;<code>}</code>&quot;. See also the <i>inline:</i> map. </p>
<p> The form &quot;<code>static:{</code><i>text</i><code>}</code> is available with Postfix 3.0 and later.</p>
<dt><code>tcp</code> (read-only)</p>
<dd> TCP/IP client. The protocol is described in <code><a href="/docs/linux/man/5-tcp_table/">tcp_table</a></code>(5).</p>
<dt><code>texthash</code> (read-only)</p>
<dd> Produces similar results as hash: files, except that you don&#8217;t need to run the <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) command before you can use the file, and that it does not detect changes after the file is read. </p>
<p> This feature is available with Postfix 2.8 and later.</p>
<dt><code>unionmap</code> (read-only)</p>
<dd> A table that sends each query to multiple lookup tables and that concatenates all found results, separated by comma. The table name syntax is the same as for <code>pipemap</code>. </p>
<p> This feature is available with Postfix 3.0 and later.</p>
<dt><code>unix</code> (read-only)</p>
<dd> A limited view of the UNIX authentication database. The following tables are implemented:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>unix:passwd.byname</code></p>
<dd> The table is the UNIX password database. The key is a login name. The result is a password file entry in <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5) format.</p>
<dt><code>unix:group.byname</code></p>
<dd> The table is the UNIX group database. The key is a group name. The result is a group file entry in <code><a href="/docs/linux/man/5-group/">group</a></code>(5) format.</dl>
</dl>
</dl>
</dl>
<dt>
<dd> Other table types may exist depending on how Postfix was built.</p>
<dt><code>-M</code></p>
<dd> Show <code>master.cf</code> file contents instead of <code>main.cf</code> file contents. Specify <code>-Mf</code> to fold long lines for human readability. </p>
<p> Specify zero or more arguments, each with a <i>service-name</i> or <i>service-name/service-type</i> pair, where <i>service-name</i> is the first field of a master.cf entry and <i>service-type</i> is one of (<code>inet</code>, <code>unix</code>, <code>fifo</code>, or <code>pass</code>). </p>
<p> If <i>service-name</i> or <i>service-name/service-type</i> is specified, only the matching master.cf entries will be output. For example, &quot;<code>postconf -Mf smtp</code>&quot; will output all services named &quot;smtp&quot;, and &quot;<code>postconf -Mf smtp/inet</code>&quot; will output only the smtp service that listens on the network. Trailing service type fields that are omitted will be handled as &quot;*&quot; wildcard fields. </p>
<p> This feature is available with Postfix 2.9 and later. The syntax was changed from &quot;<i>name.type</i>&quot; to &quot;<i>name/type</i>&quot;, and &quot;*&quot; wildcard support was added with Postfix 2.11.</p>
<dt><code>-n</code></p>
<dd> Show only configuration parameters that have explicit <i>name=value</i> settings in <code>main.cf</code>. Specify <code>-nf</code> to fold long lines for human readability (Postfix 2.9 and later). To show settings that differ from built-in defaults only, use the following bash syntax: </p>
<pre>
    comm -23 &lt;(postconf -n) &lt;(postconf -d)
</pre>
<p> Replace &quot;-23&quot; with &quot;-12&quot; to show settings that duplicate built-in defaults.</p>
<dt><code>-o </code><i>name=value</i></p>
<dd> Override <code>main.cf</code> parameter settings. </p>
<p> This feature is available with Postfix 2.10 and later.</p>
<dt><code>-p</code></p>
<dd> Show <code>main.cf</code> parameter settings. This is the default. </p>
<p> This feature is available with Postfix 2.11 and later.</p>
<dt><code>-P</code></p>
<dd> Show <code>master.cf</code> service parameter settings (by default all services and all parameters), formatted as &quot;<i>service/type/parameter=value</i>&quot;, one per line. Specify <code>-Pf</code> to fold long lines. </p>
<p> Specify one or more &quot;<i>service/type/parameter</i>&quot; instances on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line to limit the output to parameters of interest. Trailing parameter name or service type fields that are omitted will be handled as &quot;*&quot; wildcard fields. </p>
<p> This feature is available with Postfix 2.11 and later.</p>
<dt><code>-t</code> [<i>template_file</i>]</p>
<dd> Display the templates for text that appears at the beginning of delivery status notification (DSN) messages, without expanding $<code>name</code> expressions. </p>
<p> To override the <code>bounce_template_file</code> parameter setting, specify a template file name at the end of the &quot;<code>postconf -t</code>&quot; command line. Specify an empty file name to display built-in templates (in shell language: &quot;&quot;). </p>
<p> This feature is available with Postfix 2.3 and later.</p>
<dt><code>-T </code><i>mode</i></p>
<dd> If Postfix is compiled without TLS support, the <code>-T</code> option produces no output. Otherwise, if an invalid <i>mode</i> is specified, the <code>-T</code> option reports an error and exits with a non-zero status code. The valid modes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>compile-version</code></p>
<dd> Output the OpenSSL version that Postfix was compiled with (i.e. the OpenSSL version in a header file). The output format is the same as with the command &quot;<code>openssl version</code>&quot;.</p>
<dt><code>run-version</code></p>
<dd> Output the OpenSSL version that Postfix is linked with at runtime (i.e. the OpenSSL version in a shared library).</p>
<dt><code>public-key-algorithms</code></p>
<dd> Output the lower-case names of the supported public-key algorithms, one per-line.</dl>
</dl>
<dt>
<dd> This feature is available with Postfix 3.1 and later.</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</p>
<dt><code>-x</code></p>
<dd> Expand <i>$name</i> in <code>main.cf</code> or <code>master.cf</code> parameter values. The expansion is recursive. </p>
<p> This feature is available with Postfix 2.10 and later.</p>
<dt><code>-X</code></p>
<dd> Edit the <code>main.cf</code> configuration file, and remove the parameters named on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. Specify a list of parameter names, not &quot;<i>name=value</i>&quot; pairs. </p>
<p> With <code>-M</code>, edit the <code>master.cf</code> configuration file, and remove one or more service entries as specified with &quot;<i>service/type</i>&quot; on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. </p>
<p> With <code>-P</code>, edit the <code>master.cf</code> configuration file, and remove one or more service parameter settings (-o parameter=value settings) as specified with &quot;<i>service/type/parameter</i>&quot; on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. </p>
<p> In all cases the file is copied to a temporary file then renamed into place. Specify quotes to protect special characters on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. </p>
<p> There is no <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command to perform the reverse operation. </p>
<p> This feature is available with Postfix 2.10 and later. Support for -M and -P was added with Postfix 2.11.</p>
<dt><code>-#</code></p>
<dd> Edit the <code>main.cf</code> configuration file, and comment out the parameters named on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line, so that those parameters revert to their default values. Specify a list of parameter names, not &quot;<i>name=value</i>&quot; pairs. </p>
<p> With <code>-M</code>, edit the <code>master.cf</code> configuration file, and comment out one or more service entries as specified with &quot;<i>service/type</i>&quot; on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. </p>
<p> In all cases the file is copied to a temporary file then renamed into place. Specify quotes to protect special characters on the <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command line. </p>
<p> There is no <code><a href="/docs/linux/man/1-postconf/">postconf</a></code>(1) command to perform the reverse operation. </p>
<p> This feature is available with Postfix 2.6 and later. Support for -M was added with Postfix 2.11.</dl>
<h2>DIAGNOSTICS</h2>
<p> Problems are reported to the standard error stream.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd> Directory with Postfix configuration files.</dl>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>bounce_template_file (empty)</code></p>
<dd> Pathname of a configuration file with bounce message templates.</dl>
<h2>FILES</h2>
<pre>
/etc/postfix/main.cf, Postfix configuration parameters
/etc/postfix/master.cf, Postfix master daemon configuration
</pre>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/5-bounce/">bounce</a>(5), bounce template file format
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), master.cf configuration file syntax
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), main.cf configuration file syntax
</pre>
<h2>README FILES</h2>
<p> Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>
DATABASE_README, Postfix lookup table overview
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
</pre>
<h2>Index</h2>
