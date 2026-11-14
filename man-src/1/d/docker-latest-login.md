---
title: "docker-latest-login(1)"
name: "docker-latest-login"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-login/"
description: "docker-login – Log in to a Docker registry."
---

<h2 class="name">NAME</h2>
<p> docker-login &#8211; Log in to a Docker registry. </p>
<h2>SYNOPSIS</h2>
<p> <code>docker login</code> [<code>&#8211;help</code>] [<code>-p</code>|<code>&#8211;password</code>[=<i>PASSWORD</i>]] [<code>-u</code>|<code>&#8211;username</code>[=<i>USERNAME</i>]] [SERVER] </p>
<h2>DESCRIPTION</h2>
<p> Log in to a Docker Registry located on the specified SERVER. You can specify a URL or a hostname for the SERVER value. If you do not specify a SERVER, the command uses Docker&#8217;s public registry located at <a rel="nofollow" href="https://registry-1.docker.io/">https://registry-1.docker.io/</a> by default. To get a username/password for Docker&#8217;s public registry, create an account on Docker Hub. </p>
<p> docker login requires user to use sudo or be root, except when:</p>
<dl>
<dt>&bull;</p>
<dd>
<p> item connecting to a remote daemon, such as a docker-machine provisioned docker engine. item user is added to the docker group. This will impact the security of your system; the docker group is root equivalent. See &lt;<a rel="nofollow" href="https://docs.docker.com/articles/security/#docker-daemon-attack-surface">https://docs.docker.com/articles/security/#docker-daemon-attack-surface</a>&gt; for details.</dl>
<p> You can log into any public or private repository for which you have credentials. When you log in, the command stores encoded credentials in $HOME/.docker/config.json on Linux or %USERPROFILE%/.docker/config.json on Windows. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-p</code>, <code>&#8211;password</code>=&quot;&quot;<br />
Password </p>
<p> <code>-u</code>, <code>&#8211;username</code>=&quot;&quot;<br />
Username </p>
<h2>EXAMPLES</h2>
<h2>Login to a registry on your localhost</h2>
<dl>
<dt>
<dd>
<pre>
# docker login localhost:8080
</pre>
</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-logout/">docker-logout</a>(1)</code> to log out from a Docker registry. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; April 2015, updated by Mary Anthony for v2 &lt;mary [at] docker.com&gt; November 2015, updated by Sally O&#8217;Malley &lt;somalley [at] redhat.com&gt; </p>
<h2>Index</h2>
