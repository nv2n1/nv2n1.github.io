---
title: "sa1(8)"
name: "sa1"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sa1/"
description: "sa1 – Collect and store binary data in the system activity daily data file."
---

<p>sa1 &#8211; Collect and store binary data in the system activity daily data file.</p>
<h2>Synopsis</h2>
<p><code>/usr/lib/sysstat/sa1 [ &#8211;boot | &#8211;rotate [ iso ] | &#8211;sleep |</code> <i>interval count</i> <code>]</code> </p>
<h2>Description</h2>
<p>The <code>sa1</code> command is a shell procedure variant of the <code>sadc</code> command and handles all of the flags and parameters of that command. The <code>sa1</code> command collects and stores binary data in the current standard system activity daily data file. The standard system activity daily data file is named <i>saDD </i>unless <code>sadc</code>&#8216;s option <code>-D </code>is used, in which case its name is <i>saYYYYMMDD</i>, where <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day. By default it is located in the <i>/var/log/sysstat</i> directory. The <i>interval </i>and <i>count</i> parameters specify that the record should be written <i>count </i>times at <i>interval</i> seconds. If no arguments are given to <code>sa1</code> then a single record is written. The <code>sa1</code> command is designed to be started automatically by the <code>cron </code>command. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;boot</code></p>
<dd>This option tells <code>sa1 </code>that the <code>sadc</code> command should be called without specifying the <i>interval </i>and <i>count</i> parameters in order to insert a dummy record, marking the time when the counters restart from 0.</p>
<dt><code>&#8211;rotate [ iso ]</code></p>
<dd>Use this option to tell <code>sa1 </code>to insert a record of statistics to the standard <i>saDD</i> system activity daily data file of the previous day. This should be done shortly after midnight (on day DD+1) in order to make sure that the data file covers the whole day, including the last interval of time just before midnight. Adding the <code>iso</code> keyword tells <code>sa1</code> to use <i>saYYYYMMDD</i> instead of <i>saDD</i> as the standard system activity daily data file name.</p>
<dt><code>&#8211;sleep</code></p>
<dd>This option tells <code>sa1 </code>that the <code>sadc</code> command should insert a comment indicating that the system is entering or leaving sleep mode (i.e. system suspend or hibernation). </p>
</dl>
<h2>Example</h2>
<p>To collect data (including those from disks) every 10 minutes, place the following entry in your root crontab file: <code>0,10,20,30,40,50 * * * * /usr/lib/sysstat/sa1 1 1 -S DISK</code> To rotate current system activity daily data file, ensuring it is complete, place the following entry in your root crontab file: <code>0 0 * * * /usr/lib/sysstat/sa1 &#8211;rotate</code></p>
<h3>Debian note</h3>
<p>The Debian sysstat package has already placed such an entry in your system crontab. Please refer to the <i>/usr/share/doc/sysstat/README.Debian</i> file for details. </p>
<h2>Files</h2>
<p><i>/var/log/sysstat/saDD</i><br />
 <i>/var/log/sysstat/saYYYYMMDD</i></p>
<dl>
<dd>The standard system activity daily data files and their default location. <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day. </p>
</dl>
<h2>Author</h2>
<p>Sebastien Godard (sysstat &lt;at&gt; orange.fr)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/8-sadc/">sadc</a></code>(8), <code><a href="/docs/linux/man/8-sa2/">sa2</a></code>(8), <code><a href="/docs/linux/man/1-sadf/">sadf</a></code>(1), <code><a href="/docs/linux/man/5-sysstat/">sysstat</a></code>(5) <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br />
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
