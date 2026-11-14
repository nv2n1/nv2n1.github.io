---
title: "usage(3)"
name: "usage"
section: "3"
letter: "u"
url: "/docs/linux/man/3-usage/"
---

usage - Usage To use QuantLib classes in your own code just add <pre><code>#include &lt;ql/quantlib.hpp&gt;</code></pre> 
&nbsp;<wbr>at the beginning of your source/header files. Depending on the number of your files in your project, this could cause a large increase in compilation time. If this were not acceptable, collective headers are also available for smaller parts of the library;&nbsp;<wbr>in particular, each subdirectory of the ql directory contains a file all.hpp which makes available all classes and function in the respective subdirectory. Under the Examples folder you can find examples of QuantLib usage, including input files for automake and makefiles for the Borland free compiler and Microsoft Visual C++. For the latter, project files are also available.

<h2>Microsoft Visual C++</h2>

A few suggestions for Visual C++ users wanting to use QuantLib into their own application:
<dl><dt>1.
<dd>you won't have to explicitly link your application to the QuantLib library. This is done automatically by compiler directives embedded in the sources.
<dt>2.
<dd>Your project must be compiled with the same options that were used in compiling the QuantLib library you're linking with, namely,
<dt> *
<dd>Property Pages -&gt; C/C++ -&gt; Code Generation -&gt; Runtime Library: select the appropriate run-time library.
<dt> *
<dd>Property Pages -&gt; C/C++ -&gt; Code Generation -&gt; Basic Runtime Checks: select 'Both (/RTC1, equiv. to /RTCsu)'.</dl>
