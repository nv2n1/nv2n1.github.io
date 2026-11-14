---
title: "curl_getdate(3)"
name: "curl_getdate"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_getdate/"
description: "curl_getdate – Convert a date string to number of seconds since January 1, 1970"
---

<h2>NAME</h2>
<p> curl_getdate &#8211; Convert a date string to number of seconds since January 1, 1970</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>time_t curl_getdate(char *</code><i>datestring</i><code>, time_t *now</code><i> );</i></p>
<h2>DESCRIPTION</h2>
<p> This function returns the number of seconds since January 1st 1970 in the UTC time zone, for the date and time that the <i>datestring</i> parameter specifies. The <i>now</i> parameter is not used, pass a NULL there. </p>
<p> <code>NOTE:</code> This function was rewritten for the 7.12.2 release and this documentation covers the functionality of the new one. The new one is not feature-complete with the old one, but most of the formats supported by the new one was supported by the old too.</p>
<h2>PARSING DATES AND TIMES</h2>
<p> A &quot;date&quot; is a string containing several items separated by whitespace. The order of the items is immaterial. A date string may contain many flavors of items:</p>
<dl>
<dt><code>calendar date items</code></p>
<dd> Can be specified several ways. Month names can only be three-letter english abbreviations, numbers can be zero-prefixed and the year may use 2 or 4 digits. Examples: 06 Nov 1994, 06-Nov-94 and Nov-94 6.</p>
<dt><code>time of the day items</code></p>
<dd> This string specifies the time on a given day. You must specify it with 6 digits with two colons: HH:MM:SS. To not include the time in a date string, will make the function assume 00:00:00. Example: 18:19:21.</p>
<dt><code>time zone items</code></p>
<dd> Specifies international time zone. There are a few acronyms supported, but in general you should instead use the specific relative time compared to UTC. Supported formats include: -1200, MST, +0100.</p>
<dt><code>day of the week items</code></p>
<dd> Specifies a day of the week. Days of the week may be spelled out in full (using english): `Sunday&#8217;, `Monday&#8217;, etc or they may be abbreviated to their first three letters. This is usually not info that adds anything.</p>
<dt><code>pure numbers</code></p>
<dd> If a decimal number of the form YYYYMMDD appears, then YYYY is read as the year, MM as the month number and DD as the day of the month, for the specified calendar date.</dl>
<h2>EXAMPLES</h2>
<pre>
Sun, 06 Nov 1994 08:49:37 GMT
Sunday, 06-Nov-94 08:49:37 GMT
Sun Nov  6 08:49:37 1994
06 Nov 1994 08:49:37 GMT
06-Nov-94 08:49:37 GMT
Nov  6 08:49:37 1994
06 Nov 1994 08:49:37
06-Nov-94 08:49:37
1994 Nov 6 08:49:37
GMT 08:49:37 06-Nov-94 Sunday
94 6 Nov 08:49:37
1994 Nov 6
06-Nov-94
Sun Nov 6 94
1994.Nov.6
Sun/Nov/6/94/GMT
Sun, 06 Nov 1994 08:49:37 CET
06 Nov 1994 08:49:37 EST
Sun, 12 Sep 2004 15:05:58 -0700
Sat, 11 Sep 2004 21:32:11 +0200
20040912 15:05:58 -0700
20040911 +0200
</pre>
<h2>STANDARDS</h2>
<p> This parser was written to handle date formats specified in RFC 822 (including the update in RFC 1123) using time zone name or time zone delta and RFC 850 (obsoleted by RFC 1036) and ANSI C&#8217;s asctime() format. These formats are the only ones RFC2616 says HTTP applications may use.</p>
<h2>RETURN VALUE</h2>
<p> This function returns -1 when it fails to parse the date string. Otherwise it returns the number of seconds as described. </p>
<p> If the year is larger than 2037 on systems with 32 bit time_t, this function will return 0x7fffffff (since that is the largest possible signed 32 bit number). </p>
<p> Having a 64 bit time_t is not a guarantee that dates beyond 03:14:07 UTC, January 19, 2038 will work fine. On systems with a 64 bit time_t but with a crippled mktime(), <i>curl_getdate</i> will return -1 in this case.</p>
<h2>REWRITE</h2>
<p> The former version of this function was built with yacc and was not only very large, it was also never quite understood and it wasn&#8217;t possible to build with non-GNU tools since only GNU Bison could make it thread-safe! </p>
<p> The rewrite was done for 7.12.2. The new one is much smaller and uses simpler code. </p>
<h2>Index</h2>
