---
title: "stdbasic_ostream_sentry(3)"
name: "stdbasic_ostream_sentry"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_ostream_sentry/"
description: "std::basic_ostream< _CharT, _Traits >::sentry –"
---

<p>std::basic_ostream&lt; _CharT, _Traits &gt;::sentry &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<p><code>sentry</code> (<code>basic_ostream</code>&lt; _CharT, _Traits &gt; &amp;__os) </p>
<p> <code>~sentry</code> () </p>
<p> <code>operator bool</code> () const</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _CharT, typename _Traits = char_traits&lt;_CharT&gt;&gt;class std::basic_ostream&lt; _CharT, _Traits &gt;::sentry</h3>
<p>Performs setup work for output streams. </p>
<p> Objects of this class are created before all of the standard inserters are run. It is responsible for <i>exception-safe prefix and suffix operations</i>. </p>
<p> Definition at line 400 of file ostream.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;typename _CharT, typename _Traits&gt; <code>std::basic_ostream</code>&lt; _CharT, _Traits &gt;::sentry::sentry (<code>basic_ostream</code>&lt; _CharT, _Traits &gt; &amp;__os) [explicit]</h3>
<p>The constructor performs preparatory work. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__os</i> The output stream to guard.</dl>
<p> If the stream state is good (<i>__os.good()</i> is true), then if the stream is tied to another output stream, is.tie()-&gt;flush() is called to synchronize the output sequences. </p>
<p> If the stream state is still good, then the sentry state becomes true (<i>okay</i>). </p>
<p> Definition at line 47 of file ostream.tcc. </p>
<p> References std::ios_base::failbit, std::basic_ios&lt; _CharT, _Traits &gt;::good(), std::basic_ios&lt; _CharT, _Traits &gt;::setstate(), and std::basic_ios&lt; _CharT, _Traits &gt;::tie().</p>
<h3>template&lt;typename _CharT, typename _Traits = char_traits&lt;_CharT&gt;&gt; <code>std::basic_ostream</code>&lt; _CharT, _Traits &gt;::sentry::~sentry () [inline]</h3>
<p>Possibly flushes the stream. If ios_base::unitbuf is set in os.flags(), and std::uncaught_exception() is true, the sentry destructor calls flush() on the output stream. </p>
<p> Definition at line 428 of file ostream. </p>
<p> References std::ios_base::badbit, std::uncaught_exception(), and std::ios_base::unitbuf.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename _CharT, typename _Traits = char_traits&lt;_CharT&gt;&gt; <code>std::basic_ostream</code>&lt; _CharT, _Traits &gt;::sentry::operator bool () const [inline], [explicit]</h3>
<p>Quick status checking. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>The sentry state.</dl>
<p> For ease of use, sentries may be converted to booleans. The return value is that of the sentry state (true == okay). </p>
<p> Definition at line 449 of file ostream.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
