---
title: "mongoimport(1)"
name: "mongoimport"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongoimport/"
description: "mongoimport – MongoDB Import Utility"
---

<h2>NAME</h2>
<p> mongoimport &#8211; MongoDB Import Utility</p>
<h2>SYNOPSIS</h2>
<p> The <code>mongoimport</code> tool provides a route to import content from a JSON, CSV, or TSV export created by <code>mongoexport</code>, or potentially, another third-party export tool. See the <a rel="nofollow" href="http://docs.mongodb.org/manual/core/import-export">http://docs.mongodb.org/manual/core/import-export</a> document for a more in depth usage overview, and the <code>mongoexport</code> document for more information regarding <code>mongoexport</code>, which provides the inverse &quot;exporting&quot; capability.</p>
<h2>CONSIDERATIONS</h2>
<p> Do not use <code>mongoimport</code> and <code>mongoexport</code> for full instance, production backups because they will not reliably capture data type information. Use <code>mongodump</code> and <code>mongorestore</code> as described in <a rel="nofollow" href="http://docs.mongodb.org/manual/core/backups">http://docs.mongodb.org/manual/core/backups</a> for this kind of functionality.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongoimport</code></p>
<dd>
<dt><code>mongoimport</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongoimport</code> options and usage.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;quiet</code></p>
<dd> Runs <code>mongoimport</code> in a quiet mode that attempts to limit the amount of output. This option suppresses:</p>
<dt>&bull;</p>
<dd> output from <i>database commands</i></p>
<dt>&bull;</p>
<dd> replication activity</p>
<dt>&bull;</p>
<dd> connection accepted events</p>
<dt>&bull;</p>
<dd> connection closed events</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongoimport</code> release number.</p>
<dt><code>&#8211;host &lt;hostname&gt;&lt;:port&gt;, -h</code></p>
<dd> Specifies a resolvable hostname for the <code>mongod</code> to which to connect. By default <code>mongoimport</code> attempts to connect to a MongoDB instance running on the localhost on port number <code>27017</code>. </p>
<p> To connect to a replica set, specify the replica set seed name and the seed list of set members. Use the following format: </p>
<pre>
&lt;replica_set_name&gt;/&lt;hostname1&gt;&lt;:port&gt;,&lt;hostname2:&lt;port&gt;,...
</pre>
<p> You can always connect directly to a single MongoDB instance by specifying the host and port number directly.</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port number when the MongoDB instance is not running on the standard port of <code>27017</code>. You may also specify the port number using the <code>&#8211;host</code> option.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongoimport</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongoimport</code>, disable IPv6 support by default.</p>
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
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongoimport</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongoimport</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
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
<p> Directs <code>mongoimport</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;username &lt;username&gt;, -u</code></p>
<dd> Specifies a username with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;password</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;password &lt;password&gt;, -p</code></p>
<dd> Specifies a password with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;username</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;authenticationDatabase &lt;dbname&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the database that holds the user&#8217;s credentials. If you do not specify an authentication database, <code>mongoimport</code> assumes that the database specified as the argument to the <i>&#8211;db</i> option holds the user&#8217;s credentials.</p>
<dt><code>&#8211;authenticationMechanism &lt;name&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the authentication mechanism. By default, the authentication mechanism is <code>MONGODB-CR</code>, which is the MongoDB challenge/response authentication mechanism. In MongoDB Enterprise, <code>mongoimport</code> also includes support for <code>GSSAPI</code> to handle Kerberos authentication. See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication">http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication</a> for more information about Kerberos authentication.</p>
<dt><code>&#8211;dbpath &lt;path&gt;</code></p>
<dd> Specifies the directory of the MongoDB data files. If used, the <i>&#8211;dbpath</i> option enables <code>mongoimport</code> to attach directly to local data files without a running <code>mongod</code>. When run with <i>&#8211;dbpath</i>, <code>mongoimport</code> locks access to the data directory. No <code>mongod</code> can access the same path while the process runs.</p>
<dt><code>&#8211;directoryperdb</code></p>
<dd> When used in conjunction with the corresponding option in <code>mongod</code>, allows <code>mongoimport</code> to access data from MongoDB instances that use an on-disk format where every database has a distinct directory. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;journal</code></p>
<dd> Allows <code>mongoimport</code> operations to use the durability <i>journal</i> to ensure data files remain valid and recoverable. This option is only relevant when specifying the <i>&#8211;dbpath</i> option.</p>
<dt><code>&#8211;db &lt;database&gt;, -d</code></p>
<dd> Specifies the name of the database on which to run <code>mongoimport</code>.</p>
<dt><code>&#8211;collection &lt;collection&gt;, -c</code></p>
<dd> Specifies the collection to import. </p>
<p> New in version 2.6: If you do not specify <i>&#8211;collection</i>, <code>mongoimport</code> takes the collection name from the input filename. MongoDB omits the extension of the file from the collection name, if the input file has an extension. </p>
<dt><code>&#8211;fields &lt;field1[,field2]&gt;, -f</code></p>
<dd> Specify a comma separated list of field names when importing <i>csv</i> or <i>tsv</i> files that do not have field names in the first (i.e. header) line of the file.</p>
<dt><code>&#8211;fieldFile &lt;filename&gt;</code></p>
<dd> As an alternative to <i>&#8211;fields</i>, the <i>&#8211;fieldFile</i> option allows you to specify a file that holds a list of field names if your <i>csv</i> or <i>tsv</i> file does not include field names in the first line of the file (i.e. header). Place one field per line.</p>
<dt><code>&#8211;ignoreBlanks</code></p>
<dd> Ignores empty fields in <i>csv</i> and <i>tsv</i> exports. If not specified, <code>mongoimport</code> creates fields without values in imported documents.</p>
<dt><code>&#8211;type &lt;json|csv|tsv&gt;</code></p>
<dd> Specifies the file type to import. The default format is <i>JSON</i>, but it&#8217;s possible to import <i>csv</i> and <i>tsv</i> files.</p>
<dt><code>&#8211;file &lt;filename&gt;</code></p>
<dd> Specifies the location and name of a file containing the data to import. If you do not specify a file, <code>mongoimport</code> reads data from standard input (e.g. &quot;stdin&quot;).</p>
<dt><code>&#8211;drop</code></p>
<dd> Modifies the import process so that the target instance drops every collection before importing the collection from the input.</p>
<dt><code>&#8211;headerline</code></p>
<dd> If using <i>&#8211;type csv</i> or <i>&#8211;type tsv</i>, uses the first line as field names. Otherwise, <code>mongoimport</code> will import the first line as a distinct document.</p>
<dt><code>&#8211;upsert</code></p>
<dd> Modifies the import process to update existing objects in the database if they match an imported object, while inserting all other objects. </p>
<p> If you do not specify a field or fields using the <i>&#8211;upsertFields</i> <code>mongoimport</code> will upsert on the basis of the <code>_id</code> field.</p>
<dt><code>&#8211;upsertFields &lt;field1[,field2]&gt;</code></p>
<dd> Specifies a list of fields for the query portion of the <i>upsert</i>. Use this option if the <code>_id</code> fields in the existing documents don&#8217;t match the field in the document, but another field or field combination can uniquely identify documents as a basis for performing upsert operations. </p>
<p> To ensure adequate performance, indexes should exist for this field or fields.</p>
<dt><code>&#8211;stopOnError</code></p>
<dd> New in version 2.2. </p>
<p> Forces <code>mongoimport</code> to halt the import operation at the first error rather than continuing the operation despite errors.</p>
<dt><code>&#8211;jsonArray</code></p>
<dd> Accepts the import of data expressed with multiple MongoDB documents within a single <i>JSON</i> array. </p>
<p> Used in conjunction with <i>mongoexport &#8211;jsonArray</i> to import data written as a single <i>JSON</i> array. Limited to imports of 16 MB or smaller.</dl>
<h2>USE</h2>
<p> In this example, <code>mongoimport</code> imports the <i>csv</i> formatted data in the <code>/opt/backups/contacts.csv</code> into the collection <code>contacts</code> in the <code>users</code> database on the MongoDB instance running on the localhost port numbered <code>27017</code>. </p>
<pre><code>
mongoimport-- db users-- collection contacts-- type csv-- file / opt / backups / contacts.csv
</code></pre>
<p> Since <code>mongoimport</code> uses the input file name (minus the extension) as the collection name if <code>-c</code> or <code>&#8211;collection</code> is unspecified, the following example is equivalent to the previous example: </p>
<pre>
mongoimport --db users --type csv --file /opt/backups/contacts.csv
</pre>
<p> In the following example, <code>mongoimport</code> imports the data in the <i>JSON</i> formatted file <code>contacts.json</code> into the collection <code>contacts</code> on the MongoDB instance running on the localhost port number 27017. </p>
<pre>
mongoimport --collection contacts --file contacts.json
</pre>
<p> In the next example, <code>mongoimport</code> takes data passed to it on standard input (i.e. with a <code>|</code> pipe.) and imports it into the MongoDB datafiles located at <code>/srv/mongodb/</code>. if the import process encounters an error, the <code>mongoimport</code> will halt because of the <i>&#8211;stopOnError</i> option. </p>
<p>mongoimport&#8211; db sales&#8211; collection contacts&#8211; stopOnError&#8211; dbpath / srv / mongodb /</p>
<p> In the final example, <code>mongoimport</code> imports data from the file <code>/opt/backups/mdb1-examplenet.json</code> into the collection <code>contacts</code> within the database <code>marketing</code> on a remote MongoDB database. This <code>mongoimport</code> accesses the <code>mongod</code> instance running on the host <code>mongodb1.example.net</code> over port <code>37017</code>, which requires the username <code>user</code> and the password <code>pass</code>. </p>
<p>mongoimport&#8211; host mongodb1.example.net&#8211; port 37017 &#8211;username user&#8211; password pass&#8211; collection contacts&#8211; db marketing&#8211; file / opt / backups / mdb1 &#8211; examplenet.json</p>
<h2>TYPE FIDELITY</h2>
<p> <code>WARNING:</code> <code>mongoimport</code> and <code>mongoexport</code> do not reliably preserve all rich <i>BSON</i> data types because <i>JSON</i> can only represent a subset of the types supported by BSON. As a result, data exported or imported with these tools may lose some measure of fidelity. See <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/mongodb-extended-json">http://docs.mongodb.org/manual/reference/mongodb-extended-json</a> for more information. </p>
<p> JSON can only represent a subset of the types supported by BSON. To preserve type information, <code>mongoimport</code> accepts <code>strict mode representation</code> for certain types. </p>
<p> For example, to preserve type information for BSON types <code>data_date</code> and <code>data_numberlong</code> during <code>mongoimport</code>, the data should be in strict mode representation, as in the following: </p>
<pre><code>
{
    "_id" : 1, "volume" : {"$numberLong" : "2980000"}, "date":
    {
        "$date" : "2014-03-13T13:47:42.483-0400"
    }
}
</code></pre>
<p> For the <code>data_numberlong</code> type, <code>mongoimport</code> converts into a float during the import. </p>
<p> See <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/mongodb-extended-json">http://docs.mongodb.org/manual/reference/mongodb-extended-json</a> for a complete list of these types and the representations used.</p>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
