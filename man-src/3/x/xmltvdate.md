---
title: "xmltvdate(3)"
name: "xmltvdate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmltvdate/"
---

XMLTV::Date - Date parsing routines for the xmltv package 

<h2>See Also</h2>Date::Manip
<h2>parse_date()</h2>Wrapper for <tt>&quot;Date::Manip::ParseDate()&quot;</tt> that does two things: firstly, if the year is not specified it chooses between last year, this year and next year depending on which date would be closest to now. (If only one of those dates is valid, for example because day-of-week is specified, then the valid one is chosen; if the time can only be parsed without adding an explicit year then that is chosen.) Secondly, an exception is thrown if the date cannot be parsed. 

 Argument is a single string.
