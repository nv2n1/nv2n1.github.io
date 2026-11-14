---
title: "std__detail_scanner(3)"
name: "std__detail_scanner"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_scanner/"
description: "std::__detail::_Scanner< _InputIterator > –"
---

<p>std::__detail::_Scanner&lt; _InputIterator &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_Scanner_base</code>.</p>
<h3>Public Types</h3>
<p>typedef std::iterator_traits<br />
 &lt; _IteratorT &gt;::value_type <code>_CharT</code>&quot; </p>
<p> typedef const <code>std::ctype</code>&lt; _CharT &gt; <code>_CtypeT</code> </p>
<p> typedef<br />
 <code>regex_constants::syntax_option_type</code> <code>_FlagT</code>&quot; </p>
<p> typedef _InputIterator <code>_IteratorT</code> </p>
<p> typedef unsigned int <code>_StateT</code> </p>
<p> typedef <code>std::basic_string</code>&lt; _CharT &gt; <code>_StringT</code> </p>
<p> enum <code>_TokenT</code> { <code>_S_token_anychar</code>, <code>_S_token_backref</code>, <code>_S_token_bracket_begin</code>, <code>_S_token_bracket_end</code>, <code>_S_token_inverse_class</code>, <code>_S_token_char_class_name</code>, <code>_S_token_closure0</code>, <code>_S_token_closure1</code>, <code>_S_token_collelem_multi</code>, <code>_S_token_collelem_single</code>, <code>_S_token_collsymbol</code>, <code>_S_token_comma</code>, <code>_S_token_dash</code>, <code>_S_token_dup_count</code>, <code>_S_token_eof</code>, <code>_S_token_equiv_class_name</code>, <code>_S_token_interval_begin</code>, <code>_S_token_interval_end</code>, <code>_S_token_line_begin</code>, <code>_S_token_line_end</code>, <code>_S_token_opt</code>, <code>_S_token_or</code>, <code>_S_token_ord_char</code>, <code>_S_token_quoted_char</code>, <code>_S_token_subexpr_begin</code>, <code>_S_token_subexpr_end</code>, <code>_S_token_word_begin</code>, <code>_S_token_word_end</code>, <code>_S_token_unknown</code> }</p>
<h3>Public Member Functions</h3>
<p><code>_Scanner</code> (_IteratorT __begin, _IteratorT __end, _FlagT __flags, <code>std::locale</code> __loc) </p>
<p> void <code>_M_advance</code> () </p>
<p> <code>_TokenT</code> <code>_M_token</code> () const </p>
<p> const <code>_StringT</code> &amp; <code>_M_value</code> () const</p>
<h3>Static Public Attributes</h3>
<pre><code>static constexpr _StateT _S_state_at_start



static constexpr _StateT _S_state_in_brace



static constexpr _StateT _S_state_in_bracket</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _InputIterator&gt;class std::__detail::_Scanner&lt; _InputIterator &gt;</h3>
<p>struct _Scanner. Scans an input range for regex tokens. </p>
<p> The _Scanner class interprets the regular expression pattern in the input range passed to its constructor as a sequence of parse tokens passed to the regular expression compiler. The sequence of tokens provided depends on the flag settings passed to the constructor: different regular expression grammars will interpret the same input pattern in syntactically different ways. </p>
<p> Definition at line 65 of file regex_compiler.h.</p>
<h2>Member Enumeration Documentation</h2>
<h3>template&lt;typename _InputIterator&gt; enum <code>std::__detail::_Scanner::_TokenT</code></h3>
<p>Token types returned from the scanner. </p>
<p> Definition at line 75 of file regex_compiler.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
