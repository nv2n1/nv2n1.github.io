---
title: "pdldelta(1)"
name: "pdldelta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdldelta/"
---

PDL::Delta - PDL changes between V1.0 and V2.0 

<h2>Description</h2>This file is an attempt to list the major user-visible changes between <font SIZE="-1">PDL</font> versions 1.0 and 2.0.
<h2>Core Changes</h2><h3>Piddles are not hashes any more:</h3><pre> $a = zeroes 10,10;
 $$a{FOO} = &quot;bar&quot;</pre>doesn't work. They are currently scalar references (to opaque C structures in finer terms) because of speed as well as syntactic issues. If you want to have a hash, use 

 <pre> $a-&gt;hdr()</pre>which returns a reference to an anonymous hash. Also, subclassing works if you store a piddle in the hash member ``<font SIZE="-1">PDL</font>''. 

 There are also many core enhancements to support Dataflow and Slicing tricks, but these do not introduce any incompatibilities.
<h3>Incompatible Changes vs 1.11</h3><dl><dt>rgrep
<dd>Order of the arguments has changed.
<dt>copy method
<dd>No longer copies the header. This may not be a misfeature.</dl><h2>Documentation Changes</h2>Many of the base and library pods were updated.
<h2>See Also</h2>The <i>Changes</i> file for exhaustive details on what changed. 

 The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build <font SIZE="-1">PDL.</font> 

 The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff.
<h2>History</h2>pdldelta was inspired by <i>perldelta</i> man page in the Perl 5.004 distribution.
