---
title: "funinfoput(3)"
name: "funinfoput"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funinfoput/"
description: "FunInfoPut – put information into a Funtools struct"
---

<h2>NAME</h2>
<p> <code>FunInfoPut &#8211; put information into a Funtools struct</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<pre>
  int FunInfoPut(Fun fun, int type, char *addr, ...)
</pre>
<h2>DESCRIPTION</h2>
<p> The FunInfoPut() routine puts information into a Funtools structure. The first argument is the Fun handle from which information is to be retrieved. After this first required argument comes a variable length list of pairs of arguments. Each pair consists of an integer representing the type of information to store and the address of the new information to store in the struct. The variable list is terminated by a 0. The routine returns the number of put actions performed. </p>
<p> The full list of available information is described above with the <i>FunInfoPut()</i> routine. Although use of this routine is expected to be uncommon, there is one important situation in which it plays an essential part: writing multiple extensions to a single output file. </p>
<p> For input, multiple extensions are handled by calling <i>FunOpen()</i> for each extension to be processed. When opening multiple inputs, it sometimes is the case that you will want to process them and then write them (including their header parameters) to a single output file. To accomplish this, you open successive input extensions using <i>FunOpen()</i> and then call FunInfoPut() to set the Funtools reference handle of the output file to that of the newly opened input extension: </p>
<p>/* open a new input extension */<br />
  ifun=FunOpen(tbuf, &#8220;r&#8221;, NULL)) )<br />
  /* make the new extension the reference handle for the output file */<br />
  FunInfoPut(ofun, FUN_IFUN, &amp;ifun, 0);</p>
<p> Resetting <font SIZE="-1">FUN_IFUN</font> has same effect as when a funtools handle is passed as the final argument to <i>FunOpen()</i>. The state of the output file is reset so that a new extension is ready to be written. Thus, the next I/O call on the output extension will output the header, as expected. </p>
<p> For example, in a binary table, after resetting <font SIZE="-1">FUN_IFUN</font> you can then call <i>FunColumnSelect()</i> to select the columns for output. When you then call <i>FunImagePut()</i> or &lt;A href=&#8220;./library.html#funtablerowput&#8221;&gt;<i>FunTableRowPut()</i>, a new extension will be written that contains the header parameters from the reference extension. Remember to call <i>FunFlush()</i> to complete output of a given extension. </p>
<p> A complete example of this capability is given in the evcol example code. The central algorithm is:</p>
<dl>
<dt>*</p>
<dd> open the output file without a reference handle</p>
<dt>*</p>
<dd> loop: open each input extension in turn</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> set the reference handle for output to the newly opened input extension</p>
<dt>*</p>
<dd> read the input rows or image and perform processing</p>
<dt>*</p>
<dd> write new rows or image to the output file</p>
<dt>*</p>
<dd> flush the output</p>
<dt>*</p>
<dd> close input extension</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>*</p>
<dd> close output file</dl>
<p> Note that <i>FunFlush()</i> is called after processing each input extension in order to ensure that the proper padding is written to the output file. A call to <i>FunFlush()</i> also ensures that the extension header is written to the output file in the case where there are no rows to output. </p>
<p> If you wish to output a new extension without using a Funtools reference handle, you can call <i>FunInfoPut()</i> to reset the <font SIZE="-1">FUN_OPS</font> value directly. For a binary table, you would then call <i>FunColumnSelect()</i> to set up the columns for this new extension. </p>
<pre><code>
/* reset the operations performed on this handle */
int ops = 0;
FunInfoPut(ofun, FUN_OPS, &amp;ops, 0);
FunColumnSelect(fun, sizeof(EvRec), NULL,
                "MYCOL", "J", "w", FUN_OFFSET(Ev, mycol),
                NULL);
</code></pre>
<p> Once the <font SIZE="-1">FUN_OPS</font> variable has been reset, the next I/O call on the output extension will output the header, as expected.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
