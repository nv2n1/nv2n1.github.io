---
title: "sc_stateout(3)"
name: "sc_stateout"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stateout/"
description: "sc::StateOut –"
---

<p>sc::StateOut &#8211; </p>
<p> Serializes objects that derive from <code>SavableState</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;stateout.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::MsgStateSend</code>, and <code>sc::StateOutFile</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual void <code>put_header</code> ()<br />
 <i>Write out header information. </i><br />
 virtual int <code>putstring</code> (const char *)<br />
 <i>This is like put except the length of the char array is determined by interpreting the character array as a character string. </i><br />
 virtual int <code>put</code> (const std::string &amp;)<br />
 <i>Write out a std::string object. </i><br />
 virtual int <code>put</code> (char r)<br />
 <i>Write the given datum. </i><br />
 virtual int <code>put</code> (unsigned int r) </p>
<p> virtual int <code>put</code> (int r) </p>
<p> virtual int <code>put</code> (bool r) </p>
<p> virtual int <code>put</code> (unsigned long r) </p>
<p> virtual int <code>put</code> (float r) </p>
<p> virtual int <code>put</code> (double r) </p>
<p> virtual int <code>put</code> (const char *, int)<br />
 <i>Write the given array data. </i><br />
 virtual int <code>put</code> (const unsigned int *, int) </p>
<p> virtual int <code>put</code> (const int *, int) </p>
<p> virtual int <code>put</code> (const float *, int) </p>
<p> virtual int <code>put</code> (const double *, int) </p>
<p> virtual int <code>put_array_char</code> (const char *p, int size)<br />
 <i>Put arrays of data. </i><br />
 virtual int <code>put_array_uint</code> (const unsigned int *p, int size) </p>
<p> virtual int <code>put_array_int</code> (const int *p, int size) </p>
<p> virtual int <code>put_array_float</code> (const float *p, int size) </p>
<p> virtual int <code>put_array_double</code> (const double *p, int size) </p>
<p> template&lt;class T &gt; int <code>put</code> (typename std::vector&lt; T &gt; &amp;v)<br />
 <i>Write an STL vector of data. </i><br />
 void <code>forget_references</code> ()<br />
 <i>Don&#8217;t keep track of pointers to objects. </i><br />
 void <code>copy_references</code> ()<br />
 <i>If a reference to an object that has already been written is encountered, copy it instead of generating a reference to the first object. </i><br />
 virtual int <code>use_directory</code> ()<br />
 <i>Returns true if this object uses a directory. </i><br />
 virtual void <code>flush</code> ()<br />
 <i>Flush out any remaining data. </i><br />
 int <code>node_to_node</code> () const<br />
 <i>True if this is a node to node save/restore. </i><br />
 virtual int <code>tell</code> ()<br />
 <i>Returns the current position in the file. </i><br />
 virtual void <code>seek</code> (int loc)<br />
 <i>Set the current position in the file. </i><br />
 virtual int <code>seekable</code> ()<br />
 <i>Return non-zero if tell and seek do anything sensible. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual int <code>put_array_void</code> (const void *, int) </p>
<p> virtual int <code>putparents</code> (const <code>ClassDesc</code> *) </p>
<p> void <code>put_directory</code> () </p>
<p> void <code>have_classdesc</code> () </p>
<p> int <code>need_classdesc</code> () </p>
<p> virtual int <code>putobject</code> (const <code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;)<br />
 <i>This will prepare </i><code>StateOut</code> to output a pointer to data.<br />
 virtual int <code>put</code> (const <code>ClassDesc</code> *)<br />
 <i>Write out information about the given </i><code>ClassDesc</code>.</p>
<h3>Protected Attributes</h3>
<pre><code>int dir_loc_loc_



TranslateDataOut * translate_



int copy_references_



int next_object_number_



std::map&lt; Ref&lt; SavableState &gt;, StateOutData &gt; ps_



std::map&lt; ClassDescP, int &gt; classidmap_



int nextclassid_



int node_to_node_



Friends</code></pre>
<p> class <code>SavableState</code> </p>
<p> class <code>TranslateDataOut</code></p>
<h2>Detailed Description</h2>
<p>Serializes objects that derive from <code>SavableState</code>. </p>
<p> <code>StateOut</code> keeps track of pointers to data so that two references to the same piece of data do not result in that data being sent to the output device two times.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::StateOut::copy_references ()</h3>
<p>If a reference to an object that has already been written is encountered, copy it instead of generating a reference to the first object. The directory will not be updated with new objects.</p>
<h3>void sc::StateOut::forget_references ()</h3>
<p>Don&#8217;t keep track of pointers to objects. Calling this causes duplicated references to objects to be copied. The directory will not contain the forgotten objects.</p>
<h3>int sc::StateOut::node_to_node () const [inline]</h3>
<p>True if this is a node to node save/restore. This is necessary for classes that try to avoid saving databases to files that can otherwise be read in, but want to avoid reading the database from disk on all nodes.</p>
<h3>virtual int sc::StateOut::put (const char *, int) [virtual]</h3>
<p>Write the given array data. Size information is also saved. The data is allocated and read by the get(T*&amp;) routines. </p>
<p> Reimplemented in <code>sc::MsgStateSend</code>, and <code>sc::StateOutText</code>.</p>
<h3>virtual int sc::StateOut::put_array_char (const char * p, int size) [virtual]</h3>
<p>Put arrays of data. No size information is stored. This data is read by the get_array_T routines. </p>
<p> Reimplemented in <code>sc::StateOutText</code>.</p>
<h3>virtual int sc::StateOut::putobject (const <code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;) [protected, virtual]</h3>
<p>This will prepare <code>StateOut</code> to output a pointer to data. It first checks to see if the data has already been saved. If it has, then a reference to this data is saved. Otherwise the object is written out. </p>
<p> Reimplemented in <code>sc::StateOutText</code>.</p>
<h3>virtual int sc::StateOut::putstring (const char *) [virtual]</h3>
<p>This is like put except the length of the char array is determined by interpreting the character array as a character string. </p>
<p> Reimplemented in <code>sc::StateOutText</code>.</p>
<h3>virtual void sc::StateOut::seek (int loc) [virtual]</h3>
<p>Set the current position in the file. The default implementation does nothing. </p>
<p> Reimplemented in <code>sc::StateOutBin</code>.</p>
<h3>virtual int sc::StateOut::seekable () [virtual]</h3>
<p>Return non-zero if tell and seek do anything sensible. The default implementation returns 0. </p>
<p> Reimplemented in <code>sc::StateOutBin</code>.</p>
<h3>virtual int sc::StateOut::tell () [virtual]</h3>
<p>Returns the current position in the file. The default implementation returns 0. </p>
<p> Reimplemented in <code>sc::StateOutBin</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
