---
title: "mongotop(1)"
name: "mongotop"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongotop/"
description: "mongotop – MongoDB Activity Monitor"
---

<h2>NAME</h2>
<p> mongotop &#8211; MongoDB Activity Monitor</p>
<h2>SYNOPSIS</h2>
<p> <code>mongotop</code> provides a method to track the amount of time a MongoDB instance spends reading and writing data. <code>mongotop</code> provides statistics on a per-collection level. By default, <code>mongotop</code> returns values every second. </p>
<p> <code>SEE ALSO:</code> For more information about monitoring MongoDB, see <a rel="nofollow" href="http://docs.mongodb.org/manual/administration/monitoring.">http://docs.mongodb.org/manual/administration/monitoring.</a> </p>
<p> For additional background on various other MongoDB status outputs see:</p>
<dl>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/command/serverStatus">http://docs.mongodb.org/manual/reference/command/serverStatus</a></p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/command/replSetGetStatus">http://docs.mongodb.org/manual/reference/command/replSetGetStatus</a></p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/command/dbStats">http://docs.mongodb.org/manual/reference/command/dbStats</a></p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/command/collStats">http://docs.mongodb.org/manual/reference/command/collStats</a> </p>
<p> For an additional utility that provides MongoDB metrics see <code>mongostat</code>.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongotop</code></p>
<dd>
<dt><code>mongotop</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongotop</code> options and usage.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;quiet</code></p>
<dd> Runs <code>mongotop</code> in a quiet mode that attempts to limit the amount of output. This option suppresses:</p>
<dt>&bull;</p>
<dd> output from <i>database commands</i></p>
<dt>&bull;</p>
<dd> replication activity</p>
<dt>&bull;</p>
<dd> connection accepted events</p>
<dt>&bull;</p>
<dd> connection closed events</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongotop</code> release number.</p>
<dt><code>&#8211;host &lt;hostname&gt;&lt;:port&gt;, -h</code></p>
<dd> Specifies a resolvable hostname for the <code>mongod</code> to which to connect. By default <code>mongotop</code> attempts to connect to a MongoDB instance running on the localhost on port number <code>27017</code>. </p>
<p> To connect to a replica set, specify the replica set seed name and the seed list of set members. Use the following format: </p>
<pre>
&lt;replica_set_name&gt;/&lt;hostname1&gt;&lt;:port&gt;,&lt;hostname2:&lt;port&gt;,...
</pre>
<p> You can always connect directly to a single MongoDB instance by specifying the host and port number directly.</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port number when the MongoDB instance is not running on the standard port of <code>27017</code>. You may also specify the port number using the <code>&#8211;host</code> option.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongotop</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongotop</code>, disable IPv6 support by default.</p>
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
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongotop</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongotop</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
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
<p> Directs <code>mongotop</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;username &lt;username&gt;, -u</code></p>
<dd> Specifies a username with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;password</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;password &lt;password&gt;, -p</code></p>
<dd> Specifies a password with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;username</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;authenticationDatabase &lt;dbname&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the database that holds the user&#8217;s credentials. If you do not specify an authentication database, <code>mongotop</code> assumes that the database specified as the argument to the <i>&#8211;db</i> option holds the user&#8217;s credentials.</p>
<dt><code>&#8211;authenticationMechanism &lt;name&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the authentication mechanism. By default, the authentication mechanism is <code>MONGODB-CR</code>, which is the MongoDB challenge/response authentication mechanism. In MongoDB Enterprise, <code>mongotop</code> also includes support for <code>GSSAPI</code> to handle Kerberos authentication. See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication">http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication</a> for more information about Kerberos authentication.</p>
<dt><code>&#8211;locks</code></p>
<dd> Toggles the mode of <code>mongotop</code> to report on use of per-database <i>locks</i>. These data are useful for measuring concurrent operations and lock percentage.</p>
<dt><code>&lt;sleeptime&gt;</code></p>
<dd> The final argument is the length of time, in seconds, that <code>mongotop</code> waits in between calls. By default <code>mongotop</code> returns data every second.</dl>
<h2>FIELDS</h2>
<p> <code>mongotop</code> returns time values specified in milliseconds (ms.) </p>
<p> <code>mongotop</code> only reports active namespaces or databases, depending on the <i>&#8211;locks</i> option. If you don&#8217;t see a database or collection, it has received no recent activity. You can issue a simple operation in the <code>mongo</code> shell to generate activity to affect the output of <code>mongotop</code>.</p>
<dl>
<dt><code>mongotop.ns</code></p>
<dd> Contains the database namespace, which combines the database name and collection. </p>
<p> Changed in version 2.2: If you use the <i>&#8211;locks</i>, the <code>ns</code> field does not appear in the <code>mongotop</code> output. </p>
<dt><code>mongotop.db</code></p>
<dd> New in version 2.2. </p>
<p> Contains the name of the database. The database named <code>.</code> refers to the global lock, rather than a specific database. </p>
<p> This field does not appear unless you have invoked <code>mongotop</code> with the <i>&#8211;locks</i> option.</p>
<dt><code>mongotop.total</code></p>
<dd> Provides the total amount of time that this <code>mongod</code> spent operating on this namespace.</p>
<dt><code>mongotop.read</code></p>
<dd> Provides the amount of time that this <code>mongod</code> spent performing read operations on this namespace.</p>
<dt><code>mongotop.write</code></p>
<dd> Provides the amount of time that this <code>mongod</code> spent performing write operations on this namespace.</p>
<dt><code>mongotop.&lt;timestamp&gt;</code></p>
<dd> Provides a time stamp for the returned data.</dl>
<h2>USE</h2>
<p> By default <code>mongotop</code> connects to the MongoDB instance running on the localhost port <code>27017</code>. However, <code>mongotop</code> can optionally connect to remote <code>mongod</code> instances. See the <i>mongotop options</i> for more information. </p>
<p> To force <code>mongotop</code> to return less frequently specify a number, in seconds at the end of the command. In this example, <code>mongotop</code> will return every 15 seconds. </p>
<pre>
mongotop 15
</pre>
<p> This command produces the following output: </p>
<pre>
connected to: 127.0.0.1
                    ns       total        read       write           2012-08-13T15:45:40
test.system.namespaces         0ms         0ms         0ms
  local.system.replset         0ms         0ms         0ms
  local.system.indexes         0ms         0ms         0ms
  admin.system.indexes         0ms         0ms         0ms
                admin.         0ms         0ms         0ms
                    ns       total        read       write           2012-08-13T15:45:55
test.system.namespaces         0ms         0ms         0ms
  local.system.replset         0ms         0ms         0ms
  local.system.indexes         0ms         0ms         0ms
  admin.system.indexes         0ms         0ms         0ms
                admin.         0ms         0ms         0ms
</pre>
<p> To return a <code>mongotop</code> report every 5 minutes, use the following command: </p>
<pre>
mongotop 300
</pre>
<p> To report the use of per-database locks, use <i>mongotop &#8211;locks</i>, which produces the following output: </p>
<pre>
$ mongotop --locks
connected to: 127.0.0.1
                  db       total        read       write          2012-08-13T16:33:34
               local         0ms         0ms         0ms
               admin         0ms         0ms         0ms
                   .         0ms         0ms         0ms
</pre>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
