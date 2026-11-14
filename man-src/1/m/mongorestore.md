---
title: "mongorestore(1)"
name: "mongorestore"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongorestore/"
description: "mongorestore – MongoDB Data Restoration Tool"
---

<h2>NAME</h2>
<p> mongorestore &#8211; MongoDB Data Restoration Tool</p>
<h2>SYNOPSIS</h2>
<p> The <code>mongorestore</code> program writes data from a binary database dump created by <code>mongodump</code> to a MongoDB instance. <code>mongorestore</code> can create a new database or add data to an existing database. </p>
<p> <code>mongorestore</code> can write data to either <i>mongod</i> or <code>mongos</code> instances, in addition to writing directly to MongoDB data files without an active <code>mongod</code>.</p>
<h2>BEHAVIOR</h2>
<p> If you restore to an existing database, <code>mongorestore</code> will only insert into the existing database, and does not perform updates of any kind. If existing documents have the same value <code>_id</code> field in the target database and collection, <code>mongorestore</code> will <i>not</i> overwrite those documents. </p>
<p> Remember the following properties of <code>mongorestore</code> behavior:</p>
<dl>
<dt>&bull;</p>
<dd> <code>mongorestore</code> recreates indexes recorded by <code>mongodump</code>.</p>
<dt>&bull;</p>
<dd> all operations are inserts, not updates.</p>
<dt>&bull;</p>
<dd> <code>mongorestore</code> does not wait for a response from a <code>mongod</code> to ensure that the MongoDB process has received or recorded the operation. </p>
<p> The <code>mongod</code> will record any errors to its log that occur during a restore operation, but <code>mongorestore</code> will not receive errors. </p>
<p> The data format used by <code>mongodump</code> from version 2.2 or later is <i>incompatible</i> with earlier versions of <code>mongod</code>. Do not use recent versions of <code>mongodump</code> to back up older data stores.</dl>
<h2>REQUIRED ACCESS TO RESTORE USER DATA</h2>
<p> Changed in version 2.6. </p>
<p> To restore users and <i>user-defined roles</i> on a given database, you must have access to the <code>admin</code> database. MongoDB stores the user data and role definitions for all databases in the <code>admin</code> database. </p>
<p> Specifically, to restore users to a given database, you must have the <code>insert</code> <i>action</i> on the <code>admin</code> database&#8217;s <code>admin.system.users</code> collection. The <code>restore</code> role provides this privilege. </p>
<p> To restore user-defined roles to a database, you must have the <code>insert</code> action on the <code>admin</code> database&#8217;s <code>admin.system.roles</code> collection. The <code>restore</code> role provides this privilege.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongorestore</code></p>
<dd>
<dt><code>mongorestore</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongorestore</code> options and usage.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;quiet</code></p>
<dd> Runs <code>mongorestore</code> in a quiet mode that attempts to limit the amount of output. This option suppresses:</p>
<dt>&bull;</p>
<dd> output from <i>database commands</i></p>
<dt>&bull;</p>
<dd> replication activity</p>
<dt>&bull;</p>
<dd> connection accepted events</p>
<dt>&bull;</p>
<dd> connection closed events</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongorestore</code> release number.</p>
<dt><code>&#8211;host &lt;hostname&gt;&lt;:port&gt;, -h</code></p>
<dd> Specifies a resolvable hostname for the <code>mongod</code> to which to connect. By default <code>mongorestore</code> attempts to connect to a MongoDB instance running on the localhost on port number <code>27017</code>. </p>
<p> To connect to a replica set, specify the replica set seed name and the seed list of set members. Use the following format: </p>
<pre>
&lt;replica_set_name&gt;/&lt;hostname1&gt;&lt;:port&gt;,&lt;hostname2:&lt;port&gt;,...
</pre>
<p> You can always connect directly to a single MongoDB instance by specifying the host and port number directly.</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port number when the MongoDB instance is not running on the standard port of <code>27017</code>. You may also specify the port number using the <code>&#8211;host</code> option.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongorestore</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongorestore</code>, disable IPv6 support by default.</p>
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
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongorestore</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongorestore</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
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
<p> Directs <code>mongorestore</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;username &lt;username&gt;, -u</code></p>
<dd> Specifies a username with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;password</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;password &lt;password&gt;, -p</code></p>
<dd> Specifies a password with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;username</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;authenticationDatabase &lt;dbname&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the database that holds the user&#8217;s credentials. If you do not specify an authentication database, <code>mongorestore</code> assumes that the database specified as the argument to the <i>&#8211;db</i> option holds the user&#8217;s credentials.</p>
<dt><code>&#8211;authenticationMechanism &lt;name&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the authentication mechanism. By default, the authentication mechanism is <code>MONGODB-CR</code>, which is the MongoDB challenge/response authentication mechanism. In MongoDB Enterprise, <code>mongorestore</code> also includes support for <code>GSSAPI</code> to handle Kerberos authentication. See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication">http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication</a> for more information about Kerberos authentication.</p>
<dt><code>&#8211;dbpath &lt;path&gt;</code></p>
<dd> Specifies the directory of the MongoDB data files. If used, the <i>&#8211;dbpath</i> option enables <code>mongorestore</code> to attach directly to local data files without a running <code>mongod</code>. When run with <i>&#8211;dbpath</i>, <code>mongorestore</code> locks access to the data directory. No <code>mongod</code> can access the same path while the process runs.</p>
<dt><code>&#8211;directoryperdb</code></p>
<dd> When used in conjunction with the corresponding option in <code>mongod</code>, allows <code>mongorestore</code> to access data from MongoDB instances that use an on-disk format where every database has a distinct directory. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;journal</code></p>
<dd> Allows <code>mongorestore</code> operations to use the durability <i>journal</i> to ensure data files remain valid and recoverable. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;db &lt;database&gt;, -d</code></p>
<dd> Specifies a database for <code>mongorestore</code> to restore data <i>into</i>. If the database does not exist, <code>mongorestore</code> creates the database. If you do not specify a <code>&lt;db&gt;</code>, <code>mongorestore</code> creates new databases that correspond to the databases where data originated and data may be overwritten. Use this option to restore data into a MongoDB instance that already has data. </p>
<p> <i>&#8211;db</i> does <i>not</i> control which <i>BSON</i> files <code>mongorestore</code> restores. You must use the <code>mongorestore</code> <i>path option</i> to limit that restored data.</p>
<dt><code>&#8211;collection &lt;collection&gt;, -c</code></p>
<dd> Specifies a single collection for <code>mongorestore</code> to restore. If you do not specify <i>&#8211;collection</i>, <code>mongorestore</code> takes the collection name from the input filename. If the input file has an extension, MongoDB omits the extension of the file from the collection name.</p>
<dt><code>&#8211;objcheck</code></p>
<dd> Forces <code>mongorestore</code> to validate all requests from clients upon receipt to ensure that clients never insert invalid documents into the database. For objects with a high degree of sub-document nesting, <i>&#8211;objcheck</i> can have a small impact on performance. You can set <i>&#8211;noobjcheck</i> to disable object checking at run-time. </p>
<p> Changed in version 2.4: MongoDB enables <i>&#8211;objcheck</i> by default, to prevent any client from inserting malformed or invalid BSON into a MongoDB database. </p>
<dt><code>&#8211;noobjcheck</code></p>
<dd> New in version 2.4. </p>
<p> Disables the default document validation that MongoDB performs on all incoming BSON documents.</p>
<dt><code>&#8211;filter &lt;JSON&gt;</code></p>
<dd> Limits the documents that <code>mongorestore</code> imports to only those documents that match the JSON document specified as <code>&#8216;&lt;JSON&gt;&#8217;</code>. Be sure to include the document in single quotes to avoid interaction with your system&#8217;s shell environment. For an example of <i>&#8211;filter</i>, see <i>backup-restore-filter</i>.</p>
<dt><code>&#8211;drop</code></p>
<dd> Modifies the restoration procedure to drop every collection from the target database before restoring the collection from the dumped backup.</p>
<dt><code>&#8211;oplogReplay</code></p>
<dd> Replays the <i>oplog</i> after restoring the dump to ensure that the current state of the database reflects the point-in-time backup captured with the &quot;<i>mongodump &#8211;oplog</i>&quot; command. For an example of <i>&#8211;oplogReplay</i>, see <i>backup-restore-oplogreplay</i>.</p>
<dt><code>&#8211;oplogLimit &lt;timestamp&gt;</code></p>
<dd> New in version 2.2. </p>
<p> Prevents <code>mongorestore</code> from applying <i>oplog</i> entries newer than the <code>&lt;timestamp&gt;</code>. Specify <code>&lt;timestamp&gt;</code> values in the form of <code>&lt;time_t&gt;:&lt;ordinal&gt;</code>, where <code>&lt;time_t&gt;</code> is the seconds since the UNIX epoch, and <code>&lt;ordinal&gt;</code> represents a counter of operations in the oplog that occurred in the specified second. </p>
<p> You must use <i>&#8211;oplogLimit</i> in conjunction with the <i>&#8211;oplogReplay</i> option.</p>
<dt><code>&#8211;keepIndexVersion</code></p>
<dd> Prevents <code>mongorestore</code> from upgrading the index to the latest version during the restoration process.</p>
<dt><code>&#8211;noIndexRestore</code></p>
<dd> New in version 2.2. </p>
<p> Prevents <code>mongorestore</code> from restoring and building indexes as specified in the corresponding <code>mongodump</code> output.</p>
<dt><code>&#8211;noOptionsRestore</code></p>
<dd> New in version 2.2. </p>
<p> Prevents <code>mongorestore</code> from setting the collection options, such as those specified by the <code>collMod</code> <i>database command</i>, on restored collections.</p>
<dt><code>&#8211;w &lt;number of replicas per write&gt;</code></p>
<dd> New in version 2.2. </p>
<p> Specifies the <i>write concern</i> for each write operation that <code>mongorestore</code> writes to the target database. By default, <code>mongorestore</code> does not wait for a response for <i>write acknowledgment</i>.</p>
<dt><code>&lt;path&gt;</code></p>
<dd> The final argument of the <code>mongorestore</code> command is a directory path. This argument specifies the location of the database dump from which to restore.</dl>
<h2>USE</h2>
<p> See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/backup-with-mongodump">http://docs.mongodb.org/manual/tutorial/backup-with-mongodump</a> for a larger overview of <code>mongorestore</code> usage. Also see the <code>mongodump</code> document for an overview of the <code>mongodump</code>, which provides the related inverse functionality. </p>
<p> Consider the following example: </p>
<pre>
mongorestore --collection people --db accounts dump/accounts/people.bson
</pre>
<p> Here, <code>mongorestore</code> reads the database dump in the <code>dump/</code> sub-directory of the current directory, and restores <i>only</i> the documents in the collection named <code>people</code> from the database named <code>accounts</code>. <code>mongorestore</code> restores data to the instance running on the localhost interface on port <code>27017</code>. </p>
<p> In the next example, <code>mongorestore</code> restores a backup of the database instance located in <code>dump</code> to a database instance stored in the <code>/srv/mongodb</code> on the local machine. This requires that there are no active <code>mongod</code> instances attached to <code>/srv/mongodb</code> data directory. </p>
<pre>
mongorestore --dbpath /srv/mongodb
</pre>
<p> In the final example, <code>mongorestore</code> restores a database dump located at <code>/opt/backup/mongodump-2011-10-24</code>, to a database running on port <code>37017</code> on the host <code>mongodb1.example.net</code>. The <code>mongorestore</code> command authenticates to the MongoDB instance using the username <code>user</code> and the password <code>pass</code>, as follows: </p>
<pre><code>
mongorestore-- host mongodb1.example.net-- port 37017 --username user-- password pass / opt / backup / mongodump - 2011 - 10 - 24
</code></pre>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
