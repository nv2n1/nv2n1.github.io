---
title: "dm_zdump(1)"
name: "dm_zdump"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dm_zdump/"
---

<h2 class="name">NAME</h2>
 

 dm_zdump - timezone dumper 

<h2>SYNOPSIS</h2>

 This performs the same operation as the unix 'zdump' command, but using the Date::Manip module. 

 <pre><code>
dm_zdump[-v][-c YEAR][ZONE ZONE...]
</code></pre>

<h2>DESCRIPTION</h2>

 This displays the current time in each <font SIZE="-1">ZONE</font> named on the command line unless the -v option is given.
<dl>
<dt>-h, --help
<dd> Print online help.
<dt>-v, --verbose
<dd> This displays all critical dates (i.e. the times when a time change occurs due to the timezone description) for each of the timezones listed (or the local timezone if none are listed). 

 Each critical date is printed as two lines of output: the last second before the change occurs, and the first second of the new time. 

 By default, all critical dates from Jan 1, 0001 until the year 20 years in the future are printed, but this can be changed with the -c option.
<dt>-c, --cutoff <font SIZE="-1">YEAR</font>
<dd> This specifies the cutoff year. All critical dates up to the start of <font SIZE="-1">YEAR</font> are given. The <font SIZE="-1">GMT</font> time Jan 01, <font SIZE="-1">YEAR</font> at 00:00:00 is the cutoff time.</dl>

<h2>KNOWN BUGS</h2>

 None known.

<h2>BUGS AND QUESTIONS</h2>

 Please refer to the Date::Manip::Problems documentation for information on submitting bug reports or questions to the author.

<h2>SEE ALSO</h2>

 Date::Manip::Date

<h2>LICENSE</h2>

 This script is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>AUTHOR</h2>

 Sullivan Beck (sbeck [at] cpan.org) 

<h2>Index</h2>


