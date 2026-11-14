---
title: "stdstrstreambufpbackfail(3)"
name: "stdstrstreambufpbackfail"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambufpbackfail/"
description: "std::strstreambuf::pbackfail – std::strstreambuf::pbackfail"
---

<p>std::strstreambuf::pbackfail &#8211; std::strstreambuf::pbackfail</p>
<h2>Synopsis</h2>
<pre><code>protected:

virtual int_type pbackfail( int_type c = EOF );</code></pre>
<p>This protected virtual function is called by the public functions basic_streambuf::sungetc and basic_streambuf::sputbackc (which, in turn, are called by basic_istream::unget and basic_istream::putback).<br />
1) The caller is requesting that the get area is backed up by one character (pbackfail() is called with no arguments or with EOF as the argument)<br />
a) First, checks if there is a putback position, and if there really isn&#8217;t, fails. (strstreambuf has no external character source to re-read)<br />
b) If the caller was wrong and the putback position is in fact available, simply decrements basic_streambuf::gptr(), e.g. by calling gbump(-1).<br />
2) The caller attempts to putback a different character from the one retrieved earlier (pbackfail() is called with the character that needs to be put back), in which case<br />
a) First, checks if there is a putback position, and if there isn&#8217;t, fails.<br />
b) Then checks what character is in the putback position. If the character held there is already equal to (char)c, then simply decrements basic_streambuf::gptr().<br />
c) Otherwise, if the buffer is unmodifiable (this strstreambuf was constructed with a string literal or some other const array), fails.<br />
d) Otherwise, decrements basic_streambuf::gptr() and writes c to the location pointed to gptr() after adjustment. </p>
<h2>Parameters</h2>
<p>c &#8211; the character to put back, or Traits::eof() to indicate that backing up of the get area is requested</p>
<h2>Return value</h2>
<p>c on success except if c was EOF, in which case unspecified value other than EOF is returned.<br />
EOF on failure. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>pbackfail puts a character back into the input sequence, possibly modifying the input sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the next pointer in the input sequence back by one<br />
sungetc <i>(public member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;puts one character back in the input sequence<br />
sputbackc <i>(public member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unextracts a character<br />
unget <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;puts character into input stream<br />
putback <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> </p>
