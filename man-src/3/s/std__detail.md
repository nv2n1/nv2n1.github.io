---
title: "std__detail(3)"
name: "std__detail"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail/"
description: "std::__detail –"
---

<p>std::__detail &#8211;</p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>_Automaton</code> </p>
<p> struct <code>_Before_begin</code> </p>
<p> struct <code>_CharMatcher</code> </p>
<p> class <code>_Compiler</code> </p>
<p> struct <code>_Default_ranged_hash</code> </p>
<p> struct <code>_EndTagger</code> </p>
<p> struct <code>_Equal_helper</code> </p>
<p> struct <code>_Equal_helper&lt; _Key, _Value, _ExtractKey, _Equal, _HashCodeType, false &gt;</code> </p>
<p> struct <code>_Equal_helper&lt; _Key, _Value, _ExtractKey, _Equal, _HashCodeType, true &gt;</code> </p>
<p> struct <code>_Equality</code> </p>
<p> struct <code>_Equality&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, false &gt;</code> </p>
<p> struct <code>_Equality&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, true &gt;</code> </p>
<p> struct <code>_Equality_base</code> </p>
<p> class <code>_Grep_matcher</code> </p>
<p> struct <code>_Hash_code_base</code> </p>
<p> struct <code>_Hash_code_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Default_ranged_hash, false &gt;</code> </p>
<p> struct <code>_Hash_code_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Default_ranged_hash, true &gt;</code> </p>
<p> struct <code>_Hash_code_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, false &gt;</code> </p>
<p> struct <code>_Hash_node</code> </p>
<p> struct <code>_Hash_node&lt; _Value, false &gt;</code> </p>
<p> struct <code>_Hash_node&lt; _Value, true &gt;</code> </p>
<p> struct <code>_Hash_node_base</code> </p>
<p> struct <code>_Hashtable_base</code> </p>
<p> struct <code>_Hashtable_ebo_helper</code> </p>
<p> struct <code>_Hashtable_ebo_helper&lt; _Nm, _Tp, false &gt;</code> </p>
<p> struct <code>_Hashtable_ebo_helper&lt; _Nm, _Tp, true &gt;</code> </p>
<p> struct <code>_Hashtable_traits</code> </p>
<p> struct <code>_Insert</code> </p>
<p> struct <code>_Insert&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, false, _Unique_keys &gt;</code> </p>
<p> struct <code>_Insert&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, true, false &gt;</code> </p>
<p> struct <code>_Insert&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, true, true &gt;</code> </p>
<p> struct <code>_Insert_base</code> </p>
<p> struct <code>_List_node_base</code> </p>
<p> struct <code>_Local_const_iterator</code> </p>
<p> struct <code>_Local_iterator</code> </p>
<p> struct <code>_Local_iterator_base</code> </p>
<p> struct <code>_Local_iterator_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, false &gt;</code> </p>
<p> struct <code>_Local_iterator_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, true &gt;</code> </p>
<p> struct <code>_Map_base</code> </p>
<p> struct <code>_Map_base&lt; _Key, _Pair, _Alloc, _Select1st, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, false &gt;</code> </p>
<p> struct <code>_Map_base&lt; _Key, _Pair, _Alloc, _Select1st, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, true &gt;</code> </p>
<p> struct <code>_Mod_range_hashing</code> </p>
<p> class <code>_Nfa</code> </p>
<p> struct <code>_Node_const_iterator</code> </p>
<p> struct <code>_Node_iterator</code> </p>
<p> struct <code>_Node_iterator_base</code> </p>
<p> struct <code>_PatternCursor</code> </p>
<p> struct <code>_Prime_rehash_policy</code> </p>
<p> struct <code>_RangeMatcher</code> </p>
<p> struct <code>_Rehash_base</code> </p>
<p> struct <code>_Rehash_base&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _Prime_rehash_policy, _Traits &gt;</code> </p>
<p> struct <code>_Results</code> </p>
<p> class <code>_Scanner</code> </p>
<p> struct <code>_Scanner_base</code> </p>
<p> class <code>_SpecializedCursor</code> </p>
<p> class <code>_SpecializedResults</code> </p>
<p> struct <code>_StartTagger</code> </p>
<p> struct <code>_State</code> </p>
<p> class <code>_StateSeq</code></p>
<h3>Typedefs</h3>
<p>typedef <code>std::shared_ptr</code><br />
 &lt; <code>_Automaton</code> &gt; <code>_AutomatonPtr</code>&quot; </p>
<p> typedef std::function&lt; bool(const<br />
 <code>_PatternCursor</code> &amp;)&gt; <code>_Matcher</code>&quot; </p>
<p> typedef int <code>_StateIdT</code> </p>
<p> typedef <code>std::set</code>&lt; <code>_StateIdT</code> &gt; <code>_StateSet</code> </p>
<p> typedef <code>std::stack</code>&lt; <code>_StateIdT</code>,<br />
 <code>std::vector</code>&lt; <code>_StateIdT</code> &gt; &gt; <code>_StateStack</code>&quot; </p>
<p> typedef std::function&lt; void(const<br />
 <code>_PatternCursor</code> &amp;, <code>_Results</code> &amp;)&gt; <code>_Tagger</code>&quot;</p>
<h3>Enumerations</h3>
<p>enum <code>_Opcode</code> { <code>_S_opcode_unknown</code>, <code>_S_opcode_alternative</code>, <code>_S_opcode_subexpr_begin</code>, <code>_S_opcode_subexpr_end</code>, <code>_S_opcode_match</code>, <code>_S_opcode_accept</code> }</p>
<h3>Functions</h3>
<p>template&lt;typename _InIter , typename _TraitsT &gt; <code>_AutomatonPtr</code> <code>__compile</code> (const _InIter &amp;__b, const _InIter &amp;__e, _TraitsT &amp;__t, <code>regex_constants::syntax_option_type</code> __f) </p>
<p> template&lt;typename _FwdIterT &gt; <code>_SpecializedCursor</code>&lt; _FwdIterT &gt; <code>__cursor</code> (const _FwdIterT &amp;__b, const _FwdIterT __e) </p>
<p> template&lt;class _Iterator &gt; std::iterator_traits<br />
 &lt; _Iterator &gt;::difference_type <code>__distance_fw</code> (_Iterator __first, _Iterator __last, <code>std::input_iterator_tag</code>)&quot; </p>
<p> template&lt;class _Iterator &gt; std::iterator_traits<br />
 &lt; _Iterator &gt;::difference_type <code>__distance_fw</code> (_Iterator __first, _Iterator __last, <code>std::forward_iterator_tag</code>)&quot; </p>
<p> template&lt;class _Iterator &gt; std::iterator_traits<br />
 &lt; _Iterator &gt;::difference_type <code>__distance_fw</code> (_Iterator __first, _Iterator __last)&quot; </p>
<p> template&lt;typename _InputIterator , typename _OutputIterator , typename _Tp &gt; _OutputIterator <code>__normalize</code> (_InputIterator __first, _InputIterator __last, _OutputIterator __result, const _Tp &amp;__factor) </p>
<p> bool <code>_AnyMatcher</code> (const <code>_PatternCursor</code> &amp;) </p>
<p> template&lt;typename _Value , bool _Cache_hash_code&gt; bool <code>operator!=</code> (const <code>_Node_iterator_base</code>&lt; _Value, _Cache_hash_code &gt; &amp;__x, const <code>_Node_iterator_base</code>&lt; _Value, _Cache_hash_code &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Value , typename _ExtractKey , typename _H1 , typename _H2 , typename _Hash , bool __cache&gt; bool <code>operator!=</code> (const <code>_Local_iterator_base</code>&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __cache &gt; &amp;__x, const <code>_Local_iterator_base</code>&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __cache &gt; &amp;__y) </p>
<p> template&lt;typename _Value , bool _Cache_hash_code&gt; bool <code>operator==</code> (const <code>_Node_iterator_base</code>&lt; _Value, _Cache_hash_code &gt; &amp;__x, const <code>_Node_iterator_base</code>&lt; _Value, _Cache_hash_code &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Value , typename _ExtractKey , typename _H1 , typename _H2 , typename _Hash , bool __cache&gt; bool <code>operator==</code> (const <code>_Local_iterator_base</code>&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __cache &gt; &amp;__x, const <code>_Local_iterator_base</code>&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __cache &gt; &amp;__y)</p>
<h3>Variables</h3>
<pre><code>static const _StateIdT _S_invalid_state_id</code></pre>
<h2>Detailed Description</h2>
<p>Implementation details not part of the namespace std interface.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
