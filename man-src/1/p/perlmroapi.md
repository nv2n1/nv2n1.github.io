---
title: "perlmroapi(1)"
name: "perlmroapi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlmroapi/"
---

<h2 class="name">NAME</h2>
 

 perlmroapi - Perl method resolution plugin interface 

<h2>DESCRIPTION</h2>

 As of Perl 5.10.1 there is a new interface for plugging and using method resolution orders other than the default (linear depth first search). The C3 method resolution order added in 5.10.0 has been re-implemented as a plugin, without changing its Perl-space interface. 

 Each plugin should register itself by providing the following structure 

 <pre><code>
struct mro_alg {
    AV *(*resolve)(pTHX_ HV *stash, U32 level);
    const char *name;
    U16 length;
    U16 kflags;
    U32 hash;
};
</code></pre> 

 and calling <tt>&quot;Perl_mro_register&quot;</tt>: 

 <pre>
    Perl_mro_register(aTHX_ &amp;my_mro_alg);
</pre>
<dl>
<dt>resolve
<dd> Pointer to the linearisation function, described below.
<dt>name
<dd> Name of the <font SIZE="-1">MRO,</font> either in <font SIZE="-1">ISO-8859-1</font> or <font SIZE="-1">UTF-8.</font>
<dt>length
<dd> Length of the name.
<dt>kflags
<dd> If the name is given in <font SIZE="-1">UTF-8,</font> set this to <tt>&quot;HVhek_UTF8&quot;</tt>. The value is passed direct as the parameter <i>kflags</i> to <tt>&quot;hv_common()&quot;</tt>.
<dt>hash
<dd> A precomputed hash value for the <font SIZE="-1">MRO</font>'s name, or 0.</dl>

<h2>Callbacks</h2>

 The <tt>&quot;resolve&quot;</tt> function is called to generate a linearised <font SIZE="-1">ISA</font> for the given stash, using this <font SIZE="-1">MRO.</font> It is called with a pointer to the stash, and a <i>level</i> of 0. The core always sets <i>level</i> to 0 when it calls your function - the parameter is provided to allow your implementation to track depth if it needs to recurse. 

 The function should return a reference to an array containing the parent classes in order. The names of the classes should be the result of calling <tt>&quot;HvENAME()&quot;</tt> on the stash. In those cases where <tt>&quot;HvENAME()&quot;</tt> returns null, <tt>&quot;HvNAME()&quot;</tt> should be used instead. 

 The caller is responsible for incrementing the reference count of the array returned if it wants to keep the structure. Hence, if you have created a temporary value that you keep no pointer to, <tt>&quot;sv_2mortal()&quot;</tt> to ensure that it is disposed of correctly. If you have cached your return value, then return a pointer to it without changing the reference count.

<h2>Caching</h2>

 Computing MROs can be expensive. The implementation provides a cache, in which you can store a single <tt>&quot;SV *&quot;</tt>, or anything that can be cast to <tt>&quot;SV *&quot;</tt>, such as <tt>&quot;AV *&quot;</tt>. To read your private value, use the macro <tt>&quot;MRO_GET_PRIVATE_DATA()&quot;</tt>, passing it the <tt>&quot;mro_meta&quot;</tt> structure from the stash, and a pointer to your <tt>&quot;mro_alg&quot;</tt> structure: 

 <pre><code>
meta = HvMROMETA(stash);
private_sv = MRO_GET_PRIVATE_DATA(meta, &amp;my_mro_alg);
</code></pre> 

 To set your private value, call <tt>&quot;Perl_mro_set_private_data()&quot;</tt>: 

 <pre>
    Perl_mro_set_private_data(aTHX_ meta, &amp;c3_alg, private_sv);
</pre> 

 The private data cache will take ownership of a reference to private_sv, much the same way that <tt>&quot;hv_store()&quot;</tt> takes ownership of a reference to the value that you pass it.

<h2>Examples</h2>

 For examples of <font SIZE="-1">MRO</font> implementations, see <tt>&quot;S_mro_get_linear_isa_c3()&quot;</tt> and the <tt>&quot;BOOT:&quot;</tt> section of <i>ext/mro/mro.xs</i>, and <tt>&quot;S_mro_get_linear_isa_dfs()&quot;</tt> in <i>mro_core.c</i>

<h2>AUTHORS</h2>

 The implementation of the C3 <font SIZE="-1">MRO</font> and switchable MROs within the perl core was written by Brandon L Black. Nicholas Clark created the pluggable interface, refactored Brandon's implementation to work with it, and wrote this document. 

<h2>Index</h2>


