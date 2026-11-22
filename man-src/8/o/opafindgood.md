---
title: "opafindgood(8)"
name: "opafindgood"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opafindgood/"
description: "opafindgood Checks for hosts that are able to be pinged, accessed via SSH, and active on the Intel(R) Omni-Path Fabric. Produces a list of good hosts meeting all criteria. Typically used to identif..."
---

<p>opafindgood Checks for hosts that are able to be pinged, accessed via SSH, and active on the Intel(R) Omni-Path Fabric. Produces a list of good hosts meeting all criteria. Typically used to identify good hosts to undergo further testing and benchmarking during initial cluster staging and startup. The resulting good file lists each good host exactly once and can be used as input to create <i>mpi_hosts</i> files for running mpi_apps and the HFI-SW cable test. The files alive, running, active, good, and bad are created in the selected directory listing hosts passing each criteria. This command assumes the Node Description for each host is based on the <i>hostname</i>-s output in conjunction with an optional hfi1_# suffix. When using a /etc/sysconfig/opa/hosts file that lists the hostnames, this assumption may not be correct. This command automatically generates the file FF_RESULT_DIR/punchlist.csv. This file provides a concise summary of the bad hosts found. This can be imported into Excel directly as a *.csv file. Alternatively, it can be cut/pasted into Excel, and the <code>Data/Text to Columns</code> toolbar can be used to separate the information into multiple columns at the semicolons. A sample generated output is:<br/>
 # opafindgood<br/>
 3 hosts will be checked<br/>
 2 hosts are pingable (alive)<br/>
 2 hosts are ssh&#8217;able (running)<br/>
 2 total hosts have FIs active on one or more fabrics (active)<br/>
 No Quarantine Node Records Returned<br/>
 1 hosts are alive, running, active (good)<br/>
 2 hosts are bad (bad)<br/>
 Bad hosts have been added to /root/punchlist.csv<br/>
 # cat /root/punchlist.csv<br/>
 2015/10/04 11:33:22;phs1fnivd13u07n1 hfi1_0 p1 phs1swivd13u06 p16;Link errors<br/>
 2015/10/07 10:21:05;phs1swivd13u06;Switch not found in SA DB<br/>
 2015/10/09 14:36:48;phs1fnivd13u07n4;Doesn&#8217;t ping<br/>
 2015/10/09 14:36:48;phs1fnivd13u07n3;No active port  For a given run, a line is generated for each failing host. Hosts are reported exactly once for a given run. Therefore, a host that does not ping is NOT listed as can&#8217;t ssh nor No active port. There may be cases where ports could be active for hosts that do not ping, especially if Ethernet host names are used for the ping test. However, the lack of ping often implies there are other fundamental issues, such as PXE boot or inability to access DNS or DHCP to get proper host name and IP address. Therefore, reporting hosts that do not ping is typically of limited value. Note that opafindgood queries the SA for NodeDescriptions to determine hosts with active ports. As such, ports may be active for hosts that cannot be accessed via SSH or pinged. By default, opafindgood checks for and reports nodes that are quarantined for security reasons. To skip this, use the -Q option.</p>
<h2>Syntax</h2>
<p>opafindgood [-R|-A|-Q] [-d <i>dir</i>] [-f <i>hostfile</i>] [-h &#8216;<i>hosts</i>&#8216;] [-t <i>portsfile</i>]<br/>
 [-p <i>ports</i>] [-T <i>timelimit</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd>Produces full help text.</dd>
<dt>-R</dt>
<dd>Skips the running test (SSH). Recommended if password-less SSH is not set up.</dd>
<dt>-A</dt>
<dd>Skips the active test. Recommended if Intel(R) Omni-Path Fabric software or fabric is not up.</dd>
<dt>-Q</dt>
<dd>Skips the quarantine test. Recommended if Intel(R) Omni-Path Fabric software or fabric is not up.</dd>
<dt>-d <i>dir</i></dt>
<dd>Directory in which to create alive, active, running, good, and bad files. Default is /etc/sysconfig/opa directory.</dd>
<dt>-f <i>hostfile</i></dt>
<dd>File with hosts in cluster. Default is /etc/sysconfig/opa/hosts directory.</dd>
<dt>-h <i>hosts</i></dt>
<dd>List of hosts to ping.</dd>
<dt>-t <i>portsfile</i></dt>
<dd>File with list of local HFI ports used to access fabric(s) for analysis. Default is /etc/sysconfig/opa/ports file.</dd>
<dt>-p <i>ports</i></dt>
<dd>List of local HFI ports used to access fabric(s) for analysis. The default is the first active port. The first HFI in the system is 1. The first port on an HFI is 1.Uses the format hfi:port, for example:</dd>
<dl>
<dd>
</dd><dl>
<dd>0:0 First active port in system.</dd></dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>0: <i>y</i> Port <i>y</i> within system.</dd></dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>&nbsp;<wbr><i>x</i>:0&nbsp;<wbr> First active port on HFI <i>x</i>.</dd></dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>&nbsp;<wbr><i>x</i>:&nbsp;<wbr><i>y</i>&nbsp;<wbr> HFI <i>x</i>, port <i>y</i>.</dd></dl>
</dl>
<dt>-T <i>timelimit</i></dt>
<dd>Time limit in seconds for host to respond to SSH. Default = 20 seconds. </dd>
</dl>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></dt>
<dd>List of hosts, used if -h option not supplied. </dd>
<dt><code>HOSTS_FILE</code></dt>
<dd>File containing list of hosts, used in absence of -f and -h. </dd>
<dt><code>PORTS</code></dt>
<dd>List of ports, used in absence of -t and -p. </dd>
<dt><code>PORTS_FILE</code></dt>
<dd>File containing list of ports, used in absence of -t and -p. </dd>
<dt><code>FF_MAX_PARALLEL</code></dt>
<dd>Maximum concurrent operations. </dd>
</dl>
<h2>Examples</h2>
<p>opafindgood<br/>
 opafindgood -f allhosts<br/>
 opafindgood -h &#8216;arwen elrond&#8217;<br/>
 HOSTS=&#8217;arwen elrond&#8217; opafindgood<br/>
 HOSTS_FILE=allhosts opafindgood<br/>
 opafindgood -p &#8216;1:1 1:2 2:1 2:2&#8217; </p>
