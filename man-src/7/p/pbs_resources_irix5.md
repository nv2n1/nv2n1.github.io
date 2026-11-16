---
title: "pbs_resources_irix5(7)"
name: "pbs_resources_irix5"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pbs_resources_irix5/"
description: "pbs_resources_irix – pbs resources on SGI Irix"
---

<p>pbs_resources_irix &#8211; pbs resources on SGI Irix</p>
<h2>Description</h2>
<p>This page summarizes the resources supported by PBS for SGI workstations running IRIX 5. These resources are specified by including them in the <i>-l</i> option argument on the qsub or qalter command or in the PBS job script. </p>
<h2>Resources</h2>
<dl>
<dt>cput</dt>
<dd>Maximum amount of CPU time used by all processes in the job. Units: time.</dd>
<dt>file</dt>
<dd>The largest size of any single file that may be created by the job. Units: size.</dd>
<dt>nice</dt>
<dd>The nice value under which the job is to be run. Units: unitary.</dd>
<dt>pcput</dt>
<dd>Maximum amount of CPU time used by any single process in the job. Units: time.</dd>
<dt>pmem</dt>
<dd>Maximum amount of physical memory (workingset) used by any single process of the job. Units: size.</dd>
<dt>pvmem</dt>
<dd>Maximum amount of virtual memory used by any single process in the job. Units: size.</dd>
<dt>vmem</dt>
<dd>Maximum amount of virtual memory used by all concurrent processes in the job. Units: size.</dd>
<dt>walltime</dt>
<dd>Maximum amount of real time during which the job can be in the running state. Units: time.</dd>
<dt>arch</dt>
<dd>Specifies the administrator defined system architecture requried. This defaults to whatever the PBS_MACH string is set to in &quot;local.mk&quot;. Units: string.</dd>
<dt>host</dt>
<dd>Name of host on which job should be run. This resource is provided for use by the site&#8217;s scheduling policy. The allowable values and effect on job placement is site dependent. Units: string.</dd>
<dt>nodes</dt>
<dd>Number and/or type of nodes to be reserved for exclusive use by the job. The value is one or more <i>node_specs</i> joined with the &#8216;+&#8217; character, &quot;node_spec[+node_spec&#8230;]. Each node_spec is an <i>number</i> of nodes required of the type declared in the node_spec and a <i>name</i> or one or more <i>properity</i> or properities desired for the nodes. The number, the name, and each properity in the node_spec are separated by a colon &#8216;:&#8217;. If no number is specified, one (1) is assumed. Units: string.</dd>
<dd>The name of a node is its hostname. The properities of nodes are:</dd>
<dl>
<dd>
</dd><dl>
<dt>.</dt>
<dd>ppn=# specifying the number of processors per node requested. Defaults to 1.</dd>
<dt>.</dt>
<dd>arbitrary string assigned by the system administrator, please check with your administrator as to the node names and properities available to you.</dd></dl>
</dl>
<dd>Examples:</dd>
<dl>
<dd>
</dd><dl>
<dt>.</dt>
<dd>To ask for 12 nodes of any type: -l nodes=12</dd>
<dt>.</dt>
<dd>To ask for 2 &quot;server&quot; nodes and 14 other nodes (a total of 16): -l nodes=2:server+14<br />
 The above consist of two node_specs &quot;2:server&quot; and &quot;14&quot;.</dd>
<dt>.</dt>
<dd>To ask for (a) 1 node that is a &quot;server&quot; and has a &quot;hippi&quot; interface, (b) 10 nodes that are not servers, and (c) 3 nodes that have a large amount of memory an have hippi:<br />
 -l nodes=server:hippi+10:noserver+3:bigmem:hippi</dd>
<dt>.</dt>
<dd>To ask for three nodes by name:<br />
 -l nodes=b2005+b1803+b1813</dd>
<dt>.</dt>
<dd>To ask for 2 processors on each of four nodes:<br />
 -l nodes=4:ppn=2</dd>
<dt>.</dt>
<dd>To ask for 4 processors on one node:<br />
 -l nodes=1:ppn=4</dd>
<dt>.</dt>
<dd>To ask for 2 processors on each of two blue nodes and three processors on one red node:<br />
 -l nodes=2:blue:ppn=2+red:ppn=3</dd></dl>
</dl>
<dt>host</dt>
<dd>Allows a user to specify the desired execution location. This resource is provided for use by the site&#8217;s scheduling policy. The allowable values and effect on job placement is site dependent. Units: string.</dd>
<dt>other</dt>
<dd>Allows a user to specify site specific information. This resource is provided for use by the site&#8217;s scheduling policy. The allowable values and effect on job placement is site dependent. Units: string.</dd>
<dt>software</dt>
<dd>Allows a user to specify software required by the job. This is useful if certain software packages are only available on certain systems in the site. This resource is provided for use by the site&#8217;s scheduling policy. The allowable values and effect on job placement is site dependent. Units: string.</dd></dl>
<h2>Examples</h2>
<p>qsub -l nodes=15,walltime=2:00:00 script or in a qsub script as a directive: #PBS -l nodes=15,walltime=2:00:00 qsub -l cput=1:00:00,walltime=2:00:00,file=50gb,mem=15mb script<br />
 qalter -lcput=30:00,pmem=8mb 123.jobid or in a qsub script as a directive: #PBS -l cput=1:00:00,walltime=2:00:00,file=50gb,mem=15mb </p>
<h2>Resource Units</h2>
<p>The resource values take the following units:</p>
<dl>
<dt>time</dt>
<dd>specifies a maximum time period the resource can be used. Time is expressed in seconds as an integer, or in the form:<br />
 <code></dd>
<dt>size</dt>
<dd>specifies the maximum amount in terms of bytes or words. It is expressed in the form The suffix is a multiplier defined in the following table, The size of a word is the word size on the execution host.</dd>
<dl>
<dd>
</dd><dl>
<dt>&nbsp;<wbr>b or&nbsp;<wbr>&nbsp;<wbr>w</dt>
<dd>bytes or words.</dd>
<dt>kb or kw</dt>
<dd>Kilo (1024) bytes or words.</dd>
<dt>mb or mw</dt>
<dd>Mega (1,048,576) bytes or words.</dd>
<dt>gb or gw</dt>
<dd>Giga (1,073,741,824) bytes or words.</dd></dl>
</dl>
<dt>unitary</dt>
<dd>The maximum amount of a resource which is expressed as a simple integer.</dd></dl>
<p> </code></p>
<h2>See Also</h2>
<p>the PBS ERS, qsub(1B), qalter(1B), pbs_submit(3B), pbs_alterjob(3B), pbs_statjob(3b) pbs_resources_aix4(7B), pbs_resources_sp2(7B), pbs_resources_sunos4(7B), pbs_resources_unicos8(7B) </p>
