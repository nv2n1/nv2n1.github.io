---
title: "tcl_scanelement(3)"
name: "tcl_scanelement"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_scanelement/"
description: "Tcl_SplitList, Tcl_Merge, Tcl_ScanElement, Tcl_ConvertElement, Tcl_ScanCountedElement, Tcl_ConvertCountedElement – manipulate Tcl lists"
---

<p>Tcl_SplitList, Tcl_Merge, Tcl_ScanElement, Tcl_ConvertElement, Tcl_ScanCountedElement, Tcl_ConvertCountedElement &#8211; manipulate Tcl lists </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_SplitList</code>(<i>interp, list, argcPtr, argvPtr</i>)
char *
<code>Tcl_Merge</code>(<i>argc, argv</i>)
int
<code>Tcl_ScanElement</code>(<i>src, flagsPtr</i>)
int
<code>Tcl_ScanCountedElement</code>(<i>src, length, flagsPtr</i>)
int
<code>Tcl_ConvertElement</code>(<i>src, dst, flags</i>)
int
<code>Tcl_ConvertCountedElement</code>(<i>src, length, dst, flags</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (out) Interpreter to use for error reporting. If NULL, then no error message is left.</p>
<dd>char <i>*list</i> (in) Pointer to a string with proper list structure.</p>
<dd>int <i>*argcPtr</i> (out) Filled in with number of elements in <i>list</i>.</p>
<dd>const char <i>***argvPtr</i> (out) <i>*argvPtr</i> will be filled in with the address of an array of pointers to the strings that are the extracted elements of <i>list</i>. There will be <i>*argcPtr</i> valid entries in the array, followed by a NULL entry.</p>
<dd>int <i>argc</i> (in) Number of elements in <i>argv</i>.</p>
<dd>const char *const <i>*argv</i> (in) Array of strings to merge together into a single list. Each string will become a separate element of the list.</p>
<dd>const char <i>*src</i> (in) String that is to become an element of a list.</p>
<dd>int <i>*flagsPtr</i> (in) Pointer to word to fill in with information about <i>src</i>. The value of *<i>flagsPtr</i> must be passed to <code>Tcl_ConvertElement</code>.</p>
<dd>int <i>length</i> (in) Number of bytes in string <i>src</i>.</p>
<dd>char <i>*dst</i> (in) Place to copy converted list element. Must contain enough characters to hold converted string.</p>
<dd>int <i>flags</i> (in) Information about <i>src</i>. Must be value returned by previous call to <code>Tcl_ScanElement</code>, possibly OR-ed with <code>TCL_DONT_USE_BRACES</code>. </p>
</dl>
<h2>Description</h2>
<p>These procedures may be used to disassemble and reassemble Tcl lists. <code>Tcl_SplitList</code> breaks a list up into its constituent elements, returning an array of pointers to the elements using <i>argcPtr</i> and <i>argvPtr</i>. While extracting the arguments, <code>Tcl_SplitList</code> obeys the usual rules for backslash substitutions and braces. The area of memory pointed to by <i>*argvPtr</i> is dynamically allocated; in addition to the array of pointers, it also holds copies of all the list elements. It is the caller&#8217;s responsibility to free up all of this storage. For example, suppose that you have called <code>Tcl_SplitList</code> with the following code:</p>
<dl COMPACT>
<dd>
<pre>int argc, code;
char *string;
char **argv;
...
code = Tcl_SplitList(interp, string, &amp;argc, &amp;argv);</pre>
</dl>
<p> Then you should eventually free the storage with a call like the following:</p>
<dl COMPACT>
<dd>
<pre>Tcl_Free((char *) argv);</pre>
</dl>
<p> <code>Tcl_SplitList</code> normally returns <code>TCL_OK</code>, which means the list was successfully parsed. If there was a syntax error in <i>list</i>, then <code>TCL_ERROR</code> is returned and the interpreter&#8217;s result will point to an error message describing the problem (if <i>interp</i> was not NULL). If <code>TCL_ERROR</code> is returned then no memory is allocated and <i>*argvPtr</i> is not modified. </p>
<p> <code>Tcl_Merge</code> is the inverse of <code>Tcl_SplitList</code>: it takes a collection of strings given by <i>argc</i> and <i>argv</i> and generates a result string that has proper list structure. This means that commands like <code>index</code> may be used to extract the original elements again. In addition, if the result of <code>Tcl_Merge</code> is passed to <code>Tcl_Eval</code>, it will be parsed into <i>argc</i> words whose values will be the same as the <i>argv</i> strings passed to <code>Tcl_Merge</code>. <code>Tcl_Merge</code> will modify the list elements with braces and/or backslashes in order to produce proper Tcl list structure. The result string is dynamically allocated using <code>Tcl_Alloc</code>; the caller must eventually release the space using <code>Tcl_Free</code>. </p>
<p> If the result of <code>Tcl_Merge</code> is passed to <code>Tcl_SplitList</code>, the elements returned by <code>Tcl_SplitList</code> will be identical to those passed into <code>Tcl_Merge</code>. However, the converse is not true: if <code>Tcl_SplitList</code> is passed a given string, and the resulting <i>argc</i> and <i>argv</i> are passed to <code>Tcl_Merge</code>, the resulting string may not be the same as the original string passed to <code>Tcl_SplitList</code>. This is because <code>Tcl_Merge</code> may use backslashes and braces differently than the original string. </p>
<p> <code>Tcl_ScanElement</code> and <code>Tcl_ConvertElement</code> are the procedures that do all of the real work of <code>Tcl_Merge</code>. <code>Tcl_ScanElement</code> scans its <i>src</i> argument and determines how to use backslashes and braces when converting it to a list element. It returns an overestimate of the number of characters required to represent <i>src</i> as a list element, and it stores information in <i>*flagsPtr</i> that is needed by <code>Tcl_ConvertElement</code>. </p>
<p> <code>Tcl_ConvertElement</code> is a companion procedure to <code>Tcl_ScanElement</code>. It does the actual work of converting a string to a list element. Its <i>flags</i> argument must be the same as the value returned by <code>Tcl_ScanElement</code>. <code>Tcl_ConvertElement</code> writes a proper list element to memory starting at *<i>dst</i> and returns a count of the total number of characters written, which will be no more than the result returned by <code>Tcl_ScanElement</code>. <code>Tcl_ConvertElement</code> writes out only the actual list element without any leading or trailing spaces: it is up to the caller to include spaces between adjacent list elements. </p>
<p> <code>Tcl_ConvertElement</code> uses one of two different approaches to handle the special characters in <i>src</i>. Wherever possible, it handles special characters by surrounding the string with braces. This produces clean-looking output, but cannot be used in some situations, such as when <i>src</i> contains unmatched braces. In these situations, <code>Tcl_ConvertElement</code> handles special characters by generating backslash sequences for them. The caller may insist on the second approach by OR-ing the flag value returned by <code>Tcl_ScanElement</code> with <code>TCL_DONT_USE_BRACES</code>. Although this will produce an uglier result, it is useful in some special situations, such as when <code>Tcl_ConvertElement</code> is being used to generate a portion of an argument for a Tcl command. In this case, surrounding <i>src</i> with curly braces would cause the command not to be parsed correctly. </p>
<p> By default, <code>Tcl_ConvertElement</code> will use quoting in its output to be sure the first character of an element is not the hash character (&#8220;#&#8221;.) This is to be sure the first element of any list passed to <code>eval</code> is not mis-parsed as the beginning of a comment. When a list element is not the first element of a list, this quoting is not necessary. When the caller can be sure that the element is not the first element of a list, it can disable quoting of the leading hash character by OR-ing the flag value returned by <code>Tcl_ScanElement</code> with <code>TCL_DONT_QUOTE_HASH</code>. </p>
<p> <code>Tcl_ScanCountedElement</code> and <code>Tcl_ConvertCountedElement</code> are the same as <code>Tcl_ScanElement</code> and <code>Tcl_ConvertElement</code>, except the length of string <i>src</i> is specified by the <i>length</i> argument, and the string may contain embedded nulls. </p>
<h2>Keywords</h2>
<p>backslash, convert, element, list, merge, split, strings</p>
