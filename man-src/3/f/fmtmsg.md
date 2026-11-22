---

title: "fmtmsg(3)"
name: "fmtmsg"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fmtmsg/"
description: "fmtmsg – print formatted error messages"
---

<p> fmtmsg &#8211; print formatted error messages </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fmtmsg.h&gt;
int fmtmsg(long classification, const char *label,
           int severity, const char *text,
           const char *action, const char *tag);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function displays a message described by its arguments on the device(s) specified in the <i>classification</i> argument. For messages written to <i>stderr</i>, the format depends on the <code>MSGVERB</code> environment variable. </p>
<p> The <i>label</i> argument identifies the source of the message. The string must consist of two colon separated parts where the first part has not more than 10 and the second part not more than 14 characters. </p>
<p> The <i>text</i> argument describes the condition of the error. </p>
<p> The <i>action</i> argument describes possible steps to recover from the error. If it is printed, it is prefixed by &quot;TO FIX: &quot;. </p>
<p> The <i>tag</i> argument is a reference to the online documentation where more information can be found. It should contain the <i>label</i> value and a unique identification number.</p>
<h3>Dummy arguments</h3>
<p> Each of the arguments can have a dummy value. The dummy classification value <code>MM_NULLMC</code> (0L) does not specify any output, so nothing is printed. The dummy severity value <code>NO_SEV</code> (0) says that no severity is supplied. The values <code>MM_NULLLBL</code>, <code>MM_NULLTXT</code>, <code>MM_NULLACT</code>, <code>MM_NULLTAG</code> are synonyms for <i>((char&nbsp;*)&nbsp;0)</i>, the empty string, and <code>MM_NULLSEV</code> is a synonym for <code>NO_SEV</code>.</p>
<h3>The classification argument</h3>
<p> The <i>classification</i> argument is the sum of values describing 4 types of information. </p>
<p> The first value defines the output channel.</p>
<dl>
<dt><code>MM_PRINT</code></dt>
<dd> Output to <i>stderr</i>.</dd>
<dt><code>MM_CONSOLE</code></dt>
<dd> Output to the system console.</dd>
<dt><code>MM_PRINT | MM_CONSOLE</code></dt>
<dd> Output to both.</dd></dl>
<p> The second value is the source of the error:</p>
<dl>
<dt><code>MM_HARD</code></dt>
<dd> A hardware error occurred.</dd>
<dt><code>MM_FIRM</code></dt>
<dd> A firmware error occurred.</dd>
<dt><code>MM_SOFT</code></dt>
<dd> A software error occurred.</dd></dl>
<p> The third value encodes the detector of the problem:</p>
<dl>
<dt><code>MM_APPL</code></dt>
<dd> It is detected by an application.</dd>
<dt><code>MM_UTIL</code></dt>
<dd> It is detected by a utility.</dd>
<dt><code>MM_OPSYS</code></dt>
<dd> It is detected by the operating system.</dd></dl>
<p> The fourth value shows the severity of the incident:</p>
<dl>
<dt><code>MM_RECOVER</code></dt>
<dd> It is a recoverable error.</dd>
<dt><code>MM_NRECOV</code></dt>
<dd> It is a nonrecoverable error.</dd></dl>
<h3>The severity argument</h3>
<p> The <i>severity</i> argument can take one of the following values:</p>
<dl>
<dt><code>MM_NOSEV</code></dt>
<dd> No severity is printed.</dd>
<dt><code>MM_HALT</code></dt>
<dd> This value is printed as HALT.</dd>
<dt><code>MM_ERROR</code></dt>
<dd> This value is printed as ERROR.</dd>
<dt><code>MM_WARNING</code></dt>
<dd> This value is printed as WARNING.</dd>
<dt><code>MM_INFO</code></dt>
<dd> This value is printed as INFO.</dd></dl>
<p> The numeric values are between 0 and 4. Using <code><a href="/docs/linux/man/3-addseverity/">addseverity</a></code>(3) or the environment variable <code>SEV_LEVEL</code> you can add more levels and strings to print.</p>
<h2>RETURN VALUE</h2>
<p> The function can return 4 values:</p>
<dl>
<dt><code>MM_OK</code></dt>
<dd> Everything went smooth.</dd>
<dt><code>MM_NOTOK</code></dt>
<dd> Complete failure.</dd>
<dt><code>MM_NOMSG</code></dt>
<dd> Error writing to <i>stderr</i>.</dd>
<dt><code>MM_NOCON</code></dt>
<dd> Error writing to the console.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> The environment variable <code>MSGVERB</code> (&quot;message verbosity&quot;) can be used to suppress parts of the output to <i>stderr</i>. (It does not influence output to the console.) When this variable is defined, is non-NULL, and is a colon-separated list of valid keywords, then only the parts of the message corresponding to these keywords is printed. Valid keywords are &quot;label&quot;, &quot;severity&quot;, &quot;text&quot;, &quot;action&quot; and &quot;tag&quot;. </p>
<p> The environment variable <code>SEV_LEVEL</code> can be used to introduce new severity levels. By default, only the five severity levels described above are available. Any other numeric value would make <code>fmtmsg</code>() print nothing. If the user puts <code>SEV_LEVEL</code> with a format like </p>
<dl>
<dt>
</dt><dd> SEV_LEVEL=[description[:description[:&#8230;]]]</dd></dl>
<p> in the environment of the process before the first call to <code>fmtmsg</code>(), where each description is of the form </p>
<dl>
<dt>
</dt><dd> severity-keyword,level,printstring</dd></dl>
<p> then <code>fmtmsg</code>() will also accept the indicated values for the level (in addition to the standard levels 0-4), and use the indicated printstring when such a level occurs. </p>
<p> The severity-keyword part is not used by <code>fmtmsg</code>() but it has to be present. The level part is a string representation of a number. The numeric value must be a number greater than 4. This value must be used in the severity argument of <code>fmtmsg</code>() to select this class. It is not possible to overwrite any of the predefined classes. The printstring is the string printed when a message of this class is processed by <code>fmtmsg</code>().</p>
<h2>VERSIONS</h2>
<p> <code>fmtmsg</code>() is provided in glibc since version 2.1.</p>
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
<td> <code>fmtmsg</code>() </td>
<td>Thread safety</td>
<td> glibc &gt;= 2.16: MT-Safe<br/>
 glibc &lt; 2.16: MT-Unsafe
</td>
</tr>
</table>
<p> Before glibc 2.16, the <code>fmtmsg</code>() function uses a static variable that is not protected, so it is not thread-safe. </p>
<p> Since glibc 2.16, the <code>fmtmsg</code>() function uses a lock to protect the static variable, so it is thread-safe.</p>
<h2>CONFORMING TO</h2>
<p> The functions <code>fmtmsg</code>() and <code><a href="/docs/linux/man/3-addseverity/">addseverity</a></code>(3), and environment variables <code>MSGVERB</code> and <code>SEV_LEVEL</code> come from System V. </p>
<p> The function <code>fmtmsg</code>() and the environment variable <code>MSGVERB</code> are described in POSIX.1-2001 and POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> System V and UnixWare man pages tell us that these functions have been replaced by &quot;pfmt() and addsev()&quot; or by &quot;pfmt(), vpfmt(), lfmt(), and vlfmt()&quot;, and will be removed later.</p>
<h2>EXAMPLES</h2>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;fmtmsg.h&gt; </p>
<p> int main(void) {<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long class&nbsp;=&nbsp;MM_PRINT | MM_SOFT | MM_OPSYS | MM_RECOVER;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int err; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;err&nbsp;=&nbsp;fmtmsg(class,&nbsp;&quot;util-linux:mount&quot;, MM_ERROR,<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;unknown mount option&quot;,&nbsp;&quot;See&nbsp;<a href="/docs/linux/man/8-mount/">mount</a>(8).&quot;,<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;util-linux:mount:017&quot;);<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(err)&nbsp;{<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case MM_OK:<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case MM_NOTOK:<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Nothing printed
&quot;);<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case MM_NOMSG:<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Nothing printed to stderr
&quot;);<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case MM_NOCON:<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;No console output
&quot;);<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Unknown error from fmtmsg()
&quot;);<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); } </p>
<p> The output should be: </p>
<p> util-linux:mount: ERROR: unknown mount option TO FIX: See <a href="/docs/linux/man/8-mount/">mount</a>(8). util-linux:mount:017 </p>
<p> and after </p>
<p> MSGVERB=text:action; export MSGVERB </p>
<p> the output becomes: </p>
<p> unknown mount option TO FIX: See <a href="/docs/linux/man/8-mount/">mount</a>(8).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-addseverity/">addseverity</a></code>(3), <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
