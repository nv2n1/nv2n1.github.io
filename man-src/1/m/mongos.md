---
title: "mongos(1)"
name: "mongos"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongos/"
description: "mongos – MongoDB Sharded Cluster Query Router"
---

<h2>NAME</h2>
<p> mongos &#8211; MongoDB Sharded Cluster Query Router</p>
<h2>SYNOPSIS</h2>
<p> <code>mongos</code> for &quot;MongoDB Shard,&quot; is a routing service for MongoDB shard configurations that processes queries from the application layer, and determines the location of this data in the <i>sharded cluster</i>, in order to complete these operations. From the perspective of the application, a <code>mongos</code> instance behaves identically to any other MongoDB instance.</p>
<h2>OPTIONS</h2>
<h3>Core Options</h3>
<dl>
<dt><code>mongos</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongos</code> options and usage.</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongos</code> release number.</p>
<dt><code>&#8211;config &lt;filename&gt;, -f</code></p>
<dd> Specifies a configuration file for runtime configuration options. The configuration file is the preferred method for runtime configuration of <code>mongos</code>. The options are equivalent to the command-line configuration options. See <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/configuration-options">http://docs.mongodb.org/manual/reference/configuration-options</a> for more information. </p>
<p> Ensure the configuration file uses ASCII encoding. <code>mongos</code> does not support configuration files with non-ASCII encoding, including UTF-8.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;quiet</code></p>
<dd> Runs <code>mongos</code> in a quiet mode that attempts to limit the amount of output. This option suppresses:</p>
<dt>&bull;</p>
<dd> output from <i>database commands</i></p>
<dt>&bull;</p>
<dd> replication activity</p>
<dt>&bull;</p>
<dd> connection accepted events</p>
<dt>&bull;</p>
<dd> connection closed events</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port number when the MongoDB instance is not running on the standard port of <code>27017</code>. You may also specify the port number using the <code>&#8211;host</code> option.</p>
<dt><code>&#8211;bind_ip &lt;ip address&gt;</code></p>
<dd> Specifies the IP address that the <code>mongos</code> process binds to and listens for connections on. By default <code>mongos</code> listens for connections for all interfaces. You may attach <code>mongos</code> to any interface. When attaching <code>mongos</code> to a publicly accessible interface, ensure that you have implemented proper authentication and firewall restrictions to protect the integrity of your database.</p>
<dt><code>&#8211;maxConns &lt;number&gt;</code></p>
<dd> Specifies the maximum number of simultaneous connections that <code>mongos</code> will accept. This setting will have no effect if the value of this setting is higher than your operating system&#8217;s configured maximum connection tracking threshold. </p>
<p> This setting is particularly useful for <code>mongos</code> if you have a client that creates a number of collections but allows them to timeout rather than close the collections. When you set <code>maxConns</code>, ensure the value is slightly higher than the size of the connection pool or the total number of connections to prevent erroneous connection spikes from propagating to the members of a <i>sharded cluster</i>. </p>
<p> Changed in version 2.6: MongoDB removed the upward limit on the <code>maxConns</code> setting. </p>
<dt><code>&#8211;syslog</code></p>
<dd> Sends all logging output to the host&#8217;s <i>syslog</i> system rather than to standard output or a log file as with <i>&#8211;logpath</i>. </p>
<p> <i>&#8211;syslog</i> is not supported on Windows.</p>
<dt><code>&#8211;syslogFacility &lt;string&gt;</code></p>
<dd> Specifies the facility level used when logging messages to syslog. The default is <code>user</code>. The value you specify must be supported by your operating system&#8217;s implementation of syslog. To use this option, you must enable the <i>&#8211;syslog</i> option.</p>
<dt><code>&#8211;logpath &lt;path&gt;</code></p>
<dd> Specifies the path for the log file that holds all diagnostic logging information. </p>
<p> Unless specified, <code>mongos</code> will output all log information to the standard output. Additionally, unless you also specify <i>&#8211;logappend</i>, the logfile will be overwritten when the process restarts. </p>
<p> <code>NOTE:</code> The behavior of the logging system may change in the near future in response to the <i>SERVER-4499</i> case.</p>
<dt><code>&#8211;logappend</code></p>
<dd> Appends new entries to the end of the logfile when the <code>mongos</code> restarts instead of overwriting the content of the log.</p>
<dt><code>&#8211;timeStampFormat &lt;string&gt;</code></p>
<dd> Specifies the time format for timestamps in log messages. Specify one of the following values: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ctime</code> </td>
<td> Displays timestamps as <code>Wed Dec 31 18:17:54.811</code>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>iso8601-utc</code> </td>
<td> Displays timestamps in Coordinated Universal Time (UTC) in the ISO-8601 format. For example, for New York at the start of the Epoch: <code>1970-01-01T00:00:00.000Z</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>iso8601-local</code> </td>
<td> Default value. Displays timestamps in local time in the ISO-8601 format. For example, for New York at the start of the Epoch: <code>1969-12-31T19:00:00.000+0500</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>&#8211;pidfilepath &lt;path&gt;</code></p>
<dd> Specifies a file location to hold the &quot;<i>PID</i>&quot; or process ID of the <code>mongos</code> process. Useful for tracking the <code>mongos</code> process in combination with the <i>&#8211;fork</i> option. </p>
<p> Without a specified <i>&#8211;pidfilepath</i> option, <code>mongos</code> creates no PID file.</p>
<dt><code>&#8211;keyFile &lt;file&gt;</code></p>
<dd> Specifies the path to a key file to store authentication information. This option is used for interprocess authentication among the <code>mongos</code> and <code>mongod</code> instances of a <i>sharded cluster</i> or <i>replica set</i>.</p>
<dt><code>&#8211;setParameter &lt;options&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies an option to configure on startup. Specify multiple options with multiple <i>&#8211;setParameter</i> options. See <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/parameters">http://docs.mongodb.org/manual/reference/parameters</a> for full documentation of these parameters. The <code>setParameter</code> database command provides access to many of these parameters. <i>&#8211;setParameter</i> supports the following options:</p>
<dt>&bull;</p>
<dd> <code>enableLocalhostAuthBypass</code></p>
<dt>&bull;</p>
<dd> <code>enableTestCommands</code></p>
<dt>&bull;</p>
<dd> <code>logLevel</code></p>
<dt>&bull;</p>
<dd> <code>logUserIds</code></p>
<dt>&bull;</p>
<dd> <code>notablescan</code></p>
<dt>&bull;</p>
<dd> <code>quiet</code></p>
<dt>&bull;</p>
<dd> <code>supportCompatibilityFormPrivilegeDocuments</code></p>
<dt>&bull;</p>
<dd> <code>syncdelay</code></p>
<dt>&bull;</p>
<dd> <code>textSearchEnabled</code></p>
<dt>&bull;</p>
<dd> <code>userCacheInvalidationIntervalSecs</code></p>
<dt><code>&#8211;httpinterface</code></p>
<dd> New in version 2.6. </p>
<p> Enables the HTTP interface. Enabling the interface can increase network exposure. </p>
<p> Leave the HTTP interface <i>disabled</i> for production deployments. If you <i>do</i> enable this interface, you should only allow trusted clients to access this port. See <i>security-firewalls</i>. </p>
<p> <code>NOTE:</code> In MongoDB Enterprise, the HTTP Console does not support Kerberos Authentication.</p>
<dt><code>&#8211;clusterAuthMode &lt;option&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Enables <i>internal x.509 authentication</i> for membership to the cluster or replica set. The <i>&#8211;clusterAuthMode</i> option can have one of the following values: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>keyFile</code> </td>
<td> Default value. Use keyfile for authentication.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sendKeyFile</code> </td>
<td> For rolling upgrade purposes. Send the keyfile for authentication but can accept either keyfile or x.509 certificate.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sendX509</code> </td>
<td> For rolling upgrade purposes. Send the x.509 certificate for authentication but can accept either keyfile or x.509 certificate.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x509</code> </td>
<td> Recommended. Send the x.509 certificate for authentication and accept <code>only</code> x.509 certificate.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;nounixsocket</code></p>
<dd> Disables listening on the UNIX socket. <code>mongos</code> always listens on the UNIX socket, unless either: <i>&#8211;nounixsocket</i> is set, <code>bind_ip</code> is not set, or <code>bind_ip</code> does not specify <code>127.0.0.1</code>. </p>
<p> New in version 2.6: <code>mongos</code> installed from official <code>.deb</code> and <code>.rpm</code> packages have the <code>bind_ip</code> configuration set to <code>127.0.0.1</code> by default. </p>
<dt><code>&#8211;unixSocketPrefix &lt;path&gt;</code></p>
<dd> Specifies a path for the UNIX socket. If this option has no value, <code>mongos</code> creates a socket with <code>/tmp</code> as a prefix. </p>
<p> MongoDB will always create and listen on a UNIX socket, unless <i>&#8211;nounixsocket</i> is set, <code>bind_ip</code> is not set, or <code>bind_ip</code> does not specify <code>127.0.0.1</code>.</p>
<dt><code>&#8211;fork</code></p>
<dd> Enables a <i>daemon</i> mode for <code>mongos</code> that runs the process in the background. This is the normal mode of operation in production and production-like environments but may not be desirable for testing.</dl>
<h3>Sharded Cluster Options</h3>
<dl>
<dt><code>&#8211;configdb &lt;config1&gt;,&lt;config2&gt;,&lt;config3&gt;</code></p>
<dd> Specifies the <i>configuration database</i> for the <i>sharded cluster</i>. You must specify either 1 or 3 configuration servers, in a comma separated list. </p>
<p> All <code>mongos</code> instances <code>must</code> specify the hosts in the <i>&#8211;configdb</i> setting in the in the same order. </p>
<p> If your configuration databases reside in more that one data center, order the hosts so that the config database that is closest to the majority of your <code>mongos</code> instances is first servers in the list. </p>
<p> <code>WARNING:</code> Never remove a config server from this setting, even if the config server is not available or offline.</p>
<dt><code>&#8211;localThreshold</code></p>
<dd> Affects the logic that <code>mongos</code> uses when selecting <i>replica set</i> members to pass read operations to from clients. Specify a value in milliseconds. The default value is <code>15</code>, which corresponds to the default value in all of the client <code>drivers</code>. </p>
<p> When <code>mongos</code> receives a request that permits reads to <i>secondary</i> members, the <code>mongos</code> will:</p>
<dt>&bull;</p>
<dd> Find the member of the set with the lowest ping time.</p>
<dt>&bull;</p>
<dd> Construct a list of replica set members that is within a ping time of 15 milliseconds of the nearest suitable member of the set. </p>
<p> If you specify a value for <i>&#8211;localThreshold</i>, <code>mongos</code> will construct the list of replica members that are within the latency allowed by this value.</p>
<dt>&bull;</p>
<dd> Select a member to read from at random from this list. </p>
<p> The ping time used for a member compared by the <i>&#8211;localThreshold</i> setting is a moving average of recent ping times, calculated at most every 10 seconds. As a result, some queries may reach members above the threshold until the <code>mongos</code> recalculates the average. </p>
<p> See the <i>replica-set-read-preference-behavior-member-selection</i> section of the <code>read preference</code> documentation for more information.</p>
<dt><code>&#8211;upgrade</code></p>
<dd> Updates the meta data format used by the <i>config database</i>.</p>
<dt><code>&#8211;chunkSize &lt;value&gt;</code></p>
<dd> Determines the size in megabytes of each <i>chunk</i> in the <i>sharded cluster</i>. The default value is 64 megabytes, which is the ideal size for chunks in most deployments: larger chunk size can lead to uneven data distribution; smaller chunk size can lead to inefficient movement of chunks between nodes. However, in some circumstances it may be necessary to set a different chunk size. </p>
<p> This option <i>only</i> affects chunk size when you initialize the cluster for the first time. If you later modify the option, the new value has no effect. See the <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/modify-chunk-size-in-sharded-cluster">http://docs.mongodb.org/manual/tutorial/modify-chunk-size-in-sharded-cluster</a> procedure if you need to change the chunk size on an existing sharded cluster.</p>
<dt><code>&#8211;noAutoSplit</code></p>
<dd> Prevents <code>mongos</code> from automatically inserting metadata splits in a <i>sharded collection</i>. If set on all <code>mongos</code> instances, this prevents MongoDB from creating new chunks as the data in a collection grows. </p>
<p> Because any <code>mongos</code> in a cluster can create a split, to totally disable splitting in a cluster you must set <i>&#8211;noAutoSplit</i> on all <code>mongos</code>. </p>
<p> <code>WARNING:</code> With <i>&#8211;noAutoSplit</i> enabled, the data in your sharded cluster may become imbalanced over time. Enable with caution.</dl>
<h3>SSL Options</h3>
<h3>See</h3>
<p> <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl">http://docs.mongodb.org/manual/tutorial/configure-ssl</a> for full documentation of MongoDB&#8217;s support.</p>
<dl>
<dt><code>&#8211;sslOnNormalPorts</code></p>
<dd> Deprecated since version 2.6. </p>
<p> New in version 2.2. </p>
<p> Enables SSL so that <code>mongos</code> requires SSL encryption for all connections on the default MongoDB port or port specified by <i>&#8211;port</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslMode &lt;mode&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Enables SSL or mixed SSL on a port. The argument to the <i>&#8211;sslMode</i> option can be one of the following: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>disabled</code> </td>
<td> The server does not use SSL.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>allowSSL</code> </td>
<td> Connections between servers do not use SSL. For incoming connections, the server accepts both SSL and non-SSL.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>preferSSL</code> </td>
<td> Connections between servers use SSL. For incoming connections, the server accepts both SSL and non-SSL.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>requireSSL</code> </td>
<td> The server uses and accepts only SSL encrypted connections.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslPEMKeyFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains both the SSL certificate and key. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> This option is required when using the <i>&#8211;ssl</i> option to connect to a <code>mongod</code> or <code>mongos</code> that has <code>sslCAFile</code> enabled <i>without</i> <code>sslWeakCertificateValidation</code>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslPEMKeyPassword &lt;value&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongos</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongos</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslClusterFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the x.509 certificate-key file for <i>membership authentication</i> for the cluster or replica set. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslClusterPassword &lt;value&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the password to de-crypt the x.509 certificate-key file specified with <i>&#8211;sslClusterFile</i>. Use <i>&#8211;sslClusterPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongos</code> will redact the password from all logging and reporting output. </p>
<p> Changed in version 2.6: If the x.509 key file is encrypted and you do not specify <i>&#8211;sslClusterPassword</i>, <code>mongos</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslCAFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the root certificate chain from the Certificate Authority. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslCRLFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the Certificate Revocation List. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslWeakCertificateValidation</code></p>
<dd> New in version 2.4. </p>
<p> Disables the requirement for SSL certificate validation that <i>&#8211;sslCAFile</i> enables. With <i>&#8211;sslWeakCertificateValidation</i>, <code>mongos</code> will accept connections when the client does not present a certificate when establishing the connection. </p>
<p> If the client presents a certificate and <code>mongos</code> has <i>&#8211;sslWeakCertificateValidation</i> enabled, <code>mongos</code> will validate the certificate using the root certificate chain specified by <i>&#8211;sslCAFile</i> and reject clients with invalid certificates. </p>
<p> Use <i>&#8211;sslWeakCertificateValidation</i> if you have a mixed deployment that includes clients that do not or cannot present certificates to <code>mongos</code>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslAllowInvalidCertificates</code></p>
<dd> New in version 2.6. </p>
<p> Bypasses the validation checks for server certificates and allows the use of invalid certificates. When using the <code>sslAllowInvalidCertificates</code> setting, MongoDB logs as a warning the use of the invalid certificate. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslFIPSMode</code></p>
<dd> New in version 2.6. </p>
<p> Directs <code>mongos</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></dl>
<h3>Audit Options</h3>
<dl>
<dt><code>&#8211;auditDestination</code></p>
<dd> Enables auditing. The <i>&#8211;auditDestination</i> option can have one of the following values: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>syslog</code> </td>
<td> Output the audit events to syslog in JSON format. Not available on Windows. Audit messages have a syslog severity level of <code>info</code> and a facility level of <code>user</code>. </p>
<p> The syslog message limit can result in the truncation of the audit messages. The auditing system will neither detect the truncation nor error upon its occurrence.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>console</code> </td>
<td> Output the audit events to <code>stdout</code> in JSON format.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>file</code> </td>
<td> Output the audit events to the file specified in <i>&#8211;auditPath</i> in the format specified in <i>&#8211;auditFormat</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> <code>NOTE:</code> The <code>audit system</code> is available only in <i>MongoDB Enterprise</i>.</p>
<dt><code>&#8211;auditFormat</code></p>
<dd> Specifies the format of the output file if <i>&#8211;auditDestination</i> is <code>file</code>. The <i>&#8211;auditFormat</i> can have one of the following values: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>JSON</code> </td>
<td> Output the audit events in JSON format to the file specified in <i>&#8211;auditPath</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BSON</code> </td>
<td> Output the audit events in BSON binary format to the file specified in <i>&#8211;auditPath</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Printing audit events to a file in JSON format degrades server performance more than printing to a file in BSON format. </p>
<p> <code>NOTE:</code> The <code>audit system</code> is available only in <i>MongoDB Enterprise</i>.</p>
<dt><code>&#8211;auditPath</code></p>
<dd> Specifies the output file for auditing if <i>&#8211;auditDestination</i> has value of <code>file</code>. The <i>&#8211;auditPath</i> option can take either a full path name or a relative path name. </p>
<p> <code>NOTE:</code> The <code>audit system</code> is available only in <i>MongoDB Enterprise</i>.</p>
<dt><code>&#8211;auditFilter</code></p>
<dd> Specifies the filter to limit the <i>types of operations</i> the audit system records. The option takes a document of the form: </p>
<pre>
{ atype: &lt;expression&gt; }
</pre>
<p> For authentication operations, the option can also take a document of the form: </p>
<pre>
{ atype: &lt;expression&gt;, &quot;param.db&quot;: &lt;database&gt; }
</pre>
<p> <code>NOTE:</code> The <code>audit system</code> is available only in <i>MongoDB Enterprise</i>.</dl>
<h3>Additional Options</h3>
<dl>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongos</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongos</code>, disable IPv6 support by default.</p>
<dt><code>&#8211;jsonp</code></p>
<dd> Permits <i>JSONP</i> access via an HTTP interface. Consider the security implications of allowing this activity before enabling this option. If the HTTP interface is disabled, the <i>&#8211;jsonp</i> also enables the HTTP interface. </p>
<p> <code>SEE ALSO:</code> <i>&#8211;httpinterface</i></p>
<dt><code>&#8211;noscripting</code></p>
<dd> Disables the scripting engine.</dl>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
