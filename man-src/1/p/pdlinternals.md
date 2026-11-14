---
title: "pdlinternals(1)"
name: "pdlinternals"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlinternals/"
description: "PDL::Internals – description of some aspects of the current internals"
---

<p>PDL::Internals &#8211; description of some aspects of the current internals </p>
<h2>Description</h2>
<h3>Intro</h3>
<p>This document explains various aspects of the current implementation of <font SIZE="-1">PDL.</font> If you just want to use <font SIZE="-1">PDL</font> for something, you definitely do not need to read this. Even if you want to interface your C routines to <font SIZE="-1">PDL</font> or create new <font SIZE="-1">PDL::PP</font> functions, you do not need to read this man page (though it may be informative). This document is primarily intended for people interested in debugging or changing the internals of <font SIZE="-1">PDL.</font> To read this, a good understanding of the C language and programming and data structures in general is required, as well as some Perl understanding. If you read through this document and understand all of it and are able to point what any part of this document refers to in the <font SIZE="-1">PDL</font> core sources and additionally struggle to understand <font SIZE="-1">PDL::PP</font>, you will be awarded the title &#8220;<font SIZE="-1">PDL</font> Guru&#8221; (of course, the current version of this document is so incomplete that this is next to impossible from just these notes). </p>
<p> <code>Warning:</code> If it seems that this document has gotten out of date, please inform the <font SIZE="-1">PDL</font> porters email list (pdl-porters [at] jach.hawaii.edu). This may well happen.</p>
<h3>Piddles</h3>
<p>The pdl data object is generally an opaque scalar reference into a pdl structure in memory. Alternatively, it may be a hash reference with the <tt>&quot;PDL&quot;</tt> field containing the scalar reference (this makes overloading piddles easy, see PDL::Objects). You can easily find out at the Perl level which type of piddle you are dealing with. The example code below demonstrates how to do it: </p>
<pre> # check if this a piddle
 die &quot;not a piddle&quot; unless UNIVERSAL::isa($pdl, 'PDL');
 # is it a scalar ref or a hash ref?
 if (UNIVERSAL::isa($pdl, &quot;HASH&quot;)) {
 die &quot;not a valid PDL&quot; unless exists $pdl-&gt;{PDL} &amp;&amp;
 UNIVERSAL::isa($pdl-&gt;{PDL},'PDL');
 print &quot;This is a hash reference,&quot;,
 &quot; the PDL field contains the scalar ref
&quot;;
 } else {
 print &quot;This is a scalar ref that points to address $$pdl in memory
&quot;;
 }</pre>
<p>The scalar reference points to the numeric address of a C structure of type <tt>&quot;pdl&quot;</tt> which is defined in <i>pdl.h</i>. The mapping between the object at the Perl level and the C structure containing the actual data and structural that makes up a piddle is done by the <font SIZE="-1">PDL</font> typemap. The functions used in the <font SIZE="-1">PDL</font> typemap are defined pretty much at the top of the file <i>pdlcore.h</i>. So what does the structure look like: </p>
<pre> struct pdl {
 unsigned long magicno; /* Always stores PDL_MAGICNO as a sanity check */
 /* This is first so most pointer accesses to wrong type are caught */
 int state; /* What's in this pdl */
 pdl_trans *trans; /* Opaque pointer to internals of transformation from
 parent */
 pdl_vaffine *vafftrans;
 void* sv; /* (optional) pointer back to original sv.
 ALWAYS check for non-null before use.
 We cannot inc refcnt on this one or we'd
 never get destroyed */
 void *datasv; /* Pointer to SV containing data. Refcnt inced */
 void *data; /* Null: no data alloced for this one */
 PDL_Indx nvals; /* How many values allocated */
 int datatype;
 PDL_Indx *dims; /* Array of data dimensions */
 PDL_Indx *dimincs; /* Array of data default increments */
 short ndims; /* Number of data dimensions */
 unsigned char *threadids; /* Starting index of the thread index set n */
 unsigned char nthreadids;
 pdl *progenitor; /* I'm in a mutated family. make_physical_now must
 copy me to the new generation. */
 pdl *future_me; /* I'm the &quot;then&quot; pdl and this is my &quot;now&quot; (or more modern
 version, anyway */
 pdl_children children;
 short living_for; /* Perl side not referenced; delete me when */
 PDL_Indx def_dims[PDL_NDIMS]; /* Preallocated space for efficiency */
 PDL_Indx def_dimincs[PDL_NDIMS]; /* Preallocated space for efficiency */
 unsigned char def_threadids[PDL_NTHREADIDS];
 struct pdl_magic *magic;
 void *hdrsv; /* &quot;header&quot;, settable from outside */
 };</pre>
<p>This is quite a structure for just storing some data in &#8211; what is going on?</p>
<dl>
<dt>Data storage</p>
<dd>We are going to start with some of the simpler members: first of all, there is the member </p>
<pre> void *datasv;</pre>
<p>which is really a pointer to a Perl <font SIZE="-1">SV</font> structure (<tt>&quot;SV *&quot;</tt>). The <font SIZE="-1">SV</font> is expected to be representing a string, in which the data of the piddle is stored in a tightly packed form. This pointer counts as a reference to the <font SIZE="-1">SV</font> so the reference count has been incremented when the <tt>&quot;SV *&quot;</tt> was placed here (this reference count business has to do with Perl&#8217;s garbage collection mechanism &#8212; don&#8217;t worry if this doesn&#8217;t mean much to you). This pointer is allowed to have the value <tt>&quot;NULL&quot;</tt> which means that there is no actual Perl <font SIZE="-1">SV</font> for this data &#8211; for instance, the data might be allocated by a <tt>&quot;mmap&quot;</tt> operation. Note the use of an SV* was purely for convenience, it allows easy transformation of packed data from files into piddles. Other implementations are not excluded. </p>
<p> The actual pointer to data is stored in the member </p>
<pre> void *data;</pre>
<p>which contains a pointer to a memory area with space for </p>
<pre> PDL_Indx nvals;</pre>
<p>data items of the data type of this piddle. PDL_Indx is either &#8216;long&#8217; or &#8216;long long&#8217; depending on whether your perl is 64bit or not. </p>
<p> The data type of the data is stored in the variable </p>
<pre> int datatype;</pre>
<p>the values for this member are given in the enum <tt>&quot;pdl_datatypes&quot;</tt> (see <i>pdl.h</i>). Currently we have byte, short, unsigned short, long, float and double types, see also PDL::Types.</p>
<dt>Dimensions</p>
<dd>The number of dimensions in the piddle is given by the member </p>
<pre> int ndims;</pre>
<p>which shows how many entries there are in the arrays </p>
<pre> PDL_Indx *dims; 
 PDL_Indx *dimincs;</pre>
<p>These arrays are intimately related: <tt>&quot;dims&quot;</tt> gives the sizes of the dimensions and <tt>&quot;dimincs&quot;</tt> is always calculated by the code </p>
<pre> PDL_Indx inc = 1;
 for(i=0; i&lt;it-&gt;ndims; i++) {
 it-&gt;dimincs[i] = inc; inc *= it-&gt;dims[i];
 }</pre>
<p>in the routine <tt>&quot;pdl_resize_defaultincs&quot;</tt> in <tt>&quot;pdlapi.c&quot;</tt>. What this means is that the dimincs can be used to calculate the offset by code like </p>
<pre> PDL_Indx offs = 0;
 for(i=0; i&lt;it-&gt;ndims; i++) {
 offs += it-&gt;dimincs[i] * index[i];
 }</pre>
<p>but this is not always the right thing to do, at least without checking for certain things first.</p>
<dt>Default storage</p>
<dd>Since the vast majority of piddles don&#8217;t have more than 6 dimensions, it is more efficient to have default storage for the dimensions and dimincs inside the <font SIZE="-1">PDL</font> struct. </p>
<pre> PDL_Indx def_dims[PDL_NDIMS]; 
 PDL_Indx def_dimincs[PDL_NDIMS];</pre>
<p>The <tt>&quot;dims&quot;</tt> and <tt>&quot;dimincs&quot;</tt> may be set to point to the beginning of these arrays if <tt>&quot;ndims&quot;</tt> is smaller than or equal to the compile-time constant <tt>&quot;PDL_NDIMS&quot;</tt>. This is important to note when freeing a piddle struct. The same applies for the threadids: </p>
<pre> unsigned char def_threadids[PDL_NTHREADIDS];</pre>
<dt>Magic</p>
<dd>It is possible to attach magic to piddles, much like Perl&#8217;s own magic mechanism. If the member pointer </p>
<pre> struct pdl_magic *magic;</pre>
<p>is nonzero, the <font SIZE="-1">PDL</font> has some magic attached to it. The implementation of magic can be gleaned from the file <i>pdlmagic.c</i> in the distribution.</p>
<dt>State</p>
<dd>One of the first members of the structure is </p>
<pre> int state;</pre>
<p>The possible flags and their meanings are given in <tt>&quot;pdl.h&quot;</tt>. These are mainly used to implement the lazy evaluation mechanism and keep track of piddles in these operations.</p>
<dt>Transformations and virtual affine transformations</p>
<dd>As you should already know, piddles often carry information about where they come from. For example, the code </p>
<pre> $b = $a-&gt;slice(&quot;2:5&quot;);
 $b .= 1;</pre>
<p>will alter <tt>$a</tt>. So <tt>$b</tt> and <tt>$a</tt> <i>know</i> that they are connected via a <tt>&quot;slice&quot;</tt>-transformation. This information is stored in the members </p>
<pre> pdl_trans *trans; 
 pdl_vaffine *vafftrans;</pre>
<p>Both <tt>$a</tt> (the <i>parent</i>) and <tt>$b</tt> (the child) store this information about the transformation in appropriate slots of the <tt>&quot;pdl&quot;</tt> structure. </p>
<p> <tt>&quot;pdl_trans&quot;</tt> and <tt>&quot;pdl_vaffine&quot;</tt> are structures that we will look at in more detail below.</p>
<dt>The Perl SVs</p>
<dd>When piddles are referred to through Perl SVs, we store an additional reference to it in the member </p>
<pre> void* sv;</pre>
<p>in order to be able to return a reference to the user when he wants to inspect the transformation structure on the Perl side. </p>
<p> Also, we store an opaque </p>
<pre> void *hdrsv;</pre>
<p>which is just for use by the user to hook up arbitrary data with this sv. This one is generally manipulated through sethdr and gethdr calls.</dl>
<h3>Smart references and transformations: slicing and dicing</h3>
<p>Smart references and most other fundamental functions operating on piddles are implemented via <i>transformations</i> (Aas mentioned above) which are represented by the type <tt>&quot;pdl_trans&quot;</tt> in <font SIZE="-1">PDL.</font> </p>
<p> A transformation links input and output piddles and contains all the infrastructure that defines how</p>
<dl>
<dt>&bull;</p>
<dd>output piddles are obtained from input piddles</p>
<dt>&bull;</p>
<dd>changes in smartly linked output piddles (e.g. the <i>child</i> of a sliced <i>parent</i> piddle) are flown back to the input piddle in transformations where this is supported (the most often used example being <tt>&quot;slice&quot;</tt> here).</p>
<dt>&bull;</p>
<dd>datatype and size of output piddles that need to be created are obtained</dl>
<p> In general, executing a <font SIZE="-1">PDL</font> function on a group of piddles results in creation of a transformation of the requested type that links all input and output arguments (at least those that are piddles). In <font SIZE="-1">PDL</font> functions that support data flow between input and output args (e.g. <tt>&quot;slice&quot;</tt>, <tt>&quot;index&quot;</tt>) this transformation links <i>parent</i> (input) and <i>child</i> (output) piddles permanently until either the link is explicitly broken by user request (<tt>&quot;sever&quot;</tt> at the Perl level) or all parents and children have been destroyed. In those cases the transformation is lazy-evaluated, e.g. only executed when piddle values are actually accessed. </p>
<p> In <i>non-flowing</i> functions, for example addition (<tt>&quot;+&quot;</tt>) and inner products (<tt>&quot;inner&quot;</tt>), the transformation is installed just as in flowing functions but then the transformation is immediately executed and destroyed (breaking the link between input and output args) before the function returns. </p>
<p> It should be noted that the close link between input and output args of a flowing function (like slice) requires that piddle objects that are linked in such a way be kept alive beyond the point where they have gone out of scope from the point of view of Perl: </p>
<pre> $a = zeroes(20);
 $b = $a-&gt;slice('2:4');
 undef $a; # last reference to $a is now destroyed</pre>
<p>Although <tt>$a</tt> should now be destroyed according to Perl&#8217;s rules the underlying <tt>&quot;pdl&quot;</tt> structure must actually only be freed when <tt>$b</tt> also goes out of scope (since it still references internally some of <tt>$a</tt>&#8216;s data). This example demonstrates that such a dataflow paradigm between <font SIZE="-1">PDL</font> objects necessitates a special destruction algorithm that takes the links between piddles into account and couples the lifespan of those objects. The non-trivial algorithm is implemented in the function <tt>&quot;pdl_destroy&quot;</tt> in <i>pdlapi.c</i>. In fact, most of the code in <i>pdlapi.c</i> and <i>pdlfamily.c</i> is concerned with making sure that piddles (<tt>&quot;pdl *&quot;</tt>s) are created, updated and freed at the right times depending on interactions with other piddles via <font SIZE="-1">PDL</font> transformations (remember, <tt>&quot;pdl_trans&quot;</tt>).</p>
<h3>Accessing children and parents of a piddle</h3>
<p>When piddles are dynamically linked via transformations as suggested above input and output piddles are referred to as parents and children, respectively. </p>
<p> An example of processing the children of a piddle is provided by the <tt>&quot;baddata&quot;</tt> method of PDL::Bad (only available if you have compiled <font SIZE="-1">PDL</font> with the <tt>&quot;WITH_BADVAL&quot;</tt> option set to 1, but still useful as an example!). </p>
<p> Consider the following situation: </p>
<pre> pdl&gt; $a = rvals(7,7,Centre=&gt;[3,4]);
 pdl&gt; $b = $a-&gt;slice('2:4,3:5');
 pdl&gt; ? vars
 PDL variables in package main::
 Name Type Dimension Flow State Mem
 ----------------------------------------------------------------
 $a Double D [7,7] P 0.38Kb 
 $b Double D [3,3] VC 0.00Kb</pre>
<p>Now, if I suddenly decide that <tt>$a</tt> should be flagged as possibly containing bad values, using </p>
<pre> pdl&gt; $a-&gt;<a href="//www.systutorials.com/docs/linux/man/1-baddata/">baddata</a>(1)</pre>
<p>then I want the state of <tt>$b</tt> &#8211; it&#8217;s <i>child</i> &#8211; to be changed as well (since it will either share or inherit some of <tt>$a</tt>&#8216;s data and so be also <i>bad</i>), so that I get a &#8216;B&#8217; in the <i>State</i> field: </p>
<pre> pdl&gt; ? vars 
 PDL variables in package main::
 Name Type Dimension Flow State Mem
 ----------------------------------------------------------------
 $a Double D [7,7] PB 0.38Kb 
 $b Double D [3,3] VCB 0.00Kb</pre>
<p>This bit of magic is performed by the <tt>&quot;propogate_badflag&quot;</tt> function, which is listed below: </p>
<pre> /* newval = 1 means set flag, 0 means clear it */
 /* thanks to Christian Soeller for this */
 void propogate_badflag( pdl *it, int newval ) {
 PDL_DECL_CHILDLOOP(it)
 PDL_START_CHILDLOOP(it)
 {
 pdl_trans *trans = PDL_CHILDLOOP_THISCHILD(it);
 int i;
 for( i = trans-&gt;vtable-&gt;nparents;
 i &lt; trans-&gt;vtable-&gt;npdls;
 i++ ) {
 pdl *child = trans-&gt;pdls[i];
 if ( newval ) child-&gt;state |= PDL_BADVAL;
 else child-&gt;state &amp;= ~PDL_BADVAL;
 /* make sure we propogate to grandchildren, etc */
 propogate_badflag( child, newval );
 } /* for: i */
 }
 PDL_END_CHILDLOOP(it)
 } /* propogate_badflag */</pre>
<p>Given a piddle (<tt>&quot;pdl *it&quot;</tt>), the routine loops through each <tt>&quot;pdl_trans&quot;</tt> structure, where access to this structure is provided by the <tt>&quot;PDL_CHILDLOOP_THISCHILD&quot;</tt> macro. The <i>children</i> of the piddle are stored in the <tt>&quot;pdls&quot;</tt> array, after the <i>parents</i>, hence the loop from <tt>&quot;i = ...nparents&quot;</tt> to <tt>&quot;i = ...nparents - 1&quot;</tt>. Once we have the pointer to the child piddle, we can do what we want to it; here we change the value of the <tt>&quot;state&quot;</tt> variable, but the details are unimportant). What <code>is</code> important is that we call <tt>&quot;propogate_badflag&quot;</tt> on this piddle, to ensure we loop through its children. This recursion ensures we get to all the <i>offspring</i> of a particular piddle. </p>
<p> Access to <i>parents</i> is similar, with the <tt>&quot;for&quot;</tt> loop replaced by: </p>
<pre> for( i = 0;
 i &lt; trans-&gt;vtable-&gt;nparents;
 i++ ) {
 /* do stuff with parent #i: trans-&gt;pdls[i] */
 }</pre>
<h3>What&#8217;s in a transformation (pdl_trans)</h3>
<p>All transformations are implemented as structures </p>
<pre> struct XXX_trans {
 int magicno; /* to detect memory overwrites */
 short flags; /* state of the trans */
 pdl_transvtable *vtable; /* the all important vtable */
 void (*freeproc)(struct pdl_trans *); /* Call to free this trans
 (in case we had to malloc some stuff dor this trans) */
 pdl *pdls[NP]; /* The pdls involved in the transformation */
 int __datatype; /* the type of the transformation */
 /* in general more members
 /* depending on the actual transformation (slice, add, etc)
 */
 };</pre>
<p>The transformation identifies all <tt>&quot;pdl&quot;</tt>s involved in the trans </p>
<pre> pdl *pdls[NP];</pre>
<p>with <tt>&quot;NP&quot;</tt> depending on the number of piddle args of the particular trans. It records a state </p>
<pre> short flags;</pre>
<p>and the datatype </p>
<pre> int __datatype;</pre>
<p>of the trans (to which all piddles must be converted unless they are explicitly typed, <font SIZE="-1">PDL</font> functions created with <font SIZE="-1">PDL::PP</font> make sure that these conversions are done as necessary). Most important is the pointer to the vtable (virtual table) that contains the actual functionality </p>
<pre> pdl_transvtable *vtable;</pre>
<p>The vtable structure in turn looks something like (slightly simplified from <i>pdl.h</i> for clarity) </p>
<pre> typedef struct pdl_transvtable {
 pdl_transtype transtype;
 int flags;
 int nparents; /* number of parent pdls (input) */
 int npdls; /* number of child pdls (output) */
 char *per_pdl_flags; /* optimization flags */
 void (*redodims)(pdl_trans *tr); /* figure out dims of children */
 void (*readdata)(pdl_trans *tr); /* flow parents to children */
 void (*writebackdata)(pdl_trans *tr); /* flow backwards */
 void (*freetrans)(pdl_trans *tr); /* Free both the contents and it of
 the trans member */
 pdl_trans *(*copy)(pdl_trans *tr); /* Full copy */
 int structsize;
 char *name; /* For debuggers, mostly */
 } pdl_transvtable;</pre>
<p>We focus on the callback functions: </p>
<pre> void (*redodims)(pdl_trans *tr);</pre>
<p><tt>&quot;redodims&quot;</tt> will work out the dimensions of piddles that need to be created and is called from within the <font SIZE="-1">API</font> function that should be called to ensure that the dimensions of a piddle are accessible (<i>pdlapi.c</i>): </p>
<pre> void pdl_make_physdims(pdl *it)</pre>
<p><tt>&quot;readdata&quot;</tt> and <tt>&quot;writebackdata&quot;</tt> are responsible for the actual computations of the child data from the parents or parent data from those of the children, respectively (the dataflow aspect). The <font SIZE="-1">PDL</font> core makes sure that these are called as needed when piddle data is accessed (lazy-evaluation). The general <font SIZE="-1">API</font> function to ensure that a piddle is up-to-date is </p>
<pre> void pdl_make_physvaffine(pdl *it)</pre>
<p>which should be called before accessing piddle data from <font SIZE="-1">XS/C </font>(see <i>Core.xs</i> for some examples). </p>
<p> <tt>&quot;freetrans&quot;</tt> frees dynamically allocated memory associated with the trans as needed and <tt>&quot;copy&quot;</tt> can copy the transformation. Again, functions built with <font SIZE="-1">PDL::PP</font> make sure that copying and freeing via these callbacks happens at the right times. (If they fail to do that we have got a memory leak &#8212; this has happened in the past ;). </p>
<p> The transformation and vtable code is hardly ever written by hand but rather generated by <font SIZE="-1">PDL::PP</font> from concise descriptions. </p>
<p> Certain types of transformations can be optimized very efficiently obviating the need for explicit <tt>&quot;readdata&quot;</tt> and <tt>&quot;writebackdata&quot;</tt> methods. Those transformations are called <i>pdl_vaffine</i>. Most dimension manipulating functions (e.g., <tt>&quot;slice&quot;</tt>, <tt>&quot;xchg&quot;</tt>) belong to this class. </p>
<p> The basic trick is that parent and child of such a transformation work on the same (shared) block of data which they just choose to interpret differently (by using different <tt>&quot;dims&quot;</tt>, <tt>&quot;dimincs&quot;</tt> and <tt>&quot;offs&quot;</tt> on the same data, compare the <tt>&quot;pdl&quot;</tt> structure above). Each operation on a piddle sharing data with another one in this way is therefore automatically flown from child to parent and back &#8212; after all they are reading and writing the same block of memory. This is currently not Perl thread safe &#8212; no big loss since the whole <font SIZE="-1">PDL</font> core is not reentrant (Perl threading <tt>&quot;!=&quot;</tt> <font SIZE="-1">PDL</font> threading!).</p>
<h3>Signatures: threading over elementary operations</h3>
<p>Most of that functionality of <font SIZE="-1">PDL</font> threading (automatic iteration of elementary operations over multi-dim piddles) is implemented in the file <i>pdlthread.c</i>. </p>
<p> The <font SIZE="-1">PDL::PP</font> generated functions (in particular the <tt>&quot;readdata&quot;</tt> and <tt>&quot;writebackdata&quot;</tt> callbacks) use this infrastructure to make sure that the fundamental operation implemented by the trans is performed in agreement with <font SIZE="-1">PDL</font>&#8216;s threading semantics.</p>
<h3>Defining new <font SIZE="-1">PDL</font> functions &#8212; Glue code generation</h3>
<p>Please, see <font SIZE="-1">PDL::PP</font> and examples in the <font SIZE="-1">PDL</font> distribution. Implementation and syntax are currently far from perfect but it does a good job!</p>
<h3>The Core struct</h3>
<p>As discussed in <font SIZE="-1">PDL::API</font>, <font SIZE="-1">PDL</font> uses a pointer to a structure to allow <font SIZE="-1">PDL</font> modules access to its core routines. The definition of this structure (the <tt>&quot;Core&quot;</tt> struct) is in <i>pdlcore.h</i> (created by <i>pdlcore.h.PL</i> in <i>Basic/Core</i>) and looks something like </p>
<pre> /* Structure to hold pointers core PDL routines so as to be used by 
 * many modules
 */
 struct Core {
 I32 Version;
 pdl* (*SvPDLV) ( SV* );
 void (*SetSV_PDL) ( SV *sv, pdl *it );
 #if defined(PDL_clean_namespace) || defined(PDL_OLD_API)
 pdl* (*new) ( ); /* make it work with gimp-perl */
 #else
 pdl* (*pdlnew) ( ); /* renamed because of C++ clash */
 #endif
 pdl* (*tmp) ( );
 pdl* (*create) (int type);
 void (*destroy) (pdl *it);
 ...
 }
 typedef struct Core Core;</pre>
<p>The first field of the structure (<tt>&quot;Version&quot;</tt>) is used to ensure consistency between modules at run time; the following code is placed in the <font SIZE="-1">BOOT</font> section of the generated xs code: </p>
<pre> if (PDL-&gt;Version != PDL_CORE_VERSION)
 Perl_croak(aTHX_ &quot;Foo needs to be recompiled against the newly installed PDL&quot;);</pre>
<p>If you add a new field to the <i>Core</i> struct you should:</p>
<dl>
<dt>&bull;</p>
<dd>discuss it on the pdl porters email list (pdl-porters [at] jach.hawaii.edu) [with the possibility of making your changes to a separate branch of the <font SIZE="-1">CVS</font> tree if it&#8217;s a change that will take time to complete]</p>
<dt>&bull;</p>
<dd>increase by 1 the value of the <tt>$pdl_core_version</tt> variable in <i>pdlcore.h.PL</i>. This sets the value of the <tt>&quot;PDL_CORE_VERSION&quot;</tt> C macro used to populate the Version field</p>
<dt>&bull;</p>
<dd>add documentation (e.g. to <font SIZE="-1">PDL::API</font>) if it&#8217;s a &#8220;useful&#8221; function for external module writers (as well as ensuring the code is as well documented as the rest of <font SIZE="-1">PDL </font>;)</dl>
<h2>Bugs</h2>
<p>This description is far from perfect. If you need more details or something is still unclear please ask on the pdl-porters mailing list (pdl-porters [at] jach.hawaii.edu).</p>
<h2>Author</h2>
<p>Copyright(C) 1997 Tuomas J. Lukka (lukka [at] fas.harvard.edu), 2000 Doug Burke (djburke [at] cpan.org), 2002 Christian Soeller &amp; Doug Burke, 2013 Chris Marshall. </p>
<p> Redistribution in the same form is allowed but reprinting requires a permission from the author.</p>
