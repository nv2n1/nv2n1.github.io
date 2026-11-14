---
title: "stdios_baseinit(3)"
name: "stdios_baseinit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseinit/"
---

std::ios_base::Init - std::ios_base::Init

<h2>Synopsis</h2>

<pre><code>class Init;</code></pre> 
This class is used to ensure that the default C++ streams (std::cin, std::cout, etc.) are properly initialized and destructed. The class tracks how many instances of it are created and initializes the C++ streams when the first instance is constructed as well as flushes the output streams when the last instance is destructed. 
The header &lt;iostream&gt; behaves as if it defines (directly or indirectly) an instance of std::ios_base::Init with static storage duration: this makes it safe to access the standard I/O streams in the constructors and destructors of static objects with ordered_initialization (as long as #include &lt;iostream&gt; is included in the translation unit before these objects were defined) 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if *this is the first instance created, initializes the default C++ streams 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if *this is the last instance destroyed, flushes the default C++ streams 
destructor <i>(public member function)</i>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reads from the standard C input stream stdin 
cin (global object) 
wcin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C output stream stdout 
cout (global object) 
wcout 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C error stream stderr, unbuffered 
cerr (global object) 
wcerr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C error stream stderr 
clog (global object) 
wclog 
