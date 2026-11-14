---
title: "docker(1)"
name: "docker"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker/"
description: "docker – Docker image and container command line interface"
---

<h2 class="name">NAME</h2>
<p> docker &#8211; Docker image and container command line interface </p>
<h2>SYNOPSIS</h2>
<p> <code>docker</code> [OPTIONS] COMMAND [ARG&#8230;] </p>
<p> <code>docker</code> [&#8211;help|-v|&#8211;version] </p>
<h2>DESCRIPTION</h2>
<p> <code>docker</code> is a client for interacting with the daemon (see <code><a href="/docs/linux/man/8-dockerd/">dockerd</a>(8)</code>) through the CLI. </p>
<p> The Docker CLI has over 30 commands. The commands are listed below and each has its own man page which explain usage and arguments. </p>
<p> To see the man page for a command run <code>man docker </code>. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;Print usage statement </p>
<p> <code>&#8211;config</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;Specifies the location of the Docker client configuration files. The default is&nbsp;&#8216;~/.docker&#8217;. </p>
<p> <code>-D</code>, <code>&#8211;debug</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Enable debug mode. Default is false. </p>
<p> <code>-H</code>, <code>&#8211;host</code>=[<i><a href="unix:///var/run/docker.sock">unix:///var/run/docker.sock</a></i>]: <a href="tcp://[host]:[port][path]">tcp://[host]:[port][path]</a> to bind or <a href="unix://[/path/to/socket]">unix://[/path/to/socket]</a> to use.<br />
&nbsp;<wbr>&nbsp;The socket(s)&nbsp;to bind to in daemon mode specified using one or more<br />
&nbsp;<wbr>&nbsp;<a href="tcp://host:port/path,">tcp://host:port/path,</a>&nbsp;<a href="unix:///path/to/socket,">unix:///path/to/socket,</a>&nbsp;fd://*&nbsp;or fd://socketfd.<br />
&nbsp;<wbr>&nbsp;If the tcp port is not specified, then it will default to either 2375 when<br />
&nbsp;<wbr>&nbsp;&#8211;tls is off, or 2376 when &#8211;tls is on, or &#8211;tlsverify is specified. </p>
<p> <code>-l</code>, <code>&#8211;log-level</code>=&quot;<i>debug</i>|<i>info</i>|<i>warn</i>|<i>error</i>|<i>fatal</i>&quot;<br />
&nbsp;<wbr>&nbsp;Set the logging level. Default is info. </p>
<p> <code>&#8211;tls</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Use TLS;&nbsp;implied by &#8211;tlsverify. Default is false. </p>
<p> <code>&#8211;tlscacert</code>=<i>~/.docker/ca.pem</i><br />
&nbsp;<wbr>&nbsp;Trust certs signed only by this CA. </p>
<p> <code>&#8211;tlscert</code>=<i>~/.docker/cert.pem</i><br />
&nbsp;<wbr>&nbsp;Path to TLS certificate file. </p>
<p> <code>&#8211;tlskey</code>=<i>~/.docker/key.pem</i><br />
&nbsp;<wbr>&nbsp;Path to TLS key file. </p>
<p> <code>&#8211;tlsverify</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Use TLS and verify the remote&nbsp;(daemon: verify client, client: verify daemon).<br />
&nbsp;<wbr>&nbsp;Default is false. </p>
<p> <code>-v</code>, <code>&#8211;version</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;Print version information and quit. Default is false. </p>
<h2>COMMANDS</h2>
<p> Use &quot;docker help&quot; or &quot;docker &#8211;help&quot; to get an overview of available commands. </p>
<h2>EXAMPLES</h2>
<p> For specific client examples please see the man page for the specific Docker command. For example: </p>
<dl>
<dt>
<dd>
<pre>
man docker-run
</pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. </p>
<h2>Index</h2>
