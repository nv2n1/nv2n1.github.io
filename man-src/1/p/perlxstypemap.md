---
title: "perlxstypemap(1)"
name: "perlxstypemap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlxstypemap/"
description: "perlxstypemap – Perl XS C/Perl type mapping"
---

<h2 class="name">NAME</h2>
<p> perlxstypemap &#8211; Perl XS C/Perl type mapping </p>
<h2>DESCRIPTION</h2>
<p> The more you think about interfacing between two languages, the more you&#8217;ll realize that the majority of programmer effort has to go into converting between the data structures that are native to either of the languages involved. This trumps other matter such as differing calling conventions because the problem space is so much greater. There are simply more ways to shove data into memory than there are ways to implement a function call. </p>
<p> Perl <font SIZE="-1">XS</font>&#8216; attempt at a solution to this is the concept of typemaps. At an abstract level, a Perl <font SIZE="-1">XS</font> typemap is nothing but a recipe for converting from a certain Perl data structure to a certain C data structure and vice versa. Since there can be C types that are sufficiently similar to one another to warrant converting with the same logic, <font SIZE="-1">XS</font> typemaps are represented by a unique identifier, henceforth called an <font SIZE="-1"><code>XS</code></font><code> type</code> in this document. You can then tell the <font SIZE="-1">XS</font> compiler that multiple C types are to be mapped with the same <font SIZE="-1">XS</font> typemap. </p>
<p> In your <font SIZE="-1">XS</font> code, when you define an argument with a C type or when you are using a <tt>&quot;CODE:&quot;</tt> and an <tt>&quot;OUTPUT:&quot;</tt> section together with a C return type of your <font SIZE="-1">XSUB,</font> it&#8217;ll be the typemapping mechanism that makes this easy.</p>
<h3>Anatomy of a typemap</h3>
<p> In more practical terms, the typemap is a collection of code fragments which are used by the <code>xsubpp</code> compiler to map C function parameters and values to Perl values. The typemap file may consist of three sections labelled <tt>&quot;TYPEMAP&quot;</tt>, <tt>&quot;INPUT&quot;</tt>, and <tt>&quot;OUTPUT&quot;</tt>. An unlabelled initial section is assumed to be a <tt>&quot;TYPEMAP&quot;</tt> section. The <font SIZE="-1">INPUT</font> section tells the compiler how to translate Perl values into variables of certain C types. The <font SIZE="-1">OUTPUT</font> section tells the compiler how to translate the values from certain C types into values Perl can understand. The <font SIZE="-1">TYPEMAP</font> section tells the compiler which of the <font SIZE="-1">INPUT</font> and <font SIZE="-1">OUTPUT</font> code fragments should be used to map a given C type to a Perl value. The section labels <tt>&quot;TYPEMAP&quot;</tt>, <tt>&quot;INPUT&quot;</tt>, or <tt>&quot;OUTPUT&quot;</tt> must begin in the first column on a line by themselves, and must be in uppercase. </p>
<p> Each type of section can appear an arbitrary number of times and does not have to appear at all. For example, a typemap may commonly lack <tt>&quot;INPUT&quot;</tt> and <tt>&quot;OUTPUT&quot;</tt> sections if all it needs to do is associate additional C types with core <font SIZE="-1">XS</font> types like T_PTROBJ. Lines that start with a hash <tt>&quot;#&quot;</tt> are considered comments and ignored in the <tt>&quot;TYPEMAP&quot;</tt> section, but are considered significant in <tt>&quot;INPUT&quot;</tt> and <tt>&quot;OUTPUT&quot;</tt>. Blank lines are generally ignored. </p>
<p> Traditionally, typemaps needed to be written to a separate file, conventionally called <tt>&quot;typemap&quot;</tt> in a <font SIZE="-1">CPAN</font> distribution. With ExtUtils::ParseXS (the <font SIZE="-1">XS</font> compiler) version 3.12 or better which comes with perl 5.16, typemaps can also be embedded directly into <font SIZE="-1">XS</font> code using a HERE-doc like syntax: </p>
<pre>
  TYPEMAP: &lt;&lt;HERE
  ...
  HERE
</pre>
<p> where <tt>&quot;HERE&quot;</tt> can be replaced by other identifiers like with normal Perl HERE-docs. All details below about the typemap textual format remain valid. </p>
<p> The <tt>&quot;TYPEMAP&quot;</tt> section should contain one pair of C type and <font SIZE="-1">XS</font> type per line as follows. An example from the core typemap file: </p>
<pre><code>
TYPEMAP
#all variants of char *is handled by the T_PV typemap
char *T_PV const char *T_PV unsigned char *T_PV...
</code></pre>
<p> The <tt>&quot;INPUT&quot;</tt> and <tt>&quot;OUTPUT&quot;</tt> sections have identical formats, that is, each unindented line starts a new in- or output map respectively. A new in- or output map must start with the name of the <font SIZE="-1">XS</font> type to map on a line by itself, followed by the code that implements it indented on the following lines. Example: </p>
<pre>
  INPUT
  T_PV
    $var = ($type)SvPV_nolen($arg)
  T_PTR
    $var = INT2PTR($type,SvIV($arg))
</pre>
<p> We&#8217;ll get to the meaning of those Perlish-looking variables in a little bit. </p>
<p> Finally, here&#8217;s an example of the full typemap file for mapping C strings of the <tt>&quot;char *&quot;</tt> type to Perl scalars/strings: </p>
<pre>
  TYPEMAP
  char *  T_PV
  INPUT
  T_PV
    $var = ($type)SvPV_nolen($arg)
  OUTPUT
  T_PV
    sv_setpv((SV*)$arg, $var);
</pre>
<p> Here&#8217;s a more complicated example: suppose that you wanted <tt>&quot;struct netconfig&quot;</tt> to be blessed into the class <tt>&quot;Net::Config&quot;</tt>. One way to do this is to use underscores (_) to separate package names, as follows: </p>
<pre>
  typedef struct netconfig * Net_Config;
</pre>
<p> And then provide a typemap entry <tt>&quot;T_PTROBJ_SPECIAL&quot;</tt> that maps underscores to double-colons (::), and declare <tt>&quot;Net_Config&quot;</tt> to be of that type: </p>
<p>TYPEMAP<br />
  Net_Config      T_PTROBJ_SPECIAL<br />
  INPUT<br />
  T_PTROBJ_SPECIAL<br />
    if (sv_derived_from($arg, \&#8221;${(my $ntt=$ntype)=~s/_/::/g;\$ntt}\&#8221;)){<br />
      IV tmp = SvIV((SV*)SvRV($arg));<br />
      $var = INT2PTR($type, tmp);<br />
  }<br />
    else<br />
      croak(\&#8221;$var is not of type ${(my $ntt=$ntype)=~s/_/::/g;\$ntt}\&#8221;)<br />
  OUTPUT<br />
  T_PTROBJ_SPECIAL<br />
    sv_setref_pv($arg, \&#8221;${(my $ntt=$ntype)=~s/_/::/g;\$ntt}\&#8221;,<br />
                 (void*)$var);</p>
<p> The <font SIZE="-1">INPUT</font> and <font SIZE="-1">OUTPUT</font> sections substitute underscores for double-colons on the fly, giving the desired effect. This example demonstrates some of the power and versatility of the typemap facility. </p>
<p> The <tt>&quot;INT2PTR&quot;</tt> macro (defined in perl.h) casts an integer to a pointer of a given type, taking care of the possible different size of integers and pointers. There are also <tt>&quot;PTR2IV&quot;</tt>, <tt>&quot;PTR2UV&quot;</tt>, <tt>&quot;PTR2NV&quot;</tt> macros, to map the other way, which may be useful in <font SIZE="-1">OUTPUT</font> sections.</p>
<h3>The Role of the typemap File in Your Distribution</h3>
<p> The default typemap in the <i>lib/ExtUtils</i> directory of the Perl source contains many useful types which can be used by Perl extensions. Some extensions define additional typemaps which they keep in their own directory. These additional typemaps may reference <font SIZE="-1">INPUT</font> and <font SIZE="-1">OUTPUT</font> maps in the main typemap. The <code>xsubpp</code> compiler will allow the extension&#8217;s own typemap to override any mappings which are in the default typemap. Instead of using an additional <i>typemap</i> file, typemaps may be embedded verbatim in <font SIZE="-1">XS</font> with a heredoc-like syntax. See the documentation on the <tt>&quot;TYPEMAP:&quot;</tt> <font SIZE="-1">XS</font> keyword. </p>
<p> For <font SIZE="-1">CPAN</font> distributions, you can assume that the <font SIZE="-1">XS</font> types defined by the perl core are already available. Additionally, the core typemap has default <font SIZE="-1">XS</font> types for a large number of C types. For example, if you simply return a <tt>&quot;char *&quot;</tt> from your <font SIZE="-1">XSUB,</font> the core typemap will have this C type associated with the T_PV <font SIZE="-1">XS</font> type. That means your C string will be copied into the <font SIZE="-1">PV</font> (pointer value) slot of a new scalar that will be returned from your <font SIZE="-1">XSUB</font> to Perl. </p>
<p> If you&#8217;re developing a <font SIZE="-1">CPAN</font> distribution using <font SIZE="-1">XS,</font> you may add your own file called <i>typemap</i> to the distribution. That file may contain typemaps that either map types that are specific to your code or that override the core typemap file&#8217;s mappings for common C types.</p>
<h3>Sharing typemaps Between <font SIZE="-1">CPAN</font> Distributions</h3>
<p> Starting with ExtUtils::ParseXS version 3.13_01 (comes with perl 5.16 and better), it is rather easy to share typemap code between multiple <font SIZE="-1">CPAN</font> distributions. The general idea is to share it as a module that offers a certain <font SIZE="-1">API</font> and have the dependent modules declare that as a built-time requirement and import the typemap into the <font SIZE="-1">XS.</font> An example of such a typemap-sharing module on <font SIZE="-1">CPAN</font> is <tt>&quot;ExtUtils::Typemaps::Basic&quot;</tt>. Two steps to getting that module&#8217;s typemaps available in your code:</p>
<dl>
<dt>&bull;</p>
<dd> Declare <tt>&quot;ExtUtils::Typemaps::Basic&quot;</tt> as a build-time dependency in <tt>&quot;Makefile.PL&quot;</tt> (use <tt>&quot;BUILD_REQUIRES&quot;</tt>), or in your <tt>&quot;Build.PL&quot;</tt> (use <tt>&quot;build_requires&quot;</tt>).</p>
<dt>&bull;</p>
<dd> Include the following line in the <font SIZE="-1">XS</font> section of your <font SIZE="-1">XS</font> file: (don&#8217;t break the line) </p>
<pre>
  INCLUDE_COMMAND: $^X -MExtUtils::Typemaps::Cmd
                   -e &quot;print embeddable_typemap(q{Basic})&quot;
</pre>
</dl>
<h3>Writing typemap Entries</h3>
<p> Each <font SIZE="-1">INPUT</font> or <font SIZE="-1">OUTPUT</font> typemap entry is a double-quoted Perl string that will be evaluated in the presence of certain variables to get the final C code for mapping a certain C type. </p>
<p> This means that you can embed Perl code in your typemap (C) code using constructs such as <tt>&quot;${ perl code that evaluates to scalar reference here }&quot;</tt>. A common use case is to generate error messages that refer to the true function name even when using the <font SIZE="-1">ALIAS XS</font> feature: </p>
<p>$<br />
{ $ALIAS ? \q[GvNAME(CvGV(cv))] : \qq[\&#8221;$pname\&#8221;] }</p>
<p> For many typemap examples, refer to the core typemap file that can be found in the perl source tree at <i>lib/ExtUtils/typemap</i>. </p>
<p> The Perl variables that are available for interpolation into typemaps are the following:</p>
<dl>
<dt>&bull;</p>
<dd> <i></i>$var<i></i> &#8211; the name of the input or output variable, eg. <font SIZE="-1">RETVAL</font> for return values.</p>
<dt>&bull;</p>
<dd> <i></i>$type<i></i> &#8211; the raw C type of the parameter, any <tt>&quot;:&quot;</tt> replaced with <tt>&quot;_&quot;</tt>. e.g. for a type of <tt>&quot;Foo::Bar&quot;</tt>, <i></i>$type<i></i> is <tt>&quot;Foo__Bar&quot;</tt></p>
<dt>&bull;</p>
<dd> <i></i>$ntype<i></i> &#8211; the supplied type with <tt>&quot;*&quot;</tt> replaced with <tt>&quot;Ptr&quot;</tt>. e.g. for a type of <tt>&quot;Foo*&quot;</tt>, <i></i>$ntype<i></i> is <tt>&quot;FooPtr&quot;</tt></p>
<dt>&bull;</p>
<dd> <i></i>$arg<i></i> &#8211; the stack entry, that the parameter is input from or output to, e.g. <tt>ST(0)</tt></p>
<dt>&bull;</p>
<dd> <i></i>$argoff<i></i> &#8211; the argument stack offset of the argument. ie. 0 for the first argument, etc.</p>
<dt>&bull;</p>
<dd> <i></i>$pname<i></i> &#8211; the full name of the <font SIZE="-1">XSUB,</font> with including the <tt>&quot;PACKAGE&quot;</tt> name, with any <tt>&quot;PREFIX&quot;</tt> stripped. This is the non-ALIAS name.</p>
<dt>&bull;</p>
<dd> <i></i>$Package<i></i> &#8211; the package specified by the most recent <tt>&quot;PACKAGE&quot;</tt> keyword.</p>
<dt>&bull;</p>
<dd> <i></i>$ALIAS<i></i> &#8211; non-zero if the current <font SIZE="-1">XSUB</font> has any aliases declared with <tt>&quot;ALIAS&quot;</tt>.</dl>
<h3>Full Listing of Core Typemaps</h3>
<p> Each C type is represented by an entry in the typemap file that is responsible for converting perl variables (<font SIZE="-1">SV, AV, HV, CV,</font> etc.) to and from that type. The following sections list all <font SIZE="-1">XS</font> types that come with perl by default.</p>
<dl>
<dt>T_SV</p>
<dd> This simply passes the C representation of the Perl variable (an SV*) in and out of the <font SIZE="-1">XS</font> layer. This can be used if the C code wants to deal directly with the Perl variable.</p>
<dt>T_SVREF</p>
<dd> Used to pass in and return a reference to an <font SIZE="-1">SV.</font> </p>
<p> Note that this typemap does not decrement the reference count when returning the reference to an SV*. See also: T_SVREF_REFCOUNT_FIXED</p>
<dt>T_SVREF_FIXED</p>
<dd> Used to pass in and return a reference to an <font SIZE="-1">SV.</font> This is a fixed variant of T_SVREF that decrements the refcount appropriately when returning a reference to an SV*. Introduced in perl 5.15.4.</p>
<dt>T_AVREF</p>
<dd> From the perl level this is a reference to a perl array. From the C level this is a pointer to an <font SIZE="-1">AV.</font> </p>
<p> Note that this typemap does not decrement the reference count when returning an AV*. See also: T_AVREF_REFCOUNT_FIXED</p>
<dt>T_AVREF_REFCOUNT_FIXED</p>
<dd> From the perl level this is a reference to a perl array. From the C level this is a pointer to an <font SIZE="-1">AV.</font> This is a fixed variant of T_AVREF that decrements the refcount appropriately when returning an AV*. Introduced in perl 5.15.4.</p>
<dt>T_HVREF</p>
<dd> From the perl level this is a reference to a perl hash. From the C level this is a pointer to an <font SIZE="-1">HV.</font> </p>
<p> Note that this typemap does not decrement the reference count when returning an HV*. See also: T_HVREF_REFCOUNT_FIXED</p>
<dt>T_HVREF_REFCOUNT_FIXED</p>
<dd> From the perl level this is a reference to a perl hash. From the C level this is a pointer to an <font SIZE="-1">HV.</font> This is a fixed variant of T_HVREF that decrements the refcount appropriately when returning an HV*. Introduced in perl 5.15.4.</p>
<dt>T_CVREF</p>
<dd> From the perl level this is a reference to a perl subroutine (e.g. <tt>$sub</tt> = sub { 1 };). From the C level this is a pointer to a <font SIZE="-1">CV.</font> </p>
<p> Note that this typemap does not decrement the reference count when returning an HV*. See also: T_HVREF_REFCOUNT_FIXED</p>
<dt>T_CVREF_REFCOUNT_FIXED</p>
<dd> From the perl level this is a reference to a perl subroutine (e.g. <tt>$sub</tt> = sub { 1 };). From the C level this is a pointer to a <font SIZE="-1">CV.</font> </p>
<p> This is a fixed variant of T_HVREF that decrements the refcount appropriately when returning an HV*. Introduced in perl 5.15.4.</p>
<dt>T_SYSRET</p>
<dd> The T_SYSRET typemap is used to process return values from system calls. It is only meaningful when passing values from C to perl (there is no concept of passing a system return value from Perl to C). </p>
<p> System calls return -1 on error (setting <font SIZE="-1">ERRNO</font> with the reason) and (usually) 0 on success. If the return value is -1 this typemap returns <tt>&quot;undef&quot;</tt>. If the return value is not -1, this typemap translates a 0 (perl false) to &#8220;0 but true&#8221; (which is perl true) or returns the value itself, to indicate that the command succeeded. </p>
<p> The <font SIZE="-1">POSIX</font> module makes extensive use of this type.</p>
<dt>T_UV</p>
<dd> An unsigned integer.</p>
<dt>T_IV</p>
<dd> A signed integer. This is cast to the required integer type when passed to C and converted to an <font SIZE="-1">IV</font> when passed back to Perl.</p>
<dt>T_INT</p>
<dd> A signed integer. This typemap converts the Perl value to a native integer type (the <tt>&quot;int&quot;</tt> type on the current platform). When returning the value to perl it is processed in the same way as for T_IV. </p>
<p> Its behaviour is identical to using an <tt>&quot;int&quot;</tt> type in <font SIZE="-1">XS</font> with T_IV.</p>
<dt>T_ENUM</p>
<dd> An enum value. Used to transfer an enum component from C. There is no reason to pass an enum value to C since it is stored as an <font SIZE="-1">IV</font> inside perl.</p>
<dt>T_BOOL</p>
<dd> A boolean type. This can be used to pass true and false values to and from C.</p>
<dt>T_U_INT</p>
<dd> This is for unsigned integers. It is equivalent to using T_UV but explicitly casts the variable to type <tt>&quot;unsigned int&quot;</tt>. The default type for <tt>&quot;unsigned int&quot;</tt> is T_UV.</p>
<dt>T_SHORT</p>
<dd> Short integers. This is equivalent to T_IV but explicitly casts the return to type <tt>&quot;short&quot;</tt>. The default typemap for <tt>&quot;short&quot;</tt> is T_IV.</p>
<dt>T_U_SHORT</p>
<dd> Unsigned short integers. This is equivalent to T_UV but explicitly casts the return to type <tt>&quot;unsigned short&quot;</tt>. The default typemap for <tt>&quot;unsigned short&quot;</tt> is T_UV. </p>
<p> T_U_SHORT is used for type <tt>&quot;U16&quot;</tt> in the standard typemap.</p>
<dt>T_LONG</p>
<dd> Long integers. This is equivalent to T_IV but explicitly casts the return to type <tt>&quot;long&quot;</tt>. The default typemap for <tt>&quot;long&quot;</tt> is T_IV.</p>
<dt>T_U_LONG</p>
<dd> Unsigned long integers. This is equivalent to T_UV but explicitly casts the return to type <tt>&quot;unsigned long&quot;</tt>. The default typemap for <tt>&quot;unsigned long&quot;</tt> is T_UV. </p>
<p> T_U_LONG is used for type <tt>&quot;U32&quot;</tt> in the standard typemap.</p>
<dt>T_CHAR</p>
<dd> Single 8-bit characters.</p>
<dt>T_U_CHAR</p>
<dd> An unsigned byte.</p>
<dt>T_FLOAT</p>
<dd> A floating point number. This typemap guarantees to return a variable cast to a <tt>&quot;float&quot;</tt>.</p>
<dt>T_NV</p>
<dd> A Perl floating point number. Similar to T_IV and T_UV in that the return type is cast to the requested numeric type rather than to a specific type.</p>
<dt>T_DOUBLE</p>
<dd> A double precision floating point number. This typemap guarantees to return a variable cast to a <tt>&quot;double&quot;</tt>.</p>
<dt>T_PV</p>
<dd> A string (char *).</p>
<dt>T_PTR</p>
<dd> A memory address (pointer). Typically associated with a <tt>&quot;void *&quot;</tt> type.</p>
<dt>T_PTRREF</p>
<dd> Similar to T_PTR except that the pointer is stored in a scalar and the reference to that scalar is returned to the caller. This can be used to hide the actual pointer value from the programmer since it is usually not required directly from within perl. </p>
<p> The typemap checks that a scalar reference is passed from perl to <font SIZE="-1">XS.</font></p>
<dt>T_PTROBJ</p>
<dd> Similar to T_PTRREF except that the reference is blessed into a class. This allows the pointer to be used as an object. Most commonly used to deal with C structs. The typemap checks that the perl object passed into the <font SIZE="-1">XS</font> routine is of the correct class (or part of a subclass). </p>
<p> The pointer is blessed into a class that is derived from the name of type of the pointer but with all &#8216;*&#8217; in the name replaced with &#8216;Ptr&#8217;. </p>
<p> For <tt>&quot;DESTROY&quot;</tt> XSUBs only, a T_PTROBJ is optimized to a T_PTRREF. This means the class check is skipped.</p>
<dt>T_REF_IV_REF</p>
<dd> <font SIZE="-1">NOT YET</font></p>
<dt>T_REF_IV_PTR</p>
<dd> Similar to T_PTROBJ in that the pointer is blessed into a scalar object. The difference is that when the object is passed back into <font SIZE="-1">XS</font> it must be of the correct type (inheritance is not supported) while T_PTROBJ supports inheritance. </p>
<p> The pointer is blessed into a class that is derived from the name of type of the pointer but with all &#8216;*&#8217; in the name replaced with &#8216;Ptr&#8217;. </p>
<p> For <tt>&quot;DESTROY&quot;</tt> XSUBs only, a T_REF_IV_PTR is optimized to a T_PTRREF. This means the class check is skipped.</p>
<dt>T_PTRDESC</p>
<dd> <font SIZE="-1">NOT YET</font></p>
<dt>T_REFREF</p>
<dd> Similar to T_PTRREF, except the pointer stored in the referenced scalar is dereferenced and copied to the output variable. This means that T_REFREF is to T_PTRREF as T_OPAQUE is to T_OPAQUEPTR. All clear? </p>
<p> Only the <font SIZE="-1">INPUT</font> part of this is implemented (Perl to <font SIZE="-1">XSUB</font>) and there are no known users in core or on <font SIZE="-1">CPAN.</font></p>
<dt>T_REFOBJ</p>
<dd> Like T_REFREF, except it does strict type checking (inheritance is not supported). </p>
<p> For <tt>&quot;DESTROY&quot;</tt> XSUBs only, a T_REFOBJ is optimized to a T_REFREF. This means the class check is skipped.</p>
<dt>T_OPAQUEPTR</p>
<dd> This can be used to store bytes in the string component of the <font SIZE="-1">SV.</font> Here the representation of the data is irrelevant to perl and the bytes themselves are just stored in the <font SIZE="-1">SV.</font> It is assumed that the C variable is a pointer (the bytes are copied from that memory location). If the pointer is pointing to something that is represented by 8 bytes then those 8 bytes are stored in the <font SIZE="-1">SV</font> (and <code>length()</code> will report a value of 8). This entry is similar to T_OPAQUE. </p>
<p> In principle the <code>unpack()</code> command can be used to convert the bytes back to a number (if the underlying type is known to be a number). </p>
<p> This entry can be used to store a C structure (the number of bytes to be copied is calculated using the C <tt>&quot;sizeof&quot;</tt> function) and can be used as an alternative to T_PTRREF without having to worry about a memory leak (since Perl will clean up the <font SIZE="-1">SV</font>).</p>
<dt>T_OPAQUE</p>
<dd> This can be used to store data from non-pointer types in the string part of an <font SIZE="-1">SV.</font> It is similar to T_OPAQUEPTR except that the typemap retrieves the pointer directly rather than assuming it is being supplied. For example, if an integer is imported into Perl using T_OPAQUE rather than T_IV the underlying bytes representing the integer will be stored in the <font SIZE="-1">SV</font> but the actual integer value will not be available. i.e. The data is opaque to perl. </p>
<p> The data may be retrieved using the <tt>&quot;unpack&quot;</tt> function if the underlying type of the byte stream is known. </p>
<p> T_OPAQUE supports input and output of simple types. T_OPAQUEPTR can be used to pass these bytes back into C if a pointer is acceptable.</p>
<dt>Implicit array</p>
<dd> xsubpp supports a special syntax for returning packed C arrays to perl. If the <font SIZE="-1">XS</font> return type is given as </p>
<pre>
  array(type, nelem)
</pre>
<p> xsubpp will copy the contents of <tt>&quot;nelem * sizeof(type)&quot;</tt> bytes from <font SIZE="-1">RETVAL</font> to an <font SIZE="-1">SV</font> and push it onto the stack. This is only really useful if the number of items to be returned is known at compile time and you don&#8217;t mind having a string of bytes in your <font SIZE="-1">SV.</font> Use T_ARRAY to push a variable number of arguments onto the return stack (they won&#8217;t be packed as a single string though). </p>
<p> This is similar to using T_OPAQUEPTR but can be used to process more than one element.</p>
<dt>T_PACKED</p>
<dd> Calls user-supplied functions for conversion. For <tt>&quot;OUTPUT&quot;</tt> (<font SIZE="-1">XSUB</font> to Perl), a function named <tt>&quot;XS_pack_$ntype&quot;</tt> is called with the output Perl scalar and the C variable to convert from. <tt>$ntype</tt> is the normalized C type that is to be mapped to Perl. Normalized means that all <tt>&quot;*&quot;</tt> are replaced by the string <tt>&quot;Ptr&quot;</tt>. The return value of the function is ignored. </p>
<p> Conversely for <tt>&quot;INPUT&quot;</tt> (Perl to <font SIZE="-1">XSUB</font>) mapping, the function named <tt>&quot;XS_unpack_$ntype&quot;</tt> is called with the input Perl scalar as argument and the return value is cast to the mapped C type and assigned to the output C variable. </p>
<p> An example conversion function for a typemapped struct <tt>&quot;foo_t *&quot;</tt> might be: </p>
<p>static void<br />
XS_pack_foo_tPtr(SV *out, foo_t *in)<br />
{<br />
    dTHX; /* alas, signature does not include pTHX_ */<br />
    HV *hash = newHV();<br />
    hv_stores(hash, &#8220;int_member&#8221;, newSViv(in-&gt;int_member));<br />
    hv_stores(hash, &#8220;float_member&#8221;, newSVnv(in-&gt;float_member));<br />
    /* &#8230; */<br />
    /* mortalize as thy stack is not refcounted */<br />
    sv_setsv(out, sv_2mortal(newRV_noinc((SV *)hash)));<br />
}</p>
<p> The conversion from Perl to C is left as an exercise to the reader, but the prototype would be: </p>
<p>static foo_t *<br />
XS_unpack_foo_tPtr(SV *in);</p>
<p> Instead of an actual C function that has to fetch the thread context using <tt>&quot;dTHX&quot;</tt>, you can define macros of the same name and avoid the overhead. Also, keep in mind to possibly free the memory allocated by <tt>&quot;XS_unpack_foo_tPtr&quot;</tt>.</p>
<dt>T_PACKEDARRAY</p>
<dd> T_PACKEDARRAY is similar to T_PACKED. In fact, the <tt>&quot;INPUT&quot;</tt> (Perl to <font SIZE="-1">XSUB</font>) typemap is identical, but the <tt>&quot;OUTPUT&quot;</tt> typemap passes an additional argument to the <tt>&quot;XS_pack_$ntype&quot;</tt> function. This third parameter indicates the number of elements in the output so that the function can handle C arrays sanely. The variable needs to be declared by the user and must have the name <tt>&quot;count_$ntype&quot;</tt> where <tt>$ntype</tt> is the normalized C type name as explained above. The signature of the function would be for the example above and <tt>&quot;foo_t **&quot;</tt>: </p>
<pre><code>
static void
XS_pack_foo_tPtrPtr(SV *out, foo_t *in, UV count_foo_tPtrPtr);
</code></pre>
<p> The type of the third parameter is arbitrary as far as the typemap is concerned. It just has to be in line with the declared variable. </p>
<p> Of course, unless you know the number of elements in the <tt>&quot;sometype **&quot;</tt> C array, within your <font SIZE="-1">XSUB,</font> the return value from <tt>&quot;foo_t ** XS_unpack_foo_tPtrPtr(...)&quot;</tt> will be hard to decipher. Since the details are all up to the <font SIZE="-1">XS</font> author (the typemap user), there are several solutions, none of which particularly elegant. The most commonly seen solution has been to allocate memory for N+1 pointers and assign <tt>&quot;NULL&quot;</tt> to the (N+1)th to facilitate iteration. </p>
<p> Alternatively, using a customized typemap for your purposes in the first place is probably preferable.</p>
<dt>T_DATAUNIT</p>
<dd> <font SIZE="-1">NOT YET</font></p>
<dt>T_CALLBACK</p>
<dd> <font SIZE="-1">NOT YET</font></p>
<dt>T_ARRAY</p>
<dd> This is used to convert the perl argument list to a C array and for pushing the contents of a C array onto the perl argument stack. </p>
<p> The usual calling signature is </p>
<pre>
  @out = array_func( @in );
</pre>
<p> Any number of arguments can occur in the list before the array but the input and output arrays must be the last elements in the list. </p>
<p> When used to pass a perl list to C the <font SIZE="-1">XS</font> writer must provide a function (named after the array type but with &#8216;Ptr&#8217; substituted for &#8216;*&#8217;) to allocate the memory required to hold the list. A pointer should be returned. It is up to the <font SIZE="-1">XS</font> writer to free the memory on exit from the function. The variable <tt>&quot;ix_$var&quot;</tt> is set to the number of elements in the new array. </p>
<p> When returning a C array to Perl the <font SIZE="-1">XS</font> writer must provide an integer variable called <tt>&quot;size_$var&quot;</tt> containing the number of elements in the array. This is used to determine how many elements should be pushed onto the return argument stack. This is not required on input since Perl knows how many arguments are on the stack when the routine is called. Ordinarily this variable would be called <tt>&quot;size_RETVAL&quot;</tt>. </p>
<p> Additionally, the type of each element is determined from the type of the array. If the array uses type <tt>&quot;intArray *&quot;</tt> xsubpp will automatically work out that it contains variables of type <tt>&quot;int&quot;</tt> and use that typemap entry to perform the copy of each element. All pointer &#8216;*&#8217; and &#8216;Array&#8217; tags are removed from the name to determine the subtype.</p>
<dt>T_STDIO</p>
<dd> This is used for passing perl filehandles to and from C using <tt>&quot;FILE *&quot;</tt> structures.</p>
<dt>T_INOUT</p>
<dd> This is used for passing perl filehandles to and from C using <tt>&quot;PerlIO *&quot;</tt> structures. The file handle can used for reading and writing. This corresponds to the <tt>&quot;+&lt;&quot;</tt> mode, see also T_IN and T_OUT. </p>
<p> See perliol for more information on the Perl <font SIZE="-1">IO</font> abstraction layer. Perl must have been built with <tt>&quot;-Duseperlio&quot;</tt>. </p>
<p> There is no check to assert that the filehandle passed from Perl to C was created with the right <tt>&quot;open()&quot;</tt> mode. </p>
<p> Hint: The perlxstut tutorial covers the T_INOUT, T_IN, and T_OUT <font SIZE="-1">XS</font> types nicely.</p>
<dt>T_IN</p>
<dd> Same as T_INOUT, but the filehandle that is returned from C to Perl can only be used for reading (mode <tt>&quot;&lt;&quot;</tt>).</p>
<dt>T_OUT</p>
<dd> Same as T_INOUT, but the filehandle that is returned from C to Perl is set to use the open mode <tt>&quot;+&gt;&quot;</tt>. </p>
</dl>
<h2>Index</h2>
</dl>
