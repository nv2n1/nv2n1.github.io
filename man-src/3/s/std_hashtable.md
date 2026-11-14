---
title: "std_hashtable(3)"
name: "std_hashtable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_hashtable/"
description: "std::_Hashtable< _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits > –"
---

<p>std::_Hashtable&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_Hashtable_base&lt; _Key, _Value, _ExtractKey, _Equal, _H1, _H2, _Hash, _Traits &gt;</code>, <code>std::__detail::_Map_base&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;</code>, <code>std::__detail::_Insert&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;</code>, <code>std::__detail::_Rehash_base&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;</code>, and <code>std::__detail::_Equality&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;</code>.</p>
<h3>Public Types</h3>
<pre><code>typedef _Alloc allocator_type



using const_iterator = typename __hashtable_base::const_iterator



using const_local_iterator = typename __hashtable_base::const_local_iterator



typedef _Alloc::const_pointer const_pointer



typedef _Alloc::const_reference const_reference



using difference_type = typename __hashtable_base::difference_type



using iterator = typename __hashtable_base::iterator



typedef _Equal key_equal



typedef _Key key_type



using local_iterator = typename __hashtable_base::local_iterator



typedef _Alloc::pointer pointer



typedef _Alloc::reference reference



using size_type = typename __hashtable_base::size_type



typedef _Value value_type



Public Member Functions
_Hashtable (size_type __bucket_hint, const _H1 &amp;, const _H2 &amp;, const _Hash &amp;, const _Equal &amp;, const _ExtractKey &amp;, const allocator_type &amp;)



template&lt;typename _InputIterator &gt; _Hashtable (_InputIterator __first, _InputIterator __last, size_type __bucket_hint, const _H1 &amp;, const _H2 &amp;, const _Hash &amp;, const _Equal &amp;, const _ExtractKey &amp;, const allocator_type &amp;)



_Hashtable (const _Hashtable &amp;)



_Hashtable (_Hashtable &amp;&amp;)



_Hashtable (size_type __n=10, const _H1 &amp;__hf=_H1(), const key_equal &amp;__eql=key_equal(), const allocator_type &amp;__a=allocator_type())



template&lt;typename _InputIterator &gt; _Hashtable (_InputIterator __f, _InputIterator __l, size_type __n=0, const _H1 &amp;__hf=_H1(), const key_equal &amp;__eql=key_equal(), const allocator_type &amp;__a=allocator_type())



_Hashtable (initializer_list&lt; value_type &gt; __l, size_type __n=0, const _H1 &amp;__hf=_H1(), const key_equal &amp;__eql=key_equal(), const allocator_type &amp;__a=allocator_type())



const _RehashPolicy &amp; __rehash_policy () const



void __rehash_policy (const _RehashPolicy &amp;)



template&lt;typename... _Args&gt; _Hashtable&lt; _Key, _Value,


_Alloc, _ExtractKey, _Equal,

_H1, _H2, _Hash, _RehashPolicy,

_Traits &gt;::__node_type * _M_allocate_node (_Args &amp;&amp;...__args)&quot;


template&lt;typename... _Args&gt; std::pair&lt; typename _Hashtable


&lt; _Key, _Value, _Alloc,

_ExtractKey, _Equal, _H1, _H2,

_Hash, _RehashPolicy, _Traits &gt;

::iterator, bool &gt; _M_emplace (std::true_type, _Args &amp;&amp;...__args)&quot;


template&lt;typename... _Args&gt; _Hashtable&lt; _Key, _Value,


_Alloc, _ExtractKey, _Equal,

_H1, _H2, _Hash, _RehashPolicy,

_Traits &gt;::iterator _M_emplace (std::false_type, _Args &amp;&amp;...__args)&quot;


template&lt;typename _Arg &gt; std::pair&lt; typename _Hashtable


&lt; _Key, _Value, _Alloc,

_ExtractKey, _Equal, _H1, _H2,

_Hash, _RehashPolicy, _Traits &gt;

::iterator, bool &gt; _M_insert (_Arg &amp;&amp;__v, std::true_type)&quot;


template&lt;typename _Arg &gt; _Hashtable&lt; _Key, _Value,


_Alloc, _ExtractKey, _Equal,

_H1, _H2, _Hash, _RehashPolicy,

_Traits &gt;::iterator _M_insert (_Arg &amp;&amp;__v, std::false_type)&quot;


iterator begin () noexcept



const_iterator begin () const noexcept



local_iterator begin (size_type __n)



const_local_iterator begin (size_type __n) const



size_type bucket (const key_type &amp;__k) const



size_type bucket_count () const noexcept



size_type bucket_size (size_type __n) const



const_iterator cbegin () const noexcept



const_local_iterator cbegin (size_type __n) const



const_iterator cend () const noexcept



const_local_iterator cend (size_type __n) const



void clear () noexcept



size_type count (const key_type &amp;__k) const



template&lt;typename... _Args&gt; __ireturn_type emplace (_Args &amp;&amp;...__args)



template&lt;typename... _Args&gt; iterator emplace_hint (const_iterator, _Args &amp;&amp;...__args)



bool empty () const noexcept



iterator end () noexcept



const_iterator end () const noexcept



local_iterator end (size_type __n)



const_local_iterator end (size_type __n) const



std::pair&lt; iterator, iterator &gt; equal_range (const key_type &amp;__k)



std::pair&lt; const_iterator,


const_iterator &gt; equal_range (const key_type &amp;__k) const &quot;


iterator erase (const_iterator)



iterator erase (iterator __it)



size_type erase (const key_type &amp;__k)



iterator erase (const_iterator, const_iterator)



iterator find (const key_type &amp;__k)



const_iterator find (const key_type &amp;__k) const



allocator_type get_allocator () const noexcept



key_equal key_eq () const



float load_factor () const noexcept



size_type max_bucket_count () const noexcept



size_type max_size () const noexcept



_Hashtable &amp; operator= (const _Hashtable &amp;__ht)



_Hashtable &amp; operator= (_Hashtable &amp;&amp;__ht)



_Hashtable &amp; operator= (initializer_list&lt; value_type &gt; __l)



void rehash (size_type __n)



size_type size () const noexcept



void swap (_Hashtable &amp;)



Protected Member Functions</code></pre>
<p> size_type <code>_M_bucket_index</code> (__node_type *__n) const </p>
<p> size_type <code>_M_bucket_index</code> (const key_type &amp;__k, __hash_code __c) const </p>
<p> template&lt;typename&#8230; _Args&gt; <code>std::pair</code>&lt; iterator, bool &gt; <code>_M_emplace</code> (<code>std::true_type</code>, _Args &amp;&amp;&#8230;__args) </p>
<p> template&lt;typename&#8230; _Args&gt; iterator <code>_M_emplace</code> (<code>std::false_type</code>, _Args &amp;&amp;&#8230;__args) </p>
<p> const _Equal &amp; <code>_M_eq</code> () const </p>
<p> _Equal &amp; <code>_M_eq</code> () </p>
<p> bool <code>_M_equals</code> (const _Key &amp;__k, __hash_code __c, __node_type *__n) const </p>
<p> size_type <code>_M_erase</code> (<code>std::true_type</code>, const key_type &amp;) </p>
<p> size_type <code>_M_erase</code> (<code>std::false_type</code>, const key_type &amp;) </p>
<p> iterator <code>_M_erase</code> (size_type __bkt, __node_base *__prev_n, __node_type *__n) </p>
<p> __node_base * <code>_M_find_before_node</code> (size_type, const key_type &amp;, __hash_code) const </p>
<p> __node_type * <code>_M_find_node</code> (size_type __bkt, const key_type &amp;__key, __hash_code __c) const </p>
<p> __node_base * <code>_M_get_previous_node</code> (size_type __bkt, __node_base *__n) </p>
<p> template&lt;typename _Arg &gt; <code>std::pair</code>&lt; iterator, bool &gt; <code>_M_insert</code> (_Arg &amp;&amp;, <code>std::true_type</code>) </p>
<p> template&lt;typename _Arg &gt; iterator <code>_M_insert</code> (_Arg &amp;&amp;, <code>std::false_type</code>) </p>
<p> void <code>_M_insert_bucket_begin</code> (size_type, __node_type *) </p>
<p> iterator <code>_M_insert_multi_node</code> (__hash_code __code, __node_type *__n) </p>
<p> iterator <code>_M_insert_unique_node</code> (size_type __bkt, __hash_code __code, __node_type *__n) </p>
<p> void <code>_M_remove_bucket_begin</code> (size_type __bkt, __node_type *__next_n, size_type __next_bkt) </p>
<p> void <code>_M_swap</code> (_Hashtable_base &amp;__x)</p>
<h3>Friends</h3>
<p>template&lt;typename _Keya , typename _Valuea , typename _Alloca , typename _ExtractKeya , typename _Equala , typename _H1a , typename _H2a , typename _Hasha , typename _RehashPolicya , typename _Traitsa , bool _Constant_iteratorsa, bool _Unique_keysa&gt; struct <code>__detail::_Insert</code> </p>
<p> template&lt;typename _Keya , typename _Valuea , typename _Alloca , typename _ExtractKeya , typename _Equala , typename _H1a , typename _H2a , typename _Hasha , typename _RehashPolicya , typename _Traitsa &gt; struct <code>__detail::_Insert_base</code> </p>
<p> template&lt;typename _Keya , typename _Valuea , typename _Alloca , typename _ExtractKeya , typename _Equala , typename _H1a , typename _H2a , typename _Hasha , typename _RehashPolicya , typename _Traitsa , bool _Unique_keysa&gt; struct <code>__detail::_Map_base</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Key, typename _Value, typename _Alloc, typename _ExtractKey, typename _Equal, typename _H1, typename _H2, typename _Hash, typename _RehashPolicy, typename _Traits&gt;class std::_Hashtable&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;</h3>
<p>Primary class template _Hashtable. </p>
<p> <code>Template Parameters:</code></p>
<dl>
<dd><i>_Value</i> CopyConstructible type.<br />
 <i>_Key</i> CopyConstructible type.<br />
 <i>_Alloc</i> An allocator type ([lib.allocator.requirements]) whose _Alloc::value_type is _Value. As a conforming extension, we allow for _Alloc::value_type != _Value.<br />
 <i>_ExtractKey</i> Function object that takes an object of type _Value and returns a value of type _Key.<br />
 <i>_Equal</i> Function object that takes two objects of type k and returns a bool-like value that is true if the two objects are considered equal.<br />
 <i>_H1</i> The hash function. A unary function object with argument type _Key and result type size_t. Return values should be distributed over the entire range [0, numeric_limits&lt;size_t&gt;:max()].<br />
 <i>_H2</i> The range-hashing function (in the terminology of Tavori and Dreizin). A binary function object whose argument types and result type are all size_t. Given arguments r and N, the return value is in the range [0, N).<br />
 <i>_Hash</i> The ranged hash function (Tavori and Dreizin). A binary function whose argument types are _Key and size_t and whose result type is size_t. Given arguments k and N, the return value is in the range [0, N). Default: hash(k, N) = h2(h1(k), N). If _Hash is anything other than the default, _H1 and _H2 are ignored.<br />
 <i>_RehashPolicy</i> Policy class with three members, all of which govern the bucket count. <a href="/docs/linux/man/n-_m_next_bkt/">_M_next_bkt</a>(n) returns a bucket count no smaller than n. <a href="/docs/linux/man/n-_m_bkt_for_elements/">_M_bkt_for_elements</a>(n) returns a bucket count appropriate for an element count of n. _M_need_rehash(n_bkt, n_elt, n_ins) determines whether, if the current bucket count is n_bkt and the current element count is n_elt, we need to increase the bucket count. If so, returns make_pair(true, n), where n is the new bucket count. If not, returns make_pair(false, &lt;anything&gt;)<br />
 <i>_Traits</i> Compile-time class with three boolean std::integral_constant members: __cache_hash_code, __constant_iterators, __unique_keys.</dl>
<p> Each _Hashtable data structure has: </p>
<dl>
<dt>&bull;</p>
<dd>_Bucket[] _M_buckets</p>
<dt>&bull;</p>
<dd>_Hash_node_base _M_bbegin</p>
<dt>&bull;</p>
<dd>size_type _M_bucket_count</p>
<dt>&bull;</p>
<dd>size_type _M_element_count</dl>
<p> with _Bucket being _Hash_node* and _Hash_node containing: </p>
<dl>
<dt>&bull;</p>
<dd>_Hash_node* _M_next</p>
<dt>&bull;</p>
<dd>Tp _M_value</p>
<dt>&bull;</p>
<dd>size_t _M_hash_code if cache_hash_code is true</dl>
<p> In terms of Standard containers the hashtable is like the aggregation of: </p>
<dl>
<dt>&bull;</p>
<dd>std::forward_list&lt;_Node&gt; containing the elements</p>
<dt>&bull;</p>
<dd>std::vector&lt;std::forward_list&lt;_Node&gt;::iterator&gt; representing the buckets</dl>
<p> The non-empty buckets contain the node before the first node in the bucket. This design makes it possible to implement something like a std::forward_list::insert_after on container insertion and std::forward_list::erase_after on container erase calls. _M_before_begin is equivalent to std::forward_list::before_begin. Empty buckets contain nullptr. Note that one of the non-empty buckets contains &amp;_M_before_begin which is not a dereferenceable node so the node pointer in a bucket shall never be dereferenced, only its next node can be. </p>
<p> Walking through a bucket&#8217;s nodes requires a check on the hash code to see if each node is still in the bucket. Such a design assumes a quite efficient hash functor and is one of the reasons it is highly advisable to set __cache_hash_code to true. </p>
<p> The container iterators are simply built from nodes. This way incrementing the iterator is perfectly efficient independent of how many empty buckets there are in the container. </p>
<p> On insert we compute the element&#8217;s hash code and use it to find the bucket index. If the element must be inserted in an empty bucket we add it at the beginning of the singly linked list and make the bucket point to _M_before_begin. The bucket that used to point to _M_before_begin, if any, is updated to point to its new before begin node. </p>
<p> On erase, the simple iterator design requires using the hash functor to get the index of the bucket to update. For this reason, when __cache_hash_code is set to false the hash functor must not throw and this is enforced by a static assertion. </p>
<p> Functionality is implemented by decomposition into base classes, where the derived _Hashtable class is used in _Map_base, _Insert, _Rehash_base, and _Equality base classes to access the &#8216;this&#8217; pointer. _Hashtable_base is used in the base classes as a non-recursive, fully-completed-type so that detailed nested type information, such as iterator type and node type, can be used. This is similar to the &#8216;Curiously Recurring Template Pattern&#8217; (CRTP) technique, but uses a reconstructed, not explicitly passed, template pattern. </p>
<p> Base class templates are:</p>
<dl>
<dt>&bull;</p>
<dd>__detail::_Hashtable_base</p>
<dt>&bull;</p>
<dd>__detail::_Map_base</p>
<dt>&bull;</p>
<dd>__detail::_Insert</p>
<dt>&bull;</p>
<dd>__detail::_Rehash_base</p>
<dt>&bull;</p>
<dd>__detail::_Equality</dl>
<p> Definition at line 174 of file bits/hashtable.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
