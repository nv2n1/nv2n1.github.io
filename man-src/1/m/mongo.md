---
title: "mongo(1)"
name: "mongo"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongo/"
description: "mongo – MongoDB Shell"
---

<h2>NAME</h2>
<p> mongo &#8211; MongoDB Shell</p>
<h2>DESCRIPTION</h2>
<p> <code>mongo</code> is an interactive JavaScript shell interface to MongoDB, which provides a powerful interface for systems administrators as well as a way for developers to test queries and operations directly with the database. <code>mongo</code> also provides a fully functional JavaScript environment for use with a MongoDB. This document addresses the basic invocation of the <code>mongo</code> shell and an overview of its usage.</p>
<h2>OPTIONS</h2>
<h3>Core Options</h3>
<dl>
<dt><code>mongo</code></p>
<dd>
<dt><code>&#8211;shell</code></p>
<dd> Enables the shell interface. If you invoke the <code>mongo</code> command and specify a JavaScript file as an argument, or use <i>&#8211;eval</i> to specify JavaScript on the command line, the <i>&#8211;shell</i> option provides the user with a shell prompt after the file finishes executing.</p>
<dt><code>&#8211;nodb</code></p>
<dd> Prevents the shell from connecting to any database instances. Later, to connect to a database within the shell, see <i>mongo-shell-new-connections</i>.</p>
<dt><code>&#8211;norc</code></p>
<dd> Prevents the shell from sourcing and evaluating <code>~/.mongorc.js</code> on start up.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Silences output from the shell during the connection process.</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port where the <code>mongod</code> or <code>mongos</code> instance is listening. If <i>&#8211;port</i> is not specified, <code>mongo</code> attempts to connect to port <code>27017</code>.</p>
<dt><code>&#8211;host &lt;hostname&gt;</code></p>
<dd> Specifies the name of the host machine where the <code>mongod</code> or <code>mongos</code> is running. If this is not specified, <code>mongo</code> attempts to connect to a MongoDB process running on the localhost.</p>
<dt><code>&#8211;eval &lt;javascript&gt;</code></p>
<dd> Evaluates a JavaScript expression that is specified as an argument. <code>mongo</code> does not load its own environment when evaluating code. As a result many options of the shell environment are not available.</p>
<dt><code>&#8211;username &lt;username&gt;, -u</code></p>
<dd> Specifies a username with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;password</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;password &lt;password&gt;, -p</code></p>
<dd> Specifies a password with which to authenticate to a MongoDB database that uses authentication. Use in conjunction with the <code>&#8211;username</code> and <code>&#8211;authenticationDatabase</code> options.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongo</code> options and usage.</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongo</code> release number.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Increases the verbosity of the output of the shell during the connection process.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongo</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongo</code>, disable IPv6 support by default.</p>
<dt><code>&lt;db address&gt;</code></p>
<dd> Specifies the &quot;database address&quot; of the database to connect to. For example: </p>
<pre>
mongo admin
</pre>
<p> The above command will connect the <code>mongo</code> shell to the <i>admin database</i> on the local machine. You may specify a remote database instance, with the resolvable hostname or IP address. Separate the database name from the hostname using a <code>/</code> character. See the following examples: </p>
<pre>
mongo mongodb1.example.net
mongo mongodb1/admin
mongo 10.8.8.10/test
</pre>
<dt><code>&lt;file.js&gt;</code></p>
<dd> Specifies a JavaScript file to run and then exit. Generally this should be the last option specified.</dl>
<h3>Optional</h3>
<p> To specify a JavaScript file to execute <i>and</i> allow <code>mongo</code> to prompt you for a password using <i>&#8211;password</i>, pass the filename as the first parameter with <i>&#8211;username</i> and <i>&#8211;password</i> as the last options, as in the following: </p>
<pre>
mongo file.js --username username --password
</pre>
<p> Use the <i>&#8211;shell</i> option to return to a shell after the file finishes running.</p>
<h3>Authentication Options</h3>
<dl>
<dt><code>&#8211;authenticationDatabase &lt;dbname&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the database that holds the user&#8217;s credentials. If you do not specify an authentication database, <code>mongo</code> assumes that the database specified as the argument to the <i>&#8211;db</i> option holds the user&#8217;s credentials.</p>
<dt><code>&#8211;authenticationMechanism &lt;name&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies the authentication mechanism. By default, the authentication mechanism is <code>MONGODB-CR</code>, which is the MongoDB challenge/response authentication mechanism. In MongoDB Enterprise, <code>mongo</code> also includes support for <code>GSSAPI</code> to handle Kerberos authentication. See <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication">http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication</a> for more information about Kerberos authentication.</dl>
<h3>SSL Options</h3>
<dl>
<dt><code>&#8211;ssl</code></p>
<dd> New in version 2.6. </p>
<p> Enables connection to a <code>mongod</code> or <code>mongos</code> that has SSL support enabled. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslPEMKeyFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains both the SSL certificate and key. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> This option is required when using the <i>&#8211;ssl</i> option to connect to a <code>mongod</code> or <code>mongos</code> that has <code>sslCAFile</code> enabled <i>without</i> <code>sslWeakCertificateValidation</code>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslPEMKeyPassword &lt;value&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongo</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongo</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslCAFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the root certificate chain from the Certificate Authority. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslCRLFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the Certificate Revocation List. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslFIPSMode</code></p>
<dd> New in version 2.6. </p>
<p> Directs <code>mongo</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslAllowInvalidCertificates</code></p>
<dd> New in version 2.6. </p>
<p> Bypasses the validation checks for server certificates and allows the use of invalid certificates. When using the <code>sslAllowInvalidCertificates</code> setting, MongoDB logs as a warning the use of the invalid certificate. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.dbshell</code></p>
<dd> <code>mongo</code> maintains a history of commands in the <code>.dbshell</code> file. </p>
<p> <code>NOTE:</code> <code>mongo</code> does not recorded interaction related to authentication in the history file, including <code>authenticate</code> and <code>db.addUser()</code>. </p>
<p> <code>WARNING:</code> Versions of Windows <code>mongo.exe</code> earlier than 2.2.0 will save the <i>.dbshell</i> file in the <code>mongo.exe</code> working directory.</p>
<dt><code>~/.mongorc.js</code></p>
<dd> <code>mongo</code> will read the <code>.mongorc.js</code> file from the home directory of the user invoking <code>mongo</code>. In the file, users can define variables, customize the <code>mongo</code> shell prompt, or update information that they would like updated every time they launch a shell. If you use the shell to evaluate a JavaScript file or expression either on the command line with <i>&#8211;eval</i> or by specifying <i>a .js file to mongo</i>, <code>mongo</code> will read the <code>.mongorc.js</code> file <i>after</i> the JavaScript has finished processing. </p>
<p> Specify the <i>&#8211;norc</i> option to disable reading <code>.mongorc.js</code>.</p>
<dt><code>/etc/mongorc.js</code></p>
<dd> Global <code>mongorc.js</code> file which the <code>mongo</code> shell evaluates upon start-up. If a user also has a <code>.mongorc.js</code> file located in the <i>HOME</i> directory, the <code>mongo</code> shell evaluates the global <code>/etc/mongorc.js</code> file <i>before</i> evaluating the user&#8217;s <code>.mongorc.js</code> file. </p>
<p> <code>/etc/mongorc.js</code> must have read permission for the user running the shell. The <i>&#8211;norc</i> option for <code>mongo</code> suppresses only the user&#8217;s <code>.mongorc.js</code> file. </p>
<p> On Windows, the global <code>mongorc.js &lt;/etc/mongorc.js&gt;</code> exists in the <code>%ProgramData%\MongoDB</code> directory.</p>
<dt><code>/tmp/mongo_edit</code><i>&lt;time_t&gt;</i>.js</p>
<dd> Created by <code>mongo</code> when editing a file. If the file exists, <code>mongo</code> will append an integer from <code>1</code> to <code>10</code> to the time value to attempt to create a unique file.</p>
<dt><code>%TEMP%mongo_edit</code><i>&lt;time_t&gt;</i>.js</p>
<dd> Created by <code>mongo.exe</code> on Windows when editing a file. If the file exists, <code>mongo</code> will append an integer from <code>1</code> to <code>10</code> to the time value to attempt to create a unique file.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>EDITOR</code></p>
<dd> Specifies the path to an editor to use with the <code>edit</code> shell command. A JavaScript variable <code>EDITOR</code> will override the value of <i>EDITOR</i>.</p>
<dt><code>HOME</code></p>
<dd> Specifies the path to the home directory where <code>mongo</code> will read the <code>.mongorc.js</code> file and write the <code>.dbshell</code> file.</p>
<dt><code>HOMEDRIVE</code></p>
<dd> On Windows systems, <i>HOMEDRIVE</i> specifies the path the directory where <code>mongo</code> will read the <code>.mongorc.js</code> file and write the <code>.dbshell</code> file.</p>
<dt><code>HOMEPATH</code></p>
<dd> Specifies the Windows path to the home directory where <code>mongo</code> will read the <code>.mongorc.js</code> file and write the <code>.dbshell</code> file.</dl>
<h2>KEYBOARD SHORTCUTS</h2>
<p> The <code>mongo</code> shell supports the following keyboard shortcuts: [1] <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Keybinding</code> </td>
<td> <code>Function</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Up arrow </td>
<td> Retrieve previous command from history
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Down-arrow </td>
<td> Retrieve next command from history
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Home </td>
<td> Go to beginning of the line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> End </td>
<td> Go to end of the line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Tab </td>
<td> Autocomplete method/command
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Left-arrow </td>
<td> Go backward one character
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Right-arrow </td>
<td> Go forward one character
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-left-arrow </td>
<td> Go backward one word
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-right-arrow </td>
<td> Go forward one word
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-left-arrow </td>
<td> Go backward one word
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-right-arrow </td>
<td> Go forward one word
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-A </td>
<td> Go to the beginning of the line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-B </td>
<td> Go backward one character
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-C </td>
<td> Exit the <code>mongo</code> shell
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-D </td>
<td> Delete a char (or exit the <code>mongo</code> shell)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-E </td>
<td> Go to the end of the line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-F </td>
<td> Go forward one character
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-G </td>
<td> Abort
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-J </td>
<td> Accept/evaluate the line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-K </td>
<td> Kill/erase the line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-L or type <code>cls</code> </td>
<td> Clear the screen
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-M </td>
<td> Accept/evaluate the line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-N </td>
<td> Retrieve next command from history
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-P </td>
<td> Retrieve previous command from history
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-R </td>
<td> Reverse-search command history
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-S </td>
<td> Forward-search command history
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-T </td>
<td> Transpose characters
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-U </td>
<td> Perform Unix line-discard
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-W </td>
<td> Perform Unix word-rubout
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-Y </td>
<td> Yank
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-Z </td>
<td> Suspend (job control works in linux)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-H </td>
<td> Backward-delete a character
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Ctrl-I </td>
<td> Complete, same as Tab
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-B </td>
<td> Go backward one word
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-C </td>
<td> Capitalize word
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-D </td>
<td> Kill word
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-F </td>
<td> Go forward one word
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-L </td>
<td> Change word to lowercase
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-U </td>
<td> Change word to uppercase
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-Y </td>
<td> Yank-pop
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-Backspace </td>
<td> Backward-kill word
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-&lt; </td>
<td> Retrieve the first command in command history
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Meta-&gt; </td>
<td> Retrieve the last command in command history
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dl>
<dt>[1]</p>
<dd> MongoDB accommodates multiple keybinding. Since 2.0, <code>mongo</code> includes support for basic emacs keybindings.</dl>
<h2>USE</h2>
<p> Typically users invoke the shell with the <code>mongo</code> command at the system prompt. Consider the following examples for other scenarios. </p>
<p> To connect to a database on a remote host using authentication and a non-standard port, use the following form: </p>
<pre><code>
mongo-- username&lt;user&gt; --password&lt;pass&gt; --host&lt;host&gt; --port 28015
</code></pre>
<p> Alternatively, consider the following short form: </p>
<pre>
mongo -u &lt;user&gt; -p &lt;pass&gt; --host &lt;host&gt; --port 28015
</pre>
<p> Replace <code>&lt;user&gt;</code>, <code>&lt;pass&gt;</code>, and <code>&lt;host&gt;</code> with the appropriate values for your situation and substitute or omit the <i>&#8211;port</i> as needed. </p>
<p> To execute a JavaScript file without evaluating the <code>~/.mongorc.js</code> file before starting a shell session, use the following form: </p>
<pre>
mongo --shell --norc alternate-environment.js
</pre>
<p> To execute a JavaScript file with authentication, with password prompted rather than provided on the command-line, use the following form: </p>
<pre>
mongo script-file.js -u &lt;user&gt; -p
</pre>
<p> To print return a query as <i>JSON</i>, from the system prompt using the <i>&#8211;eval</i> option, use the following form: </p>
<pre>
mongo --eval 'db.collection.find().forEach(printjson)'
</pre>
<p> Use single quotes (e.g. <code>&#8216;</code>) to enclose the JavaScript, as well as the additional JavaScript required to generate this output.</p>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
