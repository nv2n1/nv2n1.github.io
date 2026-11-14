---
title: "opaenableports(8)"
name: "opaenableports"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaenableports/"
description: "opaenableports"
---

<p>opaenableports </p>
<p> <code>(Linux)</code> Accepts a disabled ports input file and re-enables the specified ports. The input file can be /etc/sysconfig/opa/disabled*.csv or a user-created subset of such a file. After enabling the port, it is removed from /etc/sysconfig/opa/disabled*.csv.</p>
<h2>Syntax</h2>
<p>opaenableports [-t <i>portsfile</i>] [-p <i>ports</i>] #8217lt; disabled.csv</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-t <i>portsfile</i></p>
<dd>File with list of local HFI ports used to access fabric for operation. Default is /etc/sysconfig/opa/ports file. </p>
<dt>-p <i>ports</i></p>
<dd>List of local HFI ports used to access fabric for operation. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </p>
<dd></dl>
<p> <code>NOTE:</code> In this release, in multi-rail fabrics, this script does not work as expected when supplied with multiple egress ports. The script processes the entire input file against the first egress port specified, leaving no data to be applied against other egress ports. As a workaround, call the script once for each egress port. </p>
<dl>
<dd>Uses the format hfi:port, for example:</p>
<dl>
<dd>
<dl>
<dd>0:0 First active port in system. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>0:y Port <i>y</i> within system. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>x:0 First active port on HFI <i>x</i>. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>x:y HFI <i>x</i>, port <i>y</i>. </p>
</dl>
</dl>
<dt>disabled.csv</p>
<dd>Input file listing the ports to enable. The list is of the form: NodeGUID;PortNum;NodeType;NodeDesc;Ignored. </p>
<dd>An input file like this is generated in /etc/sysconfig/opa/disabled* by opadisableports.</dl>
<h2>Examples</h2>
<p>opaenableports #8217lt; disabled.csv<br />
 opaenableports #8217lt; /etc/sysconfig/opa/disabled:0:0.csv<br />
 opaenableports -p &#8216;1:1 1:2 2:1 2:2&#8217; #8217lt; disabled.csv</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></p>
<dd>List of ports, used in absence of -t and -p.</p>
<dt><code>PORTS_FILE</code></p>
<dd>File containing list of ports, used in absence of -t and -p. </p>
</dl>
