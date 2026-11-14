---
title: "atomic-run(1)"
name: "atomic-run"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-run/"
description: "atomic-run – Execute container image run method"
---

<h2 class="name">NAME</h2>
<p> atomic-run &#8211; Execute container image run method </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic run</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>&#8211;display</code>] [<code>-n</code>][<code>&#8211;name</code>[=<i>NAME</i>]] [<code>&#8211;spc</code>] [<code>&#8211;storage</code>] [<code>&#8211;quiet</code>] IMAGE [COMMAND] [ARG&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic run</code> attempts to start an existing container or run a container from an image, first reading the LABEL RUN field in the container IMAGE. </p>
<p> If the container image has a LABEL RUN instruction like the following: </p>
<p> LABEL RUN /usr/bin/docker run -t -i &#8211;rm \${OPT1} &#8211;cap-add=SYS_ADMIN &#8211;net=host -v \${LOGDIR}:/var/log -v \${DATADIR}:/var/lib &#8211;name \${NAME} \${IMAGE} \${OPT2} run.sh \${OPT3} </p>
<p> atomic run will run the following: </p>
<p> /usr/bin/docker run -t -i &#8211;rm &#8211;cap-add=SYS_ADMIN &#8211;net=host -v ${LOGDIR}:/var/log -v ${DATADIR}:/var/lib &#8211;name ${NAME} ${IMAGE} run.sh </p>
<p> If this field does not exist, atomic run defaults to the following: </p>
<p> /usr/bin/docker run -t -i &#8211;rm -v ${LOGDIR}:/var/log -v ${DATADIR}:/var/lib &#8211;name ${NAME} ${IMAGE} </p>
<p> These defaults are suggested values for your container images. </p>
<p> atomic run will set the following environment variables for use in the command: </p>
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
<p> <code>RUN_OPTS</code><br />
&nbsp;<wbr>&nbsp;<wbr>Content of file specified by LABEL RUN_OPTS_FILE.&nbsp;<wbr>&nbsp;<wbr>During atomic install, the install.sh can populate the file with any additional options that need to be passed to docker run, for example &#8211;hostname=<a rel="nofollow" href="http://www.example.test">www.example.test</a>&nbsp;<wbr>or &#8211;net host. The file name undergoes environment variable expansion, so for example LABEL RUN_OPTS_FILE&nbsp;<wbr>&#8216;/var/lib/${NAME}/docker-run-opts&#8217;&nbsp;<wbr>can be used to store per-container configuration. </p>
<h2>OPTIONS:</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;display</code><br />
&nbsp;<wbr>&nbsp;<wbr>Display the image&#8217;s run options and environment variables populated into the run command. The run command will not execute if &#8211;display is specified. If &#8211;display is not specified the run command will execute. </p>
<p> <code>&#8211;n</code> <code>&#8211;name</code>=&quot;&quot;<br />
Use this name for creating run content for the container. NAME will default to the IMAGENAME if it is not specified. </p>
<p> <code>&#8211;spc</code><br />
&nbsp;<wbr>&nbsp;<wbr>Run container in super privileged container mode.&nbsp;<wbr>&nbsp;<wbr>The image will run with the following command: </p>
<p> /usr/bin/docker run -t -i &#8211;rm &#8211;privileged -v /:/host -v /run:/run &#8211;net=host &#8211;ipc=host &#8211;pid=host -e HOST=/host -e NAME=${NAME} -e IMAGE=${IMAGE} &#8211;name ${NAME} ${IMAGE} </p>
<p> <code>-storage</code><br />
Allows you to override the default definition for the storage backend where your image will reside if pulled.&nbsp;<wbr>&nbsp;<wbr>If the image is already local, the &#8211;storage option will dictate where atomic should look for the image prior to running. Valid options are docker and ostree. </p>
<p> <code>&#8211;quiet</code><br />
&nbsp;<wbr>&nbsp;<wbr>Run without verbose messaging&nbsp;<wbr>(i.e. security warnings). </p>
<h2>HISTORY</h2>
<p> January 2015, Originally compiled by Daniel Walsh (dwalsh at redhat dot com) July 2015, edited by Sally O&#8217;Malley (somalley at redhat dot com) </p>
<h2>Index</h2>
