---
title: "ndmetis(1)"
name: "ndmetis"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndmetis/"
description: "ndmetis – Computes a fill-reducing ordering of the vertices of the graph using multilevel nested dissection."
---

<h2>NAME</h2>
<p> ndmetis &#8211; Computes a fill-reducing ordering of the vertices of the graph using multilevel nested dissection.</p>
<h2>SYNOPSIS</h2>
<p> <code>ndmetis</code> [<i>options</i>] <i>&lt;filename&gt;</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> Required parameters</p>
<dt>filename</p>
<dd> Stores the graph to be partitioned.</p>
<dt>
<dd> Optional parameters</p>
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
<dd>Specifies the scheme to be used to compute the initial bisection of the graph. The possible values are:</p>
<dt>edge</p>
<dd> &#8211; Separator from an edge cut</p>
<dt>node</p>
<dd> &#8211; Separator from a greedy node-based strategy [default]</p>
<dt> <code>-rtype</code>=<i>string</i></p>
<dt>
<dd>
<dd>Specifies the scheme to be used for refinement. The possible values are:</p>
<dt>1sided</p>
<dd> &#8211; 1-sided node-based refinement [default]</p>
<dt>2sided</p>
<dd> &#8211; 2-sided node-based refinement</p>
<dt> <code>-ufactor</code>=<i>int</i></p>
<dt>
<dd>
<dd>Specifies the maximum allowed load imbalance between the left and right partitions during each bisection. The load imbalanced is measured as the ratio of the 2*max(left,right)/(left+right), where left and right are the sizes of the respective partitions. A value of x indicates that the allowed load imbalance is 1+x/1000. Default is 200, indicating a load imbalance of 1.20.</p>
<dt> <code>-pfactor</code>=<i>int</i></p>
<dt>
<dd>
<dd>Specifies the minimum degree of the vertices that will be ordered last. If the specified value is x&gt;0, then any vertices with a degree greater than 0.1*x*(average degree) are removed from the graph, an ordering of the rest of the vertices is computed, and an overall ordering is computed by ordering the removed vertices at the end of the overall ordering. Default value is 0, indicating that no vertices are removed</p>
<dt> <code>-no2hop</code></p>
<dt>
<dd>
<dd>Specifies that the coarsening will not perform any 2-hop matchings when the standard matching fails to sufficiently contract the graph.</p>
<dt> <code>-nocompress</code></p>
<dt>
<dd>
<dd>Specifies that the graph should not be compressed by combining together vertices that have identical adjacency lists.</p>
<dt> <code>-ccorder</code></p>
<dt>
<dd>
<dd>Specifies if the connected components of the graph should first be identified and ordered separately.</p>
<dt> <code>-niter</code>=<i>int</i></p>
<dt>
<dd>
<dd>Specifies the maximum number of iterations for the refinement algorithms at each stage of the uncoarsening process. Default is 10.</p>
<dt> <code>-nseps</code>=<i>int</i></p>
<dt>
<dd>
<dd>Specifies the number of different separators that it will compute at each level of the nested dissection. The final separator that is used is the smallest one. Default is 1.</p>
<dt> <code>-nooutput</code></p>
<dt>
<dd>
<dd>Specifies that no ordering file should be generated.</p>
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
