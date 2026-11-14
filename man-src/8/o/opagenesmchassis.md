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
<dt>&#8211;help</p>
<dd>Produces full help text.</p>
<dt>-u <i>user</i></p>
<dd>User to perform command as. For chassis, the default is admin.</p>
<dt>-S</p>
<dd>Securely prompts for password for user on chassis.</p>
<dt>-t <i>portsfile</i></p>
<dd>File with a list of local HFI ports used to access fabric(s) for analysis. Default is /etc/sysconfig/opa/ports</p>
<dt>-p <i>ports</i></p>
<dd>List of local HFI ports used to access fabric(s). Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </p>
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
</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>FF_CHASSIS_ADMIN_PASSWORD</code></p>
<dd>Password for chassis, used in absence of -S.</p>
<dt><code>PORTS</code></p>
<dd>List of ports, used in absence of -t and -p.</p>
<dt><code>PORTS_FILE</code></p>
<dd>File containing list of ports, used in absence of -t and -p.</dl>
<h2>Examples</h2>
<p>opagenesmchassis<br />
 opagenesmchassis -S -p &#8216;1:1 1:2 2:1 2:2&#8217; Alternatively, while editing the file, use a vi command to include the output such as:<br />
 :r! opagenesmchassis </p>
