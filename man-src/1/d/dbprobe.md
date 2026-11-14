---
title: "dbprobe(1)"
name: "dbprobe"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbprobe/"
description: "dbprobe – database response time and availability information"
---

<h2>NAME</h2>
<p> <code>dbprobe</code> &#8211; database response time and availability information</p>
<h2>SYNOPSIS</h2>
<p> <code>dbprobe.pl</code> [<i>delay</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>dbprobe</code> utility is used by <code><a href="/docs/linux/man/1-pmdadbping/">pmdadbping</a></code>(1) to measure response time from a database. A given query is executed on the database at the requested interval (<i>delay</i>, which defaults to 60 seconds). This response time measure can be exported via the Performance Co-Pilot framework for live and historical monitoring using <i><a href="/docs/linux/man/1-pmdadbping/">pmdadbping</a></i>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmdadbping/">pmdadbping</a></code>(1) and <code><a href="/docs/linux/man/3-dbi/">DBI</a></code>(3). </p>
<h2>Index</h2>
