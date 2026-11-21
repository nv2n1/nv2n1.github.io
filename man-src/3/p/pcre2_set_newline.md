---

title: "pcre2_set_newline(3)"
name: "pcre2_set_newline"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_newline/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API) </p>
<p> <code>#include &lt;pcre2.h&gt;</code> </p>
<pre><code>
 int pcre2_set_newline(pcre2_compile_context *  ccontext ,
   uint32_t  value );
</code></pre>
<p>This function sets the newline convention within a compile context. This specifies which character(s) are recognized as newlines when compiling and matching patterns. The second argument must be one of: </p>
<p> <br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_CR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Carriage return only <br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_LF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Linefeed only <br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_CRLF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CR followed by LF only <br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_ANYCRLF&nbsp;<wbr>&nbsp;<wbr>&nbsp;Any of the above <br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_ANY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Any Unicode newline sequence <br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_NUL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The NUL character&nbsp;(binary zero) </p>
<p>The result is zero for success or PCRE2_ERROR_BADDATA if the second argument is invalid. </p>
<p>There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
