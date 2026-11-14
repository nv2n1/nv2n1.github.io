---
title: "papd(8)"
name: "papd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-papd/"
description: "papd – AppleTalk print server daemon"
---

<p>papd &#8211; AppleTalk print server daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>papd</code> [-d] [-f configfile] [-p printcap]</dl>
<h2>Description</h2>
<p><code>papd</code></p>
<dd>is the AppleTalk printer daemon. This daemon accepts print jobs from AppleTalk clients (typically Macintosh computers) using the Printer Access Protocol (PAP). When used with System V printing systems, <code>papd</code> spools jobs directly into an <code><a href="/docs/linux/man/8-lpd/">lpd</a></code>(8) spool directory and wakes up <code>lpd</code> after accepting a job from the network to have it re-examine the appropriate spool directory. The actual printing and spooling is handled entirely by <code>lpd</code>. </p>
<p> <code>papd</code> can also pipe the print job to an external program for processing, and this is the preferred method on systems not using CUPS to avoid compatibility problems with all the flavours of <code>lpd</code> in use. </p>
<p> As of version 2.0, CUPS is also supported. Simply using <code>cupsautoadd</code> as first papd.conf entry will share all CUPS printers automagically using the PPD files configured in CUPS. It ist still possible to overwrite these defaults by individually define printer shares. See <code><a href="/docs/linux/man/5-papd-conf/">papd.conf</a></code>(5) for details. </p>
<p> <code>papd</code> is typically started at boot time, out of system init scripts. It first reads from its configuration file, /etc/atalk//papd.conf. The file is in the same format as /etc/printcap. See <code><a href="/docs/linux/man/5-printcap/">printcap</a></code>(5) for details. The name of the entry is registered with NBP. </p>
<p> The following options are supported: </p>
<table>
<tr VALIGN=top>
<td ALIGN=center><code> Name </code></td>
<td ALIGN=center><code> Type </code></td>
<td ALIGN=center><code> Default </code></td>
<td ALIGN=right><code> Description &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> pd </td>
<td> str </td>
<td> &#8216;.ppd&#8217; </td>
<td> Pathname to PPD file
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> pr </td>
<td> str </td>
<td> &#8216;lp&#8217; </td>
<td> LPD or CUPS printer name (or pipe to a print<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>command)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> op </td>
<td> str </td>
<td> &#8216;operator&#8217; </td>
<td> Operator name for LPD spooling
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> au </td>
<td> bool </td>
<td> false </td>
<td> Whether to do authenticated printing or not
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> ca </td>
<td> str </td>
<td> NULL </td>
<td> Pathname used for CAP-style authentification
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> sp </td>
<td> bool </td>
<td> false </td>
<td> PSSP-style authetication
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> am </td>
<td> str </td>
<td> NULL </td>
<td> UAMS to use for authentication
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> pa </td>
<td> str </td>
<td> NULL </td>
<td> Printer&#8217;s AppleTalk address
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> co </td>
<td> str </td>
<td> NULL </td>
<td> CUPS options as supplied to the <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1) command with &quot;-o&quot;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> fo </td>
<td> bool </td>
<td> false </td>
<td> adjust lineending for foomatic-rip
</td>
</tr>
</table>
<p> If no configuration file is given, the hostname of the machine is used as the NBP name and all options take their default value.</p>
<h2>Options</h2>
<p>-d</p>
<dl>
<dd>Do not fork or disassociate from the terminal. Write some debugging information to stderr.</dl>
<p> -f <i>configfile</i></p>
<dl>
<dd>Consult <i>configfile</i> instead of /etc/atalk//papd.conf for the configuration information.</dl>
<p> -p <i>printcap</i></p>
<dl>
<dd>Consult <i>printcap</i> instead of /etc/printcap for LPD configuration information.</dl>
<h2>Notes</h2>
<p>PSSP (Print Server Security Protocol) is an authentication protocol carried out through postscript printer queries to the print server. Using PSSP requires LaserWriter 8.6.1 or greater on the client mac. The user will be prompted to enter their username and password before they print. It may be necessary to re-setup the printer on each client the first time PSSP is enabled, so that the client can figure out that authentication is required to print. You can enable PSSP on a per-printer basis. PSSP is the recommended method of authenticating printers as it is more robust than CAP-style authentication, described below. CAP-style authentication gets its name from the method the CAP (Columbia APpletalk) package used to authenticate its mac clients&#8217; printing. This method requires that a user login to a file share before they print. <code>afpd</code> records the username in a temporary file named after the client&#8217;s Appletalk address, and it deletes the temporary file when the user disconnects. Therefore CAP style authentification will <i>not</i> work for clients connected to <code>afpd</code> via TCP/IP. <code>papd</code> gets the username from the file with the same Appletalk address as the machine connecting to it. CAP-style authentication will work with any mac client. If both CAP and PSSP are enabled for a particular printer, CAP will be tried first, then <code>papd</code> will fall back to PSSP. The list of UAMs to use for authentication (specified with the &#8216;am&#8217; option) applies to all printers. It is not possible to define different authentication methods on each printer. You can specify the list of UAMS multiple times, but only the last setting will be used. Currently only uams_guest.so and uams_clrtxt.so are supported as printer authentication methods. The guest method requires a valid username, but not a password. The Cleartext UAM requires both a valid username and the correct password.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 As of this writing, Mac OS X makes no use of PSSP authentication any longer. CAP-style authentication normally won&#8217;t be an option, too caused by the use of AFP over TCP these days. </p>
<h2>Files</h2>
<p>/etc/atalk//papd.conf</p>
<dl>
<dd>Default configuration file.</dl>
<p> /etc/printcap</p>
<dl>
<dd>Printer capabilities database.</dl>
<p> .ppd</p>
<dl>
<dd>PostScript Printer Description file. papd answers configuration and font queries from printing clients by consulting the configured PPD file. Such files are available for download from Adobe, Inc. (m[blue]<code><a rel="nofollow" href="http://www.adobe.com/support/downloads/main.htm">http://www.adobe.com/support/downloads/main.htm</a></code>m[]<font SIZE="-2">[1]</font>), or from the printer&#8217;s manufacturer. If no PPD file is configured, papd will return the default answer, possibly causing the client to send excessively large jobs.</dl>
<h2>Caveats</h2>
<p><code>papd</code> accepts characters with the high bit set (a full 8-bits) from the clients, but some PostScript printers (including Apple Computer&#8217;s LaserWriter family) only accept 7-bit characters on their serial interface by default. The same applies for some printers when they&#8217;re accessed via TCP/IP methods (remote LPR or socket). You will need to configure your printer to accept a full 8 bits or take special precautions and convert the printjob&#8217;s encoding (eg. by using <code>co=&quot;protocol=BCP&quot;</code> when using CUPS 1.1.19 or above). </p>
<p> When printing clients run MacOS 10.2 or above, take care that PPDs do not make use of <code>*cupsFilter:</code> comments unless the appropriate filters are installed at the client&#8217;s side, too (remember: Starting with 10.2 Apple chose to integrate CUPS into MacOS X). For in-depth information on how CUPS uses PPDs see chapter 3.4 in m[blue]<code> <a rel="nofollow" href="http://tinyurl.com/zbxn">http://tinyurl.com/zbxn</a></code>m[]<font SIZE="-2">[2]</font>).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1),<code><a href="/docs/linux/man/1-lprm/">lprm</a></code>(1),<code><a href="/docs/linux/man/5-printcap/">printcap</a></code>(5),<code><a href="/docs/linux/man/8-lpc/">lpc</a></code>(8),<code><a href="/docs/linux/man/8-lpd/">lpd</a></code>(8), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1).</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a rel="nofollow" href="http://www.adobe.com/support/downloads/main.htm">http://www.adobe.com/support/downloads/main.htm</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.adobe.com/support/downloads/main.html#Printer">http://www.adobe.com/support/downloads/main.html#Printer</a></dl>
<dt> 2.</p>
<dd><a rel="nofollow" href="http://tinyurl.com/zbxn">http://tinyurl.com/zbxn</a></p>
<dl>
<dd><a rel="nofollow" href="http://tinyurl.com/zbxn">http://tinyurl.com/zbxn</a></dl>
