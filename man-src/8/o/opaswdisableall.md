---
title: "opaswdisableall(8)"
name: "opaswdisableall"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaswdisableall/"
description: "opaswdisableall"
---

<p>opaswdisableall </p>
<p> <code>(Linux)</code> Disables all unused switch ports.</p>
<h2>Syntax</h2>
<p>opaswdisableall [-t <i>portsfile</i>] [-p <i>ports</i>] [-F <i>focus</i>] [-K <i>mkey</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-t <i>portsfile</i></p>
<dd>File with list of local HFI ports used to access fabrics when clearing counters. Default is /etc/sysconfig/opa/ports file. </p>
<dt>-p <i>ports</i></p>
<dd>List of local HFI ports used to access fabrics for counter clear. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </p>
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
<dt>-F <i>focus</i></p>
<dd>An opareport -style focus argument to limit the scope of operation. </p>
<dt>-K <i>mkey</i></p>
<dd>SM management key to access remote ports. </p>
</dl>
<h2>Examples</h2>
<p>opaswdisableall<br />
 opaswdisableall -p &#8216;1:1 1:2 2:1 2:2&#8217;</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></p>
<dd>List of ports, used in absence of -t and -p. </p>
<dt><code>PORTS_FILE</code></p>
<dd>File containing list of ports, used in absence of -t and -p. </p>
</dl>
