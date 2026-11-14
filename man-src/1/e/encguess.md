---
title: "encguess(1)"
name: "encguess"
section: "1"
letter: "e"
url: "/docs/linux/man/1-encguess/"
---

<h2 class="name">NAME</h2>
 

 encguess - guess character encodings of files 

<h2>VERSION</h2>

 <tt>$Id:</tt> encguess,v 0.3 2020/12/02 01:28:17 dankogai Exp dankogai $

<h2>SYNOPSIS</h2>

 <pre>
  encguess [switches] filename...
</pre>

<h3><font SIZE="-1">SWITCHES</font></h3>

<dl>
<dt>-h
<dd> show this message and exit.
<dt>-s
<dd> specify a list of ``suspect encoding types'' to test, separated by either <tt>&quot;:&quot;</tt> or <tt>&quot;,&quot;</tt>
<dt>-S
<dd> output a list of all acceptable encoding types that can be used with the -s param
<dt>-u
<dd> suppress display of unidentified types</dl>

<h3><font SIZE="-1">EXAMPLES:</font></h3>

<dl>
<dt>&bull;
<dd> Guess encoding of a file named <tt>&quot;test.txt&quot;</tt>, using only the default suspect types. 

 <pre>
   encguess test.txt
</pre>
<dt>&bull;
<dd> Guess the encoding type of a file named <tt>&quot;test.txt&quot;</tt>, using the suspect types <tt>&quot;euc-jp,shiftjis,7bit-jis&quot;</tt>. 

 <pre>
   encguess -s euc-jp,shiftjis,7bit-jis test.txt
   encguess -s euc-jp:shiftjis:7bit-jis test.txt
</pre>
<dt>&bull;
<dd> Guess the encoding type of several files, do not display results for unidentified files. 

 <pre>
   encguess -us euc-jp,shiftjis,7bit-jis test*.txt
</pre></dl>

<h2>DESCRIPTION</h2>

 The encoding identification is done by checking one encoding type at a time until all but the right type are eliminated. The set of encoding types to try is defined by the -s parameter and defaults to ascii, utf8 and <font SIZE="-1">UTF-16/32</font> with <font SIZE="-1">BOM.</font> This can be overridden by passing one or more encoding types via the -s parameter. If you need to pass in multiple suspect encoding types, use a quoted string with the a space separating each value.

<h2>SEE ALSO</h2>

 Encode::Guess, Encode::Detect

<h2>LICENSE AND COPYRIGHT</h2>

 Copyright 2015 Michael LaGrasta and Dan Kogai. 

 This program is free software; you can redistribute it and/or modify it under the terms of the the Artistic License (2.0). You may obtain a copy of the full license at: 

 &lt;<a rel="nofollow" HREF="http://www.perlfoundation.org/artistic_license_2_0">http://www.perlfoundation.org/artistic_license_2_0</a>&gt; 

<h2>Index</h2>



<dt><a HREF="#lbAG">DESCRIPTION</a>
<dd>
<dt><a HREF="#lbAH">SEE ALSO</a>
<dd>
<dt><a HREF="#lbAI">LICENSE AND COPYRIGHT</a>
<dd></dl>
