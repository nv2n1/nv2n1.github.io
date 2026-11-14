---
title: "cycle(1)"
name: "cycle"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cycle/"
description: "cycle – a calendar for women"
---

<h2>NAME</h2>
<p> cycle &#8211; a calendar for women</p>
<h2>SYNOPSIS</h2>
<p> <code>cycle</code></p>
<h2>DESCRIPTION</h2>
<p> Cycle is a calendar program for women. Given a cycle length or statistics for several periods, it can calculate the days until menstruation, the days of &quot;safe&quot; sex, the fertile period, and the days to ovulations, and define the d.o.b. (date of birth) of a child. It allows the user to write notes and helps to supervise the reception of hormonal contraceptive tablets.</p>
<h2>FEATURES</h2>
<p> The program is capable of: </p>
<p>&nbsp;<wbr>&#8211; Calculate of the days of menstruation, based on length of the cycle or on statistics of a period.<br />
&nbsp;<wbr>&#8211; Calculate the&nbsp;<wbr>&quot;safe&quot;&nbsp;<wbr>sex days, fertile period and day to ovulations<br />
&nbsp;<wbr>&#8211; Definition of D.O.B .&nbsp;<wbr>(Date Of Birth)&nbsp;<wbr>of a child<br />
&nbsp;<wbr>&#8211; Allows to write notes<br />
&nbsp;<wbr>&#8211; Helps to supervise reception of hormonal contraceptive tablets </p>
<h2>HOW DOES IT WORK</h2>
<p> It uses the calendar method for the definition of fertile days. For this is necessary to determine duration, at least, of last six cycles. For determine the fertile days it uses this algoritm: </p>
<p>&nbsp;<wbr>&#8211; First day: duration of shortest cycle minus 18<br />
&nbsp;<wbr>&#8211; Last day: duration of longest cycle minus 11<br />
&nbsp;<wbr>&#8211; Ovulation: is considered in the middle of fertile period&nbsp;<wbr>(Determine the exact day isn&#8217;t possible with the calendar method)&nbsp;<wbr> </p>
<p> Date of a birth of the child is counted from the beginning of last menstruation (in obstetrics are accepted 40 weeks). This date is corrected with the duration of a cycle (are subtracted or added same number of days that a cycle differs from 28 days). Is possible check the results at: <a rel="nofollow" href="http://cir.msk.ru/sroki.shtml">http://cir.msk.ru/sroki.shtml</a> (in Russian)</p>
<h2>USAGE</h2>
<p> It is necessary to mark the beginning of menstruation. This is possible clicking with the right button on the date and chosing &quot;The beginning of a cycle&quot;. Similarly the mark can be removed. Using duration of last six cycles, the program will calculate </p>
<p>&nbsp;<wbr>&#8211; Fertile period &#8211; green cells<br />
&nbsp;<wbr>&#8211; Ovulation day&nbsp;<wbr>(the middle fertile period)&nbsp;<wbr>&#8211; brightly green cell<br />
&nbsp;<wbr>&#8211; Beginning of following menstruation &#8211; pink cells&nbsp;<wbr> </p>
<p> Cycle duration is set in options or is calculated an average of last six periods. </p>
<p> To determine prospective date of a birth of the child, it is necessary first day of last cycle to mark in addition as &quot;Pregnancy&quot;. </p>
<p> Depending on your purposes, you can display only &quot;Safe&quot; sex days or only fertile days. Information about interesting day can be received clicking with left button. </p>
<p> Is possible adding a note to any date using corresponding item of the menu. Day with a note are underlined. </p>
<p> It is necessary to note that factor of failures of calendar contraception method is about 10 percent. This method is suitable only for women with enough regular cycle. </p>
<p> If your doctor has recommended hormonal contraceptive this program will help to supervise their reception. Closely familiarize with the instruction applied to the chosen preparation. Packing can contain 21 tablet (the circuit of reception 21 day on one tablet, then 7 days pause) or 28 tablets in this case all tablets are accepted without interruption every day of 28. In the program, is marked only day of reception of each first tablet of packing. </p>
<p> NOTE: This program is not a reliable contraceptive method. It does neither help to prevent sexual transmision diseases like AIDS. It is just an electronic means of keeping track of some of your medical data and extract some statistical conclusions from them. You cannot consider this program as a substitute for your gynecologist in any way.</p>
<h2>FILES</h2>
<dl>
<dt><i>~/.cycle</i></p>
<dd> This is the directory where cycle stores the data.</dl>
<h2>AUTHOR</h2>
<p> cycle was written by Oleg S. Gints. </p>
<p> This manual page was written for Debian by Miriam Ruiz &lt;little_miry [at] yahoo.es&gt;.</p>
<h2>SEE ALSO</h2>
<p> You can find cycle&#8217;s home page at: <a rel="nofollow" href="http://cycle.sourceforge.net/">http://cycle.sourceforge.net/</a> </p>
<p> More information about calendar method are available at: <a rel="nofollow" href="http://www.mama.ru/gynecolog/STA/st18.htm">http://www.mama.ru/gynecolog/STA/st18.htm</a> (in Russian) </p>
<h2>Index</h2>
