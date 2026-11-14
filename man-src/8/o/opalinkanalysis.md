---
title: "opalinkanalysis(8)"
name: "opalinkanalysis"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opalinkanalysis/"
description: "opalinkanalysis"
---

<p>opalinkanalysis </p>
<p> <code>(Switch)</code> Encapsulates the capabilities for link analysis. Additionally, this tool includes cable and fabric topology verification capabilities. This tool is built on top of opareport (and its analysis capabilities), and accepts the same syntax for input topology and snapshot files. </p>
<p> In addition to being able to run assorted opareport link analysis reports, and generate human-readable output, this tool additionally analyzes the results and appends a concise summary of issues found to the FF_RESULT_DIR/punchlist.csv file.</p>
<h2>Syntax</h2>
<p>opalinkanalysis [-U] [-t <i>portsfile</i>] [-p <i>ports</i>] [-T <i>topology_input</i>] [-X <i>snapshot_input</i>] [-x <i>snapshot_suffix</i>] [-c <i>file</i>] reports &#8230;</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-U</p>
<dd>Omits unexpected devices and links in punchlist file from verify reports. </p>
<dt>-t <i>portsfile</i></p>
<dd>File with list of local HFI ports used to access fabric(s) for analysis, default is /etc/sysconfig/opa/ports. </p>
<dt>-p <i>ports</i></p>
<dd>List of local HFI ports used to access fabric(s) for analysis. The default is the first active port. The first HFI in the system is 1. The first port on an HFI is 1. </p>
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
<dd>Name of a topology input file to use. Any #8217#160; %P markers in this filename are replaced with the hfi:port being operated on (such as 0:0 or 1:2). Default is /etc/sysconfig/opa/topology.%P.xml. If NONE is specified, does not use any topology_input files. See <i>opareport</i> for more information on topology_input files. </p>
<dt>-X <i>snapshot_input</i></p>
<dd>Performs analysis using data in <i>snapshot_input</i>. <i>snapshot_input</i> must have been generated via a previous opareport -o snapshot run. If an errors report is specified, snapshot must have been generated with the opareport -s option. When this option is used, only one port may be specified to select a topology_input file (unless -T specified). When this option is used, clearerrors and clearhwerrors reports are not permitted. </p>
<dt>-x <i>snapshot_suffix</i></p>
<dd>Creates a snapshot file per selected port. The files are created in FF_RESULT_DIR with names of the form: snapshotSUFFIX. <i>HFI:PORT</i>.xml. </p>
<dt>-c <i>file</i></p>
<dd>Error thresholds configuration file. The default is /etc/sysconfig/opa/opamon.si.conf. </p>
<dt>
&nbsp;<wbr><i>reports</i>&nbsp;<wbr></p>
<dd>The following reports are supported:</p>
<dl>
<dd>
<dl>
<dd>errors Link error analysis. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>slowlinks Links running slower than expected. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>misconfiglinks Links configured to run slower than supported. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>misconnlinks Links connected with mismatched speed potential. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>all Includes all reports above. (errors, slowlinks, misconfiglinks, and misconnlinks) </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>verifylinks Verifies links against topology input. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>verifyextlinks Verifies links against topology input. Limit analysis to links external to systems. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>verifyfis Verifies FIs against topology input. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>verifysws Verifies switches against topology input.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>verifyrtrs Verifies routers against topology input. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>verifynodes Verifies FIs, switches, and routers against topology input. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>verifysms Verifies SMs against topology input. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>verifyall Verifies links, FIs, switches, routers, and SMs against topology input. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>clearerrors Clears error counters, uses PM if available. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>clearhwerrors Clears hardware error counters, bypasses PM. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>clear Includes clearerrors and clearhwerrors. </p>
</dl>
</dl>
</dl>
<p> A punchlist of bad links is also appended to the file: FF_RESULT_DIR/punchlist.csv</p>
<h2>Examples</h2>
<p>opalinkanalysis errors<br />
 opalinkanalysis errors clearerrors<br />
 opalinkanalysis -p &#8216;1:1 1:2 2:1 2:2&#8217;</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></p>
<dd>List of ports, used in absence of -t and -p. </p>
<dt><code>PORTS_FILE</code></p>
<dd>File containing list of ports, used in absence of -t and -p. </p>
<dt><code>FF_TOPOLOGY_FILE</code></p>
<dd>File containing <i>topology_input</i>, used in absence of -T. </p>
</dl>
