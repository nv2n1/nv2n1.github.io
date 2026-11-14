---
title: "opacapture(1)"
name: "opacapture"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opacapture/"
description: "opacapture"
---

<h2>NAME</h2>
<p> opacapture </p>
<p> <code>(Host)</code> Captures critical system information into a zipped tar file. The resulting tar file should be sent to Customer Support along with any Intel(R) Omni-Path Fabric problem report regarding this system. </p>
<p> <code>NOTE:</code> The resulting host capture file can require significant amounts of space on the host. The actual size varies, but sizes can be multiple megabytes. Intel recommends ensuring that adequate disk space is available on the host system. </p>
<h2>Syntax</h2>
<p> opacapture [-d <i>detail</i>] <i>output_tgz_file</i></p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd> Shows full help text. </p>
<dt>-d <i>detail</i></p>
<dd> Captures level of detail:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 1 (Local) Obtains local information from host. Default if no options are entered. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 2 (Fabric) In addition to <i>Local</i>, also obtains basic fabric information by queries to the SM and fabric error analysis using <code>opareport</code>. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 3 (Fabric+FDB) In addition to <i>Fabric</i>, also obtains the Forwarding Database (FDB), which includes the switch forwarding tables from the SM and the server multicast membership. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 4 (Analysis) In addition to <i>Fabric+FDB</i>, also obtains opaallanalysis results. If opaallanalysis has not yet been run, it is run as part of the capture. </p>
</dl>
</dl>
<dt>
<dd>
</dl>
<p> <code>NOTE:</code> Detail levels 2 #8217#8211; 4 can be used when fabric operational problems occur. If the problem is node-specific, detail level 1 should be sufficient. Detail levels 2 &#8211; 4 require an operational Fabric Manager. Typically your support representative requests a given detail level. If a given detail level takes excessively long or fails to be gathered, try a lower detail level. </p>
<p> For detail levels 2 #8217#8211; 4, the additional information is only available on a node with Intel(R) Omni-Path Fabric Suite FastFabric Toolset installed. The information is gathered for every fabric specified in the /etc/sysconfig/opa/ports file. </p>
<dl>
<dt>
&nbsp;<wbr><i>output_tgz_file</i>&nbsp;<wbr></p>
<dd> The name of a file to be created by opacapture. The file name specified is overwritten if it already exists. Intel recommends using the .tgz suffix in the file name supplied. If the filename given does not have a .tgz suffix, the .tgz suffix is added. </p>
</dl>
<h2>Examples</h2>
<p> opacapture mycapture.tgz<br />
 opacapture -d 3 030127capture.tgz </p>
<h2>Index</h2>
