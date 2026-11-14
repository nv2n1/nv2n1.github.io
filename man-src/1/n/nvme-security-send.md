---
title: "nvme-security-send(1)"
name: "nvme-security-send"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-security-send/"
---

<h2 class="name">NAME</h2>
 

 nvme-security-send - Security Send command 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme security - send[&lt;device&gt;][--file = &lt;file&gt; | -f&lt;file&gt;]
                    [--secp = &lt;security - protocol&gt; | -p&lt;security - protocol&gt;]
                    [--spsp = &lt;protocol - specific&gt; | -s&lt;protocol - specific&gt;]
                    [--tl = &lt;transfer - length&gt; | -t&lt;transfer - length&gt;]
                    [--nssf = &lt;nvme - specific&gt; | -N&lt;nvme - specific&gt;]
                    [--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
</code></pre>

<h2>DESCRIPTION</h2>

 

 The Security Send command is used to transfer security protocol data to the controller. The data structure transferred to the controller as part of this command contains security protocol specific commands to be performed by the controller. The data structure transferred may also contain data or parameters associated with the security protocol commands. Status and data that is to be returned to the host for the security protocol commands submitted by a Security Send command are retrieved with the Security Receive command. 

 The association between a Security Send command and subsequent Security Receive command is Security Protocol field dependent as defined in SPC-4.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Target a specific namespace for this security command.</dl>
 

 -N &lt;nssf&gt;, --nssf=&lt;nssf&gt;
<dl>
<dt>
<dd> NVMe Security Specific field. If using security protocol EAh assigned for NVMe use, the NVMe security specific field indicates which reply memory buffer target.</dl>
 

 -f &lt;file&gt;, --file=&lt;file&gt;
<dl>
<dt>
<dd> Path to file used as the security protocol's payload. Required argument.</dl>
 

 -p &lt;security-protocol&gt;, --secp=&lt;security-protocol&gt;
<dl>
<dt>
<dd> Security Protocol: This field specifies the security protocol as defined in SPC-4. The controller shall fail the command with Invalid Parameter indicated if a reserved value of the Security Protocol is specified.</dl>
 

 -s &lt;security-protocol-specific&gt;, --spsp=&lt;security-protocol-specific&gt;
<dl>
<dt>
<dd> SP Specific: The value of this field is specific to the Security Protocol as defined in SPC-4.</dl>
 

 -t &lt;trans-length&gt;, --tl=&lt;trans-length&gt;
<dl>
<dt>
<dd> Transfer Length: The value of this field is specific to the Security Protocol as defined in SPC-4.</dl>

<h2>EXAMPLES</h2>

 

 No Examples

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


