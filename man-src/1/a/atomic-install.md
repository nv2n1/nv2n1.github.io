---
title: "atomic-install(1)"
name: "atomic-install"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-install/"
description: "atomic-install – Execute Image Install Method"
---

<h2 class="name">NAME</h2>
<p> atomic-install &#8211; Execute Image Install Method </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic install</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>&#8211;display</code>] [<code>-n</code>][<code>&#8211;name</code>[=<i>NAME</i>]] [<code>&#8211;rootfs</code>=<i>ROOTFS</i>] [<code>&#8211;set</code>=<i>NAME</i>=<i>VALUE</i>] [<code>&#8211;storage</code>] [<code>&#8211;system</code>] IMAGE [ARG&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic install</code> attempts to read the LABEL INSTALL field in the container IMAGE, if this field does not exist, atomic install will install the IMAGE. </p>
<p> If the container image has a LABEL INSTALL instruction like the following: </p>
<p> LABEL INSTALL /usr/bin/docker run -t -i &#8211;rm \${OPT1} &#8211;privileged -v /:/host &#8211;net=host &#8211;ipc=host &#8211;pid=host -e HOST=/host -e NAME=\${NAME} -e IMAGE=\${IMAGE} -e CONFDIR=\/etc/${NAME} -e LOGDIR=/var/log/\${NAME} -e DATADIR=/var/lib/\${NAME} \${IMAGE} \${OPT2} /bin/install.sh \${OPT3} </p>
<p> atomic install will set the following environment variables for use in the command: </p>
<p> <code>NAME</code> The name specified via the command. NAME will be replaced with IMAGE if it is not specified. </p>
<p> <code>IMAGE</code> The name and image specified via the command. </p>
<p> <code>OPT1, OPT2, OPT3</code> Additional options which can be specified via the command. </p>
<p> <code>SUDO_UID</code> The SUDO_UID environment variable. This is useful with the docker -u option for user space tools. If the environment variable is not available, the value of /proc/self/loginuid is used. </p>
<p> <code>SUDO_GID</code> The SUDO_GID environment variable. This is useful with the docker -u option for user space tools. If the environment variable is not available, the default GID of the value for SUDO_UID is used. If this value is not available, the value of /proc/self/loginuid is used. </p>
<p> Any additional arguments will be appended to the command. </p>
<h2>OPTIONS:</h2>
<p> <code>-h</code> <code>&#8211;help</code> Print usage statement </p>
<p> <code>&#8211;display</code> Display the image&#8217;s install options and environment variables populated into the install command. The install command will not execute if &#8211;display is specified. If &#8211;display is not specified the install command will execute. </p>
<p> <code>-n</code> <code>&#8211;name</code>=&quot;&quot;<br />
&nbsp;<wbr>Use this name for creating installed content for the container.<br />
&nbsp;<wbr>NAME will default to the IMAGENAME if it is not specified. </p>
<p> <code>&#8211;rootfs=ROOTFS</code> Specify a ROOTFS folder, which can be an existing, expanded container/image, or a location which contains an existing root filesystem. The existing rootfs will be used as the new system container&#8217;s rootfs (read only), and thus the new container will only contain config and info files. </p>
<p> <code>&#8211;set=NAME=VALUE</code> Set a value that is going to be used by a system container for its configuration and can be specified multiple times. It is used only by &#8211;system. OSTree is required for this feature to be available. </p>
<p> <code>&#8211;storage</code> Allows you to override the default definition for the storage backend where your image will reside if pulled. If the image is already local, the &#8211;storage option will dictate where atomic should look for the image prior to installing. Valid options are docker and ostree. </p>
<p> <code>&#8211;system</code> Install a system container. A system container is a container that is executed out of an systemd unit file early in boot, using runc. The specified <code>IMAGE</code> must be a system image already fetched. If it is not already present, atomic will attempt to fetch it assuming it is an oci image. For more information on how images are fetched, see also <code><a href="/docs/linux/man/1-atomic-pull/">atomic-pull</a>(1)</code>. Installing a system container consists of checking it the image by default under /var/lib/containers/atomic/ and generating the configuration files for runc and systemd. OSTree and runc are required for this feature to be available. </p>
<p> Note: If the image being pulled contains a label of system.type=ostree, atomic will automatically substitute the storage backend to be ostree. This can be overridden with the &#8211;storage option. </p>
<p> <code>&#8211;user</code> If running as non-root, specify to install the image from the current OSTree repository and manage it through systemd and bubblewrap. OSTree and bwrap-oci are required for this feature to be available. </p>
<h2>HISTORY</h2>
<p> January 2015, Originally compiled by Daniel Walsh (dwalsh at redhat dot com) July 2015, edited by Sally O&#8217;Malley (somalley at redhat dot com) </p>
<h2>Index</h2>
