---
title: "pbs_resources_sp2(7)"
name: "pbs_resources_sp2"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pbs_resources_sp2/"
description: "pbs_resources_sp2 – pbs resources on IBM SP-2"
---

<p>pbs_resources_sp2 &#8211; pbs resources on IBM SP-2</p>
<h2>Description</h2>
<p>This page summarizes the resources supported by PBS for the IBM SP-2. These resources are specified by including them in the <i>-l</i> option argument on the qsub or qalter command or in the PBS job script.</p>
<h2>Resources</h2>
<dl>
<dt>nice</p>
<dd>The nice value under which the job is to be run. Units: unitary.</p>
<dt>walltime</p>
<dd>Maximum amount of real time during which the job can be in the running state. Units: time.</p>
<dt>arch</p>
<dd>Specifies the administrator defined system architecture requried. This defaults to whatever the PBS_MACH string is set to in &quot;local.mk&quot;. Units: string.</p>
<dt>host</p>
<dd>Name of host on which job should be run. This resource is provided for use by the site&#8217;s scheduling policy. The allowable values and effect on job placement is site dependent. Units: string.</p>
<dt>nodes</p>
<dd>Number and/or type of nodes to be reserved for exclusive use by the job. The value is one or more <i>node_specs</i> joined with the &#8216;+&#8217; character, &quot;node_spec[+node_spec&#8230;]. Each node_spec is an <i>number</i> of nodes required of the type declared in the node_spec and a <i>name</i> or one or more <i>properity</i> or properities desired for the nodes. The number, the name, and each properity in the node_spec are separated by a colon &#8216;:&#8217;. If no number is specified, one (1) is assumed. Units: string.</p>
<dd>The name of a node is its hostname. The properities of nodes are:</p>
<dl>
<dd>
<dl>
<dt>.</p>
<dd>ppn=# specifying the number of processors per node requested. Defaults to 1.</p>
<dt>.</p>
<dd>arbitrary string assigned by the system administrator, please check with your administrator as to the node names and properities available to you.</dl>
</dl>
<dd>Examples:</p>
<dl>
<dd>
<dl>
<dt>.</p>
<dd>To ask for 12 nodes of any type: -l nodes=12</p>
<dt>.</p>
<dd>To ask for 2 &quot;server&quot; nodes and 14 other nodes (a total of 16): -l nodes=2:server+14<br />
 The above consist of two node_specs &quot;2:server&quot; and &quot;14&quot;.</p>
<dt>.</p>
<dd>To ask for (a) 1 node that is a &quot;server&quot; and has a &quot;hippi&quot; interface, (b) 10 nodes that are not servers, and (c) 3 nodes that have a large amount of memory an have hippi:<br />
 -l nodes=server:hippi+10:noserver+3:bigmem:hippi</p>
<dt>.</p>
<dd>To ask for three nodes by name:<br />
 -l nodes=b2005+b1803+b1813</p>
<dt>.</p>
<dd>To ask for 2 processors on each of four nodes:<br />
 -l nodes=4:ppn=2</p>
<dt>.</p>
<dd>To ask for 4 processors on one node:<br />
 -l nodes=1:ppn=4</p>
<dt>.</p>
<dd>To ask for 2 processors on each of two blue nodes and three processors on one red node:<br />
 -l nodes=2:blue:ppn=2+red:ppn=3</dl>
</dl>
<dt>host</p>
<dd>Allows a user to specify the desired execution location. This resource is provided for use by the site&#8217;s scheduling policy. The allowable values and effect on job placement is site dependent. Units: string.</p>
<dt>other</p>
<dd>Allows a user to specify site specific information. This resource is provided for use by the site&#8217;s scheduling policy. The allowable values and effect on job placement is site dependent. Units: string.</p>
<dt>software</p>
<dd>Allows a user to specify software required by the job. This is useful if certain software packages are only available on certain systems in the site. This resource is provided for use by the site&#8217;s scheduling policy. The allowable values and effect on job placement is site dependent. Units: string.</dl>
<h2>Examples</h2>
<p>qsub -l nodes=15,walltime=2:00:00 script or in a qsub script as a directive: #PBS -l nodes=15,walltime=2:00:00 </p>
<h2>Resource Units</h2>
<p>The resource values take the following units:</p>
<dl>
<dt>time</p>
<dd>specifies a maximum time period the resource can be used. Time is expressed in seconds as an integer, or in the form:<br />
 <code></p>
<dt>unitary</p>
<dd>The maximum amount of a resource which is expressed as a simple integer.</dl>
<p> </code></p>
<h2>See Also</h2>
<p>the PBS ERS, <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_submit/">pbs_submit</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_alterjob/">pbs_alterjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3b-pbs_statjob/">pbs_statjob</a>(3b) <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_aix4/">pbs_resources_aix4</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_irix5/">pbs_resources_irix5</a>(7B) <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_sunos4/">pbs_resources_sunos4</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_unicos8/">pbs_resources_unicos8</a>(7B) </p>
