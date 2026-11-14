---
title: "ac(1)"
name: "ac"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ac/"
description: "ac – print statistics about users’ connect time"
---

<h2>NAME</h2>
<p> ac &#8211; print statistics about users&#8217; connect time</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>ac</code></p>
<dd> [ <code>-d</code> | <code>&#8211;daily-totals</code> ] [ <code>-y</code> | <code>&#8211;print-year</code> ]<br />
 [ <code>-p</code> | <code>&#8211;individual-totals</code> ] [ <i>people</i> ]<br />
 [ <code>-f</code> | <code>&#8211;file</code> <i>filename</i> ] [ <code>-a</code> | <code>&#8211;all-days</code> ]<br />
 [ <code>&#8211;complain </code> ] [ <code>&#8211;reboots </code> ] [ <code>&#8211;supplants</code> ]<br />
 [ <code>&#8211;timewarps </code> ] [ <code>&#8211;compatibility</code> ]<br />
 [ <code>&#8211;tw-leniency</code> <i>num</i> ] [ <code>&#8211;tw-suspicious</code> <i>num</i> ]<br />
 [ <code>-z</code> | <code>&#8211;print-zeros</code> ] [ <code>&#8211;debug</code> ]<br />
 [ <code>-V</code> | <code>&#8211;version </code> ] [ <code>-h</code> | <code>&#8211;help </code> ]</dl>
<h2>DESCRIPTION</h2>
<p> <code>ac </code> prints out a report of connect time (in hours) based on the logins/logouts in the current <i>wtmp</i> file. A total is also printed out. </p>
<p> The accounting file <i>wtmp</i> is maintained by <code><a href="/docs/linux/man/8-init/">init</a></code>(8) and <code><a href="/docs/linux/man/1-login/">login</a></code>(1). Neither <code>ac</code> nor <code>login</code> creates the <i>wtmp</i> if it doesn&#8217;t exist, no accounting is done. To begin accounting, create the file with a length of zero. </p>
<p> NOTE: The <i>wtmp</i> file can get really big, really fast. You might want to trim it every once and a while. </p>
<p> GNU <code>ac </code> works nearly the same u*x <code>ac</code>, though it&#8217;s a little smarter in several ways. You should therefore expect differences in the output of GNU <code>ac</code> and the output of <code>ac</code>&#8216;s on other systems. Use the command <code>info</code><i> accounting</i> to get additional information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;daily-totals</code></p>
<dd> Print totals for each day rather than just one big total at the end. The output looks like this:<br />
&nbsp;<wbr>&nbsp;<wbr>Jul&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>total&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.17<br />
&nbsp;<wbr>&nbsp;<wbr>Jul&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>total&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2.10<br />
&nbsp;<wbr>&nbsp;<wbr>Jul&nbsp;<wbr>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>total&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8.23<br />
&nbsp;<wbr>&nbsp;<wbr>Jul&nbsp;<wbr>&nbsp;<wbr>6&nbsp;<wbr>&nbsp;<wbr>total&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2.10<br />
&nbsp;<wbr>&nbsp;<wbr>Jul&nbsp;<wbr>&nbsp;<wbr>7&nbsp;<wbr>&nbsp;<wbr>total&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.30</p>
<dt><code>-p, &#8211;individual-totals</code></p>
<dd> Print time totals for each user in addition to the usual everything-lumped-into-one value. It looks like:<br />
&nbsp;<wbr>&nbsp;<wbr>bob&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8.06<br />
&nbsp;<wbr>&nbsp;<wbr>goff&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.60<br />
&nbsp;<wbr>&nbsp;<wbr>maley&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>7.37<br />
&nbsp;<wbr>&nbsp;<wbr>root&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.12<br />
&nbsp;<wbr>&nbsp;<wbr>total&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>16.15</p>
<dt><i>people</i></p>
<dd> Print out the sum total of the connect time used by all of the users included in <i>people. </i> Note that <i>people</i> is a space separated list of valid user names; wildcards are not allowed.</p>
<dt><code>-f, &#8211;file </code><i>filename</i></p>
<dd> Read from the file <i>filename</i> instead of the system&#8217;s <i>wtmp</i> file.</p>
<dt><code>&#8211;complain</code></p>
<dd> When the <i>wtmp</i> file has a problem (a time-warp, missing record, or whatever), print out an appropriate error.</p>
<dt><code>&#8211;reboots</code></p>
<dd> Reboot records are NOT written at the time of a reboot, but when the system restarts; therefore, it is impossible to know exactly when the reboot occurred. Users may have been logged into the system at the time of the reboot, and many <code>ac&#8217;s</code> automatically count the time between the login and the reboot record against the user (even though all of that time shouldn&#8217;t be, perhaps, if the system is down for a long time, for instance). If you want to count this time, include the flag. *For vanilla <code>ac</code> compatibility, include this flag.*</p>
<dt><code>&#8211;supplants</code></p>
<dd> Sometimes, a logout record is not written for a specific terminal, so the time that the last user accrued cannot be calculated. If you want to include the time from the user&#8217;s login to the next login on the terminal (though probably incorrect), include this you want to include the time from the user&#8217;s login to the next login on the terminal (though probably incorrect), include this flag. *For vanilla <code>ac</code> compatibility, include this flag.*</p>
<dt><code>&#8211;timewarps</code></p>
<dd> Sometimes, entries in a <i>wtmp</i> file will suddenly jump back into the past without a clock change record occurring. It is impossible to know how long a user was logged in when this occurs. If you want to count the time between the login and the time warp against the user, include this flag. *For vanilla <code>ac</code> compatibility, include this flag.*</p>
<dt><code>&#8211;compatibility</code></p>
<dd> This is shorthand for typing out the three above options.</p>
<dt><code>-a, &#8211;all-days</code></p>
<dd> If we&#8217;re printing daily totals, print a record for every day instead of skipping intervening days where there is no login activity. Without this flag, time accrued during those intervening days gets listed under the next day where there is login activity.</p>
<dt><code>&#8211;tw-leniency</code><i> num</i></p>
<dd> Set the time warp leniency to <i>num </i> seconds. Records in <i>wtmp</i> files might be slightly out of order (most notably when two logins occur within a one-second period &#8211; the second one gets written first). By default, this value is set to 60. If the program notices this problem, time is not assigned to users unless the <code>&#8211;timewarps</code> flag is used.</p>
<dt><code>&#8211;tw-suspicious</code><i> num</i></p>
<dd> Set the time warp suspicious value to <i>num </i> seconds. If two records in the <i>wtmp</i> file are farther than this number of seconds apart, there is a problem with the <i>wtmp</i> file (or your machine hasn&#8217;t been used in a year). If the program notices this problem, time is not assigned to users unless the <code>&#8211;timewarps</code> flag is used.</p>
<dt><code>-y, &#8211;print-year</code></p>
<dd> Print year when displaying dates.</p>
<dt><code>-z, &#8211;print-zeros</code></p>
<dd> If a total for any category (save the grand total) is zero, print it. The default is to suppress printing.</p>
<dt><code>&#8211;debug</code></p>
<dd> Print verbose internal information.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print the version number of <code>ac</code> to standard output and quit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Prints the usage string and default locations of system files to standard output and exits.</dl>
<h2>FILES</h2>
<p> <i>wtmp</i></p>
<dl>
<dt>
<dd> The system wide login record file. See <code><a href="/docs/linux/man/5-wtmp/">wtmp</a></code>(5) for further details. </p>
</dl>
<h2>AUTHOR</h2>
<p> The GNU accounting utilities were written by Noel Cragg &lt;noel [at] gnu.ai.mit.edu&gt;. The man page was adapted from the accounting texinfo page by Susan Kleinmann &lt;sgk [at] sgk.tiac.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/5-wtmp/">wtmp</a></code>(5), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/8-sa/">sa</a></code>(8) </p>
<h2>Index</h2>
