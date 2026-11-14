---
title: "stdbasic_filebuf(3)"
name: "stdbasic_filebuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_filebuf/"
---

std::basic_filebuf&lt;CharT,Traits&gt;::seekoff - std::basic_filebuf&lt;CharT,Traits&gt;::seekoff
<h2>Synopsis</h2>
 

 
protected: 
virtual pos_type seekoff( off_type off, 
std::ios_base::seekdir dir, 
std::ios_base::openmode which = std::ios_base::in | std::ios_base::out ); 

 
Repositions the file pointer, if possible, to the position that corresponds to exactly off characters from beginning, end, or current position of the file (depending on the value of dir. 
If the associated file is not open (is_open()==false, fails immediately. 
If the multibyte character encoding is state-dependent (codecvt::encoding() returned -1) or variable-length (codecvt::encoding() returned 0) and the offset off is not 0, fails immediately: this function cannot determine the number of bytes that correspond to off characters. 
If dir is not std::basic_ios::cur or the offset off is not 0, and the most resent operation done on this filebuf object was output (that is, either the put buffer is not empty, or the most recently called function was overflow()), then calls std::codecvt::unshift to determine the unshift sequence necessary, and writes that sequence to the file by calling overflow(). 
Then converts the argument dir to a value whence of type int as follows: 

 
value of dir value of whence 
std::basic_ios::beg SEEK_SET 
std::basic_ios::end SEEK_END 
std::basic_ios::cur SEEK_CUR 

 
Then, if the character encoding is fixed-width (codecvt::encoding() returns some positive number width, moves the file pointer as if by std::fseek(file, width*off, whence). 
Otherwise, moves the file pointer as if by std::fseek(file, 0, whence). 
The openmode argument, required by the base class function signature, is usually ignored, because std::basic_filebuf maintains only one file position. 

<h2>Parameters</h2>
 

 

 
off - relative position to set the position indicator to. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;defines base position to apply the relative offset to. It can be one of the following constants: 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Constant Explanation 
dir - beg the beginning of a stream 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;end the ending of a stream 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cur the current position of stream position indicator 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;defines which of the input and/or output sequences to affect. It can be one or a combination of the following constants: 

 
which - Constant Explanation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in affect the input sequence 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;out affect the output sequence 

 

 

<h2>Return value</h2>
 

 
A newly constructed object of type pos_type which stores the resulting file position, or pos_type(off_type(-1)) on failure. 

<h2>Notes</h2>
 

 
seekoff() is called by std::basic_streambuf::pubseekoff, which is called by std::basic_istream::seekg, std::basic_ostream::seekp, std::basic_istream::tellg, and std::basic_ostream::tellp 

<h2>Example</h2>
 

 
 // Run this code 

 
&nbsp;<wbr>&nbsp;#include &lt;iostream&gt; 
&nbsp;<wbr>&nbsp;#include &lt;fstream&gt; 
&nbsp;<wbr>&nbsp;#include &lt;locale&gt; 
&nbsp;<wbr>&nbsp;int main() 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// prepare a 10-byte file holding 4 characters in UTF8 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::ofstream(&quot;text.txt&quot;) &lt;&lt; u8&quot;z\u00df\u6c34\U0001d10b&quot;; // or u8&quot;zß水&quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// or &quot;\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b&quot;; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// open using a non-converting encoding 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::ifstream f1(&quot;text.txt&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;f1's locale's encoding() returns &quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; std::use_facet&lt;std::codecvt&lt;char, char, std::mbstate_t&gt;&gt;(f1.getloc()).encoding() &lt;&lt; '\n' 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; &quot;pubseekoff(3, beg) returns &quot; &lt;&lt; f1.rdbuf()-&gt;pubseekoff(3, std::ios_base::beg) &lt;&lt; '\n' 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; &quot;pubseekoff(0, end) returns &quot; &lt;&lt; f1.rdbuf()-&gt;pubseekoff(0, std::ios_base::end) &lt;&lt; '\n';; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// open using UTF-8 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wifstream f2(&quot;text.txt&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f2.imbue(std::locale(&quot;en_US.UTF-8&quot;)); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;f2's locale's encoding() returns &quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; std::use_facet&lt;std::codecvt&lt;wchar_t, char, std::mbstate_t&gt;&gt;(f2.getloc()).encoding() &lt;&lt; '\n' 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; &quot;pubseekoff(3, beg) returns &quot; &lt;&lt; f2.rdbuf()-&gt;pubseekoff(3, std::ios_base::beg) &lt;&lt; '\n' 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; &quot;pubseekoff(0, end) returns &quot; &lt;&lt; f2.rdbuf()-&gt;pubseekoff(0, std::ios_base::end) &lt;&lt; '\n'; 

 
&nbsp;<wbr>&nbsp;} 

<h2>Output:</h2>
 

 
&nbsp;<wbr>&nbsp;f1's locale's encoding() returns 1 
&nbsp;<wbr>&nbsp;pubseekoff(3, beg) returns 3 
&nbsp;<wbr>&nbsp;pubseekoff(0, end) returns 10 
&nbsp;<wbr>&nbsp;f2's locale's encoding() returns 0 
&nbsp;<wbr>&nbsp;pubseekoff(3, beg) returns -1 
&nbsp;<wbr>&nbsp;pubseekoff(0, end) returns 10 

 

<h2>See also</h2>
 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes seekoff() 
pubseekoff <i>(public member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i> 

 
seekpos repositions the file position, using absolute addressing 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i> 
<b>[virtual]</b> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the file position indicator to a specific location in a file 
fseek <i>(function)</i>
