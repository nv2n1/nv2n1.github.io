---

title: "arcls(1)"
name: "arcls"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcls/"
description: "arcls – list files or directories"
---

<p> The <code>arcls</code> command is used for listing files in grid storage elements and file index catalogues. </p>
<p> <code>arcls [options] url</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;long</code></dt>
<dd> long format (like ls -l). The name of the object is followed by these elements: filetype of object, size in bytes, modification time, checksum and access latency (ONLINE or NEARLINE). The elements for which information is available is protocol-dependent.</dd>
<dt><code>-L</code>, <code>&#8211;locations</code></dt>
<dd> show URLs of file locations (replicas) registered in index services.</dd>
<dt><code>-m</code>, <code>&#8211;metadata</code></dt>
<dd> list all available metadata.</dd>
<dt><code>-r</code>, <code>&#8211;recursive</code></dt>
<dd> operate recursively</dd>
<dt><code>-D</code>, <code>&#8211;depth</code>=<i>level</i></dt>
<dd> operate recursively up to specified level</dd>
<dt><code>-n</code>, <code>&#8211;nolist</code></dt>
<dd> show only description of requested object, do not list content of directories (like ls -d).</dd>
<dt><code>-f</code>, <code>&#8211;forcelist</code></dt>
<dd> treat requested object as directory and always try to list content</dd>
<dt><code>-c</code>, <code>&#8211;checkaccess</code></dt>
<dd> check readability of object. Retrieving and showing information about object is supressed.</dd>
<dt><code>-P</code>, <code>&#8211;listplugins</code></dt>
<dd> list the available plugins (protocols supported)</dd>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>seconds</i></dt>
<dd> timeout in seconds (default 20)</dd>
<dt><code>-z</code>, <code>&#8211;conffile</code>=<i>filename</i></dt>
<dd> configuration file (default ~/.arc/client.conf)</dd>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>debuglevel</i></dt>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> print version information</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> print help </dd>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>url</code></dt>
<dd> the location to list</dd></dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>arcls</code> command lists files and directories on grid storage elements and in file index catalogues. Depending on the installed libraries (check with <code>-P</code> ), the following protocols may be used: file (file:// prefix may be omitted), http, https, httpg, ftp, gsiftp, srm, root.<br />
&nbsp;<wbr> In the case of a directory/fileset, attributes of objects belonging to it will be retrieved, unless <code>&#8211;nolist</code> is specified. </p>
<p> If url starts from &#8216;@&#8217;, the remainder should be a path to a local file containing list of URLs, one per line. Then arcls acts as if it was called multiple times, once for each URL. For more information on ARC URL syntax please read &quot;Protocols, Uniform Resource Locators (URL) and Extensions Supported in ARC&quot; [NORDUGRID-TECH-7] </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></dt>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>X509_USER_PROXY</code></dt>
<dd> The location of the user&#8217;s Grid proxy file. Shouldn&#8217;t be set unless the proxy is in a non-standard location. </dd>
<dt><code>ARC_LOCATION</code></dt>
<dd> The location where ARC is installed can be specified by this variable. If not specified the install location will be determined from the path to the command being executed, and if this fails a WARNING will be given stating the location which will be used. </dd>
<dt><code>ARC_PLUGIN_PATH</code></dt>
<dd> The location of ARC plugins can be specified by this variable. Multiple locations can be specified by separating them by : (; in Windows). The default location is <code>$ARC_LOCATION</code>/lib/arc (\ in Windows). </dd>
</dl>
<h2>EXAMPLE</h2>
<p> arcls -l <a href="gsiftp://example.com/grid/file.dat">gsiftp://example.com/grid/file.dat</a> </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcrename/">arcrename</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), </p>
