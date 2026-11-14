---
title: "mongostat(1)"
name: "mongostat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongostat/"
description: "mongostat – MongoDB Use Statistics"
---

<h2>NAME</h2>
<p> mongostat &#8211; MongoDB Use Statistics</p>
<h2>SYNOPSIS</h2>
<p> The <code>mongostat</code> utility provides a quick overview of the status of a currently running <code>mongod</code> or <code>mongos</code> instance. <code>mongostat</code> is functionally similar to the UNIX/Linux file system utility <code>vmstat</code>, but provides data regarding <code>mongod</code> and <code>mongos</code> instances. </p>
<p> <code>SEE ALSO:</code> For more information about monitoring MongoDB, see <a rel="nofollow" href="http://docs.mongodb.org/manual/administration/monitoring.">http://docs.mongodb.org/manual/administration/monitoring.</a> </p>
<p> For more background on various other MongoDB status outputs see:</p>
<dl>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/command/serverStatus">http://docs.mongodb.org/manual/reference/command/serverStatus</a></p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/command/replSetGetStatus">http://docs.mongodb.org/manual/reference/command/replSetGetStatus</a></p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/command/dbStats">http://docs.mongodb.org/manual/reference/command/dbStats</a></p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/command/collStats">http://docs.mongodb.org/manual/reference/command/collStats</a> </p>
<p> For an additional utility that provides MongoDB metrics see <code>mongotop</code>. </p>
<p> <code>mongostat</code> connects to the <code>mongod</code> instance running on the local host interface on TCP port <code>27017</code>; however, <code>mongostat</code> can connect to any accessible remote <code>mongod</code> instance.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongostat</code></p>
<dd>
<dt><code>mongostat</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongostat</code> options and usage.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongostat</code> release number.</p>
<dt><code>&#8211;host &lt;hostname&gt;&lt;:port&gt;, -h</code></p>
<dd> Specifies a resolvable hostname for the <code>mongod</code> to which to connect. By default <code>mongostat</code> attempts to connect to a MongoDB instance running on the localhost on port number <code>27017</code>. </p>
<p> To connect to a replica set, specify the replica set seed name and the seed list of set members. Use the following format: </p>
<pre>
&lt;replica_set_name&gt;/&lt;hostname1&gt;&lt;:port&gt;,&lt;hostname2:&lt;port&gt;,...
</pre>
<p> You can always connect directly to a single MongoDB instance by specifying the host and port number directly.</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port number when the MongoDB instance is not running on the standard port of <code>27017</code>. You may also specify the port number using the <code>&#8211;host</code> option.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongostat</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongostat</code>, disable IPv6 support by default.</p>
<dt><code>&#8211;ssl</code></p>
<dd> New in version 2.6. </p>
<p> Enables connection to a <code>mongod</code> or <code>mongos</code> that has SSL support enabled. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslCAFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the root certificate chain from the Certificate Authority. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslPEMKeyFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains both the SSL certificate and key. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> This option is required when using the <i>&#8211;ssl</i> option to connect to a <code>mongod</code> or <code>mongos</code> that has <code>sslCAFile</code> enabled <i>without</i> <code>sslWeakCertificateValidation</code>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslPEMKeyPassword &lt;value&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongostat</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongostat</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslCRLFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the Certificate Revocation List. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslAllowInvalidCertificates</code></p>
<dd> New in version 2.6. </p>
<p> Bypasses the validation checks for server certificates and allows the use of invalid certificates. When using the <code>sslAllowInvalidCertificates</code> setting, MongoDB logs as a warning the use of the invalid certificate. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslFIPSMode</code></p>
<dd> New in version 2.6. </p>
<p> Directs <code>mongostat</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;username &lt;username&gt;, -u</code></p>
<dd> Specifies a username with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;password</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;password &lt;password&gt;, -p</code></p>
<dd> Specifies a password with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;username</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;authenticationDatabase &lt;dbname&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the database that holds the user&#8217;s credentials. If you do not specify an authentication database, <code>mongostat</code> assumes that the database specified as the argument to the <i>&#8211;db</i> option holds the user&#8217;s credentials.</p>
<dt><code>&#8211;authenticationMechanism &lt;name&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the authentication mechanism. By default, the authentication mechanism is <code>MONGODB-CR</code>, which is the MongoDB challenge/response authentication mechanism. In MongoDB Enterprise, <code>mongostat</code> also includes support for <code>GSSAPI</code> to handle Kerberos authentication. See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication">http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication</a> for more information about Kerberos authentication.</p>
<dt><code>&#8211;noheaders</code></p>
<dd> Disables the output of column or field names.</p>
<dt><code>&#8211;rowcount &lt;number&gt;, -n</code></p>
<dd> Controls the number of rows to output. Use in conjunction with the <code>sleeptime</code> argument to control the duration of a <code>mongostat</code> operation. </p>
<p> Unless <i>&#8211;rowcount</i> is specified, <code>mongostat</code> will return an infinite number of rows (e.g. value of <code>0</code>.)</p>
<dt><code>&#8211;http</code></p>
<dd> Configures <code>mongostat</code> to collect data using the HTTP interface rather than a raw database connection.</p>
<dt><code>&#8211;discover</code></p>
<dd> Discovers and reports on statistics from all members of a <i>replica set</i> or <i>sharded cluster</i>. When connected to any member of a replica set, <i>&#8211;discover</i> all non-<i>hidden members</i> of the replica set. When connected to a <code>mongos</code>, <code>mongostat</code> will return data from all <i>shards</i> in the cluster. If a replica set provides a shard in the sharded cluster, <code>mongostat</code> will report on non-hidden members of that replica set. </p>
<p> The <i>mongostat &#8211;host</i> option is not required but potentially useful in this case. </p>
<p> Changed in version 2.6: When running with <i>&#8211;discover</i>, <code>mongostat</code> now respects :option:&#8211;rowcount`. </p>
<dt><code>&#8211;all</code></p>
<dd> Configures <code>mongostat</code> to return all optional <i>fields</i>.</p>
<dt><code>&lt;sleeptime&gt;</code></p>
<dd> The final argument is the length of time, in seconds, that <code>mongostat</code> waits in between calls. By default <code>mongostat</code> returns one call every second. </p>
<p> <code>mongostat</code> returns values that reflect the operations over a 1 second period. For values of <code>&lt;sleeptime&gt;</code> greater than 1, <code>mongostat</code> averages data to reflect average operations per second.</dl>
<h2>FIELDS</h2>
<p> <code>mongostat</code> returns values that reflect the operations over a 1 second period. When <code>mongostat &lt;sleeptime&gt;</code> has a value greater than 1, <code>mongostat</code> averages the statistics to reflect average operations per second. </p>
<p> <code>mongostat</code> outputs the following fields:</p>
<dl>
<dt><code>inserts</code></p>
<dd> The number of objects inserted into the database per second. If followed by an asterisk (e.g. <code>*</code>), the datum refers to a replicated operation.</p>
<dt><code>query</code></p>
<dd> The number of query operations per second.</p>
<dt><code>update</code></p>
<dd> The number of update operations per second.</p>
<dt><code>delete</code></p>
<dd> The number of delete operations per second.</p>
<dt><code>getmore</code></p>
<dd> The number of get more (i.e. cursor batch) operations per second.</p>
<dt><code>command</code></p>
<dd> The number of commands per second. On <i>slave</i> and <i>secondary</i> systems, <code>mongostat</code> presents two values separated by a pipe character (e.g. <code>|</code>), in the form of <code>local|replicated</code> commands.</p>
<dt><code>flushes</code></p>
<dd> The number of <i>fsync</i> operations per second.</p>
<dt><code>mapped</code></p>
<dd> The total amount of data mapped in megabytes. This is the total data size at the time of the last <code>mongostat</code> call.</p>
<dt><code>size</code></p>
<dd> The amount of virtual memory in megabytes used by the process at the time of the last <code>mongostat</code> call.</p>
<dt><code>non-mapped</code></p>
<dd> The total amount of virtual memory excluding all mapped memory at the time of the last <code>mongostat</code> call.</p>
<dt><code>res</code></p>
<dd> The amount of resident memory in megabytes used by the process at the time of the last <code>mongostat</code> call.</p>
<dt><code>faults</code></p>
<dd> Changed in version 2.1. </p>
<p> The number of page faults per second. </p>
<p> Before version 2.1 this value was only provided for MongoDB instances running on Linux hosts.</p>
<dt><code>locked</code></p>
<dd> The percent of time in a global write lock. </p>
<p> Changed in version 2.2: The <code>locked db</code> field replaces the <code>locked %</code> field to more appropriate data regarding the database specific locks in version 2.2. </p>
<dt><code>locked db</code></p>
<dd> New in version 2.2. </p>
<p> The percent of time in the per-database context-specific lock. <code>mongostat</code> will report the database that has spent the most time since the last <code>mongostat</code> call with a write lock. </p>
<p> This value represents the amount of time that the listed database spent in a locked state <i>combined</i> with the time that the <code>mongod</code> spent in the global lock. Because of this, and the sampling method, you may see some values greater than 100%.</p>
<dt><code>idx miss</code></p>
<dd> The percent of index access attempts that required a page fault to load a btree node. This is a sampled value.</p>
<dt><code>qr</code></p>
<dd> The length of the queue of clients waiting to read data from the MongoDB instance.</p>
<dt><code>qw</code></p>
<dd> The length of the queue of clients waiting to write data from the MongoDB instance.</p>
<dt><code>ar</code></p>
<dd> The number of active clients performing read operations.</p>
<dt><code>aw</code></p>
<dd> The number of active clients performing write operations.</p>
<dt><code>netIn</code></p>
<dd> The amount of network traffic, in <i>bytes</i>, received by the MongoDB instance. </p>
<p> This includes traffic from <code>mongostat</code> itself.</p>
<dt><code>netOut</code></p>
<dd> The amount of network traffic, in <i>bytes</i>, sent by the MongoDB instance. </p>
<p> This includes traffic from <code>mongostat</code> itself.</p>
<dt><code>conn</code></p>
<dd> The total number of open connections.</p>
<dt><code>set</code></p>
<dd> The name, if applicable, of the replica set.</p>
<dt><code>repl</code></p>
<dd> The replication status of the member. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Value</code> </td>
<td> <code>Replication Type</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> M </td>
<td> <i>master</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> SEC </td>
<td> <i>secondary</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> REC </td>
<td> recovering
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> UNK </td>
<td> unknown
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> SLV </td>
<td> <i>slave</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></dl>
<h2>USAGE</h2>
<p> In the first example, <code>mongostat</code> will return data every second for 20 seconds. <code>mongostat</code> collects data from the <code>mongod</code> instance running on the localhost interface on port 27017. All of the following invocations produce identical behavior: </p>
<pre>
mongostat --rowcount 20 1
mongostat --rowcount 20
mongostat -n 20 1
mongostat -n 20
</pre>
<p> In the next example, <code>mongostat</code> returns data every 5 minutes (or 300 seconds) for as long as the program runs. <code>mongostat</code> collects data from the <code>mongod</code> instance running on the localhost interface on port <code>27017</code>. Both of the following invocations produce identical behavior. </p>
<pre>
mongostat --rowcount 0 300
mongostat -n 0 300
mongostat 300
</pre>
<p> In the following example, <code>mongostat</code> returns data every 5 minutes for an hour (12 times.) <code>mongostat</code> collects data from the <code>mongod</code> instance running on the localhost interface on port 27017. Both of the following invocations produce identical behavior. </p>
<pre>
mongostat --rowcount 12 300
mongostat -n 12 300
</pre>
<p> In many cases, using the <i>&#8211;discover</i> will help provide a more complete snapshot of the state of an entire group of machines. If a <code>mongos</code> process connected to a <i>sharded cluster</i> is running on port <code>27017</code> of the local machine, you can use the following form to return statistics from all members of the cluster: </p>
<pre>
mongostat --discover
</pre>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
