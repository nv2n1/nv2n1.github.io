---
title: "opagenesmchassis(8)"
name: "opagenesmchassis"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opagenesmchassis/"
description: "opagenesmchassis"
---

<p>opagenesmchassis </p>
<p> Generates a list of chassis IPv4 and IPv6 addresses and/or TCP names where the Embedded Subnet Manager (ESM) is running, in a format acceptable for inclusion in the /etc/sysconfig/opa/esm_chassis file. This tool uses opagenchassis output to iterate through all the chassis.</p>
<h2>Syntax</h2>
<p>opagenesmchassis [-u user] [-S] [-t <i>portsfile</i>] [-p <i>ports</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd>Produces full help text.</dd>
<dt>-u <i>user</i></dt>
<dd>User to perform command as. For chassis, the default is admin.</dd>
<dt>-S</dt>
<dd>Securely prompts for password for user on chassis.</dd>
<dt>-t <i>portsfile</i></dt>
<dd>File with a list of local HFI ports used to access fabric(s) for analysis. Default is /etc/sysconfig/opa/ports</dd>
<dt>-p <i>ports</i></dt>
<dd>List of local HFI ports used to access fabric(s). Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </dd>
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
<h2>Environment Variables</h2>
<dl>
<dt><code>FF_CHASSIS_ADMIN_PASSWORD</code></dt>
<dd>Password for chassis, used in absence of -S.</dd>
<dt><code>PORTS</code></dt>
<dd>List of ports, used in absence of -t and -p.</dd>
<dt><code>PORTS_FILE</code></dt>
<dd>File containing list of ports, used in absence of -t and -p.</dd></dl>
<h2>Examples</h2>
<p>opagenesmchassis<br/>
 opagenesmchassis -S -p &#8216;1:1 1:2 2:1 2:2&#8217; Alternatively, while editing the file, use a vi command to include the output such as:<br/>
 :r! opagenesmchassis </p>
