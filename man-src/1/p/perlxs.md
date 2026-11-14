---
title: "perlxs(1)"
name: "perlxs"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlxs/"
description: "perlxs – XS language reference manual"
---

<h2 class="name">NAME</h2>
<p> perlxs &#8211; XS language reference manual </p>
<h2>DESCRIPTION</h2>
<h3>Introduction</h3>
<p> <font SIZE="-1">XS</font> is an interface description file format used to create an extension interface between Perl and C code (or a C library) which one wishes to use with Perl. The <font SIZE="-1">XS</font> interface is combined with the library to create a new library which can then be either dynamically loaded or statically linked into perl. The <font SIZE="-1">XS</font> interface description is written in the <font SIZE="-1">XS</font> language and is the core component of the Perl extension interface. </p>
<p> Before writing <font SIZE="-1">XS,</font> read the &#8220;<font SIZE="-1">CAVEATS&#8221;</font> section below. </p>
<p> An <font SIZE="-1"><code>XSUB</code></font> forms the basic unit of the <font SIZE="-1">XS</font> interface. After compilation by the <code>xsubpp</code> compiler, each <font SIZE="-1">XSUB</font> amounts to a C function definition which will provide the glue between Perl calling conventions and C calling conventions. </p>
<p> The glue code pulls the arguments from the Perl stack, converts these Perl values to the formats expected by a C function, call this C function, transfers the return values of the C function back to Perl. Return values here may be a conventional C return value or any C function arguments that may serve as output parameters. These return values may be passed back to Perl either by putting them on the Perl stack, or by modifying the arguments supplied from the Perl side. </p>
<p> The above is a somewhat simplified view of what really happens. Since Perl allows more flexible calling conventions than C, XSUBs may do much more in practice, such as checking input parameters for validity, throwing exceptions (or returning undef/empty list) if the return value from the C function indicates failure, calling different C functions based on numbers and types of the arguments, providing an object-oriented interface, etc. </p>
<p> Of course, one could write such glue code directly in C. However, this would be a tedious task, especially if one needs to write glue for multiple C functions, and/or one is not familiar enough with the Perl stack discipline and other such arcana. <font SIZE="-1">XS</font> comes to the rescue here: instead of writing this glue C code in long-hand, one can write a more concise short-hand <i>description</i> of what should be done by the glue, and let the <font SIZE="-1">XS</font> compiler <code>xsubpp</code> handle the rest. </p>
<p> The <font SIZE="-1">XS</font> language allows one to describe the mapping between how the C routine is used, and how the corresponding Perl routine is used. It also allows creation of Perl routines which are directly translated to C code and which are not related to a pre-existing C function. In cases when the C interface coincides with the Perl interface, the <font SIZE="-1">XSUB</font> declaration is almost identical to a declaration of a C function (in K&amp;R style). In such circumstances, there is another tool called <tt>&quot;h2xs&quot;</tt> that is able to translate an entire C header file into a corresponding <font SIZE="-1">XS</font> file that will provide glue to the functions/macros described in the header file. </p>
<p> The <font SIZE="-1">XS</font> compiler is called <code>xsubpp</code>. This compiler creates the constructs necessary to let an <font SIZE="-1">XSUB</font> manipulate Perl values, and creates the glue necessary to let Perl call the <font SIZE="-1">XSUB.</font> The compiler uses <code>typemaps</code> to determine how to map C function parameters and output values to Perl values and back. The default typemap (which comes with Perl) handles many common C types. A supplementary typemap may also be needed to handle any special structures and types for the library being linked. For more information on typemaps, see perlxstypemap. </p>
<p> A file in <font SIZE="-1">XS</font> format starts with a C language section which goes until the first <tt>&quot;MODULE =&quot;</tt> directive. Other <font SIZE="-1">XS</font> directives and <font SIZE="-1">XSUB</font> definitions may follow this line. The &#8220;language&#8221; used in this part of the file is usually referred to as the <font SIZE="-1">XS</font> language. <code>xsubpp</code> recognizes and skips <font SIZE="-1">POD</font> (see perlpod) in both the C and <font SIZE="-1">XS</font> language sections, which allows the <font SIZE="-1">XS</font> file to contain embedded documentation. </p>
<p> See perlxstut for a tutorial on the whole extension creation process. </p>
<p> Note: For some extensions, Dave Beazley&#8217;s <font SIZE="-1">SWIG</font> system may provide a significantly more convenient mechanism for creating the extension glue code. See &lt;<a rel="nofollow" href="http://www.swig.org/">http://www.swig.org/</a>&gt; for more information.</p>
<h3>On The Road</h3>
<p> Many of the examples which follow will concentrate on creating an interface between Perl and the <font SIZE="-1">ONC+ RPC</font> bind library functions. The <code>rpcb_gettime()</code> function is used to demonstrate many features of the <font SIZE="-1">XS</font> language. This function has two parameters; the first is an input parameter and the second is an output parameter. The function also returns a status value. </p>
<pre><code>
bool_t rpcb_gettime(const char *host, time_t *timep);
</code></pre>
<p> From C this function will be called with the following statements. </p>
<p>#include &lt;rpc/rpc.h&gt;<br />
bool_t status;<br />
time_t timep;<br />
status = rpcb_gettime(&#8220;localhost&#8221;, &amp;timep);</p>
<p> If an <font SIZE="-1">XSUB</font> is created to offer a direct translation between this function and Perl, then this <font SIZE="-1">XSUB</font> will be used from Perl with the following code. The <tt>$status</tt> and <tt>$timep</tt> variables will contain the output of the function. </p>
<p>use RPC;<br />
$status = rpcb_gettime(&#8220;localhost&#8221;, $timep);</p>
<p> The following <font SIZE="-1">XS</font> file shows an <font SIZE="-1">XS</font> subroutine, or <font SIZE="-1">XSUB,</font> which demonstrates one possible interface to the <code>rpcb_gettime()</code> function. This <font SIZE="-1">XSUB</font> represents a direct translation between C and Perl and so preserves the interface even from Perl. This <font SIZE="-1">XSUB</font> will be invoked from Perl with the usage shown above. Note that the first three #include statements, for <tt>&quot;EXTERN.h&quot;</tt>, <tt>&quot;perl.h&quot;</tt>, and <tt>&quot;XSUB.h&quot;</tt>, will always be present at the beginning of an <font SIZE="-1">XS</font> file. This approach and others will be expanded later in this document. A #define for <tt>&quot;PERL_NO_GET_CONTEXT&quot;</tt> should be present to fetch the interpreter context more efficiently, see perlguts for details. </p>
<p>#define PERL_NO_GET_CONTEXT<br />
#include &#8220;EXTERN.h&#8221;<br />
#include &#8220;XSUB.h&#8221;<br />
#include &#8220;perl.h&#8221;<br />
#include &lt;rpc/rpc.h&gt;<br />
MODULE = RPC PACKAGE = RPC<br />
    bool_t<br />
    rpcb_gettime(host, timep)<br />
char *host<br />
    time_t &amp;timep<br />
        OUTPUT : timep</p>
<p> Any extension to Perl, including those containing XSUBs, should have a Perl module to serve as the bootstrap which pulls the extension into Perl. This module will export the extension&#8217;s functions and variables to the Perl program and will cause the extension&#8217;s XSUBs to be linked into Perl. The following module will be used for most of the examples in this document and should be used from Perl with the <tt>&quot;use&quot;</tt> command as shown earlier. Perl modules are explained in more detail later in this document. </p>
<p>package RPC;<br />
require Exporter;<br />
require DynaLoader;<br />
@ISA = qw(Exporter DynaLoader);<br />
@EXPORT = qw(rpcb_gettime);<br />
bootstrap RPC;<br />
1;</p>
<p> Throughout this document a variety of interfaces to the <code>rpcb_gettime()</code> <font SIZE="-1">XSUB</font> will be explored. The XSUBs will take their parameters in different orders or will take different numbers of parameters. In each case the <font SIZE="-1">XSUB</font> is an abstraction between Perl and the real C <code>rpcb_gettime()</code> function, and the <font SIZE="-1">XSUB</font> must always ensure that the real <code>rpcb_gettime()</code> function is called with the correct parameters. This abstraction will allow the programmer to create a more Perl-like interface to the C function.</p>
<h3>The Anatomy of an <font SIZE="-1">XSUB</font></h3>
<p> The simplest XSUBs consist of 3 parts: a description of the return value, the name of the <font SIZE="-1">XSUB</font> routine and the names of its arguments, and a description of types or formats of the arguments. </p>
<p> The following <font SIZE="-1">XSUB</font> allows a Perl program to access a C library function called <code>sin()</code>. The <font SIZE="-1">XSUB</font> will imitate the C function which takes a single argument and returns a single value. </p>
<pre>
     double
     sin(x)
       double x
</pre>
<p> Optionally, one can merge the description of types and the list of argument names, rewriting this as </p>
<pre>
     double
     sin(double x)
</pre>
<p> This makes this <font SIZE="-1">XSUB</font> look similar to an <font SIZE="-1">ANSI C</font> declaration. An optional semicolon is allowed after the argument list, as in </p>
<p>double<br />
sin(double x);</p>
<p> Parameters with C pointer types can have different semantic: C functions with similar declarations </p>
<p>bool string_looks_as_a_number(char *s);<br />
bool make_char_uppercase(char *c);</p>
<p> are used in absolutely incompatible manner. Parameters to these functions could be described <code>xsubpp</code> like this: </p>
<pre>
     char *  s
     char    &amp;c
</pre>
<p> Both these <font SIZE="-1">XS</font> declarations correspond to the <tt>&quot;char*&quot;</tt> C type, but they have different semantics, see &#8220;The &amp; Unary Operator&#8221;. </p>
<p> It is convenient to think that the indirection operator <tt>&quot;*&quot;</tt> should be considered as a part of the type and the address operator <tt>&quot;&amp;&quot;</tt> should be considered part of the variable. See perlxstypemap for more info about handling qualifiers and unary operators in C types. </p>
<p> The function name and the return type must be placed on separate lines and should be flush left-adjusted. </p>
<p>INCORRECT CORRECT double sin(x)<br />
double double x sin(x)<br />
double x</p>
<p> The rest of the function description may be indented or left-adjusted. The following example shows a function with its body left-adjusted. Most examples in this document will indent the body for better readability. </p>
<pre>
  CORRECT
  double
  sin(x)
  double x
</pre>
<p> More complicated XSUBs may contain many other sections. Each section of an <font SIZE="-1">XSUB</font> starts with the corresponding keyword, such as <font SIZE="-1">INIT:</font> or <font SIZE="-1">CLEANUP:.</font> However, the first two lines of an <font SIZE="-1">XSUB</font> always contain the same data: descriptions of the return type and the names of the function and its parameters. Whatever immediately follows these is considered to be an <font SIZE="-1">INPUT:</font> section unless explicitly marked with another keyword. (See &#8220;The <font SIZE="-1">INPUT:</font> Keyword&#8221;.) </p>
<p> An <font SIZE="-1">XSUB</font> section continues until another section-start keyword is found.</p>
<h3>The Argument Stack</h3>
<p> The Perl argument stack is used to store the values which are sent as parameters to the <font SIZE="-1">XSUB</font> and to store the <font SIZE="-1">XSUB</font>&#8216;s return value(s). In reality all Perl functions (including non-XSUB ones) keep their values on this stack all the same time, each limited to its own range of positions on the stack. In this document the first position on that stack which belongs to the active function will be referred to as position 0 for that function. </p>
<p> XSUBs refer to their stack arguments with the macro <font SIZE="-1"><code>ST</code></font><code>(x)</code>, where <i>x</i> refers to a position in this <font SIZE="-1">XSUB</font>&#8216;s part of the stack. Position 0 for that function would be known to the <font SIZE="-1">XSUB</font> as <font SIZE="-1"><code>ST</code></font>(0). The <font SIZE="-1">XSUB</font>&#8216;s incoming parameters and outgoing return values always begin at <font SIZE="-1"><code>ST</code></font>(0). For many simple cases the <code>xsubpp</code> compiler will generate the code necessary to handle the argument stack by embedding code fragments found in the typemaps. In more complex cases the programmer must supply the code.</p>
<h3>The <font SIZE="-1">RETVAL</font> Variable</h3>
<p> The <font SIZE="-1">RETVAL</font> variable is a special C variable that is declared automatically for you. The C type of <font SIZE="-1">RETVAL</font> matches the return type of the C library function. The <code>xsubpp</code> compiler will declare this variable in each <font SIZE="-1">XSUB</font> with non-<tt>&quot;void&quot;</tt> return type. By default the generated C function will use <font SIZE="-1">RETVAL</font> to hold the return value of the C library function being called. In simple cases the value of <font SIZE="-1">RETVAL</font> will be placed in <font SIZE="-1"><code>ST</code></font>(0) of the argument stack where it can be received by Perl as the return value of the <font SIZE="-1">XSUB.</font> </p>
<p> If the <font SIZE="-1">XSUB</font> has a return type of <tt>&quot;void&quot;</tt> then the compiler will not declare a <font SIZE="-1">RETVAL</font> variable for that function. When using a <font SIZE="-1">PPCODE:</font> section no manipulation of the <font SIZE="-1">RETVAL</font> variable is required, the section may use direct stack manipulation to place output values on the stack. </p>
<p> If <font SIZE="-1">PPCODE:</font> directive is not used, <tt>&quot;void&quot;</tt> return value should be used only for subroutines which do not return a value, <i>even if</i> <font SIZE="-1">CODE:</font> directive is used which sets <font SIZE="-1"><code>ST</code></font>(0) explicitly. </p>
<p> Older versions of this document recommended to use <tt>&quot;void&quot;</tt> return value in such cases. It was discovered that this could lead to segfaults in cases when <font SIZE="-1">XSUB</font> was <i>truly</i> <tt>&quot;void&quot;</tt>. This practice is now deprecated, and may be not supported at some future version. Use the return value <tt>&quot;SV *&quot;</tt> in such cases. (Currently <tt>&quot;xsubpp&quot;</tt> contains some heuristic code which tries to disambiguate between &#8220;truly-void&#8221; and &#8220;old-practice-declared-as-void&#8221; functions. Hence your code is at mercy of this heuristics unless you use <tt>&quot;SV *&quot;</tt> as return value.)</p>
<h3>Returning SVs, AVs and HVs through <font SIZE="-1">RETVAL</font></h3>
<p> When you&#8217;re using <font SIZE="-1">RETVAL</font> to return an <tt>&quot;SV *&quot;</tt>, there&#8217;s some magic going on behind the scenes that should be mentioned. When you&#8217;re manipulating the argument stack using the <font SIZE="-1">ST</font>(x) macro, for example, you usually have to pay special attention to reference counts. (For more about reference counts, see perlguts.) To make your life easier, the typemap file automatically makes <tt>&quot;RETVAL&quot;</tt> mortal when you&#8217;re returning an <tt>&quot;SV *&quot;</tt>. Thus, the following two XSUBs are more or less equivalent: </p>
<p>void alpha()<br />
    PPCODE : ST(0) = newSVpv(&#8220;Hello World&#8221;, 0);<br />
sv_2mortal(ST(0));<br />
XSRETURN(1);<br />
SV *beta()<br />
    CODE : RETVAL = newSVpv(&#8220;Hello World&#8221;, 0);<br />
OUTPUT : RETVAL</p>
<p> This is quite useful as it usually improves readability. While this works fine for an <tt>&quot;SV *&quot;</tt>, it&#8217;s unfortunately not as easy to have <tt>&quot;AV *&quot;</tt> or <tt>&quot;HV *&quot;</tt> as a return value. You <i>should</i> be able to write: </p>
<pre>
  AV *
  array()
      CODE:
          RETVAL = newAV();
          /* do something with RETVAL */
      OUTPUT:
          RETVAL
</pre>
<p> But due to an unfixable bug (fixing it would break lots of existing <font SIZE="-1">CPAN</font> modules) in the typemap file, the reference count of the <tt>&quot;AV *&quot;</tt> is not properly decremented. Thus, the above <font SIZE="-1">XSUB</font> would leak memory whenever it is being called. The same problem exists for <tt>&quot;HV *&quot;</tt>, <tt>&quot;CV *&quot;</tt>, and <tt>&quot;SVREF&quot;</tt> (which indicates a scalar reference, not a general <tt>&quot;SV *&quot;</tt>). In <font SIZE="-1">XS</font> code on perls starting with perl 5.16, you can override the typemaps for any of these types with a version that has proper handling of refcounts. In your <tt>&quot;TYPEMAP&quot;</tt> section, do </p>
<pre>
  AV*   T_AVREF_REFCOUNT_FIXED
</pre>
<p> to get the repaired variant. For backward compatibility with older versions of perl, you can instead decrement the reference count manually when you&#8217;re returning one of the aforementioned types using <tt>&quot;sv_2mortal&quot;</tt>: </p>
<p>AV *array()<br />
    CODE : RETVAL = newAV();<br />
sv_2mortal((SV *)RETVAL);<br />
/* do something with RETVAL */<br />
OUTPUT : RETVAL</p>
<p> Remember that you don&#8217;t have to do this for an <tt>&quot;SV *&quot;</tt>. The reference documentation for all core typemaps can be found in perlxstypemap.</p>
<h3>The <font SIZE="-1">MODULE</font> Keyword</h3>
<p> The <font SIZE="-1">MODULE</font> keyword is used to start the <font SIZE="-1">XS</font> code and to specify the package of the functions which are being defined. All text preceding the first <font SIZE="-1">MODULE</font> keyword is considered C code and is passed through to the output with <font SIZE="-1">POD</font> stripped, but otherwise untouched. Every <font SIZE="-1">XS</font> module will have a bootstrap function which is used to hook the XSUBs into Perl. The package name of this bootstrap function will match the value of the last <font SIZE="-1">MODULE</font> statement in the <font SIZE="-1">XS</font> source files. The value of <font SIZE="-1">MODULE</font> should always remain constant within the same <font SIZE="-1">XS</font> file, though this is not required. </p>
<p> The following example will start the <font SIZE="-1">XS</font> code and will place all functions in a package named <font SIZE="-1">RPC.</font> </p>
<pre>
     MODULE = RPC
</pre>
<h3>The <font SIZE="-1">PACKAGE</font> Keyword</h3>
<p> When functions within an <font SIZE="-1">XS</font> source file must be separated into packages the <font SIZE="-1">PACKAGE</font> keyword should be used. This keyword is used with the <font SIZE="-1">MODULE</font> keyword and must follow immediately after it when used. </p>
<p>MODULE = RPC PACKAGE = RPC<br />
    [XS code in package RPC] MODULE = RPC PACKAGE = RPCB<br />
        [XS code in package RPCB] MODULE = RPC PACKAGE = RPC<br />
            [XS code in package RPC]</p>
<p> The same package name can be used more than once, allowing for non-contiguous code. This is useful if you have a stronger ordering principle than package names. </p>
<p> Although this keyword is optional and in some cases provides redundant information it should always be used. This keyword will ensure that the XSUBs appear in the desired package.</p>
<h3>The <font SIZE="-1">PREFIX</font> Keyword</h3>
<p> The <font SIZE="-1">PREFIX</font> keyword designates prefixes which should be removed from the Perl function names. If the C function is <tt>&quot;rpcb_gettime()&quot;</tt> and the <font SIZE="-1">PREFIX</font> value is <tt>&quot;rpcb_&quot;</tt> then Perl will see this function as <tt>&quot;gettime()&quot;</tt>. </p>
<p> This keyword should follow the <font SIZE="-1">PACKAGE</font> keyword when used. If <font SIZE="-1">PACKAGE</font> is not used then <font SIZE="-1">PREFIX</font> should follow the <font SIZE="-1">MODULE</font> keyword. </p>
<pre>
     MODULE = RPC  PREFIX = rpc_
     MODULE = RPC  PACKAGE = RPCB  PREFIX = rpcb_
</pre>
<h3>The <font SIZE="-1">OUTPUT:</font> Keyword</h3>
<p> The <font SIZE="-1">OUTPUT:</font> keyword indicates that certain function parameters should be updated (new values made visible to Perl) when the <font SIZE="-1">XSUB</font> terminates or that certain values should be returned to the calling Perl function. For simple functions which have no <font SIZE="-1">CODE:</font> or <font SIZE="-1">PPCODE:</font> section, such as the <code>sin()</code> function above, the <font SIZE="-1">RETVAL</font> variable is automatically designated as an output value. For more complex functions the <code>xsubpp</code> compiler will need help to determine which variables are output variables. </p>
<p> This keyword will normally be used to complement the <font SIZE="-1">CODE:</font> keyword. The <font SIZE="-1">RETVAL</font> variable is not recognized as an output variable when the <font SIZE="-1">CODE:</font> keyword is present. The <font SIZE="-1">OUTPUT:</font> keyword is used in this situation to tell the compiler that <font SIZE="-1">RETVAL</font> really is an output variable. </p>
<p> The <font SIZE="-1">OUTPUT:</font> keyword can also be used to indicate that function parameters are output variables. This may be necessary when a parameter has been modified within the function and the programmer would like the update to be seen by Perl. </p>
<pre>
     bool_t
     rpcb_gettime(host,timep)
          char *host
          time_t &amp;timep
        OUTPUT:
          timep
</pre>
<p> The <font SIZE="-1">OUTPUT:</font> keyword will also allow an output parameter to be mapped to a matching piece of code rather than to a typemap. </p>
<p>bool_t<br />
rpcb_gettime(host, timep)<br />
char *host<br />
    time_t &amp;timep<br />
        OUTPUT : timep sv_setnv(ST(1), (double)timep);</p>
<p> <code>xsubpp</code> emits an automatic <tt>&quot;SvSETMAGIC()&quot;</tt> for all parameters in the <font SIZE="-1">OUTPUT</font> section of the <font SIZE="-1">XSUB,</font> except <font SIZE="-1">RETVAL.</font> This is the usually desired behavior, as it takes care of properly invoking &#8216;set&#8217; magic on output parameters (needed for hash or array element parameters that must be created if they didn&#8217;t exist). If for some reason, this behavior is not desired, the <font SIZE="-1">OUTPUT</font> section may contain a <tt>&quot;SETMAGIC: DISABLE&quot;</tt> line to disable it for the remainder of the parameters in the <font SIZE="-1">OUTPUT</font> section. Likewise, <tt>&quot;SETMAGIC: ENABLE&quot;</tt> can be used to reenable it for the remainder of the <font SIZE="-1">OUTPUT</font> section. See perlguts for more details about &#8216;set&#8217; magic.</p>
<h3>The <font SIZE="-1">NO_OUTPUT</font> Keyword</h3>
<p> The <font SIZE="-1">NO_OUTPUT</font> can be placed as the first token of the <font SIZE="-1">XSUB.</font> This keyword indicates that while the C subroutine we provide an interface to has a non-<tt>&quot;void&quot;</tt> return type, the return value of this C subroutine should not be returned from the generated Perl subroutine. </p>
<p> With this keyword present &#8220;The <font SIZE="-1">RETVAL</font> Variable&#8221; is created, and in the generated call to the subroutine this variable is assigned to, but the value of this variable is not going to be used in the auto-generated code. </p>
<p> This keyword makes sense only if <tt>&quot;RETVAL&quot;</tt> is going to be accessed by the user-supplied code. It is especially useful to make a function interface more Perl-like, especially when the C return value is just an error condition indicator. For example, </p>
<p>NO_OUTPUT int<br />
delete_file(char *name)<br />
    POSTCALL : if (RETVAL != 0)<br />
                   croak(&#8220;Error %d while deleting file &#8216;%s'&#8221;, RETVAL, name);</p>
<p> Here the generated <font SIZE="-1">XS</font> function returns nothing on success, and will <code>die()</code> with a meaningful error message on error.</p>
<h3>The <font SIZE="-1">CODE:</font> Keyword</h3>
<p> This keyword is used in more complicated XSUBs which require special handling for the C function. The <font SIZE="-1">RETVAL</font> variable is still declared, but it will not be returned unless it is specified in the <font SIZE="-1">OUTPUT:</font> section. </p>
<p> The following <font SIZE="-1">XSUB</font> is for a C function which requires special handling of its parameters. The Perl usage is given first. </p>
<pre>
     $status = rpcb_gettime( &quot;localhost&quot;, $timep );
</pre>
<p> The <font SIZE="-1">XSUB</font> follows. </p>
<p>bool_t<br />
rpcb_gettime(host, timep)<br />
char *host<br />
    time_t timep<br />
        CODE : RETVAL = rpcb_gettime(host, &amp;timep);<br />
OUTPUT : timep<br />
             RETVAL</p>
<h3>The <font SIZE="-1">INIT:</font> Keyword</h3>
<p> The <font SIZE="-1">INIT:</font> keyword allows initialization to be inserted into the <font SIZE="-1">XSUB</font> before the compiler generates the call to the C function. Unlike the <font SIZE="-1">CODE:</font> keyword above, this keyword does not affect the way the compiler handles <font SIZE="-1">RETVAL.</font> </p>
<p>bool_t<br />
rpcb_gettime(host, timep)<br />
char *host<br />
    time_t &amp;timep<br />
        INIT : printf(&#8220;# Host is %s
&#8221;, host);<br />
OUTPUT : timep</p>
<p> Another use for the <font SIZE="-1">INIT:</font> section is to check for preconditions before making a call to the C function: </p>
<p>long long<br />
lldiv(a, b)<br />
long long a long long b<br />
    INIT : if (a == 0 &amp;&amp; b == 0)<br />
               XSRETURN_UNDEF;<br />
if (b == 0)<br />
    croak(&#8220;lldiv: cannot divide by 0&#8221;);</p>
<h3>The <font SIZE="-1">NO_INIT</font> Keyword</h3>
<p> The <font SIZE="-1">NO_INIT</font> keyword is used to indicate that a function parameter is being used only as an output value. The <code>xsubpp</code> compiler will normally generate code to read the values of all function parameters from the argument stack and assign them to C variables upon entry to the function. <font SIZE="-1">NO_INIT</font> will tell the compiler that some parameters will be used for output rather than for input and that they will be handled before the function terminates. </p>
<p> The following example shows a variation of the <code>rpcb_gettime()</code> function. This function uses the timep variable only as an output variable and does not care about its initial contents. </p>
<pre>
     bool_t
     rpcb_gettime(host,timep)
          char *host
          time_t &amp;timep = NO_INIT
        OUTPUT:
          timep
</pre>
<h3>The <font SIZE="-1">TYPEMAP:</font> Keyword</h3>
<p> Starting with Perl 5.16, you can embed typemaps into your <font SIZE="-1">XS</font> code instead of or in addition to typemaps in a separate file. Multiple such embedded typemaps will be processed in order of appearance in the <font SIZE="-1">XS</font> code and like local typemap files take precedence over the default typemap, the embedded typemaps may overwrite previous definitions of <font SIZE="-1">TYPEMAP, INPUT,</font> and <font SIZE="-1">OUTPUT</font> stanzas. The syntax for embedded typemaps is </p>
<pre>
      TYPEMAP: &lt;&lt;HERE
      ... your typemap code here ...
      HERE
</pre>
<p> where the <tt>&quot;TYPEMAP&quot;</tt> keyword must appear in the first column of a new line. </p>
<p> Refer to perlxstypemap for details on writing typemaps.</p>
<h3>Initializing Function Parameters</h3>
<p> C function parameters are normally initialized with their values from the argument stack (which in turn contains the parameters that were passed to the <font SIZE="-1">XSUB</font> from Perl). The typemaps contain the code segments which are used to translate the Perl values to the C parameters. The programmer, however, is allowed to override the typemaps and supply alternate (or additional) initialization code. Initialization code starts with the first <tt>&quot;=&quot;</tt>, <tt>&quot;;&quot;</tt> or <tt>&quot;+&quot;</tt> on a line in the <font SIZE="-1">INPUT:</font> section. The only exception happens if this <tt>&quot;;&quot;</tt> terminates the line, then this <tt>&quot;;&quot;</tt> is quietly ignored. </p>
<p> The following code demonstrates how to supply initialization code for function parameters. The initialization code is eval&#8217;ed within double quotes by the compiler before it is added to the output so anything which should be interpreted literally [mainly <tt>&quot;$&quot;</tt>, <tt>&quot;@&quot;</tt>, or <tt>&quot;\&quot;</tt>] must be protected with backslashes. The variables <tt>$var</tt>, <tt>$arg</tt>, and <tt>$type</tt> can be used as in typemaps. </p>
<p>bool_t<br />
rpcb_gettime(host, timep)<br />
char *host = (char *)SvPV_nolen($arg);<br />
time_t &amp;timep = 0;<br />
OUTPUT : timep</p>
<p> This should not be used to supply default values for parameters. One would normally use this when a function parameter must be processed by another library function before it can be used. Default parameters are covered in the next section. </p>
<p> If the initialization begins with <tt>&quot;=&quot;</tt>, then it is output in the declaration for the input variable, replacing the initialization supplied by the typemap. If the initialization begins with <tt>&quot;;&quot;</tt> or <tt>&quot;+&quot;</tt>, then it is performed after all of the input variables have been declared. In the <tt>&quot;;&quot;</tt> case the initialization normally supplied by the typemap is not performed. For the <tt>&quot;+&quot;</tt> case, the declaration for the variable will include the initialization from the typemap. A global variable, <tt>%v</tt>, is available for the truly rare case where information from one initialization is needed in another initialization. </p>
<p> Here&#8217;s a truly obscure example: </p>
<p>bool_t<br />
    rpcb_gettime(host, timep)<br />
        time_t &amp;timep; /* \$v{timep}=@{[$v{timep}=$arg]} */<br />
char *host + SvOK($v{timep}) ? SvPV_nolen($arg) : NULL;<br />
OUTPUT : timep</p>
<p> The construct <tt>&quot;\$v{timep}=@{[$v{timep}=$arg]}&quot;</tt> used in the above example has a two-fold purpose: first, when this line is processed by <code>xsubpp</code>, the Perl snippet <tt>&quot;$v{timep}=$arg&quot;</tt> is evaluated. Second, the text of the evaluated snippet is output into the generated C file (inside a C comment)! During the processing of <tt>&quot;char *host&quot;</tt> line, <tt>$arg</tt> will evaluate to <tt>ST(0)</tt>, and <tt>$v{timep}</tt> will evaluate to <tt><a href="/docs/linux/man/1-st/">ST</a>(1)</tt>.</p>
<h3>Default Parameter Values</h3>
<p> Default values for <font SIZE="-1">XSUB</font> arguments can be specified by placing an assignment statement in the parameter list. The default value may be a number, a string or the special string <tt>&quot;NO_INIT&quot;</tt>. Defaults should always be used on the right-most parameters only. </p>
<p> To allow the <font SIZE="-1">XSUB</font> for <code>rpcb_gettime()</code> to have a default host value the parameters to the <font SIZE="-1">XSUB</font> could be rearranged. The <font SIZE="-1">XSUB</font> will then call the real <code>rpcb_gettime()</code> function with the parameters in the correct order. This <font SIZE="-1">XSUB</font> can be called from Perl with either of the following statements: </p>
<p>$status = rpcb_gettime($timep, $host);<br />
$status = rpcb_gettime($timep);</p>
<p> The <font SIZE="-1">XSUB</font> will look like the code which follows. A <font SIZE="-1">CODE:</font> block is used to call the real <code>rpcb_gettime()</code> function with the parameters in the correct order for that function. </p>
<p>bool_t<br />
    rpcb_gettime(timep, host = &#8220;localhost&#8221;) char *host<br />
    time_t timep = NO_INIT CODE : RETVAL = rpcb_gettime(host, &amp;timep);<br />
OUTPUT : timep<br />
             RETVAL</p>
<h3>The <font SIZE="-1">PREINIT:</font> Keyword</h3>
<p> The <font SIZE="-1">PREINIT:</font> keyword allows extra variables to be declared immediately before or after the declarations of the parameters from the <font SIZE="-1">INPUT:</font> section are emitted. </p>
<p> If a variable is declared inside a <font SIZE="-1">CODE:</font> section it will follow any typemap code that is emitted for the input parameters. This may result in the declaration ending up after C code, which is C syntax error. Similar errors may happen with an explicit <tt>&quot;;&quot;</tt>-type or <tt>&quot;+&quot;</tt>-type initialization of parameters is used (see &#8220;Initializing Function Parameters&#8221;). Declaring these variables in an <font SIZE="-1">INIT:</font> section will not help. </p>
<p> In such cases, to force an additional variable to be declared together with declarations of other variables, place the declaration into a <font SIZE="-1">PREINIT:</font> section. The <font SIZE="-1">PREINIT:</font> keyword may be used one or more times within an <font SIZE="-1">XSUB.</font> </p>
<p> The following examples are equivalent, but if the code is using complex typemaps then the first example is safer. </p>
<p>bool_t<br />
rpcb_gettime(timep)<br />
time_t timep = NO_INIT<br />
    PREINIT : char *host = &#8220;localhost&#8221;;<br />
CODE : RETVAL = rpcb_gettime(host, &amp;timep);<br />
OUTPUT : timep<br />
             RETVAL</p>
<p> For this particular case an <font SIZE="-1">INIT:</font> keyword would generate the same C code as the <font SIZE="-1">PREINIT:</font> keyword. Another correct, but error-prone example: </p>
<p>bool_t<br />
rpcb_gettime(timep)<br />
time_t timep = NO_INIT<br />
    CODE : char *host = &#8220;localhost&#8221;;<br />
RETVAL = rpcb_gettime(host, &amp;timep);<br />
OUTPUT : timep<br />
             RETVAL</p>
<p> Another way to declare <tt>&quot;host&quot;</tt> is to use a C block in the <font SIZE="-1">CODE:</font> section: </p>
<p>bool_t<br />
rpcb_gettime(timep)<br />
time_t timep = NO_INIT<br />
    CODE:<br />
{<br />
    char *host = &#8220;localhost&#8221;;<br />
    RETVAL = rpcb_gettime(host, &amp;timep);<br />
}<br />
OUTPUT : timep<br />
             RETVAL</p>
<p> The ability to put additional declarations before the typemap entries are processed is very handy in the cases when typemap conversions manipulate some global state: </p>
<p>MyObject<br />
    mutate(o)<br />
        PREINIT : MyState st = global_state;<br />
INPUT : MyObject o;<br />
CLEANUP : reset_to(global_state, st);</p>
<p> Here we suppose that conversion to <tt>&quot;MyObject&quot;</tt> in the <font SIZE="-1">INPUT:</font> section and from MyObject when processing <font SIZE="-1">RETVAL</font> will modify a global variable <tt>&quot;global_state&quot;</tt>. After these conversions are performed, we restore the old value of <tt>&quot;global_state&quot;</tt> (to avoid memory leaks, for example). </p>
<p> There is another way to trade clarity for compactness: <font SIZE="-1">INPUT</font> sections allow declaration of C variables which do not appear in the parameter list of a subroutine. Thus the above code for <code>mutate()</code> can be rewritten as </p>
<p>MyObject<br />
mutate(o)<br />
MyState st = global_state;<br />
MyObject o;<br />
CLEANUP : reset_to(global_state, st);</p>
<p> and the code for <code>rpcb_gettime()</code> can be rewritten as </p>
<pre>
     bool_t
     rpcb_gettime(timep)
          time_t timep = NO_INIT
          char *host = &quot;localhost&quot;;
        C_ARGS:
          host, &amp;timep
        OUTPUT:
          timep
          RETVAL
</pre>
<h3>The <font SIZE="-1">SCOPE:</font> Keyword</h3>
<p> The <font SIZE="-1">SCOPE:</font> keyword allows scoping to be enabled for a particular <font SIZE="-1">XSUB.</font> If enabled, the <font SIZE="-1">XSUB</font> will invoke <font SIZE="-1">ENTER</font> and <font SIZE="-1">LEAVE</font> automatically. </p>
<p> To support potentially complex type mappings, if a typemap entry used by an <font SIZE="-1">XSUB</font> contains a comment like <tt>&quot;/*scope*/&quot;</tt> then scoping will be automatically enabled for that <font SIZE="-1">XSUB.</font> </p>
<p> To enable scoping: </p>
<pre>
    SCOPE: ENABLE
</pre>
<p> To disable scoping: </p>
<pre>
    SCOPE: DISABLE
</pre>
<h3>The <font SIZE="-1">INPUT:</font> Keyword</h3>
<p> The <font SIZE="-1">XSUB</font>&#8216;s parameters are usually evaluated immediately after entering the <font SIZE="-1">XSUB.</font> The <font SIZE="-1">INPUT:</font> keyword can be used to force those parameters to be evaluated a little later. The <font SIZE="-1">INPUT:</font> keyword can be used multiple times within an <font SIZE="-1">XSUB</font> and can be used to list one or more input variables. This keyword is used with the <font SIZE="-1">PREINIT:</font> keyword. </p>
<p> The following example shows how the input parameter <tt>&quot;timep&quot;</tt> can be evaluated late, after a <font SIZE="-1">PREINIT.</font> </p>
<p>bool_t<br />
rpcb_gettime(host, timep)<br />
char *host<br />
    PREINIT : time_t tt;<br />
INPUT : time_t timep<br />
            CODE : RETVAL = rpcb_gettime(host, &amp;tt);<br />
timep = tt;<br />
OUTPUT : timep<br />
             RETVAL</p>
<p> The next example shows each input parameter evaluated late. </p>
<p>bool_t<br />
    rpcb_gettime(host, timep)<br />
        PREINIT : time_t tt;<br />
INPUT : char *host<br />
            PREINIT : char *h;<br />
INPUT : time_t timep<br />
            CODE : h = host;<br />
RETVAL = rpcb_gettime(h, &amp;tt);<br />
timep = tt;<br />
OUTPUT : timep<br />
             RETVAL</p>
<p> Since <font SIZE="-1">INPUT</font> sections allow declaration of C variables which do not appear in the parameter list of a subroutine, this may be shortened to: </p>
<p>bool_t<br />
rpcb_gettime(host, timep)<br />
time_t tt;<br />
char *host;<br />
char *h = host;<br />
time_t timep;<br />
CODE : RETVAL = rpcb_gettime(h, &amp;tt);<br />
timep = tt;<br />
OUTPUT : timep<br />
             RETVAL</p>
<p> (We used our knowledge that input conversion for <tt>&quot;char *&quot;</tt> is a &#8220;simple&#8221; one, thus <tt>&quot;host&quot;</tt> is initialized on the declaration line, and our assignment <tt>&quot;h = host&quot;</tt> is not performed too early. Otherwise one would need to have the assignment <tt>&quot;h = host&quot;</tt> in a <font SIZE="-1">CODE:</font> or <font SIZE="-1">INIT:</font> section.)</p>
<h3>The <font SIZE="-1">IN/OUTLIST/IN_OUTLIST/OUT/IN_OUT</font> Keywords</h3>
<p> In the list of parameters for an <font SIZE="-1">XSUB,</font> one can precede parameter names by the <tt>&quot;IN&quot;</tt>/<tt>&quot;OUTLIST&quot;</tt>/<tt>&quot;IN_OUTLIST&quot;</tt>/<tt>&quot;OUT&quot;</tt>/<tt>&quot;IN_OUT&quot;</tt> keywords. <tt>&quot;IN&quot;</tt> keyword is the default, the other keywords indicate how the Perl interface should differ from the C interface. </p>
<p> Parameters preceded by <tt>&quot;OUTLIST&quot;</tt>/<tt>&quot;IN_OUTLIST&quot;</tt>/<tt>&quot;OUT&quot;</tt>/<tt>&quot;IN_OUT&quot;</tt> keywords are considered to be used by the C subroutine <i>via pointers</i>. <tt>&quot;OUTLIST&quot;</tt>/<tt>&quot;OUT&quot;</tt> keywords indicate that the C subroutine does not inspect the memory pointed by this parameter, but will write through this pointer to provide additional return values. </p>
<p> Parameters preceded by <tt>&quot;OUTLIST&quot;</tt> keyword do not appear in the usage signature of the generated Perl function. </p>
<p> Parameters preceded by <tt>&quot;IN_OUTLIST&quot;</tt>/<tt>&quot;IN_OUT&quot;</tt>/<tt>&quot;OUT&quot;</tt> <i>do</i> appear as parameters to the Perl function. With the exception of <tt>&quot;OUT&quot;</tt>-parameters, these parameters are converted to the corresponding C type, then pointers to these data are given as arguments to the C function. It is expected that the C function will write through these pointers. </p>
<p> The return list of the generated Perl function consists of the C return value from the function (unless the <font SIZE="-1">XSUB</font> is of <tt>&quot;void&quot;</tt> return type or <tt>&quot;The NO_OUTPUT Keyword&quot;</tt> was used) followed by all the <tt>&quot;OUTLIST&quot;</tt> and <tt>&quot;IN_OUTLIST&quot;</tt> parameters (in the order of appearance). On the return from the <font SIZE="-1">XSUB</font> the <tt>&quot;IN_OUT&quot;</tt>/<tt>&quot;OUT&quot;</tt> Perl parameter will be modified to have the values written by the C function. </p>
<p> For example, an <font SIZE="-1">XSUB</font> </p>
<p>void day_month(OUTLIST day, IN unix_time, OUTLIST month) int day<br />
    int unix_time<br />
    int month</p>
<p> should be used from Perl as </p>
<pre>
  my ($day, $month) = day_month(time);
</pre>
<p> The C signature of the corresponding function should be </p>
<p>void day_month(int *day, int unix_time, int *month);</p>
<p> The <tt>&quot;IN&quot;</tt>/<tt>&quot;OUTLIST&quot;</tt>/<tt>&quot;IN_OUTLIST&quot;</tt>/<tt>&quot;IN_OUT&quot;</tt>/<tt>&quot;OUT&quot;</tt> keywords can be mixed with ANSI-style declarations, as in </p>
<p>void day_month(OUTLIST int day, int unix_time, OUTLIST int month)</p>
<p> (here the optional <tt>&quot;IN&quot;</tt> keyword is omitted). </p>
<p> The <tt>&quot;IN_OUT&quot;</tt> parameters are identical with parameters introduced with &#8220;The &amp; Unary Operator&#8221; and put into the <tt>&quot;OUTPUT:&quot;</tt> section (see &#8220;The <font SIZE="-1">OUTPUT:</font> Keyword&#8221;). The <tt>&quot;IN_OUTLIST&quot;</tt> parameters are very similar, the only difference being that the value C function writes through the pointer would not modify the Perl parameter, but is put in the output list. </p>
<p> The <tt>&quot;OUTLIST&quot;</tt>/<tt>&quot;OUT&quot;</tt> parameter differ from <tt>&quot;IN_OUTLIST&quot;</tt>/<tt>&quot;IN_OUT&quot;</tt> parameters only by the initial value of the Perl parameter not being read (and not being given to the C function &#8211; which gets some garbage instead). For example, the same C function as above can be interfaced with as </p>
<p>void day_month(OUT int day, int unix_time, OUT int month);</p>
<p> or </p>
<p>void day_month(day, unix_time, month) int &amp;day = NO_INIT int unix_time<br />
    int &amp;month = NO_INIT OUTPUT : day<br />
                                  month</p>
<p> However, the generated Perl function is called in very C-ish style: </p>
<p>my($day, $month);<br />
day_month($day, time, $month);</p>
<h3>The length(NAME) Keyword</h3>
<p> If one of the input arguments to the C function is the length of a string argument <tt>&quot;NAME&quot;</tt>, one can substitute the name of the length-argument by <tt>&quot;length(NAME)&quot;</tt> in the <font SIZE="-1">XSUB</font> declaration. This argument must be omitted when the generated Perl function is called. E.g., </p>
<p>void dump_chars(char *s, short l)<br />
{<br />
    short n = 0;<br />
    while (n &lt; l) {<br />
        printf(&#8220;s[%d] = \&#8221;\%#03o\&#8221;
&#8221;, n, (int)s[n]);<br />
        n++;<br />
    }<br />
}<br />
MODULE = x PACKAGE = x void dump_chars(char *s, short length(s))</p>
<p> should be called as <tt>&quot;dump_chars($string)&quot;</tt>. </p>
<p> This directive is supported with ANSI-type function declarations only.</p>
<h3>Variable-length Parameter Lists</h3>
<p> XSUBs can have variable-length parameter lists by specifying an ellipsis <tt>&quot;(...)&quot;</tt> in the parameter list. This use of the ellipsis is similar to that found in <font SIZE="-1">ANSI C.</font> The programmer is able to determine the number of arguments passed to the <font SIZE="-1">XSUB</font> by examining the <tt>&quot;items&quot;</tt> variable which the <code>xsubpp</code> compiler supplies for all XSUBs. By using this mechanism one can create an <font SIZE="-1">XSUB</font> which accepts a list of parameters of unknown length. </p>
<p> The <i>host</i> parameter for the <code>rpcb_gettime()</code> <font SIZE="-1">XSUB</font> can be optional so the ellipsis can be used to indicate that the <font SIZE="-1">XSUB</font> will take a variable number of parameters. Perl should be able to call this <font SIZE="-1">XSUB</font> with either of the following statements. </p>
<p>$status = rpcb_gettime($timep, $host);<br />
$status = rpcb_gettime($timep);</p>
<p> The <font SIZE="-1">XS</font> code, with ellipsis, follows. </p>
<p>bool_t<br />
rpcb_gettime(timep, &#8230;)<br />
    time_t timep = NO_INIT PREINIT : char *host = &#8220;localhost&#8221;;<br />
CODE : if (items &gt; 1)<br />
           host = (char *)SvPV_nolen(ST(1));<br />
RETVAL = rpcb_gettime(host, &amp;timep);<br />
OUTPUT : timep<br />
             RETVAL</p>
<h3>The C_ARGS: Keyword</h3>
<p> The C_ARGS: keyword allows creating of <font SIZE="-1">XSUBS</font> which have different calling sequence from Perl than from C, without a need to write <font SIZE="-1">CODE:</font> or <font SIZE="-1">PPCODE:</font> section. The contents of the C_ARGS: paragraph is put as the argument to the called C function without any change. </p>
<p> For example, suppose that a C function is declared as </p>
<p>symbolic nth_derivative(int n, symbolic function, int flags);</p>
<p> and that the default flags are kept in a global C variable <tt>&quot;default_flags&quot;</tt>. Suppose that you want to create an interface which is called as </p>
<p>$second_deriv = $function-&gt;nth_derivative(2);</p>
<p> To do this, declare the <font SIZE="-1">XSUB</font> as </p>
<pre>
    symbolic
    nth_derivative(function, n)
        symbolic        function
        int             n
      C_ARGS:
        n, function, default_flags
</pre>
<h3>The <font SIZE="-1">PPCODE:</font> Keyword</h3>
<p> The <font SIZE="-1">PPCODE:</font> keyword is an alternate form of the <font SIZE="-1">CODE:</font> keyword and is used to tell the <code>xsubpp</code> compiler that the programmer is supplying the code to control the argument stack for the XSUBs return values. Occasionally one will want an <font SIZE="-1">XSUB</font> to return a list of values rather than a single value. In these cases one must use <font SIZE="-1">PPCODE:</font> and then explicitly push the list of values on the stack. The <font SIZE="-1">PPCODE:</font> and <font SIZE="-1">CODE:</font> keywords should not be used together within the same <font SIZE="-1">XSUB.</font> </p>
<p> The actual difference between <font SIZE="-1">PPCODE:</font> and <font SIZE="-1">CODE:</font> sections is in the initialization of <tt>&quot;SP&quot;</tt> macro (which stands for the <i>current</i> Perl stack pointer), and in the handling of data on the stack when returning from an <font SIZE="-1">XSUB.</font> In <font SIZE="-1">CODE:</font> sections <font SIZE="-1">SP</font> preserves the value which was on entry to the <font SIZE="-1">XSUB: SP</font> is on the function pointer (which follows the last parameter). In <font SIZE="-1">PPCODE:</font> sections <font SIZE="-1">SP</font> is moved backward to the beginning of the parameter list, which allows <tt>&quot;PUSH*()&quot;</tt> macros to place output values in the place Perl expects them to be when the <font SIZE="-1">XSUB</font> returns back to Perl. </p>
<p> The generated trailer for a <font SIZE="-1">CODE:</font> section ensures that the number of return values Perl will see is either 0 or 1 (depending on the <tt>&quot;void&quot;</tt>ness of the return value of the C function, and heuristics mentioned in &#8220;The <font SIZE="-1">RETVAL</font> Variable&#8221;). The trailer generated for a <font SIZE="-1">PPCODE:</font> section is based on the number of return values and on the number of times <tt>&quot;SP&quot;</tt> was updated by <tt>&quot;[X]PUSH*()&quot;</tt> macros. </p>
<p> Note that macros <tt>ST(i)</tt>, <tt>&quot;XST_m*()&quot;</tt> and <tt>&quot;XSRETURN*()&quot;</tt> work equally well in <font SIZE="-1">CODE:</font> sections and <font SIZE="-1">PPCODE:</font> sections. </p>
<p> The following <font SIZE="-1">XSUB</font> will call the C <code>rpcb_gettime()</code> function and will return its two output values, timep and status, to Perl as a single list. </p>
<p>void<br />
    rpcb_gettime(host) char *host<br />
    PREINIT : time_t timep;<br />
bool_t status;<br />
PPCODE : status = rpcb_gettime(host, &amp;timep);<br />
EXTEND(SP, 2);<br />
PUSHs(sv_2mortal(newSViv(status)));<br />
PUSHs(sv_2mortal(newSViv(timep)));</p>
<p> Notice that the programmer must supply the C code necessary to have the real <code>rpcb_gettime()</code> function called and to have the return values properly placed on the argument stack. </p>
<p> The <tt>&quot;void&quot;</tt> return type for this function tells the <code>xsubpp</code> compiler that the <font SIZE="-1">RETVAL</font> variable is not needed or used and that it should not be created. In most scenarios the void return type should be used with the <font SIZE="-1">PPCODE:</font> directive. </p>
<p> The <font SIZE="-1"><code>EXTEND</code></font><code>()</code> macro is used to make room on the argument stack for 2 return values. The <font SIZE="-1">PPCODE:</font> directive causes the <code>xsubpp</code> compiler to create a stack pointer available as <tt>&quot;SP&quot;</tt>, and it is this pointer which is being used in the <font SIZE="-1"><code>EXTEND</code></font><code>()</code> macro. The values are then pushed onto the stack with the <code>PUSHs()</code> macro. </p>
<p> Now the <code>rpcb_gettime()</code> function can be used from Perl with the following statement. </p>
<pre>
     ($status, $timep) = rpcb_gettime(&quot;localhost&quot;);
</pre>
<p> When handling output parameters with a <font SIZE="-1">PPCODE</font> section, be sure to handle &#8216;set&#8217; magic properly. See perlguts for details about &#8216;set&#8217; magic.</p>
<h3>Returning Undef And Empty Lists</h3>
<p> Occasionally the programmer will want to return simply <tt>&quot;undef&quot;</tt> or an empty list if a function fails rather than a separate status value. The <code>rpcb_gettime()</code> function offers just this situation. If the function succeeds we would like to have it return the time and if it fails we would like to have undef returned. In the following Perl code the value of <tt>$timep</tt> will either be undef or it will be a valid time. </p>
<pre>
     $timep = rpcb_gettime( &quot;localhost&quot; );
</pre>
<p> The following <font SIZE="-1">XSUB</font> uses the <tt>&quot;SV *&quot;</tt> return type as a mnemonic only, and uses a <font SIZE="-1">CODE:</font> block to indicate to the compiler that the programmer has supplied all the necessary code. The <code>sv_newmortal()</code> call will initialize the return value to undef, making that the default return value. </p>
<p>SV *rpcb_gettime(host)<br />
char *host<br />
    PREINIT : time_t timep;<br />
bool_t x;<br />
CODE : ST(0) = sv_newmortal();<br />
if (rpcb_gettime(host, &amp;timep))<br />
    sv_setnv(ST(0), (double)timep);</p>
<p> The next example demonstrates how one would place an explicit undef in the return value, should the need arise. </p>
<p>SV *rpcb_gettime(host)<br />
char *host<br />
    PREINIT : time_t timep;<br />
bool_t x;<br />
CODE : if (rpcb_gettime(host, &amp;timep))<br />
{<br />
    ST(0) = sv_newmortal();<br />
    sv_setnv(ST(0), (double)timep);<br />
}<br />
else<br />
{<br />
    ST(0) = &amp;PL_sv_undef;<br />
}</p>
<p> To return an empty list one must use a <font SIZE="-1">PPCODE:</font> block and then not push return values on the stack. </p>
<p>void<br />
    rpcb_gettime(host) char *host<br />
    PREINIT : time_t timep;<br />
PPCODE : if (rpcb_gettime(host, &amp;timep))<br />
             PUSHs(sv_2mortal(newSViv(timep)));<br />
else<br />
{<br />
    /* Nothing pushed on stack, so an empty<br />
     * list is implicitly returned. */<br />
}</p>
<p> Some people may be inclined to include an explicit <tt>&quot;return&quot;</tt> in the above <font SIZE="-1">XSUB,</font> rather than letting control fall through to the end. In those situations <tt>&quot;XSRETURN_EMPTY&quot;</tt> should be used, instead. This will ensure that the <font SIZE="-1">XSUB</font> stack is properly adjusted. Consult perlapi for other <tt>&quot;XSRETURN&quot;</tt> macros. </p>
<p> Since <tt>&quot;XSRETURN_*&quot;</tt> macros can be used with <font SIZE="-1">CODE</font> blocks as well, one can rewrite this example as: </p>
<p>int rpcb_gettime(host)<br />
char *host<br />
    PREINIT : time_t timep;<br />
CODE : RETVAL = rpcb_gettime(host, &amp;timep);<br />
if (RETVAL == 0)<br />
    XSRETURN_UNDEF;<br />
OUTPUT : RETVAL</p>
<p> In fact, one can put this check into a <font SIZE="-1">POSTCALL:</font> section as well. Together with <font SIZE="-1">PREINIT:</font> simplifications, this leads to: </p>
<p>int rpcb_gettime(host)<br />
char *host<br />
    time_t timep;<br />
POSTCALL : if (RETVAL == 0)<br />
               XSRETURN_UNDEF;</p>
<h3>The <font SIZE="-1">REQUIRE:</font> Keyword</h3>
<p> The <font SIZE="-1">REQUIRE:</font> keyword is used to indicate the minimum version of the <code>xsubpp</code> compiler needed to compile the <font SIZE="-1">XS</font> module. An <font SIZE="-1">XS</font> module which contains the following statement will compile with only <code>xsubpp</code> version 1.922 or greater: </p>
<pre>
        REQUIRE: 1.922
</pre>
<h3>The <font SIZE="-1">CLEANUP:</font> Keyword</h3>
<p> This keyword can be used when an <font SIZE="-1">XSUB</font> requires special cleanup procedures before it terminates. When the <font SIZE="-1">CLEANUP:</font> keyword is used it must follow any <font SIZE="-1">CODE:,</font> or <font SIZE="-1">OUTPUT:</font> blocks which are present in the <font SIZE="-1">XSUB.</font> The code specified for the cleanup block will be added as the last statements in the <font SIZE="-1">XSUB.</font></p>
<h3>The <font SIZE="-1">POSTCALL:</font> Keyword</h3>
<p> This keyword can be used when an <font SIZE="-1">XSUB</font> requires special procedures executed after the C subroutine call is performed. When the <font SIZE="-1">POSTCALL:</font> keyword is used it must precede <font SIZE="-1">OUTPUT:</font> and <font SIZE="-1">CLEANUP:</font> blocks which are present in the <font SIZE="-1">XSUB.</font> </p>
<p> See examples in &#8220;The <font SIZE="-1">NO_OUTPUT</font> Keyword&#8221; and &#8220;Returning Undef And Empty Lists&#8221;. </p>
<p> The <font SIZE="-1">POSTCALL:</font> block does not make a lot of sense when the C subroutine call is supplied by user by providing either <font SIZE="-1">CODE:</font> or <font SIZE="-1">PPCODE:</font> section.</p>
<h3>The <font SIZE="-1">BOOT:</font> Keyword</h3>
<p> The <font SIZE="-1">BOOT:</font> keyword is used to add code to the extension&#8217;s bootstrap function. The bootstrap function is generated by the <code>xsubpp</code> compiler and normally holds the statements necessary to register any XSUBs with Perl. With the <font SIZE="-1">BOOT:</font> keyword the programmer can tell the compiler to add extra statements to the bootstrap function. </p>
<p> This keyword may be used any time after the first <font SIZE="-1">MODULE</font> keyword and should appear on a line by itself. The first blank line after the keyword will terminate the code block. </p>
<pre>
     BOOT:
     # The following message will be printed when the
     # bootstrap function executes.
     printf(&quot;Hello from the bootstrap!
&quot;);
</pre>
<h3>The <font SIZE="-1">VERSIONCHECK:</font> Keyword</h3>
<p> The <font SIZE="-1">VERSIONCHECK:</font> keyword corresponds to <code>xsubpp</code>&#8216;s <tt>&quot;-versioncheck&quot;</tt> and <tt>&quot;-noversioncheck&quot;</tt> options. This keyword overrides the command line options. Version checking is enabled by default. When version checking is enabled the <font SIZE="-1">XS</font> module will attempt to verify that its version matches the version of the <font SIZE="-1">PM</font> module. </p>
<p> To enable version checking: </p>
<pre>
    VERSIONCHECK: ENABLE
</pre>
<p> To disable version checking: </p>
<pre>
    VERSIONCHECK: DISABLE
</pre>
<p> Note that if the version of the <font SIZE="-1">PM</font> module is an <font SIZE="-1">NV</font> (a floating point number), it will be stringified with a possible loss of precision (currently chopping to nine decimal places) so that it may not match the version of the <font SIZE="-1">XS</font> module anymore. Quoting the <tt>$VERSION</tt> declaration to make it a string is recommended if long version numbers are used.</p>
<h3>The <font SIZE="-1">PROTOTYPES:</font> Keyword</h3>
<p> The <font SIZE="-1">PROTOTYPES:</font> keyword corresponds to <code>xsubpp</code>&#8216;s <tt>&quot;-prototypes&quot;</tt> and <tt>&quot;-noprototypes&quot;</tt> options. This keyword overrides the command line options. Prototypes are disabled by default. When prototypes are enabled, XSUBs will be given Perl prototypes. This keyword may be used multiple times in an <font SIZE="-1">XS</font> module to enable and disable prototypes for different parts of the module. Note that <code>xsubpp</code> will nag you if you don&#8217;t explicitly enable or disable prototypes, with: </p>
<pre>
    Please specify prototyping behavior for Foo.xs (see perlxs manual)
</pre>
<p> To enable prototypes: </p>
<pre>
    PROTOTYPES: ENABLE
</pre>
<p> To disable prototypes: </p>
<pre>
    PROTOTYPES: DISABLE
</pre>
<h3>The <font SIZE="-1">PROTOTYPE:</font> Keyword</h3>
<p> This keyword is similar to the <font SIZE="-1">PROTOTYPES:</font> keyword above but can be used to force <code>xsubpp</code> to use a specific prototype for the <font SIZE="-1">XSUB.</font> This keyword overrides all other prototype options and keywords but affects only the current <font SIZE="-1">XSUB.</font> Consult &#8220;Prototypes&#8221; in perlsub for information about Perl prototypes. </p>
<p>bool_t<br />
rpcb_gettime(timep, &#8230;)<br />
    time_t timep = NO_INIT PROTOTYPE : $;<br />
$<br />
    PREINIT : char *host = &#8220;localhost&#8221;;<br />
CODE : if (items &gt; 1)<br />
           host = (char *)SvPV_nolen(ST(1));<br />
RETVAL = rpcb_gettime(host, &amp;timep);<br />
OUTPUT : timep<br />
             RETVAL</p>
<p> If the prototypes are enabled, you can disable it locally for a given <font SIZE="-1">XSUB</font> as in the following example: </p>
<pre>
    void
    rpcb_gettime_noproto()
        PROTOTYPE: DISABLE
    ...
</pre>
<h3>The <font SIZE="-1">ALIAS:</font> Keyword</h3>
<p> The <font SIZE="-1">ALIAS:</font> keyword allows an <font SIZE="-1">XSUB</font> to have two or more unique Perl names and to know which of those names was used when it was invoked. The Perl names may be fully-qualified with package names. Each alias is given an index. The compiler will setup a variable called <tt>&quot;ix&quot;</tt> which contain the index of the alias which was used. When the <font SIZE="-1">XSUB</font> is called with its declared name <tt>&quot;ix&quot;</tt> will be 0. </p>
<p> The following example will create aliases <tt>&quot;FOO::gettime()&quot;</tt> and <tt>&quot;BAR::getit()&quot;</tt> for this function. </p>
<p>bool_t<br />
rpcb_gettime(host, timep)<br />
char *host<br />
    time_t &amp;timep<br />
        ALIAS : FOO::gettime = 1 BAR::getit = 2 INIT : printf(&#8220;# ix = %d
&#8221;, ix);<br />
OUTPUT : timep</p>
<h3>The <font SIZE="-1">OVERLOAD:</font> Keyword</h3>
<p> Instead of writing an overloaded interface using pure Perl, you can also use the <font SIZE="-1">OVERLOAD</font> keyword to define additional Perl names for your functions (like the <font SIZE="-1">ALIAS:</font> keyword above). However, the overloaded functions must be defined in such a way as to accept the number of parameters supplied by perl&#8217;s overload system. For most overload methods, it will be three parameters; for the <tt>&quot;nomethod&quot;</tt> function it will be four. However, the bitwise operators <tt>&quot;&amp;&quot;</tt>, <tt>&quot;|&quot;</tt>, <tt>&quot;^&quot;</tt>, and <tt>&quot;~&quot;</tt> may be called with three <i>or</i> five arguments (see overload). </p>
<p> If any function has the <font SIZE="-1">OVERLOAD:</font> keyword, several additional lines will be defined in the c file generated by xsubpp in order to register with the overload magic. </p>
<p> Since blessed objects are actually stored as <font SIZE="-1">RV</font>&#8216;s, it is useful to use the typemap features to preprocess parameters and extract the actual <font SIZE="-1">SV</font> stored within the blessed <font SIZE="-1">RV.</font> See the sample for T_PTROBJ_SPECIAL below. </p>
<p> To use the <font SIZE="-1">OVERLOAD:</font> keyword, create an <font SIZE="-1">XS</font> function which takes three input parameters (or use the C-style &#8216;&#8230;&#8217; definition) like this: </p>
<pre>
    SV *
    cmp (lobj, robj, swap)
    My_Module_obj    lobj
    My_Module_obj    robj
    IV               swap
    OVERLOAD: cmp &lt;=&gt;
    { /* function defined here */}
</pre>
<p> In this case, the function will overload both of the three way comparison operators. For all overload operations using non-alpha characters, you must type the parameter without quoting, separating multiple overloads with whitespace. Note that &quot;&#8220; (the stringify overload) should be entered as \&#8221;\&quot; (i.e. escaped). </p>
<p> Since, as mentioned above, bitwise operators may take extra arguments, you may want to use something like <tt>&quot;(lobj, robj, swap, ...)&quot;</tt> (with literal <tt>&quot;...&quot;</tt>) as your parameter list.</p>
<h3>The <font SIZE="-1">FALLBACK:</font> Keyword</h3>
<p> In addition to the <font SIZE="-1">OVERLOAD</font> keyword, if you need to control how Perl autogenerates missing overloaded operators, you can set the <font SIZE="-1">FALLBACK</font> keyword in the module header section, like this: </p>
<pre>
    MODULE = RPC  PACKAGE = RPC
    FALLBACK: TRUE
    ...
</pre>
<p> where <font SIZE="-1">FALLBACK</font> can take any of the three values <font SIZE="-1">TRUE, FALSE,</font> or <font SIZE="-1">UNDEF.</font> If you do not set any <font SIZE="-1">FALLBACK</font> value when using <font SIZE="-1">OVERLOAD,</font> it defaults to <font SIZE="-1">UNDEF.</font> <font SIZE="-1">FALLBACK</font> is not used except when one or more functions using <font SIZE="-1">OVERLOAD</font> have been defined. Please see &#8220;fallback&#8221; in overload for more details.</p>
<h3>The <font SIZE="-1">INTERFACE:</font> Keyword</h3>
<p> This keyword declares the current <font SIZE="-1">XSUB</font> as a keeper of the given calling signature. If some text follows this keyword, it is considered as a list of functions which have this signature, and should be attached to the current <font SIZE="-1">XSUB.</font> </p>
<p> For example, if you have 4 C functions <code>multiply()</code>, <code>divide()</code>, <code>add()</code>, <code>subtract()</code> all having the signature: </p>
<pre>
    symbolic f(symbolic, symbolic);
</pre>
<p> you can make them all to use the same <font SIZE="-1">XSUB</font> using this: </p>
<pre>
    symbolic
    interface_s_ss(arg1, arg2)
        symbolic        arg1
        symbolic        arg2
    INTERFACE:
        multiply divide
        add subtract
</pre>
<p> (This is the complete <font SIZE="-1">XSUB</font> code for 4 Perl functions!) Four generated Perl function share names with corresponding C functions. </p>
<p> The advantage of this approach comparing to <font SIZE="-1">ALIAS:</font> keyword is that there is no need to code a switch statement, each Perl function (which shares the same <font SIZE="-1">XSUB</font>) knows which C function it should call. Additionally, one can attach an extra function <code>remainder()</code> at runtime by using </p>
<p>CV *mycv = newXSproto(&#8220;Symbolic::remainder&#8221;,<br />
                      XS_Symbolic_interface_s_ss, __FILE__, &#8220;$$&#8221;);<br />
XSINTERFACE_FUNC_SET(mycv, remainder);</p>
<p> say, from another <font SIZE="-1">XSUB.</font> (This example supposes that there was no <font SIZE="-1">INTERFACE_MACRO:</font> section, otherwise one needs to use something else instead of <tt>&quot;XSINTERFACE_FUNC_SET&quot;</tt>, see the next section.)</p>
<h3>The <font SIZE="-1">INTERFACE_MACRO:</font> Keyword</h3>
<p> This keyword allows one to define an <font SIZE="-1">INTERFACE</font> using a different way to extract a function pointer from an <font SIZE="-1">XSUB.</font> The text which follows this keyword should give the name of macros which would extract/set a function pointer. The extractor macro is given return type, <tt>&quot;CV*&quot;</tt>, and <tt>&quot;XSANY.any_dptr&quot;</tt> for this <tt>&quot;CV*&quot;</tt>. The setter macro is given cv, and the function pointer. </p>
<p> The default value is <tt>&quot;XSINTERFACE_FUNC&quot;</tt> and <tt>&quot;XSINTERFACE_FUNC_SET&quot;</tt>. An <font SIZE="-1">INTERFACE</font> keyword with an empty list of functions can be omitted if <font SIZE="-1">INTERFACE_MACRO</font> keyword is used. </p>
<p> Suppose that in the previous example functions pointers for <code>multiply()</code>, <code>divide()</code>, <code>add()</code>, <code>subtract()</code> are kept in a global C array <tt>&quot;fp[]&quot;</tt> with offsets being <tt>&quot;multiply_off&quot;</tt>, <tt>&quot;divide_off&quot;</tt>, <tt>&quot;add_off&quot;</tt>, <tt>&quot;subtract_off&quot;</tt>. Then one can use </p>
<p>#define XSINTERFACE_FUNC_BYOFFSET(ret, cv, f) \<br />
    ((XSINTERFACE_CVT_ANON(ret))fp[CvXSUBANY(cv).any_i32])<br />
#define XSINTERFACE_FUNC_BYOFFSET_set(cv, f) \<br />
    CvXSUBANY(cv).any_i32 = CAT2(f, _off)</p>
<p> in C section, </p>
<pre>
    symbolic
    interface_s_ss(arg1, arg2)
        symbolic        arg1
        symbolic        arg2
      INTERFACE_MACRO:
        XSINTERFACE_FUNC_BYOFFSET
        XSINTERFACE_FUNC_BYOFFSET_set
      INTERFACE:
        multiply divide
        add subtract
</pre>
<p> in <font SIZE="-1">XSUB</font> section.</p>
<h3>The <font SIZE="-1">INCLUDE:</font> Keyword</h3>
<p> This keyword can be used to pull other files into the <font SIZE="-1">XS</font> module. The other files may have <font SIZE="-1">XS</font> code. <font SIZE="-1">INCLUDE:</font> can also be used to run a command to generate the <font SIZE="-1">XS</font> code to be pulled into the module. </p>
<p> The file <i>Rpcb1.xsh</i> contains our <tt>&quot;rpcb_gettime()&quot;</tt> function: </p>
<pre>
    bool_t
    rpcb_gettime(host,timep)
          char *host
          time_t &amp;timep
        OUTPUT:
          timep
</pre>
<p> The <font SIZE="-1">XS</font> module can use <font SIZE="-1">INCLUDE:</font> to pull that file into it. </p>
<pre>
    INCLUDE: Rpcb1.xsh
</pre>
<p> If the parameters to the <font SIZE="-1">INCLUDE:</font> keyword are followed by a pipe (<tt>&quot;|&quot;</tt>) then the compiler will interpret the parameters as a command. This feature is mildly deprecated in favour of the <tt>&quot;INCLUDE_COMMAND:&quot;</tt> directive, as documented below. </p>
<pre>
    INCLUDE: cat Rpcb1.xsh |
</pre>
<p> Do not use this to run perl: <tt>&quot;INCLUDE: perl |&quot;</tt> will run the perl that happens to be the first in your path and not necessarily the same perl that is used to run <tt>&quot;xsubpp&quot;</tt>. See &#8220;The <font SIZE="-1">INCLUDE_COMMAND:</font> Keyword&#8221;.</p>
<h3>The <font SIZE="-1">INCLUDE_COMMAND:</font> Keyword</h3>
<p> Runs the supplied command and includes its output into the current <font SIZE="-1">XS</font> document. <tt>&quot;INCLUDE_COMMAND&quot;</tt> assigns special meaning to the <tt>$^X</tt> token in that it runs the same perl interpreter that is running <tt>&quot;xsubpp&quot;</tt>: </p>
<pre>
    INCLUDE_COMMAND: cat Rpcb1.xsh
    INCLUDE_COMMAND: $^X -e ...
</pre>
<h3>The <font SIZE="-1">CASE:</font> Keyword</h3>
<p> The <font SIZE="-1">CASE:</font> keyword allows an <font SIZE="-1">XSUB</font> to have multiple distinct parts with each part acting as a virtual <font SIZE="-1">XSUB.</font> <font SIZE="-1">CASE:</font> is greedy and if it is used then all other <font SIZE="-1">XS</font> keywords must be contained within a <font SIZE="-1">CASE:.</font> This means nothing may precede the first <font SIZE="-1">CASE:</font> in the <font SIZE="-1">XSUB</font> and anything following the last <font SIZE="-1">CASE:</font> is included in that case. </p>
<p> A <font SIZE="-1">CASE:</font> might switch via a parameter of the <font SIZE="-1">XSUB,</font> via the <tt>&quot;ix&quot;</tt> <font SIZE="-1">ALIAS:</font> variable (see &#8220;The <font SIZE="-1">ALIAS:</font> Keyword&#8221;), or maybe via the <tt>&quot;items&quot;</tt> variable (see &#8220;Variable-length Parameter Lists&#8221;). The last <font SIZE="-1">CASE:</font> becomes the <code>default</code> case if it is not associated with a conditional. The following example shows <font SIZE="-1">CASE</font> switched via <tt>&quot;ix&quot;</tt> with a function <tt>&quot;rpcb_gettime()&quot;</tt> having an alias <tt>&quot;x_gettime()&quot;</tt>. When the function is called as <tt>&quot;rpcb_gettime()&quot;</tt> its parameters are the usual <tt>&quot;(char *host, time_t *timep)&quot;</tt>, but when the function is called as <tt>&quot;x_gettime()&quot;</tt> its parameters are reversed, <tt>&quot;(time_t *timep, char *host)&quot;</tt>. </p>
<p>long<br />
        rpcb_gettime(a, b)<br />
            CASE : ix<br />
                   == 1 ALIAS : x_gettime = 1 INPUT :<br />
#&#8217;a&#8217; is timep, &#8216;b&#8217; is host<br />
    char *b<br />
    time_t a = NO_INIT CODE : RETVAL = rpcb_gettime(b, &amp;a);<br />
OUTPUT : a<br />
             RETVAL<br />
                 CASE :<br />
#&#8217;a&#8217; is host, &#8216;b&#8217; is timep<br />
    char *a<br />
        time_t &amp;b = NO_INIT<br />
            OUTPUT : b<br />
                         RETVAL</p>
<p> That function can be called with either of the following statements. Note the different argument lists. </p>
<p>$status = rpcb_gettime($host, $timep);<br />
$status = x_gettime($timep, $host);</p>
<h3>The <font SIZE="-1">EXPORT_XSUB_SYMBOLS:</font> Keyword</h3>
<p> The <font SIZE="-1">EXPORT_XSUB_SYMBOLS:</font> keyword is likely something you will never need. In perl versions earlier than 5.16.0, this keyword does nothing. Starting with 5.16, <font SIZE="-1">XSUB</font> symbols are no longer exported by default. That is, they are <tt>&quot;static&quot;</tt> functions. If you include </p>
<pre>
  EXPORT_XSUB_SYMBOLS: ENABLE
</pre>
<p> in your <font SIZE="-1">XS</font> code, the XSUBs following this line will not be declared <tt>&quot;static&quot;</tt>. You can later disable this with </p>
<pre>
  EXPORT_XSUB_SYMBOLS: DISABLE
</pre>
<p> which, again, is the default that you should probably never change. You cannot use this keyword on versions of perl before 5.16 to make XSUBs <tt>&quot;static&quot;</tt>.</p>
<h3>The &amp; Unary Operator</h3>
<p> The <tt>&quot;&amp;&quot;</tt> unary operator in the <font SIZE="-1">INPUT:</font> section is used to tell <code>xsubpp</code> that it should convert a Perl value to/from C using the C type to the left of <tt>&quot;&amp;&quot;</tt>, but provide a pointer to this value when the C function is called. </p>
<p> This is useful to avoid a <font SIZE="-1">CODE:</font> block for a C function which takes a parameter by reference. Typically, the parameter should be not a pointer type (an <tt>&quot;int&quot;</tt> or <tt>&quot;long&quot;</tt> but not an <tt>&quot;int*&quot;</tt> or <tt>&quot;long*&quot;</tt>). </p>
<p> The following <font SIZE="-1">XSUB</font> will generate incorrect C code. The <code>xsubpp</code> compiler will turn this into code which calls <tt>&quot;rpcb_gettime()&quot;</tt> with parameters <tt>&quot;(char *host, time_t timep)&quot;</tt>, but the real <tt>&quot;rpcb_gettime()&quot;</tt> wants the <tt>&quot;timep&quot;</tt> parameter to be of type <tt>&quot;time_t*&quot;</tt> rather than <tt>&quot;time_t&quot;</tt>. </p>
<pre>
    bool_t
    rpcb_gettime(host,timep)
          char *host
          time_t timep
        OUTPUT:
          timep
</pre>
<p> That problem is corrected by using the <tt>&quot;&amp;&quot;</tt> operator. The <code>xsubpp</code> compiler will now turn this into code which calls <tt>&quot;rpcb_gettime()&quot;</tt> correctly with parameters <tt>&quot;(char *host, time_t *timep)&quot;</tt>. It does this by carrying the <tt>&quot;&amp;&quot;</tt> through, so the function call looks like <tt>&quot;rpcb_gettime(host, &amp;timep)&quot;</tt>. </p>
<pre>
    bool_t
    rpcb_gettime(host,timep)
          char *host
          time_t &amp;timep
        OUTPUT:
          timep
</pre>
<h3>Inserting <font SIZE="-1">POD,</font> Comments and C Preprocessor Directives</h3>
<p> C preprocessor directives are allowed within <font SIZE="-1">BOOT:, PREINIT: INIT:, CODE:, PPCODE:, POSTCALL:,</font> and <font SIZE="-1">CLEANUP:</font> blocks, as well as outside the functions. Comments are allowed anywhere after the <font SIZE="-1">MODULE</font> keyword. The compiler will pass the preprocessor directives through untouched and will remove the commented lines. <font SIZE="-1">POD</font> documentation is allowed at any point, both in the C and <font SIZE="-1">XS</font> language sections. <font SIZE="-1">POD</font> must be terminated with a <tt>&quot;=cut&quot;</tt> command; <tt>&quot;xsubpp&quot;</tt> will exit with an error if it does not. It is very unlikely that human generated C code will be mistaken for <font SIZE="-1">POD,</font> as most indenting styles result in whitespace in front of any line starting with <tt>&quot;=&quot;</tt>. Machine generated <font SIZE="-1">XS</font> files may fall into this trap unless care is taken to ensure that a space breaks the sequence &#8220;
=&#8221;. </p>
<p> Comments can be added to XSUBs by placing a <tt>&quot;#&quot;</tt> as the first non-whitespace of a line. Care should be taken to avoid making the comment look like a C preprocessor directive, lest it be interpreted as such. The simplest way to prevent this is to put whitespace in front of the <tt>&quot;#&quot;</tt>. </p>
<p> If you use preprocessor directives to choose one of two versions of a function, use </p>
<p>#if&#8230; version1<br />
#else /* &#8230; version2  */<br />
#endif</p>
<p> and not </p>
<p>#if&#8230; version1<br />
#endif<br />
#if&#8230; version2<br />
#endif</p>
<p> because otherwise <code>xsubpp</code> will believe that you made a duplicate definition of the function. Also, put a blank line before the #else/#endif so it will not be seen as part of the function body.</p>
<h3>Using <font SIZE="-1">XS</font> With C<font SIZE="-2">++</font></h3>
<p> If an <font SIZE="-1">XSUB</font> name contains <tt>&quot;::&quot;</tt>, it is considered to be a C<font SIZE="-2">++</font> method. The generated Perl function will assume that its first argument is an object pointer. The object pointer will be stored in a variable called <font SIZE="-1">THIS.</font> The object should have been created by C<font SIZE="-2">++</font> with the <code>new()</code> function and should be blessed by Perl with the <code>sv_setref_pv()</code> macro. The blessing of the object by Perl can be handled by a typemap. An example typemap is shown at the end of this section. </p>
<p> If the return type of the <font SIZE="-1">XSUB</font> includes <tt>&quot;static&quot;</tt>, the method is considered to be a static method. It will call the C<font SIZE="-2">++</font> function using the <code>class::method()</code> syntax. If the method is not static the function will be called using the <font SIZE="-1">THIS-</font>&gt;<code>method()</code> syntax. </p>
<p> The next examples will use the following C<font SIZE="-2">++</font> class. </p>
<p>class color<br />
{<br />
  public:<br />
    color();<br />
    ~color();<br />
    int blue();<br />
    void set_blue(int);</p>
<p>  private:<br />
    int c_blue;<br />
};</p>
<p> The XSUBs for the <code>blue()</code> and <code>set_blue()</code> methods are defined with the class name but the parameter for the object (<font SIZE="-1">THIS,</font> or &#8220;self&#8221;) is implicit and is not listed. </p>
<pre>
     int
     color::blue()
     void
     color::set_blue( val )
          int val
</pre>
<p> Both Perl functions will expect an object as the first parameter. In the generated C<font SIZE="-2">++</font> code the object is called <tt>&quot;THIS&quot;</tt>, and the method call will be performed on this object. So in the C<font SIZE="-2">++</font> code the <code>blue()</code> and <code>set_blue()</code> methods will be called as this: </p>
<p>RETVAL = THIS-&gt;blue();<br />
THIS-&gt;set_blue(val);</p>
<p> You could also write a single get/set method using an optional argument: </p>
<p>int<br />
    color::blue(val = NO_INIT) int val<br />
    PROTOTYPE $;<br />
$<br />
    CODE : if (items &gt; 1)<br />
               THIS-&gt;set_blue(val);<br />
RETVAL = THIS-&gt;blue();<br />
OUTPUT : RETVAL</p>
<p> If the function&#8217;s name is <font SIZE="-1"><code>DESTROY</code></font> then the C<font SIZE="-2">++</font> <tt>&quot;delete&quot;</tt> function will be called and <tt>&quot;THIS&quot;</tt> will be given as its parameter. The generated C<font SIZE="-2">++</font> code for </p>
<pre>
     void
     color::DESTROY()
</pre>
<p> will look like this: </p>
<pre>
     color *THIS = ...;  // Initialized as in typemap
     delete THIS;
</pre>
<p> If the function&#8217;s name is <code>new</code> then the C<font SIZE="-2">++</font> <tt>&quot;new&quot;</tt> function will be called to create a dynamic C<font SIZE="-2">++</font> object. The <font SIZE="-1">XSUB</font> will expect the class name, which will be kept in a variable called <tt>&quot;CLASS&quot;</tt>, to be given as the first argument. </p>
<pre>
     color *
     color::new()
</pre>
<p> The generated C<font SIZE="-2">++</font> code will call <tt>&quot;new&quot;</tt>. </p>
<pre>
     RETVAL = new color();
</pre>
<p> The following is an example of a typemap that could be used for this C<font SIZE="-2">++</font> example. </p>
<p>TYPEMAP<br />
color *O_OBJECT<br />
    OUTPUT<br />
#The Perl object is blessed into &#8216;CLASS&#8217;, which should be a<br />
#char *having the name of the package for the blessing.<br />
        O_OBJECT<br />
            sv_setref_pv($arg, CLASS, (void *)$var);<br />
INPUT<br />
O_OBJECT<br />
if (sv_isobject($arg) &amp;&amp; (SvTYPE(SvRV($arg)) == SVt_PVMG))<br />
    $var = ($type)SvIV((SV *)SvRV($arg));<br />
else {<br />
    warn(&#8220;${Package}::$func_name() &#8212; &#8220;.&#8221;$var is not a blessed SV reference&#8221;);<br />
    XSRETURN_UNDEF;<br />
}</p>
<h3>Interface Strategy</h3>
<p> When designing an interface between Perl and a C library a straight translation from C to <font SIZE="-1">XS</font> (such as created by <tt>&quot;h2xs -x&quot;</tt>) is often sufficient. However, sometimes the interface will look very C-like and occasionally nonintuitive, especially when the C function modifies one of its parameters, or returns failure inband (as in &#8220;negative return values mean failure&#8221;). In cases where the programmer wishes to create a more Perl-like interface the following strategy may help to identify the more critical parts of the interface. </p>
<p> Identify the C functions with input/output or output parameters. The XSUBs for these functions may be able to return lists to Perl. </p>
<p> Identify the C functions which use some inband info as an indication of failure. They may be candidates to return undef or an empty list in case of failure. If the failure may be detected without a call to the C function, you may want to use an <font SIZE="-1">INIT:</font> section to report the failure. For failures detectable after the C function returns one may want to use a <font SIZE="-1">POSTCALL:</font> section to process the failure. In more complicated cases use <font SIZE="-1">CODE:</font> or <font SIZE="-1">PPCODE:</font> sections. </p>
<p> If many functions use the same failure indication based on the return value, you may want to create a special typedef to handle this situation. Put </p>
<pre>
  typedef int negative_is_failure;
</pre>
<p> near the beginning of <font SIZE="-1">XS</font> file, and create an <font SIZE="-1">OUTPUT</font> typemap entry for <tt>&quot;negative_is_failure&quot;</tt> which converts negative values to <tt>&quot;undef&quot;</tt>, or maybe <code>croak()</code>s. After this the return value of type <tt>&quot;negative_is_failure&quot;</tt> will create more Perl-like interface. </p>
<p> Identify which values are used by only the C and <font SIZE="-1">XSUB</font> functions themselves, say, when a parameter to a function should be a contents of a global variable. If Perl does not need to access the contents of the value then it may not be necessary to provide a translation for that value from C to Perl. </p>
<p> Identify the pointers in the C function parameter lists and return values. Some pointers may be used to implement input/output or output parameters, they can be handled in <font SIZE="-1">XS</font> with the <tt>&quot;&amp;&quot;</tt> unary operator, and, possibly, using the <font SIZE="-1">NO_INIT</font> keyword. Some others will require handling of types like <tt>&quot;int *&quot;</tt>, and one needs to decide what a useful Perl translation will do in such a case. When the semantic is clear, it is advisable to put the translation into a typemap file. </p>
<p> Identify the structures used by the C functions. In many cases it may be helpful to use the T_PTROBJ typemap for these structures so they can be manipulated by Perl as blessed objects. (This is handled automatically by <tt>&quot;h2xs -x&quot;</tt>.) </p>
<p> If the same C type is used in several different contexts which require different translations, <tt>&quot;typedef&quot;</tt> several new types mapped to this C type, and create separate <i>typemap</i> entries for these new types. Use these types in declarations of return type and parameters to XSUBs.</p>
<h3>Perl Objects And C Structures</h3>
<p> When dealing with C structures one should select either <code>T_PTROBJ</code> or <code>T_PTRREF</code> for the <font SIZE="-1">XS</font> type. Both types are designed to handle pointers to complex objects. The T_PTRREF type will allow the Perl object to be unblessed while the T_PTROBJ type requires that the object be blessed. By using T_PTROBJ one can achieve a form of type-checking because the <font SIZE="-1">XSUB</font> will attempt to verify that the Perl object is of the expected type. </p>
<p> The following <font SIZE="-1">XS</font> code shows the <code>getnetconfigent()</code> function which is used with <font SIZE="-1">ONC+ TIRPC.</font> The <code>getnetconfigent()</code> function will return a pointer to a C structure and has the C prototype shown below. The example will demonstrate how the C pointer will become a Perl reference. Perl will consider this reference to be a pointer to a blessed object and will attempt to call a destructor for the object. A destructor will be provided in the <font SIZE="-1">XS</font> source to free the memory used by <code>getnetconfigent()</code>. Destructors in <font SIZE="-1">XS</font> can be created by specifying an <font SIZE="-1">XSUB</font> function whose name ends with the word <font SIZE="-1"><code>DESTROY</code></font>. <font SIZE="-1">XS</font> destructors can be used to free memory which may have been malloc&#8217;d by another <font SIZE="-1">XSUB.</font> </p>
<p>struct netconfig *getnetconfigent(const char *netid);</p>
<p> A <tt>&quot;typedef&quot;</tt> will be created for <tt>&quot;struct netconfig&quot;</tt>. The Perl object will be blessed in a class matching the name of the C type, with the tag <tt>&quot;Ptr&quot;</tt> appended, and the name should not have embedded spaces if it will be a Perl package name. The destructor will be placed in a class corresponding to the class of the object and the <font SIZE="-1">PREFIX</font> keyword will be used to trim the name to the word <font SIZE="-1">DESTROY</font> as Perl will expect. </p>
<p>typedef struct netconfig Netconfig;<br />
MODULE = RPC PACKAGE = RPC<br />
                           Netconfig *<br />
                       getnetconfigent(netid)<br />
char *netid<br />
    MODULE = RPC PACKAGE = NetconfigPtr PREFIX = rpcb_ void<br />
                                                     rpcb_DESTROY(netconf)<br />
                                                         Netconfig *<br />
                                                 netconf<br />
                                                     CODE : printf(&#8220;Now in NetconfigPtr::DESTROY
&#8221;);<br />
free(netconf);</p>
<p> This example requires the following typemap entry. Consult perlxstypemap for more information about adding new typemaps for an extension. </p>
<pre>
     TYPEMAP
     Netconfig *  T_PTROBJ
</pre>
<p> This example will be used with the following Perl statements. </p>
<p>use RPC;<br />
$netconf = getnetconfigent(&#8220;udp&#8221;);</p>
<p> When Perl destroys the object referenced by <tt>$netconf</tt> it will send the object to the supplied <font SIZE="-1">XSUB DESTROY</font> function. Perl cannot determine, and does not care, that this object is a C struct and not a Perl object. In this sense, there is no difference between the object created by the <code>getnetconfigent()</code> <font SIZE="-1">XSUB</font> and an object created by a normal Perl subroutine.</p>
<h3>Safely Storing Static Data in <font SIZE="-1">XS</font></h3>
<p> Starting with Perl 5.8, a macro framework has been defined to allow static data to be safely stored in <font SIZE="-1">XS</font> modules that will be accessed from a multi-threaded Perl. </p>
<p> Although primarily designed for use with multi-threaded Perl, the macros have been designed so that they will work with non-threaded Perl as well. </p>
<p> It is therefore strongly recommended that these macros be used by all <font SIZE="-1">XS</font> modules that make use of static data. </p>
<p> The easiest way to get a template set of macros to use is by specifying the <tt>&quot;-g&quot;</tt> (<tt>&quot;--global&quot;</tt>) option with h2xs (see h2xs). </p>
<p> Below is an example module that makes use of the macros. </p>
<p>#define PERL_NO_GET_CONTEXT<br />
#include &#8220;EXTERN.h&#8221;<br />
#include &#8220;XSUB.h&#8221;<br />
#include &#8220;perl.h&#8221;<br />
/* Global Data */<br />
#define MY_CXT_KEY &#8220;BlindMice::_guts&#8221; XS_VERSION<br />
typedef struct {<br />
    int count;<br />
    char name[3][100];<br />
} my_cxt_t;<br />
START_MY_CXT<br />
MODULE = BlindMice PACKAGE = BlindMice<br />
    BOOT:<br />
{<br />
    MY_CXT_INIT;<br />
    MY_CXT.count = 0;<br />
    strcpy(MY_CXT.name[0], &#8220;None&#8221;);<br />
    strcpy(MY_CXT.name[1], &#8220;None&#8221;);<br />
    strcpy(MY_CXT.name[2], &#8220;None&#8221;);<br />
}<br />
int newMouse(char *name)<br />
    PREINIT : dMY_CXT;<br />
CODE : if (MY_CXT.count &gt;= 3)<br />
{<br />
    warn(&#8220;Already have 3 blind mice&#8221;);<br />
    RETVAL = 0;<br />
}<br />
else<br />
{<br />
    RETVAL = ++MY_CXT.count;<br />
    strcpy(MY_CXT.name[MY_CXT.count &#8211; 1], name);<br />
}<br />
OUTPUT : RETVAL char *<br />
         get_mouse_name(index)<br />
int index<br />
    PREINIT : dMY_CXT;<br />
CODE : if (index &gt; MY_CXT.count)<br />
           croak(&#8220;There are only 3 blind mice.&#8221;);<br />
else RETVAL = MY_CXT.name[index &#8211; 1];<br />
OUTPUT : RETVAL void<br />
         CLONE(&#8230;)<br />
             CODE : MY_CXT_CLONE;</p>
<p> <i></i><font SIZE="-1"><i>MY_CXT REFERENCE</i></font><i></i></p>
<dl>
<dt><font SIZE="-1">MY_CXT_KEY</font></p>
<dd> This macro is used to define a unique key to refer to the static data for an <font SIZE="-1">XS</font> module. The suggested naming scheme, as used by h2xs, is to use a string that consists of the module name, the string &#8220;::_guts&#8221; and the module version number. </p>
<p>#define MY_CXT_KEY &#8220;MyModule::_guts&#8221; XS_VERSION</p>
<dt>typedef my_cxt_t</p>
<dd> This struct typedef <i>must</i> always be called <tt>&quot;my_cxt_t&quot;</tt>. The other <tt>&quot;CXT*&quot;</tt> macros assume the existence of the <tt>&quot;my_cxt_t&quot;</tt> typedef name. </p>
<p> Declare a typedef named <tt>&quot;my_cxt_t&quot;</tt> that is a structure that contains all the data that needs to be interpreter-local. </p>
<p>typedef struct {<br />
    int some_value;<br />
} my_cxt_t;</p>
<dt><font SIZE="-1">START_MY_CXT</font></p>
<dd> Always place the <font SIZE="-1">START_MY_CXT</font> macro directly after the declaration of <tt>&quot;my_cxt_t&quot;</tt>.</p>
<dt><font SIZE="-1">MY_CXT_INIT</font></p>
<dd> The <font SIZE="-1">MY_CXT_INIT</font> macro initializes storage for the <tt>&quot;my_cxt_t&quot;</tt> struct. </p>
<p> It <i>must</i> be called exactly once, typically in a <font SIZE="-1">BOOT:</font> section. If you are maintaining multiple interpreters, it should be called once in each interpreter instance, except for interpreters cloned from existing ones. (But see &#8220;<font SIZE="-1">MY_CXT_CLONE&#8221;</font> below.)</p>
<dt>dMY_CXT</p>
<dd> Use the dMY_CXT macro (a declaration) in all the functions that access <font SIZE="-1">MY_CXT.</font></p>
<dt><font SIZE="-1">MY_CXT</font></p>
<dd> Use the <font SIZE="-1">MY_CXT</font> macro to access members of the <tt>&quot;my_cxt_t&quot;</tt> struct. For example, if <tt>&quot;my_cxt_t&quot;</tt> is </p>
<p>typedef struct {<br />
    int index;<br />
} my_cxt_t;</p>
<p> then use this to access the <tt>&quot;index&quot;</tt> member </p>
<pre>
    dMY_CXT;
    MY_CXT.index = 2;
</pre>
<dt>aMY_CXT/pMY_CXT</p>
<dd> <tt>&quot;dMY_CXT&quot;</tt> may be quite expensive to calculate, and to avoid the overhead of invoking it in each function it is possible to pass the declaration onto other functions using the <tt>&quot;aMY_CXT&quot;</tt>/<tt>&quot;pMY_CXT&quot;</tt> macros, eg </p>
<p>void sub1()<br />
{<br />
    dMY_CXT;<br />
    MY_CXT.index = 1;<br />
    sub2(aMY_CXT);<br />
}<br />
void sub2(pMY_CXT)<br />
{<br />
    MY_CXT.index = 2;<br />
}</p>
<p> Analogously to <tt>&quot;pTHX&quot;</tt>, there are equivalent forms for when the macro is the first or last in multiple arguments, where an underscore represents a comma, i.e. <tt>&quot;_aMY_CXT&quot;</tt>, <tt>&quot;aMY_CXT_&quot;</tt>, <tt>&quot;_pMY_CXT&quot;</tt> and <tt>&quot;pMY_CXT_&quot;</tt>.</p>
<dt><font SIZE="-1">MY_CXT_CLONE</font></p>
<dd> By default, when a new interpreter is created as a copy of an existing one (eg via <tt>&quot;threads-&gt;create()&quot;</tt>), both interpreters share the same physical my_cxt_t structure. Calling <tt>&quot;MY_CXT_CLONE&quot;</tt> (typically via the package&#8217;s <tt>&quot;CLONE()&quot;</tt> function), causes a byte-for-byte copy of the structure to be taken, and any future dMY_CXT will cause the copy to be accessed instead.</p>
<dt><font SIZE="-1">MY_CXT_INIT_INTERP</font>(my_perl)</p>
<dd>
<dt>dMY_CXT_INTERP(my_perl)</p>
<dd> These are versions of the macros which take an explicit interpreter as an argument.</dl>
<p> Note that these macros will only work together within the <i>same</i> source file; that is, a dMY_CTX in one source file will access a different structure than a dMY_CTX in another source file.</p>
<h3>Thread-aware system interfaces</h3>
<p> Starting from Perl 5.8, in C/C<font SIZE="-2">++</font> level Perl knows how to wrap system/library interfaces that have thread-aware versions (e.g. <code>getpwent_r()</code>) into frontend macros (e.g. <code>getpwent()</code>) that correctly handle the multithreaded interaction with the Perl interpreter. This will happen transparently, the only thing you need to do is to instantiate a Perl interpreter. </p>
<p> This wrapping happens always when compiling Perl core source (<font SIZE="-1">PERL_CORE</font> is defined) or the Perl core extensions (<font SIZE="-1">PERL_EXT</font> is defined). When compiling <font SIZE="-1">XS</font> code outside of the Perl core, the wrapping does not take place before Perl 5.28. Starting in that release you can </p>
<p>#define PERL_REENTRANT</p>
<p> in your code to enable the wrapping. It is advisable to do so if you are using such functions, as intermixing the <tt>&quot;_r&quot;</tt>-forms (as Perl compiled for multithreaded operation will do) and the <tt>&quot;_r&quot;</tt>-less forms is neither well-defined (inconsistent results, data corruption, or even crashes become more likely), nor is it very portable. Unfortunately, not all systems have all the <tt>&quot;_r&quot;</tt> forms, but using this <tt>&quot;#define&quot;</tt> gives you whatever protection that Perl is aware is available on each system.</p>
<h2>EXAMPLES</h2>
<p> File <tt>&quot;RPC.xs&quot;</tt>: Interface to some <font SIZE="-1">ONC+ RPC</font> bind library functions. </p>
<p>#define PERL_NO_GET_CONTEXT<br />
#include &#8220;EXTERN.h&#8221;<br />
#include &#8220;XSUB.h&#8221;<br />
#include &#8220;perl.h&#8221;<br />
#include &lt;rpc/rpc.h&gt;<br />
typedef struct netconfig Netconfig;<br />
MODULE = RPC PACKAGE = RPC<br />
                           SV *<br />
                       rpcb_gettime(host = &#8220;localhost&#8221;) char * host PREINIT : time_t timep;<br />
CODE : ST(0) = sv_newmortal();<br />
if (rpcb_gettime(host, &amp;timep))<br />
    sv_setnv(ST(0), (double)timep);<br />
Netconfig *<br />
    getnetconfigent(netid = &#8220;udp&#8221;) char *netid<br />
    MODULE = RPC PACKAGE = NetconfigPtr PREFIX = rpcb_ void rpcb_DESTROY(netconf)<br />
                                                     Netconfig<br />
                                                 * netconf<br />
                                                 CODE : printf(&#8220;NetconfigPtr::DESTROY
&#8221;);<br />
free(netconf);</p>
<p> File <tt>&quot;typemap&quot;</tt>: Custom typemap for <font SIZE="-1">RPC</font>.xs. (cf. perlxstypemap) </p>
<pre>
     TYPEMAP
     Netconfig *  T_PTROBJ
</pre>
<p> File <tt>&quot;RPC.pm&quot;</tt>: Perl module for the <font SIZE="-1">RPC</font> extension. </p>
<p>package RPC;<br />
require Exporter;<br />
require DynaLoader;<br />
@ISA = qw(Exporter DynaLoader);<br />
@EXPORT = qw(rpcb_gettime getnetconfigent);<br />
bootstrap RPC;<br />
1;</p>
<p> File <tt>&quot;rpctest.pl&quot;</tt>: Perl test program for the <font SIZE="-1">RPC</font> extension. </p>
<p>use RPC;<br />
$netconf = getnetconfigent();<br />
$a = rpcb_gettime();<br />
print &#8220;time = $a
&#8221;;<br />
print &#8220;netconf = $netconf
&#8221;;<br />
$netconf = getnetconfigent(&#8220;tcp&#8221;);<br />
$a = rpcb_gettime(&#8220;poplar&#8221;);<br />
print &#8220;time = $a
&#8221;;<br />
print &#8220;netconf = $netconf
&#8221;;</p>
<h2>CAVEATS</h2>
<p> <font SIZE="-1">XS</font> code has full access to system calls including C library functions. It thus has the capability of interfering with things that the Perl core or other modules have set up, such as signal handlers or file handles. It could mess with the memory, or any number of harmful things. Don&#8217;t. </p>
<p> Some modules have an event loop, waiting for user-input. It is highly unlikely that two such modules would work adequately together in a single Perl application. </p>
<p> In general, the perl interpreter views itself as the center of the universe as far as the Perl program goes. <font SIZE="-1">XS</font> code is viewed as a help-mate, to accomplish things that perl doesn&#8217;t do, or doesn&#8217;t do fast enough, but always subservient to perl. The closer <font SIZE="-1">XS</font> code adheres to this model, the less likely conflicts will occur. </p>
<p> One area where there has been conflict is in regards to C locales. (See perllocale.) perl, with one exception and unless told otherwise, sets up the underlying locale the program is running in to the locale passed into it from the environment. This is an important difference from a generic C language program, where the underlying locale is the &#8220;C&#8221; locale unless the program changes it. As of v5.20, this underlying locale is completely hidden from pure Perl code outside the lexical scope of <tt>&quot;use locale&quot;</tt> except for a couple of function calls in the <font SIZE="-1">POSIX</font> module which of necessity use it. But the underlying locale, with that one exception is exposed to <font SIZE="-1">XS</font> code, affecting all C library routines whose behavior is locale-dependent. Your <font SIZE="-1">XS</font> code better not assume that the underlying locale is &#8220;C&#8221;. The exception is the <tt>&quot;LC_NUMERIC&quot;</tt> locale category, and the reason it is an exception is that experience has shown that it can be problematic for <font SIZE="-1">XS</font> code, whereas we have not had reports of problems with the other locale categories. And the reason for this one category being problematic is that the character used as a decimal point can vary. Many European languages use a comma, whereas English, and hence Perl are expecting a dot (U+002E: <font SIZE="-1">FULL STOP</font>). Many modules can handle only the radix character being a dot, and so perl attempts to make it so. Up through Perl v5.20, the attempt was merely to set <tt>&quot;LC_NUMERIC&quot;</tt> upon startup to the <tt>&quot;C&quot;</tt> locale. Any <code>setlocale()</code> otherwise would change it; this caused some failures. Therefore, starting in v5.22, perl tries to keep <tt>&quot;LC_NUMERIC&quot;</tt> always set to <tt>&quot;C&quot;</tt> for <font SIZE="-1">XS</font> code. </p>
<p> To summarize, here&#8217;s what to expect and how to handle locales in <font SIZE="-1">XS</font> code:</p>
<dl>
<dt>Non-locale-aware <font SIZE="-1">XS</font> code</p>
<dd> Keep in mind that even if you think your code is not locale-aware, it may call a library function that is. Hopefully the man page for such a function will indicate that dependency, but the documentation is imperfect. </p>
<p> The current locale is exposed to <font SIZE="-1">XS</font> code except possibly <tt>&quot;LC_NUMERIC&quot;</tt> (explained in the next paragraph). There have not been reports of problems with the other categories. Perl initializes things on start-up so that the current locale is the one which is indicated by the user&#8217;s environment in effect at that time. See &#8220;<font SIZE="-1">ENVIRONMENT&#8221;</font> in perllocale. </p>
<p> However, up through v5.20, Perl initialized things on start-up so that <tt>&quot;LC_NUMERIC&quot;</tt> was set to the &#8220;C&#8221; locale. But if any code anywhere changed it, it would stay changed. This means that your module can&#8217;t count on <tt>&quot;LC_NUMERIC&quot;</tt> being something in particular, and you can&#8217;t expect floating point numbers (including version strings) to have dots in them. If you don&#8217;t allow for a non-dot, your code could break if anyone anywhere changed the locale. For this reason, v5.22 changed the behavior so that Perl tries to keep <tt>&quot;LC_NUMERIC&quot;</tt> in the &#8220;C&#8221; locale except around the operations internally where it should be something else. Misbehaving <font SIZE="-1">XS</font> code will always be able to change the locale anyway, but the most common instance of this is checked for and handled.</p>
<dt>Locale-aware <font SIZE="-1">XS</font> code</p>
<dd> If the locale from the user&#8217;s environment is desired, there should be no need for <font SIZE="-1">XS</font> code to set the locale except for <tt>&quot;LC_NUMERIC&quot;</tt>, as perl has already set the others up. <font SIZE="-1">XS</font> code should avoid changing the locale, as it can adversely affect other, unrelated, code and may not be thread-safe. To minimize problems, the macros &#8220;<font SIZE="-1">STORE_LC_NUMERIC_SET_TO_NEEDED&#8221;</font> in perlapi, &#8220;<font SIZE="-1">STORE_LC_NUMERIC_FORCE_TO_UNDERLYING&#8221;</font> in perlapi, and &#8220;<font SIZE="-1">RESTORE_LC_NUMERIC&#8221;</font> in perlapi should be used to affect any needed change. </p>
<p> But, starting with Perl v5.28, locales are thread-safe on platforms that support this functionality. Windows has this starting with Visual Studio 2005. Many other modern platforms support the thread-safe <font SIZE="-1">POSIX 2008</font> functions. The C <tt>&quot;#define&quot;</tt> <tt>&quot;USE_THREAD_SAFE_LOCALE&quot;</tt> will be defined iff this build is using these. From Perl-space, the read-only variable <tt>&quot;${SAFE_LOCALES}&quot;</tt> is 1 if either the build is not threaded, or if <tt>&quot;USE_THREAD_SAFE_LOCALE&quot;</tt> is defined; otherwise it is 0. </p>
<p> The way this works under-the-hood is that every thread has a choice of using a locale specific to it (this is the Windows and <font SIZE="-1">POSIX 2008</font> functionality), or the global locale that is accessible to all threads (this is the functionality that has always been there). The implementations for Windows and <font SIZE="-1">POSIX</font> are completely different. On Windows, the runtime can be set up so that the standard <tt><a href="/docs/linux/man/3-setlocale/">setlocale</a>(3)</tt> function either only knows about the global locale or the locale for this thread. On <font SIZE="-1">POSIX,</font> <tt>&quot;setlocale&quot;</tt> always deals with the global locale, and other functions have been created to handle per-thread locales. Perl makes this transparent to perl-space code. It continues to use <tt>&quot;POSIX::setlocale()&quot;</tt>, and the interpreter translates that into the per-thread functions. </p>
<p> All other locale-senstive functions automatically use the per-thread locale, if that is turned on, and failing that, the global locale. Thus calls to <tt>&quot;setlocale&quot;</tt> are ineffective on <font SIZE="-1">POSIX</font> systems for the current thread if that thread is using a per-thread locale. If perl is compiled for single-thread operation, it does not use the per-thread functions, so <tt>&quot;setlocale&quot;</tt> does work as expected. </p>
<p> If you have loaded the <tt>&quot;POSIX&quot;</tt> module you can use the methods given in perlcall to call <tt>&quot;POSIX::setlocale&quot;</tt> to safely change or query the locale (on systems where it is safe to do so), or you can use the new 5.28 function &#8220;Perl_setlocale&#8221; in perlapi instead, which is a drop-in replacement for the system <tt><a href="/docs/linux/man/3-setlocale/">setlocale</a>(3)</tt>, and handles single-threaded and multi-threaded applications transparently. </p>
<p> There are some locale-related library calls that still aren&#8217;t thread-safe because they return data in a buffer global to all threads. In the past, these didn&#8217;t matter as locales weren&#8217;t thread-safe at all. But now you have to be aware of them in case your module is called in a multi-threaded application. The known ones are </p>
<p>asctime()<br />
    ctime()<br />
        gcvt()[POSIX .1 &#8211; 2001 only(function removed in POSIX .1 &#8211; 2008)] getdate()<br />
            wcrtomb() if its final argument is NULL<br />
    wcsrtombs() if its final argument is NULL<br />
    wcstombs()<br />
        wctomb()</p>
<p> Some of these shouldn&#8217;t really be called in a Perl application, and for others there are thread-safe versions of these already implemented: </p>
<pre>
 asctime_r()
 ctime_r()
 Perl_langinfo()
</pre>
<p> The <tt>&quot;_r&quot;</tt> forms are automatically used, starting in Perl 5.28, if you compile your code, with </p>
<pre><code>
#define PERL_REENTRANT
</code></pre>
<p> See also &#8220;Perl_langinfo&#8221; in perlapi. You can use the methods given in perlcall, to get the best available locale-safe versions of these </p>
<pre>
 POSIX::localeconv()
 POSIX::wcstombs()
 POSIX::wctomb()
</pre>
<p> And note, that some items returned by <tt>&quot;Localeconv&quot;</tt> are available through &#8220;Perl_langinfo&#8221; in perlapi. </p>
<p> The others shouldn&#8217;t be used in a threaded application. </p>
<p> Some modules may call a non-perl library that is locale-aware. This is fine as long as it doesn&#8217;t try to query or change the locale using the system <tt>&quot;setlocale&quot;</tt>. But if these do call the system <tt>&quot;setlocale&quot;</tt>, those calls may be ineffective. Instead, <tt>&quot;Perl_setlocale&quot;</tt> works in all circumstances. Plain setlocale is ineffective on multi-threaded <font SIZE="-1">POSIX 2008</font> systems. It operates only on the global locale, whereas each thread has its own locale, paying no attention to the global one. Since converting these non-Perl libraries to <tt>&quot;Perl_setlocale&quot;</tt> is out of the question, there is a new function in v5.28 <tt>&quot;switch_to_global_locale&quot;</tt> that will switch the thread it is called from so that any system <tt>&quot;setlocale&quot;</tt> calls will have their desired effect. The function <tt>&quot;sync_locale&quot;</tt> must be called before returning to perl. </p>
<p> This thread can change the locale all it wants and it won&#8217;t affect any other thread, except any that also have been switched to the global locale. This means that a multi-threaded application can have a single thread using an alien library without a problem; but no more than a single thread can be so-occupied. Bad results likely will happen. </p>
<p> In perls without multi-thread locale support, some alien libraries, such as <tt>&quot;Gtk&quot;</tt> change locales. This can cause problems for the Perl core and other modules. For these, before control is returned to perl, starting in v5.20.1, calling the function <code>sync_locale()</code> from <font SIZE="-1">XS</font> should be sufficient to avoid most of these problems. Prior to this, you need a pure Perl statement that does this: </p>
<pre>
 POSIX::setlocale(LC_ALL, POSIX::setlocale(LC_ALL));
</pre>
<p> or use the methods given in perlcall.</dl>
<h2>XS VERSION</h2>
<p> This document covers features supported by <tt>&quot;ExtUtils::ParseXS&quot;</tt> (also known as <tt>&quot;xsubpp&quot;</tt>) 3.13_01.</p>
<h2>AUTHOR</h2>
<p> Originally written by Dean Roehrich &lt;<i>roehrich [at] cray.com</i>&gt;. </p>
<p> Maintained since 1996 by The Perl Porters &lt;<i>perlbug [at] perl.org</i>&gt;. </p>
<h2>Index</h2>
<dt><a href="#lbCA">EXAMPLES</a></p>
<dd>
<dt><a href="#lbCB">CAVEATS</a></p>
<dd>
<dt><a href="#lbCC">XS VERSION</a></p>
<dd>
<dt><a href="#lbCD">AUTHOR</a></p>
<dd></dl>
