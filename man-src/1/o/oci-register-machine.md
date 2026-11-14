---
title: "oci-register-machine(1)"
name: "oci-register-machine"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oci-register-machine/"
description: "oci-register-machine – Register OCI containers with systemd-machined"
---

<h2 class="name">NAME</h2>
<p> oci-register-machine &#8211; Register OCI containers with systemd-machined</p>
<h2>SYNOPSIS</h2>
<p> <code>oci-register-machine</code> </p>
<h2>DESCRIPTION</h2>
<p> oci-register-machine is a OCI hook program. If you add it to the runc json data as a hook, runc will execute the application after the container process is created but before it is executed, with a prestart flag. When the container exits oci-register-machine will be executed, after the container exits but before it is destroyed, with the poststop flag. Docker will execute oci-register-machine as a container hook when it is installed in the /usr/libexec/oci/hooks.d directory. </p>
<p> After starting an OCI container, the container will be listed with the machinectl. The machine name will be the container ID. Machinectl will then be able to manage the container. When container exits, the oci-register-machine will remove the instance from machinectl. </p>
<p> You can disable this service by editing the /etc/oci-register-machine.conf file and setting the disabled field to true. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ docker run -it busybox /bin/sh
(In different terminal):
$ machinectl
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
#
MACHINE                          CLASS     SERVICE
5556287c7fa1c2312243f5ca2d75c90b container docker 
1 machines listed.
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-docker-run/">docker-run</a>(1), <a href="/docs/linux/man/1-machinectl/">machinectl</a>(1), <a href="/docs/linux/man/8-systemd-machined/">systemd-machined</a>(8) </p>
<h2>HISTORY</h2>
<p> November 2015, updated by Sally O&#8217;Malley &lt;somalley [at] redhat.com&gt; </p>
<h2>Index</h2>
