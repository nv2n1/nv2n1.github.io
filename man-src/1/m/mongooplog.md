---
title: "mongooplog(1)"
name: "mongooplog"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongooplog/"
description: "mongooplog – MongoDB Oplog Utility"
---

<h2>NAME</h2>
<p> mongooplog &#8211; MongoDB Oplog Utility </p>
<p> New in version 2.2. </p>
<h2>SYNOPSIS</h2>
<p> <code>mongooplog</code> is a simple tool that polls operations from the <i>replication</i> <i>oplog</i> of a remote server, and applies them to the local server. This capability supports certain classes of real-time migrations that require that the source server remain online and in operation throughout the migration process. </p>
<p> Typically this command will take the following form: </p>
<pre>
mongooplog  --from mongodb0.example.net --host mongodb1.example.net
</pre>
<p> This command copies oplog entries from the <code>mongod</code> instance running on the host <code>mongodb0.example.net</code> and duplicates operations to the host <code>mongodb1.example.net</code>. If you do not need to keep the <i>&#8211;from</i> host running during the migration, consider using <code>mongodump</code> and <code>mongorestore</code> or another <code>backup</code> operation, which may be better suited to your operation. </p>
<p> <code>NOTE:</code> If the <code>mongod</code> instance specified by the <i>&#8211;from</i> argument is running with <code>authentication</code>, then <code>mongooplog</code> will not be able to copy oplog entries. </p>
<p> <code>SEE ALSO:</code> <code>mongodump</code>, <code>mongorestore</code>, <a rel="nofollow" href="http://docs.mongodb.org/manual/core/backups,">http://docs.mongodb.org/manual/core/backups,</a> <a href="http://docs.mongodb.org/manual/core/replica-set-oplog.">http://docs.mongodb.org/manual/core/replica-set-oplog.</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongooplog</code></p>
<dd>
<dt><code>mongooplog</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongooplog</code> options and usage.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;quiet</code></p>
<dd> Runs <code>mongooplog</code> in a quiet mode that attempts to limit the amount of output. This option suppresses:</p>
<dt>&bull;</p>
<dd> output from <i>database commands</i></p>
<dt>&bull;</p>
<dd> replication activity</p>
<dt>&bull;</p>
<dd> connection accepted events</p>
<dt>&bull;</p>
<dd> connection closed events</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongooplog</code> release number.</p>
<dt><code>&#8211;host &lt;hostname&gt;&lt;:port&gt;, -h</code></p>
<dd> Specifies a resolvable hostname for the <code>mongod</code> instance to which <code>mongooplog</code> will apply <i>oplog</i> operations retrieved from the server specified by the <i>&#8211;from</i> option. </p>
<p> By default <code>mongooplog</code> attempts to connect to a MongoDB instance running on the localhost on port number <code>27017</code>. </p>
<p> To connect to a replica set, specify the replica set seed name and the seed list of set members. Use the following format: </p>
<pre>
&lt;replica_set_name&gt;/&lt;hostname1&gt;&lt;:port&gt;,&lt;hostname2:&lt;port&gt;,...
</pre>
<p> You can always connect directly to a single MongoDB instance by specifying the host and port number directly.</p>
<dt><code>&#8211;port</code></p>
<dd> Specifies the port number of the <code>mongod</code> instance where <code>mongooplog</code> will apply <i>oplog</i> entries. Specify this option only if the MongoDB instance to connect to is not running on the standard port of <code>27017</code>. You may also specify a port number using the <i>&#8211;host</i> command.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongooplog</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongooplog</code>, disable IPv6 support by default.</p>
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
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongooplog</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongooplog</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
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
<p> Directs <code>mongooplog</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;username &lt;username&gt;, -u</code></p>
<dd> Specifies a username with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;password</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;password &lt;password&gt;, -p</code></p>
<dd> Specifies a password with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;username</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;authenticationDatabase &lt;dbname&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the database that holds the user&#8217;s credentials. If you do not specify an authentication database, <code>mongooplog</code> assumes that the database specified as the argument to the <i>&#8211;db</i> option holds the user&#8217;s credentials.</p>
<dt><code>&#8211;authenticationMechanism &lt;name&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the authentication mechanism. By default, the authentication mechanism is <code>MONGODB-CR</code>, which is the MongoDB challenge/response authentication mechanism. In MongoDB Enterprise, <code>mongooplog</code> also includes support for <code>GSSAPI</code> to handle Kerberos authentication. See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication">http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication</a> for more information about Kerberos authentication.</p>
<dt><code>&#8211;dbpath &lt;path&gt;</code></p>
<dd> Specifies a directory, containing MongoDB data files, to which <code>mongooplog</code> will apply operations from the <i>oplog</i> of the database specified with the <i>&#8211;from</i> option. </p>
<p> When used, the <i>&#8211;dbpath</i> option enables <code>mongo</code> to attach directly to local data files and write data without a running <code>mongod</code> instance. </p>
<p> To run with <i>&#8211;dbpath</i>, <code>mongooplog</code> needs to restrict access to the data directory: as a result, no <code>mongod</code> can be access the same path while the process runs.</p>
<dt><code>&#8211;directoryperdb</code></p>
<dd> When used in conjunction with the corresponding option in <code>mongod</code>, allows <code>mongooplog</code> to access data from MongoDB instances that use an on-disk format where every database has a distinct directory. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;journal</code></p>
<dd> Allows <code>mongooplog</code> operations to use the durability <i>journal</i> to ensure data files remain valid and recoverable. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;db &lt;database&gt;, -d</code></p>
<dd> Specifies the name of the database on which to run <code>mongooplog</code>.</p>
<dt><code>&#8211;collection &lt;collection&gt;, -c</code></p>
<dd> Specifies the collection to export.</p>
<dt><code>&#8211;seconds &lt;number&gt;, -s</code></p>
<dd> Specify a number of seconds of operations for <code>mongooplog</code> to pull from the <i>remote host</i>. Unless specified the default value is <code>86400</code> seconds, or 24 hours.</p>
<dt><code>&#8211;from &lt;host[:port]&gt;</code></p>
<dd> Specify the host for <code>mongooplog</code> to retrieve <i>oplog</i> operations from. <code>mongooplog</code> <i>requires</i> this option. </p>
<p> Unless you specify the <i>&#8211;host</i> option, <code>mongooplog</code> will apply the operations collected with this option to the oplog of the <code>mongod</code> instance running on the localhost interface connected to port <code>27017</code>.</p>
<dt><code>&#8211;oplogns &lt;namespace&gt;</code></p>
<dd> Specify a namespace in the <i>&#8211;from</i> host where the oplog resides. The default value is <code>local.oplog.rs</code>, which is the where <i>replica set</i> members store their operation log. However, if you&#8217;ve copied <i>oplog</i> entries into another database or collection, use this option to copy oplog entries stored in another location. Namespaces take the form of <code>[database].[collection]</code>.</dl>
<h2>USE</h2>
<p> Consider the following prototype <code>mongooplog</code> command: </p>
<pre>
mongooplog  --from mongodb0.example.net --host mongodb1.example.net
</pre>
<p> Here, entries from the <i>oplog</i> of the <code>mongod</code> running on port <code>27017</code>. This only pull entries from the last 24 hours. </p>
<p> Use the <i>&#8211;seconds</i> argument to capture a greater or smaller amount of time. Consider the following example: </p>
<pre>
mongooplog  --from mongodb0.example.net --seconds 172800
</pre>
<p> In this operation, <code>mongooplog</code> captures 2 full days of operations. To migrate 12 hours of <i>oplog</i> entries, use the following form: </p>
<pre>
mongooplog  --from mongodb0.example.net --seconds 43200
</pre>
<p> For the previous two examples, <code>mongooplog</code> migrates entries to the <code>mongod</code> process running on the localhost interface connected to the <code>27017</code> port. <code>mongooplog</code> can also operate directly on MongoDB&#8217;s data files if no <code>mongod</code> is running on the <i>target</i> host. Consider the following example: </p>
<pre>
mongooplog  --from mongodb0.example.net --dbpath /srv/mongodb --journal
</pre>
<p> Here, <code>mongooplog</code> imports <i>oplog</i> operations from the <code>mongod</code> host connected to port <code>27017</code>. This migrates operations to the MongoDB data files stored in the <code>/srv/mongodb</code> directory. Additionally <code>mongooplog</code> will use the durability <i>journal</i> to ensure that the data files remain valid.</p>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
