---
title: "stdstreamsize(3)"
name: "stdstreamsize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstreamsize/"
---

std::streamsize - std::streamsize

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ios&gt;

typedef /*unspecified*/ streamsize;</code></pre> 
The type std::streamsize is a signed integral type used to represent the number of characters transferred in an I/O operation or the size of an I/O buffer. It is used as a signed counterpart of std::size_t, similar to the POSIX type ssize_t. 
Except in the constructors of std::strstreambuf, negative values of std::streamsize are never used. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns number of characters extracted by last unformatted input operation 
gcount <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extracts and discards characters until the given character is found 
ignore <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extracts blocks of characters 
read <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inserts blocks of characters 
write <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
