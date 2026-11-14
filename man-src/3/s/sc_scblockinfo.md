---
title: "sc_scblockinfo(3)"
name: "sc_scblockinfo"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scblockinfo/"
description: "sc::SCBlockInfo –"
---

<p>sc::SCBlockInfo &#8211; </p>
<p> <code>SCBlockInfo</code> contains blocking information for the <code>SCDimension</code> class.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;dim.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCBlockInfo (int n, int nblocks=0, const int *blocksizes=0)


Create a SCBlockInfo object.


SCBlockInfo (StateIn &amp;)



SCBlockInfo (const Ref&lt; KeyVal &gt; &amp;keyval)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


int equiv (SCBlockInfo *bi)


Return nonzero if this is equivalent to bi.


int nelem () const


Return the total number of elements.


int nblock () const


Return the number of blocks.


int start (int i) const


Return the starting index for block i.


int size (int i) const


Return the size of block i.


int fence (int i) const


Return the last index + 1 for block i.


void elem_to_block (int i, int &amp;block, int &amp;offset)



RefSCDimension subdim (int i)


Retreive subdimension information.


void set_subdim (int i, const RefSCDimension &amp;dim)


Set subdimension information.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print the object to the stream o.



Protected Member Functions
void init_start ()



Protected Attributes
int n_



int nblocks_



int * start_



int * size_



RefSCDimension * subdims_</code></pre>
<h2>Detailed Description</h2>
<p><code>SCBlockInfo</code> contains blocking information for the <code>SCDimension</code> class. </p>
<p> There are really two ways that it can contain blocking information. In the first way, a vector of block offsets and block sizes is stored. The second method is only used by those specializations created by the <code>BlockedSCMatrixKit</code> class. In this method the blocking information is stored as subdimensions of type <code>SCDimension</code>. If both methods are used, they must be used consistently. That is, the number, sizes, and order of the blocks must match the number, sizes, and order of the <code>SCDimension</code> objects.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SCBlockInfo::SCBlockInfo (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp; keyval)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;sizes&quot; 1c This is a vector giving the size of each subblock. There is no default. </p>
<dl>
<dt>subdims</p>
<dd>If this vector is given there is must be entry for each entry in the sizes vector. Each entry is an <code>SCDimension</code> object. The default is to not store subdimension information.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::SCBlockInfo::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h3>void sc::SCBlockInfo::set_subdim (int i, const <code>RefSCDimension</code> &amp; dim)</h3>
<p>Set subdimension information. The dimension dim and index i must be consistent with the nblocks and blocksizes information given to the constructor.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
