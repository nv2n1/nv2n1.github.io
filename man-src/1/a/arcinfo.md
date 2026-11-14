---
title: "arcinfo(1)"
name: "arcinfo"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcinfo/"
description: "arcinfo – ARC Info"
---

<h2 class="name">NAME</h2>
<p> arcinfo &#8211; ARC Info</p>
<h2>DESCRIPTION</h2>
<p> The <code>arcinfo</code> command is used for obtaining status and information of clusters on the grid. </p>
<h2>SYNOPSIS</h2>
<p> <code>arcinfo [options] [cluster &#8230;]</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;cluster</code>=<i>name</i></p>
<dd> select one or more computing elements: <i>name</i> can be an alias for a single CE, a group of CEs or a URL</p>
<dt><code>-I</code>, <code>&#8211;infointerface</code>=<i>InterfaceName</i></p>
<dd> the computing element specified by URL at the command line should be queried using this information interface (possible options: org.nordugrid.ldapng, org.nordugrid.ldapglue2, org.nordugrid.wsrfglue2, org.ogf.glue.emies.resourceinfo)</p>
<dt><code>-g</code>, <code>&#8211;index</code>=<i>name</i></p>
<dd> select one or more registries: <i>name</i> can be an alias for a single registry, a group of registries or a URL</p>
<dt><code>-R</code>, <code>&#8211;rejectdiscovery</code>=<i>URL</i></p>
<dd> skip the service with the given URL during service discovery</p>
<dt><code>-S</code>, <code>&#8211;submissioninterface</code>=<i>InterfaceName</i></p>
<dd> only get information about executon targets which supports this job submission interface (e.g. org.nordugrid.gridftpjob, org.ogf.glue.emies.activitycreation, org.nordugrid.xbes)</p>
<dt><code>-l</code>, <code>&#8211;long</code></p>
<dd> long format (more information)</p>
<dt><code>-L</code>, <code>&#8211;list-configured-services</code></p>
<dd> print a list of services configured in the client.conf</p>
<dt><code>-P</code>, <code>&#8211;listplugins</code></p>
<dd> list the available plugins</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd> timeout in seconds (default 20)</p>
<dt><code>-z</code>, <code>&#8211;conffile</code>=<i>filename</i></p>
<dd> configuration file (default ~/.arc/client.conf)</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>debuglevel</i></p>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> print version information</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> print help</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>arcinfo</code> command is used to get the status and information of clusters and queues available on the grid. You can specify the URLs of cluster with the <code>&#8211;cluster</code> option, or by just listing them as arguments. The <code>&#8211;index</code> flag can be used to specify an index server which should be queried for clusters. Both of these flags take a service endpoint as argument. See <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) for a discussion of this format. </p>
<p> Detailed information about queried computing services can be obtained by specifying the <code>&#8211;long</code> flag. </p>
<p> When specifying the <code>&#8211;index</code> flag, the information about the computing services registered at the index server will be queried rather than the status of the index server itself. Currently no command exists to query a index server. </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></p>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>X509_USER_PROXY</code></p>
<dd> The location of the user&#8217;s Grid proxy file. Shouldn&#8217;t be set unless the proxy is in a non-standard location. Note that this could also be set in the client configuration file, however the environment variable overrides the settings in configuration. </p>
<dt><code>ARC_LOCATION</code></p>
<dd> The location where ARC is installed can be specified by this variable. If not specified the install location will be determined from the path to the command being executed, and if this fails a WARNING will be given stating the location which will be used. </p>
<dt><code>ARC_PLUGIN_PATH</code></p>
<dd> The location of ARC plugins can be specified by this variable. Multiple locations can be specified by separating them by : (; in Windows). The default location is <code>$ARC_LOCATION</code>/lib/arc (\ in Windows). </p>
</dl>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arccat/">arccat</a></code>(1), <code><a href="/docs/linux/man/1-arcclean/">arcclean</a></code>(1), <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcget/">arcget</a></code>(1), <code><a href="/docs/linux/man/1-arckill/">arckill</a></code>(1), <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcproxy/">arcproxy</a></code>(1), <code><a href="/docs/linux/man/1-arcrenew/">arcrenew</a></code>(1), <code><a href="/docs/linux/man/1-arcresub/">arcresub</a></code>(1), <code><a href="/docs/linux/man/1-arcresume/">arcresume</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1), <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1), <code><a href="/docs/linux/man/1-arcsync/">arcsync</a></code>(1), <code><a href="/docs/linux/man/1-arctest/">arctest</a></code>(1) </p>
<h2>Index</h2>
