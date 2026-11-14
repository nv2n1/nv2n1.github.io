---
title: "std__detail_state(3)"
name: "std__detail_state"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_state/"
description: "std::__detail::_State –"
---

<p>std::__detail::_State &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef int <code>_OpcodeT</code></p>
<h3>Public Member Functions</h3>
<p><code>_State</code> (_OpcodeT __opcode) </p>
<p> <code>_State</code> (const <code>_Matcher</code> &amp;__m) </p>
<p> <code>_State</code> (_OpcodeT __opcode, unsigned int __s, const <code>_Tagger</code> &amp;__t) </p>
<p> <code>_State</code> (<code>_StateIdT</code> __next, <code>_StateIdT</code> __alt)</p>
<h3>Public Attributes</h3>
<p><code>_StateIdT</code> <code>_M_alt</code> </p>
<p> <code>_Matcher</code> <code>_M_matches</code> </p>
<p> <code>_StateIdT</code> <code>_M_next</code> </p>
<p> _OpcodeT <code>_M_opcode</code> </p>
<p> unsigned int <code>_M_subexpr</code> </p>
<p> <code>_Tagger</code> <code>_M_tagger</code></p>
<h2>Detailed Description</h2>
<p>struct _State </p>
<p> An individual state in an NFA </p>
<p> In this case a &#8216;state&#8217; is an entry in the NFA definition coupled with its outgoing transition(s). All states have a single outgoing transition, except for accepting states (which have no outgoing transitions) and alt states, which have two outgoing transitions. </p>
<p> Definition at line 211 of file regex_nfa.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
