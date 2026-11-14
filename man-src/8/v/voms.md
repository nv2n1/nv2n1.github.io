---
title: "voms(8)"
name: "voms"
section: "8"
letter: "v"
url: "/docs/linux/man/8-voms/"
description: "voms – VOMS server"
---

<p>voms &#8211; VOMS server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>voms</code> [-foreground] [-port&nbsp;<wbr><i>port</i>] [-backlog&nbsp;<wbr><i>pnum</i>] [-logfile&nbsp;<wbr><i>file</i>] [-globusid&nbsp;<wbr><i>id</i>] [-globuspwd&nbsp;<wbr><i>file</i>] [-passfile&nbsp;<wbr><i>file</i>] [-x509_cert_dir&nbsp;<wbr><i>path</i>] [-x509_cert_file&nbsp;<wbr><i>file</i>] [-x509_user_cert&nbsp;<wbr><i>file</i>] [-x509_user_key&nbsp;<wbr><i>file</i>] [-x509_user_proxy&nbsp;<wbr><i>file</i>] [-dbname&nbsp;<wbr><i>name</i>] [-username&nbsp;<wbr><i>name</i>] [-vo&nbsp;<wbr><i>&nbsp;<wbr>name</i>] [-timeout&nbsp;<wbr><i>&nbsp;<wbr>limit</i>] [-test] [-conf&nbsp;<wbr><i>&nbsp;<wbr>file</i>] [-uri&nbsp;<wbr><i>&nbsp;<wbr>uri</i>] [-version] [-code&nbsp;<wbr><i>c</i>] [-loglevel&nbsp;<wbr><i>lev</i>] [-logtype&nbsp;<wbr><i>type</i>] [-logformat&nbsp;<wbr><i>str</i>] [-logdateformat&nbsp;<wbr><i>str</i>] [-debug] [-sqlloc&nbsp;<wbr><i>path</i>] [-compat] [-socktimeout&nbsp;<wbr><i>num</i>] [-logmax&nbsp;<wbr><i>num</i>] [-newformat] [-skipcacheck] [-help] [-usage] [-globus&nbsp;<wbr><i>version</i>] [-contactstring&nbsp;<wbr><i>contact</i>] [-mysql-port&nbsp;<wbr><i>port</i>] [-mysql-socket&nbsp;<wbr><i>socket</i>] [-shortfqans] [-syslog] [-base64] [-nologfile]</dl>
<h2>Description</h2>
<dd>VOMS &#8211; Virtual Organization Membership Service. </p>
<p> For the initial setup of the server, run the voms_install_db script as root.</p>
<h2>Options</h2>
<p>Options may be specified indifferently with either a &quot;-&quot; or &quot;&#8211;&quot; prefix. Their meaning is the following. </p>
<p> <code>-help</code> </p>
<p> <code>-usage</code> </p>
<p> These options print a list of options that the server accepts. They are synonyms. </p>
<p> <code>-foreground</code> </p>
<p> Runs part of the server in foreground. Easier debugging. </p>
<p> <code>-port</code> <i>port</i> </p>
<p> Listens on port <i>port</i>. The default is 754. </p>
<p> <code>-backlog</code> <i>num</i> </p>
<p> Sets the maximum backlof for the connections. The default is 50. </p>
<p> <code>-logfile</code> <i>file</i> </p>
<p> Selects the file for logging. The default is /ver/log/voms. </p>
<p> <code>-globusid</code> <i>id</i> </p>
<p> <code>-globuspwd</code> <i>file</i> </p>
<p> This options are supported for backwards compatibility only. They have no effect, and indeed do not get listed by the -help option. </p>
<p> <code>-passfile</code> <i>file</i> </p>
<p> Reads the password to access the DB from <i>file</i>. The default is to read it from the console during server&#8217;s startup. </p>
<p> <code>-x509_cert_dir</code> <i>path</i> </p>
<p> <code>-x509_cert_file</code> <i>file</i> </p>
<p> <code>-x509_user_cert</code> <i>file</i> </p>
<p> <code>-x509_user_key</code> <i>file</i> </p>
<p> <code>-x509_user_proxy</code> <i>file</i> </p>
<p> These options set the respective variables. </p>
<p> <code>-dbname</code> <i>name</i> </p>
<p> Sets the name of the DB. Default <i>voms</i>. </p>
<p> <code>-username</code> <i>name</i> </p>
<p> Sets the name of the user for the DB login. The default is <i>voms</i>. </p>
<p> <code>-vo</code> <i>name</i> </p>
<p> Sets the name of the VO that owns this server. The default is <i>unspecified</i>. </p>
<p> <code>-timeout</code> <i>limit</i> </p>
<p> Sets the length of time that the information is valid, measured in secods. The default is 86400 seconds (24 hours). </p>
<p> <code>-test</code> </p>
<p> Prints information about the server startup and then exits. </p>
<p> <code>-conf</code> <i>file</i> </p>
<p> Reads option from the file <i>file</i>. The options must be present one per line in the format <code>-option[=value]</code> where the value part must obviously be present only if it is required. </p>
<p> <code>-uri</code> <i>uri</i> </p>
<p> Defines the uri of the server that will be included in the generated pseudo certificate. The default value is hostname:port </p>
<p> <code>-version</code> </p>
<p> Prints information about the server and then exits. </p>
<p> <code>-code</code> <i>c</i> </p>
<p> <code>-globus</code> <i>version</i> </p>
<p> These option are obsolete and only present for backwards compatibility with old installation. Currently, their values are ignored. Do not specify them in new installations. </p>
<p> <code>-logtype</code> <i>type</i> </p>
<p> Sets the type of messages that will be loggged. Acceptable values are: </p>
<dl>
<dd>&bull; 1 &#8211; STARTUP, print startup messages.</dl>
<dl>
<dd>&bull; 2 &#8211; REQUEST, print messages during the request interpretation phase.</dl>
<dl>
<dd>&bull; 4 &#8211; RESULT, print messages during the result sending phase.</dl>
<p> This values can be ORed together to indicate that all the corresponding types of messages are required. The default values is 255. </p>
<p> <code>-loglevel</code> <i>lev</i> </p>
<p> Sets the level of verbosity of log messages. Acceptable values are: </p>
<dl>
<dd>&bull; 1 &#8211; LEV_NONE, do not log anything.</dl>
<dl>
<dd>&bull; 2 &#8211; LEV_ERROR, the default, logs only error conditions.</dl>
<dl>
<dd>&bull; 3 &#8211; LEV_WARNINGS, logs also warning messages.</dl>
<dl>
<dd>&bull; 4 &#8211; LEV_INFO, logs also general informational messages.</dl>
<dl>
<dd>&bull; 5 &#8211; LEV_DEBUG, logs also a lot of debug messages. Setting this level of verbosity overwrites the value of the <code>-logtype</code> option to 255.</dl>
<p> Higher values include all messages printed by lower ones, and values not documented here are translated as the highest level possible, LEV_DEBUG </p>
<p> <code>-logformat</code> <i>str</i> </p>
<p> Sets the format used by the loggin system according toa printf-like format string with the following directives format: <i>\%[size][char]</i> where size, if present, sets the maximum length of the field and <i>char</i> selects the type of substitution done. Possible values are the following: </p>
<dl>
<dd>&bull; % &#8211; Substitutes a plain &#8216;%&#8217;.</dl>
<dl>
<dd>&bull; d &#8211; Substitutes the date. The date format is specified by the <code>-logdateformat</code> option.</dl>
<dl>
<dd>&bull; f &#8211; Substitutes the name of the source file that logs the message.</dl>
<dl>
<dd>&bull; F &#8211; Substitutes the name of the function that logs the message.</dl>
<dl>
<dd>&bull; h &#8211; Substitutes the hostname of the machine hosting the service.</dl>
<dl>
<dd>&bull; l &#8211; Substitutes the line number that logs the message.</dl>
<dl>
<dd>&bull; m &#8211; Substitutes the message proper.</dl>
<dl>
<dd>&bull; p &#8211; Substitutes the process&#8217; pid.</dl>
<dl>
<dd>&bull; s &#8211; Substitutes the service name (&quot;vomsd&quot;).</dl>
<dl>
<dd>&bull; t &#8211; Substitutes the number of the message type. (see the <code>-logtype</code> option)</dl>
<dl>
<dd>&bull; T &#8211; Substitutes the name of the message type. (see the <code>-logtype</code> option)</dl>
<dl>
<dd>&bull; v &#8211; Substitutes the number of the message level. (see the <code>-loglevel</code> option)</dl>
<dl>
<dd>&bull; V &#8211; Substitutes the name of the message level. (see the <code>-loglevel</code> option)</dl>
<p> The default value for this options is: &quot;%d:%h:%s(%p):%V:%T:%F (%f:%l):%m&quot; </p>
<p> <code>-logdateformat</code> <i>str</i> </p>
<p> This option sets the format used to print the date. The format is the same used by the <a href="/docs/linux/man/3-strftime/">strftime</a>(3) function, and its default value is: &quot;%c&quot;. </p>
<p> <code>-debug</code> </p>
<p> This option puts the server into debug mode. This mode automatically implies <code>-loglevel 5</code>. Also, this option hurts scalability and is not suggested in a production environment </p>
<p> <code>-sqlloc</code> <i>/path/file</i> </p>
<p> This option specifies the full path for the DB access library. Please note that there is no default for this option! </p>
<p> <code>-socktimeout</code> <i>num</i> </p>
<p> This option sets the amount of time, in seconds, after which the server will drop an inactive connection. The default is 60 seconds. </p>
<p> <code>-maxlog</code> <i>num</i> </p>
<p> This options sets the maximum size of a log file. Please note that this size is approximate, and may be exceeded by a few thousand bytes. In any case, when the specified amount is surpassed, logfiles are rotated. The default is 10Mb </p>
<p> <code>-newformat</code> </p>
<p> This forces the server to generate ACs in the new (correct) format. This is meant as a compatibility feature to ease migration while the servers upgrade to the new version. </p>
<p> <code>-skipcacheck</code> </p>
<p> This option, if specified, forces voms to drop some of the checks done as the authorization step before AC creation. Specifically, voms will no longer be capable of distinguishing to certificates with the same DN but different issuers. For obvious reasons, use of this option is discouraged. Note also that activating this option requires a previous check by the voms server administrator that there are no certificates registered in the DB which the same DN and different issuers. If there are, the result of a voms-proxy-init command for one of those users will be unpredictable. </p>
<p> <code>-contactstring</code> <i>contact</i> </p>
<p> This string specifies information on how to contact the DB server. Its exact meaning depends on the DB backend used. For MySQL it is the hostname of the MySQL server, and it defaults to &#8216;localhost&#8217;. For Oracle it is the contactstring of the DB. However, for oracle it is better to put what whould be the argument of this string into the &#8216;tnsnames.ora&#8217; file and ignore this option, </p>
<p> <code>-mysql-port </code> <i>port</i> </p>
<p> This option specified the port on which the MySQL server is listening if it is different from its 3306 default. This value is ignored for Oracle backends. </p>
<p> <code>-mysql-socket</code> <i>socket</i> </p>
<p> MySQL servers may be configured to allow access through a unix-level socket. This option allows to specify this method of contact. However, it is almost always better to contact the server through the port. This option is ignored for Oracle backends. </p>
<p> <code>-shortfqans</code> </p>
<p> This option instructs the server to always generate FQANs in their short form, i.e. without the /Role=NULL and /Capability=NULL parts. Successive server version will make this behaviour the default, and provide a <code>-noshortfqans</code> option to fallback to the longer format. Specifying this option is recommended. </p>
<p> <code>-syslog</code> </p>
<p> This option allows log messages to be sent to syslog. </p>
<p> <code>-base64</code> </p>
<p> This option instructs the server to use the base64 encoding for its messages, rather than the in-house encoding. This option will be made the default in future versions and <code>-nobase64</code> will be provided to fallback to the inhouse encoding. Specifying this option is recommended. </p>
<p> <code>-nologfile</code> </p>
<p> This option disables logging on the voms specific logfile. Please note that specifying this option without at the same time specifying <code>-syslog</code> implies that no logging will take place.</p>
<h2>Bugs</h2>
<p>m[blue]<code>EGEE Bug Tracking Tool</code>m[]<font SIZE="-2">[1]</font></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-voms-proxy-init/">voms-proxy-init</a>(1), <a href="/docs/linux/man/1-voms-proxy-info/">voms-proxy-info</a>(1), <a href="/docs/linux/man/1-voms-proxy-destroy/">voms-proxy-destroy</a>(1) </p>
<p> m[blue]<code>EDT Auth Home page</code>m[]<font SIZE="-2">[2]</font> </p>
<p> m[blue]<code>CVSweb</code>m[]<font SIZE="-2">[3]</font> </p>
<p> m[blue]<code>RPM repository</code>m[]<font SIZE="-2">[4]</font></p>
<h2>Authors</h2>
<p>Vincenzo Ciaschini Vincenzo.Ciaschini [at] cnaf.infn.it. </p>
<p> Valerio Venturi Valerio.Venturi [at] cnaf.infn.it.</p>
<h2>Copyright</h2>
<p>Copyright (c) Members of the EGEE Collaboration. 2004. See the beneficiaries list for details on the copyright holders. </p>
<p> Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may not use this file except in compliance with the License. You may obtain a copy of the License at </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.apache.org">www.apache.org</a>/licenses/LICENSE-2.0</code>m[]<font SIZE="-2">[5]</font> </p>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>EGEE Bug Tracking Tool</p>
<dl>
<dd><a rel="nofollow" href="https://savannah.cern.ch/projects/jra1mdw/">https://savannah.cern.ch/projects/jra1mdw/</a></dl>
<dt> 2.</p>
<dd>EDT Auth Home page</p>
<dl>
<dd><a rel="nofollow" href="http://grid-auth.infn.it">http://grid-auth.infn.it</a></dl>
<dt> 3.</p>
<dd>CVSweb</p>
<dl>
<dd><a rel="nofollow" href="http://datagrid.in2p3.fr/cgi-bin/cvsweb.cgi/Auth/voms">http://datagrid.in2p3.fr/cgi-bin/cvsweb.cgi/Auth/voms</a></dl>
<dt> 4.</p>
<dd>RPM repository</p>
<dl>
<dd><a rel="nofollow" href="http://datagrid.in2p3.fr/distribution/autobuild/i386-rh7.3">http://datagrid.in2p3.fr/distribution/autobuild/i386-rh7.3</a></dl>
<dt> 5.</p>
<dd><a rel="nofollow" href="http://www.apache.org">www.apache.org</a>/licenses/LICENSE-2.0</p>
<dl>
<dd><a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a></dl>
