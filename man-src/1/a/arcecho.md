---
title: "arcecho(1)"
name: "arcecho"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcecho/"
description: "arcecho – ARC echo client"
---

<h2 class="name">NAME</h2>
<p> arcecho &#8211; ARC echo client</p>
<h2>DESCRIPTION</h2>
<p> The <code>arcecho</code> command is a client for the ARC echo service. </p>
<h2>SYNOPSIS</h2>
<p> <code>arcecho [options] service message</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-z</code>, <code>&#8211;conffile</code>=<i>filename</i></p>
<dd> configuration file (default ~/.arc/client.conf)</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>debuglevel</i></p>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> print version information</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> print help</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>service</code></p>
<dd> A URL to an ARC echo service</p>
<dt><code>message</code></p>
<dd> The message the service should return</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> <code>arcecho</code> is a simple test tool: we can send a message to the echo service and it will respond with the same message. </p>
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
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>Index</h2>
