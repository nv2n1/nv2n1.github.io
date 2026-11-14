---
title: "sysstat(5)"
name: "sysstat"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sysstat/"
description: "sysstat – sysstat configuration file."
---

<p>sysstat &#8211; sysstat configuration file.</p>
<h2>Description</h2>
<p>This file is read by <code><a href="/docs/linux/man/8-sa1/">sa1</a></code>(8) and <code><a href="/docs/linux/man/8-sa2/">sa2</a></code>(8) shell scripts from the sysstat&#8217;s set of tools. It consists of a sequence of shell variable assignments used to configure sysstat logging. The variables and their meanings are:</p>
<dl>
<dt><code>COMPRESSAFTER</code></p>
<dd>Number of days after which daily data files are to be compressed. The compression program is given in the <code>ZIP </code>variable.</p>
<dt><code>DELAY_RANGE</code></p>
<dd>Tell <code>sa2</code> script to wait for a random delay in the indicated range before running. This delay is expressed in seconds, and is aimed at preventing a massive I/O burst at the same time on VM sharing the same storage area. A value of 0 means that <code>sa2</code> script will generate its reports files immediately.</p>
<dt><code>HISTORY</code></p>
<dd>The number of days during which a daily data file or a report should be kept. Data files or reports older than this number of days will be removed by the <code><a href="/docs/linux/man/8-sa2/">sa2</a></code>(8) shell script. Data files and reports are normally saved in the /var/log/sysstat directory, under the name <i>saDD </i>(for data files) or <i>sarDD </i>(for reports), where the <i>DD</i> parameter indicates the current day. The number of files actually kept in the /var/log/sysstat directory may be slightly higher than the <code>HISTORY </code>value due to the way the <code>sa2</code> script figures out which files are to be removed (see below &quot;How the <code><a href="/docs/linux/man/8-sa2/">sa2</a></code>(8) script applies <code>HISTORY</code> value&quot;). Using a value of 28 keeps a whole month&#8217;s worth of data. If you set <code>HISTORY</code> to a value greater than 28 then you should consider using <code>sadc</code>&#8216;s option <code>-D</code> to prevent older data files from being overwritten (see <code><a href="/docs/linux/man/8-sadc/">sadc</a></code>(8) manual page). In this latter case data files are named <i>saYYYYMMDD </i>and reports <i>sarYYYYMMDD</i>, where <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day. How the <code><a href="/docs/linux/man/8-sa2/">sa2</a></code>(8) script applies <code>HISTORY </code>value The <code>sa2</code> script uses the <code>find </code>command with the <code>-mtime </code>option to figure out which files are to be removed. The <code>find </code>command interprets this value as &quot;N 24 hour periods&quot;, ignoring any fractional part. This means that the last modified time of a given <i>sa[r]DD </i>data or report file, using a <code>HISTORY</code> of 1, has to have been modified at least two days ago before it will be removed. And for a <code>HISTORY </code>of 28 that would mean 29 days ago. To figure out how a <code>HISTORY</code> of 28 is applied in practice, we need to consider that the <code>sa2 </code>script that issues the <code>find </code>command to remove the old files typically runs just before mid-night on a given system, and since the first record from <code>sadc</code> can also be written to the previous day&#8217;s data file (thereby moving its modification time up a bit), the <code>sa2</code> script will leave 30 files untouched. So for a setting of 28, and counting the data file of the current day, there will always be 31 files (or 30 files, depending on the number of days in a month) in the /var/log/sysstat directory during the majority of a given day. E.g.: April 30th: 31 files (Apr 30th-1st, Mar 31th)<br />
 May 1st: 30 files (May 1st, Apr 30th-2nd) Yet we can note the following exceptions (as inspected at Noon of the given day): February 28th: 31 files (Feb 28th-1st, Jan 31st, 30th &amp; 29th)<br />
 March 1st: 30 files (Mar 1st, Feb 28th-2nd, Jan 31st &amp; 30th)<br />
 March 2nd: 29 files (Mar 1st &amp; 2nd, Feb 28th-3rd, Jan. 31st)<br />
 March 3rd: 28 files (Mar 1st-3rd, Feb 28th-4th)<br />
 March 4th &#8211; March 28th: 28 files<br />
 March 29th: 29 files<br />
 March 30th: 30 files<br />
 March 31st: 31 files (Determining the number of files in March on a leap year is left as an exercise for the reader). Things are simpler if you use the <i>sa[r]YYYYMMDD </i>name format. Apply the same logic as above in this case and you will find that there are always <code>HISTORY </code>+ 3 files in the <i>/var/log/sysstat</i> directory during the majority of a given day.</p>
<dt><code>REPORTS</code></p>
<dd>Set this variable to <code>false </code>to prevent the <code>sa2</code> script from generating reports (the <i>sarDD </i>files).</p>
<dt><code>SA_DIR</code></p>
<dd>Directory where the standard system activity daily data and report files are saved. Its default value is <i>/var/log/sysstat</i>.</p>
<dt><code>SADC_OPTIONS</code></p>
<dd>Options that should be passed to <code><a href="/docs/linux/man/8-sadc/">sadc</a></code>(8). With these options (see <code><a href="/docs/linux/man/8-sadc/">sadc</a></code>(8) manual page), you can select some additional data which are going to be saved in daily data files. These options are used only when a new data file is created. They will be ignored with an already existing one.</p>
<dt><code>YESTERDAY</code></p>
<dd>By default <code>sa2</code> script generates yesterday&#8217;s summary, since the <code>cron </code>job usually runs right after midnight. If you want <code>sa2</code> to generate the summary of the same day (for example when cron job runs at 23:53) set this variable to <code>no</code>.</p>
<dt><code>ZIP</code></p>
<dd>Program used to compress data and report files. </p>
<h2>File</h2>
<p><i>/etc/sysstat/sysstat</i></p>
<h2>Author</h2>
<p>Sebastien Godard (sysstat &lt;at&gt; orange.fr)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sadc/">sadc</a></code>(8), <code><a href="/docs/linux/man/8-sa1/">sa1</a></code>(8), <code><a href="/docs/linux/man/8-sa2/">sa2</a></code>(8) <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br />
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
