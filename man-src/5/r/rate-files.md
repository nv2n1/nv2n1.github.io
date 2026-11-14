---
title: "rate-files(5)"
name: "rate-files"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rate-files/"
description: "rate-files – Format of rate-files"
---

<p>rate-files &#8211; Format of rate-files</p>
<h2>Description</h2>
<p>The rate-files used by <a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8) and by <a href="/docs/linux/man/1-isdnrate/">isdnrate</a>(1) are textfiles defining the telephone fees for different destinations at certain dates/times for all providers of one country.<br />
 The rate-files have the following overall layout: </p>
<p> <i>Header entries</i> </p>
<p> <i>Provider entries</i> </p>
<p> Comments starting with a hash-sign &#8216;#&#8217; and empty lines are ignored. The first letter (tag) followed by a colon separates the entries. Additional white space may be used after the tags to group content more readably.</p>
<h3>Special entries</h3>
<p><code>I:includefile</code> </p>
<p> <code>i:includefile</code> </p>
<dl>
<dd><i>includefile</i> get&#8217;s substituted at the current position. There are two possibilities. In the rate source file (which is prepared by <i>pp_rate</i>) a small <i>&#8216;i&#8217;</i> puts the contents of the include file in the outputfile. An <i>&#8216;I&#8217;</i>-Tag means, for the preprocessor, write a new output file (the includefile) and leave the tag in the rate-files. This is for real include files.<br />
 Includes may be nested twice. The filename should not contain any paths (except for &#8216;i&#8217; of course), they are taken relative to their parent file.</p>
<dd></dl>
<h3>Header entries</h3>
<p><code>V:versionsstring</code></p>
<dl>
<dd>e.g. V:1.0-Germany [18-Mar-1999]</dl>
<p> <code>S:Servicename</code> </p>
<p> <code>N:Servicenumber[,Servicenumber&#8230;]</code></p>
<dl>
<dd>This defines telephone services with special numbers. Special numbers are numbers which a) start with no &#8216;0&#8217; or b) can not be dialed with every provider. A number with a variable length should have the wildcard &#8216;*&#8217; at the end, eg. <i>07189*</i> which matches all numbers starting with <i>07189</i>. Numbers with wildcards should be placed after numbers which would match the wildcard, because matching is done straight top down. There may be multiple <code>N:</code> tags for one telephone service.</p>
<dd>e.g.<br />
 S:Internet<br />
 N:07189*,19430<br />
 N:19440</dl>
<p> <code>U:currencyfmt currency</code></p>
<dl>
<dd>If the first char of <i>currencyfmt</i> is ^, the amount is multiplied by 100 before it is displayed without leading ^.</p>
<dd>e.g. (one of these, ¢ = cent)<br />
 U:%.3f EUR<br />
 U:^%.3f ¢</dl>
<p> <code>X:num_wildcard = provider[zZone] [,&#8230;]</code></p>
<dl>
<dd>Define exception. If a certain number is always routed to a certain provider and not to the preselected provider, you should use this tag.<br />
 e.g. in Austria, online service numbers 194x or 07189 go always via Telekom, ignoring your preselection:<br />
 X: 194*=1,07189*=1<br />
 or<br />
 X: 194*=1z6<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># Provider 1 Zone 6
</dl>
<h3>Provider entries</h3>
<p>A new provider starts always with a <code>P:</code> tag and consists of a <i>Providerheader</i> followed by <i>Providerzones.</i></p>
<h3>Providerheader</h3>
<p><code>P:</code>[<code>daterange</code>]<code> providernumber providername</code></p>
<dl>
<dd><i>daterange</i> is <code>[</code>[<code>fromDate</code>][<code>-toDate</code>]<code>]</code><br />
 This defines a time range for the validity of rates for this provider. Dates have to be numeric in format <code>dd.mm.yyyy</code>. Note: as time is assumed as 00:00, take for <i>toDate</i> the day+1. The daterange has to be enclosed in square brackets. Either <i>fromDate</i> or <i>-toDate</i> or both may be given.<br />
 The <i>providernumber</i> may be a simple number, normally the last digits of the VBN-number, or <code>providernumber,variant</code> if a provider has different connection fees.<br />
 e.g.<br />
 P:02 UTA<br />
 or<br />
 P:[01.01.1999] 1,1 Telekom Minimumfee</dl>
<p> <code>B:vbn</code> </p>
<p> VBN-Number for provider</p>
<dl>
<dd>e.g. B:1002<br />
 This is the number to select this provider and depends on your country.</dl>
<p> <code>C:COMMENT: comment</code> </p>
<p> <code>COMMENT</code> may be an arbitrary string, but the following entries are used already:</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>C:Name:</code></td>
<td>Providername
</td>
</tr>
<tr VALIGN=top>
<td><code>C:Maintainer:</code></td>
<td>Who did the hard work
</td>
</tr>
<tr VALIGN=top>
<td><code>C:TarifChanged:</code></td>
<td>and when
</td>
</tr>
<tr VALIGN=top>
<td><code>C:Address:</code></td>
<td>Provideraddress
</td>
</tr>
<tr VALIGN=top>
<td><code>C:Homepage:</code></td>
<td>http:URL for provider
</td>
</tr>
<tr VALIGN=top>
<td><code>C:TarifURL:</code></td>
<td>URL for tarif info
</td>
</tr>
<tr VALIGN=top>
<td><code>C:EMail:</code></td>
<td>EMail-Address
</td>
</tr>
<tr VALIGN=top>
<td><code>C:Telefon:</code></td>
<td>Telefon number
</td>
</tr>
<tr VALIGN=top>
<td><code>C:Telefax:</code></td>
<td>Fax number
</td>
</tr>
<tr VALIGN=top>
<td><code>C:Hotline:</code></td>
<td>Telefon number
</td>
</tr>
<tr VALIGN=top>
<td><code>C:Zone:</code></td>
<td>Textual info about zones
</td>
</tr>
<tr VALIGN=top>
<td><code>C:Special:</code></td>
<td>Guess
</td>
</tr>
<tr VALIGN=top>
<td><code>C:GT:</code></td>
<td>Additional charge text
</td>
</tr>
<tr VALIGN=top>
<td><code>C:GF:</code></td>
<td>Additional charge formula
</td>
</tr>
</table>
</dl>
<p> If there are multiple comments with the same comment name, they get appended separated by a newline char. </p>
<p> <code>D:zone</code> </p>
<p> Name of zone file (inserted for <code>%s</code> in ZONEFILE = /usr/lib/isdn/zone-<i>CC</i>-%s.dat from isdn.conf)</p>
<dl>
<dd>e.g. D:1001 # zone file is zone-at-1001.gdbm</dl>
<p> Note: if the provider has no different domestic zones, you should not define a D:tag.</p>
<h3>Providerzones</h3>
<p>A Providerzone entry starts with a <code>Z:</code> tag followed by one or more <code>A:</code> and <code>T:</code> tags. </p>
<p> A zone is a region of areas, for which the same rates apply. Domestic and foreign zones should not be mixed and all foreign zones should follow domestic zones. </p>
<p> <code>R:prov, sub ; zonelist</code> </p>
<p> Read zones from provider <i>prov</i> subprovider number <i>sub</i>. A <i>zonelist</i> is defined below. If the referenced provider doesn&#8217;t have a subprovider number, the <i>sub</i> must be -1. The referenced provider may be defined before or after the R:-tag. The referenced zones must be real Z:-entries, not references themself. The zone numbers and names are taken from the referenced provider. The last <i>to_zone</i> may be missing then all zones from the start zone are used.<br />
 e.g.<br />
 R:1,1 ; 1-4,6, 10- </p>
<p> There some limitations:<br />
 The reference cannot be more exact than the referenced providerzones. R:42,0;1 will not work as desired if P:42,0 defines Z:1-4.<br />
 It is not possible to reference a providerzone without areas when the default domestic zone (with your countrycode as area) is not included in the same range of referenced zones. This applies mainly to zones for different distances in the national fixed network, e.g. Z:1-3 in Germany. </p>
<p> <code>r:prov, sub ; start_zone-</code> </p>
<p> This tag is related to the R:-tag. It is interpreted by the rate-preprocessor <i>pp_rate</i>. All providerzones with a zone number greater or equal <i>start_zone</i> are copied from provider <i>prov[,sub]</i> and replace the r:-tag. If an <i>area</i> is already used in a previous providerzone of the current provider, it will not be copied. If all areas of a providerzone are already defined, the entire zone will not be copied. Lines that contain only comments are also not copied, but comments at the end of other lines are. </p>
<p> This tag is designed for providers with a rate variant that offers different fees for some foreign destinations. </p>
<p> <code>Z:zonelist zonename</code> </p>
<p> where <i>zonelist</i> is <code>zone</code>[<code>-to_zone</code>][<code>,&#8230;</code>]</p>
<dl>
<dd>e.g. Z:1-2,4 Interior
</dl>
<p> <code>A:area</code>[<code>,area&#8230;</code>] </p>
<p> <i>area</i> may be a telephone number (including +countrycode for numbers which may be reached from everywhere, a telephone number without +countrycode for numbers only reachable in the own country) or an area name or alias as defined in country.dat. Country names have to be translated to their code by the rate-preprocessor <i>pp_rate</i>.</p>
<dl>
<dd>e.g. A:19430,07189 # Online</p>
<dd>e.g. A:+31,Belgium # Int 1</dl>
<p> Note: There should always be exactly one zone with your countrycode or countryname respectively:</p>
<dl>
<dd>Z:4<br />
 A:+49<br />
 T:&#8230;</dl>
<p> Countrynames like <i>Belgium</i> in the above example are replaced by their ISO-Code (or TLD) with the rate preprocessor <i>pp_rate</i>. </p>
<p> <code>T:</code>[<code>daterange</code>]<code>daylist/timelist</code>[<code>!</code>]<code>=chargelist chargename</code> </p>
<p> where <i>daterange</i> is <code>[</code>[<code>fromDate</code>][<code>-toDate</code>]<code>]</code> like the corresonding provider entry. Note that the <i>daterange</i> is enclosed in sqare brackets, either <i>fromDate</i> or <i>-toDate</i> are optional. </p>
<p> <i>daylist</i> is <code>day</code>[<code>-day</code>][<code>,&#8230;</code>] and day is a daynumber (1=Mon, 2=Tue, &#8230;) or W (workday, Monday to Friday), E (weekend), H (holiday) or * (everyday). If more than one of these days match a given date, the following order of priority (highest first) applies: H 7 .. 1 E W *. </p>
<p> <i>timelist</i> is <code>hour</code>[<code>-hour</code>][<code>,hour</code>] where hour is a number 0..23 or * for everytime. </p>
<p> After <i>daylist/timelist</i> follows <code>=</code> or <code>!=</code> which means, provider doesn&#8217;t adjust rates on a rate boundary e.g. at 18h00. </p>
<p> A <i>chargelist</i> consists of </p>
<p> [<code>MinCharge|</code>]<code>Charge</code>[<code>(Divider)</code>]<code>/Duration</code>[<code>:Delay</code>][<code>/Duration&#8230;</code>] </p>
<p> where <i>MinCharge|</i> is an (optional) minimum charge, <i>Charge</i> the rate per <i>Duration</i> seconds or optional rate per <i>(Divider)</i> seconds, <i>Duration</i> is the length of one charge unit in seconds. After <i>Delay</i> the next duration is taken. If delay is not given it equals to the duration. The last duration may not have a delay and may not be zero.</p>
<dl>
<dd>EXAMPLES<br />
 T:1-4/8-18=1.5(60)/60/1 workday</p>
<dd>Monday until Thursday, daytime the charge is 1.50 per minute, first charge is for one minute after this charging is calculated in seconds interval.</p>
<dd>T:W/18-8=0.30|1.2(60)/1 night</p>
<dd>On workdays, night, charge is the bigger of 1.20 per minute or 0.30</p>
<dd>T:*/*=0.50/0,1(60)/1 always</p>
<dd>Everyday, everytime there is a connection fee of 0.50, then charge is 1 per minute.</p>
<dd>T:H/*=0.5/60:600,0.5/30 holidays</p>
<dd>On holidays, everytime a charge of 0.5 per minute in a minutes interval, after 10 minutes 0.5 per half minute in half a minutes interval.</p>
<dd>T:*/*=1.3/0,0/1</p>
<dd>Everyday, everytime the charge is 1.30 independent of duration, which could also be written as T:*/*=1.3|0/1.</p>
<dd>T: [-01.02.2000] */17-19=0.79(60)/60/1 Happy Hour<br />
 T: [-01.02.2000] */19-17=0.90(60)/60/1 Normal</p>
<dd>Until the first of Feb 0:00h (i.e. end is 31.1.2000 24:00), everyday between 17 and 19h a charge of 0.79 per minute, the first minute is always charged fully, after this, charging is calculated in seconds interval.<br />
 The second entry defines a charge of 0.90 in the time outside the happy hour.</p>
<dd>T:[15.11.1999-01.02.2000]*/17-19=0.79(60)/60/1 HH</p>
<dd>Like above, but a full date range is given.</dl>
<p> The next two t:-tags are interpreted by <i>pp_rate</i> and replaced by one or more T:-lines. Both methods can be used together. </p>
<p> <code>t:[daterange]?[H]=chargelist chargename</code> </p>
<p> This line is replaced by according T:-lines for not yet defined <i>day/hour</i> pairs. </p>
<p> If a <i>daterange</i> is given, only previous T:-lines without a daterange or with the same daterange will be considered as earlier definitions. If <i>H</i> is noted, definitions will also be added for holidays.</p>
<dl>
<dd>EXAMPLE<br />
 T:W/08-18=0.10/60 normal time<br />
 t:?H=0.04/60 save time</p>
<dd>This lines will lead to the following lines after <i>pp_rate</i>:</p>
<dd>T:W/08-18=0.10/60 normal time<br />
 T:W/18-08=0.04/60 save time<br />
 T:E,H/*=0.04 save time</dl>
<p> <code>t:daterange=srcrange [chargename]</code> </p>
<p> Generates T:-lines for <i>daterange</i> by copying previous T:-lines with <i>srcrange</i> in the same zone. If a <i>chargename</i> is given, it will replace the chargename of the originating line. <i>srcrange</i> can be shortened as long as it remains definite.</p>
<dl>
<dd>EXAMPLE<br />
 T:[-24.12.2003]W/*=0.08/60 on workdays<br />
 T:[-24.12.2003]E,H/*=0.06 weekend<br />
 T:[24.12.2003-25.12.2003]*/*=0.04 Christmas Eve<br />
 t:[25.12.2003-31.12.2003]=[-24.12.2003]<br />
 t:[31.12.2003-01.01.2004]=[24.12.] New Year&#8217;s Eve<br />
 t:[01.01.2004]=[-24.12.]</p>
<dd>This will be transformed into:</p>
<dd>T:[-24.12.2003]W/*=0.08/60 on workdays<br />
 T:[-24.12.2003]E,H/*=0.06/60 weekend<br />
 T:[24.12.2003-25.12.2003]*/*=0.04/60 Christmas Eve<br />
 T:[25.12.2003-31.12.2003]W/*=0.08/60 on workdays<br />
 T:[25.12.2003-31.12.2003]E,H/*=0.06/60 weekend<br />
 T:[31.12.2003-01.01.2004]=0.04/60 New Years&#8217; Eve<br />
 T:[01.01.2004]W/*=0.08/60 on workdays<br />
 T:[01.01.2004]E,H/*=0.06/60 weekend</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8)</i>, <i><a href="/docs/linux/man/1-isdnrate/">isdnrate</a>(1)</i>, <i><a href="/docs/linux/man/5-rate-conf/">rate.conf</a>(5)</i>, isdnlog/README, rate-at.dat</p>
<h2>Author</h2>
<p>Leopold Toetsch &lt;lt [at] toetsch.at&gt; (of this man page of course). Tobias Becker &lt;tobiasb [at] isdn4linux.de&gt; added the tags r: and t:.</p>
