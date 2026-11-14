---
title: "opashowmc(1)"
name: "opashowmc"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opashowmc/"
description: "opashowmc"
---

<h2>NAME</h2>
<p> opashowmc </p>
<p> <code>(Linux)</code> Displays the Intel(R) Omni-Path Multicast groups created for the fabric along with the Intel(R) Omni-Path Host Fabric Interface (HFI) ports which are a member of each multicast group. This command can be helpful when attempting to analyze or debug Intel(R) Omni-Path multicast usage by applications or ULPs such as IPoIB.</p>
<h2>Syntax</h2>
<p> opashowmc [-v] [-t <i>portsfile</i>] [-p <i>ports</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd> Produces full help text. </p>
<dt>-v</p>
<dd> Returns verbose output and shows name of each member. </p>
<dt>-t <i>portsfile</i></p>
<dd> File with list of local HFI ports used to access fabric(s) for analysis. Default is /etc/sysconfig/opa/ports file. </p>
<dt>-p <i>ports</i></p>
<dd> List of local HFI ports used to access fabric(s) for analysis. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </p>
<dt>
<dd> Uses the format hfi:port, for example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 0:0 First active port in system. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 0:y Port <i>y</i> within system. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> x:0 First active port on HFI <i>x</i>. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> x:y HFI <i>x</i>, port <i>y</i>. </p>
</dl>
</dl>
</dl>
<h2>Examples</h2>
<p> opashowmc<br />
 opashowmc -p &#8216;1:1 1:2 2:1 2:2&#8217;</p>
<h2>Environment Variables</h2>
<p> The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></p>
<dd> List of ports, used in absence of -t and -p. </p>
<dt><code>PORTS_FILE</code></p>
<dd> File containing list of ports, used in absence of -t and -p. </p>
</dl>
<h2>Index</h2>
