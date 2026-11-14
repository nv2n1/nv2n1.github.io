---
title: "stdtr2dynamic_bitset(3)"
name: "stdtr2dynamic_bitset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtr2dynamic_bitset/"
description: "std::tr2::dynamic_bitset< _WordT, _Alloc > –"
---

<p>std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::tr2::__dynamic_bitset_base&lt; _WordT, _Alloc &gt;</code>.</p>
<h3>Classes</h3>
<p>class <code>reference</code></p>
<h3>Public Types</h3>
<p>typedef <code>__dynamic_bitset_base</code><br />
 &lt; _WordT, _Alloc &gt; <code>_Base</code>&quot; </p>
<p> typedef _Alloc <code>allocator_type</code> </p>
<p> typedef _WordT <code>block_type</code> </p>
<p> typedef bool <code>const_reference</code> </p>
<p> typedef size_t <code>size_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>dynamic_bitset (size_type __nbits, unsigned long long __val=0ULL, const allocator_type &amp;__alloc=allocator_type())



dynamic_bitset (initializer_list&lt; block_type &gt; __il, const allocator_type &amp;__alloc=allocator_type())



template&lt;typename _CharT , typename _Traits , typename _Alloc1 &gt; dynamic_bitset (const std::basic_string&lt; _CharT, _Traits, _Alloc1 &gt; &amp;__str, typename basic_string&lt; _CharT, _Traits, _Alloc1 &gt;::size_type __pos=0, typename basic_string&lt; _CharT, _Traits, _Alloc1 &gt;::size_type __n=std::basic_string&lt; _CharT, _Traits, _Alloc1 &gt;::npos, _CharT __zero=_CharT('0'), _CharT __one=_CharT('1'), const allocator_type &amp;__alloc=allocator_type())



dynamic_bitset (const char *__str, const allocator_type &amp;__alloc=allocator_type())



dynamic_bitset (const dynamic_bitset &amp;__b)



dynamic_bitset (dynamic_bitset &amp;&amp;__b)



template&lt;typename _CharT , typename _Traits &gt; void _M_copy_from_ptr (const _CharT *, size_t, size_t, size_t, _CharT, _CharT)



template&lt;typename _CharT , typename _Traits , typename _Alloc1 &gt; void _M_copy_from_string (const std::basic_string&lt; _CharT, _Traits, _Alloc1 &gt; &amp;__str, size_t __pos, size_t __n, _CharT __zero=_CharT('0'), _CharT __one=_CharT('1'))



template&lt;typename _CharT , typename _Traits , typename _Alloc1 &gt; void _M_copy_to_string (std::basic_string&lt; _CharT, _Traits, _Alloc1 &gt; &amp;__str, _CharT __zero=_CharT('0'), _CharT __one=_CharT('1')) const



_M_Nb (0)



bool all () const



bool any () const



void append (block_type __block)



void append (initializer_list&lt; block_type &gt; __il)



template&lt;typename _BlockInputIterator &gt; void append (_BlockInputIterator __first, _BlockInputIterator __last)



void clear ()



size_type count () const noexcept



bool empty () const noexcept



size_type find_first () const



size_type find_next (size_t __prev) const



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; flip ()



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; flip (size_type __pos)



allocator_type get_allocator () const



bool is_proper_subset_of (const dynamic_bitset &amp;__b) const



bool is_subset_of (const dynamic_bitset &amp;__b) const



constexpr size_type max_size () noexcept



bool none () const



size_type num_blocks () const noexcept



dynamic_bitset &amp; operator= (const dynamic_bitset &amp;__b)



dynamic_bitset &amp; operator= (dynamic_bitset &amp;&amp;__b)



dynamic_bitset&lt; _WordT, _Alloc &gt; operator~ () const



void push_back (bool __bit)



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; reset ()



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; reset (size_type __pos)



void resize (size_type __nbits, bool __value=false)



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; set ()



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; set (size_type __pos, bool __val=true)



size_type size () const noexcept



void swap (dynamic_bitset &amp;__b)



bool test (size_type __pos) const



template&lt;typename _CharT  = char, typename _Traits  = std::char_traits&lt;_CharT&gt;, typename _Alloc1  = std::allocator&lt;_CharT&gt;&gt; std::basic_string&lt; _CharT,


_Traits, _Alloc1 &gt; to_string (_CharT __zero=_CharT('0'), _CharT __one=_CharT('1')) const &quot;


unsigned long long to_ullong () const



unsigned long to_ulong () const

dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; operator&amp;= (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; operator&amp;= (dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;&amp;__rhs)



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; operator|= (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; operator^= (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)



dynamic_bitset&lt; _WordT, _Alloc &gt; &amp; operator-= (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)
</code></pre>
<p> <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp; <code>operator&lt;&lt;=</code> (size_type __pos) </p>
<p> <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp; <code>operator&gt;&gt;=</code> (size_type __pos) </p>
<p> <code>reference</code> <code>operator[]</code> (size_type __pos) </p>
<p> const_reference <code>operator[]</code> (size_type __pos) const </p>
<p> <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; <code>operator&lt;&lt;</code> (size_type __pos) const </p>
<p> <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; <code>operator&gt;&gt;</code> (size_type __pos) const</p>
<h3>Public Attributes</h3>
<p><code>__pad0__</code>: <code>_Base</code>(__alloc)</p>
<h3>Static Public Attributes</h3>
<p>static const size_type bits_per_block</p>
<p>static const size_type npos</p>
<p>Private Member Functions<br />
size_t _M_are_all_aux () const</p>
<p>void _M_assign (const __dynamic_bitset_base &amp;__b)</p>
<p>void _M_clear ()</p>
<p>void _M_do_and (const __dynamic_bitset_base &amp;__x)</p>
<p>void _M_do_append_block (block_type __block, size_type __pos)</p>
<p>size_t _M_do_count () const</p>
<p>void _M_do_dif (const __dynamic_bitset_base &amp;__x)</p>
<p>size_type _M_do_find_first (size_t __not_found) const</p>
<p>size_type _M_do_find_next (size_t __prev, size_t __not_found) const</p>
<p>void _M_do_flip ()</p>
<p>void _M_do_left_shift (size_t __shift)</p>
<p>void _M_do_or (const __dynamic_bitset_base &amp;__x)</p>
<p>void _M_do_reset ()</p>
<p>void _M_do_right_shift (size_t __shift)</p>
<p>void _M_do_set ()</p>
<p>unsigned long long _M_do_to_ullong () const</p>
<p>unsigned long _M_do_to_ulong () const</p>
<p>void _M_do_xor (const __dynamic_bitset_base &amp;__x)</p>
<p>allocator_type _M_get_allocator () const</p>
<p>block_type &amp; _M_getword (size_type __pos)</p>
<p>block_type _M_getword (size_type __pos) const</p>
<p>block_type &amp; _M_hiword ()</p>
<p>block_type _M_hiword () const</p>
<p>bool _M_is_any () const</p>
<p>bool _M_is_equal (const __dynamic_bitset_base &amp;__x) const</p>
<p>bool _M_is_less (const __dynamic_bitset_base &amp;__x) const</p>
<p>bool _M_is_proper_subset_of (const __dynamic_bitset_base &amp;__b) const</p>
<p>bool _M_is_subset_of (const __dynamic_bitset_base &amp;__b)</p>
<p>void _M_resize (size_t __nbits, bool __value)</p>
<p>size_type _M_size () const noexcept</p>
<p>void _M_swap (__dynamic_bitset_base &amp;__b)</p>
<p>Static Private Member Functions<br />
static block_type _S_maskbit (size_type __pos) noexcept</p>
<p>static size_type _S_whichbit (size_type __pos) noexcept</p>
<p>static size_type _S_whichbyte (size_type __pos) noexcept</p>
<p>static size_type _S_whichword (size_type __pos) noexcept</p>
<p>Private Attributes<br />
 <code>std::vector</code>&lt; block_type,<br />
 allocator_type &gt; <code>_M_w</code>&quot;</p>
<h3>Static Private Attributes</h3>
<pre><code>static const size_type _S_bits_per_block



Friends</code></pre>
<p> class <code>reference</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt;class std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;</h3>
<p>The dynamic_bitset class represents a sequence of bits. </p>
<p> (Note that dynamic_bitset does <i>not</i> meet the formal requirements of a container. Mainly, it lacks iterators.) </p>
<p> The template argument, <i>Nb</i>, may be any non-negative number, specifying the number of bits (e.g., &#8216;0&#8217;, &#8217;12&#8217;, &#8216;1024*1024&#8217;). </p>
<p> In the general unoptimized case, storage is allocated in word-sized blocks. Let B be the number of bits in a word, then (Nb+(B-1))/B words will be used for storage. B &#8211; NbB bits are unused. (They are the high-order bits in the highest word.) It is a class invariant that those unused bits are always zero. </p>
<p> If you think of dynamic_bitset as &#8216;a simple array of bits,&#8217; be aware that your mental picture is reversed: a dynamic_bitset behaves the same way as bits in integers do, with the bit at index 0 in the &#8216;least significant / right-hand&#8217; position, and the bit at index Nb-1 in the &#8216;most significant / left-hand&#8217; position. Thus, unlike other containers, a dynamic_bitset&#8217;s index &#8216;counts from right to left,&#8217; to put it very loosely. </p>
<p> This behavior is preserved when translating to and from strings. For example, the first line of the following program probably prints &#8216;b(&#8216;a&#8217;) is 0001100001&#8242; on a modern ASCII system. </p>
<pre>* #include &lt;dynamic_bitset&gt;
* #include &lt;iostream&gt;
* #include &lt;sstream&gt;
*
* using namespace std;
*
* int main()
* {
* long a = 'a';
* dynamic_bitset b(a);
*
* cout &lt;&lt; &quot;b('a') is &quot; &lt;&lt; b &lt;&lt; endl;
*
* ostringstream s;
* s &lt;&lt; b;
* string str = s.str();
* cout &lt;&lt; &quot;index 3 in the string is &quot; &lt;&lt; str[3] &lt;&lt; &quot; but
* &lt;&lt; &quot;index 3 in the bitset is &quot; &lt;&lt; b[3] &lt;&lt; endl;
* }
* </pre>
<p>Also see: <a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/libstdc++/manual/bk01pt12ch33s02.html">http://gcc.gnu.org/onlinedocs/libstdc++/manual/bk01pt12ch33s02.html</a> for a description of extensions. </p>
<p> Most of the actual code isn&#8217;t contained in dynamic_bitset&lt;&gt; itself, but in the base class __dynamic_bitset_base. The base class works with whole words, not with individual bits. This allows us to specialize __dynamic_bitset_base for the important special case where the dynamic_bitset is only a single word. </p>
<p> Extra confusion can result due to the fact that the storage for __dynamic_bitset_base <i>is</i> a vector, and is indexed as such. This is carefully encapsulated. </p>
<p> Definition at line 569 of file dynamic_bitset.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::<code>dynamic_bitset</code> (size_type__nbits, unsigned long long__val = 0ULL, const allocator_type &amp;__alloc = allocator_type()) [inline], [explicit]</h3>
<p>Initial bits bitwise-copied from a single word (others set to zero). </p>
<p> Definition at line 727 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; template&lt;typename _CharT , typename _Traits , typename _Alloc1 &gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::<code>dynamic_bitset</code> (const <code>std::basic_string</code>&lt; _CharT, _Traits, _Alloc1 &gt; &amp;__str, typename <code>basic_string</code>&lt; _CharT, _Traits, _Alloc1 &gt;::size_type__pos = 0, typename <code>basic_string</code>&lt; _CharT, _Traits, _Alloc1 &gt;::size_type__n = <code>std::basic_string</code>&lt;_CharT, _Traits, _Alloc1&gt;::npos, _CharT__zero = _CharT(&#8216;0&#8217;), _CharT__one = _CharT(&#8216;1&#8217;), const allocator_type &amp;__alloc = allocator_type()) [inline], [explicit]</h3>
<p>Use a subset of a string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__str</i> A string of &#8216;0&#8217; and &#8216;1&#8217; characters.<br />
 <i>__pos</i> Index of the first character in __str to use.<br />
 <i>__n</i> The number of characters to copy.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::out_of_range</i> If __pos is bigger the size of __str.<br />
 <i>std::invalid_argument</i> If a character appears in the string which is neither &#8216;0&#8217; nor &#8216;1&#8217;.</dl>
<p> Definition at line 749 of file dynamic_bitset. </p>
<p> References std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::resize(), and std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::size().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::<code>dynamic_bitset</code> (const char *__str, const allocator_type &amp;__alloc = allocator_type()) [inline], [explicit]</h3>
<p>Construct from a string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__str</i> A string of &#8216;0&#8217; and &#8216;1&#8217; characters.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::invalid_argument</i> If a character appears in the string which is neither &#8216;0&#8217; nor &#8216;1&#8217;.</dl>
<p> Definition at line 777 of file dynamic_bitset. </p>
<p> References std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::resize().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::<code>dynamic_bitset</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__b) [inline]</h3>
<p>Copy constructor. </p>
<p> Definition at line 793 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::<code>dynamic_bitset</code> (<code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;&amp;__b) [inline]</h3>
<p>Move constructor. </p>
<p> Definition at line 800 of file dynamic_bitset.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; bool <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::all () const [inline]</h3>
<p>Tests whether all the bits are on. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>True if all the bits are set.</dl>
<p> Definition at line 1187 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; bool <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::any () const [inline]</h3>
<p>Tests whether any of the bits are on. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>True if at least one bit is set.</dl>
<p> Definition at line 1195 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; void <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::append (block_type__block) [inline]</h3>
<p>Append a block. </p>
<p> Definition at line 881 of file dynamic_bitset. </p>
<p> Referenced by std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::append().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; template&lt;typename _BlockInputIterator &gt; void <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::append (_BlockInputIterator__first, _BlockInputIterator__last) [inline]</h3>
<p>Append an iterator range of blocks. </p>
<p> Definition at line 899 of file dynamic_bitset. </p>
<p> References std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::append().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; void <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::clear () [inline]</h3>
<p>Clear the bitset. </p>
<p> Definition at line 859 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; size_type <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::count () const [inline], [noexcept]</h3>
<p>Returns the number of bits which are set. </p>
<p> Definition at line 1143 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; bool <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::empty () const [inline], [noexcept]</h3>
<p>Returns true if the dynamic_bitset is empty. </p>
<p> Definition at line 1158 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; size_type <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::find_first () const [inline]</h3>
<p>Finds the index of the first &#8216;on&#8217; bit. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>The index of the first bit set, or size() if not found.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd>find_next</dl>
<p> Definition at line 1223 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; size_type <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::find_next (size_t__prev) const [inline]</h3>
<p>Finds the index of the next &#8216;on&#8217; bit after prev. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>The index of the next bit set, or size() if not found.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__prev</i> Where to start searching.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd>find_first</dl>
<p> Definition at line 1233 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::flip () [inline]</h3>
<p>Toggles every bit to its opposite value. </p>
<p> Definition at line 1038 of file dynamic_bitset. </p>
<p> Referenced by std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::operator~().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::flip (size_type__pos) [inline]</h3>
<p>Toggles a given bit to its opposite value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__pos</i> The index of the bit.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::out_of_range</i> If <i>__pos</i> is bigger the size of the set.</dl>
<p> Definition at line 1051 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; allocator_type <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::get_allocator () const [inline]</h3>
<p>Return the allocator for the bitset. </p>
<p> Definition at line 841 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; constexpr size_type <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::max_size () [inline], [noexcept]</h3>
<p>Returns the maximum size of a dynamic_bitset object having the same type as *this. The real answer is max() * bits_per_block but is likely to overflow. </p>
<p> Definition at line 1165 of file dynamic_bitset. </p>
<p> References std::numeric_limits&lt; _Tp &gt;::max().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; bool <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::none () const [inline]</h3>
<p>Tests whether any of the bits are on. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>True if none of the bits are set.</dl>
<p> Definition at line 1203 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; size_type <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::num_blocks () const [inline], [noexcept]</h3>
<p>Returns the total number of blocks. </p>
<p> Definition at line 1153 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator&amp;= (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) [inline]</h3>
<p>Operations on dynamic_bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__rhs</i> A same-sized dynamic_bitset.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 914 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator&amp;= (<code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;&amp;__rhs) [inline]</h3>
<p>Operations on dynamic_bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__rhs</i> A same-sized dynamic_bitset.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 921 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator-= (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) [inline]</h3>
<p>Operations on dynamic_bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__rhs</i> A same-sized dynamic_bitset.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 942 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator&lt;&lt; (size_type__pos) const [inline]</h3>
<p>Self-explanatory. </p>
<p> Definition at line 1209 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator&lt;&lt;= (size_type__pos) [inline]</h3>
<p>Operations on dynamic_bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__pos</i> The number of places to shift.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 957 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator= (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__b) [inline]</h3>
<p>Assignment. </p>
<p> Definition at line 818 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator= (<code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;&amp;__b) [inline]</h3>
<p>Move assignment. </p>
<p> Definition at line 831 of file dynamic_bitset. </p>
<p> References std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::swap().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator&gt;&gt; (size_type__pos) const [inline]</h3>
<p>Self-explanatory. </p>
<p> Definition at line 1213 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator&gt;&gt;= (size_type__pos) [inline]</h3>
<p>Operations on dynamic_bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__pos</i> The number of places to shift.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 970 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>reference</code> <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator[] (size_type__pos) [inline]</h3>
<p>Array-indexing support. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__pos</i> Index into the dynamic_bitset.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A bool for a &#8216;const dynamic_bitset&#8217;. For non-const bitsets, an instance of the reference proxy class.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>These operators do no range checking and throw no exceptions, as required by DR 11 to the standard.</dl>
<p> Definition at line 1073 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; const_reference <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator[] (size_type__pos) const [inline]</h3>
<p>Array-indexing support. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__pos</i> Index into the dynamic_bitset.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A bool for a &#8216;const dynamic_bitset&#8217;. For non-const bitsets, an instance of the reference proxy class.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>These operators do no range checking and throw no exceptions, as required by DR 11 to the standard.</dl>
<p> Definition at line 1077 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator^= (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) [inline]</h3>
<p>Operations on dynamic_bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__rhs</i> A same-sized dynamic_bitset.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 935 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator|= (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) [inline]</h3>
<p>Operations on dynamic_bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__rhs</i> A same-sized dynamic_bitset.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 928 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::operator~ () const [inline]</h3>
<p>See the no-argument flip(). </p>
<p> Definition at line 1060 of file dynamic_bitset. </p>
<p> References std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::flip().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; void <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::push_back (bool__bit) [inline]</h3>
<p>Push a bit onto the high end of the bitset. </p>
<p> Definition at line 869 of file dynamic_bitset. </p>
<p> References std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::size().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::reset () [inline]</h3>
<p>Sets every bit to false. </p>
<p> Definition at line 1013 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::reset (size_type__pos) [inline]</h3>
<p>Sets a given bit to false. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__pos</i> The index of the bit.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::out_of_range</i> If <i>__pos</i> is bigger the size of the set.</dl>
<p> Same as writing set(__pos, false). </p>
<p> Definition at line 1027 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; void <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::resize (size_type__nbits, bool__value = false) [inline]</h3>
<p>Resize the bitset. </p>
<p> Definition at line 848 of file dynamic_bitset. </p>
<p> Referenced by std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::dynamic_bitset(), and std::tr2::operator&gt;&gt;().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::<code>set</code> () [inline]</h3>
<p>Sets every bit to true. </p>
<p> Definition at line 988 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt;&amp; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::<code>set</code> (size_type__pos, bool__val = true) [inline]</h3>
<p>Sets a given bit to a particular value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__pos</i> The index of the bit.<br />
 <i>__val</i> Either true or false, defaults to true.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::out_of_range</i> If <i>__pos</i> is bigger the size of the set.</dl>
<p> Definition at line 1002 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; size_type <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::size () const [inline], [noexcept]</h3>
<p>Returns the total number of bits. </p>
<p> Definition at line 1148 of file dynamic_bitset. </p>
<p> Referenced by std::tr2::operator&gt;&gt;(), and std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::push_back().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; void <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::swap (<code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__b) [inline]</h3>
<p>Swap with another bitset. </p>
<p> Definition at line 808 of file dynamic_bitset. </p>
<p> References std::swap(). </p>
<p> Referenced by std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::operator=().</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; bool <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::test (size_type__pos) const [inline]</h3>
<p>Tests the value of a bit. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__pos</i> The index of a bit.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The value at <i>__pos</i>.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::out_of_range</i> If <i>__pos</i> is bigger the size of the set.</dl>
<p> Definition at line 1175 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; template&lt;typename _CharT = char, typename _Traits = std::char_traits&lt;_CharT&gt;, typename _Alloc1 = std::allocator&lt;_CharT&gt;&gt; <code>std::basic_string</code>&lt;_CharT, _Traits, _Alloc1&gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::to_string (_CharT__zero = _CharT(&#8216;0&#8217;), _CharT__one = _CharT(&#8216;1&#8217;)) const [inline]</h3>
<p>Returns a character interpretation of the dynamic_bitset. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>The string equivalent of the bits.</dl>
<p> Note the ordering of the bits: decreasing character positions correspond to increasing bit positions (see the main class notes for an example). </p>
<p> Definition at line 1113 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; unsigned long long <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::to_ullong () const [inline]</h3>
<p>Returns a numerical interpretation of the dynamic_bitset. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>The integral equivalent of the bits.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::overflow_error</i> If there are too many bits to be represented in an unsigned long.</dl>
<p> Definition at line 1098 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; unsigned long <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::to_ulong () const [inline]</h3>
<p>Returns a numerical interpretation of the dynamic_bitset. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>The integral equivalent of the bits.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::overflow_error</i> If there are too many bits to be represented in an unsigned long.</dl>
<p> Definition at line 1088 of file dynamic_bitset.</p>
<h2>Member Data Documentation</h2>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>std::tr2::dynamic_bitset</code>&lt; _WordT, _Alloc &gt;::__pad0__ [explicit]</h3>
<p>All bits set to zero. </p>
<p> Definition at line 722 of file dynamic_bitset.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
