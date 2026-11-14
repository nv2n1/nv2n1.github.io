---
title: "qgpureset(1)"
name: "qgpureset"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qgpureset/"
description: "qgpureset – reset GPU error counts"
---

<h2 class="name">NAME</h2>
<p>&nbsp;<wbr>qgpureset &#8211; reset GPU error counts </p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr>qgpureset -H host -g gpuid -p -v</p>
<h2>DESCRIPTION</h2>
<p> The <code>qgpureset </code> command will request a MOM to reset the ECC counts on one of it&#8217;s Nvidia GPUs. The GPU&#8217;s error count is reset by sending a <i>GPU Control</i> batch request to the batch server. </p>
<p> Changing the GPU mode requires PBS Operator or Manager privilege. It also requires that Torque be configured with &#8211;enable-nvidia-gpu. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-H host</p>
<dd> Specifies the host within the cluster on which the GPU is located. The argument is the name of a host that is a member of the cluster of hosts managed by the server.</p>
<dt>-g gpuid</p>
<dd> Specifies the ID of the GPU.</p>
<dt>-p</p>
<dd> Specifies to reset the GPU&#8217;s permanent ECC error count.</dl>
<dl>
<dt>-v</p>
<dd> Specifies to reset the GPU&#8217;s volatile ECC error count.</dl>
<h2>OPERANDS</h2>
<p> None </p>
<h2>STANDARD ERROR</h2>
<p> The qgpureset command will write a diagnostic messages to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the<br />
&nbsp;<wbr>qgpureset command, the exit status will be a value of zero. </p>
<p> If the qgpureset command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/8B-pbs_mom/">pbs_mom</a>(8B) and <a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B) </p>
<h2>Index</h2>
