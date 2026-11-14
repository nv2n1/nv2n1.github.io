---
title: "mongoexport(1)"
name: "mongoexport"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongoexport/"
description: "mongoexport – MongoDB Export Utility"
---

<h2>NAME</h2>
<p> mongoexport &#8211; MongoDB Export Utility</p>
<h2>SYNOPSIS</h2>
<p> <code>mongoexport</code> is a utility that produces a JSON or CSV export of data stored in a MongoDB instance. See the <a rel="nofollow" href="http://docs.mongodb.org/manual/core/import-export">http://docs.mongodb.org/manual/core/import-export</a> document for a more in depth usage overview, and the <code>mongoimport</code> document for more information regarding the <code>mongoimport</code> utility, which provides the inverse &quot;importing&quot; capability.</p>
<h2>CONSIDERATIONS</h2>
<p> Do not use <code>mongoimport</code> and <code>mongoexport</code> for full-scale production backups because they may not reliably capture data type information. Use <code>mongodump</code> and <code>mongorestore</code> as described in <a rel="nofollow" href="http://docs.mongodb.org/manual/core/backups">http://docs.mongodb.org/manual/core/backups</a> for this kind of functionality.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongoexport</code></p>
<dd>
<dt><code>mongoexport</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongoexport</code> options and usage.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;quiet</code></p>
<dd> Runs <code>mongoexport</code> in a quiet mode that attempts to limit the amount of output. This option suppresses:</p>
<dt>&bull;</p>
<dd> output from <i>database commands</i></p>
<dt>&bull;</p>
<dd> replication activity</p>
<dt>&bull;</p>
<dd> connection accepted events</p>
<dt>&bull;</p>
<dd> connection closed events</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongoexport</code> release number.</p>
<dt><code>&#8211;host &lt;hostname&gt;&lt;:port&gt;, -h</code></p>
<dd> Specifies a resolvable hostname for the <code>mongod</code> to which to connect. By default <code>mongoexport</code> attempts to connect to a MongoDB instance running on the localhost on port number <code>27017</code>. </p>
<p> To connect to a replica set, specify the replica set seed name and the seed list of set members. Use the following format: </p>
<pre>
&lt;replica_set_name&gt;/&lt;hostname1&gt;&lt;:port&gt;,&lt;hostname2:&lt;port&gt;,...
</pre>
<p> You can always connect directly to a single MongoDB instance by specifying the host and port number directly.</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port number when the MongoDB instance is not running on the standard port of <code>27017</code>. You may also specify the port number using the <code>&#8211;host</code> option.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongoexport</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongoexport</code>, disable IPv6 support by default.</p>
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
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongoexport</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongoexport</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
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
<p> Directs <code>mongoexport</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;username &lt;username&gt;, -u</code></p>
<dd> Specifies a username with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;password</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;password &lt;password&gt;, -p</code></p>
<dd> Specifies a password with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;username</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;authenticationDatabase &lt;dbname&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the database that holds the user&#8217;s credentials. If you do not specify an authentication database, <code>mongoexport</code> assumes that the database specified as the argument to the <i>&#8211;db</i> option holds the user&#8217;s credentials.</p>
<dt><code>&#8211;authenticationMechanism &lt;name&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the authentication mechanism. By default, the authentication mechanism is <code>MONGODB-CR</code>, which is the MongoDB challenge/response authentication mechanism. In MongoDB Enterprise, <code>mongoexport</code> also includes support for <code>GSSAPI</code> to handle Kerberos authentication. See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication">http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication</a> for more information about Kerberos authentication.</p>
<dt><code>&#8211;dbpath &lt;path&gt;</code></p>
<dd> Specifies the directory of the MongoDB data files. If used, the <i>&#8211;dbpath</i> option enables <code>mongoexport</code> to attach directly to local data files without a running <code>mongod</code>. When run with <i>&#8211;dbpath</i>, <code>mongoexport</code> locks access to the data directory. No <code>mongod</code> can access the same path while the process runs.</p>
<dt><code>&#8211;directoryperdb</code></p>
<dd> When used in conjunction with the corresponding option in <code>mongod</code>, allows <code>mongoexport</code> to export data from MongoDB instances that have every database&#8217;s files saved in discrete directories on the disk. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;journal</code></p>
<dd> Allows <code>mongoexport</code> operations to use the durability <i>journal</i> to ensure data files remain valid and recoverable. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;db &lt;database&gt;, -d</code></p>
<dd> Specifies the name of the database on which to run <code>mongoexport</code>.</p>
<dt><code>&#8211;collection &lt;collection&gt;, -c</code></p>
<dd> Specifies the collection to export.</p>
<dt><code>&#8211;fields &lt;field1[,field2]&gt;, -f</code></p>
<dd> Specifies a field or fields to <i>include</i> in the export. Use a comma separated list of fields to specify multiple fields. </p>
<p> For <i>&#8211;csv</i> output formats, <code>mongoexport</code> includes only the specified field(s), and the specified field(s) can be a field within a sub-document. </p>
<p> For <i>JSON</i> output formats, <code>mongoexport</code> includes only the specified field(s) <code>and</code> the <code>_id</code> field, and if the specified field(s) is a field within a sub-document, the <code>mongoexport</code> includes the sub-document with all its fields, not just the specified field within the document.</p>
<dt><code>&#8211;fieldFile &lt;filename&gt;</code></p>
<dd> As an alternative to <i>&#8211;fields</i>, the <i>&#8211;fieldFile</i> option allows you to specify in a file the field or fields to <i>include</i> in the export and is <code>only valid</code> with the <i>&#8211;csv</i> option. The file must have only one field per line, and the line(s) must end with the LF character (<code>0x0A</code>). </p>
<p> <code>mongoexport</code> includes only the specified field(s). The specified field(s) can be a field within a sub-document.</p>
<dt><code>&#8211;query &lt;JSON&gt;, -q</code></p>
<dd> Provides a <i>JSON document</i> as a query that optionally limits the documents returned in the export. Specify JSON in <code>strict format</code>. </p>
<p> For example, given a collection named <code>records</code> in the database <code>test</code> with the following documents: </p>
<pre><code>
{"_id" : ObjectId("51f0188846a64a1ed98fde7c"), "a" : 1} {"_id" : ObjectId("520e61b0c6646578e3661b59"), "a" : 1, "b" : 2} {"_id" : ObjectId("520e642bb7fa4ea22d6b1871"), "a" : 2, "b" : 3, "c" : 5} {"_id" : ObjectId("520e6431b7fa4ea22d6b1872"), "a" : 3, "b" : 3, "c" : 6} {
    "_id" : ObjectId("520e6445b7fa4ea22d6b1873"), "a" : 5, "b" : 6, "c" : 8
}
</code></pre>
<p> The following <code>mongoexport</code> uses the <i>-q</i> option to export only the documents with the field <code>a</code> greater than or equal to (<code>$gte</code>) to <code>3</code>: </p>
<p>mongoexport &#8211; d test &#8211; c records &#8211; q &#8220;{ a: { \$gte: 3 } } }&#8221; &#8211;out exportdir / myRecords.json</p>
<p> The resulting file contains the following documents: </p>
<p>{&#8220;_id&#8221; : {&#8220;$oid&#8221; : &#8220;520e6431b7fa4ea22d6b1872&#8221;}, &#8220;a&#8221; : 3, &#8220;b&#8221; : 3, &#8220;c&#8221; : 6} {<br />
    &#8220;_id&#8221; : {&#8220;$oid&#8221; : &#8220;520e6445b7fa4ea22d6b1873&#8221;}, &#8220;a&#8221; : 5, &#8220;b&#8221; : 6, &#8220;c&#8221; : 8<br />
}</p>
<p> You can sort the results with the <i>&#8211;sort</i> option to <code>mongoexport</code>.</p>
<dt><code>&#8211;csv</code></p>
<dd> Changes the export format to a comma-separated-values (CSV) format. By default <code>mongoexport</code> writes data using one <i>JSON</i> document for every MongoDB document. </p>
<p> If you specify <i>&#8211;csv</i>, then you must also use either the <i>&#8211;fields</i> or the <i>&#8211;fieldFile</i> option to declare the fields to export from the collection.</p>
<dt><code>&#8211;out &lt;file&gt;, -o</code></p>
<dd> Specifies a file to write the export to. If you do not specify a file name, the <code>mongoexport</code> writes data to standard output (e.g. <code>stdout</code>).</p>
<dt><code>&#8211;jsonArray</code></p>
<dd> Modifies the output of <code>mongoexport</code> to write the entire contents of the export as a single <i>JSON</i> array. By default <code>mongoexport</code> writes data using one JSON document for every MongoDB document.</p>
<dt><code>&#8211;slaveOk, -k</code></p>
<dd> Allows <code>mongoexport</code> to read data from secondary or slave nodes when using <code>mongoexport</code> with a replica set. This option is only available if connected to a <code>mongod</code> or <code>mongos</code> and is not available when used with the &quot;<i>mongoexport &#8211;dbpath</i>&quot; option. </p>
<p> This is the default behavior.</p>
<dt><code>&#8211;forceTableScan</code></p>
<dd> New in version 2.2. </p>
<p> Forces <code>mongoexport</code> to scan the data store directly: typically, <code>mongoexport</code> saves entries as they appear in the index of the <code>_id</code> field. Use <i>&#8211;forceTableScan</i> to skip the index and scan the data directly. Typically there are two cases where this behavior is preferable to the default:</p>
<dt>1.</p>
<dd> If you have key sizes over 800 bytes that would not be present in the <code>_id</code> index.</p>
<dt>2.</p>
<dd> Your database uses a custom <code>_id</code> field. </p>
<p> When you run with <i>&#8211;forceTableScan</i>, <code>mongoexport</code> does not use <code>$snapshot</code>. As a result, the export produced by <code>mongoexport</code> can reflect the state of the database at many different points in time. </p>
<p> <code>WARNING:</code> Use <i>&#8211;forceTableScan</i> with extreme caution and consideration.</p>
<dt><code>&#8211;skip &lt;number&gt;</code></p>
<dd> Use <i>&#8211;skip</i> to control where <code>mongoexport</code> begins exporting documents. See <code>skip()</code> for information about the underlying operation.</p>
<dt><code>&#8211;limit &lt;number&gt;</code></p>
<dd> Specifies a maximum number of documents to include in the export. See <code>limit()</code> for information about the underlying operation.</p>
<dt><code>&#8211;sort &lt;JSON&gt;</code></p>
<dd> Specifies an ordering for exported results. If an index does <code>not</code> exist that can support the sort operation, the results must be <i>less than</i> 32 megabytes. </p>
<p> Use <i>&#8211;sort</i> conjunction with <i>&#8211;skip</i> and <i>&#8211;limit</i> to limit number of exported documents. </p>
<p>mongoexport &#8211; d test &#8211; c records&#8211; sort &#8216;{a: 1}&#8217; &#8211;limit 100 &#8211;out export .0.json mongoexport &#8211; d test &#8211; c records&#8211; sort &#8216;{a: 1}&#8217; &#8211;limit 100 &#8211;skip 100 &#8211;out export .1.json mongoexport &#8211; d test &#8211; c records&#8211; sort &#8216;{a: 1}&#8217; &#8211;limit 100 &#8211;skip 200 &#8211;out export .2.json</p>
<p> See <code>sort()</code> for information about the underlying operation.</dl>
<h2>USE</h2>
<h3>Export in CSV Format</h3>
<p> In the following example, <code>mongoexport</code> exports the collection <code>contacts</code> from the <code>users</code> database from the <code>mongod</code> instance running on the localhost port number <code>27017</code>. This command writes the export data in <i>CSV</i> format into a file located at <code>/opt/backups/contacts.csv</code>. The <code>fields.txt</code> file contains a line-separated list of fields to export. </p>
<p>mongoexport&#8211; db users&#8211; collection contacts&#8211; csv&#8211; fieldFile fields.txt&#8211; out / opt / backups / contacts.csv</p>
<h3>Export in JSON Format</h3>
<p> The next example creates an export of the collection <code>contacts</code> from the MongoDB instance running on the localhost port number <code>27017</code>, with journaling explicitly enabled. This writes the export to the <code>contacts.json</code> file in <i>JSON</i> format. </p>
<p>mongoexport&#8211; db sales&#8211; collection contacts&#8211; out contacts.json&#8211; journal</p>
<h3>Export Collection Directly From Data Files</h3>
<p> The following example exports the collection <code>contacts</code> from the <code>sales</code> database located in the MongoDB data files located at <code>/srv/mongodb/</code>. This operation writes the export to standard output in <i>JSON</i> format. </p>
<pre>
mongoexport --db sales --collection contacts --dbpath /srv/mongodb/
</pre>
<p> <code>WARNING:</code> The above example will only succeed if there is no <code>mongod</code> connected to the data files located in the <code>/srv/mongodb/</code> directory.</p>
<h3>Export from Remote Host Running with Authentication</h3>
<p> The following example exports the collection <code>contacts</code> from the database <code>marketing</code> . This data resides on the MongoDB instance located on the host <code>mongodb1.example.net</code> running on port <code>37017</code>, which requires the username <code>user</code> and the password <code>pass</code>. </p>
<p>mongoexport&#8211; host mongodb1.example.net&#8211; port 37017 &#8211;username user&#8211; password pass&#8211; collection contacts&#8211; db marketing&#8211; out mdb1 &#8211; examplenet.json</p>
<h2>TYPE FIDELITY</h2>
<p> <code>WARNING:</code> <code>mongoimport</code> and <code>mongoexport</code> do not reliably preserve all rich <i>BSON</i> data types because <i>JSON</i> can only represent a subset of the types supported by BSON. As a result, data exported or imported with these tools may lose some measure of fidelity. See <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/mongodb-extended-json">http://docs.mongodb.org/manual/reference/mongodb-extended-json</a> for more information. </p>
<p> JSON can only represent a subset of the types supported by BSON. To preserve type information, <code>mongoexport</code> uses the <code>strict mode representation</code> for certain types. </p>
<p> For example, the following insert operation in the <code>mongo</code> shell uses the <code>mongoShell mode representation</code> for the BSON types <code>data_date</code> and <code>data_numberlong</code>: </p>
<pre>
use test
db.traffic.insert( { _id: 1, volume: NumberLong(2980000), date: new Date() } )
</pre>
<p> Use <code>mongoexport</code> to export the data: </p>
<pre>
mongoexport --db test --collection traffic --out traffic.json
</pre>
<p> The exported data is in <code>strict mode representation</code> to preserve type information: </p>
<pre><code>
{
    "_id" : 1, "volume" : {"$numberLong" : "2980000"}, "date":
    {
        "$date" : "2014-03-13T13:47:42.483-0400"
    }
}
</code></pre>
<p> See <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/mongodb-extended-json">http://docs.mongodb.org/manual/reference/mongodb-extended-json</a> for a complete list of these types and the representations used.</p>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
