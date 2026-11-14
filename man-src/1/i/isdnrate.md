---
title: "isdnrate(1)"
name: "isdnrate"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isdnrate/"
description: "isdnrate – Print telephone rates and various info from rate-files(5)."
---

<h2>NAME</h2>
<p> isdnrate &#8211; Print telephone rates and various info from <a href="/docs/linux/man/5-rate-files/">rate-files</a>(5).</p>
<h2>SYNOPSIS</h2>
<p> <code>isdnrate -a -b</code><i>best</i><code> -d</code><i>day</i><code> -f</code><i>from</i><code> -h</code><i>hour</i><code> -l</code><i>len</i> <code>-o</code> <code>-p</code><i>provs</i><code> -r</code> <i></i>v<i>NN</i> <code>-s</code> <code>-t</code><i>takt</i><code> -v</code><i>verbose</i><code> -x</code><i>exclude</i> <code> -C -D</code><i>det</i><code> -G</code><i>data</i><code> -H -L -N -O</code><i>socketfile</i><code> -P</code><i>piddir</i> <code> -S</code><i>sort</i><code> -T -U -V -X</code><i>explain</i> <code>-Z</code> <code>NUMBER &#8230;</code> </p>
<p> All options are optional.</p>
<h2>DESCRIPTION</h2>
<p> The <code>isdnrate</code> program prints various information from <a href="/docs/linux/man/5-rate-files/">rate-files</a>(5). Its main purpose is the calculation of telephone rates from your location to an arbitrary destination at a certain time and of a certain length for all the providers in a rate-file. </p>
<h3><code>NUMBER</code></h3>
<p> A telephone number may be</p>
<dl>
<dt>
<dd> <code>1234</code> a local area number</p>
<dt>
<dd> <code>01234</code> a different area in your country</p>
<dt>
<dd> <code>+12345</code> a foreign country</p>
<dt>
<dd> <code>China</code> text for a foreign country</p>
<dt>
<dd> <code>Paris</code> a town</p>
<dt>
<dd> <code>US</code> a code as defined in <i>country.dat</i>.</p>
<dt>
<dd> <code>Internet</code> a Service name (if option <code>-s</code> is also given).</dl>
<p> Note that currently only city names in AT, DE and NL are supported plus some international capitals.<br />
 Note also, spaces in country- or service names may be given as underscores.</p>
<h3><code>OPTIONS</code></h3>
<p> <code>-a</code> Show old and newer rates. Default actual only. </p>
<p> <code>-b</code><i>best</i> Print only <i>best</i> providers. Default is all. </p>
<p> <code>-c</code><i>rateconf</i> Use <i>rateconf</i> as provider selection file and ignore setting in <i>isdn.conf</i>. </p>
<p> <code>-d</code><i>day</i> Calc rates for <i>day</i>. <i>day</i> can be one of</p>
<dl>
<dt>
<dd> <i>dd</i> day of current month<br />
 <i>dd.mm</i> day month<br />
 <i>dd.mm.yy</i>[<i>yy</i>] day, month, year<br />
 <i>W</i> Weekday<br />
 <i>N</i> Weekday &#8211; night<br />
 <i>E</i> Weekend</dl>
<p> Default is now. </p>
<p> <code>-f</code><i>from</i> Callers location. Default is from <i>isdn.conf</i>. </p>
<p> <code>-h</code><i>hour</i> Time <i>hh</i>[<i>:mm</i>[<i>:ss</i>]] of call. Default is now. </p>
<p> <code>-i</code><i>ratefile</i> Use <i>ratefile</i> (usually rate-CC.dat) as source for telephone fees and ignore setting in <i>isdn.conf</i>. </p>
<p> <code>-l</code><i>len</i> Length of call in seconds. Default is 153 seconds. </p>
<p> <code>-o</code> Show only booked providers. These are providers, which are listed in <i>rate.conf</i>. </p>
<p> <i></i><code>-p</code> provider[<i>,provider&#8230;</i>] Print only info for given <i>provider</i>(s). <i>provider</i> is the provider number, without the leading VBN, or <i>provider_variant</i> if there are more variations, or <i>B</i> for business providers. </p>
<p> <code>-r</code>v<i>NN</i> Show only providers whose VBN begins with <i>NN</i>. The VBN is also known as provider prefix consisting of VBN and provider number. </p>
<p> <code>-s</code> Consider <code>NUMBER</code> as the name of a service and print all numbers / providers, which supply this service. </p>
<p> <code>-t</code><i>takt</i> Print only providers, which have calculation impulses smaller or equal to <i>takt</i>. Default is 9999. </p>
<p> <code>-v</code><i>verbose</i> Set <i>verbose</i> level. </p>
<p> <i></i><code>-x</code> provider[<i>,provider&#8230;</i>] Exclude these <i>provider</i>(s). </p>
<h3><code>DISPLAY AND RUN OPTIONS</code></h3>
<p> <code>-C</code> Connect to a running isdnrate daemon. This avoids long start-up times. </p>
<p> <code>-D</code> Start as a daemon, waiting for connections from a client. The socket <i>/tmp/isdnrate</i> is created, which clients can connect to. </p>
<p> <code>-D2</code> Start as a daemon and go background. </p>
<p> <code>-CD3</code> Stop a running daemon. </p>
<p> <code>-G</code><i>n</i> Print raw data for connection. <i>n</i> may be currently 97,98,99. </p>
<p> <code>-H</code> Print a header. </p>
<p> <code>-L</code> Print a semicolon separated list of</p>
<dl>
<dt>
<dd> vbn ; providername ; zone ; day ; time ; currency ; charge ; basicprice ; price ; duration ; charge/min ; takt ; minimum price</dl>
<p> <code>-N</code> Show info about following numbers. If no provider is given, the preselected provider is used. </p>
<p> <code>-O</code><i>socketfile</i> Write socket to given filename on start of daemon. Default is <i>tmp/isdnrate</i>. </p>
<p> <code>-P</code><i>piddir</i> Write own PID to <i>piddir/isdnrate.pid</i> on start of daemon. </p>
<p> <code>-S</code><i>sort</i> Sort output by <i>sort</i>, which may be</p>
<dl>
<dt>
<dd> <code>v</code> vbn or <code>n</code> provider name. Default is by charge.</dl>
<p> <code>-T</code> Print a table of charges for daytimes weekday/weekend. </p>
<p> <code>-V</code> Print version info and exit. </p>
<p> <code>-X</code><i>explain</i> Print additional information for charge or from rate-file. <i>explain</i> may be</p>
<dl>
<dt>
<dd> <code>1</code> (zone)<br />
 <code>2</code> (charge/min, zone, day, time)<br />
 <code>50</code> International areas<br />
 <code>51</code> National zones<br />
 <code>52</code> Services<br />
 <code>COMMENT</code> Print C:COMMENT: info from rate files.</dl>
<p> If <i>-s</i> is given, the number of the service is also listed with <i>-X1</i> or <i>-X2</i>. </p>
<p> <code>-Z</code> Print info for LCR<br />
 e.g. isdnrate -p1 -ZX 19430<br />
 shows the rate for provider 1 and the cheapest rate to this service. </p>
<p> Note: Various output options may not be used together. Conflicting options will produce a warning.<br />
 Note also: Sort by name or providernumber and <code>-b</code><i>best</i> will bring you the first <i>best</i> providers in sorting order, not the cheapest.<br />
 And finally: Some options like <i>-X50</i>, <i>-X51</i>, <i>-X52</i>, <i>-D</i>, <i>-V</i> don&#8217;t require a telephone <i>NUMBER</i>.</p>
<h2>FILES</h2>
<p> <i>rate-CC.dat</i>, <i>holiday-CC.dat</i>, <i>dest.gdbm</i>, <i>zone-CC-PPP.gdbm</i>, <i>isdn.conf</i>, <i>telrate.cgi</i> and more.<br />
 Note: The extension of zone- and dest data files depends on configuration. Recently <i>.cdb</i> is used.</p>
<h2>EXAMPLES</h2>
<p> <i>isdnrate -D2</i><br />
 Start the isdnrate daemon. </p>
<p> <i>isdnrate -D2 -P /var/run -O /tmp/isdnr_socket</i><br />
 Start the isdnrate daemon, write <i>isdnrate.pid</i> to /var/run and create the given socket. </p>
<p> <i>isdnrate -CH -b5 -f01 -l120 Attersee</i><br />
 Connect to running daemon, print a header and the best 5 rates from Vienna (<i>01</i>) to destination <i>Attersee</i> for a connection length of 2 Minutes. </p>
<p> <i>isdnrate -CX -p1_2,24 +1</i><br />
 Show rates and zones for destination USA for providers <i>1, 2</i> and <i>24</i>. </p>
<p> <i>isdnrate -C -l60 -rv010 HAM</i><br />
 Show rates for a one minute call to Hamburg (HAM: airport code) and use only providers whose vbn begins with 010. So provider A with vbn 01030 is displayed, provider B with vbn 0190023 is not. </p>
<p> <i>isdnrate -CX -H -dW -b5 US CA</i><br />
 Show a header, rates and zones for destinations USA and Canada for best 5 providers during workday. </p>
<p> <i>isdnrate -CHoX US</i><br />
 Show header, rate and zone for destination USA for booked providers only. </p>
<p> <i>isdnrate -CsX -l60 Internet</i><br />
 Show rates and numbers for service <i>Internet</i> for a 1 minute call. </p>
<p> <i>isdnrate -CZ 19430</i><br />
 Show rates and the best provider for this (service-)number. </p>
<p> <i>isdnrate -CD3</i><br />
 Stop the running isdnrate daemon.</p>
<h2>SIGNALS</h2>
<p> A isdnrate daemon restarts (and therefore rereads its configuration) on getting a SIGHUP signal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-rate-files/">rate-files</a>(5)</code>, <code><a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8)</code>, <code><a href="/docs/linux/man/5-isdn-conf/">isdn.conf</a>(5)</code></p>
<h2>BUGS</h2>
<p> Definitely yes. Sometimes more then one daemon can be started, sometimes the socket is not removed, when the daemon terminates. if this happens (&#8216;socket in use&#8217;), do a <i>rm /tmp/isdnrate</i> and try again.</p>
<h2>AUTHORS</h2>
<p> Andreas Kool &lt;akool [at] isdn4linux.de&gt; started this program. Leopold Toetsch &lt;lt [at] toetsch.at&gt; continued the work and brought this man page to you. Michael Reinelt &lt;reinelt [at] eunet.at&gt; did the calculation engine and various tools for it. </p>
<h2>Index</h2>
<dt><a href="#lbAH">FILES</a></p>
<dd>
<dt><a href="#lbAI">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAJ">SIGNALS</a></p>
<dd>
<dt><a href="#lbAK">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAL">BUGS</a></p>
<dd>
<dt><a href="#lbAM">AUTHORS</a></p>
<dd></dl>
