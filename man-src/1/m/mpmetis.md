---
title: "mpmetis(1)"
name: "mpmetis"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpmetis/"
description: "mpmetis – Partitions a mesh into a specified number of parts."
---

<h2>NAME</h2>
<p> mpmetis &#8211; Partitions a mesh into a specified number of parts.</p>
<h2>SYNOPSIS</h2>
<p> <code>mpmetis</code> [<i>options</i>] <i>meshfile nparts</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> Required parameters</p>
<dt>meshfile</p>
<dd> Stores the mesh to be partitioned.</p>
<dt>nparts</p>
<dd> The number of partitions to split the mesh.</p>
<dt>
<dd> Optional parameters</p>
<dt> <code>-gtype</code>=<i>string</i></p>
<dt>
<dd>
<dd>Specifies the graph to be used for computing the partitioning The possible values are:</p>
<dt>dual</p>
<dd> &#8211; Partition the dual graph of the mesh [default]</p>
<dt>nodal</p>
<dd> &#8211; Partition the nodal graph of the mesh</p>
<dt> <code>-ptype</code>=<i>string</i></p>
<dt>
<dd>
<dd>Specifies the scheme to be used for computing the k-way partitioning. The possible values are:</p>
<dt>rb</p>
<dd> &#8211; Recursive bisectioning</p>
<dt>kway</p>
<dd> &#8211; Direct k-way partitioning [default]</p>
<dt> <code>-ctype</code>=<i>string</i></p>
<dt>
<dd>
<dd>Specifies the scheme to be used to match the vertices of the graph during the coarsening. The possible values are:</p>
<dt>rm</p>
<dd> &#8211; Random matching</p>
<dt>shem</p>
<dd> &#8211; Sorted heavy-edge matching [default]</p>
<dt> <code>-iptype</code>=<i>string</i> [applies only when <code>-ptype</code>=<i>rb]</i></p>
<dt>
<dd>
<dd>Specifies the scheme to be used to compute the initial partitioning of the graph. The possible values are:</p>
<dt>grow</p>
<dd> &#8211; Grow a bisection using a greedy strategy [default]</p>
<dt>random</p>
<dd> &#8211; Compute a bisection at random</p>
<dt> <code>-objtype</code>=<i>string</i> [applies only when <code>-ptype</code>=<i>kway]</i></p>
<dt>
<dd>
<dd>Specifies the objective that the partitioning routines will optimize. The possible values are:</p>
<dt>cut</p>
<dd> &#8211; Minimize the edgecut [default]</p>
<dt>vol</p>
<dd> &#8211; Minimize the total communication volume</p>
<dt> <code>-contig</code> [applies only when <code>-ptype</code>=<i>kway]</i></p>
<dt>
<dd>
<dd>Specifies that the partitioning routines should try to produce partitions that are contiguous. Note that if the input graph is not connected this option is ignored.</p>
<dt> <code>-minconn</code> [applies only when <code>-ptype</code>=<i>kway]</i></p>
<dt>
<dd>
<dd>Specifies that the partitioning routines should try to minimize the maximum degree of the subdomain graph, i.e., the graph in which each partition is a node, and edges connect subdomains with a shared interface.</p>
<dt> <code>-tpwgts</code>=<i>filename</i></p>
<dt>
<dd>
<dd>Specifies the name of the file that stores the target weights for each partition. By default, all partitions are assumed to be of the same size.</p>
<dt> <code>-ufactor</code>=<i>int</i></p>
<dt>
<dd>
<dd>Specifies the maximum allowed load imbalance among the partitions. A value of x indicates that the allowed load imbalance is 1+x/1000. For ptype=rb, the load imbalance is measured as the ratio of the 2*max(left,right)/(left+right), where left and right are the sizes of the respective partitions at each bisection. For ptype=kway, the load imbalance is measured as the ratio of max_i(pwgts[i])/avgpwgt, where pwgts[i] is the weight of the ith partition and avgpwgt is the sum of the total vertex weights divided by the number of partitions requested. For ptype=rb, the default value is 1 (i.e., load imbalance of 1.001). For ptype=kway, the default value is 30 (i.e., load imbalance of 1.03).</p>
<dt> <code>-ncommon</code>=<i>int</i></p>
<dt>
<dd>
<dd>Specifies the common number of nodes that two elements must have in order to put an edge between them in the dual graph. Default is 1.</p>
<dt> <code>-niter</code>=<i>int</i></p>
<dt>
<dd>
<dd>Specifies the number of iterations for the refinement algorithms at each stage of the uncoarsening process. Default is 10.</p>
<dt> <code>-ncuts</code>=<i>int</i></p>
<dt>
<dd>
<dd>Specifies the number of different partitionings that it will compute. The final partitioning is the one that achieves the best edgecut or communication volume. Default is 1.</p>
<dt> <code>-nooutput</code></p>
<dt>
<dd>
<dd>Specifies that no partitioning file should be generated.</p>
<dt> <code>-seed</code>=<i>int</i></p>
<dt>
<dd>
<dd>Selects the seed of the random number generator.</p>
<dt> <code>-dbglvl</code>=<i>int</i></p>
<dt>
<dd>
<dd>Selects the dbglvl.</p>
<dt> <code>-help</code></p>
<dt>
<dd>
<dd>Prints this message. </p>
</dl>
<h2>Index</h2>
