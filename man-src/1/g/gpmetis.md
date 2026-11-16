---
title: "gpmetis(1)"
name: "gpmetis"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpmetis/"
description: "gpmetis – Partitions a graph into a specified number of parts."
---

<h2>NAME</h2>
<p> gpmetis &#8211; Partitions a graph into a specified number of parts.</p>
<h2>SYNOPSIS</h2>
<p> <code>gpmetis</code> [<i>options</i>] <i>graphfile nparts</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
</dt><dd> Required parameters</dd>
<dt>graphfile</dt>
<dd> Stores the graph to be partitioned.</dd>
<dt>nparts</dt>
<dd> The number of partitions to split the graph.</dd>
<dt>
</dt><dd> Optional parameters</dd>
<dt> <code>-ptype</code>=<i>string</i></dt>
<dd>Specifies the scheme to be used for computing the k-way partitioning. The possible values are:</dd>
<dt>rb</dt>
<dd> &#8211; Recursive bisectioning</dd>
<dt>kway</dt>
<dd> &#8211; Direct k-way partitioning [default]</dd>
<dt> <code>-ctype</code>=<i>string</i></dt>
<dd>Specifies the scheme to be used to match the vertices of the graph during the coarsening. The possible values are:</dd>
<dt>rm</dt>
<dd> &#8211; Random matching</dd>
<dt>shem</dt>
<dd> &#8211; Sorted heavy-edge matching [default]</dd>
<dt> <code>-iptype</code>=<i>string</i> [applies only when <code>-ptype</code>=<i>rb]</i></dt>
<dd>Specifies the scheme to be used to compute the initial partitioning of the graph. The possible values are:</dd>
<dt>grow</dt>
<dd> &#8211; Grow a bisection using a greedy scheme [default for ncon=1]</dd>
<dt>random</dt>
<dd> &#8211; Compute a bisection at random [default for ncon&gt;1]</dd>
<dt> <code>-objtype</code>=<i>string</i> [applies only when <code>-ptype</code>=<i>kway]</i></dt>
<dd>Specifies the objective that the partitioning routines will optimize. The possible values are:</dd>
<dt>cut</dt>
<dd> &#8211; Minimize the edgecut [default]</dd>
<dt>vol</dt>
<dd> &#8211; Minimize the total communication volume</dd>
<dt> <code>-no2hop</code></dt>
<dd>Specifies that the coarsening will not perform any 2-hop matchings when the standard matching fails to sufficiently contract the graph.</dd>
<dt> <code>-contig</code> [applies only when <code>-ptype</code>=<i>kway]</i></dt>
<dd>Specifies that the partitioning routines should try to produce partitions that are contiguous. Note that if the input graph is not connected this option is ignored.</dd>
<dt> <code>-minconn</code> [applies only when <code>-ptype</code>=<i>kway]</i></dt>
<dd>Specifies that the partitioning routines should try to minimize the maximum degree of the subdomain graph, i.e., the graph in which each partition is a node, and edges connect subdomains with a shared interface.</dd>
<dt> <code>-tpwgts</code>=<i>filename</i></dt>
<dd>Specifies the name of the file that stores the target weights for each partition. By default, all partitions are assumed to be of the same size.</dd>
<dt> <code>-ufactor</code>=<i>int</i></dt>
<dd>Specifies the maximum allowed load imbalance among the partitions. A value of x indicates that the allowed load imbalance is 1+x/1000. For ptype=rb, the load imbalance is measured as the ratio of the 2*max(left,right)/(left+right), where left and right are the sizes of the respective partitions at each bisection. For ptype=kway, the load imbalance is measured as the ratio of max_i(pwgts[i])/avgpwgt, where pwgts[i] is the weight of the ith partition and avgpwgt is the sum of the total vertex weights divided by the number of partitions requested. For ptype=rb, the default value is 1 (i.e., load imbalance of 1.001). For ptype=kway, the default value is 30 (i.e., load imbalance of 1.03).</dd>
<dt> <code>-ubvec</code>=<i>string</i></dt>
<dd>Applies only for multi-constraint partitioning and specifies the per constraint allowed load imbalance among partitions. The required parameter corresponds to a space separated set of floating point numbers, one for each of the constraints. For example, for three constraints, the string can be &quot;1.02 1.2 1.35&quot; indicating a desired maximum load imbalance of 2%, 20%, and 35%, respectively. The load imbalance is defined in a way similar to ufactor. If supplied, this parameter takes priority over ufactor.</dd>
<dt> <code>-niter</code>=<i>int</i></dt>
<dd>Specifies the number of iterations for the refinement algorithms at each stage of the uncoarsening process. Default is 10.</dd>
<dt> <code>-ncuts</code>=<i>int</i></dt>
<dd>Specifies the number of different partitionings that it will compute. The final partitioning is the one that achieves the best edgecut or communication volume. Default is 1.</dd>
<dt> <code>-nooutput</code></dt>
<dd>Specifies that no partitioning file should be generated.</dd>
<dt> <code>-seed</code>=<i>int</i></dt>
<dd>Selects the seed of the random number generator.</dd>
<dt> <code>-dbglvl</code>=<i>int</i></dt>
<dd>Selects the dbglvl.</dd>
<dt> <code>-help</code></dt>
<dd>Prints this message. </dd>
</dl>
<h2>Index</h2>
