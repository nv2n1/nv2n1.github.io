---
title: "ods-timing(5)"
name: "ods-timing"
section: "5"
letter: "o"
url: "/docs/linux/man/5-ods-timing/"
description: "ods-timing – OpenDNSSEC timing specification"
---

<p><code>ods-timing</code> &#8211; OpenDNSSEC timing specification</p>
<h2>Synopsis</h2>
<p><code>/etc/opendnssec/conf.xml</code><br />
 <code>/etc/opendnssec/kasp.xml</code><br />
 <code>/etc/opendnssec/zonelist.xml</code></p>
<h2>Description</h2>
<p>The configuration files of OpenDNSSEC need to have timing descriptions, notably for periods. These descriptions follow ISO 8601 with exceptions for the duration of a month and a year, as these periods would be allowed to vary if ISO 8601 were strictly adhered to. </p>
<p> Durations are represented by the format <code>P[n]Y[n]M[n]DT[n]H[n]M[n]S</code>. In these representations, the <code>[n]</code> is replaced by the value for each of the date and time elements that follow the <code>[n]</code>. Leading zeros are not required. The capital letters <code>P</code>, <code>Y</code>, <code>M</code>, <code>W</code>, <code>D</code>, <code>T</code>, <code>H</code>, <code>M</code> and <code>S</code> are designators for each of the date and time elements and are not replaced</p>
<dl>
<dt><code>P</code></p>
<dd>is the duration designator (historically called &quot;period&quot;) placed at the start of the duration representation.</p>
<dt><code>Y</code></p>
<dd>is the year designator that follows the value for the number of years.</p>
<dt><code>M</code></p>
<dd>is the month designator that follows the value for the number of months.</p>
<dt><code>W</code></p>
<dd>is the week designator that follows the value for the number of weeks.</p>
<dt><code>D</code></p>
<dd>is the day designator that follows the value for the number of days.</p>
<dt><code>T</code></p>
<dd>is the time designator that precedes the time components of the representation.</p>
<dt><code>H</code></p>
<dd>is the hour designator that follows the value for the number of hours.</p>
<dt><code>M</code></p>
<dd>is the minute designator that follows the value for the number of minutes.</p>
<dt><code>S</code></p>
<dd>is the second designator that follows the value for the number of seconds.</dl>
<p> For example, <code>P3Y6M4DT12H30M5S</code> represents a duration of &quot;three years, six months, four days, twelve hours, thirty minutes, and five seconds&quot;. Date and time elements including their designator may be omitted if their value is zero, and lower order elements may also be omitted for reduced precision. For example, <code>P23DT23H</code> and <code>P4Y</code> are both acceptable duration representations.</p>
<h2>Exception</h2>
<p>A year or month vary in duration depending on the current date. For OpenDNSSEC, we assume fixed values</p>
<dl>
<dt><code>One month</code></p>
<dd>is assumed to be 31 days.</p>
<dt><code>One year</code></p>
<dd>is assumed to be 365 days.</dl>
<p> This exception may or may not change in future releases of OpenDNSSEC. The reason for making this exception is to avoid complicating this software in a way that may not meet any practical need.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmspeed/">ods-hsmspeed</a>(1), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), ISO 8601, <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>Authors</h2>
<p><code>OpenDNSSEC</code> was made by the OpenDNSSEC project, to be found on <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
