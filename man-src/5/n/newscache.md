---
title: "newscache(5)"
name: "newscache"
section: "5"
letter: "n"
url: "/docs/linux/man/5-newscache/"
description: "newscache.conf"
---

<p>newscache.conf </p>
<h2>Synopsis</h2>
<p><code>/etc/newscache.conf</code> </p>
<h2>Description</h2>
<p>The file <i>/etc/newscache.conf</i> defines all the <code>NewsCache &#8216;s</code> configuration options. It is also used for <code><a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</code> ,which is responsible for submitting articles from the outgoing spool directory and prefetching newsgroups and <code><a href="/docs/linux/man/8-newscacheclean/">newscacheclean</a>(8),</code> which cleans up the Cache. </p>
<dl>
<dt>NewsCache is a free cache server for USENET News. NewsCache acts to news reading clients like a news server, except that it stores only those articles that have been requested by at least one client. NewsCache targets problems of the current News System like network bandwidth consumption or the IO load caused by news clients. NewsCache acts to the upstream news server like a news reader programm.</p>
<dd>
<dt>It supports principles the following modes (for a detailed description read ServerSpec Configuration Options below):</p>
<dd>
<dt><i>cached</i></p>
<dd>NewsCache store every retrieved article in his internal cache. If this article is retrieved by another news reader client, then NewsCache can get the article from his cache instead of retrieving this article again from the upstream newsserver.</p>
<dt><i>not-cached</i></p>
<dd>NewsCache act as a &quot;proxy&quot; and does&#8217;nt store retrieved article in his local cache. This is usefull for combined multiple local newsserver configuration.</p>
<dt><i>offline</i></p>
<dd>NewsCache does&#8217;nt connect to the upstream newsserver. Only the specified newsgroups are retrieved by <code><a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</code> and stored in the cache. This is usefull in dialup configurations. The news reader clients can only access this newsgroups.</p>
<dt><i>semi-offline, cached</i></p>
<dd>The overview informations are loaded with <code><a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</code> and the articles retrieved by NewsCache, if a news reader client request it. The article is stored in the internal cache. </p>
</dl>
<h3>General Configuration Options</h3>
<dl>
<dt><i>ConfigVersion version</i></p>
<dd>Specifies the syntax version of the configuration file. This manual page describes version 3. This allows NewsCache to detect a configuration file of an older NewsCache version. If specified, it should be specified as the first configuration option.</p>
<dt><i>ServerType type</i></p>
<dd>This may be either <i>standalone</i> for a standalone server or <i>inetd</i> if NewsCache is started from inetd. A standalone server has the advantage that the configuration file will be read once only, for the cost of an extra process running all the time. Usually, you use a standalone server, if NewsCache is frequently accessed. The default value is standalone.</p>
<dt><i>PidFile filename</i></p>
<dd>On startup NewsCache will write its PID to the given file. This can then be used by system scripts to gracefully stop NewsCache by sending a SIGTERM to the parent process. No default value.</p>
<dt><i>Username username</i></p>
<dd>Change the user id to username as soon as NewsCache has bound to <i>CachePort</i>. No default value.</p>
<dt><i>Groupname groupname</i></p>
<dd>Change the group id to groupname as soon as NewsCache has bound to <i>CachePort</i>. No default value.</p>
<dt><i>Admin email-address</i></p>
<dd>The email address of this NewsCache&#8217;s administrator.</p>
<dt><i>AccessList { AccessSpec AccessSpec &#8230; }</i></p>
<dd>Client access configuration.</p>
<dt><i>NewsServerList { ServerSpec ServerSpec &#8230; }</i></p>
<dd>Defines a list of news servers and the newsgroups to retrieve from which news server. For a detailed description of <i>ServerSpec </i> see the ServerSpec Configuration Options section below.</p>
<dt><i>Timeouts active-db group-description</i></p>
<dd>Timeouts in seconds for the retrieval of the active database (first parameter) and the description of the newsgroups (second parameter). If a client requests &quot;list active&quot;, then newscache checks if the active database timeout is reached and first requests the active informations from the upstream servers before returning the data to the client. Note: if the ServerSpec section contains the Options offline or semioffline, then the data will be not downloaded from the upstream server. You need <code><a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</code>. The default values are 3600 seconds for both parameter.</p>
<dt><i>ClientTimeout t</i></p>
<dd>Terminate the connection after t seconds inactivity. The default value is 1200 seconds.</p>
<dt><i>MaxConnections number</i></p>
<dd>Maximal number of simultanous connections. This Parameter works only in standalone mode. The default number is 32.</p>
<dt><i>SpoolDirectory directory</i></p>
<dd>The directory, where the cached newsgroups and articles should be stored. The default value is /var/cache/newscache.</p>
<dt><i>Spoolsize KBytes</i></p>
<dd>The maximum size of the spool area. This is controlled by the <code><a href="/docs/linux/man/8-newscacheclean/">newscacheclean</a></code>(8)<code>.</code> The default value is 1048576 KBytes (1 GByte).</p>
<dt><i>LogDirectory directory</i></p>
<dd>Directory, where all the log-files should go. No default value.</p>
<dt><i>LogStyle [strict-inn][hostname][ip-address]</i></p>
<dd>StrictINN style logging; log client&#8217;s hostname and or IP-address.</p>
<dt><i>CachePort port</i></p>
<dd>Listen on port for incoming requests. Port may be a valid service-name (Ususally, listed in /etc/services) or a port number preceded by a #-sign. This directive is uneffective if NewsCache is started from inetd.</p>
<dt><i>Retries number</i></p>
<dd>Specifies the number of retries for connecting to the news server. If this limit is exceded NewsCache assumes that the news server is unreachable.</p>
<dt><i>PrefetchFile filename</i></p>
<dd>Specifies the filename. No default value.</p>
<dt><i>NiceServer n</i></p>
<dd>Increment priority of the server process by n. See also <code><a href="/docs/linux/man/1-nice/">nice</a>(1)</code>. The default value is 0.</p>
<dt><i>NiceClient n</i></p>
<dd>Increment priority of the client process by n. The client process communicates with the user program. See also <code><a href="/docs/linux/man/1-nice/">nice</a>(1)</code>.</p>
<dt><i>NiceClean n</i></p>
<dd>Increment priority of the newscacheclean process by n. See also <code><a href="/docs/linux/man/1-nice/">nice</a>(1)</code>. The newscacheclean process is a housekeeping process. See alco <code><a href="/docs/linux/man/8-newscacheclean/">newscacheclean</a>(8)</code>.</p>
<dt><i>ListenTo specification</i></p>
<dd>The Address, where NewsCache is listening, if running in standalone mode. In a multihomed environment the address of one NIC can be specified. The default Port is nntp from /etc/services. For the port-number an entry fom /etc/services or a port-number can be specified.</dl>
<h3>AccessSpec Configuration Options</h3>
<dl>
<dd>
<pre><i>Client</i> [fqdn-or-part | ip-address/netmask]
{
 <i>allow</i> read post debug none authentication
 <i>List</i> <i>NGSpecification</i>
 <i>Read</i> NGSpecification
 <i>PostTo</i> NGSpecification
 <i>Authentication</i> authenticationSpecification
}</pre>
<dt>allow [read] [post] [debug] [none] [authentication]</p>
<dd>Allow read, post, debug for this Client. The default is none. If only authenticated users are allowed for this network, then authentication can be specified. See example &quot;Only authenticated users&quot;.</p>
<dt>List <i>NGSpecification</i></p>
<dd>Permits client access to the specified newsgroups.</p>
<dt>Read <i>NGSpecification</i></p>
<dd>Allow reading specified newsgroups. Same format as List.</p>
<dt>PostTo <i>NGSpecification</i></p>
<dd>Allow posting to specified newsgroups. Same format as List.</p>
<dt>NGSpecification</p>
<dd>is a comma seperated list of newsgroups, where the last part of newsgroup may be substituted by * standing for any string. Each newsgroup is retrieved from the news server with the longest match. Examples: * (all newsgroups), at.* (the whole at. hierarchy), *,!alt.binaries.* (all newsgroups without alt.binaries hierarchy).</p>
<dt>Authentication</p>
<dd>Type of authentication plus authenication specific options. Possible values are:</p>
<dt>none</p>
<dd>no further authentication necessary</p>
<dt>file:/path/to/file</p>
<dd>formatdescription: </p>
<pre> username:password:list:read:postto:allow</pre>
<p>The additional access specification are added to the normal List Read and PostTo Parameters (see above and the example section). The password field is a encrypted password (md5crypt of crypt) or plaintext (configured with &#8211;enable-plainpass). htpasswd from the apache project can create such a password. In the allow field can be additional permission specified (Example: authenticated user can be use the post command).</p>
<dt>unix:list:read:postto:allow</p>
<dd>Use unix authentication (getpwnam or getspnam). The additional access specification are added to the normal List Read and PostTo Parameters and allow(see above and the example section). If only unix is specified, then all clients must step throuh the authentication. If further fields specified, then unauthenticated clients have the access specified with the parameter allow, List, ReadTo, PostTo and authenticated clients uses the arguments and modify the original parameters.<br />
 It is also possible to specifiy empty fields, example: unix:::*:debug. Which means, that the PostTo parameter is extended with *. What actual settings are used by NewsCache can be determined with the xdebug dump authorization command. </p>
<dt>pam:list:read:postto:allow</p>
<dd>Use pam authentication. For additional description of the fields see: <i>unix:list:read:postto:allow</i> The PAM Servicename can be specified with the configuration parameter <i>PAMServicename</i> </p>
<dt>pam+file:/path/to/file</p>
<dd>The authentication is handled over pam and the additional permission values are taken from the file. The recordformats in the file are valid: </p>
<pre>#this is a comment
hugo:at.test:at.test:at.test:post
@mygroup:de.*:de.*:de.*:post
*:us.*:us.*::</pre>
<p>This mean, that after a succussfully authentication process, the user hugo can list at.test, read at.test, postto at.test and allow the use of post command. If the account is member of the group mygroup additionally allow list de.* read de.* and postto de.*, also allowing the use of the post command. * means, that all users can list us.* and read us.* newsgroups. </p>
<dt>PAMServicename</p>
<dd>This parameter specifiy the name of the PAM Service. The default is newscache. You can use different PAM settings for each Client network. For further explanation of PAM see the System administrators PAM Guide. This Guide can be downloaded from <a rel="nofollow" href="http://www.kernel.org/pub/linux/libs/pam/pre/doc/">http://www.kernel.org/pub/linux/libs/pam/pre/doc/</a> </p>
</dl>
<h3>ServerSpec Configuration Options</h3>
<pre><i>[Server | NoServer]</i> news.host Service 
{
 <i>Read</i> GroupSpec
 <i>PostTo</i> GroupSpec
 <i>GroupTimeout</i> seconds
 <i>BindFrom</i> address (FIXME)
 <i>Retris</i> nr-of-retries
 <i>User</i> username
 <i>Password</i> password
 <i>Options</i> flags
 <i>Commands</i> commands
}</pre>
<dl>
<dd>to specify what newsgroups have to be retrived from which news server and which articles have to be submitted to which news server or <i>ServerSpec</i> may be:</p>
<dt>NoServer { Read <i>GroupSpec</i> PostTo <i>GroupSpec</i> }</p>
<dd>to specify what newsgroup has to be retrieved by no news server and to which newsgroups no articles should be posted to. Or:</p>
<dt>Server news.host Service</p>
<dd>
<dd><i>news.host</i> is the name of the news server and <i>Service</i> indicates the port, where the news server is listening for connections.</p>
<dt>Read <i>NewsgroupList</i></p>
<dd>The comma separated list specifiy the wildmat newsgroup specifications. Each element of the list will be fetched with the list active element. Example: Read at.*,de.* will send to the upstream newsserver the following two commands: list active at.* and list active de.*. For details see section 2.1.2 LIST ACTIVE [WILDMAT] of RFC2980. These parameter can help you saving bandwidth. <i>AccessSpec Configuration Options</i><br />
&nbsp;<wbr>. No default value.</p>
<dt>PostTo <i>NGSpecification</i></p>
<dd>NewsCache post an article to the best matching upstream newsserver. If the article cannot be submitted immediately, it is kept for later transmission. See the example: Multiple Upstream NewsServer.</p>
<dt>GroupTimeout <i>seconds</i></p>
<dd>specified how long the group information (for instance retrieved with the command GROUP at.linux) is valid (in seconds). Note: if the ServerSpec section contains the Options offline, then the data will be not downloaded from the upstream server. You need <code><a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</code>. The default value is 600 seconds.</p>
<dt>Options <i>flags</i></p>
<dd>Specifies a list of options that should be turned on or off. The default flags are: cached setpostflag. Valid flags are: </p>
<pre> <i>[not-]setpostflag</i>
 <i>[not-]cached</i>
 <i>[not-]offline</i>
 <i>semioffline</i></pre>
<dl>
<dd>
<dl>
<dt>
<dt>[not-]setpostflag</p>
<dd>
<dd>set postflag to n in the active database, if posting to the news server is not allowed. not-setpostflag, setpostflag indicates whether the postflag of newsgroups on servers without posting permission should be set to `n&#8217;.</p>
<dt>[not-]cached</p>
<dd>not-cached, cached indicate, whether groups from this server should be cached or not. </p>
<dt>[not-]offline</p>
<dd>NewsCache does&#8217;nt connect to the upstream newsserver. Only the specified newsgroups are retrieved by <code><a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</code> and stored in the cache. This is usefull in dialup configurations. The news reader clients can only access this newsgroups.</p>
<dt>semioffline</p>
<dd>The overview informations are loaded with <code><a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</code> and the articles retrieved by NewsCache, if a news reader client request it. The article is stored in the internal cache.</dl>
</dl>
<dt>Commands <i>commands</i></p>
<dd>All commands are switched on by default and NewsCache tries itself to find out which of the commands are supported. In some situations it might be necessary to deactivate a command manually (eg. it is not implemented correctly by your news server). To switch off, prepend the command with not-support commands: listgroup, over</dl>
<h2>Examples</h2>
<dl>
<dt>Reducing Load from a NewsServer &#8211; cached mode</p>
<dd>
<pre>ConfigVersion 5
ListenTo DEFAULT
AccessList {
 Client 127.0.0.1/255.255.255.255 {
 allow read post
 # No xdebug command for unauthenticated
 # clients.
 List *
 Read *
 PostTo *
 Authentication unix::::debug
 # xdebug command for authenticated clients.
 # the empty fields (:::) doesn't modify
 # List, Read, PostTo parameters.
 }
 Default {
 allow none
 }
}
NewsServerList {
 Server news.host nntp {
 List at.*
 Read at.*
 PostTo at.*
 GroupTimeout 1200
 Options cached
 Authentication unix:*:*:*
 # Authenticated user see all groups
 }
}</pre>
<dt>Local NewsGroups</p>
<dd>Configuration to transparently include local Newsgroups. The local Newsgroups are not cached. </p>
<pre>ConfigVersion 5
ListenTo DEFAULT
AccessList {
 Client 127.0.0.1/255.255.255.255 {
 allow read post debug
 List *
 Read *
 PostTo *
 Authentication none
 }
 Default {
 allow none
 }
}
NewsServerList {
 Server upstream.newsserver nntp {
 Read *
 PostTo *
 GroupTimeout 1200
 Options cached
 }
 Server local.newsserver #120 {
 Read *
 PostTo *
 GroupTimeout 1200
 Options not-cached
 }
}</pre>
<dt>Offline Mode</p>
<dd>Offline Mode for ppp dialup connections. The Newsgroup of interesst have to list in prefetch-file and retrieved with the updatenews program. </p>
<pre>ConfigVersion 5
ListenTo DEFAULT
AccessList {
 Client 127.0.0.1/255.255.255.255 {
 allow read post debug
 List *
 Read *
 PostTo *
 Authentication none
 }
 Default {
 allow none
 }
}
NewsServerList {
 Server upstream.newsserver nntp {
 Read *
 PostTo *
 GroupTimeout 1200
 Options offline
 }
}</pre>
<dt>Only Authenticated Users</p>
<dd>Only authenticated users are allowed. This example show how to setup. </p>
<pre>ConfigVersion 5
ListenTo DEFAULT
AccessList {
 Client 127.0.0.1/255.255.255.255 {
 allow authentication
 List !*
 Read !*
 PostTo !*
 Authentication pam:*:*:*:read,post
 }
 Default {
 allow none
 }
}
NewsServerList {
 Server upstream.newsserver nntp {
 Read *
 PostTo *
 GroupTimeout 1200
 Options cached
 }
}</pre>
<dt>Multiple Upstream NewsServer</p>
<dd>We are connected to the main upstream NewsServer f.q.d.n and various other NewsServer. The new Newsgroups after modifications of the NewsServerList are available after the Timeout ActiveDB Value. This can be forced with updatenews -a (see manual page updatenews). </p>
<pre>ConfigVersion 5
ListenTo DEFAULT
AccessList {
 Client 127.0.0.1/255.255.255.255 {
 allow authentication
 List *
 Read *
 PostTo *
 Authentication none
 }
 Default {
 allow none
 }
}
NewsServerList {
 Server f.q.d.n nntp {
 Read *
 PostTo *
 GroupTimeout 1200
 Options cached
 }
 NewsServerList {
 Server news.redhat.com nntp {
 Retries 3
 Read gated.*
 PostTo gated.*
 GroupTimeout 1200
 Options cached
 }
 Server nntp.perl.org nntp {
 Retries 3
 Read perl.*
 PostTo perl.*
 GroupTimeout 1200
 Options cached
 }
 Server news.php.net nntp {
 Retries 3
 Read php.*
 PostTo php.*
 GroupTimeout 1200
 Options cached
 }
}</pre>
<h2>THE xdebug COMMAND</h2>
<dl>
<dt>telnet localhost 119 and the xdebug command</p>
<dd>Note: in the configuration file the allow must contain the debug option. The following example show the a typical xdebug session.&quot; </p>
<pre>telnet localhost 119
Trying 127.0.0.1...
Connected to faultier.
Escape character is '^]'.
200 NewsCache 1.2, accepting NNRP commands
xdebug dump authorization
xxx authorization data follows
127.0.0.1/255.255.255.255{
 access_flags=4 ( debug)
 list=at.*
 read=at.*
 postto=at.*
 authentication=unix:*:*:*:post,read
}
authinfo user myusername
381 password please
authinfo pass mypassword
281 OK.
xdebug dump authorization
xxx authorization data follows
127.0.0.1/255.255.255.255{
 access_flags=7 ( read post debug)
 list=at.*,*
 read=at.*,*
 postto=at.*,*
 authentication=unix:*:*:*:post,read
}
quit
205 Good bye
Connection closed by foreign host.</pre>
</dl>
<h2>Files</h2>
<p>/etc/newscache.conf<br />
 /usr/sbin/newscache<br />
 /usr/sbin/newscacheclean<br />
 /usr/sbin/updatenews</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-newscache/">newscache</a>(8), <a href="/docs/linux/man/8-newscacheclean/">newscacheclean</a>(8), <a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</p>
<h2>Authors</h2>
<p>1997-2000 Thomas Gschwind &lt;tom [at] infosys.tuwien.ac.at&gt;<br />
 2001-2004 Herbert Straub &lt;h.straub [at] aon.at&gt;</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;newscache [at] linuxhacker.org&gt;.</p>
<h2>Copyright</h2>
<p><code>NewsCache</code> is released under the <code>GNU General Public License (GPL).</code> There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
