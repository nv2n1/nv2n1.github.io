---
title: "arcsync(1)"
name: "arcsync"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcsync/"
description: "arcsync – ARC Synchronize"
---

<h2 class="name">NAME</h2>
<p> arcsync &#8211; ARC Synchronize</p>
<h2>DESCRIPTION</h2>
<p> The <code>arcsync</code> command synchronizes your local jobs list with the information at a given cluster or index server. </p>
<h2>SYNOPSIS</h2>
<p> <code>arcsync [options]</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;cluster</code>=<i>name</i></p>
<dd> select one or more computing elements: <i>name</i> can be an alias for a single CE, a group of CEs or a URL</p>
<dt><code>-g</code>, <code>&#8211;index</code>=<i>name</i></p>
<dd> select one or more registries: <i>name</i> can be an alias for a single registry, a group of registries or a URL</p>
<dt><code>-j</code>, <code>&#8211;joblist</code>=<i>filename</i></p>
<dd> the file storing information about active jobs (default ~/.arc/jobs.xml)</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> don&#8217;t ask for verification</p>
<dt><code>-T</code>, <code>&#8211;truncate</code></p>
<dd> shrinks the joblist before synchronizing</p>
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
<p> The ARC user interface keeps a local list of active jobs in the users home directory (see <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1)). If this file is lost, or the user wants to recreate the file on a different computer,the <code>arcsync</code> command can be used to recreate the file from the information available the specified cluster or index server. </p>
<p> Since the information about a job retrieved from a cluster can be slightly out of date if the user very recently submitted or removed a job a warning is issued when this command is run. The <code>&#8211;force</code> option disables this warning. </p>
<p> The <code>&#8211;cluster</code> options can be used to select or reject clusters that should be considered in the synchronization. This options can be repeated several times. See <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) for a discussion of the format of arguments to this option. </p>
<p> If the joblist is not empty when invoking synchronization the old jobs will be merged with the new jobs, unless the <code>&#8211;truncate</code> option is given, in which case the joblist will first be cleaned of old jobs and then the new jobs will be added. </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></p>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </p>
<dt><code>~/.arc/jobs.xml</code></p>
<dd> This is a local list of the user&#8217;s active jobs. When a job is successfully submitted it is added to this list and when it is removed from the remote cluster it is removed from this list. This list is used as the list of all active jobs when the user specifies the <code>&#8211;all</code> option to the various NorduGrid ARC user interface commands. By using the <code>&#8211;joblist</code> option a different file can be used than the default. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>X509_USER_PROXY</code></p>
<dd> The location of the user&#8217;s Grid proxy file. Shouldn&#8217;t be set unless the proxy is in a non-standard location. </p>
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
<p> <code><a href="/docs/linux/man/1-arccat/">arccat</a></code>(1), <code><a href="/docs/linux/man/1-arcclean/">arcclean</a></code>(1), <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcget/">arcget</a></code>(1), <code><a href="/docs/linux/man/1-arcinfo/">arcinfo</a></code>(1), <code><a href="/docs/linux/man/1-arckill/">arckill</a></code>(1), <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcproxy/">arcproxy</a></code>(1), <code><a href="/docs/linux/man/1-arcrenew/">arcrenew</a></code>(1), <code><a href="/docs/linux/man/1-arcresub/">arcresub</a></code>(1), <code><a href="/docs/linux/man/1-arcresume/">arcresume</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1), <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1), <code><a href="/docs/linux/man/1-arctest/">arctest</a></code>(1) </p>
<h2>Index</h2>
