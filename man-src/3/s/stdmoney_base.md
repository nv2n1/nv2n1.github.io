---
title: "stdmoney_base(3)"
name: "stdmoney_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmoney_base/"
---

std::money_base - std::money_base

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

class money_base;</code></pre> 
The class std::money_base provides constants which are inherited and used by the std::moneypunct, std::money_get and std::money_put facets. 

<h2>Member types</h2>

Member type Definition 
enum part { none, space, symbol, sign, value }; unscoped enumeration type 
struct pattern { char field[4]; }; the monetary format type 

 

 
Enumeration constant Definition 
none whitespace is permitted but not required except in the last position, where whitespace is not permitted 
space one or more whitespace characters are required 
symbol the sequence of characters returned by moneypunct::curr_symbol is required 
sign the first of the characters returned by moneypunct::positive_sign or moneypunct::negative_sign is required 
value the absolute numeric monetary value is required

<h2>Notes</h2>

The monetary format is an array of four chars convertible to std::money_base::part. In that sequence, each of symbol, sign, and value appears exactly once, and either space or none appears in the remaining position. The value none, if present, is not first; the value space, if present, is neither first nor last. 
The default format, returned by the standard specializations of std::moneypunct is {symbol, sign, none, value} 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;defines monetary formatting parameters used by std::money_get and std::money_put 
moneypunct <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses and constructs a monetary value from an input character sequence 
money_get <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;formats a monetary value for output as a character sequence 
money_put <i>(class template)</i> 
