---
title: "opadisablehosts(8)"
name: "opadisablehosts"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opadisablehosts/"
description: "opadisablehosts"
---

<p>opadisablehosts </p>
<p> <code>(Linux)</code> Searches for a set of hosts in the fabric and disables their corresponding switch port.</p>
<h2>Syntax</h2>
<p>opadisablehosts [-h <i>hfi</i>] [-p <i>port</i>] <i>reason</i> host &#8230;</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-h/&#8211;hfi <i>hfi</i></p>
<dd>HFI to send through. The default is the first HFI. </p>
<dt>-p/&#8211;port <i>port</i></p>
<dd>Port to send through. The default is the first active port. </p>
<dt>
&nbsp;<wbr><i>reason</i>&nbsp;<wbr></p>
<dd>Text describing the reason hosts are being disabled. <i>reason</i> is saved in the reason field of the output file. </p>
<dd>Information about the links disabled is written to a CSV file. By default, this file is named /opa/disabled:hfi:port.csv where the hfi:port part of the file name is replaced by the HFI number and the port number being operated on (such as 0:0 or 1:2). This CSV file can be used as input to opaenableports.</p>
<dd>The list is of the form: NodeGUID;PortNum;NodeType;NodeDesc;NodeGUID; PortNum;NodeType;NodeDesc;Reason For each listed link, the switch port closer to this is the one that has been disabled.</dl>
<h2>Examples</h2>
<p>opadisablehosts &#8216;bad DRAM&#8217; compute001 compute045<br />
 opadisablehosts -h 1 -p 2 &#8216;crashed&#8217; compute001 compute045 </p>
