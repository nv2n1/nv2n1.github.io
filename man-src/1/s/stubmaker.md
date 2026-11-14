---
title: "stubmaker(1)"
name: "stubmaker"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stubmaker/"
---

<h2 class="name">NAME</h2>
 

 stubmaker.pl - Generates client stubs from a WSDL file. 

<h2>OPTIONS</h2>

<dl>
<dt>-d &lt;dirname&gt;
<dd> Specifies the directory you wish to output the files to. The directory must already exist.
<dt>-v
<dd> Turns on ``verbose'' output during the code stub generation process. To be honest, there is not much the program outputs, but if you must see something output to the console, then this fits the bill.
<dt>--help
<dd> Outputs a short help message.
<dt>--version
<dd> Outputs the current version of stubmaker.pl.</dl>

<h2>STUB FILES</h2>

<h2><font SIZE="-1">STUB</font> <font SIZE="-1">SUBROUTINES</font></h2>

 The ``class'' or ``package'' created by stubmaker.pl is actually a sub-class of the core SOAP::Lite object. As a result, all methods one can call upon SOAP::Lite one can also call upon generated stubs. 

 For example, suppose you wanted to obtain readable output from the generated stub, then simply call <tt><a HREF="/docs/linux/man/1-readable/">readable</a>(1)</tt> on the stub's instance. See the example below. 

 The following subroutines are unique to generated stub classes, and help the user control and configure the stub class.
<dl>
<dt>want_som(boolean)
<dd> When set to 1, SOAP::Lite will return <font SIZE="-1">SOAP::SOM</font> objects to the user upon invoking a method on a remote service. This is very helpful when you need to check to see if the return value is a SOAP::Fault or not. When set to 0, SOAP::Lite will return the return value of the method.</dl>

<h2>EXAMPLES</h2>

<h2>Invoking stubmaker.pl from the command line</h2>

 &gt; perl stubmaker.pl <a rel="nofollow" HREF="http://www.xmethods.net/sd/StockQuoteService.wsdl">http://www.xmethods.net/sd/StockQuoteService.wsdl</a> Or: &gt; perl ``-MStockQuoteService qw(:all)'' -le ``print getQuote('<font SIZE="-1">MSFT</font>')''

<h2>Working with stub classes</h2>

 Command line: &gt; perl stubmaker.pl <a rel="nofollow" HREF="http://ws1.api.re2.yahoo.com/ws/soap-demo/full.wsdl">http://ws1.api.re2.yahoo.com/ws/soap-demo/full.wsdl</a> 

 File: echo.pl &gt; use full; &gt; use SOAP::Lite +trace =&gt; qw( debug ); &gt; my <tt>$f</tt> = new full; &gt; <tt>$f</tt>-&gt;<i>use_prefix</i>(0); &gt; <tt>$f</tt>-&gt;<i><a HREF="/docs/linux/man/1-readable/">readable</a></i>(1); &gt; <tt>$f</tt>-&gt;<i><a HREF="/docs/linux/man/1-want_som/">want_som</a></i>(1); &gt; <tt>$som</tt> = <tt>$f</tt>-&gt;echoViaBase64(``foo'');

<h2>COPYRIGHT</h2>

 Copyright (C) 2000-2005 Paul Kulchenko. All rights reserved. 

 This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>


