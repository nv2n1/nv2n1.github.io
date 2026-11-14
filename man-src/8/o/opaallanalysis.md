---
title: "opaallanalysis(8)"
name: "opaallanalysis"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaallanalysis/"
description: "opaallanalysis"
---

<p>opaallanalysis </p>
<p> <code>(All)</code> opaallanalysis command performs the set of analysis specified in FF_ALL_ANALYSIS and can be specified for fabric, chassis, esm, or hostsm.</p>
<h2>Syntax</h2>
<p>opaallanalysis [-b|-e] [-s] [-d <i>dir</i>] [-c <i>file</i>] [-t <i>portsfile</i>] [-p <i>ports</i>] [-F#8217#160; <i>chassisfile</i>] [-H &#8216;<i>chassis</i>&#8216;] [-G <i>esmchassisfile</i>] [-E <i>esmchassis</i>] [-T <i>topology_input</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text.</p>
<dt>-b</p>
<dd>Baseline mode. Default is compare/check mode.</p>
<dt>-e</p>
<dd>Evaluates health only. Default is compare/check mode.</p>
<dt>-s</p>
<dd>Saves history of failures (errors/differences).</p>
<dt>-d <i>dir</i></p>
<dd>Top-level directory for saving baseline and history of failed checks. Default = /var/lib/opa-ff/analysis</p>
<dt>-c <i>file</i></p>
<dd>Error thresholds configuration file. Default = /etc/sysconfig/opa/opamon.conf</p>
<dt>-t <i>portsfile</i></p>
<dd>File with list of local HFI ports used to access fabric(s) for analysis. Default = /etc/sysconfig/opa/ports</p>
<dt>-p <i>ports</i></p>
<dd>List of local HFI ports used to access fabric(s) for analysis. Default is the first active port. Specified as HFI:port as follows:</p>
<dl>
<dd>
<dl>
<dd>0:0 First active port in system.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>0: <i>y</i> Port <i>y</i> within system.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>&nbsp;<wbr><i>x</i>:0&nbsp;<wbr> First active port on HFI <i>x</i>.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>&nbsp;<wbr><i>x</i>:&nbsp;<wbr><i>y</i>&nbsp;<wbr> HFI <i>x</i>, port <i>y</i>.</dl>
</dl>
<dt>-F#8217#160; <i>chassisfile</i></p>
<dd>File with a chassis in a cluster. Default = /etc/sysconfig/opa/chassis</p>
<dt>-H &#8216;<i>chassis</i>&#8216;</p>
<dd>List of chassis on which to execute the command.</p>
<dt>-G <i>esmchassisfile</i></p>
<dd>File with embedded SM chassis in the cluster. Default = /etc/sysconfig/opa/esm_chassis</p>
<dt>-E <i>esmchassis</i></p>
<dd>List of embedded SM chassis to analyze.</p>
<dt>-T <i>topology_input</i></p>
<dd>Name of topology input file to use. Any %P markers in this filename are replaced with the HFI:port being operated on, such as 0:0 or 1:2. Default = /etc/sysconfig/opa/topology.%P.xml. If -T NONE is specified, no topology input file is used. See <i>opareport</i> for more information.</dl>
<h2>Example</h2>
<p>opaallanalysis<br />
 opaallanalysis -p &#8216;1:1 2:1&#8217;</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></p>
<dd>List of ports, used in absence of -t and -p.</p>
<dt><code>PORTS_FILE</code></p>
<dd>File containing list of ports, used in absence of -t and -p.</p>
<dt><code>FF_TOPOLOGY_FILE</code></p>
<dd>File containing topology_input (may have %P marker in filename), used in absence of -T.</p>
<dt><code>CHASSIS</code></p>
<dd>List of chassis, used if -F and -H options are not supplied.</p>
<dt><code>CHASSIS_FILE</code></p>
<dd>File containing list of chassis, used if -F and -H options are not supplied.</p>
<dt><code>ESM_CHASSIS</code></p>
<dd>List of SM chassis, used if -G and -E options are not supplied.</p>
<dt><code>ESM_CHASSIS_FILE</code></p>
<dd>File containing list of SM chassis, used if -G and -E options are not supplied.</p>
<dt><code>FF_ANALYSIS_DIR</code></p>
<dd>Top level directory for baselines and failed health checks.</dl>
<h2>Details</h2>
<p>The opaallanalysis command performs the set of analysis specified in <code>FF_ALL_ANALYSIS</code>, which must be a space-separated list. This can be provided by the environment or using /etc/sysconfig/opa/opafastfabric.conf. The analysis set includes the options: fabric, chassis, esm, or hostsm. </p>
<p> Note that the opaallanalysis command has options which are a super-set of the options for all other analysis commands. The options are passed along to the respective tools as needed. For example, the -c file option is passed on to opafabricanalysis if it is specified in <code>FF_ALL_ANALYSIS</code>. </p>
<p> The output files are all the output files for the <code>FF_ALL_ANALYSIS</code> selected set of analysis. See the previous sections for the specific output files.</p>
