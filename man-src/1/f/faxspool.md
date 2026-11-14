---
title: "faxspool(1)"
name: "faxspool"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faxspool/"
description: "faxspool – queue and convert files for faxing with"
---

<h2 class="name">NAME</h2>
<p> faxspool &#8211; queue and convert files for faxing with </p>
<p><a href="/docs/linux/man/8-sendfax/">sendfax</a>(8)</p>
<h2>SYNOPSIS</h2>
<p> <code>faxspool</code> [options] phone-number files&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Queue the named files for later transmission with <i><a href="/docs/linux/man/8-sendfax/">sendfax</a>(8).</i> The input files are converted to G3 fax files, spooled to /var/spool/fax/outgoing/&lt;dir&gt;/f*.g3, and queued for transmsssion to the fax address &quot;phone-number&quot;. </p>
<p> On top of each page, <i>faxspool</i> puts a header line, telling the other side the number of pages, your fax id, &#8230;, whatever you like. The format of this line is configurable via the file <code>/etc/mgetty+sendfax/faxheader</code> and per-user via the file <code>$HOME/.faxheader.</code> (you can select another one with the &quot;-h&quot; option, for example, one for your business faxes and one for the private stuff). </p>
<p> This file should contain a few lines of text, normally only one line, but more than one line is permitted. The text may use the tokens @T@ for the remote telephone number, @U@ for the sending user name, @N@ for his full name (fifth field of /etc/passwd, if not given with &quot;-F&quot;), @P@ for the page number and @M@ for the total number of pages. @D@ will be replaced by the string specified with the &quot;-D&quot; option (see below), @DATE@ will be substituted by the output of the `date` command, and @ID@ stands for the sender&#8217;s fax number (FAX_STATION_ID). Finally, @S@ will be substituted by the JOB ID (Fxxxxxx). </p>
<p> If &quot;phone-number&quot; contains non-numeric characters, <i>faxspool</i> interprets it as an alias and tries to look it up in the files <code>/etc/mgetty+sendfax/faxaliases</code> and <code>$HOME/.faxnrs.</code> These files have a very simple format: one line per alias, alias name first, whitespace (tab or blank), phone number. Optionally, you can place a short description of the receiver after the phone number, this will be used as if it had been specified with &quot;-D&quot; (an explicit &quot;-D&quot; flag overrides this). </p>
<p> Example: gert 0893244814 Gert Doering </p>
<p> Access control is handled similar to the way &quot;crontab&quot; does it: if a file /etc/mgetty+sendfax/fax.allow exists, only those users listed in that file (one name per line) may use the fax service. If it does not exist, but a file /etc/mgetty+sendfax/fax.deny exists, all users but those listed in that file may use <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), and if neither file exists, only root may send faxes. (Note: if the user name in the fax.allow file is followed by a blank, the rest of that line is ignored. Some other fax spooling software uses this to store additional information about the user sending the request). </p>
<p> Optionally, <i>faxspool</i> can generate user-customizable fax cover pages. It is quite easy to set up: if a file /usr/lib64/mgetty+sendfax/make.coverpg exists and is executable, it is run with all relevant source/destination data on the command line, and its output is sent as the first page of the resulting fax. If $HOME/.make.coverpg exists, this file is used instead. See <a href="/docs/linux/man/1-coverpg/">coverpg</a>(1) for details. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code></p>
<dd> Tells <i>faxspool</i> to use normal resolution (as opposed to the default, fine resolution) both when converting files to G3 format and when transmitting (no effect on pbm files)</p>
<dt><code>-h &lt;text file&gt;</code></p>
<dd> Use <code>&lt;text file&gt;</code> for the FAX header line(s). The default format file for <i>faxspool</i> is <code>/etc/mgetty+sendfax/faxheader. &#8216;-&#8216; means &#8216;no header line&#8217;.</code></p>
<dt><code>-q</code></p>
<dd> do not output progress messages (file &#8230; is format &#8230;, spooling to &#8230;). Error messages will be seen anyway.</p>
<dt><code>-f &lt;mail address&gt;</code></p>
<dd> Use the address given for the status mail that <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1) sends after completing / dequeueing the request. If no mail address is specified, the requesting user (on the local machine) gets the mail.</p>
<dt><code>-u &lt;user name&gt;</code></p>
<dd> Do not use the current user ID for authentication purposes but the user name specified. Since this can lead to easy breach of security, only &quot;trusted&quot; users may use this flag. Currently, those users are &quot;root&quot;, &quot;lp&quot; and &quot;daemon&quot; (hardwired into the code). Note: the status mail will still go to the user running <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) unless changed with &quot;-f&quot;.</p>
<dt><code>-D &lt;destination&gt;</code></p>
<dd> Verbose form of the fax&#8217;s destination. Used only for informational purposes, that is, <a href="/docs/linux/man/1-faxq/">faxq</a>(1) will show it, <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1) will put it into the return mail (&quot;Subject: your fax to &#8230;&quot;), and a @D@ in the page header will be replaced by it.</p>
<dt><code>-F &lt;description&gt;</code></p>
<dd> Full name or similar description of the sending user (if not specified, the full name field from /etc/passwd will be used). Used only for informational purposes, that is, <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) will substitute a @N@ in the page header file with it, and it will be passed to the cover page program (if used) as &lt;sender-NAME&gt;.</p>
<dt><code>-P &lt;priority&gt;</code></p>
<dd> Sets the priority of the fax in the queue. 9 is highest (meaning: faxes get sent out first), 1 is lowest. If nothing is specified, a default value of 5 is used. Right now, only <i>faxrunqd</i> understands priority, <i>faxrunq</i> will silently ignore it.</p>
<dt><code>-C &lt;cover page program&gt;</code></p>
<dd> Specify that the named program is to be used to generate a cover page for the fax that is being queued. How the program is called is described in the <a href="/docs/linux/man/1-coverpg/">coverpg</a>(1) manpage. </p>
<p> The special program name &quot;-&quot; is used to specify &quot;no coverpage at all&quot;. </p>
<p> No message is issued if the program isn&#8217;t found, or cannot be executed, faxspool will simply queue the fax without cover page. </p>
<p> The default cover page program used is $HOME/.make.coverpg; if this file doesn&#8217;t exist /usr/lib64/mgetty+sendfax/make.coverpg is used. (However, if $HOME/.make.coverpg exists, but is not executable, no coverpage is used at all.)</p>
<dt><code>-p</code></p>
<dd> Spool a request that will try polling (see &quot;sendfax -p&quot;). The implementation isn&#8217;t too smart yet, the polled files will simply go into the job&#8217;s spool directory.</p>
<dt><code>-t &lt;hh:mm&gt;</code></p>
<dd> Don&#8217;t send the fax before the time given. It may not be sent exactly at &lt;hh:mm&gt;, but the first time <i>faxrunq</i> runs after that time. If the fax cannot be sent successfully before midnight, it won&#8217;t be sent on the next day until &lt;hh:mm&gt;!</p>
<dt><code>-t &lt;hh:mm&gt;-&lt;hh:mm&gt;</code></p>
<dd> Only send the fax in the time range between those two times. This is only implemented in <i>faxrunqd.</i> If the second time specified is &#8216;earlier&#8217; than the first time, it is interpreted as a time range crossing midnight.</p>
<dt><code>-A &lt;data&gt;</code></p>
<dd> pass faxspool a chunk of data that is ignored (so you can put anything you want here), but written to all the log files (acct.log, sendfax.log). This can be used to tag faxes as private/corporate, to tag faxes with the customer ID to use for billing, or something along that lines.</p>
<dt><code>-m &lt;phone1&gt; &lt;phone2&gt; &lt;phone3&gt; &#8230; &#8212;</code></p>
<dd> Multicasting &#8211; send the specified files to all phone numbers in the list given after &quot;-m&quot;. The list is terminated with &quot;&#8211;&quot;. &quot;-m&quot; has to be the last option on the command line (not implemented yet).</p>
<dt><code>-M &lt;file name&gt;</code></p>
<dd> Multicasting &#8211; read a list of telephone numbers to send the fax to from the given file. Do not use in conjunction with &quot;-m&quot; (not implemented yet).</p>
<dt><code>-c</code></p>
<dd> Copy source files to a sub directory &quot;.source-files/&quot; in the fax queue directory (most likely, you won&#8217;t ever need this &#8211; I needed it for one project, so it&#8217;s here and documented. Don&#8217;t ask what it&#8217;s good for).</dl>
<h2>FILES</h2>
<dl>
<dt><code>/var/spool/fax/outgoing/*</code></p>
<dd> fax spool directory</p>
<dt><code>/etc/mgetty+sendfax/faxaliases</code></p>
<dd> global fax alias file</p>
<dt><code>$HOME/.faxnrs</code></p>
<dd> private fax alias file</p>
<dt><code>/etc/mgetty+sendfax/fax.allow</code></p>
<dd> list of allowed users</p>
<dt><code>/etc/mgetty+sendfax/fax.deny</code></p>
<dd> list of denied users</p>
<dt><code>/etc/mgetty+sendfax/faxheader</code></p>
<dd> default fax page header</p>
<dt><code>/usr/lib64/mgetty+sendfax/make.coverpg</code></p>
<dd> program to create fax cover page (see <a href="/docs/linux/man/1-coverpg/">coverpg</a>(1)).</p>
<dt><code>/etc/mgetty+sendfax/faxspool.rules</code></p>
<dd> program to control which file extentions are recognized (.txt, .ps, &#8230;) and how those file formats should be converted to G3.</p>
<dt><code>/usr/lib64/mgetty+sendfax/faxq-helper</code></p>
<dd> this a small C helper program that facilitates access to the fax spool queue (which is since mgetty 1.1.29 no longer world-writeable) </p>
</dl>
<h2>BUGS</h2>
<p> <i>faxspool</i> is not too smart about recognizing file types </p>
<p> Use of <i>faxspool -n</i> with bitmap files may give wrong results, depending on the aspect ratio of the input files. </p>
<p> Multicasting with the -m and -M options is not implemented yet. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-g3cat/">g3cat</a>(1), <a href="/docs/linux/man/1-pbm2g3/">pbm2g3</a>(1), <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8), <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1), <a href="/docs/linux/man/8-faxrunqd/">faxrunqd</a>(8), <a href="/docs/linux/man/1-faxq/">faxq</a>(1), <a href="/docs/linux/man/5-faxqueue/">faxqueue</a>(5), <a href="/docs/linux/man/1-coverpg/">coverpg</a>(1)</p>
<h2>AUTHOR</h2>
<p> <i>faxspool</i> is Copyright (C) 1993-2002 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. Access control and alias handling suggested by Caz Yokoyama, &lt;caz [at] shoki.osk.psq.mei.co.jp&gt;. </p>
<h2>Index</h2>
