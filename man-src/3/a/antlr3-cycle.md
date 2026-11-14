---
title: "antlr3-cycle(3)"
name: "antlr3-cycle"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-cycle/"
description: "ANTLR3_TOPO_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_TOPO_struct &#8211; </p>
<p> A topological sort system that given a set of dependencies of a node m on node n, can sort them in dependency order.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> void(* <code>addEdge</code> )(struct <code>ANTLR3_TOPO_struct</code> *topo, <code>ANTLR3_UINT32</code> edge, <code>ANTLR3_UINT32</code> dependency)<br />
 <i>A method that adds an edge from one node to another. </i><br />
 <code>pANTLR3_UINT32</code> <code>cycle</code><br />
 <i>A vector used to detect cycles in the edge dependecies. </i><br />
 <code>ANTLR3_UINT32</code> <code>cycleMark</code><br />
 <i>A watermark used to accumulate potential cycles in the cycle array. </i><br />
 <code>pANTLR3_BITSET</code> * <code>edges</code><br />
 <i>A vector of vectors of edges, built by calling the addEdge method() to indicate that node number n depends on node number m. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_TOPO_struct</code> *topo)<br />
 <i>A method to free this structure and any associated memory. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>hasCycle</code><br />
 <i>A flag that indicates the algorithm found a cycle in the edges such as 9-&gt;8-&gt;1-&gt;9 If this flag is set after you have called one of the sort routines then the detected cycle will be contained in the cycle array and cycleLimit will point to the one after the last entry in the cycle. </i><br />
 <code>ANTLR3_UINT32</code> <code>limit</code><br />
 <i>One more than the largest node index that is contained in edges/sorted. </i><br />
 <code>pANTLR3_UINT32</code> <code>sorted</code><br />
 <i>A vector used to build up the sorted output order. </i><br />
 <code>pANTLR3_UINT32</code>(* <code>sortToArray</code> )(struct <code>ANTLR3_TOPO_struct</code> *topo)<br />
 <i>A method that returns a pointer to an array of sorted node indexes. </i><br />
 void(* <code>sortVector</code> )(struct <code>ANTLR3_TOPO_struct</code> *topo, <code>pANTLR3_VECTOR</code> v)<br />
 <i>A method that sorts the supplied ANTLR3_VECTOR in place based on the previously supplied edge data. </i><br />
 <code>pANTLR3_BITSET</code> <code>visited</code><br />
 <i>The set of visited nodes as determined by a set entry in the bitmap. </i></p>
<h2>Detailed Description</h2>
<p> A topological sort system that given a set of dependencies of a node m on node n, can sort them in dependency order. </p>
<p> This is a generally useful utility object that does not care what the things are it is sorting. Generally the set to be sorted will be numeric indexes into some other structure such as an ANTLR3_VECTOR. I have provided a sort method that given ANTLR3_VECTOR as an input will sort the vector entries in place, as well as a sort method that just returns an array of the sorted noded indexes, in case you are not sorting ANTLR3_VECTORS but some set of your own device. </p>
<p> Of the two main algorithms that could be used, I chose to use the depth first search for unvisited nodes as a) This runs in linear time, and b) it is what we used in the ANTLR Tool to perform a topological sort of the input grammar files based on their dependencies.</p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_TOPO_struct::addEdge</code>)(struct <code>ANTLR3_TOPO_struct</code> *topo, <code>ANTLR3_UINT32</code> edge, <code>ANTLR3_UINT32</code> dependency)</h3>
<p> A method that adds an edge from one node to another. An edge of n -&gt; m indicates that node n is dependent on node m. Note that while building these edges, it is perfectly OK to add nodes out of sequence. So, if you have edges: </p>
<p> 3 -&gt; 0 2 -&gt; 1 1 -&gt; 3 </p>
<p> The you can add them in that order and so add node 3 before nodes 2 and 1 </p>
<p> Referenced by antlr3TopoNew().</p>
<h3><code>pANTLR3_UINT32</code> <code>ANTLR3_TOPO_struct::cycle</code></h3>
<p> A vector used to detect cycles in the edge dependecies. It is used as a stack and each time we descend a node to one of its edges we add the node into this stack. If we find a node that we have already visited in the stack, then it means there wasa cycle such as 9-&gt;8-&gt;1-&gt;9 as the only way a node can be on the stack is if we are currently descnding from it as we remove it from the stack as we exit from descending its dependencies </p>
<p> Referenced by antlr3TopoNew(), DFS(), freeTopo(), and sortToArray().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_TOPO_struct::cycleMark</code></h3>
<p> A watermark used to accumulate potential cycles in the cycle array. This should be zero when we are done. Check hasCycle after calling one of the sort methods and if it is ANTLR3_TRUE then you can find the cycle in cycle[0]&#8230;cycle[cycleMark-1] </p>
<p> Referenced by antlr3TopoNew(), and DFS().</p>
<h3><code>pANTLR3_BITSET</code>* <code>ANTLR3_TOPO_struct::edges</code></h3>
<p> A vector of vectors of edges, built by calling the addEdge method() to indicate that node number n depends on node number m. Each entry in the vector contains a bitset, which has a bit index set for each node upon which the entry node depends. </p>
<p> Referenced by addEdge(), antlr3TopoNew(), DFS(), freeTopo(), and sortToArray().</p>
<h3>void(* <code>ANTLR3_TOPO_struct::free</code>)(struct <code>ANTLR3_TOPO_struct</code> *topo)</h3>
<p> A method to free this structure and any associated memory. </p>
<p> Referenced by antlr3TopoNew().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_TOPO_struct::hasCycle</code></h3>
<p> A flag that indicates the algorithm found a cycle in the edges such as 9-&gt;8-&gt;1-&gt;9 If this flag is set after you have called one of the sort routines then the detected cycle will be contained in the cycle array and cycleLimit will point to the one after the last entry in the cycle. </p>
<p> Referenced by antlr3TopoNew(), DFS(), sortToArray(), and sortVector().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_TOPO_struct::limit</code></h3>
<p> One more than the largest node index that is contained in edges/sorted. </p>
<p> Referenced by addEdge(), antlr3TopoNew(), DFS(), freeTopo(), sortToArray(), and sortVector().</p>
<h3><code>pANTLR3_UINT32</code> <code>ANTLR3_TOPO_struct::sorted</code></h3>
<p> A vector used to build up the sorted output order. Note that as the vector contains UINT32 then the maximum node index is &#8216;limited&#8217; to 2^32, as nodes should be zero based. </p>
<p> Referenced by antlr3TopoNew(), DFS(), freeTopo(), sortToArray(), and sortVector().</p>
<h3><code>pANTLR3_UINT32</code>(* <code>ANTLR3_TOPO_struct::sortToArray</code>)(struct <code>ANTLR3_TOPO_struct</code> *topo)</h3>
<p> A method that returns a pointer to an array of sorted node indexes. The array is sorted in topological sorted order. Note that the array is only as large as the largest node index you created an edge for. This means that if you had an input of 32 nodes, but that largest node with an edge was 16, then the returned array will be the sorted order of the first 16 nodes and the last 16 nodes of your array are basically fine as they are as they had no dependencies and do not need any particular sort order. </p>
<p> NB: If the structure that contains the array is freed, then the sorted array will be freed too so you should use the value of limit to make a long term copy of this array if you do not want to keep the topo structure around as well. </p>
<p> Referenced by antlr3TopoNew(), and sortVector().</p>
<h3>void(* <code>ANTLR3_TOPO_struct::sortVector</code>)(struct <code>ANTLR3_TOPO_struct</code> *topo, <code>pANTLR3_VECTOR</code> v)</h3>
<p> A method that sorts the supplied ANTLR3_VECTOR in place based on the previously supplied edge data. </p>
<p> Referenced by antlr3TopoNew().</p>
<h3><code>pANTLR3_BITSET</code> <code>ANTLR3_TOPO_struct::visited</code></h3>
<p> The set of visited nodes as determined by a set entry in the bitmap. </p>
<p> Referenced by antlr3TopoNew(), DFS(), freeTopo(), and sortToArray(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAR">Author</a></p>
<dd></dl>
