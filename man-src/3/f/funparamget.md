---
title: "funparamget(3)"
name: "funparamget"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funparamget/"
description: "FunParamGet – get a Funtools param value"
---

<h2>NAME</h2>
<p> <code>FunParamGet &#8211; get a Funtools param value</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p>int FunParamGetb(Fun fun, char *name, int n, int defval, int *got)</p>
<p>int FunParamGeti(Fun fun, char *name, int n, int defval, int *got)</p>
<p>double FunParamGetd(Fun fun, char *name, int n, double defval, int *got)</p>
<p>char *FunParamGets(Fun fun, char *name, int n, char *defval, int *got)</p>
<h2>DESCRIPTION</h2>
<p> The four routines FunParamGetb(), FunParamGeti(), FunParamGetd(), and FunParamGets(), return the value of a <font SIZE="-1">FITS</font> header parameter as a boolean, int, double, and string, respectively. The string returned by FunParamGets() is a malloc&#8217;ed copy of the header value and should be freed when no longer needed. </p>
<p> The first argument is the Fun handle associated with the <font SIZE="-1">FITS</font> header being accessed. Normally, the header is associated with the <font SIZE="-1">FITS</font> extension that you opened with FunOpen(). However, you can use <i>FunInfoPut()</i> to specify access of the primary header. In particular, if you set the <font SIZE="-1">FUN_PRIMARYHEADER</font> parameter to 1, then the primary header is used for all parameter access until the value is reset to 0. For example: </p>
<p>int val;<br />
FunParamGeti(fun, &#8220;NAXIS&#8221;, 1, 0, &amp;got);<br />
#current header<br />
    val = 1;<br />
FunInfoPut(fun, FUN_PRIMARYHEADER, &amp;val, 0);<br />
#switch to&#8230; FunParamGeti(fun, &#8220;NAXIS&#8221;, 1, 0, &amp;got);<br />
#&#8230; primary header FunParamGeti(fun, &#8220;NAXIS&#8221;, 2, 0, &amp; got);<br />
#&#8230; primary header val = 0;<br />
FunInfoPut(fun, FUN_PRIMARYHEADER, &amp;val, 0);<br />
#switch back to&#8230; FunParamGeti(fun, &#8220;NAXIS&#8221;, 2, 0, &amp;got);<br />
#current header</p>
<p> Alternatively, you can use the <font SIZE="-1">FUN_PRIMARY</font> macro to access parameters from the primary header on a per-parameter basis: </p>
<p>FunParamGeti(fun, &#8220;NAXIS1&#8221;, 0, 0, &amp;got);<br />
#current header<br />
    FunParamGeti(FUN_PRIMARY(fun), &#8220;NAXIS1&#8221;, 0, 0, &amp;got);<br />
#primary header</p>
<p> <font SIZE="-1"><code>NB:</code></font><font SIZE="-1"><code>FUN_PRIMARY</code></font><code> is deprecated.</code> It makes use of a global parameter and therefore will not not appropriate for threaded applications, when we make funtools thread-safe. We recommend use of <i>FunInfoPut()</i> to switch between the extension header and the primary header. </p>
<p> For output data, access to the primary header is only possible until the header is written out, which usually takes place when the first data are written. </p>
<p> The second argument is the name of the parameter to access. The third <code>n</code> argument, if non-zero, is an integer that will be added as a suffix to the parameter name. This makes it easy to use a simple loop to process parameters having the same root name. For example, to gather up all values of <font SIZE="-1">TLMIN</font> and <font SIZE="-1">TLMAX</font> for each column in a binary table, you can use: </p>
<p>for (i = 0, got = 1; got; i++) {<br />
    fun-&gt;cols[i]-&gt;tlmin = (int)FunParamGeti(fun, &#8220;TLMIN&#8221;, i + 1, 0.0, &amp;got);<br />
    fun-&gt;cols[i]-&gt;tlmax = (int)FunParamGeti(fun, &#8220;TLMAX&#8221;, i + 1, 0.0, &amp;got);<br />
}</p>
<p> The fourth <code>defval</code> argument is the default value to return if the parameter does not exist. Note that the data type of this parameter is different for each specific <i>FunParamGet()</i> call. The final <code>got</code> argument will be 0 if no param was found. Otherwise the data type of the parameter is returned as follows: <font SIZE="-1">FUN_PAR_UNKNOWN</font> (&#8216;u&#8217;), <font SIZE="-1">FUN_PAR_COMMENT</font> (&#8216;c&#8217;), <font SIZE="-1">FUN_PAR_LOGICAL</font> (&#8216;l&#8217;), <font SIZE="-1">FUN_PAR_INTEGER</font> (&#8216;i&#8217;), <font SIZE="-1">FUN_PAR_STRING</font> (&#8216;s&#8217;), <font SIZE="-1">FUN_PAR_REAL</font> (&#8216;r&#8217;), <font SIZE="-1">FUN_PAR_COMPLEX</font> (&#8216;x&#8217;). </p>
<p> These routines return the value of the header parameter, or the specified default value if the header parameter does not exist. The returned value is a malloc&#8217;ed string and should be freed when no longer needed. </p>
<p> By default, FunParamGets() returns the string value of the named parameter. However, you can use <i>FunInfoPut()</i> to retrieve the raw 80-character <font SIZE="-1">FITS</font> card instead. In particular, if you set the <font SIZE="-1">FUN_RAWPARAM</font> parameter to 1, then card images will be returned by <i>FunParamGets()</i> until the value is reset to 0. </p>
<p> Alternatively, if the <font SIZE="-1">FUN_RAW</font> macro is applied to the name, then the 80-character raw <font SIZE="-1">FITS</font> card is returned instead. <font SIZE="-1"><code>NB:</code></font><font SIZE="-1"><code>FUN_RAW</code></font><code> is deprecated.</code> It makes use of a global parameter and therefore will not not appropriate for threaded applications, when we make funtools thread-safe. We recommend use of <i>FunInfoPut()</i> to switch between the extension header and the primary header. </p>
<p> Note that in addition to the behaviors described above, the routine FunParamGets() will return the 80 raw characters of the <code>nth</code> <font SIZE="-1">FITS</font> card (including the comment) if <code>name</code> is specified as <font SIZE="-1">NULL</font> and <code>n</code> is positive. For example, to loop through all <font SIZE="-1">FITS</font> header cards in a given extension and print out the raw card, use: </p>
<pre><code>
for (i = 1;; i++) {
    if ((s = FunParamGets(fun, NULL, i, NULL, &amp;got))) {
        fprintf(stdout, "%.80s
", s);
        free(s);
    } else {
        break;
    }
}
</code></pre>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
