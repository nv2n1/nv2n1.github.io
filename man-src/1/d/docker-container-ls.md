---
title: "docker-container-ls(1)"
name: "docker-container-ls"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-ls/"
description: "docker-container-ls – List containers"
---

<h2 class="name">NAME</h2>
<p> docker-container-ls &#8211; List containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container ls [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> List the containers in the local repository. By default this shows only the running containers. </p>
<h2>Filters</h2>
<p> Filter output based on these conditions:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; ancestor=([:tag]||image [at] digest &lt;mailto:image [at] digest&gt;)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;containers created from an image or a descendant.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; before=(|)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; expose=([/]|/[])<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; exited=&nbsp;an exit code of&nbsp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; health=(starting|healthy|unhealthy|none)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; id=&nbsp;a container&#8217;s ID<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; isolation=(default|process|hyperv)&nbsp;(Windows daemon only)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; is-task=(true|false)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; label=&nbsp;or label==<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; name=&nbsp;a container&#8217;s name<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; network=(|)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; publish=([/]|/[])<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; since=(|)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; status=(created|restarting|removing|running|paused|exited)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; volume=(|) </p>
<h2>Format</h2>
<p> The formatting option (<code>&#8211;format</code>) pretty-prints container output using a Go template. </p>
<p> Valid placeholders for the Go template are listed below:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Container ID.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Image&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Image ID.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Command&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Quoted command.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .CreatedAt&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Time when the container was created.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .RunningFor&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Elapsed time since the container was started.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Ports&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Exposed ports.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Status&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Container status.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Container disk size.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Names&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Container names.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Labels&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; All labels assigned to the container.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Label&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Value of a specific label for this container.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;For example&nbsp;<code>&#8216;&#123;&#123;.Label&nbsp;&quot;com.docker.swarm.cpu&quot;}}&#8217;</code>.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Mounts&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Names of the volumes mounted in this container.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; .Networks&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; Names of the networks attached to this container. </p>
<h2>EXAMPLES</h2>
<h2>Display all containers, including non-running</h2>
<dl>
<dt>
<dd>
<pre>
$ docker container ls -a
CONTAINER ID        IMAGE                 COMMAND                CREATED             STATUS      PORTS    NAMES
a87ecb4f327c        fedora:20             /bin/sh -c #(nop) MA   20 minutes ago      Exit 0               desperate_brattain
01946d9d34d8        vpavlin/rhel7:latest  /bin/sh -c #(nop) MA   33 minutes ago      Exit 0               thirsty_bell
c1d3b0166030        acffc0358b9e          /bin/sh -c yum -y up   2 weeks ago         Exit 1               determined_torvalds
41d50ecd2f57        fedora:20             /bin/sh -c #(nop) MA   2 weeks ago         Exit 0               drunk_pike
</pre>
</dl>
<h2>Display only IDs of all containers, including non-running</h2>
<dl>
<dt>
<dd>
<pre>
$ docker container ls -a -q
a87ecb4f327c
01946d9d34d8
c1d3b0166030
41d50ecd2f57
</pre>
</dl>
<h2>Display only IDs of all containers that have the name determined_torvalds</h2>
<dl>
<dt>
<dd>
<pre>
$ docker container ls -a -q --filter=name=determined_torvalds
c1d3b0166030
</pre>
</dl>
<h2>Display containers with their commands</h2>
<dl>
<dt>
<dd>
<pre><code>
$ docker container ls-- format "&#123;&#123;.ID}}: &#123;&#123;.Command}}" a87ecb4f327c : / bin / sh - c #(nop)MA 01946d9d34d8 : / bin / sh - c #(nop)MA c1d3b0166030 : / bin / sh - c yum - y up 41d50ecd2f57 : / bin / sh - c #(nop)MA
</code></pre>
</dl>
<h2>Display containers with their labels in a table</h2>
<dl>
<dt>
<dd>
<p>$ docker container ls&#8211; format &#8220;table &#123;&#123;.ID}}	&#123;&#123;.Labels}}&#8221; CONTAINER ID LABELS<br />
    a87ecb4f327c com.docker.swarm.node = ubuntu,<br />
                 com.docker.swarm.storage = ssd 01946d9d34d8 c1d3b0166030 com.docker.swarm.node = debian, com.docker.swarm.cpu = 6 41d50ecd2f57 com.docker.swarm.node = fedora, com.docker.swarm.cpu = 3, com.docker.swarm.storage = ssd
</dl>
<h2>Display containers with their node label in a table</h2>
<dl>
<dt>
<dd>
<p>$ docker container ls&#8211; format &#8216;table &#123;&#123;.ID}}	&#123;&#123;(.Label &#8220;com.docker.swarm.node&#8221;)}}&#8217; CONTAINER ID NODE<br />
    a87ecb4f327c ubuntu 01946d9d34d8 c1d3b0166030 debian 41d50ecd2f57 fedora
</dl>
<h2>Display containers with remote-volume mounted</h2>
<dl>
<dt>
<dd>
<p>$ docker container ls&#8211; filter volume = remote &#8211; volume&#8211; format &#8220;table &#123;&#123;.ID}}	&#123;&#123;.Mounts}}&#8221; CONTAINER ID MOUNTS 9c3527ed70ce remote &#8211; volume
</dl>
<h2>Display containers with a volume mounted in /data</h2>
<dl>
<dt>
<dd>
<pre><code>
$ docker container ls-- filter volume = / data-- format "table &#123;&#123;.ID}}	&#123;&#123;.Mounts}}" CONTAINER ID MOUNTS 9c3527ed70ce remote - volume
</code></pre>
</dl>
<h2>Display containers that have published port of 80:</h2>
<dl>
<dt>
<dd>
<pre>
$ docker ps --filter publish=80
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS                   NAMES
fc7e477723b7        busybox             &quot;top&quot;               About a minute ago   Up About a minute   0.0.0.0:32768-&gt;80/tcp   admiring_roentgen
</pre>
</dl>
<h2>Display containers that have exposed TCP port in the range of 8000-8080:</h2>
<dl>
<dt>
<dd>
<pre>
$ docker ps --filter expose=8000-8080/tcp
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
9833437217a5        busybox             &quot;top&quot;               21 seconds ago      Up 19 seconds       8080/tcp            dreamy_mccarthy
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show all containers (default shows just running)</p>
<p> <code>-f</code>, <code>&#8211;filter</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Filter output based on conditions provided</p>
<p> <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pretty-print containers using a Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for ls</p>
<p> <code>-n</code>, <code>&#8211;last</code>=-1 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show n last created containers (includes all states)</p>
<p> <code>-l</code>, <code>&#8211;latest</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show the latest created container (includes all states)</p>
<p> <code>&#8211;no-trunc</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Don&#8217;t truncate output</p>
<p> <code>-q</code>, <code>&#8211;quiet</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Only display container IDs</p>
<p> <code>-s</code>, <code>&#8211;size</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Display total file sizes</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
