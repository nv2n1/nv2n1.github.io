---
title: "opashowmc(8)"
name: "opashowmc"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opashowmc/"
description: "opashowmc"
---

<p>opashowmc </p>
<p> <code>(Linux)</code> Displays the Intel(R) Omni-Path Multicast groups created for the fabric along with the Intel(R) Omni-Path Host Fabric Interface (HFI) ports which are a member of each multicast group. This command can be helpful when attempting to analyze or debug Intel(R) Omni-Path multicast usage by applications or ULPs such as IPoIB.</p>
<h2>Syntax</h2>
<p>opashowmc [-v] [-t <i>portsfile</i>] [-p <i>ports</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd>Produces full help text. </dd>
<dt>-v</dt>
<dd>Returns verbose output and shows name of each member. </dd>
<dt>-t <i>portsfile</i></dt>
<dd>File with list of local HFI ports used to access fabric(s) for analysis. Default is /etc/sysconfig/opa/ports file. </dd>
<dt>-p <i>ports</i></dt>
<dd>List of local HFI ports used to access fabric(s) for analysis. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </dd>
<dd>Uses the format hfi:port, for example:</dd>
<dl>
<dd>
</dd><dl>
<dd>0:0 First active port in system. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>0:y Port <i>y</i> within system. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>x:0 First active port on HFI <i>x</i>. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>x:y HFI <i>x</i>, port <i>y</i>. </dd>
</dl>
</dl>
</dl>
<h2>Examples</h2>
<p>opashowmc<br/>
 opashowmc -p &#8216;1:1 1:2 2:1 2:2&#8217;</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></dt>
<dd>List of ports, used in absence of -t and -p. </dd>
<dt><code>PORTS_FILE</code></dt>
<dd>File containing list of ports, used in absence of -t and -p. </dd>
</dl>
