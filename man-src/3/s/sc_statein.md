---
title: "sc_statein(3)"
name: "sc_statein"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_statein/"
description: "sc::StateIn –"
---

<p>sc::StateIn &#8211; </p>
<p> Restores objects that derive from <code>SavableState</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;statein.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::MsgStateBufRecv</code>, and <code>sc::StateInFile</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual void get_header ()


Read in the header information.


virtual int version (const ClassDesc *)


Returns the version of the ClassDesc in the persistent object or -1 if info on the ClassDesc doesn't exist.


virtual int getstring (char *&amp;)


This restores strings saved with StateOut::putstring.


virtual int get (std::string &amp;)


This restores a std::string object.


virtual int get (char &amp;r, const char *keyword=0)


These restore data saved with StateOut's put. members.


virtual int get (unsigned int &amp;r, const char *keyword=0)



virtual int get (int &amp;r, const char *keyword=0)



virtual int get (bool &amp;r, const char *keyword=0)



virtual int get (float &amp;r, const char *keyword=0)



virtual int get (double &amp;r, const char *keyword=0)



virtual int get (char *&amp;)


These restore data saved with StateOut's put.


virtual int get (unsigned int *&amp;)



virtual int get (int *&amp;)



virtual int get (float *&amp;)



virtual int get (double *&amp;)



virtual int get_array_char (char *p, int size)


These restore data saved with StateOut's put.


virtual int get_array_uint (unsigned int *p, int size)



virtual int get_array_int (int *p, int size)



virtual int get_array_float (float *p, int size)



virtual int get_array_double (double *p, int size)



template&lt;class T &gt; int get (typename std::vector&lt; T &gt; &amp;v)


Read an STL vector of data.


int node_to_node () const


True if this is a node to node save/restore.


virtual int use_directory ()


Returns true of this object uses a directory.


virtual int tell ()


Return the current position in the file.


virtual void seek (int)


Set the current position in the file.


virtual int seekable ()


Return non-zero if seek does anything sensible.


int has_directory () const



virtual void list_objects (std::ostream &amp;=ExEnv::out0())


List all the objects to the stream.


void set_override (const Ref&lt; KeyVal &gt; &amp;kv)


Give this StateIn a KeyVal object that is used to override values.


const Ref&lt; KeyVal &gt; &amp; override () const


Return the KeyVal used to override values.



Protected Member Functions</code></pre>
<p> virtual int <code>get_array_void</code> (void *, int) </p>
<p> int <code>push_key</code> (const char *key) </p>
<p> void <code>pop_key</code> (int n) </p>
<p> const char * <code>key</code> () </p>
<p> void <code>get_directory</code> () </p>
<p> int <code>directory_location</code> () const </p>
<p> void <code>find_and_get_directory</code> () </p>
<p> virtual int <code>getobject</code> (<code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;)<br />
 <i>This is used to restore an object. </i><br />
 virtual int <code>dir_getobject</code> (<code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;, const char *name)<br />
 <i>This restores objects that are listed in the directory. </i><br />
 virtual void <code>haveobject</code> (int, const <code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;)<br />
 <i>When storage has been allocated during object restoration, this routine is called with the object reference number and the pointer to the new storage so getpointer can find the data if it is referenced again. </i><br />
 virtual void <code>nextobject</code> (int)<br />
 <i>A call to nextobject followed by havepointer(int) is equiv to havepointer(int,void**);. </i><br />
 virtual void <code>haveobject</code> (const <code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;) </p>
<p> void <code>have_classdesc</code> () </p>
<p> int <code>need_classdesc</code> () </p>
<p> virtual int <code>get</code> (const <code>ClassDesc</code> **)<br />
 <i>This restores ClassDesc&#8217;s. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>KeyVal</code> &gt; <code>override_</code> </p>
<p> <code>TranslateDataIn</code> * <code>translate_</code> </p>
<p> std::map&lt; int, <code>StateInData</code> &gt; <code>ps_</code> </p>
<p> int <code>expected_object_num_</code> </p>
<p> std::map&lt; <code>ClassDescP</code>, int &gt; <code>classidmap_</code> </p>
<p> std::map&lt; int, <code>StateClassData</code> &gt; <code>classdatamap_</code> </p>
<p> int <code>nextclassid_</code> </p>
<p> int <code>node_to_node_</code> </p>
<p> int <code>version_</code> </p>
<p> int <code>date_</code> </p>
<p> char <code>userid_</code> [9] </p>
<p> char <code>format_</code></p>
<h3>Friends</h3>
<p>class <code>SavableState</code> </p>
<p> class <code>TranslateDataIn</code></p>
<h2>Detailed Description</h2>
<p>Restores objects that derive from <code>SavableState</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual int sc::StateIn::get (char *&amp;) [virtual]</h3>
<p>These restore data saved with StateOut&#8217;s put. members. The data is allocated by <code>StateIn</code>. </p>
<p> Reimplemented in <code>sc::MsgStateRecv</code>, and <code>sc::StateInText</code>.</p>
<h3>virtual int sc::StateIn::get (const <code>ClassDesc</code> **) [protected, virtual]</h3>
<p>This restores ClassDesc&#8217;s. It will set the pointer to the address of the static <code>ClassDesc</code> for the class which has the same name as the class that had the <code>ClassDesc</code> that was saved by put(const ClassDesc*). </p>
<p> Reimplemented in <code>sc::MsgStateRecv</code>, and <code>sc::StateInText</code>.</p>
<h3>virtual int sc::StateIn::get_array_char (char * p, int size) [virtual]</h3>
<p>These restore data saved with StateOut&#8217;s put. members. The data must be preallocated by the user. </p>
<p> Reimplemented in <code>sc::StateInText</code>.</p>
<h3>virtual void sc::StateIn::get_header () [virtual]</h3>
<p>Read in the header information. Changes the translation scheme if necessary.</p>
<h3>virtual int sc::StateIn::getobject (<code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;) [protected, virtual]</h3>
<p>This is used to restore an object. It is called with the reference to the reference being restored. If the data being restored has previously been restored, then the pointer being restored is set to a reference to the previously restored object. </p>
<p> Reimplemented in <code>sc::StateInText</code>.</p>
<h3>virtual void sc::StateIn::haveobject (int, const <code>Ref</code>&lt; <code>SavableState</code> &gt; &amp;) [protected, virtual]</h3>
<p>When storage has been allocated during object restoration, this routine is called with the object reference number and the pointer to the new storage so getpointer can find the data if it is referenced again.</p>
<h3>virtual void sc::StateIn::list_objects (std::ostream &amp; = ExEnv::out0()) [virtual]</h3>
<p>List all the objects to the stream. Only <code>StateIn</code> specializations with directories can list objects.</p>
<h3>int sc::StateIn::node_to_node () const [inline]</h3>
<p>True if this is a node to node save/restore. This is for classes that try to avoid saving databases to files that can otherwise be read in, but want to avoid reading the database from disk on all nodes.</p>
<h3>const <code>Ref</code>&lt;<code>KeyVal</code>&gt;&amp; sc::StateIn::override () const [inline]</h3>
<p>Return the <code>KeyVal</code> used to override values.</p>
<h3>virtual void sc::StateIn::seek (int) [virtual]</h3>
<p>Set the current position in the file. The default implementation does nothing. </p>
<p> Reimplemented in <code>sc::BcastStateInBin</code>, and <code>sc::StateInBin</code>.</p>
<h3>virtual int sc::StateIn::seekable () [virtual]</h3>
<p>Return non-zero if seek does anything sensible. The default implementation returns 0. </p>
<p> Reimplemented in <code>sc::BcastStateInBin</code>, and <code>sc::StateInBin</code>.</p>
<h3>void sc::StateIn::set_override (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp; kv) [inline]</h3>
<p>Give this <code>StateIn</code> a <code>KeyVal</code> object that is used to override values.</p>
<h3>virtual int sc::StateIn::version (const <code>ClassDesc</code> *) [virtual]</h3>
<p>Returns the version of the <code>ClassDesc</code> in the persistent object or -1 if info on the <code>ClassDesc</code> doesn&#8217;t exist. </p>
<p> Reimplemented in <code>sc::MsgStateRecv</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
