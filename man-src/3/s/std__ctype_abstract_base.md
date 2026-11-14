---
title: "std__ctype_abstract_base(3)"
name: "std__ctype_abstract_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__ctype_abstract_base/"
description: "std::__ctype_abstract_base< _CharT > –"
---

<p>std::__ctype_abstract_base&lt; _CharT &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::locale::facet</code>, and <code>std::ctype_base</code>. Inherited by <code>std::ctype&lt; _CharT &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef const int * <code>__to_type</code> </p>
<p> typedef _CharT <code>char_type</code> </p>
<p> typedef unsigned short <code>mask</code></p>
<h3>Public Member Functions</h3>
<p>bool <code>is</code> (mask __m, <code>char_type</code> __c) const </p>
<p> const <code>char_type</code> * <code>is</code> (const <code>char_type</code> *__lo, const <code>char_type</code> *__hi, mask *__vec) const </p>
<p> char <code>narrow</code> (<code>char_type</code> __c, char __dfault) const </p>
<p> const <code>char_type</code> * <code>narrow</code> (const <code>char_type</code> *__lo, const <code>char_type</code> *__hi, char __dfault, char *__to) const </p>
<p> const <code>char_type</code> * <code>scan_is</code> (mask __m, const <code>char_type</code> *__lo, const <code>char_type</code> *__hi) const </p>
<p> const <code>char_type</code> * <code>scan_not</code> (mask __m, const <code>char_type</code> *__lo, const <code>char_type</code> *__hi) const </p>
<p> <code>char_type</code> <code>tolower</code> (<code>char_type</code> __c) const </p>
<p> const <code>char_type</code> * <code>tolower</code> (<code>char_type</code> *__lo, const <code>char_type</code> *__hi) const </p>
<p> <code>char_type</code> <code>toupper</code> (<code>char_type</code> __c) const </p>
<p> const <code>char_type</code> * <code>toupper</code> (<code>char_type</code> *__lo, const <code>char_type</code> *__hi) const </p>
<p> <code>char_type</code> <code>widen</code> (char __c) const </p>
<p> const char * <code>widen</code> (const char *__lo, const char *__hi, <code>char_type</code> *__to) const</p>
<h3>Static Public Attributes</h3>
<pre><code>static const mask alnum



static const mask alpha



static const mask cntrl



static const mask digit



static const mask graph



static const mask lower



static const mask print



static const mask punct



static const mask space



static const mask upper



static const mask xdigit



Protected Member Functions
__ctype_abstract_base (size_t __refs=0)



virtual bool do_is (mask __m, char_type __c) const =0



virtual const char_type * do_is (const char_type *__lo, const char_type *__hi, mask *__vec) const =0



virtual char do_narrow (char_type __c, char __dfault) const =0



virtual const char_type * do_narrow (const char_type *__lo, const char_type *__hi, char __dfault, char *__to) const =0



virtual const char_type * do_scan_is (mask __m, const char_type *__lo, const char_type *__hi) const =0



virtual const char_type * do_scan_not (mask __m, const char_type *__lo, const char_type *__hi) const =0



virtual char_type do_tolower (char_type __c) const =0



virtual const char_type * do_tolower (char_type *__lo, const char_type *__hi) const =0



virtual char_type do_toupper (char_type __c) const =0



virtual const char_type * do_toupper (char_type *__lo, const char_type *__hi) const =0



virtual char_type do_widen (char __c) const =0



virtual const char * do_widen (const char *__lo, const char *__hi, char_type *__to) const =0



Static Protected Member Functions
static __c_locale _S_clone_c_locale (__c_locale &amp;__cloc)  throw ()



static void _S_create_c_locale (__c_locale &amp;__cloc, const char *__s, __c_locale __old=0)



static void _S_destroy_c_locale (__c_locale &amp;__cloc)



static __c_locale _S_get_c_locale ()



static const char * _S_get_c_name ()  throw ()



static __c_locale _S_lc_ctype_c_locale (__c_locale __cloc, const char *__s)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _CharT&gt;class std::__ctype_abstract_base&lt; _CharT &gt;</h3>
<p>Common base for ctype facet. </p>
<p> This template class provides implementations of the public functions that forward to the protected virtual functions. </p>
<p> This template also provides abstract stubs for the protected virtual functions. </p>
<p> Definition at line 143 of file locale_facets.h.</p>
<h2>Member Typedef Documentation</h2>
<h3>template&lt;typename _CharT&gt; typedef _CharT <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::<code>char_type</code></h3>
<p>Typedef for the template parameter. </p>
<p> Definition at line 148 of file locale_facets.h.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename _CharT&gt; virtual bool <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_is (mask__m, <code>char_type</code>__c) const [protected], [pure virtual]</h3>
<p>Test char_type classification. This function finds a mask M for <i>c</i> and compares it to mask <i>m</i>. </p>
<p> do_is() is a hook for a derived facet to change the behavior of classifying. do_is() must always return the same result for the same input. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char_type to find the mask of.<br />
 <i>__m</i> The mask to compare against.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(M &amp; __m) != 0.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>. </p>
<p> Referenced by std::__ctype_abstract_base&lt; wchar_t &gt;::is().</p>
<h3>template&lt;typename _CharT&gt; virtual const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_is (const <code>char_type</code> *__lo, const <code>char_type</code> *__hi, mask *__vec) const [protected], [pure virtual]</h3>
<p>Return a mask array. This function finds the mask for each char_type in the range [lo,hi) and successively writes it to vec. vec must have as many elements as the input. </p>
<p> do_is() is a hook for a derived facet to change the behavior of classifying. do_is() must always return the same result for the same input. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.<br />
 <i>__vec</i> Pointer to an array of mask storage.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>.</p>
<h3>template&lt;typename _CharT&gt; virtual char <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_narrow (<code>char_type</code>__c, char__dfault) const [protected], [pure virtual]</h3>
<p>Narrow char_type to char. This virtual function converts the argument to char using the simplest reasonable transformation. If the conversion fails, dfault is returned instead. </p>
<p> do_narrow() is a hook for a derived facet to change the behavior of narrowing. do_narrow() must always return the same result for the same input. </p>
<p> Note: this is not what you want for codepage conversions. See codecvt for that. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char_type to convert.<br />
 <i>__dfault</i> Char to return if conversion fails.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The converted char.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>. </p>
<p> Referenced by std::__ctype_abstract_base&lt; wchar_t &gt;::narrow().</p>
<h3>template&lt;typename _CharT&gt; virtual const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_narrow (const <code>char_type</code> *__lo, const <code>char_type</code> *__hi, char__dfault, char *__to) const [protected], [pure virtual]</h3>
<p>Narrow char_type array to char. This virtual function converts each char_type in the range [__lo,__hi) to char using the simplest reasonable transformation and writes the results to the destination array. For any element in the input that cannot be converted, <i>__dfault</i> is used instead. </p>
<p> do_narrow() is a hook for a derived facet to change the behavior of narrowing. do_narrow() must always return the same result for the same input. </p>
<p> Note: this is not what you want for codepage conversions. See codecvt for that. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.<br />
 <i>__dfault</i> Char to use if conversion fails.<br />
 <i>__to</i> Pointer to the destination array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>.</p>
<h3>template&lt;typename _CharT&gt; virtual const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_scan_is (mask__m, const <code>char_type</code> *__lo, const <code>char_type</code> *__hi) const [protected], [pure virtual]</h3>
<p>Find char_type matching mask. This function searches for and returns the first char_type c in [__lo,__hi) for which is(__m,c) is true. </p>
<p> do_scan_is() is a hook for a derived facet to change the behavior of match searching. do_is() must always return the same result for the same input. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__m</i> The mask to compare against.<br />
 <i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Pointer to a matching char_type if found, else <i>__hi</i>.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>. </p>
<p> Referenced by std::__ctype_abstract_base&lt; wchar_t &gt;::scan_is().</p>
<h3>template&lt;typename _CharT&gt; virtual const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_scan_not (mask__m, const <code>char_type</code> *__lo, const <code>char_type</code> *__hi) const [protected], [pure virtual]</h3>
<p>Find char_type not matching mask. This function searches for and returns a pointer to the first char_type c of [lo,hi) for which is(m,c) is false. </p>
<p> do_scan_is() is a hook for a derived facet to change the behavior of match searching. do_is() must always return the same result for the same input. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__m</i> The mask to compare against.<br />
 <i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Pointer to a non-matching char_type if found, else <i>__hi</i>.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>. </p>
<p> Referenced by std::__ctype_abstract_base&lt; wchar_t &gt;::scan_not().</p>
<h3>template&lt;typename _CharT&gt; virtual <code>char_type</code> <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_tolower (<code>char_type</code>__c) const [protected], [pure virtual]</h3>
<p>Convert to lowercase. This virtual function converts the argument to lowercase if possible. If not possible (for example, &#8216;2&#8217;), returns the argument. </p>
<p> do_tolower() is a hook for a derived facet to change the behavior of lowercasing. do_tolower() must always return the same result for the same input. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char_type to convert.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The lowercase char_type if convertible, else <i>__c</i>.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>. </p>
<p> Referenced by std::__ctype_abstract_base&lt; wchar_t &gt;::tolower().</p>
<h3>template&lt;typename _CharT&gt; virtual const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_tolower (<code>char_type</code> *__lo, const <code>char_type</code> *__hi) const [protected], [pure virtual]</h3>
<p>Convert array to lowercase. This virtual function converts each char_type in the range [__lo,__hi) to lowercase if possible. Other elements remain untouched. </p>
<p> do_tolower() is a hook for a derived facet to change the behavior of lowercasing. do_tolower() must always return the same result for the same input. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>.</p>
<h3>template&lt;typename _CharT&gt; virtual <code>char_type</code> <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_toupper (<code>char_type</code>__c) const [protected], [pure virtual]</h3>
<p>Convert to uppercase. This virtual function converts the char_type argument to uppercase if possible. If not possible (for example, &#8216;2&#8217;), returns the argument. </p>
<p> do_toupper() is a hook for a derived facet to change the behavior of uppercasing. do_toupper() must always return the same result for the same input. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char_type to convert.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The uppercase char_type if convertible, else <i>__c</i>.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>. </p>
<p> Referenced by std::__ctype_abstract_base&lt; wchar_t &gt;::toupper().</p>
<h3>template&lt;typename _CharT&gt; virtual const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_toupper (<code>char_type</code> *__lo, const <code>char_type</code> *__hi) const [protected], [pure virtual]</h3>
<p>Convert array to uppercase. This virtual function converts each char_type in the range [__lo,__hi) to uppercase if possible. Other elements remain untouched. </p>
<p> do_toupper() is a hook for a derived facet to change the behavior of uppercasing. do_toupper() must always return the same result for the same input. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>.</p>
<h3>template&lt;typename _CharT&gt; virtual <code>char_type</code> <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_widen (char__c) const [protected], [pure virtual]</h3>
<p>Widen char. This virtual function converts the char to char_type using the simplest reasonable transformation. </p>
<p> do_widen() is a hook for a derived facet to change the behavior of widening. do_widen() must always return the same result for the same input. </p>
<p> Note: this is not what you want for codepage conversions. See codecvt for that. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char to convert.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The converted char_type</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>. </p>
<p> Referenced by std::__ctype_abstract_base&lt; wchar_t &gt;::widen().</p>
<h3>template&lt;typename _CharT&gt; virtual const char* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::do_widen (const char *__lo, const char *__hi, <code>char_type</code> *__to) const [protected], [pure virtual]</h3>
<p>Widen char array. This function converts each char in the input to char_type using the simplest reasonable transformation. </p>
<p> do_widen() is a hook for a derived facet to change the behavior of widening. do_widen() must always return the same result for the same input. </p>
<p> Note: this is not what you want for codepage conversions. See codecvt for that. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start range.<br />
 <i>__hi</i> Pointer to end of range.<br />
 <i>__to</i> Pointer to the destination array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Implemented in <code>std::ctype&lt; wchar_t &gt;</code>, and <code>std::ctype&lt; _CharT &gt;</code>.</p>
<h3>template&lt;typename _CharT&gt; bool <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::is (mask__m, <code>char_type</code>__c) const [inline]</h3>
<p>Test char_type classification. This function finds a mask M for <i>__c</i> and compares it to mask <i>__m</i>. It does so by returning the value of ctype&lt;char_type&gt;::do_is(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char_type to compare the mask of.<br />
 <i>__m</i> The mask to compare against.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(M &amp; __m) != 0.</dl>
<p> Definition at line 162 of file locale_facets.h. </p>
<p> Referenced by std::basic_istream&lt; _CharT, _Traits &gt;::sentry::sentry().</p>
<h3>template&lt;typename _CharT&gt; const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::is (const <code>char_type</code> *__lo, const <code>char_type</code> *__hi, mask *__vec) const [inline]</h3>
<p>Return a mask array. This function finds the mask for each char_type in the range [lo,hi) and successively writes it to vec. vec must have as many elements as the char array. It does so by returning the value of ctype&lt;char_type&gt;::do_is(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.<br />
 <i>__vec</i> Pointer to an array of mask storage.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Definition at line 179 of file locale_facets.h.</p>
<h3>template&lt;typename _CharT&gt; char <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::narrow (<code>char_type</code>__c, char__dfault) const [inline]</h3>
<p>Narrow char_type to char. This function converts the char_type to char using the simplest reasonable transformation. If the conversion fails, dfault is returned instead. It does so by returning ctype&lt;char_type&gt;::do_narrow(__c). </p>
<p> Note: this is not what you want for codepage conversions. See codecvt for that. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char_type to convert.<br />
 <i>__dfault</i> Char to return if conversion fails.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The converted char.</dl>
<p> Definition at line 324 of file locale_facets.h. </p>
<p> Referenced by std::time_put&lt; _CharT, _OutIter &gt;::put().</p>
<h3>template&lt;typename _CharT&gt; const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::narrow (const <code>char_type</code> *__lo, const <code>char_type</code> *__hi, char__dfault, char *__to) const [inline]</h3>
<p>Narrow array to char array. This function converts each char_type in the input to char using the simplest reasonable transformation and writes the results to the destination array. For any char_type in the input that cannot be converted, <i>dfault</i> is used instead. It does so by returning ctype&lt;char_type&gt;::do_narrow(__lo, __hi, __dfault, __to). </p>
<p> Note: this is not what you want for codepage conversions. See codecvt for that. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.<br />
 <i>__dfault</i> Char to use if conversion fails.<br />
 <i>__to</i> Pointer to the destination array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Definition at line 346 of file locale_facets.h.</p>
<h3>template&lt;typename _CharT&gt; const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::scan_is (mask__m, const <code>char_type</code> *__lo, const <code>char_type</code> *__hi) const [inline]</h3>
<p>Find char_type matching a mask. This function searches for and returns the first char_type c in [lo,hi) for which is(m,c) is true. It does so by returning ctype&lt;char_type&gt;::do_scan_is(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__m</i> The mask to compare against.<br />
 <i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Pointer to matching char_type if found, else <i>__hi</i>.</dl>
<p> Definition at line 195 of file locale_facets.h.</p>
<h3>template&lt;typename _CharT&gt; const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::scan_not (mask__m, const <code>char_type</code> *__lo, const <code>char_type</code> *__hi) const [inline]</h3>
<p>Find char_type not matching a mask. This function searches for and returns the first char_type c in [lo,hi) for which is(m,c) is false. It does so by returning ctype&lt;char_type&gt;::do_scan_not(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__m</i> The mask to compare against.<br />
 <i>__lo</i> Pointer to first char in range.<br />
 <i>__hi</i> Pointer to end of range.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Pointer to non-matching char if found, else <i>__hi</i>.</dl>
<p> Definition at line 211 of file locale_facets.h.</p>
<h3>template&lt;typename _CharT&gt; <code>char_type</code> <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::tolower (<code>char_type</code>__c) const [inline]</h3>
<p>Convert to lowercase. This function converts the argument to lowercase if possible. If not possible (for example, &#8216;2&#8217;), returns the argument. It does so by returning ctype&lt;char_type&gt;::do_tolower(c). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char_type to convert.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The lowercase char_type if convertible, else <i>__c</i>.</dl>
<p> Definition at line 254 of file locale_facets.h.</p>
<h3>template&lt;typename _CharT&gt; const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::tolower (<code>char_type</code> *__lo, const <code>char_type</code> *__hi) const [inline]</h3>
<p>Convert array to lowercase. This function converts each char_type in the range [__lo,__hi) to lowercase if possible. Other elements remain untouched. It does so by returning ctype&lt;char_type&gt;:: do_tolower(__lo, __hi). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Definition at line 269 of file locale_facets.h.</p>
<h3>template&lt;typename _CharT&gt; <code>char_type</code> <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::toupper (<code>char_type</code>__c) const [inline]</h3>
<p>Convert to uppercase. This function converts the argument to uppercase if possible. If not possible (for example, &#8216;2&#8217;), returns the argument. It does so by returning ctype&lt;char_type&gt;::do_toupper(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char_type to convert.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The uppercase char_type if convertible, else <i>__c</i>.</dl>
<p> Definition at line 225 of file locale_facets.h.</p>
<h3>template&lt;typename _CharT&gt; const <code>char_type</code>* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::toupper (<code>char_type</code> *__lo, const <code>char_type</code> *__hi) const [inline]</h3>
<p>Convert array to uppercase. This function converts each char_type in the range [lo,hi) to uppercase if possible. Other elements remain untouched. It does so by returning ctype&lt;char_type&gt;:: do_toupper(lo, hi). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Definition at line 240 of file locale_facets.h.</p>
<h3>template&lt;typename _CharT&gt; <code>char_type</code> <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::widen (char__c) const [inline]</h3>
<p>Widen char to char_type. This function converts the char argument to char_type using the simplest reasonable transformation. It does so by returning ctype&lt;char_type&gt;::do_widen(c). </p>
<p> Note: this is not what you want for codepage conversions. See codecvt for that. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__c</i> The char to convert.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The converted char_type.</dl>
<p> Definition at line 286 of file locale_facets.h. </p>
<p> Referenced by std::money_get&lt; _CharT, _InIter &gt;::do_get(), std::time_put&lt; _CharT, _OutIter &gt;::do_put(), std::money_put&lt; _CharT, _OutIter &gt;::do_put(), std::tr2::operator&lt;&lt;(), and std::operator&lt;&lt;().</p>
<h3>template&lt;typename _CharT&gt; const char* <code>std::__ctype_abstract_base</code>&lt; _CharT &gt;::widen (const char *__lo, const char *__hi, <code>char_type</code> *__to) const [inline]</h3>
<p>Widen array to char_type. This function converts each char in the input to char_type using the simplest reasonable transformation. It does so by returning ctype&lt;char_type&gt;::do_widen(c). </p>
<p> Note: this is not what you want for codepage conversions. See codecvt for that. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__lo</i> Pointer to start of range.<br />
 <i>__hi</i> Pointer to end of range.<br />
 <i>__to</i> Pointer to the destination array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd><i>__hi</i>.</dl>
<p> Definition at line 305 of file locale_facets.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
