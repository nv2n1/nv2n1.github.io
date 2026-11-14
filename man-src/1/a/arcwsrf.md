---
title: "arcwsrf(1)"
name: "arcwsrf"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcwsrf/"
description: "arcwsrf – run WSRF query against service"
---

<h2 class="name">NAME</h2>
<p> arcwsrf &#8211; run WSRF query against service</p>
<h2>DESCRIPTION</h2>
<p> The <code>arcwsrf</code> command issues WSRF resource property query to service specified by its URL. </p>
<h2>SYNOPSIS</h2>
<p> <code>arcwsrf [options] service_url [query]</code> </p>
<h2>OPTIONS</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help options<br />
&nbsp;<wbr>&nbsp;<wbr>-p, &#8211;property=[-]name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Request for specific Resource Property<br />
&nbsp;<wbr>&nbsp;<wbr>-t, &#8211;timeout=seconds&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>timeout in seconds&nbsp;<wbr>(default 20)<br />
&nbsp;<wbr>&nbsp;<wbr>-z, &#8211;conffile=filename&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>configuration file&nbsp;<wbr>(default&nbsp;<wbr>~/.arc/client.conf)<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;debug=debuglevel&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG<br />
&nbsp;<wbr>&nbsp;<wbr>-v, &#8211;version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print version information </p>
<dl>
<dt><code>-p</code>, <code>&#8211;property</code></p>
<dd> request specific Resource Property.</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd> timeout in seconds (default 20)</p>
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
<dt><code>service_url</code></p>
<dd> URL of service to which request is sent</p>
<dt><code>query</code></p>
<dd> query expression (usually XPath) to be sent</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>arcwsrf</code> send WSRF query to specified service URL and prints response. If query is provided this query is sent to service. Otherwise request for whole information document or for selected properties (if -p options are specified) is made. </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></p>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>X509_USER_PROXY</code></p>
<dd> The location of the user&#8217;s grid proxy file. Shouldn&#8217;t be set unless the proxy is in a non-standard location. </p>
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
<p> <code><a href="/docs/linux/man/1-arcinfo/">arcinfo</a></code>(1) </p>
<h2>Index</h2>
