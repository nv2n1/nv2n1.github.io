---
title: "pamseq(1)"
name: "pamseq"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamseq/"
description: "pamseq – generate PAM image of all possible tuple values, in sequence"
---

<h2 class="name">NAME</h2>
<p> pamseq &#8211; generate PAM image of all possible tuple values, in sequence</p>
<h2>SYNOPSIS</h2>
<p> <code>pamseq</code> [<code>-tupletype=</code><i>tupletype</i>] <i>depth</i> <i>maxval</i> </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamseq</code> generates a PAM image of a specified depth and specified maxval that consists of a single row. The row consists of one tuple of every possible value, in order. </p>
<p> For a depth of one, the order is simple: From 0 to maxval, going from left to right. For higher depths, the highest numbered plane goes from 0 to maxval (going left to right) while all the other planes have value 0. Then the sequence repeats except with the next highest plane set to a value of 1, then 2, etc. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-tupletype</code></p>
<dd> This is the value of the &quot;tuple_type&quot; attribute of the created PAM image. It can be any string up to 255 characters. </p>
</dl>
<h2>USAGE</h2>
<p> To create a simple ramp of the values 0..255, for input to various matrix calculations, try </p>
<pre>
<tt>
  pamseq 1 255 
</tt>
</pre>
<p> (Before <code>pamseq</code> existed, <code>pgmramp</code> was often pressed into service for this). </p>
<p> To create a PPM color map of all the possible colors representable with a maxval of 5, do </p>
<pre>
<tt>
  pamseq 3 5 -tupletype=RGB | pamtopnm
</tt>
</pre>
<p> Again, with a modern program based on the Netpbm library, you don&#8217;t need the <code>pamtopnm</code> because a PAM RGB image is equivalent to a PPM image. </p>
<p> You can use such a color map with <code><a href="/docs/linux/man/1-pnmremap/">pnmremap</a></code>(1)<br />
&nbsp;<wbr>to quantize the colors in an image. With the maxval of 5 given in the example, you get a color map of the set of &quot;web safe&quot; colors as defined by Netscape. Most web browsers guarantee that they can produce at least these 216 colors (215 plus black). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmremap/">pnmremap</a></code>(1) , <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamseq</code> was added to Netpbm in June 2002. </p>
<h2>Index</h2>
