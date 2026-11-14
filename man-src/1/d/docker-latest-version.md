---
title: "docker-latest-version(1)"
name: "docker-latest-version"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-version/"
description: "docker-version – Show the Docker version information."
---

<h2 class="name">NAME</h2>
<p> docker-version &#8211; Show the Docker version information. </p>
<h2>SYNOPSIS</h2>
<p> <code>docker version</code> [<code>&#8211;help</code>] [<code>-f</code>|<code>&#8211;format</code>[=<i>FORMAT</i>]] </p>
<h2>DESCRIPTION</h2>
<p> This command displays version information for both the Docker client and daemon. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>Print usage statement </p>
<p> <code>-f</code>, <code>&#8211;format</code>=&quot;&quot;<br />
&nbsp;<wbr>Format the output using the given go template. </p>
<h2>EXAMPLES</h2>
<h2>Display Docker version information</h2>
<p> The default output: </p>
<dl>
<dt>
<dd>
<pre>
$ docker version
Client:
 Version:      1.8.0
 API version:  1.20
 Go version:   go1.4.2
 Git commit:   f5bae0a
 Built:        Tue Jun 23 17:56:00 UTC 2015
 OS/Arch:      linux/amd64
Server:
 Version:      1.8.0
 API version:  1.20
 Go version:   go1.4.2
 Git commit:   f5bae0a
 Built:        Tue Jun 23 17:56:00 UTC 2015
 OS/Arch:      linux/amd64
</pre>
</dl>
<p> Get server version: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker version-- format '&#123;&#123;.Server.Version}}' 1.8.0
</code></pre>
</dl>
<p> Dump raw data: </p>
<p> To view all available fields, you can use the format &#123;&#123;json .}}. </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker version-- format '&#123;&#123;json .}}'
{
    "Client" : {"Version" : "1.8.0", "ApiVersion" : "1.20", "GitCommit" : "f5bae0a", "GoVersion" : "go1.4.2", "Os" : "linux", "Arch" : "amd64", "BuildTime" : "Tue Jun 23 17:56:00 UTC 2015"}, "ServerOK" : true, "Server":
    {
        "Version" : "1.8.0", "ApiVersion" : "1.20", "GitCommit" : "f5bae0a", "GoVersion" : "go1.4.2", "Os" : "linux", "Arch" : "amd64", "KernelVersion" : "3.13.2-gentoo", "BuildTime" : "Tue Jun 23 17:56:00 UTC 2015"
    }
}
</code></pre>
</dl>
<h2>HISTORY</h2>
<p> June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; June 2015, updated by John Howard &lt;jhoward [at] microsoft.com&gt; June 2015, updated by Patrick Hemmer &lt;patrick.hemmer [at] gmail.com </p>
<h2>Index</h2>
