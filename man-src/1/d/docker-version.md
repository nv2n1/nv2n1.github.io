---
title: "docker-version(1)"
name: "docker-version"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-version/"
description: "docker-version – Show the Docker version information"
---

<h2 class="name">NAME</h2>
<p> docker-version &#8211; Show the Docker version information </p>
<h2>SYNOPSIS</h2>
<p> <code>docker version [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> This command displays version information for both the Docker client and daemon. </p>
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
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Format the output using the given Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for version</p>
<p> <code>&#8211;kubeconfig</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Kubernetes config file</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code> </p>
<h2>Index</h2>
