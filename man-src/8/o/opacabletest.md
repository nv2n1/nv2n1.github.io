---
title: "opacabletest(8)"
name: "opacabletest"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opacabletest/"
description: "opacabletest"
---

<p>opacabletest </p>
<p> <code>(Switch)</code> Initiates or stops Cable Bit Error Rate stress tests for Intel(R) Omni-Path Host Fabric Interface (HFI)-to-switch links and/or ISLs.</p>
<h2>Syntax</h2>
<p>opacabletest [-C|-A] [-c <i>file</i>] [-f <i>hostfile</i>] [-h <i>&#8216;hosts&#8217;</i>] [-n <i>numprocs</i>] [-t#8217#160; <i>portsfile</i>] [-p <i>ports</i>] [start|start_fi|start_isl|stop|stop_fi| stop_isl] &#8230;</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-C</p>
<dd>Clears error counters. </p>
<dt>-A</p>
<dd>Forces clear of hardware error counters. Implies -C. </p>
<dt>-c <i>file</i></p>
<dd>Error thresholds configuration file. Default is /etc/sysconfig/opa/opamon.si.conf file. Only used if -C or -A specified. </p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts to include in HFI -to-SW test. Default is /etc/sysconfig/opa/hosts file. </p>
<dt>-h <i>hosts</i></p>
<dd>List of hosts to include in HFI -SW test. </p>
<dt>-n <i>numprocs</i></p>
<dd>Number of processes per host for HFI -SW test. </p>
<dt>-t <i>portsfile</i></p>
<dd>File with list of local HFI ports used to access fabrics when clearing counters. Default is /etc/sysconfig/opa/ports file. </p>
<dt>-p <i>ports</i></p>
<dd>List of local HFI ports used to access fabrics for counter clear. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </p>
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
<dt>start</p>
<dd>Starts the HFI -SW and ISL tests. </p>
<dt>start_fi</p>
<dd>Starts the HFI -SW test. </p>
<dt>start_isl</p>
<dd>Starts the ISL test. </p>
<dt>stop</p>
<dd>Stops the HFI -SW and ISL tests. </p>
<dt>stop_fi</p>
<dd>Stops the HFI -SW test. </p>
<dt>stop_isl</p>
<dd>Stops the ISL test. </p>
</dl>
<p> The HFI -SW cable test requires that the <code>FF_MPI_APPS_DIR</code> is set, and it contains a pre-built copy of the mpi_apps for an appropriate message passing interface (MPI). </p>
<p> The ISL cable test started by this tool assumes that the master Host Subnet Manager (HSM) is running on this host. If using the Embedded Subnet Manager (ESM), or if a different host is the master HSM, the ISL cable test must be controlled by the switch CLI, or by Intel(R) Omni-Path Fabric Suite FastFabric on the master HSM respectively.</p>
<h2>Examples</h2>
<p>opacabletest -A start<br />
 opacabletest -f good -A start<br />
 opacabletest -h &#8216;arwen elrond&#8217; start_fi<br />
 HOSTS=&#8217;arwen elrond&#8217; opacabletest stop<br />
 opacabletest -A</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts, used if -h option not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts, used in absence of -f and -h. </p>
<dt><code>PORTS</code></p>
<dd>List of ports, used in absence of -t and -p. </p>
<dt><code>PORTS_FILE</code></p>
<dd>File containing list of ports, used in absence of -t and -p. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>Maximum concurrent operations. </p>
</dl>
