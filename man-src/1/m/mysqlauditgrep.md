---
title: "mysqlauditgrep(1)"
name: "mysqlauditgrep"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlauditgrep/"
description: "mysqlauditgrep – Search an audit log"
---

<h2 class="name">NAME</h2>
<p> mysqlauditgrep &#8211; Search an audit log </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code> mysqlauditgrep [</code><i>OPTIONS</i><code>]&#8230; </code><i>AUDIT_LOG_FILE</i><code> mysqlauditgrep &#8211;file-stats[&#8211;format=</code><i>FORMAT</i><code>] </code><i>AUDIT_LOG_FILE</i><code> mysqlauditgrep &#8211;format=</code><i>FORMAT</i><i>AUDIT_LOG_FILE</i><code> mysqlauditgrep [&#8211;users=</code><i>USERS</i><code>] [&#8211;start-date=</code><i>START_DATE</i><code>] [&#8211;end-date=</code><i>END_DATE</i><code>] [&#8211;pattern=</code><i>PATTERN</i><code>[&#8211;regexp]] [&#8211;query-type=</code><i>QUERY_TYPE</i><code>] [&#8211;event-type=</code><i>EVENT_TYPE</i><code>] [&#8211;status=</code><i>STATUS</i><code>] [&#8211;format=</code><i>FORMAT</i><code>] </code><i>AUDIT_LOG_FILE</i></dl>
<h2>DESCRIPTION</h2>
<dd>This utility allows you to search the current or archived audit logs, allowing you to display data from the audit log file according to the defined search criterion. It also allows you to output the results in different formats, namely GRID (default), TAB, CSV, VERTICAL, and RAW (the original XML format). </p>
<p> This utility allows you to search and filter the returned audit log records by: users (<code>&#8211;users</code>), date and time ranges (<code>&#8211;start-date</code> and <code>&#8211;end-date</code>), SQL query types (<code>&#8211;query-type</code>), logged event and record types (<code>&#8211;event-type</code>), status (<code>&#8211;status</code>), and matching patterns (<code>&#8211;pattern</code>). Any of these search options can be combined and used together, with the retrieved records resulting from all passed in options being true. </p>
<p> The <code>&#8211;pattern</code> supports two types of pattern matching: standard SQL, used with the SQL <i>LIKE</i> operator (SQL patterns), and standard <i>REGEXP</i> (POSIX regular expression patterns). </p>
<p> This utility always requires an audit log file to be passed in, so the <i>AUDIT_LOG_FILE</i> argument is searched as a full path and file name for the audit log file. If not specified, a notification concerning this requirement will be printed. And if <code>&#8211;format</code> is passed in without search parameters, then all the records of the audit log are displayed in the specified format. </p>
<p> The <code>&#8211;file-stats</code> option is not considered a search criteria, and is used to display the file statistics of a specified audit log. Other search options will be ignored when the <code>&#8211;file-stats</code> option is used, except the <code>&#8211;format</code> option will continue to format the results accordingly. </p>
<p> To specify the format of the generated results, use one of the following values with the <code>&#8211;format</code> option: </p>
<dl>
<dt>
<dd> 1. <i>GRID (default)</i> </p>
<p> Display output in grid or table format like that of the <code>mysql</code> monitor.</dl>
<dl>
<dt>
<dd> 2. <i>CSV</i> </p>
<p> Display output in comma-separated values format.</dl>
<dl>
<dt>
<dd> 3. <i>VERTICAL</i> </p>
<p> Display output in single-column format like that of the \G command for the <code>mysql</code> monitor.</dl>
<dl>
<dt>
<dd> 4. <i>RAW</i> </p>
<p> Display output results in the original raw format of the audit log records, which is written in XML.</dl>
<p>Standard SQL Pattern Matching </p>
<p> The simple patterns defined by the SQL standard enables users to use two characters with special meanings: &#8220;%&#8221; (percent) matches zero or more characters, and &#8220;_&#8221; (underscore) matches exactly one arbitrary character. In standard SQL, these types of patterns are used with the LIKE comparison operator, and they are case-insensitive by default. This utility assumes that they are case-insensitive. </p>
<p> For example: </p>
<dl>
<dt>
<dd> &bull; &quot;audit%&quot; </p>
<p> Match any string that starts with &quot;audit&quot;.</dl>
<dl>
<dt>
<dd> &bull; &quot;%log%&quot; </p>
<p> Match any string containing the word &quot;log&quot;.</dl>
<dl>
<dt>
<dd> &bull; &quot;%_&quot; </p>
<p> Match any string consisting of one or more characters.</dl>
<p> For documentation about the standard SQL pattern matching syntax, see m[blue]<code>Pattern Matching</code>m[]<font SIZE="-2">[1]</font>.<br />
REGEXP Pattern Matching&nbsp;<wbr>(POSIX) </p>
<p> Standard <i>REGEXP</i> patterns are more powerful than the simple patterns defined in the SQL standard. A regular expression is a string of ordinary and special characters specified to match other strings. Unlike SQL Patterns, <i>REGEXP</i> patterns are case-sensitive. The <i>REGEXP</i> syntax defines the following characters with special meaning: </p>
<dl>
<dt>
<dd> &bull; <i>.</i> </p>
<p> Match any character.</dl>
<dl>
<dt>
<dd> &bull; <i>^</i> </p>
<p> Match the beginning of a string.</dl>
<dl>
<dt>
<dd> &bull; <i>$</i> </p>
<p> Match the end of a string.</dl>
<dl>
<dt>
<dd> &bull; <i>\</i> </p>
<p> Match zero or more repetitions of the preceding regular expression.</dl>
<dl>
<dt>
<dd> &bull; <i>+</i> </p>
<p> Match one or more repetitions of the preceding regular expression.</dl>
<dl>
<dt>
<dd> &bull; <i>?</i> </p>
<p> Match zero or one repetition of the preceding regular expression.</dl>
<dl>
<dt>
<dd> &bull; <i>|</i> </p>
<p> Match either the regular expressions from the left or right of |.</dl>
<dl>
<dt>
<dd> &bull; <i>[]</i> </p>
<p> Indicates a set of characters to match. Note that, special characters lose their special meaning inside sets. In particular, ^ acquires a different meaning if it is the first character of the set, matching the complementary set (i.e., all the characters that are not in the set will be matched).</dl>
<dl>
<dt>
<dd> &bull; <i>{m}</i> </p>
<p> Match <i>m</i> repetitions of the preceding regular expression.</dl>
<dl>
<dt>
<dd> &bull; <i>{m,n}</i> </p>
<p> Match from <i>m</i> to <i>n</i> repetitions of the preceding regular expression.</dl>
<dl>
<dt>
<dd> &bull; <i>()</i> </p>
<p> Define a matching group, and matches the regular expression inside the parentheses.</dl>
<p> For example: </p>
<dl>
<dt>
<dd> &bull; <i>&quot;a\*&quot;</i> </p>
<p> Match a sequence of zero or more a.</dl>
<dl>
<dt>
<dd> &bull; <i>&quot;a+&quot;</i> </p>
<p> Match a sequence of one or more a.</dl>
<dl>
<dt>
<dd> &bull; <i>&quot;a?&quot;</i> </p>
<p> Match zero or one a.</dl>
<dl>
<dt>
<dd> &bull; <i>&quot;ab|cd&quot;</i> </p>
<p> Match ab or cd.</dl>
<dl>
<dt>
<dd> &bull; <i>&quot;[axy]&quot;</i> </p>
<p> Match a, x or y.</dl>
<dl>
<dt>
<dd> &bull; <i>&quot;[a-f]&quot;</i> </p>
<p> Match any character in the range a to f (that is, a, b, c, d, e, or f).</dl>
<dl>
<dt>
<dd> &bull; <i>&quot;[^axy]&quot;</i> </p>
<p> Match any character <i>except</i>a, x or y.</dl>
<dl>
<dt>
<dd> &bull; <i>&quot;a{5}&quot;</i> </p>
<p> Match exactly five copies of a.</dl>
<dl>
<dt>
<dd> &bull; <i>&quot;a{2,5}&quot;</i> </p>
<p> Match from two to five copies of a.</dl>
<dl>
<dt>
<dd> &bull; <i>&quot;(abc)+&quot;</i> </p>
<p> Match one or more repetitions of abc.</dl>
<p> This is a brief overview of regular expressions that can be used to define this type of patterns. The full syntax is described in the m[blue]<code>Python &quot;re&quot; module docs</code>m[]<font SIZE="-2">[2]</font>, supporting the definition of much more complex pattern matching expression.<br />
OPTIONS </p>
<p> <code>mysqlauditgrep</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;end-date=&lt;END_DATE&gt; </p>
<p> End date/time to retrieve log entries until the specified date/time range. If not specified or the value is 0, all entries to the end of the log are displayed. Accepted formats: &quot;yyyy-mm-ddThh:mm:ss&quot; or &quot;yyyy-mm-dd&quot;.</dl>
<dl>
<dt>
<dd> &bull; &#8211;event-type=&lt;EVENT_TYPE&gt; </p>
<p> Comma-separated list of event types to search in all audit log records matching the specified types. Supported values are: Audit, Binlog Dump, Change user, Close stmt, Connect Out, Connect, Create DB, Daemon, Debug, Delayed insert, Drop DB, Execute, Fetch, Field List, Init DB, Kill, Long Data, NoAudit, Ping, Prepare, Processlist, Query, Quit, Refresh, Register Slave, Reset stmt, Set option, Shutdown, Sleep, Statistics, Table Dump, Time.</dl>
<dl>
<dt>
<dd> &bull; &#8211;file-stats </p>
<p> Display the audit log file statistics.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=FORMAT, -f FORMAT </p>
<p> Output format to display the resulting data. Supported format values: GRID (default), TAB, CSV, VERTICAL and RAW.</dl>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;pattern=&lt;PATTERN&gt;, -e &lt;PATTERN&gt; </p>
<p> Search pattern to retrieve all entries with at least one attribute value matching the specified pattern. By default the standard SQL <i>LIKE</i> patterns are used for matching. If the <code>&#8211;regexp</code> option is set, then <i>REGEXP</i> patterns must be specified for matching.</dl>
<dl>
<dt>
<dd> &bull; &#8211;query-type=&lt;QUERY_TYPE&gt; </p>
<p> Comma-separated list of SQL statements/commands to search for and match. Supported values: CREATE, ALTER, DROP, TRUNCATE, RENAME, GRANT, REVOKE, SELECT, INSERT, UPDATE, DELETE, COMMIT, SHOW, SET, CALL, PREPARE, EXECUTE, DEALLOCATE.</dl>
<dl>
<dt>
<dd> &bull; &#8211;regexp, &#8211;basic-regexp, -G </p>
<p> Indicates that pattern matching will be performed using a regular expression <i>REGEXP</i> (from the Python re module). By default, the simple standard SQL <i>LIKE</i> patterns are used for matching. This affects how the value specified by the <code>&#8211;pattern</code> option is interpreted.</dl>
<dl>
<dt>
<dd> &bull; &#8211;start-date=&lt;START_DATE&gt; </p>
<p> Starting date/time to retrieve log entries from the specified date/time range. If not specified or the value is 0, all entries from the start of the log are displayed. Accepted formats: yyyy-mm-ddThh:mm:ss or yyyy-mm-dd.</dl>
<dl>
<dt>
<dd> &bull; &#8211;status=&lt;STATUS&gt; </p>
<p> Comma-separated list of status values or intervals to search for all audit log records with a matching status. Status values are non-negative integers (corresponding to MySQL error codes). Status intervals are closed (i.e., include both endpoints) and defined simply using a dash between its endpoints. For Example: 1051,1068-1075,1109,1146. </p>
<p> The &#8211;status option is available as of MySQL Utilities 1.2.4 / 1.3.3.</dl>
<dl>
<dt>
<dd> &bull; &#8211;users=&lt;USERS&gt;, -u &lt;USERS&gt; </p>
<p> Comma-separated list of user names, to search for their associated log entries. For example: &quot;dan,jon,john,paul,philip,stefan&quot;.</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<p>NOTES </p>
<p> This utility is available as of μ 1.2.0. </p>
<p> This utility can only be applied to servers with the m[blue]<code>audit log plugin enabled</code>m[]<font SIZE="-2">[3]</font>. And the audit log plugin is available as of MySQL Server versions 5.5.28 and 5.6.10. </p>
<p> This utility requires the use of Python version 2.6 or higher, but does not support Python 3. </p>
<p> Single or double quote characters (respectively, <i>&#8216;</i> or <i>&quot;</i>) can be used around option values. In fact, quotes are required to set some options values correctly, such as values with whitespace. For example, to specify the event types <code>Create DB</code> and <code>Drop DB</code> for the <code>&#8211;event-type</code> option, the following syntax must be used: <code>&#8211;event-type=&#8217;Create DB,Drop DB&#8217;</code> or <code>&#8211;event-type=&quot;Create DB,Drop DB&quot;</code>.<br />
EXAMPLES </p>
<p> To display the audit log file statistics and output the results in CSV format, run the following command: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; mysqlauditgrep --file-stats --format=CSV /SERVER/data/audit.log
  #
  # Audit Log File Statistics:
  #
  File,Size,Created,Last Modified
  audit.log,9101,Thu Sep 27 13:33:11 2012,Thu Oct 11 17:40:35 2012
  #
  # Audit Log Startup Entries:
  #
  SERVER_ID,STARTUP_OPTIONS,NAME,TIMESTAMP,MYSQL_VERSION,OS_VERSION,VERSION
  1,/SERVER/sql/mysqld --defaults-file=/SERVER/my.cnf,Audit,2012-09-27T13:33:11,5.5.29-log,x86_64-Linux,1
</pre>
</dl>
<p> To display the audit log entries of specific users, use the following command: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; mysqlauditgrep --users=tester1,tester2 /SERVER/data/audit.log
</pre>
</dl>
<p> To display the audit log file statistics, run the following command: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqlauditgrep-- users = tester1, tester2 / SERVER / data / audit.log + -- -- -- -- -+-- -- -- -- -- --+-- -- -- -- --+-- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- --+-- -- -- -- --+-- -- -- -- -- --+-- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+ | STATUS | SERVER_ID | NAME | TIMESTAMP | CONNECTION_ID | HOST | USER | PRIV_USER | IP | SQLTEXT |
                                              +-- -- -- -- -+-- -- -- -- -- --+-- -- -- -- --+-- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- --+-- -- -- -- --+-- -- -- -- -- --+-- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+ | 0 | 1 | Connect | 2012 - 09 - 28T11 : 26 : 50 | 9 | localhost | root | tester1 | 127.0.0.1 | None |
                                              | 0 | 1 | Query | 2012 - 09 - 28T11 : 26 : 50 | 9 | None | root | tester1 | None | SET @ @session.autocommit = OFF |
                                                                                                                                                             | 0 | 1 | Ping | 2012 - 09 - 28T11 : 26 : 50 | 9 | None | root | tester1 | None | None |
                                                                                                                                                             | 0 | 1 | Query | 2012 - 09 - 28T11 : 26 : 50 | 9 | None | root | tester1 | None | SHOW VARIABLES LIKE 'READ_ONLY' |
                                                                                                                                                             | 0 | 1 | Query | 2012 - 09 - 28T11 : 26 : 50 | 9 | None | root | tester1 | None | COMMIT |
                                                                                                                                                             | 0 | 1 | Ping | 2012 - 09 - 28T11 : 26 : 50 | 9 | None | root | tester1 | None | None |
                                                                                                                                                             | 0 | 1 | Query | 2012 - 09 - 28T11 : 26 : 50 | 9 | None | root | tester1 | None | COMMIT |
                                                                                                                                                             | 0 | 1 | Quit | 2012 - 09 - 28T11 : 26 : 50 | 9 | None | root | tester1 | None | None |
                                                                                                                                                             | 0 | 1 | Connect | 2012 - 10 - 10T15 : 55 : 55 | 11 | localhost | tester2 | root | 127.0.0.1 | None |
                                                                                                                                                             | 0 | 1 | Query | 2012 - 10 - 10T15 : 55 : 55 | 11 | None | tester2 | root | None | select @ @version_comment limit 1 |
                                                                                                                                                             | 0 | 1 | Query | 2012 - 10 - 10T15 : 56 : 10 | 11 | None | tester2 | root | None | show databases |
                                                                                                                                                             | 1046 | 1 | Query | 2012 - 10 - 10T15 : 57 : 26 | 11 | None | tester2 | root | None | show tables test |
                                                                                                                                                             | 1046 | 1 | Query | 2012 - 10 - 10T15 : 57 : 36 | 11 | None | tester2 | root | None | show tables test |
                                                                                                                                                             | 0 | 1 | Query | 2012 - 10 - 10T15 : 57 : 51 | 11 | None | tester2 | root | None | show tables in test |
                                                                                                                                                             | 0 | 1 | Quit | 2012 - 10 - 10T15 : 57 : 59 | 11 | None | tester2 | root | None | None |
                                                                                                                                                             | 0 | 1 | Connect | 2012 - 10 - 10T17 : 35 : 42 | 12 | localhost | tester2 | root | 127.0.0.1 | None |
                                                                                                                                                             | 0 | 1 | Query | 2012 - 10 - 10T17 : 35 : 42 | 12 | None | tester2 | root | None | select @ @version_comment limit 1 |
                                                                                                                                                             | 0 | 1 | Quit | 2012 - 10 - 10T17 : 47 : 22 | 12 | None | tester2 | root | None | None |
                                                                                                                                                             +-- -- -- -- -+-- -- -- -- -- --+-- -- -- -- --+-- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- --+-- -- -- -- --+-- -- -- -- -- --+-- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+
</code></pre>
</dl>
<p> To display the audit log entries for a specific date/time range, use the following command: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlauditgrep&#8211; start &#8211; date = 2012 &#8211; 09 &#8211; 27T13 : 33 : 47 &#8211;end &#8211; date = 2012 &#8211; 09 &#8211; 28 / SERVER / data / audit.log + &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | STATUS | TIMESTAMP | NAME | CONNECTION_ID | SQLTEXT |<br />
                                                                                   +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 47 | Ping | 7 | None |<br />
                                                                                   | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 47 | Query | 7 | SELECT * FROM INFORMATION_SCHEMA.PLUGINS WHERE PLUGIN_NAME LIKE &#8216;audit%&#8217; |<br />
                                                                                   | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 47 | Query | 7 | COMMIT |<br />
                                                                                   | 0 | 2012 &#8211; 09 &#8211; 27T13 : 34 : 48 | Quit | 7 | None |<br />
                                                                                   | 0 | 2012 &#8211; 09 &#8211; 27T13 : 34 : 48 | Quit | 8 | None |<br />
                                                                                   +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+
</dl>
<p> To display the audit log entries matching a specific SQL <i>LIKE</i> pattern, use the following command: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlauditgrep&#8211; pattern = &#8220;% = ___&#8221;;<br />
/ SERVER / data / audit.log + &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | STATUS | TIMESTAMP | NAME | SQLTEXT | CONNECTION_ID |<br />
    +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SET @ @session.autocommit = OFF | 7 |<br />
                                                                                                                                                                                                                   | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SET @ @session.autocommit = OFF | 8 |<br />
                                                                                                                                                                                                                                                                                           | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SET @ @session.autocommit = OFF | 9 |<br />
                                                                                                                                                                                                                                                                                                                                                                   | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SET @ @session.autocommit = OFF | 10 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                           +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+
</dl>
<p> To display the audit log entries matching a specific <i>REGEXP </i> pattern, use the following command: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlauditgrep&#8211; pattern = &#8220;.* = &#8230;&#8221; &#8211;regexp / SERVER / data / audit.log + &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | STATUS | TIMESTAMP | NAME | SQLTEXT | CONNECTION_ID |<br />
                                   +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SET @ @session.autocommit = OFF | 7 |<br />
                                                                                                                                                                                                                                                  | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SET @ @session.autocommit = OFF | 8 |<br />
                                                                                                                                                                                                                                                                                                                          | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SET @ @session.autocommit = OFF | 9 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                  | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SET @ @session.autocommit = OFF | 10 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+
</dl>
<p> To display the audit log entries of specific query types, use the following command: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlauditgrep&#8211; query &#8211; type = show, SET / SERVER / data / audit.log + &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | STATUS | TIMESTAMP | NAME | SQLTEXT | CONNECTION_ID |<br />
                                                  +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SET NAMES &#8216;latin1&#8217; COLLATE &#8216;latin1_swedish_ci&#8217; | 7 |<br />
                                                  | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SET @ @session.autocommit = OFF | 7 |<br />
                                                                                                                          | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SHOW VARIABLES LIKE &#8216;READ_ONLY&#8217; | 7 |<br />
                                                                                                                          | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SHOW VARIABLES LIKE &#8216;datadir&#8217; | 7 |<br />
                                                                                                                          | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SHOW VARIABLES LIKE &#8216;basedir&#8217; | 7 |<br />
                                                                                                                          | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SET NAMES &#8216;latin1&#8217; COLLATE &#8216;latin1_swedish_ci&#8217; | 8 |<br />
                                                                                                                          | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SET @ @session.autocommit = OFF | 8 |<br />
                                                                                                                                                                                                  | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SHOW VARIABLES LIKE &#8216;READ_ONLY&#8217; | 8 |<br />
                                                                                                                                                                                                  | 0 | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | Query | SHOW VARIABLES LIKE &#8216;basedir&#8217; | 8 |<br />
                                                                                                                                                                                                  | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SET NAMES &#8216;latin1&#8217; COLLATE &#8216;latin1_swedish_ci&#8217; | 9 |<br />
                                                                                                                                                                                                  | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SET @ @session.autocommit = OFF | 9 |<br />
                                                                                                                                                                                                                                                                          | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SHOW VARIABLES LIKE &#8216;READ_ONLY&#8217; | 9 |<br />
                                                                                                                                                                                                                                                                          | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SET NAMES &#8216;latin1&#8217; COLLATE &#8216;latin1_swedish_ci&#8217; | 10 |<br />
                                                                                                                                                                                                                                                                          | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SET @ @session.autocommit = OFF | 10 |<br />
                                                                                                                                                                                                                                                                                                                                                  | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SHOW VARIABLES LIKE &#8216;READ_ONLY&#8217; | 10 |<br />
                                                                                                                                                                                                                                                                                                                                                  | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SET @ @GLOBAL.audit_log_flush = ON | 10 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                              | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SHOW VARIABLES LIKE &#8216;audit_log_policy&#8217; | 10 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                              | 0 | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | Query | SHOW VARIABLES LIKE &#8216;audit_log_rotate_on_size&#8217; | 10 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                              | 0 | 2012 &#8211; 10 &#8211; 10T15 : 56 : 10 | Query | show databases | 11 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                              | 1046 | 2012 &#8211; 10 &#8211; 10T15 : 57 : 26 | Query | show tables test | 11 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                              | 1046 | 2012 &#8211; 10 &#8211; 10T15 : 57 : 36 | Query | show tables test | 11 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                              | 0 | 2012 &#8211; 10 &#8211; 10T15 : 57 : 51 | Query | show tables in test | 11 |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                              +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+
</dl>
<p> To display the audit log entries of specific event types, use the following command: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlauditgrep&#8211; event &#8211; type = &#8220;Ping,Connect&#8221; / SERVER / data / audit.log + &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ | STATUS | NAME | TIMESTAMP | CONNECTION_ID | HOST | USER | PRIV_USER | IP |<br />
                                        +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 0 | Connect | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | 7 | localhost | root | root | 127.0.0.1 |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | 7 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | 7 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | 7 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | 7 | None | None | None | None |<br />
                                        | 0 | Connect | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | 8 | localhost | root | root | 127.0.0.1 |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | 8 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 27T13 : 33 : 39 | 8 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 27T13 : 33 : 47 | 7 | None | None | None | None |<br />
                                        | 0 | Connect | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | 9 | localhost | root | tester | 127.0.0.1 |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | 9 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | 9 | None | None | None | None |<br />
                                        | 0 | Connect | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | 10 | localhost | root | root | 127.0.0.1 |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | 10 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | 10 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | 10 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | 10 | None | None | None | None |<br />
                                        | 0 | Ping | 2012 &#8211; 09 &#8211; 28T11 : 26 : 50 | 10 | None | None | None | None |<br />
                                        | 0 | Connect | 2012 &#8211; 10 &#8211; 10T15 : 55 : 55 | 11 | localhost | tester | root | 127.0.0.1 |<br />
                                        | 0 | Connect | 2012 &#8211; 10 &#8211; 10T17 : 35 : 42 | 12 | localhost | tester | root | 127.0.0.1 |<br />
                                        +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+
</dl>
<p> To display the audit log entries with a specific status, use the following command: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlauditgrep&#8211; status = 1100 &#8211; 1199, 1046 / SERVER / data / audit.log + &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | STATUS | TIMESTAMP | NAME | SQLTEXT | CONNECTION_ID |<br />
                                                   +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 1046 | 2012 &#8211; 10 &#8211; 10T15 : 57 : 26 | Query | show tables test | 11 |<br />
                                                   | 1046 | 2012 &#8211; 10 &#8211; 10T15 : 57 : 36 | Query | show tables test | 11 |<br />
                                                   | 1146 | 2012 &#8211; 10 &#8211; 10T17 : 44 : 55 | Query | select *from teste.employees where salary &gt; 500 and salary &lt; 1000 | 12 |<br />
                                                   | 1046 | 2012 &#8211; 10 &#8211; 10T17 : 47 : 17 | Query | select *from test_encoding where value = &#8216;&lt;&gt;&#8221;&amp;&#8217; | 12 |<br />
                                                                                                                                           +&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+
</dl>
<p> Note: You can view all successful commands with <code>&#8211;status=0</code> and all unsuccessful ones with <code>&#8211;status=1-9999</code>. </p>
<p> To display the audit log entries matching several search criteria, use the following command: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqlauditgrep-- users = root-- start - date = 0 --end - date = 2012 - 10 - 10 --event - type = Query-- query - type = SET-- status = 0 --pattern = "%audit_log%" / SERVER / data / audit.log + -- -- -- -- -+-- -- -- -- -- --+-- -- -- --+-- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -+-- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+ | STATUS | SERVER_ID | NAME | TIMESTAMP | CONNECTION_ID | USER | PRIV_USER | SQLTEXT |
                                                                                                                                                            +-- -- -- -- -+-- -- -- -- -- --+-- -- -- --+-- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -+-- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+ | 0 | 1 | Query | 2012 - 09 - 28T11 : 26 : 50 | 10 | root | root | SET @ @GLOBAL.audit_log_flush = ON |
                                                                                                                                                                                                                                                                                                                                                                                                                                                         +-- -- -- -- -+-- -- -- -- -- --+-- -- -- --+-- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -+-- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Pattern Matching</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://dev.mysql.com/doc/refman/5.6/en/pattern-matching.html">http://dev.mysql.com/doc/refman/5.6/en/pattern-matching.html</a></dl>
<dt> 2.</p>
<dd> Python &quot;re&quot; module docs</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://docs.python.org/2/library/re.html">http://docs.python.org/2/library/re.html</a></dl>
<dt> 3.</p>
<dd> audit log plugin enabled</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://dev.mysql.com/doc/refman/5.6/en/audit-log-plugin-installation.html">http://dev.mysql.com/doc/refman/5.6/en/audit-log-plugin-installation.html</a></dl>
</dl>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
