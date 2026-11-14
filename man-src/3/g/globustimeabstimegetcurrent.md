---
title: "globustimeabstimegetcurrent(3)"
name: "globustimeabstimegetcurrent"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globustimeabstimegetcurrent/"
description: "globus_time.h –"
---

<p>globus_time.h &#8211; </p>
<p> Time Types and Macros.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_types.h&#8217;<br />
 #include &lt;time.h&gt; </p>
<h3>Macros</h3>
<p>#define <code>GlobusTimeAbstimeSet</code>(Abstime, Sec, USec) </p>
<p> #define <code>GlobusTimeAbstimeGet</code>(Abstime, Sec, USec) </p>
<p> #define <code>GlobusTimeReltimeSet</code>(Reltime, Sec, USec) </p>
<p> #define <code>GlobusTimeAbstimeDiff</code>(Reltime, T1, T2) </p>
<p> #define <code>GlobusTimeReltimeToUSec</code>(SlpInt, Reltime) </p>
<p> #define <code>GlobusTimeReltimeToMilliSec</code>(Milliseconds, Reltime) </p>
<p> #define <code>GlobusTimeAbstimeInc</code>(Abstime, Reltime) </p>
<p> #define <code>GlobusTimeAbstimeGetCurrent</code>(Abstime) </p>
<p> #define <code>GlobusTimeAbstimeCopy</code>(Dest, Src) </p>
<p> #define <code>GlobusTimeReltimeCopy</code>(Dest, Src) </p>
<p> #define <code>GlobusTimeReltimeMultiply</code>(Reltime, Factor) </p>
<p> #define <code>GlobusTimeReltimeDivide</code>(Reltime, Factor) </p>
<h3>Functions</h3>
<p><code>globus_bool_t</code> <code>globus_time_has_expired</code> (const globus_abstime_t *abstime) </p>
<p> <code>globus_bool_t</code> <code>globus_time_abstime_is_infinity</code> (const globus_abstime_t *abstime) </p>
<p> <code>globus_bool_t</code> <code>globus_time_reltime_is_infinity</code> (const globus_reltime_t *reltime) </p>
<p> int <code>globus_abstime_cmp</code> (const globus_abstime_t *abstime_1, const globus_abstime_t *abstime_2) </p>
<p> int <code>globus_reltime_cmp</code> (const globus_reltime_t *reltime_1, const globus_reltime_t *reltime_2) </p>
<h2>Detailed Description</h2>
<p>Time Types and Macros. </p>
<h2>Macro Definition Documentation</h2>
<h3>#define GlobusTimeAbstimeCopy(Dest, Src)</h3>
<p><code>Value:</code> </p>
<pre>{ (Dest).tv_sec = (Src).tv_sec; (Dest).tv_nsec = (Src).tv_nsec; }</pre>
<p>Copy the absolute time</p>
<h3>#define GlobusTimeAbstimeDiff(Reltime, T1, T2)</h3>
<p><code>Value:</code> </p>
<pre>{ int __res = globus_abstime_cmp(&amp;(T1), &amp;(T2)); if(__res &lt; 0) { (Reltime).tv_sec = (T2).tv_sec - (T1).tv_sec; (Reltime).tv_usec = (((T2).tv_nsec - (T1).tv_nsec) / 1000); if((Reltime).tv_usec &lt; 0) { (Reltime).tv_sec--; (Reltime).tv_usec += 1000000; } } else if(__res &gt; 0) { (Reltime).tv_sec = (T1).tv_sec - (T2).tv_sec; (Reltime).tv_usec = (((T1).tv_nsec - (T2).tv_nsec) / 1000); if((Reltime).tv_usec &lt; 0) { (Reltime).tv_sec--; (Reltime).tv_usec += 1000000; } } else { (Reltime).tv_sec = 0; (Reltime).tv_usec = 0; } }</pre>
<p>Find the difference between the 2 absolute times.</p>
<h3>#define GlobusTimeAbstimeGet(Abstime, Sec, USec)</h3>
<p><code>Value:</code> </p>
<pre>{ Sec = (Abstime).tv_sec; USec = ((Abstime).tv_nsec / 1000); }</pre>
<p>Seperates abstime structure into its components,sec and usec.</p>
<h3>#define GlobusTimeAbstimeGetCurrent(Abstime)</h3>
<p><code>Value:</code> </p>
<pre>{ struct timeval __time; gettimeofday(&amp;__time, GLOBUS_NULL); (Abstime).tv_sec = __time.tv_sec; (Abstime).tv_nsec = (__time.tv_usec * 1000); }</pre>
<p>Get the current time</p>
<h3>#define GlobusTimeAbstimeInc(Abstime, Reltime)</h3>
<p><code>Value:</code> </p>
<pre>{ (Abstime).tv_nsec += ((Reltime).tv_usec * 1000); if((Abstime).tv_nsec &gt;= 1000000000) { (Abstime).tv_sec++; (Abstime).tv_nsec -= 1000000000; } (Abstime).tv_sec += (Reltime).tv_sec; }</pre>
<p>Add reltime to abstime</p>
<h3>#define GlobusTimeAbstimeSet(Abstime, Sec, USec)</h3>
<p><code>Value:</code> </p>
<pre>{ \
 GlobusTimeAbstimeGetCurrent(Abstime); (Abstime).tv_nsec += (USec * 1000); if((Abstime).tv_nsec &gt;= 1000000000) { (Abstime).tv_sec += ((Abstime).tv_nsec / 1000000000); (Abstime).tv_nsec = (Abstime).tv_nsec % 1000000000; } (Abstime).tv_sec += Sec; }</pre>
<p>Set the abstime structure to the sec and usec parameter values.</p>
<h3>#define GlobusTimeReltimeCopy(Dest, Src)</h3>
<p><code>Value:</code> </p>
<pre>{ (Dest).tv_sec = (Src).tv_sec; (Dest).tv_usec = (Src).tv_usec; }</pre>
<p>Copy the relative time</p>
<h3>#define GlobusTimeReltimeDivide(Reltime, Factor)</h3>
<p><code>Value:</code> </p>
<pre>{ (Reltime).tv_usec /= Factor; (Reltime).tv_sec /= Factor; }</pre>
<p>divide the reltime by factor</p>
<h3>#define GlobusTimeReltimeMultiply(Reltime, Factor)</h3>
<p><code>Value:</code> </p>
<pre>{ (Reltime).tv_usec *= Factor; (Reltime).tv_sec *= Factor; if((Reltime).tv_usec &gt;= 1000000) { (Reltime).tv_sec += ((Reltime).tv_usec / 1000000); (Reltime).tv_usec = (Reltime).tv_usec % 1000000; } }</pre>
<p>Multiple the reltime by factor</p>
<h3>#define GlobusTimeReltimeSet(Reltime, Sec, USec)</h3>
<p><code>Value:</code> </p>
<pre>{ (Reltime).tv_usec = (USec); (Reltime).tv_sec = Sec; if((Reltime).tv_usec &gt;= 1000000) { (Reltime).tv_sec += ((Reltime).tv_usec / 1000000); (Reltime).tv_usec = (Reltime).tv_usec % 1000000; } }</pre>
<p>Set the reltime structure to the sec and usec parameter values.</p>
<h3>#define GlobusTimeReltimeToMilliSec(Milliseconds, Reltime)</h3>
<p><code>Value:</code> </p>
<pre>{ Milliseconds = ((Reltime).tv_sec * 1000) + ((Reltime).tv_usec)/ 1000; }</pre>
<p>Convert a relative time into a long in millisec units</p>
<h3>#define GlobusTimeReltimeToUSec(SlpInt, Reltime)</h3>
<p><code>Value:</code> </p>
<pre>{ SlpInt = ((Reltime).tv_sec * 1000000) + ((Reltime).tv_usec); }</pre>
<p>Convert a relitive time into a long in usec units</p>
<h2>Function Documentation</h2>
<h3>int globus_abstime_cmp (const globus_abstime_t *abstime_1, const globus_abstime_t *abstime_2)</h3>
<p>Compare two absolute times. </p>
<p> This function returns an integer that reflects the comparison of two abstimes in the following way. </p>
<p> 0 : values are the same. -1 : the first value is less than the second. 1 : the first value is greater than the second.</p>
<h3>int globus_reltime_cmp (const globus_reltime_t *reltime_1, const globus_reltime_t *reltime_2)</h3>
<p>Compare two absolute times. </p>
<p> This function returns an integer that reflects the comparison of two reltimes in the following way. </p>
<p> 0 : values are the same. -1 : the first value is less than the second. 1 : the first value is greater than the second.</p>
<h3><code>globus_bool_t</code> globus_time_abstime_is_infinity (const globus_abstime_t *abstime)</h3>
<p>Returns a boolean that reflects whether or not abstime is infinity.</p>
<h3><code>globus_bool_t</code> globus_time_has_expired (const globus_abstime_t *abstime)</h3>
<p>Has abstime expired </p>
<p> Returns a boolean that reflects whether or not abstime is less than the current time.</p>
<h3><code>globus_bool_t</code> globus_time_reltime_is_infinity (const globus_reltime_t *reltime)</h3>
<p>Returns a boolean that reflects whether or not reltime is infinity.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
