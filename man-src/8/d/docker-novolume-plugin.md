---
title: "docker-novolume-plugin(8)"
name: "docker-novolume-plugin"
section: "8"
letter: "d"
url: "/docs/linux/man/8-docker-novolume-plugin/"
description: "docker-novolume-plugin – Blocks self provisioned volumes"
---

<p>docker-novolume-plugin &#8211; Blocks self provisioned volumes </p>
<h2>Synopsis</h2>
<p><code>docker-novolume-plugin</code> [<code>&#8211;cert-path</code>=[=<i>&quot;&quot;</i>]] [<code>&#8211;host</code>=[=<i><a href="unix:///var/run/docker.sock">unix:///var/run/docker.sock</a></i>]] [<code>&#8211;tls-verify</code>=[=<i>false</i>]] </p>
<h2>Description</h2>
<p>When a volume in provisioned via the VOLUME instruction in a Dockerfile or via docker run -v volumename, host&#8217;s storage space is used. This could lead to an unexpected out of space issue which could bring down everything. There are situations where this is not an accepted behavior. PAAS, for instance, can&#8217;t allow their users to run their own images without the risk of filling the entire storage space on a server. One solution to this is to deny users from running images with volumes. This way the only storage a user gets can be limited and PAAS can assign quota to it. This plugin solves this issue by disallowing starting a container with local volumes defined. In particular, the plugin will block docker run with:  </p>
<pre>--volumes-from
images that have VOLUME(s) defined
volumes early provisioned with docker volume command</pre>
</dl>
<p> The only thing allowed will be just bind mounts. </p>
<h2>Options</h2>
<p><code>&#8211;cert-path</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>Certificates path to connect to Docker&nbsp;<wbr>(cert.pem, key.pem) <code>&#8211;host</code>=&quot;<a href="unix:///var/run/docker.sock">unix:///var/run/docker.sock</a>&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>Specifies the host where to contact the docker daemon. <code>&#8211;tls-verify</code>=&quot;false&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>Whether to verify certificates or not</p>
<h2>Authors</h2>
<p>Antonio Murdaca &lt;runcom [at] redhat.com&gt;</p>
