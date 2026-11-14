---
title: "pdlapi(1)"
name: "pdlapi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlapi/"
---

PDL::API - making piddles from Perl and C/XS code 

<h2>Description</h2>A simple cookbook how to create piddles manually. It covers both the Perl and the C/XS level. Additionally, it describes the <font SIZE="-1">PDL</font> core routines that can be accessed from other modules. These routines basically define the <font SIZE="-1">PDL API.</font> If you need to access piddles from C/XS you probably need to know about these functions.
<h2>Synopsis</h2><pre> use PDL;
 sub mkmypiddle {
 ...
 }</pre><h2>Creating a piddle manually from Perl</h2>Sometimes you want to create a piddle <i>manually</i> from binary data. You can do that at the Perl level. Examples in the distribution include some of the <font SIZE="-1">IO</font> routines. The code snippet below illustrates the required steps. 

 <pre> use Carp;
 sub mkmypiddle {
 my $class = shift;
 my $pdl = $class-&gt;new;
 $pdl-&gt;set_datatype($PDL_B);
 my @dims = (1,3,4);
 my $size = 1;
 for (@dims) { $size *= $_ }
 $pdl-&gt;setdims([@dims]);
 my $dref = $pdl-&gt;get_dataref();
 # read data directly from file
 open my $file, '&lt;data.dat' or die &quot;couldn't open data.dat&quot;;
 my $len = $size*PDL::Core::howbig($pdl-&gt;get_datatype);
 croak &quot;couldn't read enough data&quot; if
 read( $file, $$dref, $len) != $len;
 close $file;
 $pdl-&gt;upd_data();
 return $pdl;
 }</pre><h2>Creating a piddle in C</h2>The following example creates a piddle at the C level. We use the <tt>&quot;Inline&quot;</tt> module which is really the way to interface Perl and C these days. Note the use of the <tt>&quot;PDL_INCLUDE&quot;</tt>, <tt>&quot;PDL_TYPEMAP&quot;</tt>, <tt>&quot;PDL_AUTO_INCLUDE&quot;</tt> and <tt>&quot;PDL_BOOT&quot;</tt> functions that were imported from <tt>&quot;PDL::Core::Dev&quot;</tt>. They are used in conjunction with an Inline Config call to ensure that the <font SIZE="-1">PDL</font> typemap, the <font SIZE="-1">PDL</font> include files and the <font SIZE="-1">PDL</font> Core routines are found during compilation and later runtime execution. 

 <pre> use PDL::LiteF;
 use PDL::Core::Dev;
 $a = myfloatseq(); # exercise our C piddle constructor
 print $a-&gt;info,&quot;\n&quot;;
 # the reason for this config call is explained below
 use Inline C =&gt; Config =&gt;
 INC =&gt; &amp;PDL_INCLUDE, # make sure we find pdlcore.h etc
 TYPEMAPS =&gt; &amp;PDL_TYPEMAP, # use the PDL typemap
 AUTO_INCLUDE =&gt; &amp;PDL_AUTO_INCLUDE, # global declarations and includes
 BOOT =&gt; &amp;PDL_BOOT; # boot code to load the Core struct
 use Inline C;
 Inline-&gt;init; # useful if you want to be able to 'do'-load this script
 __DATA__
 __C__
 static pdl* new_pdl(int datatype, PDL_Indx dims[], int ndims)
 {
 pdl *p = PDL-&gt;pdlnew();
 PDL-&gt;setdims (p, dims, ndims); /* set dims */
 p-&gt;datatype = datatype; /* and data type */
 PDL-&gt;allocdata (p); /* allocate the data chunk */
 return p;
 }
 pdl* myfloatseq()
 {
 PDL_Indx dims[] = {5,5,5};
 pdl *p = new_pdl(PDL_F,dims,3);
 PDL_Float *dataf = (PDL_Float *) p-&gt;data;
 PDL_Indx i; /* dimensions might be 64bits */
 for (i=0;i&lt;5*5*5;i++)
 dataf[i] = i; /* the data must be initialized ! */
 return p;
 }</pre><h3>Wrapping your own data into a piddle</h3>Sometimes you obtain a chunk of data from another source, for example an image processing library, etc. All you want to do in that case is wrap your data into a piddle struct at the C level. Examples using this approach can be found in the <font SIZE="-1">IO</font> modules (where FastRaw and FlexRaw use it for mmapped access) and the Gimp Perl module (that uses it to wrap Gimp pixel regions into piddles). The following script demonstrates a simple example: 

 <pre> use PDL::LiteF;
 use PDL::Core::Dev;
 use PDL::Graphics::PGPLOT;
 $b = mkpiddle();
 print $b-&gt;info,&quot;\n&quot;;
 imag1 $b;
 use Inline C =&gt; Config =&gt;
 INC =&gt; &amp;PDL_INCLUDE,
 TYPEMAPS =&gt; &amp;PDL_TYPEMAP,
 AUTO_INCLUDE =&gt; &amp;PDL_AUTO_INCLUDE,
 BOOT =&gt; &amp;PDL_BOOT;
 use Inline C;
 Inline-&gt;init;
 __DATA__
 __C__
 /* wrap a user supplied chunk of data into a piddle
 * You must specify the dimensions (dims,ndims) and 
 * the datatype (constants for the datatypes are declared
 * in pdl.h; e.g. PDL_B for byte type, etc)
 *
 * when the created piddle 'npdl' is destroyed on the
 * Perl side the function passed as the 'delete_magic'
 * parameter will be called with the pointer to the pdl structure
 * and the 'delparam' argument.
 * This gives you an opportunity to perform any clean up
 * that is necessary. For example, you might have to
 * explicitly call a function to free the resources
 * associated with your data pointer.
 * At the very least 'delete_magic' should zero the piddle's data pointer:
 * 
 * void delete_mydata(pdl* pdl, int param)
 * {
 * pdl-&gt;data = 0;
 * }
 * pdl *p = pdl_wrap(mydata, PDL_B, dims, ndims, delete_mydata,0);
 *
 * pdl_wrap returns the pointer to the pdl
 * that was created.
 */
 typedef void (*DelMagic)(pdl *, int param);
 static void default_magic(pdl *p, int pa) { p-&gt;data = 0; }
 static pdl* pdl_wrap(void *data, int datatype, PDL_Indx dims[],
 int ndims, DelMagic delete_magic, int delparam)
 {
 pdl* npdl = PDL-&gt;pdlnew(); /* get the empty container */
 PDL-&gt;setdims(npdl,dims,ndims); /* set dims */
 npdl-&gt;datatype = datatype; /* and data type */
 npdl-&gt;data = data; /* point it to your data */
 /* make sure the core doesn't meddle with your data */
 npdl-&gt;state |= PDL_DONTTOUCHDATA | PDL_ALLOCATED;
 if (delete_magic != NULL)
 PDL-&gt;add_deletedata_magic(npdl, delete_magic, delparam);
 else
 PDL-&gt;add_deletedata_magic(npdl, default_magic, 0);
 return npdl;
 }
 #define SZ 256
 /* a really silly function that makes a ramp image
 * in reality this could be an opaque function
 * in some library that you are using
 */
 static PDL_Byte* mkramp(void)
 {
 PDL_Byte *data;
 int i; /* should use PDL_Indx to support 64bit pdl indexing */
 if ((data = malloc(SZ*SZ*sizeof(PDL_Byte))) == NULL)
 croak(&quot;mkramp: Couldn't allocate memory&quot;);
 for (i=0;i&lt;SZ*SZ;i++)
 data[i] = i % SZ;
 return data;
 }
 /* this function takes care of the required clean-up */
 static void delete_myramp(pdl* p, int param)
 {
 if (p-&gt;data)
 free(p-&gt;data);
 p-&gt;data = 0;
 }
 pdl* mkpiddle()
 {
 PDL_Indx dims[] = {SZ,SZ};
 pdl *p;
 p = pdl_wrap((void *) mkramp(), PDL_B, dims, 2, 
 delete_myramp,0); /* the delparam is abitrarily set to 0 */
 return p;
 }</pre><h2>The gory details</h2><h3>The Core struct --- getting at <font SIZE="-1">PDL</font> core routines at runtime</h3><font SIZE="-1">PDL</font> uses a technique similar to that employed by the Tk modules to let other modules use its core routines. A pointer to all shared core <font SIZE="-1">PDL</font> routines is stored in the <tt>$PDL::SHARE</tt> variable. <font SIZE="-1">XS</font> code should get hold of this pointer at boot time so that the rest of the C/XS code can then use that pointer for access at run time. This initial loading of the pointer is most easily achieved using the functions <tt>&quot;PDL_AUTO_INCLUDE&quot;</tt> and <tt>&quot;PDL_BOOT&quot;</tt> that are defined and exported by <tt>&quot;PDL::Core::Dev&quot;</tt>. Typical usage with the Inline module has already been demonstrated: 

 <pre> use Inline C =&gt; Config =&gt;
 INC =&gt; &amp;PDL_INCLUDE,
 TYPEMAPS =&gt; &amp;PDL_TYPEMAP,
 AUTO_INCLUDE =&gt; &amp;PDL_AUTO_INCLUDE, # declarations
 BOOT =&gt; &amp;PDL_BOOT; # code for the XS boot section</pre>The code returned by <tt>&quot;PDL_AUTO_INCLUDE&quot;</tt> makes sure that <i>pdlcore.h</i> is included and declares the static variables to hold the pointer to the <tt>&quot;Core&quot;</tt> struct. It looks something like this: 

 <pre> print PDL_AUTO_INCLUDE;
 #include &lt;pdlcore.h&gt;
 static Core* PDL; /* Structure holds core C functions */
 static SV* CoreSV; /* Gets pointer to Perl var holding core structure */</pre>The code returned by <tt>&quot;PDL_BOOT&quot;</tt> retrieves the <tt>$PDL::SHARE</tt> variable and initializes the pointer to the <tt>&quot;Core&quot;</tt> struct. For those who know their way around the Perl <font SIZE="-1">API</font> here is the code: 

 <pre> print PDL_BOOT;
 perl_require_pv (&quot;PDL::Core&quot;); /* make sure PDL::Core is loaded */
 CoreSV = perl_get_sv(&quot;PDL::SHARE&quot;,FALSE); /* SV* value */
 #ifndef aTHX_
 #define aTHX_
 #endif
 if (CoreSV==NULL)
 Perl_croak(aTHX_ &quot;We require the PDL::Core module, which was not found&quot;);
 PDL = INT2PTR(Core*,SvIV( CoreSV )); /* Core* value */
 if (PDL-&gt;Version != PDL_CORE_VERSION)
 Perl_croak(aTHX_ &quot;The code needs to be recompiled against the newly installed PDL&quot;);</pre>The <tt>&quot;Core&quot;</tt> struct contains version info to ensure that the structure defined in <i>pdlcore.h</i> really corresponds to the one obtained at runtime. The code above tests for this 

 <pre> if (PDL-&gt;Version != PDL_CORE_VERSION)
 ....</pre>For more information on the Core struct see PDL::Internals. 

 With these preparations your code can now access the core routines as already shown in some of the examples above, e.g. 

 <pre> pdl *p = PDL-&gt;pdlnew();</pre>By default the C variable named <tt>&quot;PDL&quot;</tt> is used to hold the pointer to the <tt>&quot;Core&quot;</tt> struct. If that is (for whichever reason) a problem you can explicitly specify a name for the variable with the <tt>&quot;PDL_AUTO_INCLUDE&quot;</tt> and the <tt>&quot;PDL_BOOT&quot;</tt> routines: 

 <pre> use Inline C =&gt; Config =&gt;
 INC =&gt; &amp;PDL_INCLUDE,
 TYPEMAPS =&gt; &amp;PDL_TYPEMAP,
 AUTO_INCLUDE =&gt; &amp;PDL_AUTO_INCLUDE 'PDL_Corep',
 BOOT =&gt; &amp;PDL_BOOT 'PDL_Corep';</pre>Make sure you use the same identifier with <tt>&quot;PDL_AUTO_INCLUDE&quot;</tt> and <tt>&quot;PDL_BOOT&quot;</tt> and use that same identifier in your own code. E.g., continuing from the example above: 

 <pre> pdl *p = PDL_Corep-&gt;pdlnew();</pre><h3>Some selected core routines explained</h3>The full definition of the <tt>&quot;Core&quot;</tt> struct can be found in the file <i>pdlcore.h</i>. In the following the most frequently used member functions of this struct are briefly explained.
<dl><dt>&bull;
<dd><tt>&quot;pdl *SvPDLV(SV *sv)&quot;</tt>
<dt>&bull;
<dd><tt>&quot;pdl *SetSV_PDL(SV *sv, pdl *it)&quot;</tt>
<dt>&bull;
<dd><tt>&quot;pdl *pdlnew()&quot;</tt> 

 <tt>&quot;pdlnew&quot;</tt> returns an empty pdl object that needs further initialization to turn it into a proper piddle. Example: 

 <pre> pdl *p = PDL-&gt;pdlnew();
 PDL-&gt;setdims(p,dims,ndims);
 p-&gt;datatype = PDL_B;</pre><dt>&bull;
<dd><tt>&quot;pdl *null()&quot;</tt>
<dt>&bull;
<dd><tt>&quot;SV *copy(pdl* p, char* )&quot;</tt>
<dt>&bull;
<dd><tt>&quot;void *smalloc(STRLEN nbytes)&quot;</tt>
<dt>&bull;
<dd><tt>&quot;int howbig(int pdl_datatype)&quot;</tt>
<dt>&bull;
<dd><tt>&quot;void add_deletedata_magic(pdl *p, void (*func)(pdl*, int), int param)&quot;</tt>
<dt>&bull;
<dd><tt>&quot;void allocdata(pdl *p)&quot;</tt>
<dt>&bull;
<dd><tt>&quot;void make_physical(pdl *p)&quot;</tt>
<dt>&bull;
<dd><tt>&quot;void make_physdims(pdl *p)&quot;</tt>
<dt>&bull;
<dd><tt>&quot;void make_physvaffine(pdl *p)&quot;</tt>
<dt>&bull;
<dd><tt>&quot;void qsort_X(PDL_Xtype *data, PDL_Indx a, PDL_Indx b)&quot;</tt> and <tt>&quot;void qsort_ind_X(PDL_Xtype *data, PDL_Indx *ix, PDL_Indx a, PDL_Indx b)&quot;</tt> 

 where X is one of B,S,U,L,F,D and Xtype is one of Byte, Short, Ushort, Long, Float or Double. PDL_Indx is the C integer type corresponding to appropriate indexing size for the perl configuration (ivsize and ivtype). It can be either 'long' or 'long long' depending on whether your perl is 32bit or 64bit enabled.
<dt>&bull;
<dd><tt>&quot;float NaN_float&quot;</tt> and <tt>&quot;double NaN_double&quot;</tt> 

 These are constants to produce the required NaN values.
<dt>&bull;
<dd><tt>&quot;void pdl_barf(const char* pat,...)&quot;</tt> and <tt>&quot;void pdl_warn(const char* pat,...)&quot;</tt> 

 These are C-code equivalents of <tt>&quot;barf&quot;</tt> and <tt>&quot;warn&quot;</tt>. They include special handling of error or warning messages during pthreading (i.e. processor multi-threading) that defer the messages until after pthreading is completed. When pthreading is complete, perl's <tt>&quot;barf&quot;</tt> or <tt>&quot;warn&quot;</tt> is called with the deferred messages. This is needed to keep from calling perl's <tt>&quot;barf&quot;</tt> or <tt>&quot;warn&quot;</tt> during pthreading, which can cause segfaults. 

 Note that <tt>&quot;barf&quot;</tt> and <tt>&quot;warn&quot;</tt> have been redefined (using c-preprocessor macros) in pdlcore.h to <tt>&quot;PDL-&gt;barf&quot;</tt> and <tt>&quot;PDL-&gt;warn&quot;</tt>. This is to keep any <font SIZE="-1">XS</font> or <font SIZE="-1">PP</font> code from calling perl's <tt>&quot;barf&quot;</tt> or <tt>&quot;warn&quot;</tt> directly, which can cause segfaults during pthreading. 

 See PDL::ParallelCPU for more information on pthreading.</dl><h2>See Also</h2><font SIZE="-1">PDL</font> 

 Inline
<h2>Bugs</h2>This manpage is still under development. Feedback and corrections are welcome.
<h2>Copyright</h2>Copyright 2013 Chris Marshall (chm [at] cpan.org). 

 Copyright 2010 Christian Soeller (c.soeller [at] auckland.ac.nz). You can distribute and/or modify this document under the same terms as the current Perl license. 

 See: <a rel="nofollow" HREF="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a>
