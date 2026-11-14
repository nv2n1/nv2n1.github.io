---
title: "popularity-contest(8)"
name: "popularity-contest"
section: "8"
letter: "p"
url: "/docs/linux/man/8-popularity-contest/"
description: "popularity-contest – list the most popular Debian packages"
---

<p>popularity-contest &#8211; list the most popular Debian packages</p>
<h2>Synopsis</h2>
<p><code>popularity-contest</code></p>
<h2>Description</h2>
<p>The <code>popularity-contest</code> command gathers information about Debian packages installed on the system, and prints the name of the most recently used executable program in that package as well as its last-accessed time (atime) and last-attribute-changed time (ctime) to stdout. </p>
<p> When aggregated with the output of <code>popularity-contest</code> from many other systems, this information is valuable because it can be used to determine which Debian packages are commonly installed, used, or installed and never used. This helps Debian maintainers make decisions such as which packages should be installed by default on new systems. </p>
<p> The resulting statistic is available from the project home page <code><a rel="nofollow" href="https://popcon.debian.org/">https://popcon.debian.org/</a></code>. </p>
<p> Normally, <code>popularity-contest</code> is run from a <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8) job, <code>/etc/cron.daily/popularity-contest</code>, which automatically submits the results to Debian package maintainers (only once a week) according to the settings in <code>/etc/popularity-contest.conf</code> and <code>/usr/share/popularity-contest/default.conf</code>.</p>
<h2>See Also</h2>
<p>The popularity-contest FAQ at <code>/usr/share/doc/popularity-contest/FAQ</code> <code><a href="/docs/linux/man/8-popcon-largest-unused/">popcon-largest-unused</a></code>(8), <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8) </p>
<p> Additional documentation is in <code>/usr/share/doc/popularity-contest/</code>.</p>
<h2>Author</h2>
<p>Avery Pennarun &lt;apenwarr [at] debian.org&gt;.</p>
