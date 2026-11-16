---
title: "isdnrep(1)"
name: "isdnrep"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isdnrep/"
description: "isdnrep – report ISDN activity"
---

<h2 class="name">NAME</h2>
<p> isdnrep &#8211; report ISDN activity</p>
<h2>DESCRIPTION</h2>
<p> Isdnrep reads the isdnlog log files, generates reports, does statistics, and other things. It can also generate HTML output for use with a web server. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></dt>
<dd> show version information and exit. </dd>
<dt><code>-a<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all</code></dt>
<dd> Show all connections registered. If this option is<br />
 not given, show only the connections made today. </dd>
<dt><code>-S<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Summary</code></dt>
<dd> Show a summary (no individual calls) for selected date range. If this<br />
 option is given twice, the summaries per day are hidden too. Don&#8217;t use with <code>-h</code> </dd>
<dt><code>-h<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>no header</code></dt>
<dd> There will be no header for each day, nor will the summary at the end<br />
 of each day and at the end of the report be generated. This is useful if the output is to be processed by another program. </dd>
<p> This option doesn&#8217;t work if the <code>-wX</code> is also given. </p>
<dt><code>-n<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>numbers</code></dt>
<dd> Display numbers instead of the aliases for those numbers.</dd>
<dt><code>-fFILE</code></dt>
<dd> The file from which to generate the report. This is usually /var/log/isdn.log, or whatever is configured in /etc/isdn/isdn.conf as <code>LOGFILE = .</code> The -f option will override the setting in /etc/isdn/isdn.conf. </dd>
<dt><code>-t time span<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>time=time span</code></dt>
<dd> With this option a specific time span covered by the log file can be<br />
 displayed, e.g. all calls in November 1995, or on January 3rd 1996 between 03:00 and 09:45. </dd>
<p> The format in which times are given is described below. The time span has the following syntax: </p>
<dl>
<dl>
<dt>time-time</dt>
<dd> display from begin time up to end time</dd>
<dt>time-</dt>
<dd> display from given time up to &quot;now&quot;</dd>
<dt>-time</dt>
<dd> display from beginning of log file up to given time</dd>
<dt>time</dt>
<dd> display the given month, day, hour, &#8230;</dd></dl>
</dl>
<dt><code>-d -time<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>delete=time</code></dt>
<dd> Delete entries from the log file up to (but not including) the specified<br />
 time. The format is the same as for the -t option. The minus before the time <code>must</code> be given! It is not possible to define begin and end times; entries are always deleted from the beginning up to the time given. </dd>
<p> <code>Warning!</code> Entries are <code>really</code> deleted from the file. Careless use can result in all entries being deleted, e.g. with &quot;isdnrep -d -&quot;. </p>
<dt><code>-E<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>print Errors</code></dt>
<dd> Display all connections and connection attempts. Without this option,<br />
 only successful connections are displayed. </dd>
<dt><code>-v<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>verbose</code></dt>
<dd> Display warnings on start-up.</dd>
<dt><code>-c<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ignore default options</code></dt>
<dd> Do not append the &quot;REPOPTIONS&quot; setting from /etc/isdn/isdn.conf<br />
 to the command line. </dd>
<dt><code>-p [n][m]&#8217;number'[,[m]&#8217;number&#8217;&#8230;]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>phonenumber</code></dt>
<dd> Display only selected phone numbers.</dd>
<p> &quot;number&quot; is specified in the same format as in configuration files (see <a href="/docs/linux/man/5-isdn-conf/">isdn.conf</a>(5)). E.g. wildcards can be used. </p>
<p> If the flag &#8216;m&#8217; is given, the corresponding MSN is meant. E.g.: &quot;m2&quot; means MSN#2. If &quot;m0&quot; is given, all numbers are to be displayed. </p>
<p> If the flag &#8216;n&#8217; is given, the given number is <code>not</code> to be displayed. </p>
<dt><code>-U [_][.]&#8217;number&#8217; default source number</code></dt>
<dd> Use &#8216;number&#8217; as source number for outgoing calls with an unknown source number (&quot;?&quot;). &#8216;.&#8217; is replaced by country and area code from isdn.conf. </dd>
<p> With &#8216;_&#8217; the default source number is used internally (e.g. for fetching the right zone names from the ratefile) but it is not displayed. </p>
<dt><code>-i<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>incoming</code></dt>
<dd> Only incoming connections are displayed.</dd>
<dt><code>-o<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>outgoing</code></dt>
<dd> Only outgoing connections are displayed.</dd>
<dt><code>-xX<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>include/exclude calls</code></dt>
<dd> Select calls by day and/or hour. The following selections are possible<br />
 and can specified in any combination and quantity using <code>: </code> as separator:</dd>
<dl>
<dl>
<dt>d<i>daylist</i></dt>
<dd> only days matching <i>daylist</i></dd>
<dt>D<i>daylist</i></dt>
<dd> all days not matching <i>daylist</i></dd>
<dt>h<i>timelist</i></dt>
<dd> only hours matching <i>timelist</i></dd>
<dt>H<i>timelist</i></dt>
<dd> all hours not matching <i>timelist</i></dd></dl>
</dl>
<p> <i>daylist</i> and <i>timelist</i> have the same syntax as described in <i><a href="/docs/linux/man/5-rate-files/">rate-files</a>(5)</i>. If a day or an hour is included and excluded it will be excluded. </p>
<p> Example: </p>
<dl>
<dt>
</dt><dd> -xd2-4:DH:h9-17:H12-15</dd></dl>
<p> This will display all calls on Tuesdays, Wednesdays, or Thursdays that are not holidays with a start time between 09:00 and 12:00 or 15:00 and 17:00. </p>
<dt><code>-u<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>unknown caller</code></dt>
<dd> At the end of the report, all numbers not aliased in callerid.conf or<br />
 ~/.isdn are displayed. This option is unavailable when HTML output is requested. </dd>
<dt><code>-LX<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>summary lists</code></dt>
<dd> Select the summaries in the footer by any combination of the following<br />
 letters:</dd>
<dl>
<dl>
<dt>i,I</dt>
<dd> foreign numbers of incoming calls</dd>
<dt>o,O</dt>
<dd> foreign numbers of outgoing calls</dd>
<dt>c,C</dt>
<dd> foreign numbers of all calls</dd>
<dt>z,Z</dt>
<dd> zones of outgoing calls</dd>
<dt>p,P</dt>
<dd> providers of outgoing calls</dd>
<dt>m,M</dt>
<dd> MSNs (own subscriber numbers) of outgoing calls</dd></dl>
</dl>
<p> Upper case letters deselect, lower case letters select a summary. With at least one lower case letter, only the selected summaries are shown, as long as they are not also deselected. -LiI for example will show no summary at all. Per default all summaries are displayed. </p>
<dt><code>-rPROV recompute</code></dt>
<dd> Recompute the connection fees with the current ratefile instead of showing the amounts stored in the logfile as usual. The provider <code>PROV</code> for recomputation is selected in one of the following ways: </dd>
<dl>
<dl>
<dt>&#8211;</dt>
<dd> Use the logged provider.</dd>
<dt>pNUM</dt>
<dd> Use provider with Pnum NUM (according to P: tag in ratefile). The provider variant is taken from rate.conf where the provider must be enabled.</dd>
<dt>pNUM_VAR</dt>
<dd> Use provider with Pnum NUM and variant VAR (according to P:NUM,VAR in ratefile). No requirements for rate.conf.</dd>
<dt>vVBN</dt>
<dd>
</dd><dt>vVBN_VAR</dt>
<dd> Similar to pNUM[_VAR] but the provider is selected via VBN (B: tag in ratefile) instead of Pnum.</dd>
<dt>b</dt>
<dd> Use the cheapest of all booked providers. The provider selection is done per call. Booked providers are those, which are enabled in rate.conf</dd>
<dt>B</dt>
<dd> Like b but allow all providers, not only the booked.</dd></dl>
</dl>
<dt><code>-m</code>[<code>*</code>|<code>/</code>]<i>number</i><code> modify call costs</code></dt>
<dd> Multiply (*) or divide (/) the stored or recalculated call costs by number before displaying them. If neither * nor / is given, multiply. </dd>
<dt><code>-wX<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>WWW</code></dt>
<dd> isdnrep can give its output in HTML format; this is switched on with<br />
 this option. Two modes are possible: </dd>
<dl>
<dl>
<dt>0</dt>
<dd> The HTML header is suppressed. Useful if the output is to be included into an existing page.</dd>
<dt>1</dt>
<dd> A complete HTML page is generated.</dd></dl>
</dl>
<dt><code>-sX<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>format string</code></dt>
<dd> The output generated by isdnrep can be modified by specifying the format<br />
 of the line generated for each connection. The syntax is similar to that used by printf. The following parameters are possible (the <code>x</code> where given means that a width for the field, also known as the precision, must be given): </dd>
<dl>
<dl>
<dt>%X</dt>
<dd> time without date, e.g. 23:54:06</dd>
<dt>%x</dt>
<dd> the date, e.g. 25/07/97</dd>
<dt>%y</dt>
<dd> date without year, e.g. Sun May 04</dd>
<dt>%Y</dt>
<dd> year, in four digits, e.g. 1997</dd>
<dt>%D</dt>
<dd> duration of connection, e.g. 00:03:34</dd>
<dt>%<code>x</code>H</dt>
<dd> the local MSN; if an alias can be found, that will be displayed instead</dd>
<dt>%<code>x</code>h</dt>
<dd> the local MSN, only as a number; no aliases will be substituted</dd>
<dt>%<code>x</code>F</dt>
<dd> the remote number; if an alias can be found, that will be displayed instead</dd>
<dt>%<code>x</code>f</dt>
<dd> the remote number, only as a number; no aliases will be substituted</dd>
<dt>%<code>x</code>L</dt>
<dd> the town corresponding to the local MSN if known; an empty string otherwise</dd>
<dt>%<code>x</code>l</dt>
<dd> the town corresponding to the remote number if known; an empty string otherwise</dd>
<dt>%T</dt>
<dd> an arrow indicating the direction of the connection (&quot;-&gt;&quot; outgoing or &quot;&lt;-&quot; incoming); the local MSN should be displayed on the left side of this.</dd>
<dt>%t</dt>
<dd> an arrow indicating the direction of the connection, reversed (&quot;&lt;-&quot; outgoing or &quot;-&gt;&quot; incoming); the local MSN should be displayed on the right side of this.</dd>
<dt>%<code>x</code>u</dt>
<dd> the charge units, if known, e.g. 6 EH</dd>
<dt>%U</dt>
<dd> the cost, if known, e.g. 2,28 DM</dd>
<dt>%<code>x</code>j</dt>
<dd> the name of the used provider</dd>
<dt>%v</dt>
<dd> the VBN (carrier selection prefix) of the provider, e.g. 01012</dd>
<dt>%V</dt>
<dd> the VBN and variant of the provider, e.g. 01012_3</dd>
<dt>%I</dt>
<dd> amount of INPUT data</dd>
<dt>%O</dt>
<dd> amount of OUTPUT data</dd>
<dt>%P</dt>
<dd> INPUT throughput (bps)</dd>
<dt>%p</dt>
<dd> OUTPUT throughput (bps)</dd>
<dt>%S</dt>
<dd> Service Indicator</dd>
<dt>%G</dt>
<dd> displays a HTTP link to the corresponding fax, when a fax was received by mgetty. This fax can be displayed by using the link in a HTTP browser. </dd>
<p> This option is only valid when used with -wx, see below for more information.</p>
<dt>%C</dt>
<dd> displays a HTTP link to the corresponding voice file, when a call was recorded by vbox. This option is only valid when used with -wx, see below for more information.</dd></dl>
</dl>
<p> The default format string for (non-HTML output) is</p>
<dl>
<dt>
</dt><dd> &quot; %X %D %15.15H %T %-15.15F %7u %U %I %O&quot;</dd></dl>
<p> With the following string all the important data is displayed while keeping the total length to 80: </p>
<dl>
<dt>
</dt><dd> &quot;%X%D %10.10H%T%-14.14F%U%I %O&quot;</dd></dl>
<p> The above string is put into isdn.conf at installation as <code>REPFMTSHORT</code> and can be used with <code>-Fshort.</code> </p>
<p> Without showing the transferred bytes, this string also fits into 80 chars: </p>
<dl>
<dt>
</dt><dd> &quot; %X %D %16.16H %T %-25.25F %U&quot;</dd></dl>
<p> It is included as <code>REPFMTNIO.</code> </p>
<dt><code>-FX<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>format</code></dt>
<dd> format strings can be specified in isdn.conf; this option<br />
 is used to select one of these. Entries can be defined in the section [ISDNLOG] with names beginning with &quot;REPFMT&quot;. The string after the -F option is added to REPFMT to find the correct entry. Case is not sensitive. E.g.: </dd>
<pre>
REPFMT1        = ... # -&gt; isdnrep -F1
REPFMTMYSTRING = ... # -&gt; isdnrep -Fmystring or
                          isdnrep -F MYSTRING
</pre>
</dl>
<h2>HTML USE</h2>
<p> isdnrep can generate a HTML page containing links to files generated by vbox and mgetty (faxes), so that the messages and faxes can be heard or seen from within a browser. However, a couple of things need to be configured first. </p>
<p> answering machine messages </p>
<p> The %C can be used in the isdnrep output format to make a link to a voice recording file. For this to work, the following entry is needed in the [ISDNLOG] section in isdn.conf: </p>
<pre>
    VBOXPATH= /var/spool/vbox/fred/incoming # incoming directory pathname
</pre>
<p> Now isdnrep can find the file correctly. Clicking on this link will cause the file to be sent. These files are in ZyXEL format; the browser cannot use these directly. The type is given by isdnrep as follows: </p>
<pre>
    Content-Type: application/x-zyxel4
</pre>
<p> The correct application (helper) for this has to be configured in the browser. Alternatively, a conversion program can be specified to isdnrep which will convert the ZyXEL format. The pathname of the file to convert is given as a parameter to the program. </p>
<p> In the [ISDNLOG] section of isdn.conf an entry as follows specifies which conversion program to use: </p>
<pre>
    VBOXCMD1 = /usr/bin/program1
for versions 0.x and 1.x of vbox, and
    VBOXCMD2 = /usr/bin/program2
</pre>
<p> for versions 2.x of vbox. Both entries can be given, isdnrep recognizes which version created the recording. </p>
<p> The program must first output a line with the content-type, followed by the data itself. To convert the ZyXEL format into a WAV file, the following script may be used:</p>
<dl>
<dt>
</dt><dd>
<pre>
#! /bin/sh
##
## script to play voice messages from vbox-2.0
##
## WARNING! If the paths are not set correctly,
## netscape may simply crash!
PATH=$PATH:&quot;path to sox&quot;:&quot;path to pvftools&quot;:&quot;path to vbox&quot;
FILENAME1=/tmp/voxplay.$$.voc
FILENAME2=/tmp/voxplay.$$.wav
VOLUME=8
vboxtoau &lt;$1             | \
          autopvf        | \
          pvfamp $VOLUME | \
          pvfcut 0.20    | \
                pvftovoc &gt; $FILENAME1
sox $FILENAME1 $FILENAME2
echo Content-Type: audio/x-wav
echo
cat $FILENAME2
rm -f $FILENAME1 $FILENAME2
</pre>
</dd></dl>
<p> The script above needs the packages sox and pvftools. Additionally, the browser needs to be told how to handle &quot;audio/x-wav&quot;. This is done by adding the following lines to the files listed: </p>
<pre>
<dl><dl>
<dt><code>~/.mime.types</code>
</dt><dd>type=audio/x-wav    \
desc=&quot;auWAV Audio&quot;  \
exts=&quot;wav&quot;
</dd><dt><code>~/.mailcap</code>
</dt><dd>audio/x-wav;/usr/bin/auplay %s
</dd></dl>
</dl>
</pre>
<p> The NAS (Network Audio System) package may be needed. </p>
<p> Now, when the browser is started, it will recognize WAV files and start the corresponding program to handle them. The WAV format has been chosen as it can also be played from a Windows PC. </p>
<p> faxes received by mgetty </p>
<p> When %G is used in the isdnrep output format, any faxes received by mgetty will be accessible via a HTML link, in the same manner as the answering machine messages. </p>
<p> For the faxes the following entry in the [ISDNLOG] section in isdn.conf is needed: </p>
<pre>
    MGETTYPATH = /var/spool/fax/incoming
</pre>
<p> WARNING: if isdnrep doesn&#8217;t have permission to read the files, they will not be displayed; there will be no error message. </p>
<p> When isdnrep passes these files back to the browser, they have the G3 format. The following header is used to notify the browser of this: </p>
<pre>
    Content-Type: application/x-faxg3
</pre>
<p> As the browser probably doesn&#8217;t understand this format, the following changes to the files listed are needed: </p>
<pre>
<dl><dl>
<dt><code>~/.mime.types</code>
</dt><dd>type=application/x-faxg3  \
desc=&quot;G3-Fax Format&quot;      \
exts=&quot;fax,g3&quot;
</dd><dt><code>~/.mailcap</code>
</dt><dd>pplication/x-faxg3;/usr/X11/bin/g3view %s
</dd></dl>
</dl>
</pre>
<p> The program g3view has to be installed for this to work. </p>
<p> If now the link is clicked on, the browser will automatically start the external g3view to handle this data. </p>
<p> If you prefer another format (instead of G3) such as JPEG, the format has to be converted. The following entry in the [ISDNLOG] section of isdn.conf takes care of this: </p>
<pre>
VBOXCMD = /usr/bin/g3tojpeg # example
</pre>
<p> The script g3tojpeg can be something like this: </p>
<dl>
<dt>
</dt><dd>
<pre>
#! /bin/sh
##
## command to display faxes in a browser
##
## WARNING! If the paths are not set correctly,
## netscape may simply crash!
export PATH=$PATH:&quot;path to g3topbm&quot;:&quot;path to convert&quot;
echo Content-Type: image/jpeg
echo
g3topbm &lt; $1 | convert pbm:- jpeg:-
</pre>
</dd></dl>
<p> The packages ImageMagick and mgetty are needed. Mgetty is probably already installed if you want to use this feature :-) </p>
<p> The advantage of the JPEG format is that it can also be displayed by a browser running on a Windows PC. </p>
<p> summary </p>
<p> A suitable value for REPFMTWWW is </p>
<pre>
    REPFMTWWW = &quot;%X %D %17.17H %T %-17.17F %-20.20l SI: %S %9u %U %I %O %G %C&quot;
</pre>
<p> Netscape 3.0 Gold and Arena have been tested, and both work fine with isdnrep&#8217;s HTML output, although Arena&#8217;s display is not as colourful as Netscape&#8217;s. </p>
<p> A known problem (which is impossible to solve completely) is determining the relationship between an isdn connection and a fax or vbox recording. Unfortunately the times for isdnrep, mgetty and vbox differ. Isdnrep tries to make the best guess, but it&#8217;s always possible that e.g. a fax is connected to the wrong isdn connection. </p>
<h2>EXAMPLE OUTPUT</h2>
<p> With the default configuration the following output can be generated on stdout (whitespace slightly edited for clarity): </p>
<dl>
<dt>
</dt><dd>
<pre><code>
$ isdnrep -v -t 6/1/96
I S D N  Connection Report  -  Tue Aug 26 22:21:19 1997
Sat Jan  6 1996
  00:54:19                 UNKNOWN -&gt; UNKNOWN     No user responding      (4)
[...]
  16:33:24  0:03:23        UNKNOWN -&gt; UNKNOWN        7 EH      0,84 DM
  17:33:47                 UNKNOWN -&gt; UNKNOWN     Unallocated (unassigned)(5)
                                                  number
  20:02:28  0:02:37     Phone/HDLC &lt;- UNKNOWN                             (1)
  20:09:53  0:07:01     Modem/X.75 -&gt; T-Online       3 EH      0,36 DM    (2)
  21:27:56                 UNKNOWN -&gt; UNKNOWN     User busy               (3)
  22:09:41  0:29:36        UNKNOWN -&gt; UNKNOWN       43 EH      9,89 DM*
======================================================================
  1 IN= 0:02:37,  13 OUT= 3:40:14,   3 failed      210 EH     25,20 DM
(6)^^^^^^^^^^^^  (7)^^^^^^^^^^^^^  (8)^^^^^^^   (9)^^^^^^ (10)^^^^^^^^
DIALOUT Summary for Sat Jan  6 1996                                      (11)
-----------------------------------------------------------
T-Online         1 call(s)  0:07:01     3 EH    0,36 DM
UNKNOWN         11 call(s)  0:17:00    20 EH    2,40 DM
DIALIN Summary for Sat Jan  6 1996                                       (12)
-----------------------------------------------------------
UNKNOWN          1 call(s)  0:02:37
Zone 1 : City              2 call(s)  2:23:13     50 EH    6,00 DM       (13)
Zone x : UNKNOWN          11 call(s)  0:17:00     20 EH    2,40 DM
</code></pre>
</dd></dl>
<p> <code>Notes</code></p>
<dl>
<dl>
<dt>
&nbsp;<wbr>(1)</dt>
<dd> &quot;xxx &lt;- xxx&quot; was an incoming call, so doesn&#8217;t cost anything</dd>
<dt>
&nbsp;<wbr>(2)</dt>
<dd> &quot;xxx -&gt; xxx&quot; was an outgoing call lasting 203 seconds, so for City zone, off-peak time (Saturday), 3 charge units = DM 0,36</dd>
<dt>
&nbsp;<wbr>(3)</dt>
<dd> there was no connection, as the called party was busy</dd>
<dt>
&nbsp;<wbr>(4)</dt>
<dd> there was no connection, as the called party didn&#8217;t pick up the phone</dd>
<dt>
&nbsp;<wbr>(5)</dt>
<dd> &quot;the number you have dialed is not connected. Hang up and dial again. &#8230;&quot;</dd>
<dt>
&nbsp;<wbr>(6)</dt>
<dd> total time for incoming calls</dd>
<dt>
&nbsp;<wbr>(7)</dt>
<dd> total time for outgoing calls</dd>
<dt>
&nbsp;<wbr>(8)</dt>
<dd> 3 calls failed; busy (3), no answer (4) and error in dialing (5)</dd>
<dt>
&nbsp;<wbr>(9)</dt>
<dd> total charge units incurred for one day</dd>
<dt>(10)</dt>
<dd> total costs incurred for one day</dd>
<dt>(11)</dt>
<dd> outgoing calls grouped per number</dd>
<dt>(12)</dt>
<dd> incoming calls grouped per number</dd>
<dt>(13)</dt>
<dd> outgoing and incoming calls grouped per tariff zone</dd></dl>
</dl>
<p> If the charge units are marked with &quot;*&quot;, the PTT switch did not give charge info; these are the number of units guestimated by isdnrep. </p>
<h2>TIME FORMAT</h2>
<p> For the -d and -t options, the time is specified in the following formats: </p>
<dl>
<dt>[DD/][M]M/[[YY]YY]</dt>
<dd> specifies the month or day. </dd>
<p> Examples: </p>
<dl>
<dl>
<dt>7/</dt>
<dd> July of the current year</dd>
<dt>8/1996</dt>
<dd> August 1996</dd>
<dt>29/6/05</dt>
<dd> June 29th 2005</dd>
<dt>6/6/</dt>
<dd> error, is not June 6th of the current year; it&#8217;s June 1906</dd></dl>
</dl>
<dt>[D]D</dt>
<dd> day of current month </dd>
<dt>[D]D.[M]M.[[[CC]Y]Y]</dt>
<dd> specifies a day. If century or year and century are missing, they will be taken from the current date. </dd>
<p> Examples: </p>
<dl>
<dl>
<dt>23.5.</dt>
<dd> May 23rd in the current year</dd>
<dt>19.01.38</dt>
<dd> January 19th 2038</dd>
<dt>16.10.1998</dt>
<dd> October 16th 1998</dd></dl>
</dl>
<dt>[MM]DD[hhmm[[CC]YY][.ss]]</dt>
<dd> specifies an exact time. Unspecified parts are defined as 0 when interpreted as a begin time, and 23 or 59 when interpreted as an end time. </dd>
<p> If a year is to be specified, the hours and minutes <code>must</code> also be specified. </p>
<p> The format is copied from the date command. </p>
<p> Examples: </p>
<dl>
<dl>
<dt>0107</dt>
<dd> January 1st in the current year</dd>
<dt>0107173196.25</dt>
<dd> January 7th 1996 17:31:25</dd>
<dt>010717311996</dt>
<dd> January 7th 1996 17:31:00 (or 17:31:59)</dd>
<dt>12141995</dt>
<dd> error: <code>not</code> December 12th 1995, but December 12th of the current year at 19:95, so it&#8217;s garbage.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> Examples of time spans and their meaning:</dd>
<dl>
<dl>
<dt>6/95-081214381996.25</dt>
<dd> all entries between June 1st 1995 00:00:00 and August 12th 14:38:25</dd>
<dt>0912030495.20-12/95</dt>
<dd> all entries between September 12th 1995 03:04:20 and December 31st 1995 23:59:59</dd>
<dt>09.06.2006-9/7/6</dt>
<dd> all entries between June 6th 2006 00:00:00 and July 7th 2006 00:00:00</dd>
<dt>7/95</dt>
<dd> all entries between July 1st 1995 00:00:00 and July 31st 1995 23:59:59</dd>
<dt>0908</dt>
<dd> all entries between September 8th in the current year 00:00:00 and September 8th in the current year 23:59:59</dd>
<dt>3</dt>
<dd> third day of the current month</dd></dl>
</dl>
</dl>
<dt>[CC]YY-MM-DDThh:mm:ss</dt>
<dd> specifies a year, a moment, or something between. Each separator &#8216;-&#8216;, &#8216;T&#8217;, and &#8216;:&#8217; can be omitted or not. If the first &#8216;-&#8216; is missing, the century must be given. </dd>
<p> This notation cannot be combined with the above notations. Time spans are noted with &#8216;&#8211;&#8216; instead of &#8216;-&#8216;. If no &#8216;&#8211;&#8216; is given, &#8216;i&#8217; must be noted after the -t option. </p>
<p> Examples: </p>
<dl>
<dl>
<dt>i2002</dt>
<dd> the entire year 2002 from January 1st 00:00:00 to December 31st 23:59:59</dd>
<dt>i200306</dt>
<dd> the entire month June 2003</dd>
<dt>200308&#8211;200309</dt>
<dd> August and September 2003</dd>
<dt>2003-10-03T17&#8211;</dt>
<dd> all entries after October 3rd 2003 16:59:59</dd>
<dt>2003-08-27T11:51:25&#8211;20030827115128</dt>
<dd> 4 seconds at August 27th 2003</dd>
<dt>200306</dt>
<dd> error: neither &#8216;i&#8217; nor &#8216;&#8211;&#8216; given</dd>
<dt>2003-1-4</dt>
<dd> error: leading zeros (at month and day) must not omitted</dd></dl>
</dl>
<dt>&quot;y&quot;</dt>
<dd> yesterday,</dd>
<dt>&quot;yy&quot;</dt>
<dd> the day before yesterday,</dd>
<dt>&quot;yyy&quot;</dt>
<dd> three days ago and so on. For time spans these can also be used in conjunction with the notations explained above. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/var/log/isdn.log</code> or <code>/var/lib/isdn/calls</code></dt>
<dd> isdnlog log file with information about all calls. </dd>
<dt><code>/etc/isdn/isdn.conf</code></dt>
<dd> general configuration </dd>
<dt><code>/etc/isdn/callerid.conf</code></dt>
<dd> aliases for telephone numbers </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-isdnlog/">isdnlog</a>(5) <a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8) <a href="/docs/linux/man/5-isdn-conf/">isdn.conf</a>(5)</code> </p>
<h2>AUTHOR</h2>
<p> This manual page was adapted from isdnlog/README by Paul Slootman &lt;paul [at] isdn4linux.de&gt;, for Debian GNU/Linux and isdn4linux. </p>
<h2>Index</h2>
