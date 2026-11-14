---
title: "idate(1)"
name: "idate"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idate/"
description: "idate – A Gregorian/Meladi to/from Hijri/Islamic date converter"
---

<h2 class="name">NAME</h2>
<p> idate &#8211; A Gregorian/Meladi to/from Hijri/Islamic date converter </p>
<h2>SYNOPSIS</h2>
<p> <code>idate</code> [<code>&#8211;gregorian</code> yyyymmdd<i>]</i> [<code>&#8211;hijri</code> yyyymmdd<i>]</i> [<code>&#8211;simple]</code> [<code>&#8211;umm_alqura</code>] [<code>&#8211;help</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>idate</code> program is a Gregorian to Hijri (and vice-versa) date converter. The application uses and offers multiple calculation methods with not all of them agreeing at all times. The reason for this multiplicity is due to not having one agreed upon method and so various entities develop and advocate their calculations. </p>
<p> <code>idate</code> is able to comprehend and calculate both pre-epoch or pre-Hijrah, denoted as &quot;B.H&quot;, as well as post-epoch or post-Hijrah, denoted as &quot;A.H&quot;, dates. <code>idate</code> also utilizes Gregorian&#8217;s pre-epoch &quot;B.C&quot; and post-epoch &quot;A.D&quot; dates and notes them per its output. When entering pre-epoch years, negative numbers ought to be utilized. </p>
<p> <code>idate</code> when run without any command-line options uses the host machine&#8217;s current Gregorian date and converts it to Hijri.</p>
<h2>OPTIONS</h2>
<p> <code>idate</code> follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of all options is noted below:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options</p>
<dt><code>-g, &#8211;gregorian </code><i>yyyymmdd</i></p>
<dd> Specify the Gregorian date to be converted where &#8216;y&#8217; stands for year, &#8216;m&#8217; for month and &#8216;d&#8217; for day</p>
<dt><code>-hi, &#8211;hijri </code><i>yyyymmdd</i></p>
<dd> Specify the Hijri date to be converted where &#8216;y&#8217; stands for year, &#8216;m&#8217; for month and &#8216;d&#8217; for day</p>
<dt><code>-s, &#8211;simple</code></p>
<dd> Specify a simplified output mode</p>
<dt><code>-u, &#8211;umm_alqura</code></p>
<dd> Specify to use the Umm Al-Qura calculation method (used mostly in Saudi Arabia)</dl>
<h2>BACKGROUND</h2>
<p> The Hijri calendar is used in most of the Arab world and is the symbolic calendar of the Islamic faithed worldwide. This calendar is known as the &quot;Hijri&quot; (based on the word &quot;Hijrah&quot; &#8211; denoting migration in Arabic) to signal Prophet Mohammed&#8217;s (PBUH) migration from Makkah to Medinah on Thursday, July 15, 622 AD (Julian) or July 19, 622 AD (Gregorian). </p>
<p> The Islamic Hijri calendar is strictly lunar (ie. moon-based) with twelve lunar months which do not correspond or track their solar counterparts (the Gregorian calendar is a solar or sun-based calendar). Lunar years and thus Hijri years are, on average, about 354 days long resulting in a Hijri year being roughly about 11 days shorter than its Gregorian counterpart. </p>
<p> There is much discussion and confusion regarding how best to track the Hijri calendar. A great deal of that confusion is based on the fact that many rely on a human moon sighting to denote the start (or end) of a month (each month of the Hijri calendar starts when a new moon&#8217;s crescent is observed or is made visible at sunset) as opposed to using an empirical mathematic certainty. The methods presented in this application and its underlying ITL library are strictly arithmetic in nature and do NOT take moon-phases into consideration (in short, observational approximation is not used).</p>
<h2>LIMITATIONS</h2>
<p> The Umm Al-Qura option doesn&#8217;t function with pre-epoch settings.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs on the web using <a rel="nofollow" href="http://bugs.arabeyes.org">http://bugs.arabeyes.org</a></p>
<h2>AUTHOR</h2>
<p> Written by Nadim Shaikli as part of the Arabeyes.org project.</p>
<h2>COPYRIGHT</h2>
<p> <code>idate</code> is subject to the GNU General Public License (GPL).<br />
 Copyright &#169; 2005, Arabeyes, Nadim Shaikli.</p>
<h2>SEE ALSO</h2>
<p> The ITL library (libitl) from the Islamic Tools and Libraries project. It is the underlying requirement for <code>idate</code> to function. The ITL library was created and is hosted at <code><a rel="nofollow" href="http://www.arabeyes.org">www.arabeyes.org</a></code>. </p>
<h2>Index</h2>
