---
title: "regerror(3)"
name: "regerror"
section: "3"
letter: "r"
url: "/docs/linux/man/3-regerror/"
description: "regcomp, regexec, regerror, regfree – POSIX regex functions"
---

<p>regcomp, regexec, regerror, regfree &#8211; POSIX regex functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;regex.h&gt;
int regcomp(regex_t *preg, const char *regex, int cflags);
int regexec(const regex_t *preg, const char *string, size_t nmatch,
            regmatch_t pmatch[], int eflags);
size_t regerror(int errcode, const regex_t *preg, char *errbuf,
                size_t errbuf_size);
void regfree(regex_t *preg);</code></pre>
<h2>Description</h2>
<h3>POSIX regex compiling</h3>
<p><code>regcomp</code>() is used to compile a regular expression into a form that is suitable for subsequent <code>regexec</code>() searches. <code>regcomp</code>() is supplied with <i>preg</i>, a pointer to a pattern buffer storage area; <i>regex</i>, a pointer to the null-terminated string and <i>cflags</i>, flags used to determine the type of compilation. All regular expression searching must be done via a compiled pattern buffer, thus <code>regexec</code>() must always be supplied with the address of a <code>regcomp</code>() initialized pattern buffer. cflags</p>
<p>is the<br />
bitwise-or</p>
<p>of zero or more of the following:</p>
<p>REG_EXTENDED</p>
<p>Use<br />
POSIX</p>
<p>Extended Regular Expression syntax when interpreting<br />
regex.</p>
<p>If not set,<br />
POSIX</p>
<p>Basic Regular Expression syntax is used.<br />
REG_ICASE</p>
<p>Do not differentiate case.<br />
Subsequent<br />
regexec()</p>
<p>searches using this pattern buffer will be case insensitive.<br />
REG_NOSUB</p>
<p>Do not report position of matches.<br />
The<br />
nmatch</p>
<p>and<br />
pmatch</p>
<p>arguments to<br />
regexec()</p>
<p>are ignored if the pattern buffer supplied was compiled with this flag set.<br />
REG_NEWLINE</p>
<p>Match-any-character operators don&#8217;t match a newline.</p>
<p>A nonmatching list<br />
([ha&#8230;])</p>
<p>not containing a newline does not match a newline.</p>
<p>Match-beginning-of-line operator<br />
(ha)</p>
<p>matches the empty string immediately after a newline, regardless of<br />
whether<br />
eflags,</p>
<p>the execution flags of<br />
regexec(),</p>
<p>contains<br />
REG_NOTBOL.</p>
<p>Match-end-of-line operator<br />
($)</p>
<p>matches the empty string immediately before a newline, regardless of<br />
whether<br />
eflags</p>
<p>contains<br />
REG_NOTEOL.</p>
<p>POSIX regex matching</p>
<p>regexec()</p>
<p>is used to match a null-terminated string<br />
against the precompiled pattern buffer,<br />
preg.</p>
<p>nmatch</p>
<p>and<br />
pmatch</p>
<p>are used to provide information regarding the location of any matches.<br />
eflags</p>
<p>is the<br />
bitwise-or</p>
<p>of zero or more of the following flags:</p>
<p>REG_NOTBOL</p>
<p>The match-beginning-of-line operator always fails to match (but see the<br />
compilation flag<br />
REG_NEWLINE</p>
<p>above).<br />
This flag may be used when different portions of a string are passed to<br />
regexec()</p>
<p>and the beginning of the string should not be interpreted as the<br />
beginning of the line.<br />
REG_NOTEOL</p>
<p>The match-end-of-line operator always fails to match (but see the<br />
compilation flag<br />
REG_NEWLINE</p>
<p>above).<br />
REG_STARTEND</p>
<p>Use<br />
pmatch[0]</p>
<p>on the input string, starting at byte<br />
pmatch[0].rm_so</p>
<p>and ending before byte<br />
pmatch[0].rm_eo.</p>
<p>This allows matching embedded NUL bytes<br />
and avoids a<br />
strlen(3)</p>
<p>on large strings.<br />
It does not use<br />
nmatch</p>
<p>on input, and does not change<br />
REG_NOTBOL</p>
<p>or<br />
REG_NEWLINE</p>
<p>processing.<br />
This flag is a BSD extension, not present in POSIX.</p>
<p>Byte offsets</p>
<p>Unless<br />
REG_NOSUB</p>
<p>was set for the compilation of the pattern buffer, it is possible to<br />
obtain match addressing information.<br />
pmatch</p>
<p>must be dimensioned to have at least<br />
nmatch</p>
<p>elements.<br />
These are filled in by<br />
regexec()</p>
<p>with substring match addresses.<br />
The offsets of the subexpression starting at the<br />
ith</p>
<p>open parenthesis are stored in<br />
pmatch[i].</p>
<p>The entire regular expression&#8217;s match addresses are stored in<br />
pmatch[0].</p>
<p>(Note that to return the offsets of<br />
N</p>
<p>subexpression matches,<br />
nmatch</p>
<p>must be at least<br />
N+1.)</p>
<p>Any unused structure elements will contain the value -1. The <i>regmatch_t</i> structure which is the type of <i>pmatch</i> is defined in <i>&lt;regex.h&gt;</i>. typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regoff_t rm_so;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regoff_t rm_eo; } regmatch_t; Each <i>rm_so</i> element that is not -1 indicates the start offset of the next largest substring match within the string. The relative <i>rm_eo</i> element indicates the end offset of the match, which is the offset of the first character after the matching text.</p>
<h3>POSIX error reporting</h3>
<p><code>regerror</code>() is used to turn the error codes that can be returned by both <code>regcomp</code>() and <code>regexec</code>() into error message strings. <code>regerror</code>() is passed the error code, <i>errcode</i>, the pattern buffer, <i>preg</i>, a pointer to a character string buffer, <i>errbuf</i>, and the size of the string buffer, <i>errbuf_size</i>. It returns the size of the <i>errbuf</i> required to contain the null-terminated error message string. If both <i>errbuf</i> and <i>errbuf_size</i> are nonzero, <i>errbuf</i> is filled in with the first <i>errbuf_size &#8211; 1</i> characters of the error message and a terminating null byte (&#8216;\0&#8217;).  </p>
<h3>POSIX pattern buffer freeing</h3>
<p> Supplying <code>regfree</code>() with a precompiled pattern buffer, <i>preg</i> will free the memory allocated to the pattern buffer by the compiling process, <code>regcomp</code>().  </p>
<h2>RETURN VALUE</h2>
<p> <code>regcomp</code>() returns zero for a successful compilation or an error code for failure. </p>
<p> <code>regexec</code>() returns zero for a successful match or <code>REG_NOMATCH</code> for failure.  </p>
<h2>ERRORS</h2>
<p> The following errors can be returned by <code>regcomp</code>(): </p>
<dl>
<dt><code>REG_BADBR</code></dt>
<dd> <p> Invalid use of back reference operator. </p>
 </dd>
<dt><code>REG_BADPAT</code></dt>
<dd> <p> Invalid use of pattern operators such as group or list. </p>
 </dd>
<dt><code>REG_BADRPT</code></dt>
<dd> <p> Invalid use of repetition operators such as using &#8216;*&#8216; as the first character. </p>
 </dd>
<dt><code>REG_EBRACE</code></dt>
<dd> <p> Un-matched brace interval operators. </p>
 </dd>
<dt><code>REG_EBRACK</code></dt>
<dd> <p> Un-matched bracket list operators. </p>
 </dd>
<dt><code>REG_ECOLLATE</code></dt>
<dd> <p> Invalid collating element. </p>
 </dd>
<dt><code>REG_ECTYPE</code></dt>
<dd> <p> Unknown character class name. </p>
 </dd>
<dt><code>REG_EEND</code></dt>
<dd> <p> Nonspecific error. This is not defined by POSIX.2. </p>
 </dd>
<dt><code>REG_EESCAPE</code></dt>
<dd> <p> Trailing backslash. </p>
 </dd>
<dt><code>REG_EPAREN</code></dt>
<dd> <p> Un-matched parenthesis group operators. </p>
 </dd>
<dt><code>REG_ERANGE</code></dt>
<dd> <p> Invalid use of the range operator; for example, the ending point of the range occurs prior to the starting point. </p>
 </dd>
<dt><code>REG_ESIZE</code></dt>
<dd> <p> Compiled regular expression requires a pattern buffer larger than 64 kB. This is not defined by POSIX.2. </p>
 </dd>
<dt><code>REG_ESPACE</code></dt>
<dd> <p> The regex routines ran out of memory. </p>
 </dd>
<dt><code>REG_ESUBREG</code></dt>
<dd> <p> Invalid back reference to a subexpression. </p>
 </dd></dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>regcomp</code>(), <code>regexec</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>regerror</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env
</td>
</tr>
<tr VALIGN=top>
<td> <code>regfree</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.  </p>
<h2>EXAMPLES</h2>
<p> #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;regex.h&gt; </p>
<p> #define ARRAY_SIZE(arr) (sizeof((arr)) / sizeof((arr)[0])) </p>
<p> static const char *const str = <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;1)&nbsp;John Driverhacker;\n2)&nbsp;John Doe;\n3)&nbsp;John Foo;\n&quot;; static const char *const re = &quot;John.*o&quot;; </p>
<p> int main(void) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static const char&nbsp;*s&nbsp;=&nbsp;str; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regex_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regex; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regmatch_t&nbsp;<wbr>&nbsp;pmatch[1]; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regoff_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off, len; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(regcomp(&amp;regex, re, REG_NEWLINE)) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;String&nbsp;=&nbsp;\&quot;%s\&quot;\n&quot;, str); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Matches:\n&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;0;&nbsp;;&nbsp;i++)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(regexec(&amp;regex, s, ARRAY_SIZE(pmatch), pmatch, 0)) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off&nbsp;=&nbsp;pmatch[0].rm_so&nbsp;+&nbsp;(s &#8211; str); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len&nbsp;=&nbsp;pmatch[0].rm_eo &#8211; pmatch[0].rm_so; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;#%d:\n&quot;, i); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;offset&nbsp;=&nbsp;%jd;&nbsp;length&nbsp;=&nbsp;%jd\n&quot;,&nbsp;(intmax_t)&nbsp;off, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;len); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;substring&nbsp;=&nbsp;\&quot;%.*s\&quot;\n&quot;, len, s&nbsp;+&nbsp;pmatch[0].rm_so); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;+=&nbsp;pmatch[0].rm_eo; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) </p>
<p> The glibc manual section, <i>Regular Expressions</i>  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
