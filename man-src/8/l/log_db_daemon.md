---
title: "log_db_daemon(8)"
name: "log_db_daemon"
section: "8"
letter: "l"
url: "/docs/linux/man/8-log_db_daemon/"
description: "log_db_daemon – Database logging daemon for Squid"
---

<p>log_db_daemon &#8211; Database logging daemon for Squid</p>
<h2>Synopsis</h2>
<p>log_db_daemon <font SIZE="-1">DSN</font> [options]</p>
<h2>Descriptoin</h2>
<p>This program writes Squid access.log entries to a database. Presently only accepts the <code>squid</code> native format</p>
<dl>
<dt><font SIZE="-1"><code>DSN</code></font></p>
<dd>Database <font SIZE="-1">DSN</font> encoded as a path. This is sent as the access_log file path. </p>
<p> Sample configuration:<br />
&nbsp;<wbr>&nbsp;<wbr>access_log daemon:/host/database/table/username/password squid </p>
<pre> to leave a parameter unspecified use a double slash:
 access_log <a href="daemon://database/table/username/password">daemon://database/table/username/password</a> squid</pre>
<p>Default &#8220;DBI:mysql:database=squid&#8221;</p>
<dt><code>&#8211;debug</code></p>
<dd>Write debug messages to Squid stderr or cache.log</dl>
<h2>Description</h2>
<p>This module exploits the new logfile daemon support available in squid 2.7 and 3.2 to store access log entries in a MySQL database.</p>
<h2>Configuration</h2>
<h3>Squid configuration</h3>
<p><i>access_log directive</i> </p>
<p> The path to the access log file is used to provide the database connection parameters. </p>
<pre> access_log daemon:/mysql_host:port/database/table/username/password squid</pre>
<p>The &#8216;daemon&#8217; prefix is mandatory and tells squid that the <code>logfile_daemon</code> helper is to be used instead of the normal file logging. </p>
<p> The last parameter tells squid which log format to use when writing lines to the log daemon. Presently <code>squid</code> format is supported.</p>
<dl>
<dt>mysql_host:port</p>
<dd>Host where the mysql server is running. If left empty, &#8216;localhost&#8217; is assumed.</p>
<dt>database</p>
<dd>Name of the database to connect to. If left empty, &#8216;squid_log&#8217; is assumed.</p>
<dt>table</p>
<dd>Name of the database table where log lines are stored. If left empty, &#8216;access_log&#8217; is assumed.</p>
<dt>username</p>
<dd>Username to use when connecting to the database. If left empty, &#8216;squid&#8217; is assumed.</p>
<dt>password</p>
<dd>Password to use when connecting to the database. If left empty, no password is used.</dl>
<p> To leave all fields to their default values, you can use a single slash: </p>
<pre> access_log daemon:/ squid</pre>
<p>To specify only the database password, which by default is empty, you must leave unspecified all the other parameters by using null strings: </p>
<pre> access_log <a href="daemon://///password">daemon://///password</a> squid</pre>
<p><i>logfile_daemon directive</i> </p>
<p> This is the current way of telling squid where the logfile daemon resides. </p>
<pre> logfile_daemon /path/to/squid/libexec/logfile-daemon_mysql.pl</pre>
<p>The script must be copied to the location specified in the directive.</p>
<h3>Database configuration</h3>
<p>Let&#8217;s call the database &#8216;squid_log&#8217; and the log table &#8216;access_log&#8217;. The username and password for the db connection will be both &#8216;squid&#8217;. </p>
<p> <i>Database</i> </p>
<p> Create the database: </p>
<pre> CREATE DATABASE squid_log;</pre>
<p><i>User</i> </p>
<p> Create the user: </p>
<pre> GRANT INSERT,SELECT,CREATE ON squid_log.* TO 'squid'@'localhost' IDENTIFIED BY 'squid';
 FLUSH PRIVILEGES;</pre>
<p>Note that only <font SIZE="-1">CREATE, INSERT</font> and <font SIZE="-1">SELECT</font> privileges are granted to the &#8216;squid&#8217; user. This ensures that the logfile daemon script cannot change or modify the log entries. </p>
<p> <i>Table</i> </p>
<p> The Daemon will attempt to initialize this table if none exists when it starts. </p>
<p> The table created should look like: </p>
<pre> CREATE TABLE access_log (
 id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
 time_since_epoch DECIMAL(15,3),
 time_response INTEGER,
 ip_client CHAR(15),
 ip_server CHAR(15),
 http_status_code VARCHAR(10),
 http_reply_size INTEGER,
 http_method VARCHAR(20),
 http_url TEXT,
 http_username VARCHAR(20),
 http_mime_type VARCHAR(50),
 squid_hier_status VARCHAR(20),
 squid_request_status VARCHAR(20)
 );</pre>
<h2>Version Information</h2>
<p>This document refers to <tt>&quot;log_db_daemon&quot;</tt> script version 0.5. </p>
<p> The script has been developed and tested in the following environment:</p>
<dl>
<dt>squid-2.7 Squid-3.2</p>
<dd>
<dt>mysql 5.0.26 and 5.1</p>
<dd>
<dt>perl 5.8.8</p>
<dd>
<dt>OpenSUSE 10.2</p>
<dd></dl>
<h2>Data Extraction</h2>
<h3>Sample queries.</h3>
<dl>
<dt>Clients accessing the cache</p>
<dd>
<pre> SELECT DISTINCT ip_client FROM access_log;</pre>
<dt>Number of request per day</p>
<dd>
<pre> SELECT
 DATE(FROM_UNIXTIME(time_since_epoch)) AS date_day,
 COUNT(*) AS num_of_requests
 FROM access_log
 GROUP BY 1
 ORDER BY 1;</pre>
<dt>Request status count</p>
<dd>To obtain the raw count of each request status: </p>
<pre> SELECT squid_request_status, COUNT(*) AS n
 FROM access_log
 GROUP BY squid_request_status
 ORDER BY 2 DESC;</pre>
<p>To calculate the percentage of each request status: </p>
<pre> SELECT
 squid_request_status,
 (COUNT(*)/(SELECT COUNT(*) FROM access_log)*100) AS percentage
 FROM access_log
 GROUP BY squid_request_status
 ORDER BY 2 DESC;</pre>
<p>To distinguish only between HITs and MISSes: </p>
<pre> SELECT
 'hits',
 (SELECT COUNT(*)
 FROM access_log
 WHERE squid_request_status LIKE '%HIT%')
 /
 (SELECT COUNT(*) FROM access_log)*100
 AS percentage
 UNION
 SELECT
 'misses',
 (SELECT COUNT(*)
 FROM access_log
 WHERE squid_request_status LIKE '%MISS%')
 /
 (SELECT COUNT(*) FROM access_log)*100
 AS pecentage;</pre>
<dt>Response time ranges</p>
<dd>
<pre> SELECT
 '0..500',
 COUNT(*)/(SELECT COUNT(*) FROM access_log)*100 AS percentage
 FROM access_log
 WHERE time_response &gt;= 0 AND time_response &lt; 500
 UNION
 SELECT
 '500..1000',
 COUNT(*)/(SELECT COUNT(*) FROM access_log)*100 AS percentage
 FROM access_log
 WHERE time_response &gt;= 500 AND time_response &lt; 1000
 UNION
 SELECT
 '1000..2000',
 COUNT(*)/(SELECT COUNT(*) FROM access_log)*100 AS percentage
 FROM access_log
 WHERE time_response &gt;= 1000 AND time_response &lt; 2000
 UNION
 SELECT
 '&gt;= 2000',
 COUNT(*)/(SELECT COUNT(*) FROM access_log)*100 AS percentage
 FROM access_log
 WHERE time_response &gt;= 2000;</pre>
<dt>Traffic by mime type</p>
<dd>
<pre> SELECT
 http_mime_type,
 SUM(http_reply_size) as total_bytes
 FROM access_log
 GROUP BY http_mime_type
 ORDER BY 2 DESC;</pre>
<dt>Traffic by client</p>
<dd>
<pre> SELECT
 ip_client,
 SUM(http_reply_size) AS total_bytes
 FROM access_log
 GROUP BY 1
 ORDER BY 2 DESC;</pre>
</dl>
<h3>Speed issues</h3>
<p>The MyISAM storage engine is known to be faster than the InnoDB one, so although it doesn&#8217;t support transactions and referential integrity, it might be more appropriate in this scenario. You might want to append &#8220;ENGINE=MYISAM&#8221; at the end of the table creation code in the above <font SIZE="-1">SQL</font> script. </p>
<p> Indexes should be created according to the queries that are more frequently run. The <font SIZE="-1">DDL</font> script only creates an implicit index for the primary key column.</p>
<h2>Todo</h2>
<h3>Table cleanup</h3>
<p>This script currently implements only the <tt>&quot;L&quot;</tt> (i.e. &#8220;append a line to the log&#8221;) command, therefore the log lines are never purged from the table. This approach has an obvious scalability problem. </p>
<p> One solution would be to implement e.g. the &#8220;rotate log&#8221; command in a way that would calculate some summary values, put them in a &#8220;summary table&#8221; and then delete the lines used to caluclate those values. </p>
<p> Similar cleanup code could be implemented in an external script and run periodically independently from squid log commands.</p>
<h3>Testing</h3>
<p>This script has only been tested in low-volume scenarios (single client, less than 10 req/s). Tests in high volume environments could reveal performance bottlenecks and bugs.</p>
<h2>Author</h2>
<p>Marcello Romani, marcello.romani [at] libero.it Amos Jeffries, amosjeffries [at] squid-cache.org</p>
<h2>Copyright And License</h2>
<pre> * Copyright (C) 1996-2016 The Squid Software Foundation and contributors
 *
 * Squid software is distributed under GPLv2+ license and includes
 * contributions from numerous individuals and organizations.
 * Please see the COPYING and CONTRIBUTORS files for details.</pre>
<p>Copyright (C) 2008 by Marcello Romani </p>
<p> This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself, either Perl version 5.8.8 or, at your option, any later version of Perl 5 you may have available.</p>
