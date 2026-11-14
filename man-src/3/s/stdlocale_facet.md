---
title: "stdlocale_facet(3)"
name: "stdlocale_facet"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocale_facet/"
description: "std::locale::facet –"
---

<p>std::locale::facet &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::__codecvt_abstract_base&lt; _InternT, _ExternT, encoding_state &gt;</code>, <code>std::__codecvt_abstract_base&lt; char, char, mbstate_t &gt;</code>, <code>std::__codecvt_abstract_base&lt; wchar_t, char, mbstate_t &gt;</code>, <code>std::__ctype_abstract_base&lt; wchar_t &gt;</code>, <code>std::__codecvt_abstract_base&lt; _InternT, _ExternT, _StateT &gt;</code>, <code>std::__ctype_abstract_base&lt; _CharT &gt;</code>, std::__moneypunct_cache&lt; _CharT, _Intl &gt;, std::__numpunct_cache&lt; _CharT &gt;, std::__timepunct&lt; _CharT &gt;, std::__timepunct_cache&lt; _CharT &gt;, <code>std::collate&lt; _CharT &gt;</code>, <code>std::ctype&lt; char &gt;</code>, <code>std::messages&lt; _CharT &gt;</code>, <code>std::money_get&lt; _CharT, _InIter &gt;</code>, <code>std::money_put&lt; _CharT, _OutIter &gt;</code>, <code>std::moneypunct&lt; _CharT, _Intl &gt;</code>, <code>std::num_get&lt; _CharT, _InIter &gt;</code>, <code>std::num_put&lt; _CharT, _OutIter &gt;</code>, <code>std::numpunct&lt; _CharT &gt;</code>, <code>std::time_get&lt; _CharT, _InIter &gt;</code>, and <code>std::time_put&lt; _CharT, _OutIter &gt;</code>.</p>
<h3>Protected Member Functions</h3>
<pre><code>facet (size_t __refs=0)  throw ()



virtual ~facet ()



Static Protected Member Functions
static __c_locale _S_clone_c_locale (__c_locale &amp;__cloc)  throw ()



static void _S_create_c_locale (__c_locale &amp;__cloc, const char *__s, __c_locale __old=0)



static void _S_destroy_c_locale (__c_locale &amp;__cloc)



static __c_locale _S_get_c_locale ()



static const char * _S_get_c_name ()  throw ()



static __c_locale _S_lc_ctype_c_locale (__c_locale __cloc, const char *__s)



Friends</code></pre>
<p> class <code>locale</code> </p>
<p> class <code>locale::_Impl</code></p>
<h2>Detailed Description</h2>
<p>Localization functionality base class. </p>
<p> The facet class is the base class for a localization feature, such as money, time, and number printing. It provides common support for facets and reference management. </p>
<p> Facets may not be copied or assigned. </p>
<p> Definition at line 338 of file locale_classes.h.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>std::locale::facet::facet (size_t__refs = 0) [inline], [explicit], [protected]</h3>
<p>Facet constructor. This is the constructor provided by the standard. If refs is 0, the facet is destroyed when the last referencing locale is destroyed. Otherwise the facet will never be destroyed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__refs</i> The initial value for reference count.</dl>
<p> Definition at line 370 of file locale_classes.h.</p>
<h3>virtual std::locale::facet::~facet () [protected], [virtual]</h3>
<p>Facet destructor.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
