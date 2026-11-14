---
title: "std__debuglist(3)"
name: "std__debuglist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__debuglist/"
description: "std::__debug::list< _Tp, _Allocator > –"
---

<p>std::__debug::list&lt; _Tp, _Allocator &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits list&lt; _Tp, _Allocator &gt;, and <code>__gnu_debug::_Safe_sequence&lt; list&lt; _Tp, _Allocator &gt; &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef _Allocator <code>allocator_type</code> </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_iterator</code><br />
 &lt; <code>_Base_const_iterator</code>, <code>list</code> &gt; <code>const_iterator</code>&quot; </p>
<p> typedef _Base::const_pointer <code>const_pointer</code> </p>
<p> typedef _Base::const_reference <code>const_reference</code> </p>
<p> typedef <code>std::reverse_iterator</code><br />
 &lt; <code>const_iterator</code> &gt; <code>const_reverse_iterator</code>&quot; </p>
<p> typedef _Base::difference_type <code>difference_type</code> </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_iterator</code><br />
 &lt; <code>_Base_iterator</code>, <code>list</code> &gt; <code>iterator</code>&quot; </p>
<p> typedef _Base::pointer <code>pointer</code> </p>
<p> typedef _Base::reference <code>reference</code> </p>
<p> typedef <code>std::reverse_iterator</code><br />
 &lt; <code>iterator</code> &gt; <code>reverse_iterator</code>&quot; </p>
<p> typedef _Base::size_type <code>size_type</code> </p>
<p> typedef _Tp <code>value_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>_Base::splice(__position.base(), std::move(__x._M_base()))

        _Base::splice(__position.base(), std::move(__x._M_base()), __i.base())

            void _M_attach(_Safe_iterator_base *__it, bool __constant)

                void _M_attach_single(_Safe_iterator_base *__it, bool __constant) throw()

                    _Base
    &amp; _M_base() noexcept

    const _Base
    &amp; _M_base() const noexcept

    void _M_detach(_Safe_iterator_base * __it)

        void _M_detach_single(_Safe_iterator_base * __it) throw()

            void _M_invalidate_all() const

    void _M_invalidate_if(_Predicate __pred)

        void _M_transfer_from_if(_Safe_sequence &amp; __from, _Predicate __pred)

            this _M_transfer_from_if(__x, _Not_equal(__x._M_base().end()))

                this _M_transfer_from_if(__x, _Equal(__i.base()))

                    reference back()

                        const_reference back() const

    const _Tp const _Allocator iterator begin() noexcept

    const_iterator begin() const noexcept

    const_iterator cbegin() const noexcept

    const_iterator cend() const noexcept

    void clear() noexcept

    const_reverse_iterator crbegin() const noexcept

    const_reverse_iterator crend() const noexcept

    template &lt;typename... _Args&gt;
    iterator emplace(iterator __position, _Args &amp;&amp;...__args)

        iterator end() noexcept

    const_iterator end() const noexcept

    iterator erase(iterator __position)

        iterator erase(iterator __position, iterator __last)

            reference front()

                const_reference front() const

    iterator insert(iterator __position, const _Tp &amp;__x)

        iterator insert(iterator __position, _Tp &amp;&amp;__x)

            void insert(iterator __p, initializer_list&lt;value_type&gt; __l)

                void insert(iterator __position, size_type __n, const _Tp &amp;__x)

                    template &lt;class _InputIterator, typename = std::_RequireInputIter&lt;_InputIterator&gt;&gt;
                    void insert(iterator __position, _InputIterator __first, _InputIterator __last)

                        void pop_back()

                            void pop_front()

                                reverse_iterator rbegin() noexcept

    const_reverse_iterator rbegin() const noexcept

    void remove(const _Tp &amp;__value)

        template &lt;class _Predicate&gt;
        void remove_if(_Predicate __pred)

            reverse_iterator rend() noexcept

    const_reverse_iterator rend() const noexcept

    void resize(size_type __sz)

        void resize(size_type __sz, const _Tp &amp;__c)

            void splice(iterator __position, list &amp;__x)

                void splice(iterator __position, list &amp;__x, iterator __i)

                    void splice(iterator __position, list &amp;&amp;__x, iterator __first, iterator __last)

                        void splice(iterator __position, list &amp;__x, iterator __first, iterator __last)

                            void swap(list &amp; __x)

                                void unique()

                                    template &lt;class _BinaryPredicate&gt;
                                    void unique(_BinaryPredicate __binary_pred)

                                        while (false)

                                            while (false)

                                                while (false)

                                                    Public Attributes const _Tp const _Allocator
    &amp; __a

    __pad0__ : _Base(__a)
{
}
explicit list(size_type __n)
    : _Base(__n)
{
} list(size_type __n



const _Tp &amp; __value



_Safe_iterator_base * _M_const_iterators



_Safe_iterator_base * _M_iterators



unsigned int _M_version



do



void



Protected Member Functions
void _M_detach_all ()



void _M_detach_singular ()



__gnu_cxx::__mutex &amp; _M_get_mutex ()  throw ()



void _M_revalidate_singular ()



void _M_swap (_Safe_sequence_base &amp;__x)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Allocator = std::allocator&lt;_Tp&gt;&gt;class std::__debug::list&lt; _Tp, _Allocator &gt;</h3>
<p>Class std::list with safety/checking/debug instrumentation. </p>
<p> Definition at line 42 of file debug/list.</p>
<h2>Member Function Documentation</h2>
<h3>void __gnu_debug::_Safe_sequence_base::_M_attach (<code>_Safe_iterator_base</code> *__it, bool__constant) [inherited]</h3>
<p>Attach an iterator to this sequence.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_attach_single (<code>_Safe_iterator_base</code> *__it, bool__constant) [inherited]</h3>
<p>Likewise but not thread safe.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_detach (<code>_Safe_iterator_base</code> *__it) [inherited]</h3>
<p>Detach an iterator from this sequence</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_detach_all () [protected], [inherited]</h3>
<p>Detach all iterators, leaving them singular. </p>
<p> Referenced by __gnu_debug::_Safe_sequence_base::~_Safe_sequence_base().</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_detach_single (<code>_Safe_iterator_base</code> *__it) [inherited]</h3>
<p>Likewise but not thread safe.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_detach_singular () [protected], [inherited]</h3>
<p>Detach all singular iterators. </p>
<p> <code>Postcondition:</code></p>
<dl>
<dd>for all iterators i attached to this sequence, i-&gt;_M_version == _M_version.</dl>
<h3>__gnu_cxx::__mutex&amp; __gnu_debug::_Safe_sequence_base::_M_get_mutex () [protected], [inherited]</h3>
<p>For use in _Safe_sequence. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_invalidate_all () const [inline], [inherited]</h3>
<p>Invalidates all iterators. </p>
<p> Definition at line 233 of file safe_base.h. </p>
<p> References __gnu_debug::_Safe_sequence_base::_M_version.</p>
<h3>void <code>__gnu_debug::_Safe_sequence</code>&lt; <code>list</code>&lt; _Tp, _Allocator &gt; &gt;::_M_invalidate_if (_Predicate__pred) [inherited]</h3>
<p>Invalidates all iterators x that reference this sequence, are not singular, and for which __pred(x) returns true. __pred will be invoked with the normal iterators nested in the safe ones.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_revalidate_singular () [protected], [inherited]</h3>
<p>Revalidates all attached singular iterators. This method may be used to validate iterators that were invalidated before (but for some reason, such as an exception, need to become valid again).</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_swap (<code>_Safe_sequence_base</code> &amp;__x) [protected], [inherited]</h3>
<p>Swap this sequence with the given sequence. This operation also swaps ownership of the iterators, so that when the operation is complete all iterators that originally referenced one container now reference the other container.</p>
<h3>void <code>__gnu_debug::_Safe_sequence</code>&lt; <code>list</code>&lt; _Tp, _Allocator &gt; &gt;::_M_transfer_from_if (<code>_Safe_sequence</code>&lt; <code>list</code>&lt; _Tp, _Allocator &gt; &gt; &amp;__from, _Predicate__pred) [inherited]</h3>
<p>Transfers all iterators x that reference from sequence, are not singular, and for which __pred(x) returns true. __pred will be invoked with the normal iterators nested in the safe ones.</p>
<h2>Member Data Documentation</h2>
<h3>_Safe_iterator_base* __gnu_debug::_Safe_sequence_base::_M_const_iterators [inherited]</h3>
<p>The list of constant iterators that reference this container. </p>
<p> Definition at line 184 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3>_Safe_iterator_base* __gnu_debug::_Safe_sequence_base::_M_iterators [inherited]</h3>
<p>The list of mutable iterators that reference this container. </p>
<p> Definition at line 181 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3>unsigned int __gnu_debug::_Safe_sequence_base::_M_version [mutable], [inherited]</h3>
<p>The container version number. This number may never be 0. </p>
<p> Definition at line 187 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence_base::_M_invalidate_all(), and __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
