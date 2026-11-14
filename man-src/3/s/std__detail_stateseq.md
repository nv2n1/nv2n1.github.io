---
title: "std__detail_stateseq(3)"
name: "std__detail_stateseq"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_stateseq/"
---

std::__detail::_StateSeq -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>_StateSeq (_Nfa &amp;__ss, _StateIdT __s, _StateIdT __e=_S_invalid_state_id)



_StateSeq (const _StateSeq &amp;__e1, const _StateSeq &amp;__e2)



_StateSeq (const _StateSeq &amp;__e, _StateIdT __id)



_StateSeq (const _StateSeq &amp;__rhs)



void _M_append (_StateIdT __id)



void _M_append (_StateSeq &amp;__rhs)



_StateIdT _M_clone ()



_StateIdT _M_front () const



void _M_push_back (_StateIdT __id)



_StateSeq &amp; operator= (const _StateSeq &amp;__rhs)</code></pre>

<h2>Detailed Description</h2>

Describes a sequence of one or more _State, its current start and end(s). This structure contains fragments of an NFA during construction. 

 Definition at line 352 of file regex_nfa.h.

<h2>Author</h2>

Generated automatically by Doxygen for libstdc++ from the source code.
