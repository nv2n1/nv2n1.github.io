---
title: "stdios_baseopenmode(3)"
name: "stdios_baseopenmode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseopenmode/"
---

std::ios_base::openmode - std::ios_base::openmode

<h2>Synopsis</h2>

<pre><code>typedef /*implementation defined*/ openmode;

static constexpr openmode app = /*implementation defined*/

static constexpr openmode binary = /*implementation defined*/

static constexpr openmode in = /*implementation defined*/

static constexpr openmode out = /*implementation defined*/

static constexpr openmode trunc = /*implementation defined*/

static constexpr openmode ate = /*implementation defined*/</code></pre> 
Specifies available file open flags. It is a BitmaskType, the following constants are defined: 
Constant Explanation 
app seek to the end of stream before each write 
binary open in binary_mode 
in open for reading 
out open for writing 
trunc discard the contents of the stream when opening 
ate seek to the end of stream immediately after open 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;opens a file and configures it as the associated character sequence 
open <i>(public member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a basic_stringbuf object 
constructor <i>(public member function of std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;)</i> 
