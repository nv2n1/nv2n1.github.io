---
title: "std__codecvt_abstract_base(3)"
name: "std__codecvt_abstract_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__codecvt_abstract_base/"
description: "std::__codecvt_abstract_base< _InternT, _ExternT, _StateT > –"
---

<p>std::__codecvt_abstract_base&lt; _InternT, _ExternT, _StateT &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::locale::facet</code>, and <code>std::codecvt_base</code>. Inherited by <code>std::codecvt&lt; _InternT, _ExternT, _StateT &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef _ExternT <code>extern_type</code> </p>
<p> typedef _InternT <code>intern_type</code> </p>
<p> typedef codecvt_base::result <code>result</code> </p>
<p> typedef _StateT <code>state_type</code></p>
<h3>Public Member Functions</h3>
<p>bool <code>always_noconv</code> () const throw () </p>
<p> int <code>encoding</code> () const throw () </p>
<p> result <code>in</code> (state_type &amp;__state, const extern_type *__from, const extern_type *__from_end, const extern_type *&amp;__from_next, intern_type *__to, intern_type *__to_end, intern_type *&amp;__to_next) const </p>
<p> int <code>length</code> (state_type &amp;__state, const extern_type *__from, const extern_type *__end, size_t __max) const </p>
<p> int <code>max_length</code> () const throw () </p>
<p> result <code>out</code> (state_type &amp;__state, const intern_type *__from, const intern_type *__from_end, const intern_type *&amp;__from_next, extern_type *__to, extern_type *__to_end, extern_type *&amp;__to_next) const </p>
<p> result <code>unshift</code> (state_type &amp;__state, extern_type *__to, extern_type *__to_end, extern_type *&amp;__to_next) const</p>
<h3>Protected Member Functions</h3>
<pre><code>__codecvt_abstract_base (size_t __refs=0)



virtual bool do_always_noconv () const =0  throw ()



virtual int do_encoding () const =0  throw ()



virtual result do_in (state_type &amp;__state, const extern_type *__from, const extern_type *__from_end, const extern_type *&amp;__from_next, intern_type *__to, intern_type *__to_end, intern_type *&amp;__to_next) const =0



virtual int do_length (state_type &amp;, const extern_type *__from, const extern_type *__end, size_t __max) const =0



virtual int do_max_length () const =0  throw ()



virtual result do_out (state_type &amp;__state, const intern_type *__from, const intern_type *__from_end, const intern_type *&amp;__from_next, extern_type *__to, extern_type *__to_end, extern_type *&amp;__to_next) const =0



virtual result do_unshift (state_type &amp;__state, extern_type *__to, extern_type *__to_end, extern_type *&amp;__to_next) const =0



Static Protected Member Functions
static __c_locale _S_clone_c_locale (__c_locale &amp;__cloc)  throw ()



static void _S_create_c_locale (__c_locale &amp;__cloc, const char *__s, __c_locale __old=0)



static void _S_destroy_c_locale (__c_locale &amp;__cloc)



static __c_locale _S_get_c_locale ()



static const char * _S_get_c_name ()  throw ()



static __c_locale _S_lc_ctype_c_locale (__c_locale __cloc, const char *__s)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _InternT, typename _ExternT, typename _StateT&gt;class std::__codecvt_abstract_base&lt; _InternT, _ExternT, _StateT &gt;</h3>
<p>Common base for codecvt functions. </p>
<p> This template class provides implementations of the public functions that forward to the protected virtual functions. </p>
<p> This template also provides abstract stubs for the protected virtual functions. </p>
<p> Definition at line 68 of file codecvt.h.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename _InternT, typename _ExternT, typename _StateT&gt; virtual result <code>std::__codecvt_abstract_base</code>&lt; _InternT, _ExternT, _StateT &gt;::do_out (state_type &amp;__state, const intern_type *__from, const intern_type *__from_end, const intern_type *&amp;__from_next, extern_type *__to, extern_type *__to_end, extern_type *&amp;__to_next) const [protected], [pure virtual]</h3>
<p>Convert from internal to external character set. Converts input string of intern_type to output string of extern_type. This function is a hook for derived classes to change the value returned. </p>
<p> <code>See Also:</code></p>
<dl>
<dd>out for more information.</dl>
<p> Implemented in <code>std::codecvt&lt; wchar_t, char, mbstate_t &gt;</code>, <code>std::codecvt&lt; char, char, mbstate_t &gt;</code>, <code>std::codecvt&lt; _InternT, _ExternT, _StateT &gt;</code>, and <code>std::codecvt&lt; _InternT, _ExternT, encoding_state &gt;</code>. </p>
<p> Referenced by std::__codecvt_abstract_base&lt; _InternT, _ExternT, encoding_state &gt;::out().</p>
<h3>template&lt;typename _InternT, typename _ExternT, typename _StateT&gt; result <code>std::__codecvt_abstract_base</code>&lt; _InternT, _ExternT, _StateT &gt;::in (state_type &amp;__state, const extern_type *__from, const extern_type *__from_end, const extern_type *&amp;__from_next, intern_type *__to, intern_type *__to_end, intern_type *&amp;__to_next) const [inline]</h3>
<p>Convert from external to internal character set. Converts input string of extern_type to output string of intern_type. This is analogous to mbsrtowcs. It does this by calling codecvt::do_in. </p>
<p> The source and destination character sets are determined by the facet&#8217;s locale, internal and external types. </p>
<p> The characters in [from,from_end) are converted and written to [to,to_end). from_next and to_next are set to point to the character following the last successfully converted character, respectively. If the result needed no conversion, from_next and to_next are not affected. </p>
<p> The <i>state</i> argument should be initialized if the input is at the beginning and carried from a previous call if continuing conversion. There are no guarantees about how <i>state</i> is used. </p>
<p> The result returned is a member of codecvt_base::result. If all the input is converted, returns codecvt_base::ok. If no conversion is necessary, returns codecvt_base::noconv. If the input ends early or there is insufficient space in the output, returns codecvt_base::partial. Otherwise the conversion failed and codecvt_base::error is returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__state</i> Persistent conversion state data.<br />
 <i>__from</i> Start of input.<br />
 <i>__from_end</i> End of input.<br />
 <i>__from_next</i> Returns start of unconverted data.<br />
 <i>__to</i> Start of output buffer.<br />
 <i>__to_end</i> End of output buffer.<br />
 <i>__to_next</i> Returns start of unused output area.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>codecvt_base::result.</dl>
<p> Definition at line 196 of file codecvt.h.</p>
<h3>template&lt;typename _InternT, typename _ExternT, typename _StateT&gt; result <code>std::__codecvt_abstract_base</code>&lt; _InternT, _ExternT, _StateT &gt;::out (state_type &amp;__state, const intern_type *__from, const intern_type *__from_end, const intern_type *&amp;__from_next, extern_type *__to, extern_type *__to_end, extern_type *&amp;__to_next) const [inline]</h3>
<p>Convert from internal to external character set. Converts input string of intern_type to output string of extern_type. This is analogous to wcsrtombs. It does this by calling codecvt::do_out. </p>
<p> The source and destination character sets are determined by the facet&#8217;s locale, internal and external types. </p>
<p> The characters in [from,from_end) are converted and written to [to,to_end). from_next and to_next are set to point to the character following the last successfully converted character, respectively. If the result needed no conversion, from_next and to_next are not affected. </p>
<p> The <i>state</i> argument should be initialized if the input is at the beginning and carried from a previous call if continuing conversion. There are no guarantees about how <i>state</i> is used. </p>
<p> The result returned is a member of codecvt_base::result. If all the input is converted, returns codecvt_base::ok. If no conversion is necessary, returns codecvt_base::noconv. If the input ends early or there is insufficient space in the output, returns codecvt_base::partial. Otherwise the conversion failed and codecvt_base::error is returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__state</i> Persistent conversion state data.<br />
 <i>__from</i> Start of input.<br />
 <i>__from_end</i> End of input.<br />
 <i>__from_next</i> Returns start of unconverted data.<br />
 <i>__to</i> Start of output buffer.<br />
 <i>__to_end</i> End of output buffer.<br />
 <i>__to_next</i> Returns start of unused output area.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>codecvt_base::result.</dl>
<p> Definition at line 116 of file codecvt.h.</p>
<h3>template&lt;typename _InternT, typename _ExternT, typename _StateT&gt; result <code>std::__codecvt_abstract_base</code>&lt; _InternT, _ExternT, _StateT &gt;::unshift (state_type &amp;__state, extern_type *__to, extern_type *__to_end, extern_type *&amp;__to_next) const [inline]</h3>
<p>Reset conversion state. Writes characters to output that would restore <i>state</i> to initial conditions. The idea is that if a partial conversion occurs, then the converting the characters written by this function would leave the state in initial conditions, rather than partial conversion state. It does this by calling codecvt::do_unshift(). </p>
<p> For example, if 4 external characters always converted to 1 internal character, and input to in() had 6 external characters with state saved, this function would write two characters to the output and set the state to initialized conditions. </p>
<p> The source and destination character sets are determined by the facet&#8217;s locale, internal and external types. </p>
<p> The result returned is a member of codecvt_base::result. If the state could be reset and data written, returns codecvt_base::ok. If no conversion is necessary, returns codecvt_base::noconv. If the output has insufficient space, returns codecvt_base::partial. Otherwise the reset failed and codecvt_base::error is returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__state</i> Persistent conversion state data.<br />
 <i>__to</i> Start of output buffer.<br />
 <i>__to_end</i> End of output buffer.<br />
 <i>__to_next</i> Returns start of unused output area.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>codecvt_base::result.</dl>
<p> Definition at line 155 of file codecvt.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
