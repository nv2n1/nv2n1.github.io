---
title: "numconv(1)"
name: "numconv"
section: "1"
letter: "n"
url: "/docs/linux/man/1-numconv/"
description: "numconv – convert numbers from one number system to another"
---

<h2>NAME</h2>
<p> numconv &#8211; convert numbers from one number system to another</p>
<h2>SYNOPSIS</h2>
<p> <code>Numconv</code> &lt;options&gt;</p>
<h2>DESCRIPTION</h2>
<p> numconv is a filter that converts integers from one number system to another. For example, it can convert from Roman Numerals such as &quot;CCLVI&quot; to ordinary Western numbers such as &quot;256&quot; or from Western numbers to Chinese. The great majority of number systems, both modern and ancient, are supported, including numerous variants. </p>
<p> If the input number system is &#8216;all&#8217;, the number system will be autodetected. </p>
<p> <code>numconv</code> is a command line interface to <code>libuninum</code> a library for converting between textual representations of numbers and machine-internal representations. Further information about the conversions performed is available in the documentation for this library.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> &lt;input file&gt;</p>
<dd> Read input from the specified file.</p>
<dt><code>-o</code> &lt;output file&gt;</p>
<dd> Write output into the specified file.</p>
<dt><code>-I</code></p>
<dd> Identify the number system of the input.</p>
<dt><code>-c</code></p>
<dd> List the available number system cover terms.</p>
<dt><code>-l</code></p>
<dd> List the available number systems.</p>
<dt><code>-f</code> &lt;input number system&gt;</p>
<dd> Specify the number system of the input.</p>
<dt><code>-t</code> &lt;output number system&gt;</p>
<dd> Specify the number system of the output.</p>
<dt><code>-b</code> &lt;input base&gt;</p>
<dd> Specify the input base for Western numbers. The base must be in the range [1,36].</p>
<dt><code>-B</code> &lt;output base&gt;</p>
<dd> Specify the output base for Western numbers. The base must be in the range [1,36].</p>
<dt><code>-g</code> &lt;output general group size&gt;</p>
<dd> Specify the size of digit groups other than the ow-order group. The default is 3.</p>
<dt><code>-G</code> &lt;output low group size&gt;</p>
<dd> Specify the size of the low-order group of digits. The default is 3.</p>
<dt><code>-s</code> &lt;output group separator character&gt;</p>
<dd> Specify character to use as &quot;thousands separator&quot;. The default is a comma.</p>
<dt><code>-L</code></p>
<dd> Set the output grouping parameters, general group size, first group size, and group separator character, according to the current locale.</p>
<dt><code>-m</code></p>
<dd> When generating Roman numerals, use unit characters with superscript macron for thousands greater than one instead of Ms.</p>
<dt><code>-h</code></p>
<dd> Print help information.</p>
<dt><code>-v</code></p>
<dd> Print version information.</dl>
<h2>EXAMPLES</h2>
<p> To convert from Roman Numerals to ordinary Western numbers: </p>
<p> numconv -f Roman -t Western_Lower </p>
<p> To convert from ordinary Western numbers to the variety of number in current use in the People&#8217;s Republic of China: </p>
<p> numconv -f Western -t Mandarin_Regular_Simplified </p>
<p> To convert from ordinary Western numbers to Western numbers in base 2: </p>
<p> numconv -f Western_Lower -t Western_Lower -B 2 </p>
<p> To convert from Urdu numbers to Hindi numbers with the traditional Indian grouping: </p>
<p> numconv -f Perso_Arabic -t Devanagari -g 2 </p>
<h2>SEE ALSO</h2>
<p> libuninum (3) </p>
<h2>AUTHOR</h2>
<p> Bill Poser (billposer [at] alum.mit.edu)</p>
<h2>LICENSE</h2>
<p> GNU General Public License, version 2. (<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt)">http://www.gnu.org/licenses/gpl.txt)</a> </p>
<h2>Index</h2>
