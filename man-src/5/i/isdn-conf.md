---
title: "isdn-conf(5)"
name: "isdn-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-isdn-conf/"
description: "/etc/isdn/isdn.conf – config file for isdnlog"
---

<p>/etc/isdn/isdn.conf &#8211; config file for isdnlog</p>
<h2>Format</h2>
<p>The config file has the format described in <a href="/docs/linux/man/5-isdnformat/">isdnformat</a>(5). I recommend starting isdnlog with -f/etc/isdn/isdn.conf, and storing all options in this file in section [options]. Read the man page for more details. </p>
<p> Isdnlog will always read the /etc/isdn/isdn.conf config file for the sections [global] [variables] and [isdnlog]; it will ignore other sections. To make isdnlog process the [options] section you must pass it with the -f option!</p>
<h2>Global Section</h2>
<p>This section holds common information for all isdn programs. All settings are for EuroISDN (DSS1). </p>
<dl>
<dt><code>AREACODE</code></p>
<dd>Telephone area code of your city. With 1TR6 ISDN protocol you must specify your whole telephone number (without MSN). Required. </p>
<dt><code>AREAPREFIX</code></p>
<dd>Prefix for area code. Default is &quot;0&quot;. Your area code may start with this prefix (e.g. &quot;0721&quot; and &quot;721&quot; is the same area code). Optional. </p>
<dt><code>COUNTRYCODE</code></p>
<dd>Telephone country code (e.g. 49 for Germany). Required. </p>
<dt><code>COUNTRYPREFIX</code></p>
<dd>Prefix for country code. Default is &quot;+&quot;. Your country code may start with this prefix (e.g. &quot;+49&quot; and &quot;49&quot; is the same country code). Optional. </p>
</dl>
<h2>Variables</h2>
<p>The ISDN tools allow to set variables and use them later. All variables must be uppercase. Example : &quot;MYPATH = /home/foo&quot;.</p>
<h2>Isdnlog</h2>
<p>Settings for isdnlog. </p>
<dl>
<dt><code>VBN</code></p>
<dd>The initial numbers of the alternate carrier prefix (to choose an alternate telephone provider). If there is more than one possible prefix, separate them with colons. </p>
<dt><code>VBNLEN</code></p>
<dd>The number of significant digits after the <i>VBN</i> prefix that identify the chosen carrier (provider). If there are different numbers possible, separate them with colons. </p>
<dt><code>PRESELECTED</code></p>
<dd>The default telephone carrier (provider), if no alternate carrier prefix is dialed. </p>
<dt><code>COUNTRYFILE</code></p>
<dd>Location and name of <i>country.dat</i>. This file contains country names, aliases, codes and prefixes. </p>
<dt><code>RATECONF</code></p>
<dd>Location and name of <i>rate.conf</i>. This file defines booked providers and provider variants. </p>
<dt><code>RATEFILE</code></p>
<dd>Location and name of <i>rate-CC.dat</i>, where <i>CC</i> is your country code. This file contains all the connection fees for all providers to various destinations at certain dates/times. See <a href="/docs/linux/man/5-rate-files/">rate-files</a>(5) for more info. </p>
<dt><code>HOLIDAYS</code></p>
<dd>Name and location of <i>holiday-CC.dat</i>. </p>
<dt><code>ZONEFILE</code></p>
<dd>Name and location of <i>zone-CC-PPP.cdb</i>. The provider <i>PPP</i> is taken from the D:-tag in rate-CC.dat and is substituted for &#8216;%s&#8217; in the configuration entry. This file contains domestic zone info for all areas of a country. </p>
<dt><code>DESTFILE</code></p>
<dd>Name and location of the destination database <i>dest.cdb</i>. </p>
<dt><code>LOGFILE</code></p>
<dd>Isdnlog will store a list of all calls in this file, and isdnrep will read this file to calculate isdn telephone costs. Default value is &quot;/var/log/isdn.log&quot;. Optional. </p>
<dt><code>RELOADCMD</code></p>
<dd>Isdnlog can use this command to reactivate the isdn subsystem. Default value is &quot;/etc/rc.d/init.d/isdn restart&quot;. Optional. </p>
<dt><code>STOPCMD</code></p>
<dd>Isdnlog can use this command to stop the isdn subsystem. Default value is &quot;/etc/rc.d/init.d/isdn stop&quot;. Optional. </p>
<dt><code>REBOOTCMD</code></p>
<dd>Isdnlog can use this command to reboot Linux (when all else fails). Default value is &quot;/sbin/reboot&quot;. Optional. </p>
<dt><code>CURRENCY</code></p>
<dd>Cost per charge unit and currency. Default is &quot;0.12,DM&quot;.<br />
 Note: the charge entry is not used anymore. </p>
<dt><code>CHARGEMAX</code></p>
<dd>Isdnlog can manage your isdn costs and prevent you from spending more than a maximum per day. Unit is national currency. Example: In Germany you want to set CURRENCY to &quot;0.12,DM&quot; and CHARGEMAX to &quot;15.00&quot;, so you will spend max. 15 DM per day. Required. </p>
<dt><code>CONNECTMAX</code></p>
<dd>Isdnlog can also limit your online time in seconds per month. Example: &quot;CONNECTMAX=18000,0&quot; will allow you to be 5 hours online per month. Optional. </p>
<dt><code>BYTEMAX</code></p>
<dd>Isdnlog can also limit your transfer in bytes. Example: &quot;BYTEMAX=67108864&quot; will limit your transfer to 64 MB per month. Optional. </p>
<dt><code>REPOPTIONS</code></p>
<dd>General commandline options for isdnrep. The options noted here have the same effect as appended to each isdnrep commandline. Options are separated by <code>;</code> instead of the usual space.<br />
 Example: &quot;REPOPTIONS=-LP;-E&quot; will turn off the provider summary and show failed calls. Optional. </p>
<dt><code>VBOXPATH</code></p>
<dd>Isdnrep can include information from the voice box system vbox in its report. To do this, you must specify the vbox spooldir (e.g. VBOXPATH=/var/spool/vbox/foo/incoming). Optional. </p>
<dt><code>VBOXCMD1 VBOXCMD2</code></p>
<dd>Isdnrep can convert vbox messages. To do this, you should supply a command. VBOXCMD1 is used with old vbox files (&lt;2.0), VBOXCMD2 is used with new vbox files (&gt;=2.0). Example: &quot;VBOXCMD1=/usr/bin/zyxeltowav&quot;. Optional. </p>
<dt><code>MGETTYPATH</code></p>
<dd>Isdnrep can include information from the mgetty fax system in its report. To do this, you must specify the mgetty spooldir (e.g. MGETTYPATH=/var/spool/fax/incoming). Optional. </p>
<dt><code>MGETTYCMD</code></p>
<dd>Isdnrep can convert mgetty fax files. To do this, you should supply a command. Example: &quot;MGETTYCMD=/usr/bin/g3tojpg&quot;. Optional. </p>
<dt><code>START = { &#8230; }</code></p>
<dd>This option is ignored without -S flag or start=yes. Here you can instruct isdnlog to act on any event by starting a command. However, isdnlog can not react on outgoing connections from other isdn devices (e.g. an isdn telephone). Any start commands listed here are used for all connections, including connections from unknown telephone numbers. For more information, please read <a href="/docs/linux/man/5-callerid-conf/">callerid.conf</a>(5). </p>
</dl>
<h2>Format Options</h2>
<p>You can specify different format strings for the way isdnlog reports incoming messages, outgoing messages, isdnrep, and the WWW mode of isdnrep. </p>
<dl>
<dt><code>REPFMT</code></p>
<dd>Format for isdnrep (normal mode). Default is &quot; %X %D %15.15H %T %-15.15F %7u %U %I %O&quot;. </p>
<dt><code>REPFMTWWW</code></p>
<dd>Format for isdnrep (WWW mode). Default is &quot;%X %D %17.17H %T %-17.17F -20.20l SI: %S %9u %U %I %O&quot;. </p>
<dt><code>REPFMTxxx</code></p>
<dd>Additional format strings for isdnrep. </p>
<dt><code>ILABEL</code></p>
<dd>Format for isdnlog (incoming connections). Isdnlog will add the additional information such as RING, TIME, CONNECT &#8230; </p>
<dt><code>OLABEL</code></p>
<dd>Format for isdnlog (outgoing connections). Isdnlog will add the additional information such as RING, TIME, CONNECT &#8230; </p>
<dt><code>FORMAT MACROS</code></p>
<dd>You can build the format string for any combination of normal chars, digits and these special cookies: </p>
<dt>%t</p>
<dd>tei </p>
<dt>%C</p>
<dd>Call reference </p>
<dt>%Nx</p>
<dd>Remote site&#8217;s telephone number: %N0 exact number, %N1 isdnlog adds country and area prefix to number, %N2 isdnlog beautifies number and adds location, %N3 area code, %N4 number without area code, %N5 alias name, %N6 location, %N7 country code </p>
<dt>%nx</p>
<dd>Local site&#8217;s telephone number (encoding like %N). </p>
<dt>%cx</p>
<dd>Telephone number as given by CLIP (encoding like %N). </p>
<dt>%A</p>
<dd>the text &quot; alias &lt;MSN&gt;&quot; if CLIP message, otherwise empty. </p>
<dt>%I</p>
<dd>Magic tab : empty if first active B-Channel, two blanks if second B-Channel, &quot;* &quot; if new connection (B-Channel not yet assigned). </p>
<dt>%a</p>
<dd>Day of week (e.g. &quot;Fri&quot;) </p>
<dt>%b</p>
<dd>Month (e.g. &quot;Aug&quot;) </p>
<dt>%e</p>
<dd>Day of month (e.g. &quot; 8&quot;) </p>
<dt>%T</p>
<dd>time of day (e.g. &quot;13:17:11&quot;) </p>
<dt>%B</p>
<dd>B-channel (0 or 1) </p>
<dt>%k</p>
<dd>Number of isdn card. </p>
<dt>%( %/ %)</p>
<dd>If the number of the remote side is known: this char, i.e. the (, /, or ) that comes after the %. If the number if not known, a blank is substituted. </p>
</dl>
<h2>Example</h2>
<pre>[GLOBAL]
COUNTRYPREFIX=+
AREAPREFIX=0
COUNTRYCODE=49 # Germany
AREACODE=0721 # Karlsruhe
[VARIABLES]
[ISDNLOG]
VBN = 010
VBNLEN = 2:3
PRESELECTED = 33
LOGFILE = /var/log/isdn.log
ILABEL = %b %e %T %ICall to tei %t from %N2 on %n2
OLABEL = %b %e %T %Itei %t calling %N2 with %n2
REPFMTWWW = &quot;%X %D %17.17H %T %-17.17F %-20.20l SI: %S %9u %U %I %O&quot;
REPFMTSHORT = &quot;%X%D %8.8H %T %-14.14F%U%I %O&quot;
REPFMT = &quot; %X %D %15.15H %T %-15.15F %7u %U %I %O&quot;
CHARGEMAX = 50.00
CURRENCY = 0.12,DEM
COUNTRYFILE = /usr/share/isdn/country.dat
RATECONF= /etc/isdn/rate.conf
RATEFILE= /usr/share/isdn/rate-de.dat
HOLIDAYS= /usr/share/isdn/holiday-de.dat
ZONEFILE= /usr/share/isdn/zone-de-%s.cdb
DESTFILE= /usr/share/isdn/dest.cdb</pre>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/isdn.conf</code></p>
<dd>This file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8) <a href="/docs/linux/man/5-callerid-conf/">callerid.conf</a>(5) <a href="/docs/linux/man/5-rate-files/">rate-files</a>(5) <a href="/docs/linux/man/1-isdnrep/">isdnrep</a>(1)</code><br />
 <code><a href="/docs/linux/man/5-isdnformat/">isdnformat</a>(5)</code> and samples/isdn.conf.* </p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux. Now maintained by Paul Slootman &lt;paul [at] isdn4linux.de&gt;, updated by Leopold Toetsch &lt;lt [at] toetsch.at&gt;.</p>
