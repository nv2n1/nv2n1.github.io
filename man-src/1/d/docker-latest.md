---
title: "docker-latest(1)"
name: "docker-latest"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest/"
description: "docker – Docker image and container command line interface"
---

<h2 class="name">NAME</h2>
<p> docker &#8211; Docker image and container command line interface </p>
<h2>SYNOPSIS</h2>
<p> <code>docker</code> [OPTIONS] COMMAND [arg&#8230;] </p>
<p> <code>docker</code> daemon [&#8211;help|&#8230;] </p>
<p> <code>docker</code> [&#8211;help|-v|&#8211;version] </p>
<h2>DESCRIPTION</h2>
<p> is a client for interacting with the daemon (see <code><a href="/docs/linux/man/8-dockerd/">dockerd</a>(8)</code>) through the CLI. </p>
<p> The Docker CLI has over 30 commands. The commands are listed below and each has its own man page which explain usage and arguments. </p>
<p> To see the man page for a command run <code>man docker &lt;command&gt;</code>. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;config</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>Specifies the location of the Docker client configuration files. The default is&nbsp;<wbr>&#8216;~/.docker&#8217;. </p>
<p> <code>-D</code>, <code>&#8211;debug</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>Enable debug mode. Default is false. </p>
<p> <code>-H</code>, <code>&#8211;host</code>=[<i><a href="unix:///var/run/docker.sock">unix:///var/run/docker.sock</a></i>]: <a href="tcp://[host]:[port][path]">tcp://[host]:[port][path]</a> to bind or <a href="unix://[/path/to/socket]">unix://[/path/to/socket]</a> to use.<br />
&nbsp;<wbr>&nbsp;<wbr>The socket(s)&nbsp;<wbr>to bind to in daemon mode specified using one or more<br />
&nbsp;<wbr>&nbsp;<wbr><a href="tcp://host:port/path,">tcp://host:port/path,</a>&nbsp;<wbr><a href="unix:///path/to/socket,">unix:///path/to/socket,</a>&nbsp;<wbr>fd://*&nbsp;<wbr>or fd://socketfd.<br />
&nbsp;<wbr>&nbsp;<wbr>If the tcp port is not specified, then it will default to either 2375 when<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;tls is off, or 2376 when &#8211;tls is on, or &#8211;tlsverify is specified. </p>
<p> <code>-l</code>, <code>&#8211;log-level</code>=&quot;<i>debug</i>|<i>info</i>|<i>warn</i>|<i>error</i>|<i>fatal</i>&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>Set the logging level. Default is info. </p>
<p> <code>&#8211;tls</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>Use TLS;&nbsp;<wbr>implied by &#8211;tlsverify. Default is false. </p>
<p> <code>&#8211;tlscacert</code>=<i>~/.docker/ca.pem</i><br />
&nbsp;<wbr>&nbsp;<wbr>Trust certs signed only by this CA. </p>
<p> <code>&#8211;tlscert</code>=<i>~/.docker/cert.pem</i><br />
&nbsp;<wbr>&nbsp;<wbr>Path to TLS certificate file. </p>
<p> <code>&#8211;tlskey</code>=<i>~/.docker/key.pem</i><br />
&nbsp;<wbr>&nbsp;<wbr>Path to TLS key file. </p>
<p> <code>&#8211;tlsverify</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>Use TLS and verify the remote&nbsp;<wbr>(daemon: verify client, client: verify daemon).<br />
&nbsp;<wbr>&nbsp;<wbr>Default is false. </p>
<p> <code>-v</code>, <code>&#8211;version</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>Print version information and quit. Default is false. </p>
<h2>COMMANDS</h2>
<p> <code>attach</code><br />
&nbsp;<wbr>&nbsp;<wbr>Attach to a running container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-attach/">docker-attach</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>attach</code>&nbsp;<wbr>command. </p>
<p> <code>build</code><br />
&nbsp;<wbr>&nbsp;<wbr>Build an image from a Dockerfile<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-build/">docker-build</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>build</code>&nbsp;<wbr>command. </p>
<p> <code>commit</code><br />
&nbsp;<wbr>&nbsp;<wbr>Create a new image from a container&#8217;s changes<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-commit/">docker-commit</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>commit</code>&nbsp;<wbr>command. </p>
<p> <code>cp</code><br />
&nbsp;<wbr>&nbsp;<wbr>Copy files/folders between a container and the local filesystem<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-cp/">docker-cp</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>cp</code>&nbsp;<wbr>command. </p>
<p> <code>create</code><br />
&nbsp;<wbr>&nbsp;<wbr>Create a new container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-create/">docker-create</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>create</code>&nbsp;<wbr>command. </p>
<p> <code>diff</code><br />
&nbsp;<wbr>&nbsp;<wbr>Inspect changes on a container&#8217;s filesystem<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-diff/">docker-diff</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>diff</code>&nbsp;<wbr>command. </p>
<p> <code>events</code><br />
&nbsp;<wbr>&nbsp;<wbr>Get real time events from the server<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-events/">docker-events</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>events</code>&nbsp;<wbr>command. </p>
<p> <code>exec</code><br />
&nbsp;<wbr>&nbsp;<wbr>Run a command in a running container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-exec/">docker-exec</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>exec</code>&nbsp;<wbr>command. </p>
<p> <code>export</code><br />
&nbsp;<wbr>&nbsp;<wbr>Stream the contents of a container as a tar archive<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-export/">docker-export</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>export</code>&nbsp;<wbr>command. </p>
<p> <code>history</code><br />
&nbsp;<wbr>&nbsp;<wbr>Show the history of an image<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-history/">docker-history</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>history</code>&nbsp;<wbr>command. </p>
<p> <code>images</code><br />
&nbsp;<wbr>&nbsp;<wbr>List images<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-images/">docker-images</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>images</code>&nbsp;<wbr>command. </p>
<p> <code>import</code><br />
&nbsp;<wbr>&nbsp;<wbr>Create a new filesystem image from the contents of a tarball<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-import/">docker-import</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>import</code>&nbsp;<wbr>command. </p>
<p> <code>info</code><br />
&nbsp;<wbr>&nbsp;<wbr>Display system-wide information<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-info/">docker-info</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>info</code>&nbsp;<wbr>command. </p>
<p> <code>inspect</code><br />
&nbsp;<wbr>&nbsp;<wbr>Return low-level information on a container or image<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-inspect/">docker-inspect</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>inspect</code>&nbsp;<wbr>command. </p>
<p> <code>kill</code><br />
&nbsp;<wbr>&nbsp;<wbr>Kill a running container&nbsp;<wbr>(which includes the wrapper process and everything inside it)<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-kill/">docker-kill</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>kill</code>&nbsp;<wbr>command. </p>
<p> <code>load</code><br />
&nbsp;<wbr>&nbsp;<wbr>Load an image from a tar archive<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-load/">docker-load</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>load</code>&nbsp;<wbr>command. </p>
<p> <code>login</code><br />
&nbsp;<wbr>&nbsp;<wbr>Log in to a Docker Registry<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-login/">docker-login</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>login</code>&nbsp;<wbr>command. </p>
<p> <code>logout</code><br />
&nbsp;<wbr>&nbsp;<wbr>Log the user out of a Docker Registry<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-logout/">docker-logout</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>logout</code>&nbsp;<wbr>command. </p>
<p> <code>logs</code><br />
&nbsp;<wbr>&nbsp;<wbr>Fetch the logs of a container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-logs/">docker-logs</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>logs</code>&nbsp;<wbr>command. </p>
<p> <code>pause</code><br />
&nbsp;<wbr>&nbsp;<wbr>Pause all processes within a container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-pause/">docker-pause</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>pause</code>&nbsp;<wbr>command. </p>
<p> <code>port</code><br />
&nbsp;<wbr>&nbsp;<wbr>Lookup the public-facing port which is NAT-ed to PRIVATE_PORT<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-port/">docker-port</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>port</code>&nbsp;<wbr>command. </p>
<p> <code>ps</code><br />
&nbsp;<wbr>&nbsp;<wbr>List containers<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-ps/">docker-ps</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>ps</code>&nbsp;<wbr>command. </p>
<p> <code>pull</code><br />
&nbsp;<wbr>&nbsp;<wbr>Pull an image or a repository from a Docker Registry<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-pull/">docker-pull</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>pull</code>&nbsp;<wbr>command. </p>
<p> <code>push</code><br />
&nbsp;<wbr>&nbsp;<wbr>Push an image or a repository to a Docker Registry<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-push/">docker-push</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>push</code>&nbsp;<wbr>command. </p>
<p> <code>rename</code><br />
&nbsp;<wbr>&nbsp;<wbr>Rename a container.<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-rename/">docker-rename</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>rename</code>&nbsp;<wbr>command. </p>
<p> <code>restart</code><br />
&nbsp;<wbr>&nbsp;<wbr>Restart a container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-restart/">docker-restart</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>restart</code>&nbsp;<wbr>command. </p>
<p> <code>rm</code><br />
&nbsp;<wbr>&nbsp;<wbr>Remove one or more containers<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-rm/">docker-rm</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>rm</code>&nbsp;<wbr>command. </p>
<p> <code>rmi</code><br />
&nbsp;<wbr>&nbsp;<wbr>Remove one or more images<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-rmi/">docker-rmi</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>rmi</code>&nbsp;<wbr>command. </p>
<p> <code>run</code><br />
&nbsp;<wbr>&nbsp;<wbr>Run a command in a new container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-run/">docker-run</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>run</code>&nbsp;<wbr>command. </p>
<p> <code>save</code><br />
&nbsp;<wbr>&nbsp;<wbr>Save an image to a tar archive<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-save/">docker-save</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>save</code>&nbsp;<wbr>command. </p>
<p> <code>search</code><br />
&nbsp;<wbr>&nbsp;<wbr>Search for an image in the Docker index<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-search/">docker-search</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>search</code>&nbsp;<wbr>command. </p>
<p> <code>start</code><br />
&nbsp;<wbr>&nbsp;<wbr>Start a container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-start/">docker-start</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>start</code>&nbsp;<wbr>command. </p>
<p> <code>stats</code><br />
&nbsp;<wbr>&nbsp;<wbr>Display a live stream of one or more containers&#8217;&nbsp;<wbr>resource usage statistics<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-stats/">docker-stats</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>stats</code>&nbsp;<wbr>command. </p>
<p> <code>stop</code><br />
&nbsp;<wbr>&nbsp;<wbr>Stop a container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-stop/">docker-stop</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>stop</code>&nbsp;<wbr>command. </p>
<p> <code>tag</code><br />
&nbsp;<wbr>&nbsp;<wbr>Tag an image into a repository<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-tag/">docker-tag</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>tag</code>&nbsp;<wbr>command. </p>
<p> <code>top</code><br />
&nbsp;<wbr>&nbsp;<wbr>Lookup the running processes of a container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-top/">docker-top</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>top</code>&nbsp;<wbr>command. </p>
<p> <code>unpause</code><br />
&nbsp;<wbr>&nbsp;<wbr>Unpause all processes within a container<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-unpause/">docker-unpause</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>unpause</code>&nbsp;<wbr>command. </p>
<p> <code>version</code><br />
&nbsp;<wbr>&nbsp;<wbr>Show the Docker version information<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-version/">docker-version</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>version</code>&nbsp;<wbr>command. </p>
<p> <code>wait</code><br />
&nbsp;<wbr>&nbsp;<wbr>Block until a container stops, then print its exit code<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><code><a href="/docs/linux/man/1-docker-wait/">docker-wait</a>(1)</code>&nbsp;<wbr>for full documentation on the&nbsp;<wbr><code>wait</code>&nbsp;<wbr>command. </p>
<h2>RUNTIME EXECUTION OPTIONS</h2>
<p> Use the <code>&#8211;exec-opt</code> flags to specify options to the execution driver. The following options are available: </p>
<h3>native.cgroupdriver</h3>
<p> Specifies the management of the container&#8217;s cgroups. You can specify cgroupfs or systemd. If you specify systemd and it is not available, the system errors out. </p>
<h3>Client</h3>
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
