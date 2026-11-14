---
title: "mongodump(1)"
name: "mongodump"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongodump/"
description: "mongodump – MongoDB Data Dump Utility"
---

<h2>NAME</h2>
<p> mongodump &#8211; MongoDB Data Dump Utility</p>
<h2>SYNOPSIS</h2>
<p> <code>mongodump</code> is a utility for creating a binary export of the contents of a database. Consider using this utility as part an effective <code>backup strategy</code>. Use <code>mongodump</code> in conjunction with <code>mongorestore</code> to restore databases. </p>
<p> <code>mongodump</code> can read data from either <code>mongod</code> or <code>mongos</code> instances, in addition to reading directly from MongoDB data files without an active <code>mongod</code>. </p>
<p> <code>SEE ALSO:</code> <code>mongorestore</code>, <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/backup-sharded-cluster-with-database-dumps">http://docs.mongodb.org/manual/tutorial/backup-sharded-cluster-with-database-dumps</a> and <a rel="nofollow" href="http://docs.mongodb.org/manual/core/backups.">http://docs.mongodb.org/manual/core/backups.</a></p>
<h2>BEHAVIOR</h2>
<p> <code>mongodump</code> does <i>not</i> dump the content of the <code>local</code> database. </p>
<p> The data format used by <code>mongodump</code> from version 2.2 or later is <i>incompatible</i> with earlier versions of <code>mongod</code>. Do not use recent versions of <code>mongodump</code> to back up older data stores. </p>
<p> When running <code>mongodump</code> against a <code>mongos</code> instance where the <i>sharded cluster</i> consists of <i>replica sets</i>, the <i>read preference</i> of the operation will prefer reads from <i>secondary</i> members of the set. </p>
<p> Changed in version 2.2: When used in combination with <code>fsync</code> or <code>db.fsyncLock()</code>, <code>mongod</code> may block some reads, including those from <code>mongodump</code>, when queued write operation waits behind the <code>fsync</code> lock. </p>
<h2>REQUIRED ACCESS</h2>
<h3>Backup Collections</h3>
<p> To backup all the databases in a cluster via <code>mongodump</code>, you should have the <code>backup</code> role. The <code>backup</code> role provides all the needed privileges for backing up all database. The role confers no additional access, in keeping with the policy of <i>least privilege</i>. </p>
<p> To backup a given database, you must have <code>read</code> access on the database. Several roles provide this access, including the <code>backup</code> role. </p>
<p> To backup the <code>system.profile</code> collection in a database, you must have <code>read</code> access on certain system collections in the database. Several roles provide this access, including the <code>clusterAdmin</code> and <code>dbAdmin</code> roles.</p>
<h3>Backup Users</h3>
<p> Changed in version 2.6. </p>
<p> To backup users and <i>user-defined roles</i> for a given database, you must have access to the <code>admin</code> database. MongoDB stores the user data and role definitions for all databases in the <code>admin</code> database. </p>
<p> Specifically, to backup a given database&#8217;s users, you must have the <code>find</code> <i>action</i> on the <code>admin</code> database&#8217;s <code>admin.system.users</code> collection. The <code>backup</code> and <code>userAdminAnyDatabase</code> roles both provide this privilege. </p>
<p> To backup the user-defined roles on a database, you must have the <code>find</code> action on the <code>admin</code> database&#8217;s <code>admin.system.roles</code> collection. Both the <code>backup</code> and <code>userAdminAnyDatabase</code> roles provide this privilege.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongodump</code></p>
<dd>
<dt><code>mongodump</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongodump</code> options and usage.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;quiet</code></p>
<dd> Runs <code>mongodump</code> in a quiet mode that attempts to limit the amount of output. This option suppresses:</p>
<dt>&bull;</p>
<dd> output from <i>database commands</i></p>
<dt>&bull;</p>
<dd> replication activity</p>
<dt>&bull;</p>
<dd> connection accepted events</p>
<dt>&bull;</p>
<dd> connection closed events</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongodump</code> release number.</p>
<dt><code>&#8211;host &lt;hostname&gt;&lt;:port&gt;, -h</code></p>
<dd> Specifies a resolvable hostname for the <code>mongod</code> to which to connect. By default <code>mongodump</code> attempts to connect to a MongoDB instance running on the localhost on port number <code>27017</code>. </p>
<p> To connect to a replica set, specify the replica set seed name and the seed list of set members. Use the following format: </p>
<pre>
&lt;replica_set_name&gt;/&lt;hostname1&gt;&lt;:port&gt;,&lt;hostname2:&lt;port&gt;,...
</pre>
<p> You can always connect directly to a single MongoDB instance by specifying the host and port number directly.</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port number when the MongoDB instance is not running on the standard port of <code>27017</code>. You may also specify the port number using the <code>&#8211;host</code> option.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongodump</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongodump</code>, disable IPv6 support by default.</p>
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
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongodump</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongodump</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
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
<p> Directs <code>mongodump</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;username &lt;username&gt;, -u</code></p>
<dd> Specifies a username with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;password</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;password &lt;password&gt;, -p</code></p>
<dd> Specifies a password with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;username</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;authenticationDatabase &lt;dbname&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the database that holds the user&#8217;s credentials. If you do not specify an authentication database, <code>mongodump</code> assumes that the database specified as the argument to the <i>&#8211;db</i> option holds the user&#8217;s credentials.</p>
<dt><code>&#8211;authenticationMechanism &lt;name&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the authentication mechanism. By default, the authentication mechanism is <code>MONGODB-CR</code>, which is the MongoDB challenge/response authentication mechanism. In MongoDB Enterprise, <code>mongodump</code> also includes support for <code>GSSAPI</code> to handle Kerberos authentication. See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication">http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication</a> for more information about Kerberos authentication.</p>
<dt><code>&#8211;dbpath &lt;path&gt;</code></p>
<dd> Specifies the directory of the MongoDB data files. If used, the <i>&#8211;dbpath</i> option enables <code>mongodump</code> to attach directly to local data files without a running <code>mongod</code>. When run with <i>&#8211;dbpath</i>, <code>mongodump</code> locks access to the data directory. No <code>mongod</code> can access the same path while the process runs.</p>
<dt><code>&#8211;directoryperdb</code></p>
<dd> When used in conjunction with the corresponding option in <code>mongod</code>, allows <code>mongodump</code> to access data from MongoDB instances that use an on-disk format where every database has a distinct directory. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;journal</code></p>
<dd> Allows <code>mongodump</code> operations to use the durability <i>journal</i> to ensure data files remain valid and recoverable. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;db &lt;database&gt;, -d</code></p>
<dd> Specifies a database to backup. If you do not specify a database, <code>mongodump</code> copies all databases in this instance into the dump files.</p>
<dt><code>&#8211;collection &lt;collection&gt;, -c</code></p>
<dd> Specifies a collection to backup. If you do not specify a collection, this option copies all collections in the specified database or instance to the dump files.</p>
<dt><code>&#8211;out &lt;path&gt;, -o</code></p>
<dd> Specifies the directory where <code>mongodump</code> saves the output of the database dump. By default, <code>mongodump</code> saves output files in a directory named <code>dump</code> in the current working directory. </p>
<p> To send the database dump to standard output, specify &quot;<code>&#8211;</code>&quot; instead of a path. Write to standard output if you want process the output before saving it, such as to use <code>gzip</code> to compress the dump. When writing standard output, <code>mongodump</code> does not write the metadata that writes in a <code>&lt;dbname&gt;.metadata.json</code> file when writing to files directly.</p>
<dt><code>&#8211;query &lt;json&gt;, -q</code></p>
<dd> Provides a <i>JSON document</i> as a query that optionally limits the documents included in the output of <code>mongodump</code>.</p>
<dt><code>&#8211;oplog</code></p>
<dd> Ensures that <code>mongodump</code> creates a dump of the database that includes a partial <i>oplog</i> containing operations from the duration of the <code>mongodump</code> operation. This oplog produces an effective point-in-time snapshot of the state of a <code>mongod</code> instance. To restore to a specific point-in-time backup, use the output created with this option in conjunction with <i>mongorestore &#8211;oplogReplay</i>. </p>
<p> Without <i>&#8211;oplog</i>, if there are write operations during the dump operation, the dump will not reflect a single moment in time. Changes made to the database during the update process can affect the output of the backup. </p>
<p> <i>&#8211;oplog</i> has no effect when running <code>mongodump</code> against a <code>mongos</code> instance to dump the entire contents of a sharded cluster. However, you can use <i>&#8211;oplog</i> to dump individual shards. </p>
<p> <i>&#8211;oplog</i> only works against nodes that maintain an <i>oplog</i>. This includes all members of a replica set, as well as <i>master</i> nodes in master/slave replication deployments. </p>
<p> <i>&#8211;oplog</i> does not dump the oplog collection.</p>
<dt><code>&#8211;repair</code></p>
<dd> Runs a repair option in addition to dumping the database. The repair option attempts to repair a database that may be in an invalid state as a result of an improper shutdown or <code>mongod</code> crash. </p>
<p> The <i>&#8211;repair</i> option uses aggressive data-recovery algorithms that may produce a large amount of duplication.</p>
<dt><code>&#8211;forceTableScan</code></p>
<dd> Forces <code>mongodump</code> to scan the data store directly: typically, <code>mongodump</code> saves entries as they appear in the index of the <code>_id</code> field. Use <i>&#8211;forceTableScan</i> to skip the index and scan the data directly. Typically there are two cases where this behavior is preferable to the default:</p>
<dt>1.</p>
<dd> If you have key sizes over 800 bytes that would not be present in the <code>_id</code> index.</p>
<dt>2.</p>
<dd> Your database uses a custom <code>_id</code> field. </p>
<p> When you run with <i>&#8211;forceTableScan</i>, <code>mongodump</code> does not use <code>$snapshot</code>. As a result, the dump produced by <code>mongodump</code> can reflect the state of the database at many different points in time. </p>
<p> <code>IMPORTANT:</code> Use <i>&#8211;forceTableScan</i> with extreme caution and consideration.</p>
<dt><code>&#8211;dumpDbUsersAndRoles</code></p>
<dd> Includes user and role definitions when performing <code>mongodump</code> on a specific database. This option applies only when you specify a database in the <i>&#8211;db</i> option. MongoDB always includes user and role definitions when <code>mongodump</code> applies to an entire instance and not just a specific database.</dl>
<h2>USE</h2>
<p> See the <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/backup-with-mongodump">http://docs.mongodb.org/manual/tutorial/backup-with-mongodump</a> for a larger overview of <code>mongodump</code> usage. Also see the <code>mongorestore</code> document for an overview of the <code>mongorestore</code>, which provides the related inverse functionality. </p>
<p> The following command creates a dump file that contains only the collection named <code>collection</code> in the database named <code>test</code>. In this case the database is running on the local interface on port <code>27017</code>: </p>
<pre>
mongodump --collection collection --db test
</pre>
<p> In the next example, <code>mongodump</code> creates a backup of the database instance stored in the <code>/srv/mongodb</code> directory on the local machine. This requires that no <code>mongod</code> instance is using the <code>/srv/mongodb</code> directory. </p>
<pre>
mongodump --dbpath /srv/mongodb
</pre>
<p> In the final example, <code>mongodump</code> creates a database dump located at <code>/opt/backup/mongodump-2011-10-24</code>, from a database running on port <code>37017</code> on the host <code>mongodb1.example.net</code> and authenticating using the username <code>user</code> and the password <code>pass</code>, as follows: </p>
<pre><code>
mongodump-- host mongodb1.example.net-- port 37017 --username user-- password pass-- out / opt / backup / mongodump - 2011 - 10 - 24
</code></pre>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
