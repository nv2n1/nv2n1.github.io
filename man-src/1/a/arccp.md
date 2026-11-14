---
title: "arccp(1)"
name: "arccp"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arccp/"
description: "arccp – copy files"
---

<h2 class="name">NAME</h2>
<p> arccp &#8211; copy files</p>
<h2>DESCRIPTION</h2>
<p> The <code>arccp</code> command copies files to, from and between grid storage elements. </p>
<h2>SYNOPSIS</h2>
<p> <code>arccp [options] source destination</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;passive</code></p>
<dd> use passive transfer (off by default if secure is on, on by default if secure is not requested)</p>
<dt><code>-n</code>, <code>&#8211;nopassive</code></p>
<dd> do not try to force passive transfer</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> if the destination is an indexing service and not the same as the source and the destination is already registered, then the copy is normally not done. However, if this option is specified the source is assumed to be a replica of the destination created in an uncontrolled way and the copy is done like in case of replication. Using this option also skips validation of completed transfers.</p>
<dt><code>-i</code>, <code>&#8211;indicate</code></p>
<dd> show progress indicator. Using this option forces a check of the source file before trying to transfer it, in order to find its size. Depending on other information obtained about the source, there may be side-effects of using this option, for example checksum verification or pre-staging data from tape.</p>
<dt><code>-T</code>, <code>&#8211;notransfer</code></p>
<dd> do not transfer, but register source into destination. destination must be a meta-url. If destination already exists then meta-information of source must match meta-information of destination. This can be overridden using the &#8211;force option.</p>
<dt><code>-3</code>, <code>&#8211;thirdparty</code></p>
<dd> perform third party transfer, where the destination pulls from the source (only available with GFAL plugin)</p>
<dt><code>-u</code>, <code>&#8211;secure</code></p>
<dd> use secure transfer (insecure by default)</p>
<dt><code>-y</code>, <code>&#8211;cache</code>=<i>path</i></p>
<dd> path to local cache (use to put file into cache)</p>
<dt><code>-r</code>, <code>&#8211;recursive</code></p>
<dd> operate recursively</p>
<dt><code>-D</code>, <code>&#8211;depth</code>=<i>level</i></p>
<dd> operate recursively up to specified level</p>
<dt><code>-R</code>, <code>&#8211;retries</code>=<i>number</i></p>
<dd> number of retries before failing file transfer</p>
<dt><code>-L</code>, <code>&#8211;location</code>=<i>URL</i></p>
<dd> physical file to write to when destination is an indexing service. Must be specified for indexing services which do not automatically generate physical locations. Can be specified multiple times &#8211; locations will be tried in order until one succeeds.</p>
<dt><code>-P</code>, <code>&#8211;listplugins</code></p>
<dd> list the available plugins (protocols supported)</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd> timeout in seconds (default 20). This timeout applies to connections to remote services and indicates the maximum allowed idle time of the transfer.</p>
<dt><code>-z</code>, <code>&#8211;conffile</code>=<i>filename</i></p>
<dd> configuration file (default ~/.arc/client.conf)</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>debuglevel</i></p>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> print version information</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> print help </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>source</code></p>
<dd> the source of the transfer</p>
<dt><code>destination</code></p>
<dd> the destination of the transfer</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>arccp</code> command copies files to, from and between grid storage elements. It can also be used to register files in file index catalogues, either automatically as the result of a file transfer, or by using the <code>&#8211;notransfer</code> option. For more information on ARC URL syntax please read &quot;Protocols, Uniform Resource Locators (URL) and Extensions Supported in ARC&quot; [NORDUGRID-TECH-7]. </p>
<p> If <code>source</code> and/or <code>destination</code> start from &#8216;@&#8217;, the remaining argument is assumed to be a path to a local file containing a list of URLs, one per line. In this case <code>arccp</code> performs like it were called multiple times &#8211; once for every URL. </p>
<p> When copying directories both the source and destination must end with the directory separator character and a recursion option <code>-r</code> or <code>-D</code> must be specified. </p>
<p> All data transfer goes through the machine of the caller of arccp, even in the case of two remote endpoints, unless the <code>&#8211;thirdparty</code> option is used. With this option credentials are delegated to the destination and it pulls the data directly from the source. The timeout option in this case applies to the entire transfer itself and default timeouts are used for connections to the remote endpoints. Note that third-party transfer is only possible if the GFAL2 plugin is installed. </p>
<p> Depending on the installed libraries (check with <code>-P</code> ), the following protocols may be used: file (file:// prefix may be omitted), http, https, httpg, ftp, gsiftp, srm, root. To connect source or destination to standard input/output use &#8216;-&#8216; instead of URL. </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></p>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </p>
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
<h2>EXAMPLE</h2>
<p> arccp -i <a href="gsiftp://example.com/grid/file1.dat">gsiftp://example.com/grid/file1.dat</a> /tmp/file1.dat </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcrename/">arcrename</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), </p>
<h2>Index</h2>
