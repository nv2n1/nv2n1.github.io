---
title: "opafabricinfo(1)"
name: "opafabricinfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opafabricinfo/"
description: "opafabricinfo"
---

<h2>NAME</h2>
<p> opafabricinfo </p>
<p> Provides a brief summary of the components in the fabric, using the first active port on the given local host to perform its analysis. opafabricinfo is supplied in both:</p>
<dl>
<dt>&bull;</p>
<dd> Intel(R) Omni-Path Fabric Suite FastFabric Toolset In this situation, the command can manage more than one fabric (subnet). </p>
<dt>&bull;</p>
<dd> FastFabric Tools In this situation, the command performs analysis against the first active port on the system only. It takes no options and uses no environment variables. </p>
</dl>
<p> opafabricinfo can be very useful as a quick assessment of the fabric state. It can be run against a known good fabric to identify its components and then later run to see if anything has changed about the fabric configuration or state. </p>
<p> For more extensive fabric analysis, use <i>opareport</i> and <i>opareports</i> <i>Intel(R) Omni-Path Fabric Suite FastFabric User Guide</i> </p>
<h2>Syntax</h2>
<p> opafabricinfo [-t <i>portsfile</i>] [-p <i>ports</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd> Produces full help text.</p>
<dt>-t <i>portsfile</i></p>
<dd> File with list of local HFI ports used to access fabric(s) for analysis. Default is /etc/sysconfig/opa/ports file.</p>
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
<h2>Environment Variables</h2>
<p> The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></p>
<dd> List of ports, used in absence of -t and -p.</p>
<dt><code>PORTS_FILE</code></p>
<dd> File containing list of ports, used in absence of -t and -p. </p>
<dt>
<dd> For simple fabrics, the Intel(R) Omni-Path Fabric Suite FastFabric Toolset host is connected to a single fabric. By default, the first active port on the FastFabric Toolset host is used to analyze the fabric. However, in more complex fabrics, the FastFabric Toolset host may be connected to more than one fabric or subnet. In this case, you can specify the ports or HFIs to use with one of the following methods:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> On the command line using the -p option.</p>
<dt>&bull;</p>
<dd> In a file specified using the -t option.</p>
<dt>&bull;</p>
<dd> Through the environment variables <code>PORTS</code> or <code>PORTS_FILE</code>.</p>
<dt>&bull;</p>
<dd> Using the ports_file configuration option in opafastfabric.conf. </p>
</dl>
</dl>
<dt>
<dd> If the specified port does not exist or is empty, the first active port on the local system is used. In more complex configurations, you must specify the exact ports to use for all fabrics to be analyzed.</dl>
<h2>Example</h2>
<p> opafabricinfo<br />
 opafabricinfo -p &#8216;1:1 1:2 2:1 2:2&#8217; </p>
<p> <code>Output example</code> </p>
<p> # opafabricinfo<br />
 Fabric 0:0 Information:<br />
 SM: hds1fnb6241 hfi1_0 Guid: 0x0011750101575ffe State: Master<br />
 Number of HFIs: 8<br />
 Number of Switches: 1<br />
 Number of Links: 8<br />
 Number of HFI Links: 8 (Internal: 0 External: 8)<br />
 Number of ISLs: 0 (Internal: 0 External: 0)<br />
 Number of Degraded Links: 0 (HFI Links: 0 ISLs: 0)<br />
 Number of Omitted Links: 0 (HFI Links: 0 ISLs: 0) </p>
<h2>Index</h2>
