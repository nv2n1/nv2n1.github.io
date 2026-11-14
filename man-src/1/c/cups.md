---
title: "cups(1)"
name: "cups"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cups/"
description: "cups – a standards-based, open source printing system"
---

<h2 class="name">NAME</h2>
<p> cups &#8211; a standards-based, open source printing system </p>
<h2>DESCRIPTION</h2>
<p> <code>CUPS</code> is the software you use to print from applications like word processors, email readers, photo editors, and web browsers. It converts the page descriptions produced by your application (put a paragraph here, draw a line there, and so forth) into something your printer can understand and then sends the information to the printer for printing. </p>
<p> Now, since every printer manufacturer does things differently, printing can be very complicated. <code>CUPS</code> does its best to hide this from you and your application so that you can concentrate on printing and less on how to print. Generally, the only time you need to know anything about your printer is when you use it for the first time, and even then <code>CUPS</code> can often figure things out on its own.</p>
<h3>HOW DOES IT WORK?</h3>
<p> The first time you print to a printer, <code>CUPS</code> creates a queue to keep track of the current status of the printer (everything OK, out of paper, etc.) and any pages you have printed. Most of the time the queue points to a printer connected directly to your computer via a USB port, however it can also point to a printer on your network, a printer on the Internet, or multiple printers depending on the configuration. Regardless of where the queue points, it will look like any other printer to you and your applications. </p>
<p> Every time you print something, <code>CUPS</code> creates a job which contains the queue you are sending the print to, the name of the document you are printing, and the page descriptions. Job are numbered (queue-1, queue-2, and so forth) so you can monitor the job as it is printed or cancel it if you see a mistake. When <code>CUPS</code> gets a job for printing, it determines the best programs (filters, printer drivers, port monitors, and backends) to convert the pages into a printable format and then runs them to actually print the job. </p>
<p> When the print job is completely printed, <code>CUPS</code> removes the job from the queue and moves on to any other jobs you have submitted. You can also be notified when the job is finished, or if there are any errors during printing, in several different ways.</p>
<h3>WHERE DO I BEGIN?</h3>
<p> The easiest way to start is by using the web interface to configure your printer. Go to &quot;<a rel="nofollow" href="http://localhost:631">http://localhost:631</a>&quot; and choose the Administration tab at the top of the page. Click/press on the Add Printer button and follow the prompts. </p>
<p> When you are asked for a username and password, enter your login username and password or the &quot;root&quot; username and password. </p>
<p> After the printer is added you will be asked to set the default printer options (paper size, output mode, etc.) for the printer. Make any changes as needed and then click/press on the Set Default Options button to save them. Some printers also support auto-configuration &#8211; click/press on the Query Printer for Default Options button to update the options automatically. </p>
<p> Once you have added the printer, you can print to it from any application. You can also choose Print Test Page from the maintenance menu to print a simple test page and verify that everything is working properly. </p>
<p> You can also use the <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8) and <code><a href="/docs/linux/man/8-lpinfo/">lpinfo</a></code>(8) commands to add printers to <code>CUPS</code>. Additionally, your operating system may include graphical user interfaces or automatically create printer queues when you connect a printer to your computer.</p>
<h3>HOW DO I GET HELP?</h3>
<p> The <code>OpenPrinting CUPS</code> web site (<a rel="nofollow" href="https://openprinting.github.io/cups)">https://openprinting.github.io/cups)</a> provides access to the <i>cups</i> and <i>cups-devel</i> mailing lists, additional documentation and resources, and a bug report database. Most vendors also provide online discussion forums to ask printing questions for your operating system of choice.</p>
<h2>ENVIRONMENT</h2>
<p> <code>CUPS</code> commands use the following environment variables to override the default locations of files and so forth. For security reasons, these environment variables are ignored for setuid programs:</p>
<dl>
<dt><code>CUPS_ANYROOT</code></p>
<dd> Whether to allow any X.509 certificate root (Y or N).</p>
<dt><code>CUPS_CACHEDIR</code></p>
<dd> The directory where semi-persistent cache files can be found.</p>
<dt><code>CUPS_DATADIR</code></p>
<dd> The directory where data files can be found.</p>
<dt><code>CUPS_ENCRYPTION</code></p>
<dd> The default level of encryption (Always, IfRequested, Never, Required).</p>
<dt><code>CUPS_EXPIREDCERTS</code></p>
<dd> Whether to allow expired X.509 certificates (Y or N).</p>
<dt><code>CUPS_GSSSERVICENAME</code></p>
<dd> The Kerberos service name used for authentication.</p>
<dt><code>CUPS_SERVER</code></p>
<dd> The hostname/IP address and port number of the CUPS scheduler (hostname:port or ipaddress:port).</p>
<dt><code>CUPS_SERVERBIN</code></p>
<dd> The directory where server helper programs, filters, backend, etc. can be found.</p>
<dt><code>CUPS_SERVERROOT</code></p>
<dd> The root directory of the server.</p>
<dt><code>CUPS_STATEDIR</code></p>
<dd> The directory where state files can be found.</p>
<dt><code>CUPS_USER</code></p>
<dd> Specifies the name of the user for print requests.</p>
<dt><code>HOME</code></p>
<dd> Specifies the home directory of the current user.</p>
<dt><code>IPP_PORT</code></p>
<dd> Specifies the default port number for IPP requests.</p>
<dt><code>LOCALEDIR</code></p>
<dd> Specifies the location of localization files.</p>
<dt><code>LPDEST</code></p>
<dd> Specifies the default print queue (System V standard).</p>
<dt><code>PRINTER</code></p>
<dd> Specifies the default print queue (Berkeley standard).</p>
<dt><code>TMPDIR</code></p>
<dd> Specifies the location of temporary files.</dl>
<h2>FILES</h2>
<pre>
<i>~/.cups/client.conf</i>
<i>~/.cups/lpoptions</i>
</pre>
<h2>CONFORMING TO</h2>
<p> <code>CUPS</code> conforms to the Internet Printing Protocol version 2.1 and implements the Berkeley and System V UNIX print commands.</p>
<h2>NOTES</h2>
<p> CUPS printer drivers, backends, and PPD files are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/5-client-conf/">client.conf</a></code>(5), <code><a href="/docs/linux/man/8-cupsctl/">cupsctl</a></code>(8), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8), <code><a href="/docs/linux/man/8-lpinfo/">lpinfo</a></code>(8), <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-lprm/">lprm</a></code>(1), <code><a href="/docs/linux/man/1-lpq/">lpq</a></code>(1), <code><a href="/docs/linux/man/1-lpstat/">lpstat</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a>), OpenPrinting CUPS Web Site (<a rel="nofollow" href="https://openprinting.github.io/cups">https://openprinting.github.io/cups</a>), PWG Internet Printing Protocol Workgroup (<a rel="nofollow" href="http://www.pwg.org/ipp)">http://www.pwg.org/ipp)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
