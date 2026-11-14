---
title: "mongofiles(1)"
name: "mongofiles"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongofiles/"
description: "mongofiles – MongoDB GridFS Utility"
---

<h2>NAME</h2>
<p> mongofiles &#8211; MongoDB GridFS Utility</p>
<h2>SYNOPSIS</h2>
<p> The <code>mongofiles</code> utility makes it possible to manipulate files stored in your MongoDB instance in <i>GridFS</i> objects from the command line. It is particularly useful as it provides an interface between objects stored in your file system and GridFS. </p>
<p> All <code>mongofiles</code> commands have the following form: </p>
<pre>
mongofiles &lt;options&gt; &lt;commands&gt; &lt;filename&gt;
</pre>
<p> The components of the <code>mongofiles</code> command are:</p>
<dl>
<dt>1.</p>
<dd> <i>Options</i>. You may use one or more of these options to control the behavior of <code>mongofiles</code>.</p>
<dt>2.</p>
<dd> <i>Commands</i>. Use one of these commands to determine the action of <code>mongofiles</code>.</p>
<dt>3.</p>
<dd> A filename which is either: the name of a file on your local&#8217;s file system, or a GridFS object. </p>
<p> <code>mongofiles</code>, like <code>mongodump</code>, <code>mongoexport</code>, <code>mongoimport</code>, and <code>mongorestore</code>, can access data stored in a MongoDB data directory without requiring a running <code>mongod</code> instance, if no other <code>mongod</code> is running. </p>
<p> <code>IMPORTANT:</code> For <i>replica sets</i>, <code>mongofiles</code> can only read from the set&#8217;s &#8216;<i>primary</i>.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongofiles</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongofiles</code> options and usage.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;quiet</code></p>
<dd> Runs <code>mongofiles</code> in a quiet mode that attempts to limit the amount of output. This option suppresses:</p>
<dt>&bull;</p>
<dd> output from <i>database commands</i></p>
<dt>&bull;</p>
<dd> replication activity</p>
<dt>&bull;</p>
<dd> connection accepted events</p>
<dt>&bull;</p>
<dd> connection closed events</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongofiles</code> release number.</p>
<dt><code>&#8211;host &lt;hostname&gt;&lt;:port&gt;</code></p>
<dd> Specifies a resolvable hostname for the <code>mongod</code> that holds your GridFS system. By default <code>mongofiles</code> attempts to connect to a MongoDB process running on the localhost port number <code>27017</code>. </p>
<p> Optionally, specify a port number to connect a MongoDB instance running on a port other than 27017.</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port number when the MongoDB instance is not running on the standard port of <code>27017</code>. You may also specify the port number using the <code>&#8211;host</code> option.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongofiles</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongofiles</code>, disable IPv6 support by default.</p>
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
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongofiles</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongofiles</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
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
<p> Directs <code>mongofiles</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;username &lt;username&gt;, -u</code></p>
<dd> Specifies a username with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;password</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;password &lt;password&gt;, -p</code></p>
<dd> Specifies a password with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;username</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;authenticationDatabase &lt;dbname&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the database that holds the user&#8217;s credentials. If you do not specify an authentication database, <code>mongofiles</code> assumes that the database specified as the argument to the <i>&#8211;db</i> option holds the user&#8217;s credentials.</p>
<dt><code>&#8211;authenticationMechanism &lt;name&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the authentication mechanism. By default, the authentication mechanism is <code>MONGODB-CR</code>, which is the MongoDB challenge/response authentication mechanism. In MongoDB Enterprise, <code>mongofiles</code> also includes support for <code>GSSAPI</code> to handle Kerberos authentication. See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication">http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication</a> for more information about Kerberos authentication.</p>
<dt><code>&#8211;dbpath &lt;path&gt;</code></p>
<dd> Specifies the directory of the MongoDB data files. If used, the <i>&#8211;dbpath</i> option enables <code>mongofiles</code> to attach directly to local data files without a running <code>mongod</code>. When run with <i>&#8211;dbpath</i>, <code>mongofiles</code> locks access to the data directory. No <code>mongod</code> can access the same path while the process runs.</p>
<dt><code>&#8211;directoryperdb</code></p>
<dd> When used in conjunction with the corresponding option in <code>mongod</code>, allows <code>mongofiles</code> to access data from MongoDB instances that use an on-disk format where every database has a distinct directory. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;journal</code></p>
<dd> Allows <code>mongofiles</code> operations to use the durability <i>journal</i> to ensure data files remain valid and recoverable. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;db &lt;database&gt;, -d</code></p>
<dd> Specifies the name of the database on which to run <code>mongofiles</code>.</p>
<dt><code>&#8211;collection &lt;collection&gt;, -c</code></p>
<dd> This option has no use in this context and a future release may remove it. See <i>SERVER-4931</i> for more information.</p>
<dt><code>&#8211;local &lt;filename&gt;, -l</code></p>
<dd> Specifies the local filesystem name of a file for get and put operations. </p>
<p> In the <code>mongofiles put</code> and <code>mongofiles get</code> commands, the required <code>&lt;filename&gt;</code> modifier refers to the name the object will have in GridFS. <code>mongofiles</code> assumes that this reflects the file&#8217;s name on the local file system. This setting overrides this default.</p>
<dt><code>&#8211;type &lt;MIME&gt;</code></p>
<dd> Provides the ability to specify a <i>MIME</i> type to describe the file inserted into GridFS storage. <code>mongofiles</code> omits this option in the default operation. </p>
<p> Use only with <code>mongofiles put</code> operations.</p>
<dt><code>&#8211;replace, -r</code></p>
<dd> Alters the behavior of <code>mongofiles put</code> to replace existing GridFS objects with the specified local file, rather than adding an additional object with the same name. </p>
<p> In the default operation, files will not be overwritten by a <code>mongofiles put</code> option.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>list &lt;prefix&gt;</code></p>
<dd> Lists the files in the GridFS store. The characters specified after <code>list</code> (e.g. <code>&lt;prefix&gt;</code>) optionally limit the list of returned items to files that begin with that string of characters.</p>
<dt><code>search &lt;string&gt;</code></p>
<dd> Lists the files in the GridFS store with names that match any portion of <code>&lt;string&gt;</code>.</p>
<dt><code>put &lt;filename&gt;</code></p>
<dd> Copy the specified file from the local file system into GridFS storage. </p>
<p> Here, <code>&lt;filename&gt;</code> refers to the name the object will have in GridFS, and <code>mongofiles</code> assumes that this reflects the name the file has on the local file system. If the local filename is different use the <i>mongofiles &#8211;local</i> option.</p>
<dt><code>get &lt;filename&gt;</code></p>
<dd> Copy the specified file from GridFS storage to the local file system. </p>
<p> Here, <code>&lt;filename&gt;</code> refers to the name the object will have in GridFS, and <code>mongofiles</code> assumes that this reflects the name the file has on the local file system. If the local filename is different use the <i>mongofiles &#8211;local</i> option.</p>
<dt><code>delete &lt;filename&gt;</code></p>
<dd> Delete the specified file from GridFS storage.</dl>
<h2>EXAMPLES</h2>
<p> To return a list of all files in a <i>GridFS</i> collection in the <code>records</code> database, use the following invocation at the system shell: </p>
<pre>
mongofiles -d records list
</pre>
<p> This <code>mongofiles</code> instance will connect to the <code>mongod</code> instance running on the <code>27017</code> localhost interface to specify the same operation on a different port or hostname, and issue a command that resembles one of the following: </p>
<pre><code>
mongofiles-- port 37017 - d records list mongofiles-- hostname db1.example.net - d records list mongofiles-- hostname db1.example.net-- port 37017 - d records list
</code></pre>
<p> Modify any of the following commands as needed if you&#8217;re connecting the <code>mongod</code> instances on different ports or hosts. </p>
<p> To upload a file named <code>32-corinth.lp</code> to the GridFS collection in the <code>records</code> database, you can use the following command: </p>
<pre>
mongofiles -d records put 32-corinth.lp
</pre>
<p> To delete the <code>32-corinth.lp</code> file from this GridFS collection in the <code>records</code> database, you can use the following command: </p>
<pre>
mongofiles -d records delete 32-corinth.lp
</pre>
<p> To search for files in the GridFS collection in the <code>records</code> database that have the string <code>corinth</code> in their names, you can use following command: </p>
<pre>
mongofiles -d records search corinth
</pre>
<p> To list all files in the GridFS collection in the <code>records</code> database that begin with the string <code>32</code>, you can use the following command: </p>
<pre>
mongofiles -d records list 32
</pre>
<p> To fetch the file from the GridFS collection in the <code>records</code> database named <code>32-corinth.lp</code>, you can use the following command: </p>
<pre>
mongofiles -d records get 32-corinth.lp
</pre>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
