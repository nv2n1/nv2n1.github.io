---
title: "pflogsumm(1)"
name: "pflogsumm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pflogsumm/"
---

<h2 class="name">NAME</h2>
 

 pflogsumm.pl - Produce Postfix MTA logfile summary 

 Copyright (C) 1998-2010 by James S. Seymour, Release 1.1.3. 

<h2>SYNOPSIS</h2>

 <pre><code>
pflogsumm.pl - [eq][-d&lt;today | yesterday&gt;][--detail&lt;cnt&gt;][--bounce_detail&lt;cnt&gt;][--deferral_detail&lt;cnt&gt;][-h&lt;cnt&gt;][-i | --ignore_case][--iso_date_time][--mailq][-m | --uucp_mung][--no_bounce_detail][--no_deferral_detail][--no_no_msg_size][--no_reject_detail][--no_smtpd_warnings][--problems_first][--rej_add_from][--reject_detail&lt;cnt&gt;][--smtp_detail&lt;cnt&gt;][--smtpd_stats][--smtpd_warning_detail&lt;cnt&gt;][--syslog_name = string][-u&lt;cnt&gt;][--verbose_msg_detail][--verp_mung[=&lt;n&gt;]][--zero_fill][file1[filen]] pflogsumm.pl - [help | version] If no file(s) specified, reads from stdin.Output is to stdout.
</code></pre>

<h2>DESCRIPTION</h2>

 <pre>
    Pflogsumm is a log analyzer/summarizer for the Postfix MTA.  It is
    designed to provide an over-view of Postfix activity, with just enough
    detail to give the administrator a &quot;heads up&quot; for potential trouble
    spots.
    
    Pflogsumm generates summaries and, in some cases, detailed reports of
    mail server traffic volumes, rejected and bounced email, and server
    warnings, errors and panics.
</pre>

<h2>OPTIONS</h2>

 
    --bounce_detail &lt;cnt&gt;
                   Limit detailed bounce reports to the top &lt;cnt&gt;.  0
                   to suppress entirely.
    -d today       generate report for just today
    -d yesterday   generate report for just "yesterday"
    --deferral_detail &lt;cnt&gt;
                   Limit detailed deferral reports to the top &lt;cnt&gt;.  0
                   to suppress entirely.
    --detail &lt;cnt&gt;
    
                   Sets all --*_detail, -h and -u to &lt;cnt&gt;.  Is
                   over-ridden by individual settings.  --detail 0
                   suppresses *all* detail.
    -e             extended (extreme? excessive?) detail
                   Emit detailed reports.  At present, this includes
                   only a per-message report, sorted by sender domain,
                   then user-in-domain, then by queue i.d.
                   WARNING: the data built to generate this report can
                   quickly consume very large amounts of memory if a
                   lot of log entries are processed!
    -h &lt;cnt&gt;       top &lt;cnt&gt; to display in host/domain reports.
    
                   0 = none.
                   See also: "-u" and "--*_detail" options for further
                             report-limiting options.
    --help         Emit short usage message and bail out.
    
                   (By happy coincidence, "-h" alone does much the same,
                   being as it requires a numeric argument :-).  Yeah, I
                   know: lame.)
    -i
    --ignore_case  Handle complete email address in a case-insensitive
                   manner.
                   
                   Normally pflogsumm lower-cases only the host and
                   domain parts, leaving the user part alone.  This
                   option causes the entire email address to be lower-
                   cased.
    --iso_date_time
                   For summaries that contain date or time information,
                   use ISO 8601 standard formats (CCYY-MM-DD and HH:MM),
                   rather than "Mon DD CCYY" and "HHMM".
    -m             modify (mung?) UUCP-style bang-paths
    --uucp_mung
                   This is for use when you have a mix of Internet-style
                   domain addresses and UUCP-style bang-paths in the log.
                   Upstream UUCP feeds sometimes mung Internet domain
                   style address into bang-paths.  This option can
                   sometimes undo the "damage".  For example:
                   "somehost.dom!username@foo" (where "foo" is the next
                   host upstream and "somehost.dom" was whence the email
                   originated) will get converted to
                   "foo!username [at] somehost.dom".  This also affects the
                   extended detail report (-e), to help ensure that by-
                    domain-by-name sorting is more accurate.
    --mailq        Run "mailq" command at end of report.
    
                   Merely a convenience feature.  (Assumes that "mailq"
                   is in $PATH.  See "$mailqCmd" variable to path thisi
                   if desired.)
    --no_bounce_detail
    --no_deferral_detail
    --no_reject_detail
                   These switches are depreciated in favour of
                   --bounce_detail, --deferral_detail and
                   --reject_detail, respectively.
                   Suppresses the printing of the following detailed
                   reports, respectively:
                        message bounce detail (by relay)
                        message deferral detail
                        message reject detail
                   See also: "-u" and "-h" for further report-limiting
                             options.
    --no_no_msg_size
                    Do not emit report on "Messages with no size data".
                    Message size is reported only by the queue manager.
                    The message may be delivered long-enough after the
                    (last)
    qmgr log entry that the information is not in
        the
        log(s) processed by a particular run of
                    pflogsumm.pl.  This throws off "Recipients by message
                    size" and the total for "bytes delivered." These are
                    normally reported by pflogsumm as "Messages with no
                    size data."
    --no_smtpd_warnings
                   This switch is depreciated in favour of
                   smtpd_warning_detail
                    On a busy mail server, say at an ISP, SMTPD warnings
                    can result in a rather sizeable report.  This option
                    turns reporting them off.
    --problems_first
                   Emit "problems" reports (bounces, defers, warnings,
                   etc.) before "normal" stats.
    --rej_add_from
                   For those reject reports that list IP addresses or
                   host/domain names: append the email from address to
                   each listing.  (Does not apply to "Improper use of
                   SMTP command pipelining" report.)
    -q             quiet - don't print headings for empty reports
    
                   note: headings for warning, fatal, and "master"
                   messages will always be printed.
    --reject_detail &lt;cnt&gt;
                   Limit detailed smtpd reject, warn, hold and discard
                   reports to the top &lt;cnt&gt;.  0 to suppress entirely.
    --smtp_detail &lt;cnt&gt;
                   Limit detailed smtp delivery reports to the top &lt;cnt&gt;.
                   0 to suppress entirely.
    --smtpd_stats
                   Generate smtpd connection statistics.
                   The "per-day" report is not generated for single-day
                   reports.  For multiple-day reports: "per-hour" numbers
                   are daily averages (reflected in the report heading).
    --smtpd_warning_detail &lt;cnt&gt;
                   Limit detailed smtpd warnings reports to the top &lt;cnt&gt;.
                   0 to suppress entirely.
    --syslog_name=name
                   Set syslog_name to look for for Postfix log entries.
                   By default, pflogsumm looks for entries in logfiles
                   with a syslog name of "postfix," the default.
                   If you've set a non-default "syslog_name" parameter
                   in your Postfix configuration, use this option to
                   tell pflogsumm what that is.
                   See the discussion about the use of this option under
                   "NOTES," below.
    -u &lt;cnt&gt;       top &lt;cnt&gt; to display in user reports. 0 == none.
                   See also: "-h" and "--*_detail" options for further
                             report-limiting options.
    --verbose_msg_detail
                   For the message deferral, bounce and reject summaries:
                   display the full "reason", rather than a truncated one.
                   Note: this can result in quite long lines in the report.
    --verp_mung    do "VERP" generated address (?) munging.  Convert
    --verp_mung=2  sender addresses of the form
                   "list-return-NN-someuser=some.dom [at] host.sender.dom"
                    to
                      "list-return-ID-someuser=some.dom [at] host.sender.dom"
                    In other words: replace the numeric value with "ID".
                   By specifying the optional "=2" (second form), the
                   munging is more "aggressive", converting the address
                   to something like:
                        "list-return [at] host.sender.dom"
                   Actually: specifying anything less than 2 does the
                   "simple" munging and anything greater than 1 results
                   in the more "aggressive" hack being applied.
                   See "NOTES" regarding this option.
    --version      Print program name and version and bail out.
    --zero_fill    "Zero-fill" certain arrays so reports come out with
                   data in columns that that might otherwise be blank.


<h2>RETURN VALUE</h2>

 <pre>
    Pflogsumm doesn't return anything of interest to the shell.
</pre>

<h2>ERRORS</h2>

 <pre>
    Error messages are emitted to stderr.
</pre>

<h2>EXAMPLES</h2>

 <pre>
    Produce a report of previous day's activities:
        pflogsumm.pl -d yesterday /var/log/maillog
    A report of prior week's activities (after logs rotated):
        pflogsumm.pl /var/log/maillog.0
    What's happened so far today:
        pflogsumm.pl -d today /var/log/maillog
    Crontab entry to generate a report of the previous day's activity
    at 10 minutes after midnight.
        10 0 * * * /usr/local/sbin/pflogsumm -d yesterday /var/log/maillog
        2&gt;&amp;1 |/usr/bin/mailx -s &quot;`uname -n` daily mail stats&quot; postmaster
    Crontab entry to generate a report for the prior week's activity.
    (This example assumes one rotates ones mail logs weekly, some time
    before 4:10 a.m. on Sunday.)
        10 4 * * 0   /usr/local/sbin/pflogsumm /var/log/maillog.0
        2&gt;&amp;1 |/usr/bin/mailx -s &quot;`uname -n` weekly mail stats&quot; postmaster
    The two crontab examples, above, must actually be a single line
    each.  They're broken-up into two-or-more lines due to page
    formatting issues.
</pre>

<h2>SEE ALSO</h2>

 <pre>
    The pflogsumm FAQ: pflogsumm-faq.txt.
</pre>

<h2>NOTES</h2>

 <pre><code>
    Pflogsumm makes no attempt to catch/parse non-Postfix log
    entries.  Unless it has "postfix/" in the log entry, it will be
    ignored.
    It's important that the logs are presented to pflogsumm in
    chronological order so that message sizes are available when
    needed.
    For display purposes: integer values are munged into "kilo" and
    "mega" notation as they exceed certain values.  I chose the
    admittedly arbitrary boundaries of 512k and 512m as the points at
    which to do this--my thinking being 512x was the largest number
    (of digits) that most folks can comfortably grok at-a-glance.
    These are "computer" "k" and "m", not 1000 and 1,000,000.  You
    can easily change all of this with some constants near the
    beginning of the program.
    "Items-per-day" reports are not generated for single-day
    reports.  For multiple-day reports: "Items-per-hour" numbers are
    daily averages (reflected in the report headings).
    Message rejects, reject warnings, holds and discards are all
    reported under the "rejects" column for the Per-Hour and Per-Day
    traffic summaries.
    Verp munging may not always result in correct address and
    address-count reduction.
    Verp munging is always in a state of experimentation.  The use
    of this option may result in inaccurate statistics with regards
    to the "senders" count.
    UUCP-style bang-path handling needs more work.  Particularly if
    Postfix is not being run with "swap_bangpath = yes" and/or *is* being
    run with "append_dot_mydomain = yes", the detailed by-message report
    may not be sorted correctly by-domain-by-user.  (Also depends on
    upstream MTA, I suspect.)
    The "percent rejected" and "percent discarded" figures are only
    approximations.  They are calculated as follows (example is for
    "percent rejected"):
        percent rejected =
        
            (rejected / (delivered + rejected + discarded)) * 100
    There are some issues with the use of --syslog_name.  The problem is
    that, even with $syslog_name set, Postfix will sometimes still log
    things with "postfix" as the syslog_name.  This is noted in
    /etc/postfix/sample-misc.cf:
#Beware : a non - default syslog_name setting takes effect only
#after process initialization.Some initialization errors will be
#logged with the default name, especially errors while parsing
#the command line and errors while accessing the Postfix main.cf
#configuration file.
    As a consequence, pflogsumm must always look for "postfix," in logs,
    as well as whatever is supplied for syslog_name.
    Where this becomes an issue is where people are running two or more
    instances of Postfix, logging to the same file.  In such a case:
        . Neither instance may use the default "postfix" syslog name
          and...
        . Log entries that fall victim to what's described in
          sample-misc.cf will be reported under "postfix", so that if
          you're running pflogsumm twice, once for each syslog_name, such
          log entries will show up in each report.
    The Pflogsumm Home Page is at:
        http://jimsun.LinxNet.com/postfix_contrib.html
</code></pre>

<h2>REQUIREMENTS</h2>

 <pre>
    For certain options (e.g.: --smtpd_stats), Pflogsumm requires the
    Date::Calc module, which can be obtained from CPAN at
    <a rel="nofollow" HREF="http://www.perl.com.">http://www.perl.com.</a>
    Pflogsumm is currently written and tested under Perl 5.8.3.
    As of version 19990413-02, pflogsumm worked with Perl 5.003, but
    future compatibility is not guaranteed.
</pre>

<h2>LICENSE</h2>

 <pre>
    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2
    of the License, or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You may have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307,
    USA.
    
    An on-line copy of the GNU General Public License can be found
    <a rel="nofollow" HREF="http://www.fsf.org/copyleft/gpl.html.">http://www.fsf.org/copyleft/gpl.html.</a>
</pre> 

<h2>Index</h2>


