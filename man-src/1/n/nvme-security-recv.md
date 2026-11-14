---
title: "nvme-security-recv(1)"
name: "nvme-security-recv"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-security-recv/"
---

<h2 class="name">NAME</h2>
 

 nvme-security-recv - Security Recv command 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme security - recv[&lt;device&gt;][--size = &lt;size&gt; | -x&lt;size&gt;]
                    [--secp = &lt;security - protocol&gt; | -p&lt;security - protocol&gt;]
                    [--spsp = &lt;protocol - specific&gt; | -s&lt;protocol - specific&gt;]
                    [--nssf = &lt;nvme - specific&gt; | -N&lt;nvme - specific&gt;]
                    [--tl = &lt;transfer - length&gt; | -t&lt;transfer - length&gt;]
                    [--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
                    [-b | --raw - binary]
</code></pre>

<h2>DESCRIPTION</h2>

 

 The Security Receive command transfers the status and data result of one or more Security Send commands that were previously submitted to the controller. 

 The association between a Security Receive command and previous Security Send commands is dependent on the Security Protocol. The format of the data to be transferred is dependent on the Security Protocol. Refer to SPC-4 for Security Protocol details. 

 Each Security Receive command returns the appropriate data corresponding to a Security Send command as defined by the rules of the Security Protocol. The Security Receive command data may not be retained if there is a loss of communication between the controller and host, or if a controller reset occurs.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Target a specific namespace for this security command.</dl>
 

 -N &lt;nssf&gt;, --nssf=&lt;nssf&gt;
<dl>
<dt>
<dd> NVMe Security Specific field. If using security protocol EAh assigned for NVMe use, the NVMe security specific field indicates which reply memory buffer target.</dl>
 

 -x &lt;size&gt;, --size=&lt;size&gt;
<dl>
<dt>
<dd> Size of buffer to allocate. One success it will be printed to STDOUT.</dl>
 

 -p &lt;security-protocol&gt;, --secp=&lt;security-protocol&gt;
<dl>
<dt>
<dd> Security Protocol: This field specifies the security protocol as defined in SPC-4. The controller shall fail the command with Invalid Parameter indicated if a reserved value of the Security Protocol is specified.</dl>
 

 -s &lt;security-protocol-specific&gt;, --spsp=&lt;security-protocol-specific&gt;
<dl>
<dt>
<dd> SP Specific: The value of this field is specific to the Security Protocol as defined in SPC-4.</dl>
 

 -a &lt;allocation-length&gt;, --al=&lt;allocation-length&gt;
<dl>
<dt>
<dd> Allocation Length: The value of this field is specific to the Security Protocol as defined in SPC-4.</dl>
 

 -b, --raw-binary
<dl>
<dt>
<dd> Print the raw buffer to stdout. Defaults to print in hex.</dl>

<h2>EXAMPLES</h2>

 

 No Examples

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


