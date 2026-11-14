---
title: "postalias(1)"
name: "postalias"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postalias/"
description: "postalias – Postfix alias database maintenance"
---

<h2 class="name">NAME</h2>
<p> postalias &#8211; Postfix alias database maintenance </p>
<h2>SYNOPSIS</h2>
<p> <code>postalias</code> [<code>-Nfinoprsuvw</code>] [<code>-c </code><i>config_dir</i>] [<code>-d </code><i>key</i>] [<code>-q </code><i>key</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<i>file_type</i>:]<i>file_name</i>&nbsp;&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) command creates or queries one or more Postfix alias databases, or updates an existing one. The input and output file formats are expected to be compatible with Sendmail version 8, and are expected to be suitable for the use as NIS alias maps. </p>
<p> If the result files do not exist they will be created with the same group and other read permissions as their source file. </p>
<p> While a database update is in progress, signal delivery is postponed, and an exclusive, advisory, lock is placed on the entire database, in order to avoid surprises in spectator processes. </p>
<p> The format of Postfix alias input files is described in <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5). </p>
<p> By default the lookup key is mapped to lowercase to make the lookups case insensitive; as of Postfix 2.3 this case folding happens only with tables whose lookup keys are fixed-case strings such as btree:, dbm: or hash:. With earlier versions, the lookup key is folded even with tables where a lookup field can match both upper and lower case text, such as regexp: and pcre:. This resulted in loss of information with $<i>number</i> substitutions. </p>
<p> Options:</p>
<dl>
<dt><code>-c </code><i>config_dir</i></p>
<dd> Read the <code>main.cf</code> configuration file in the named directory instead of the default configuration directory.</p>
<dt><code>-d </code><i>key</i></p>
<dd> Search the specified maps for <i>key</i> and remove one entry per map. The exit status is zero when the requested information was found. </p>
<p> If a key value of <code>&#8211;</code> is specified, the program reads key values from the standard input stream. The exit status is zero when at least one of the requested keys was found.</p>
<dt><code>-f</code></p>
<dd> Do not fold the lookup key to lower case while creating or querying a table. </p>
<p> With Postfix version 2.3 and later, this option has no effect for regular expression tables. There, case folding is controlled by appending a flag to a pattern.</p>
<dt><code>-i</code></p>
<dd> Incremental mode. Read entries from standard input and do not truncate an existing database. By default, <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) creates a new database from the entries in <i>file_name</i>.</p>
<dt><code>-N</code></p>
<dd> Include the terminating null character that terminates lookup keys and values. By default, <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) does whatever is the default for the host operating system.</p>
<dt><code>-n</code></p>
<dd> Don&#8217;t include the terminating null character that terminates lookup keys and values. By default, <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) does whatever is the default for the host operating system.</p>
<dt><code>-o</code></p>
<dd> Do not release root privileges when processing a non-root input file. By default, <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) drops root privileges and runs as the source file owner instead.</p>
<dt><code>-p</code></p>
<dd> Do not inherit the file access permissions from the input file when creating a new file. Instead, create a new file with default access permissions (mode 0644).</p>
<dt><code>-q </code><i>key</i></p>
<dd> Search the specified maps for <i>key</i> and write the first value found to the standard output stream. The exit status is zero when the requested information was found. </p>
<p> Note: this performs a single query with the key as specified, and does not make iterative queries with substrings of the key as described in the <a href="/docs/linux/man/5-aliases/">aliases</a>(5) manual page. </p>
<p> If a key value of <code>&#8211;</code> is specified, the program reads key values from the standard input stream and writes one line of <i>key: value</i> output for each key that was found. The exit status is zero when at least one of the requested keys was found.</p>
<dt><code>-r</code></p>
<dd> When updating a table, do not complain about attempts to update existing entries, and make those updates anyway.</p>
<dt><code>-s</code></p>
<dd> Retrieve all database elements, and write one line of <i>key: value</i> output for each element. The elements are printed in database order, which is not necessarily the same as the original input order. This feature is available in Postfix version 2.2 and later, and is not available for all database types.</p>
<dt><code>-u</code></p>
<dd> Disable UTF-8 support. UTF-8 support is enabled by default when &quot;smtputf8_enable = yes&quot;. It requires that keys and values are valid UTF-8 strings.</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</p>
<dt><code>-w</code></p>
<dd> When updating a table, do not complain about attempts to update existing entries, and ignore those attempts.</dl>
<p> Arguments:</p>
<dl>
<dt><i>file_type</i></p>
<dd> The database type. To find out what types are supported, use the &quot;<code>postconf -m</code>&quot; command. </p>
<p> The <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) command can query any supported file type, but it can create only the following file types:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>btree</code></p>
<dd> The output is a btree file, named <i>file_name</i><code>.db</code>. This is available on systems with support for <code>db</code> databases.</p>
<dt><code>cdb</code></p>
<dd> The output is one file named <i>file_name</i><code>.cdb</code>. This is available on systems with support for <code>cdb</code> databases.</p>
<dt><code>dbm</code></p>
<dd> The output consists of two files, named <i>file_name</i><code>.pag</code> and <i>file_name</i><code>.dir</code>. This is available on systems with support for <code>dbm</code> databases.</p>
<dt><code>hash</code></p>
<dd> The output is a hashed file, named <i>file_name</i><code>.db</code>. This is available on systems with support for <code>db</code> databases.</p>
<dt><code>fail</code></p>
<dd> A table that reliably fails all requests. The lookup table name is used for logging only. This table exists to simplify Postfix error tests.</p>
<dt><code>sdbm</code></p>
<dd> The output consists of two files, named <i>file_name</i><code>.pag</code> and <i>file_name</i><code>.dir</code>. This is available on systems with support for <code>sdbm</code> databases.</dl>
<p> When no <i>file_type</i> is specified, the software uses the database type specified via the <code>default_database_type</code> configuration parameter. The default value for this parameter depends on the host environment.</dl>
<dt><i>file_name</i></p>
<dd> The name of the alias database source file when creating a database.</dl>
<h2>DIAGNOSTICS</h2>
<p> Problems are logged to the standard error stream and to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) or <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8). No output means that no problems were detected. Duplicate entries are skipped and are flagged with a warning. </p>
<p> <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) terminates with zero exit status in case of success (including successful &quot;<code>postalias -q</code>&quot; lookup) and terminates with non-zero exit status in case of failure.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd> Directory with Postfix configuration files.</p>
<dt><code>MAIL_VERBOSE</code></p>
<dd> Enable verbose logging for debugging purposes.</dl>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>alias_database (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The alias databases for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery that are updated with &quot;<code>newaliases</code>&quot; or with &quot;<code>sendmail -bi</code>&quot;.</p>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>berkeley_db_create_buffer_size (16777216)</code></p>
<dd> The per-table I/O buffer size for programs that create Berkeley DB hash or btree tables.</p>
<dt><code>berkeley_db_read_buffer_size (131072)</code></p>
<dd> The per-table I/O buffer size for programs that read Berkeley DB hash or btree tables.</p>
<dt><code>default_database_type (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default database type for use in <code><a href="/docs/linux/man/1-newaliases/">newaliases</a></code>(1), <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) and <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) commands.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</p>
<dt><code>smtputf8_enable (yes)</code></p>
<dd> Enable preliminary SMTPUTF8 support for the protocols described in RFC 6531..6533.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd> The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd> A prefix that is prepended to the process name in syslog records, so that, for example, &quot;smtpd&quot; becomes &quot;prefix/smtpd&quot;.</dl>
<h2>STANDARDS</h2>
<pre>
RFC 822 (ARPA Internet Text Messages)
</pre>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/5-aliases/">aliases</a>(5), format of alias database input file.
<a href="//www.systutorials.com/docs/linux/man/8-local/">local</a>(8), Postfix local delivery agent.
<a href="//www.systutorials.com/docs/linux/man/1-postconf/">postconf</a>(1), supported database types
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), create/update/query lookup tables
<a href="//www.systutorials.com/docs/linux/man/1-newaliases/">newaliases</a>(1), Sendmail compatibility interface.
<a href="//www.systutorials.com/docs/linux/man/8-postlogd/">postlogd</a>(8), Postfix logging
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging
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
