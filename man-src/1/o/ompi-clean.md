---
title: "ompi-clean(1)"
name: "ompi-clean"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ompi-clean/"
description: "orte-clean – Cleans up any stale processes and files leftover from Open MPI jobs."
---

<h2 class="name">NAME</h2>
<p> <code>orte-clean</code> &#8211; Cleans up any stale processes and files leftover from Open MPI jobs. </p>
<h2>SYNOPSIS</h2>
<pre><code>
orte - clean[--verbose]

    mpirun-- pernode[--host | --hostfile file] orte -
    clean[--verbose]
</code></pre>
<h2>OPTIONS</h2>
<p> [-v | &#8211;verbose] This argument will run the command in verbose mode and print out the universes that are getting cleaned up as well as processes that are being killed. </p>
<h2>DESCRIPTION</h2>
<p> <i>orte-clean</i> attempts to clean up any processes and files left over from Open MPI jobs that were run in the past as well as any currently running jobs. This includes OMPI infrastructure and helper commands, any processes that were spawned as part of the job, and any temporary files. orte-clean will only act upon processes and files that belong to the user running the orte-clean command. If run as root, it will kill off processes belonging to any users. </p>
<p> When run from the command line, orte-clean will attempt to clean up the local node it is run from. When launched via mpirun, it will clean up the nodes selected by mpirun. </p>
<h2>EXAMPLES</h2>
<p> Example 1: Clean up local node only. </p>
<pre>
example% orte-clean
</pre>
<p> Example 2: To clean up on a specific set of nodes specified on command line, it is recommended to use the pernode option. This will run one orte-clean for each node. </p>
<pre>
example% mpirun --pernode --host node1,node2,node3 orte-clean
</pre>
<p> To clean up on a specific set of nodes from a file. </p>
<pre>
example% mpirun --pernode --hostfile nodes_file orte-clean
</pre>
<p> Example 3: Within a resource managed environment like N1GE, SLURM, or Torque. The following example is from N1GE. </p>
<p> First, we see that we have two nodes with two CPUs each. </p>
<pre>
example% qsh -pe orte 4
<br>
example% mpirun -np 4 hostname
<br>
node1
<br>
node1
<br>
node2
<br>
node2
</pre>
<p> Clean up all the nodes in the cluster. </p>
<pre>
example% mpirun --pernode orte-clean
</pre>
<p> Clean up a subset of the nodes in the cluster. </p>
<pre>
example% mpirun --pernode --host node1 orte-clean
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-orterun/">orterun</a>(1), <a href="/docs/linux/man/1-orte-ps/">orte-ps</a>(1) </p>
<h2>Index</h2>
