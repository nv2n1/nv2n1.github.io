---
title: "tcpvmexportd(1)"
name: "tcpvmexportd"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcpvmexportd/"
description: "tcpvmexportd – transcode PVM3 export interface"
---

<h2>NAME</h2>
<p> tcpvmexportd &#8211; transcode PVM3 export interface</p>
<h2>SYNOPSIS</h2>
<p> <code>tcpvmexportd</code> <code>-s|-m</code> [ <code>options</code> ]</p>
<h2>COPYRIGHT</h2>
<p> <code>tcpvmexportd</code> is Copyright (C) by Malanchini Marzio</p>
<h2>DESCRIPTION</h2>
<p> <code>tcpvmexportd</code> This is the frontend for all the activity of export_pvm module: the program is spawned on all cluster hosts and wait to do the encode work.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code></p>
<dd> Start tcpvmexportd in slave mode (internal use of export_pvm) [default].</p>
<dt><code> Sub Options for slave mode</code></p>
<dd>
<p> <code>-j</code> Start merger process [off]. </p>
<p> <code>-L</code> Create only the merge list [off]. </p>
<p> <code>-c name</code> Name of slave function req in slave mode [none]. </p>
<p> <code>-x parameters</code> Multiplex parameters [none]. </p>
<p> <code>-1 param</code> First parameter to pass to the slave function [null]. </p>
<p> <code>-2 param</code> Second parameter to pass to the slave function [null]. </p>
<p> <code>-3 param</code> Third parameter to pass to the slave function [null]. </p>
<p> <code>-t type</code> Elab video or audio frame (video|audio|system|multisystem) . </p>
<p> <code>-f name</code> Out file name [/tmp/my_file_name] </p>
<p> <code>-p number</code> Multipass (0,1,2,3) [0]. </p>
<p> <code>-M </code> Enable internal multipass [off]. </p>
<dt><code>-m</code></p>
<dd> Start tcpvmexportd in master mode [off]. </p>
<dt><code> Sub Options for master mode</code></p>
<dd>
<p> <code>-j</code> Start the batch merge mode [off]. </p>
<p> <code>-C</code> Check the config or merge file [off]. </p>
<p> <code>-f name</code> Input file name [/tmp/my_file_name] </p>
<dt><code>-h</code></p>
<dd> Print help.</p>
<dt><code>-v</code></p>
<dd> Print the version.</dl>
<h2>EXAMPLES</h2>
<p> Command: </p>
<p> <code>tcpvmexportd -m -j -f mylistfile.lst</code> </p>
<p> Run tcpvmexportd in batch merge mode. </p>
<p> <code>tcpvmexportd -m -C -f mylistfile.lst</code> </p>
<p> Check the config or the merge file. </p>
<h2>AUTHORS</h2>
<p> <code>tcpvmexportd</code> was written by Marzio Malanchini<br />
 &lt;marzio_malanchini [at] vodafone.it&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
