---
title: "docker-latest-ps(1)"
name: "docker-latest-ps"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-ps/"
description: "docker-ps – List containers"
---

<h2 class="name">NAME</h2>
<p> docker-ps &#8211; List containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker ps</code> [<code>-a</code>|<code>&#8211;all</code>] [<code>-f</code>|<code>&#8211;filter</code>[=<i>[]</i>]] [<code>&#8211;format</code>=<i>&quot;TEMPLATE&quot;</i>] [<code>&#8211;help</code>] [<code>-l</code>|<code>&#8211;latest</code>] [<code>-n</code>[=<i>-1</i>]] [<code>&#8211;no-trunc</code>] [<code>-q</code>|<code>&#8211;quiet</code>] [<code>-s</code>|<code>&#8211;size</code>] </p>
<h2>DESCRIPTION</h2>
<p> List the containers in the local repository. By default this shows only the running containers. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all</code>=<i>true</i>|<i>false</i><br />
Show all containers. Only running containers are shown by default. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>-f</code>, <code>&#8211;filter</code>=[]<br />
Filter output based on these conditions:<br />
&#8211; exited=&lt;int&gt;&nbsp;<wbr>an exit code of&nbsp;<wbr>&lt;int&gt;<br />
&#8211; label=&lt;key&gt;&nbsp;<wbr>or label=&lt;key&gt;=&lt;value&gt;<br />
&#8211; status=(created|restarting|running|paused|exited|dead)<br />
&#8211; name=&lt;string&gt;&nbsp;<wbr>a container&#8217;s name<br />
&#8211; id=&lt;ID&gt;&nbsp;<wbr>a container&#8217;s ID<br />
&#8211; before=(&lt;container-name&gt;|&lt;container-id&gt;)<br />
&#8211; since=(&lt;container-name&gt;|&lt;container-id&gt;)<br />
&#8211; ancestor=(&lt;image-name&gt;[:tag]|&lt;image-id&gt;| &lt;image [at] digest&gt;) &#8211; containers created from an image or a descendant.<br />
&#8211; volume=(&lt;volume-name&gt;|&lt;mount-point-destination&gt;)<br />
&#8211; network=(&lt;network-name&gt;|&lt;network-id&gt;)&nbsp;<wbr>&#8211; containers connected to the provided network </p>
<p> <code>&#8211;format</code>=&quot;<i>TEMPLATE</i>&quot;<br />
Pretty-print containers using a Go template.<br />
Valid placeholders:<br />
.ID &#8211; Container ID<br />
.Image &#8211; Image ID<br />
.Command &#8211; Quoted command<br />
.CreatedAt &#8211; Time when the container was created.<br />
.RunningFor &#8211; Elapsed time since the container was started.<br />
.Ports &#8211; Exposed ports.<br />
.Status &#8211; Container status.<br />
.Size &#8211; Container disk size.<br />
.Names &#8211; Container names.<br />
.Labels &#8211; All labels assigned to the container.<br />
.Label &#8211; Value of a specific label for this container. For example&nbsp;<wbr>&#123;&#123;.Label&nbsp;<wbr>&quot;com.docker.swarm.cpu&quot;}}<br />
.Mounts &#8211; Names of the volumes mounted in this container. </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-l</code>, <code>&#8211;latest</code>=<i>true</i>|<i>false</i><br />
Show only the latest created container&nbsp;<wbr>(includes all states). The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>-n</code>=<i>-1</i><br />
Show n last created containers&nbsp;<wbr>(includes all states). </p>
<p> <code>&#8211;no-trunc</code>=<i>true</i>|<i>false</i><br />
Don&#8217;t truncate output. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>-q</code>, <code>&#8211;quiet</code>=<i>true</i>|<i>false</i><br />
Only display numeric IDs. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>-s</code>, <code>&#8211;size</code>=<i>true</i>|<i>false</i><br />
Display total file sizes. The default is&nbsp;<wbr><i>false</i>. </p>
<h2>EXAMPLES</h2>
<h2>Display all containers, including non-running</h2>
<dl>
<dt>
<dd>
<pre>
# docker ps -a
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
# docker ps -a -q
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
# docker ps -a -q --filter=name=determined_torvalds
c1d3b0166030
</pre>
</dl>
<h2>Display containers with their commands</h2>
<dl>
<dt>
<dd>
<pre><code>
#docker ps-- format "&#123;&#123;.ID}}: &#123;&#123;.Command}}"
a87ecb4f327c : / bin / sh - c #(nop)MA 01946d9d34d8 : / bin / sh - c #(nop)MA c1d3b0166030 : / bin / sh - c yum - y up 41d50ecd2f57 : / bin / sh - c #(nop)MA
</code></pre>
</dl>
<h2>Display containers with their labels in a table</h2>
<dl>
<dt>
<dd>
<p>#docker ps&#8211; format &#8220;table &#123;&#123;.ID}}	&#123;&#123;.Labels}}&#8221;<br />
CONTAINER ID LABELS<br />
    a87ecb4f327c com.docker.swarm.node = ubuntu,<br />
                 com.docker.swarm.storage = ssd 01946d9d34d8 c1d3b0166030 com.docker.swarm.node = debian, com.docker.swarm.cpu = 6 41d50ecd2f57 com.docker.swarm.node = fedora, com.docker.swarm.cpu = 3, com.docker.swarm.storage = ssd
</dl>
<h2>Display containers with their node label in a table</h2>
<dl>
<dt>
<dd>
<p>#docker ps&#8211; format &#8216;table &#123;&#123;.ID}}	&#123;&#123;(.Label &#8220;com.docker.swarm.node&#8221;)}}&#8217;<br />
CONTAINER ID NODE<br />
    a87ecb4f327c ubuntu 01946d9d34d8 c1d3b0166030 debian 41d50ecd2f57 fedora
</dl>
<h2>Display containers with remote-volume mounted</h2>
<dl>
<dt>
<dd>
<p>$ docker ps&#8211; filter volume = remote &#8211; volume&#8211; format &#8220;table &#123;&#123;.ID}}	&#123;&#123;.Mounts}}&#8221; CONTAINER ID MOUNTS 9c3527ed70ce remote &#8211; volume
</dl>
<h2>Display containers with a volume mounted in /data</h2>
<dl>
<dt>
<dd>
<pre><code>
$ docker ps-- filter volume = / data-- format "table &#123;&#123;.ID}}	&#123;&#123;.Mounts}}" CONTAINER ID MOUNTS 9c3527ed70ce remote - volume
</code></pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; August 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; November 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; February 2015, updated by André Martins &lt;martins [at] noironetworks.com&gt; </p>
<h2>Index</h2>
