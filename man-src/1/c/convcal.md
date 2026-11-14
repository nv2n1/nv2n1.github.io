---
title: "convcal(1)"
name: "convcal"
section: "1"
letter: "c"
url: "/docs/linux/man/1-convcal/"
description: "convcal – convert dates to different formats"
---

<h2>NAME</h2>
<p> convcal &#8211; convert dates to different formats </p>
<h2>SYNOPSIS</h2>
<p> <code>convcal</code> [<i>OPTIONS</i>] [<i>DATE</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>convcal</code> is part of the <i>grace</i> software package, an application for two-dimensional data visualization. <code>convcal</code> converts dates from and to various formats. The following date formats are supported (hour, minutes and seconds are always optional): </p>
<dl>
<dt><i>iso</i></p>
<dd> 1999-12-31T23:59:59.999</p>
<dt><i>european</i></p>
<dd> 31/12/1999 23:59:59.999 or 31/12/99 23:59:59.999</p>
<dt><i>us</i></p>
<dd> 12/31/1999 23:59:59.999 or 12/31/99 23:59:59.999</p>
<dt><i>days</i></p>
<dd> 123456.789</p>
<dt><i>seconds</i></p>
<dd> 123456.789 </p>
</dl>
<h2></h2>
<p> The formats are tried in the following order : users&#8217;s choice, iso, european and us (there is no ambiguity between calendar formats and numerical formats and therefore no order is specified for them). </p>
<h2>USAGE</h2>
<p> <code>convcal</code> reads the dates either on the command line or in the standard input if the command line contains no date. </p>
<p> The user&#8217;s choice for the input format put one format before the other ones in the trial list, this is mainly useful for US citizen which would certainly prefer to have US format checked before european format. The default user&#8217;s choice (nohint) does nothing so the following formats of the list are checked. </p>
<p> The separators between various fields can be any characters in the set: &quot; :/.-T&quot;. One or more spaces act as one separator, other characters can not be repeated, the T separator is allowed only between date and time, mainly for iso8601. So the string &quot;1999-12 31:23-59&quot; is allowed (but not recommended). The &#8216;-&#8216; character is used both as a separator (it is traditionally used in iso8601 format) and as the unary minus (for dates in the far past or for numerical dates). When the year is between 0 and 99 and is written with two or less digits, it is mapped to the era beginning at wrap year and ending at wrap year + 99 as follows : </p>
<p> [wy ; 99] -&gt; [ wrap_year ; 100*(1 + wrap_year/100) &#8211; 1 ] </p>
<p> [00 ; wy-1] -&gt; [ 100*(1 + wrap_year/100) ; wrap_year + 99] </p>
<p> so for example if the wrap year is set to 1950 (which is the default value), then the mapping is : </p>
<p> range [00 ; 49] is mapped to [2000 ; 2049] </p>
<p> range [50 ; 99] is mapped to [1950 ; 1999] </p>
<p> this is reasonably Y2K compliant and is consistent with current use. Specifying year 1 is still possible using more than two digits as follows : &quot;0001-03-04&quot; is unambiguously March the 4th, year 1, even if the user&#8217;s choice is us format. However using two digits only is not recommended (we introduce a 2050 bug here so this feature should be removed at some point in the future ;-) </p>
<p> Numerical dates (days and seconds formats) can be specified using integer, real or exponential formats (the &#8216;d&#8217; and &#8216;D&#8217; exponant markers from fortran are supported in addition to &#8216;e&#8217; and &#8216;E&#8217;). They are computed according to a customizable reference date. The default value is given by the REFDATE constant in the source file. You can change this value as you want before compiling, and you can change it at will using the -r command line option. The default value in the distributed file is &quot;-4713-01-01T12:00:00&quot;, it is a classical reference for astronomical events (note that the &#8216;-&#8216; is used here both as a unary minus and as a separator). </p>
<p> The program can be used either for Denys&#8217;s and gregorian calendars. It does not take into account leap seconds : you can think it works only in International Atomic Time (TAI) and not in Coordinated Unified Time (UTC) &#8230; Inexistant dates are detected, they include year 0, dates between 1582-10-05 and 1582-10-14, February 29th of non leap years, months below 1 or above 12, &#8230; </p>
<h2>OPTIONS</h2>
<p> A summary of the options supported by <code>convcal</code> is included below. </p>
<dl>
<dt><code>-h</code></p>
<dd> prints the help message on stderr and exits successfully</p>
<dt><code>-i</code> <i>format</i></p>
<dd> set user&#8217;s choice for input format, supported formats are iso, european, us, days, seconds and nohint. At the beginning the input format is nohint, which means the program try to guess the format by itself, if the user&#8217;s choice does not allow to parse the date, other formats are tried</p>
<dt><code>-o</code> <i>format</i></p>
<dd> force output format, supported formats are iso, european, us, days, seconds and nohint. At the beginning, the output format is nohint, which means the program uses days format for dates read in any calendar format and uses iso8601 for dates read in numerical format</p>
<dt><code>-r</code> <i>date</i></p>
<dd> set reference date (the date is read using the current input format) at the beginning the reference is set according to the REFDATE constant in the code, which is -4713-01-01T12:00:00 in the distributed file.</p>
<dt><code>-w</code> <i>year</i></p>
<dd> set the wrap year to year </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grace/">grace</a>(1)</code> </p>
<p> <i><a rel="nofollow" href="http://plasma-gate.weizmann.ac.il/Grace/">http://plasma-gate.weizmann.ac.il/Grace/</a></i> </p>
<h2>AUTHOR</h2>
<p> Luc Maisonobe </p>
<p> This man-page was written by Jan Schaumann &lt;jschauma [at] netmeister.org&gt; as part of &quot;The Missing Man Pages Project&quot;. Please see <i><a rel="nofollow" href="http://www.netmeister.org/misc/m2p2/index.html">http://www.netmeister.org/misc/m2p2/index.html</a></i> for details. </p>
<h2>Index</h2>
