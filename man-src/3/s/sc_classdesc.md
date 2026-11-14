---
title: "sc_classdesc(3)"
name: "sc_classdesc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_classdesc/"
description: "sc::ClassDesc –"
---

<p>sc::ClassDesc &#8211; </p>
<p> This class is used to contain information about classes.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;class.h&gt;</code></pre>
<p> Inherits <code>sc::Identity</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>ClassDesc (const std::type_info &amp;, const char *, int=1, const char *p=0, DescribedClass *(*ctor)()=0, DescribedClass *(*keyvalctor)(const Ref&lt; KeyVal &gt; &amp;)=0, DescribedClass *(*stateinctor)(StateIn &amp;)=0)



const ParentClasses &amp; parents () const



const char * name () const


Returns the name of the class.


int version () const


Returns the version number of the class.


DescribedClass * create_described_class () const


This member has been replaced by create().


virtual DescribedClass * create () const


Create an instance of DescribedClass with exact type equal to the class to which this class descriptor belongs.


virtual DescribedClass * create (const Ref&lt; KeyVal &gt; &amp;) const


Create an instance of DescribedClass with exact type equal to the class to which this class descriptor belongs.


virtual DescribedClass * create (StateIn &amp;) const


Create an instance of DescribedClass with exact type equal to the class to which this class descriptor belongs.



Static Public Member Functions
static std::map&lt; std::string, ClassDescP &gt; &amp; all ()



static void list_all_classes ()


Writes a list of all of the classes to ExEnv::out0().


static ClassDesc * name_to_class_desc (const char *)


Given the name of the class, return a pointer to the class descriptor.


static ClassDesc * class_desc (const std::type_info &amp;)


Given a type_info object return a pointer to the ClassDesc.


static int load_class (const char *classname)


Attempt to dynamically load the shared object file for classname.



Friends</code></pre>
<p> class <code>ParentClasses</code></p>
<h2>Detailed Description</h2>
<p>This class is used to contain information about classes. </p>
<p> Each <code>DescribedClass</code> type has a static <code>ClassDesc</code> member. This member has lists of the parents, children and virtual parents for each class. The <code>ClassDesc</code> class also has a static member that is a list of all described classes in the system. These lists are constructed as the constructors for the static <code>ClassDesc</code> members for each class are called and are completed before main is entered. See <code>class</code> for more information.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>ClassDesc</code>* sc::ClassDesc::class_desc (const std::type_info &amp;) [static]</h3>
<p>Given a type_info object return a pointer to the <code>ClassDesc</code>.</p>
<h3>virtual <code>DescribedClass</code>* sc::ClassDesc::create (<code>StateIn</code> &amp;) const [virtual]</h3>
<p>Create an instance of <code>DescribedClass</code> with exact type equal to the class to which this class descriptor belongs. The <code>StateIn</code>&amp; constructor is used. If this constructor doesn&#8217;t exist or a static function that calls it with new wasn&#8217;t passed to this <code>ClassDesc</code>, then 0 will be returned.</p>
<h3>virtual <code>DescribedClass</code>* sc::ClassDesc::create (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) const [virtual]</h3>
<p>Create an instance of <code>DescribedClass</code> with exact type equal to the class to which this class descriptor belongs. The <code>KeyVal</code>&amp; constructor is used. If this constructor doesn&#8217;t exist or a static function that calls it with new wasn&#8217;t passed to this <code>ClassDesc</code>, then 0 will be returned.</p>
<h3>virtual <code>DescribedClass</code>* sc::ClassDesc::create () const [virtual]</h3>
<p>Create an instance of <code>DescribedClass</code> with exact type equal to the class to which this class descriptor belongs. The constructor which takes no arguments is used. If this constructor doesn&#8217;t exist or a static function that calls it with new wasn&#8217;t given to this <code>ClassDesc</code> when it was created, then 0 will be returned.</p>
<h3>static int sc::ClassDesc::load_class (const char * classname) [static]</h3>
<p>Attempt to dynamically load the shared object file for classname.</p>
<h3>static <code>ClassDesc</code>* sc::ClassDesc::name_to_class_desc (const char *) [static]</h3>
<p>Given the name of the class, return a pointer to the class descriptor.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
