---
title: "stdbasic_istream_sentry(3)"
name: "stdbasic_istream_sentry"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_istream_sentry/"
description: "std::basic_istream< _CharT, _Traits >::sentry –"
---

<p>std::basic_istream&lt; _CharT, _Traits &gt;::sentry &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef<br />
 <code>__istream_type::__ctype_type</code> <code>__ctype_type</code>&quot; </p>
<p> typedef _Traits::int_type <code>__int_type</code> </p>
<p> typedef <code>basic_istream</code>&lt; _CharT,<br />
 _Traits &gt; <code>__istream_type</code>&quot; </p>
<p> typedef <code>basic_streambuf</code><br />
 &lt; _CharT, _Traits &gt; <code>__streambuf_type</code>&quot; </p>
<p> typedef _Traits <code>traits_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>sentry (basic_istream&lt; _CharT, _Traits &gt; &amp;__is, bool __noskipws=false)



operator bool () const</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _CharT, typename _Traits = char_traits&lt;_CharT&gt;&gt;class std::basic_istream&lt; _CharT, _Traits &gt;::sentry</h3>
<p>Performs setup work for input streams. </p>
<p> Objects of this class are created before all of the standard extractors are run. It is responsible for <i>exception-safe prefix and suffix operations,</i> although only prefix actions are currently required by the standard. </p>
<p> Definition at line 657 of file istream.</p>
<h2>Member Typedef Documentation</h2>
<h3>template&lt;typename _CharT, typename _Traits = char_traits&lt;_CharT&gt;&gt; typedef _Traits <code>std::basic_istream</code>&lt; _CharT, _Traits &gt;::<code>sentry::traits_type</code></h3>
<p>Easy access to dependent types. </p>
<p> Definition at line 664 of file istream.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;typename _CharT, typename _Traits&gt; <code>std::basic_istream</code>&lt; _CharT, _Traits &gt;::sentry::sentry (<code>basic_istream</code>&lt; _CharT, _Traits &gt; &amp;__is, bool__noskipws = false) [explicit]</h3>
<p>The constructor performs all the work. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__is</i> The input stream to guard.<br />
 <i>__noskipws</i> Whether to consume whitespace or not.</dl>
<p> If the stream state is good (<i>__is.good()</i> is true), then the following actions are performed, otherwise the sentry state is false (<i>not okay</i>) and failbit is set in the stream state. </p>
<p> The sentry&#8217;s preparatory actions are: </p>
<dl>
<dt>1.</p>
<dd>if the stream is tied to an output stream, is.tie()-&gt;flush() is called to synchronize the output sequence</p>
<dt>2.</p>
<dd>if <i>__noskipws</i> is false, and ios_base::skipws is set in is.flags(), the sentry extracts and discards whitespace characters from the stream. The currently imbued locale is used to determine whether each character is whitespace.</dl>
<p> If the stream state is still good, then the sentry state becomes true (<i>okay</i>). </p>
<p> Definition at line 47 of file istream.tcc. </p>
<p> References std::ios_base::eofbit, std::ios_base::failbit, std::ios_base::flags(), std::basic_ios&lt; _CharT, _Traits &gt;::good(), std::ios_base::goodbit, std::__ctype_abstract_base&lt; _CharT &gt;::is(), std::basic_ios&lt; _CharT, _Traits &gt;::rdbuf(), std::basic_ios&lt; _CharT, _Traits &gt;::setstate(), std::basic_streambuf&lt; _CharT, _Traits &gt;::sgetc(), std::ios_base::skipws, std::basic_streambuf&lt; _CharT, _Traits &gt;::snextc(), and std::basic_ios&lt; _CharT, _Traits &gt;::tie().</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename _CharT, typename _Traits = char_traits&lt;_CharT&gt;&gt; <code>std::basic_istream</code>&lt; _CharT, _Traits &gt;::sentry::operator bool () const [inline], [explicit]</h3>
<p>Quick status checking. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>The sentry state.</dl>
<p> For ease of use, sentries may be converted to booleans. The return value is that of the sentry state (true == okay). </p>
<p> Definition at line 705 of file istream.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
