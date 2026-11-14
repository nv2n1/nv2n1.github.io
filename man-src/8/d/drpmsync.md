---
title: "drpmsync(8)"
name: "drpmsync"
section: "8"
letter: "d"
url: "/docs/linux/man/8-drpmsync/"
description: "drpmsync – sync a file tree with deltarpms"
---

<p>drpmsync &#8211; sync a file tree with deltarpms </p>
<h2>Synopsis</h2>
<p><code>drpmsync</code> [<code>-c</code> <i>config</i>] [<i>source</i>] <i>dir</i><br />
 <code>drpmsync</code> [<code>-s</code>|<code>-S</code>] <i>serverconfig</i><br />
 <code>cgi-bin/drpmsync</code> </p>
<h2>Description</h2>
<p>Drpmsync keeps a local file system tree in sync with a remote one. Its intended use is to work with rpm trees; the deltarpm technology can only save bandwidth if rpms get transmitted. Please use the rsync program for normal file trees. Drpmsync can run in two modes: as a client it connects to a server, receives a file list and brings the tree up to date, as a server it answers incoming requests and transmits files and rpms. </p>
<h2>Client Mode</h2>
<p>In this mode drpmsync updates the tree in <i>dir</i>. It opens the configuration file <i>dir</i><code>/drpmsync/config</code> to get information about which server to use and other settings. You can specify a different configuration file with the <code>-c</code> option. The following settings are understood (the default for the boolean settings is false): </p>
<p> <code>source:</code> <i>server1</i> <i>server2</i>&#8230; </p>
<p> This is a list of servers to connect to. Drpmsync advances through this list until a working server is found. If a source is specified on the command line it is used instead of the one from the configuration. The syntax for the server entries is &quot;<i>host</i>[<code>:</code><i>port</i>]/<i>tree</i>&quot;. </p>
<p> <code>log:</code> <i>logfile</i> </p>
<p> Specifies the name of a logfile. If the name does not start with a slash, <i>dir</i><code>/drpmsync/</code> is prepended to it. </p>
<p> <code>generate_deltas:</code> <code>true|false</code> </p>
<p> Controls whether drpmsync generates a delta if it receives a new version of a rpm and the server doesn&#8217;t provide a delta. This is only useful if the local tree is also exported to other clients via a local drpmsync server. </p>
<p> <code>generate_delta_compression:</code> <i>comp</i> </p>
<p> This parameter is forwarded to the makedeltarpm program when creating deltas. An example would be <code>gzip,gzip</code>. </p>
<p> <code>keep_deltas:</code> <code>true|false</code> </p>
<p> Tell drpmsync to save received or freshly created deltas to the <i>dir</i><code>/drpmsync/delta</code> directory. Automatically true if <code>generate_deltas</code> or <code>keep_uncombined</code> is set to true. </p>
<p> <code>keep_uncombined:</code> <code>true|false</code> </p>
<p> This tells drpmsync to request uncombined deltas from the server instead of a precombined single delta. This makes sense if you re-export the tree and want to maximize the number of versions your clients can update from. </p>
<p> <code>always_get_rpm:</code> <code>true|false</code> </p>
<p> Configures whether drpmsync should request that the full rpm is always sent along with the delta. Only makes sense if you have a fast network connection so that applydeltarpm takes longer than transmitting the ful rpm. </p>
<p> <code>deltarpmpath:</code> <i>path</i> </p>
<p> Sets the directory where drpmsync searches for the deltarpm programs. The default is to search the <code>$PATH</code> variable.</p>
<h2>Server Mode</h2>
<p>Drpmsync can wither work as CGI script or as a standalone server. CGI script mode is automatically selected if the <code>REQUEST_METHOD</code> environment variable is set. In this mode drpmsync expects the <code>DRPMSYNC_CONFIG</code> environment variable to contain the path to a server config file. For apache you can set this with the <code>SetEnv</code> directive. </p>
<p> Standalone mode is selected with the <code>-s</code> or <code>-S</code> option. In this mode the server configuration must be specified as an argument to the drpmsync program. The <code>-s</code> option makes the drpmsync program background itself and exit right away, while <code>-S</code> keeps the server in the foreground. </p>
<p> The server configuration can contain the following settings: </p>
<p> <code>allow:</code> <i>pattern1</i> <i>pattern2</i>&#8230;<br />
 <code>deny:</code> <i>pattern1</i> <i>pattern2</i>&#8230; </p>
<p> This provides the access control for the server. <i>pattern</i> can either be a simple glob pattern (only <code>*</code> is supported) or it can be a full regular expression if it is written as <code>/RE/</code>. The regular expression is automatically anchored at the start and the end. Examples are <code>10.10.*</code> or <code>/10\.10\..*/</code> If either the numerical ip address or the domain name of the client matches any entry of the deny list, access is forbidden. Otherwise the allow list is searched for a match. If none is found, access is also denied. The default setting for both lists is empty, so you have to provide an allow list to allow access for the clients. </p>
<p> <code>log:</code> <i>logfile</i> </p>
<p> Specifies the path of a logfile. </p>
<p> <code>no_combine:</code> <code>true|false</code> </p>
<p> If this setting is true the server does not combine deltarpms. This increases to amount of data that has to be transferred but reduces the processor load on the server. </p>
<p> <code>tree:</code> <i>external_path</i> <i>internal_path</i> </p>
<p> This statements exports the tree located at <i>internal_path</i> to the clients as directory <i>external_path</i>. All of the above settings are saved as settings of this particular tree, so different trees can use different configurations. This also means that the configuration directives of a tree must be above the <code>tree</code> statement. </p>
<p> The following settings are global and only needed for standalone mode: </p>
<p> <code>serverlog:</code> <i>logfile</i> </p>
<p> Specifies the path of a logfile used for logging server events. </p>
<p> <code>servername:</code> <i>hostname</i>[:<i>port</i>] </p>
<p> The name of the server. If <i>hostname </i> is empty, the fully qualified domain name is used instead. The port defaults to port 80. </p>
<p> <code>serveraddr:</code> <i>addr</i> </p>
<p> This address is used for binding the server&#8217;s socket. If not specified, connections can come from any interface. </p>
<p> <code>serveruser:</code> <i>user</i><br />
 <code>servergroup:</code> <i>group</i> </p>
<p> Configures the user and group the servers swicthes to after binding the socket to the desired port. Examples are <code>nobody</code> or <code>wwwrun</code>. </p>
<p> <code>maxclients:</code> <i>num</i> </p>
<p> This settings limits the maximum number of concurrent connections to <i>num</i>. The default value is 10 connections. </p>
<p> <code>deltarpmpath:</code> <i>path</i> </p>
<p> Sets the directory where drpmsync searches for the deltarpm programs. The default is to search the <code>$PATH</code> variable.</p>
<h2>Files</h2>
<dl>
<dt><i>dir</i>/drpmsync/deltas</p>
<dd>directory used to store the deltas</p>
<dt><i>dir</i>/drpmsync/lock</p>
<dd>lock used to serialize syncrpm calls</p>
<dt><i>dir</i>/drpmsync/wip</p>
<dd>temporary storing space for the transmitted objects</p>
<dt><i>dir</i>/drpmsync/cache</p>
<dd>md5sum cache to speed up the calculation of the tree state</p>
<dt><i>dir</i>/drpmsync/timstamp</p>
<dd>contains the time of the last finished sync and the last time the remote tree state was requested. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-makedeltarpm/">makedeltarpm</a></code>(8), <code><a href="/docs/linux/man/8-combinedeltarpm/">combinedeltarpm</a></code>(8), <code><a href="/docs/linux/man/8-applydeltarpm/">applydeltarpm</a></code>(8), </p>
<h2>Author</h2>
<p>Michael Schroeder &lt;mls [at] suse.de&gt;</p>
