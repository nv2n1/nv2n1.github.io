---
title: "stdstreamoff(3)"
name: "stdstreamoff"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstreamoff/"
---

std::streamoff - std::streamoff

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ios&gt;

typedef /*unspecified*/ streamoff;</code></pre> 
The type std::streamoff is a signed integral type of sufficient size to represent the maximum possible file size supported by the operating system. Typically, this is a typedef to long long. 
It is used to represent offsets from stream positions (values of type std::fpos). A std::streamoff value of -1 is also used to represent error conditions by some of the I/O library functions. 
Relationship with std::fpos 
* the difference between two std::fpos objects is a value of type std::streamoff 
* a value of type std::streamoff may be added or subtracted from std::fpos yielding a different std::fpos. 
* a value of type std::fpos is implicitly convertible to std::streamoff (the conversion result is the offset from the beginning of the file). 
* a value of type std::fpos is constructible from a value of type std::streamoff 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;represents absolute position in a stream or a file 
fpos <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the input position indicator 
seekg <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the output position indicator 
seekp <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
