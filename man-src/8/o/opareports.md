---
title: "opareports(8)"
name: "opareports"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opareports/"
description: "opareports"
---

<p>opareports </p>
<p> <code>(All)</code> opareports is a front end to opareport that provides many of the same options and capabilities. It can also run a report against multiple fabrics or subnets (for example, local host HFI ports). opareports can use an input file to augment the reports using additional details from the topology_input file.</p>
<h2>Syntax</h2>
<p>opareports [-t <i>portsfile</i>] [-p <i>ports</i>] [-T <i>topology_input</i>] [opareport <i>arguments</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text.</p>
<dt>-t <i>portsfile</i></p>
<dd>File with list of local HFI ports used to access fabric for analysis. Default is /etc/sysconfig/opa/ports file.</p>
<dt>-p <i>ports</i></p>
<dd>List of local HFI ports used to access fabric for counter clear. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </p>
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
<dt>-T <i>topology_input</i></p>
<dd>Name of a topology input file to use. The filename may have %P as a marker which is replaced with the hfi:port being operated on, such as 0:0 or 1:2. The default filename is specified by <code>FF_TOPOLOGY_FILE</code> as /etc/sysconfig/opa/topology.%P.xml. If -T NONE is specified, no topology input file is used.</p>
<dt>opareport <i>arguments</i></p>
<dd>Any of the other opareport arguments. The -h and -X options are not available. Note that the meaning of -p is different for opareports than opareport. When run against multiple fabrics, the -x and -o snapshot options are not available.</p>
<dd></dl>
<p> <code>NOTE:</code> When run against multiple fabrics, the -F option is applied to all fabrics. See <i>opareport</i> for more information.</p>
<h2>Example</h2>
<p>opareports opareports -p &#8216;1:1 2:1&#8217;</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></p>
<dd>List of ports, used in absence of -t and -p.</p>
<dt><code>PORTS_FILE</code></p>
<dd>File containing list of ports, used in absence of -t and -p.</p>
<dt><code>FF_TOPOLOGY_FILE</code></p>
<dd>File containing topology_input (may have %P marker in filename), used in absence of -T.</dl>
<h2>Details</h2>
<p>For simple fabrics, the Intel(R) Omni-Path Fabric Suite FastFabric Toolset host is connected to a single fabric. By default, the first active port on the FastFabric Toolset host is used to analyze the fabric. </p>
<p> However, in more complex fabrics, the FastFabric Toolset host may be connected to more than one fabric or subnet. In this case, you can specify the ports or HFIs to use with one of the following methods:</p>
<dl>
<dt>&bull;</p>
<dd>On the command line using the -p option.</p>
<dt>&bull;</p>
<dd>In a file specified using the -t option.</p>
<dt>&bull;</p>
<dd>Through the environment variables <code>PORTS</code> or <code>PORTS_FILE</code>.</p>
<dt>&bull;</p>
<dd>Using the ports_file configuration option in /etc/sysconfig/opa/opafastfabric.conf.</dl>
<p> If the specified port does not exist or is empty, the first active port on the local system is used. In more complex configurations, you must specify the exact ports to use for all fabrics to be analyzed. </p>
<p> You can specify the topology_input file to be used with one of the following methods:</p>
<dl>
<dt>&bull;</p>
<dd>On the command line using the -T option.</p>
<dt>&bull;</p>
<dd>In a file specified through the environment variable <code>FF_TOPOLOGY_FILE</code>.</p>
<dt>&bull;</p>
<dd>Using the ff_topology_file configuration option in opafastfabric.conf.</dl>
<p> If the specified file does not exist, no topology_input file is used. Alternately the filename can be specified as NONE to prevent use of an input file.</p>
