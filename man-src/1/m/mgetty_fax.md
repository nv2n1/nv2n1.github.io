---
title: "mgetty_fax(1)"
name: "mgetty_fax"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgetty_fax/"
description: "fax – fax sending and receiving with mgetty+sendfax"
---

<h2 class="name">NAME</h2>
<p> fax &#8211; fax sending and receiving with mgetty+sendfax </p>
<h2>SYNOPSIS</h2>
<p> <code>faxspool</code> [options] phone-number file </p>
<p> <code>faxrm</code> job-id </p>
<p> <code>faxq</code> [options] </p>
<p> <code>faxrunq</code> [options] </p>
<p> <code>faxrunqd</code> [options] </p>
<p> <code>sendfax</code> [options] phone-number file </p>
<p> <code>mgetty</code> [options] tty </p>
<p> <code>pbm2g3</code> [options] [pbm-file] </p>
<p> <code>g32pbm</code> [options] [pbm-file] </p>
<p> <code>g3cat</code> [options] [g3-file(s)] </p>
<h2>DESCRIPTION</h2>
<p> This manpage very briefly describes every program from the mgetty+sendfax fax/modem software suite. For details, see the manpages for each program. </p>
<p> <i>faxspool</i> is used to queue jobs for later transmission by fax. <i>faxspool</i> accepts different input formats, converts them into the proper format required by <i>sendfax</i> and places the jobs into the outgoing spool directory. </p>
<p> <i>faxq</i> displays the current FAX work queue. </p>
<p> <i>faxrm</i> removes one or more jobs from the current fax work queue. You have to specify the job id (returned by faxq) on the command line. </p>
<p> <i>faxrunq</i> processes all the faxes in the fax work queue, and sends them one-by-one. If transmission isn&#8217;t possible, the job will be retried later. While meant to be run from <i>cron,</i> <i>faxrunq</i> can as well be started from the shell (but you must have access to the fax queue and the modems, which means you must be &#8216;root&#8217; or &#8216;fax&#8217;) </p>
<p> <i>faxrunqd</i> is a replacement for <i>faxrunq</i> to be used in environments that send a high number of faxes per day, or need more flexibility. </p>
<p> <i>sendfax</i> is the backend used by faxrunq for actually sending the fax. It is not meant to be ever called directly, but can be used in own applications. </p>
<p> <i>faxq-helper</i> is a helper program that is used by <i>faxspool,</i> <i>faxq</i> and <i>faxrm</i> to access the fax spool directory (which is not world-writeable since mgetty version 1.1.29). </p>
<p> <i>mgetty</i> is the part of the program suite that handles incoming calls. Data calls are handled as <i>getty</i> does it (login, shell), while fax calls are handled internally. The received faxes are stored in /var/spool/fax/incoming. See the <a href="/docs/linux/man/8-mgetty/">mgetty</a>(8) manpage for details. <i>mgetty </i> can not be called directly, it must be called by /etc/init. </p>
<p> <i>pbm2g3 </i> is used to convert portable bitmaps to G3 fax data (for sendfax). Do not use the pbmtog3 program from the pbmplus or netpbm toolkit, it will create broken G3 data. </p>
<p> <i>g32pbm</i> is used to convert received faxes (which are stored in G3 format) to portable bitmap format. PBM can be converted to other formats with the named pbmplus toolkit. </p>
<p> <i>g3cat</i> is used to concat multiple G3 files, as <i>cat</i> does with text files. </p>
<h2>FILES</h2>
<dl>
<dt><code>/var/spool/fax/outgoing/</code></p>
<dd> outgoing fax spool directory</p>
<dt><code>/var/spool/fax/incoming/</code></p>
<dd> incoming faxes</p>
<dt><code>/usr/lib64/mgetty+sendfax/</code></p>
<dd> The cover page program, faxq-helper, and a few font files live here.</p>
<dt><code>/etc/mgetty+sendfax/</code></p>
<dd> most configuration files for mgetty and sendfax live here.</p>
<dt><code>/usr/sbin</code></p>
<dd> mgetty, sendfax and faxrunqd live here</p>
<dt><code>/usr/bin</code></p>
<dd> all the other programs</p>
<dt><code>/etc/mgetty+sendfax/faxaliases</code></p>
<dd> global fax alias file</p>
<dt><code>$HOME/.faxnrs</code></p>
<dd> private fax alias file</p>
<dt><code>/etc/mgetty+sendfax/fax.allow</code></p>
<dd> list of allowed users</p>
<dt><code>/etc/mgetty+sendfax/fax.deny</code></p>
<dd> list of denied users</p>
<dt><code>/etc/mgetty+sendfax/faxheader</code></p>
<dd> fax page header</p>
<dt><code>/usr/lib64/mgetty+sendfax/make.coverpg</code></p>
<dd> program to create fax cover page (see <a href="/docs/linux/man/1-coverpg/">coverpg</a>(1)).</p>
<dt><code>/etc/mgetty+sendfax/login.config</code></p>
<dd> login configuration file for mgetty.</p>
<dt><code>/etc/mgetty+sendfax/dialin.config</code></p>
<dd> caller ID setup file for mgetty (optional).</p>
<dt><code>/etc/mgetty+sendfax/mgetty.config</code></p>
<dd> runtime configuration file for mgetty (not implemented yet).</p>
<dt><code>/etc/mgetty+sendfax/sendfax.config</code></p>
<dd> runtime configuration file for sendfax (optional). </p>
</dl>
<h2>BUGS</h2>
<p> Look into the responding man pages. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), <a href="/docs/linux/man/1-faxq/">faxq</a>(1), <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1), <a href="/docs/linux/man/8-faxrunqd/">faxrunqd</a>(8), <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8), <a href="/docs/linux/man/1-faxrm/">faxrm</a>(1), <a href="/docs/linux/man/8-mgetty/">mgetty</a>(8), <a href="/docs/linux/man/1-pbm2g3/">pbm2g3</a>(1), <a href="/docs/linux/man/1-g32pbm/">g32pbm</a>(1), <a href="/docs/linux/man/1-g3cat/">g3cat</a>(1), <a href="/docs/linux/man/5-faxqueue/">faxqueue</a>(5), <a href="/docs/linux/man/4-mgettydefs/">mgettydefs</a>(4), <a href="/docs/linux/man/1-coverpg/">coverpg</a>(1) </p>
<p> mgetty.info</p>
<h2>AUTHOR</h2>
<p> The <i>mgetty+sendfax</i> program suite is Copyright (C) 1993-2002 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. Parts of the programs kindly donated by Chris Lewis, Paul Sutcliffe, Klaus Weidner, and numerous others. </p>
<h2>Index</h2>
