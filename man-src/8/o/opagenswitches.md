---
title: "opagenswitches(8)"
name: "opagenswitches"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opagenswitches/"
description: "opagenswitches"
---

<p>opagenswitches </p>
<p> Analyzes the present fabric and produces a list of Externally Managed switches in the required format for the /etc/sysconfig/opa/switches file.</p>
<h2>Syntax</h2>
<p>opagenswitches [-t portsfile] [-p ports] [-R] [-L switches_file] [-o output_file] [-T topology_file] [-X snapshot_file] [-s] [-v level] [-K]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd>Produces full help text.</dd>
<dt>-t <i>portsfile</i></dt>
<dd>File with list of local HFI ports used to access fabric(s) for analysis. Default is /etc/sysconfig/opa/ports file.</dd>
<dt>-p <i>ports</i></dt>
<dd>List of local HFI ports used to access fabrics for counter clear. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </dd>
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
<dt>-R</dt>
<dd>Does not attempt to get routes for computation of distance.</dd>
<dt>-s</dt>
<dd>Updates/resolves switch names using topology XML data.</dd>
<dt>-L <i>switches_file</i></dt>
<dd>Specifies the name of a pre-existing <i>switches_file</i> to be used as input in conjunction with a topology file. When specified, the file is used instead of switches data obtained from the actual fabric. The updated switches data is output to stdout (common to all opagenswitches operations). Does not generate switches data; must also use -s option. </dd>
<dt>-o <i>output_file</i></dt>
<dd>Writes switches data to <i>output_file</i>. Default is stdout.</dd>
<dt>-T <i>topology_file</i></dt>
<dd>Specifies <i>topology_file</i> to use. May contain &#8216;%P&#8217; . Must also use -s. </dd>
<dd>Link data in the topology file is compared to actual fabric link data (obtained by opareport -o links or opareport -X snapshot -o links). The data is also matched to a list of switch node GUIDs and the switch NodeDesc values are generated. This list is then applied to the switches data to update NodeDesc values. The comparison of topology link data to actual fabric link data starts with the host names. The host names in the actual fabric must match those in the topology file for the comparison to succeed. However, the comparison logic allows for some mismatches, which could be due to swapped or missing cables. Switch NodeDesc values are matched to GUIDs based on which switch has the greater number of matching links.</dd>
<dt>-X <i>snapshot_file</i></dt>
<dd>Uses <i>snapshot_file</i> XML for fabric link information.</dd>
<dt>-v <i>level</i></dt>
<dd>Verbose level. Default = 0. Values include:</dd>
<dl>
<dd>
</dd><dl>
<dd>0 No output.</dd></dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>1 Progress output.</dd></dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>2 Reserved.</dd></dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>4 Time stamps.</dd></dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>8 Reserved.</dd></dl>
</dl>
<dt>-K</dt>
<dd>Does not clean temporary files. Temporary files are CSV format and contain lists of links used during script operation. The files are not normally needed after execution, but they can be retained for subsequent inspection or processing. </dd>
</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>PORTS</code></dt>
<dd>List of ports, used in absence of -t and -p.</dd>
<dt><code>PORTS_FILE</code></dt>
<dd>File containing list of ports, used in absence of -t and -p.</dd>
<dt><code>FF_TOPOLOGY_FILE</code></dt>
<dd>File containing topology XML data, used in absence of -T.</dd></dl>
<h2>Examples</h2>
<p>opagenswitches<br/>
 opagenswitches -p &#8216;1:1 2:1&#8217;<br/>
 opagenswitches -o switches<br/>
 opagenswitches -s -o switches<br/>
 opagenswitches -L switches -s -o switches<br/>
 opagenswitches -s -T topology.%P.xml<br/>
 opagenswitches -L switches -s -T topology.%P.xml -X snapshot.%P.xml </p>
