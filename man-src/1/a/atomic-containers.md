---
title: "atomic-containers(1)"
name: "atomic-containers"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-containers/"
description: "atomic-containers – operations on containers"
---

<h2 class="name">NAME</h2>
<p> atomic-containers &#8211; operations on containers </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic containers COMMAND [OPTIONS] [CONTAINERS&#8230;]</code> </p>
<p> atomic containers allows the user to view and operate on containers </p>
<h2>COMMANDS</h2>
<p> <code>delete</code> </p>
<p> delete specified container(s). </p>
<p> <code>list</code> </p>
<p> list containers on your system. </p>
<p> <code>trim</code> </p>
<p> discard unused blocks (fstrim) on running containers. </p>
<p> <code>update</code> </p>
<p> update a system container. </p>
<p> <code>rollback</code> </p>
<p> rollback a system container. </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic containers delete</code>, delete specified container image from the system. </p>
<p> Using &#8211;all will delete all the installed containers. </p>
<p> <code>atomic containers list</code>, by default, will list all running containers on your system. </p>
<p> Using &#8211;all will list all the installed containers. </p>
<p> <code>atomic containers trim</code>, Discard unused blocks (fstrim) on rootfs of running containers. </p>
<p> e.g. If you have 2 running containers on your system with container IDs (496b8679b6cf, 9bb990da1203). </p>
<dl>
<dt>
<dd>
<p> atomic containers trim Trimming container id 496b8679b6cf Trimming container id 9bb990da1203</dl>
<p> <code>atomic containers update</code>, update a system container to use a newer version of an image. </p>
<p> Can use &#8211;set to update environment variables. </p>
<p> <code>atomic containers rollback</code>, rollback a system container to the other deployment if one exists. </p>
<h2>OPTIONS:</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>delete OPTIONS:</h2>
<p> <code>-a</code> <code>&#8211;all</code><br />
&nbsp;<wbr>&nbsp;<wbr>Delete all the installed containers </p>
<p> <code>-f</code> <code>&#8211;force</code><br />
&nbsp;<wbr>&nbsp;<wbr>Force the deletion of specified running containers </p>
<h2>list OPTIONS:</h2>
<p> <code>-a</code> <code>&#8211;all</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print all the installed containers </p>
<p> <code>-f</code> <code>&#8211;filter</code><br />
&nbsp;<wbr>&nbsp;<wbr>Filter output based on given filters, example usage: &#8211;filter id=foo will list all containers that has&nbsp;<wbr>&quot;foo&quot;&nbsp;<wbr>as part of their ID. </p>
<p> Filterables: container (id), image, command, created, status, runtime </p>
<p> <code>&#8211;json</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print in a machine parsable format </p>
<p> <code>-n</code> <code>&#8211;noheading</code><br />
&nbsp;<wbr>&nbsp;<wbr>Do not print heading when listing the containers </p>
<p> <code>&#8211;no-trunc</code><br />
&nbsp;<wbr>&nbsp;<wbr>Do not truncate output </p>
<p> <code>-q</code> <code>&#8211;quiet</code><br />
&nbsp;<wbr>&nbsp;<wbr>Only display container IDs </p>
<h2>update OPTIONS:</h2>
<p> <code>&#8211;set=NAME=VALUE</code><br />
&nbsp;<wbr>&nbsp;<wbr>Set a value that is going to be used by a system container for its configuration and can be specified multiple times.&nbsp;<wbr>&nbsp;<wbr>OSTree is required for this feature to be available. </p>
<h2>HISTORY</h2>
<p> June 2016, Originally compiled by Giuseppe Scrivano (gscrivan at redhat dot com) July 2016, Added sub-commands filter, no-trunc and quiet (jerzhang at redhat dot com) Sept 2016, Added atomic containers trim subcommand (shishir dot mahajan at redhat dot com) </p>
<h2>Index</h2>
