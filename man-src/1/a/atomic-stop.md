---
title: "atomic-stop(1)"
name: "atomic-stop"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-stop/"
description: "atomic-stop – Execute container image stop method"
---

<h2 class="name">NAME</h2>
<p> atomic-stop &#8211; Execute container image stop method </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic stop</code> [<code>-h</code>|<code>&#8211;help</code>] container [ARG&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic stop</code> attempts to stop a running container, first reading the LABEL STOP field in the container IMAGE. </p>
<p> If the container image has a LABEL STOP instruction like the following: </p>
<p> LABEL STOP /usr/bin/docker kill -s HUP \${NAME} </p>
<p> atomic would execute this command before stopping the container. </p>
<p> atomic stop will set the following environment variables for use in the command: </p>
<p> If this field does not exist, atomic stop will just stop the container, if the container is running. </p>
<p> Any additional arguments will be appended to the command. </p>
<h2>OPTIONS:</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>HISTORY</h2>
<p> March 2015, Originally compiled by Daniel Walsh (dwalsh at redhat dot com) </p>
<h2>Index</h2>
