---
title: "opaswenableall(8)"
name: "opaswenableall"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaswenableall/"
description: "opaswenableall"
---

<p>opaswenableall </p>
<p> <code>(Linux)</code> Re-enables all unused (or disabled) switch ports.</p>
<h2>Syntax</h2>
<p>opaswenableall [-t <i>portsfile</i>] [-p <i>ports</i>] [-F <i>focus</i>] [-K <i>mkey</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd>Produces full help text. </dd>
<dt>-t <i>portsfile</i></dt>
<dd>File with list of local HFI ports used to access fabrics for operation. Default is /etc/sysconfig/opa/ports file. </dd>
<dt>-p <i>ports</i></dt>
<dd>List of local HFI ports used to access fabrics for operation. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </dd>
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
<dt>-F <i>focus</i></dt>
<dd>An opareport -style focus argument to limit the scope of operation. </dd>
<dt>-K <i>mkey</i></dt>
<dd>SM management key to access remote ports. </dd>
</dl>
<h2>Examples</h2>
<p>opaswenableall<br />
 opaswenableall -p &#8216;1:1 1:2 2:1 2:2&#8217;</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></dt>
<dd>List of ports, used in absence of -t and -p. </dd>
<dt><code>PORTS_FILE</code></dt>
<dd>File containing list of ports, used in absence of -t and -p. </dd>
</dl>
