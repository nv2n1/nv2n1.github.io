---
title: "byobu-ulevel(1)"
name: "byobu-ulevel"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byobu-ulevel/"
description: "byobu-ulevel – helper script for notification level indicators"
---

<h2>NAME</h2>
<p> <code>byobu-ulevel </code> &#8211; helper script for notification level indicators </p>
<h2>DESCRIPTION</h2>
<p> <code>byobu-ulevel</code> is a helper script that can be used to create history graphs with UTF8 characters </p>
<h2>USAGE</h2>
<p> <code>byobu-ulevel </code> [options] -c &lt;current_num&gt; </p>
<p> <code>byobu-ulevel </code> [options] &lt;current_num&gt; </p>
<p> <code>byobu-ulevel </code> &lt;current_num&gt; </p>
<h2>OPTIONS</h2>
<p>&nbsp;<wbr>-a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Accessibility mode: only output ASCII.&nbsp;<wbr>&nbsp;<wbr>(Also enabled if variable&nbsp;<wbr>&#8216;$a11y_variable&#8217;&nbsp;<wbr>set).<br />
&nbsp;<wbr>-b&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Display current value as space if zero, rather than lowest&nbsp;<wbr>&#8216;value&#8217;&nbsp;<wbr>of theme.<br />
&nbsp;<wbr>-c&nbsp;<wbr>&lt;num&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Current value of your indicator.<br />
&nbsp;<wbr>-d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Enable debug output.<br />
&nbsp;<wbr>-e&nbsp;<wbr>&lt;int&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Number of decimal places to use for accessibility mode&nbsp;<wbr>(default=$default_decimal_places).<br />
&nbsp;<wbr>-h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Show this help.<br />
&nbsp;<wbr>-i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Invert colour scheme&nbsp;<wbr>(rating themes only).<br />
&nbsp;<wbr>-l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: List available themes. If&nbsp;<wbr>&#8216;-t&#8217;&nbsp;<wbr>also specified, show all values for specified theme.<br />
&nbsp;<wbr>-m&nbsp;<wbr>&lt;num&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Minimum value&nbsp;<wbr>(default=$min_default).<br />
&nbsp;<wbr>-n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Supress output of newline character.<br />
&nbsp;<wbr>-p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Permissive mode &#8211; if current value out of bounds, set it to the nearest bound&nbsp;<wbr>(min or max).<br />
&nbsp;<wbr>-q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Suppress messages&nbsp;<wbr>(requires&nbsp;<wbr>&#8216;-t&#8217;).<br />
&nbsp;<wbr>-r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Reverse&nbsp;<wbr>&#8216;direction&#8217;&nbsp;<wbr>of display&nbsp;<wbr>(rating theme only).<br />
&nbsp;<wbr>-t&nbsp;<wbr>&lt;theme&gt;&nbsp;<wbr>&nbsp;<wbr>: Name of theme&nbsp;<wbr>(default=$theme_default).<br />
&nbsp;<wbr>-u&nbsp;<wbr>&lt;chars&gt;&nbsp;<wbr>&nbsp;<wbr>: Specify a user theme&nbsp;<wbr>(2 or more values).<br />
&nbsp;<wbr>-w&nbsp;<wbr>&lt;int&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Width of rating theme&nbsp;<wbr>(default=$width_default).<br />
&nbsp;<wbr>-x&nbsp;<wbr>&lt;num&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Maximum value&nbsp;<wbr>(default=$max_default). </p>
<h2>EXAMPLES</h2>
<p> Display character representing 27% using default theme.<br />
&nbsp;<wbr>&nbsp;<wbr>byobu-ulevel 27 </p>
<p> As above.<br />
&nbsp;<wbr>&nbsp;<wbr>byobu-ulevel -c 27 </p>
<p> Example showing floating-point and negative values.<br />
&nbsp;<wbr>&nbsp;<wbr>byobu-ulevel -c 1.100001 -m -5.00234 -x 2.71828 -t dice_6 </p>
<p> Use accessibility mode to display a percentage value (rounded to nearest percentage)<br />
&nbsp;<wbr>&nbsp;<wbr>byobu-ulevel -m -22.613 -x 5.00212 -c 0.10203 -a -e 0 </p>
<p> Display value using a &quot;rating theme&quot; (displayed left-to-right).<br />
&nbsp;<wbr>&nbsp;<wbr>byobu-ulevel -c 83 -t stars_2 </p>
<p> Display right-to-left inverted &quot;rating theme&quot;.<br />
&nbsp;<wbr>&nbsp;<wbr>byobu-ulevel -c 60 -t diamonds_2 -ri </p>
<p> Display all glyphs in &#8216;solid_numbers_a_10&#8217; theme.<br />
&nbsp;<wbr>&nbsp;<wbr>byobu-ulevel -l -t solid_numbers_a_10 </p>
<p> Display a user-specified rating theme 10 glyphs wide.<br />
&nbsp;<wbr>&nbsp;<wbr>byobu-ulevel -c 666.321 -m -273.15 -x 1370 -u&nbsp;<wbr>&quot;·&nbsp;<wbr>&#x2622;&quot;&nbsp;<wbr>-w 10 </p>
<p> A multi-element user theme (this prints &#8216;e&#8217;).<br />
&nbsp;<wbr>&nbsp;<wbr>byobu-ulevel -c 50 -u&nbsp;<wbr>&quot;a b c d e f g h i j&quot; </p>
<h2>NOTES</h2>
<p> Arguments of type &quot;&lt;int&gt;&quot; denote an integer value, whereas arguments of type &quot;&lt;num&gt;&quot; denotes either an integer or a floating-point number. </p>
<p> The final &#8216;_&lt;number&gt;&#8217; in a theme name denotes the number of glyphs in it. </p>
<p> &quot;Rating themes&quot; are those with only 2 values. </p>
<p> The &lt;chars&gt; argument to &#8216;-u&#8217; must contain space-delimited characters. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1) </p>
<dl>
<dt><i><a rel="nofollow" href="http://byobu.co">http://byobu.co</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This utility was written by James Hunt &lt;james.hunt [at] canonical.com&gt;, and this manpage was written by Dustin Kirkland &lt;kirkland [at] byobu.co&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document and the utility under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> The complete text of the GNU General Public License can be found in <i>/usr/share/common-licenses/GPL</i> on Debian/Ubuntu systems, or in <i>/usr/share/doc/fedora-release-*/GPL</i> on Fedora systems, or on the web at <i><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a></i>. </p>
<h2>Index</h2>
