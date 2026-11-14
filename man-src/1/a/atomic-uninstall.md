---
title: "atomic-uninstall(1)"
name: "atomic-uninstall"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-uninstall/"
description: "atomic-uninstall – Remove/Uninstall container/container image from system"
---

<h2 class="name">NAME</h2>
<p> atomic-uninstall &#8211; Remove/Uninstall container/container image from system </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic uninstall</code> [<code>-f</code>][<code>&#8211;force</code>] [<code>-h</code>|<code>&#8211;help</code>] [<code>-n</code>][<code>&#8211;name</code>[=<i>NAME</i>]] IMAGE [ARG&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic uninstall</code> attempts to read the LABEL UNINSTALL field in the container IMAGE, if this field does not exist <code>atomic uninstall</code> will just uninstall the image. </p>
<p> If the container image has a LABEL UNINSTALL instruction like the following: </p>
<p> LABEL UNINSTALL /usr/bin/docker run -t -i &#8211;rm \${OPT1} &#8211;privileged -v /:/host &#8211;net=host &#8211;ipc=host &#8211;pid=host -e HOST=/host -e NAME=${NAME} -e IMAGE=${IMAGE} -e CONFDIR=\/etc/${NAME} -e LOGDIR=/var/log/\${NAME} -e DATADIR=/var/lib/\${NAME} ${IMAGE} \${OPT2} /bin/uninstall.sh \${OPT3} </p>
<p> atomic uninstall will set the following environment variables for use in the command: </p>
<p> <code>NAME</code><br />
&nbsp;<wbr>&nbsp;<wbr>The name specified via the command.&nbsp;<wbr>&nbsp;<wbr>NAME will be replaced with IMAGE if it is not specified. </p>
<p> <code>IMAGE</code><br />
&nbsp;<wbr>&nbsp;<wbr>The name and image specified via the command. </p>
<p> <code>OPT1, OPT2, OPT3</code><br />
&nbsp;<wbr>&nbsp;<wbr>Additional options which can be specified via the command. </p>
<p> <code>SUDO_UID</code><br />
&nbsp;<wbr>&nbsp;<wbr>The SUDO_UID environment variable.&nbsp;<wbr>&nbsp;<wbr>This is useful with the docker -u option for user space tools.&nbsp;<wbr>&nbsp;<wbr>If the environment variable is not available, the value of&nbsp;<wbr>/proc/self/loginuid is used. </p>
<p> <code>SUDO_GID</code><br />
&nbsp;<wbr>&nbsp;<wbr>The SUDO_GID environment variable.&nbsp;<wbr>&nbsp;<wbr>This is useful with the docker -u option for user space tools.&nbsp;<wbr>&nbsp;<wbr>If the environment variable is not available, the default GID of the value for SUDO_UID is used.&nbsp;<wbr>&nbsp;<wbr>If this value is not available, the value of&nbsp;<wbr>/proc/self/loginuid is used. </p>
<p> Any additional arguments will be appended to the command. </p>
<h2>OPTIONS:</h2>
<p> <code>-f</code> <code>&#8211;force</code><br />
&nbsp;<wbr>&nbsp;<wbr>Remove all containers based on this image </p>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-n</code> <code>&#8211;name</code>=&quot;&quot;<br />
If name is specified atomic uninstall will uninstall the named container from the system, otherwise it will uninstall the container images. </p>
<h2>HISTORY</h2>
<p> January 2015, Originally compiled by Daniel Walsh (dwalsh at redhat dot com) </p>
<h2>Index</h2>
