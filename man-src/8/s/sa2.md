---
title: "sa2(8)"
name: "sa2"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sa2/"
description: "sa2 – Create a report from the current standard system activity daily data file."
---

<p>sa2 &#8211; Create a report from the current standard system activity daily data file.</p>
<h2>Synopsis</h2>
<p><code>/usr/lib/sysstat/sa2</code> </p>
<h2>Description</h2>
<p>The <code>sa2 </code>command is a shell procedure variant of the <code>sar</code> command which writes a daily report in the <i>sarDD </i>or the <i>sarYYYYMMDD </i>file, where <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day. By default the report is saved in the <i>/var/log/sysstat</i> directory. The <code>sa2</code> command will also remove reports more than one week old by default. You can however keep reports for a longer (or a shorter) period by setting the <code>HISTORY</code> environment variable. Read the <code><a href="/docs/linux/man/5-sysstat/">sysstat</a></code>(5) manual page for details. The <code>sa2 </code>command accepts most of the flags and parameters of the <code>sar </code>command. The <code>sa2 </code>command is designed to be started automatically by the <code>cron </code>command. </p>
<h2>Examples</h2>
<p>To run the <code>sa2</code> command daily, place the following entry in your root crontab file: </p>
<p> <code>5 19 * * 1-5 /usr/lib/sysstat/sa2 -A</code> </p>
<p> This will generate by default a daily report called <i>sarDD </i>in the <i>/var/log/sysstat</i> directory, where the <i>DD </i>parameter is a number representing the day of the month.</p>
<h3>Debian note</h3>
<p>The Debian sysstat package has already placed such an entry in your system crontab. Please refer to the <i>/usr/share/doc/sysstat/README.Debian</i> file for details.</p>
<h2>Files</h2>
<p><i>/var/log/sysstat/sarDD</i><br />
 <i>/var/log/sysstat/sarYYYYMMDD</i></p>
<dl>
<dd>The standard system activity daily report files and their default location. <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD </i>for the current day. </p>
</dl>
<h2>Author</h2>
<p>Sebastien Godard (sysstat &lt;at&gt; orange.fr)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/8-sadc/">sadc</a></code>(8), <code><a href="/docs/linux/man/8-sa1/">sa1</a></code>(8), <code><a href="/docs/linux/man/1-sadf/">sadf</a></code>(1), <code><a href="/docs/linux/man/5-sysstat/">sysstat</a></code>(5) <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br />
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
