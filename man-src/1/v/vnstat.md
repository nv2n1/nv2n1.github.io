---
title: "vnstat(1)"
name: "vnstat"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vnstat/"
description: "vnstat – a console-based network traffic monitor"
---

<h2>NAME</h2>
<p> vnstat &#8211; a console-based network traffic monitor </p>
<h2>SYNOPSIS</h2>
<p> <code>vnstat</code> [ <code>-Ddhlmqrstuvw?</code> ] [ <code>&#8211;cleartop</code> ] [ <code>&#8211;config</code> <i>file</i> ] [ <code>&#8211;create</code> ] [ <code>&#8211;days</code> ] [ <code>&#8211;delete</code> ] [ <code>&#8211;dbdir</code> <i>directory</i> ] [ <code>&#8211;debug</code> ] [ <code>&#8211;disable</code> ] [ <code>&#8211;enable</code> ] [ <code>&#8211;exportdb</code> ] [ <code>&#8211;help</code> ] [ <code>&#8211;hours</code> ] [ <code>&#8211;importdb</code> <i>file</i> ] [ <code>-i</code> <i>interface</i> ] [ <code>&#8211;iface</code> <i>interface</i> ] [ <code>&#8211;iflist</code> ] [ <code>&#8211;json</code> <i>mode</i> ] [ <code>&#8211;live</code> <i>mode</i> ] [ <code>&#8211;locale</code> <i>locale</i> ] [ <code>&#8211;longhelp</code> ] [ <code>&#8211;months</code> ] [ <code>&#8211;nick</code> <i>nickname</i> ] [ <code>&#8211;oneline</code> ] [ <code>&#8211;query</code> ] [ <code>&#8211;rateunit</code> ] [ <code>&#8211;rebuildtotal</code> ] [ <code>&#8211;reset</code> ] [ <code>-ru</code> ] [ <code>&#8211;savemerged</code> ] [ <code>&#8211;short</code> ] [ <code>&#8211;showconfig</code> ] [ <code>&#8211;style</code> <i>number</i> ] [ <code>&#8211;sync</code> ] [ <code>&#8211;testkernel</code> ] [ <code>&#8211;top10</code> ] [ <code>-tr</code> <i>time</i> ] [ <code>&#8211;traffic</code> <i>time</i> ] [ <code>&#8211;update</code> ] [ <code>&#8211;version</code> ] [ <code>&#8211;weeks</code> ] [ <code>&#8211;xml</code> <i>mode</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>vnStat</code> is a console-based network traffic monitor. It keeps a log of hourly, daily and monthly network traffic for the selected interface(s). However, it isn&#8217;t a packet sniffer. The traffic information is read from the <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) or <code>sys</code> filesystems depending on availability. That way vnStat can be used even without root permissions on most systems. </p>
<p> The implementation is divided into two commands. The purpose of the <code>vnstat</code> command is to provide an interface for querying the traffic information stored in network interface specific databases where as the daemon <code><a href="/docs/linux/man/1-vnstatd/">vnstatd</a></code>(1) is responsible for data retrieval and storage. Although the daemon process is constantly running as a service, it is actually spending most of the time sleeping between data updates. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cleartop</code></p>
<dd> Remove all top 10 entries. </p>
<dt><code>&#8211;config </code><i>file</i></p>
<dd> Use <i>file</i> as configuration file instead of using normal configuration file search functionality. </p>
<dt><code>&#8211;create</code></p>
<dd> Create database for interface specified with <code>-i</code> or <code>&#8211;iface</code> option. </p>
<dt><code>-d, &#8211;days</code></p>
<dd> Show traffic statistics on a daily basis for the last 30 days. </p>
<dt><code>&#8211;dbdir </code><i>directory</i></p>
<dd> Use <i>directory</i> as database directory instead of using the directory specified in the configuration file or the hardcoded default if no configuration file is available. </p>
<dt><code>-D, &#8211;debug</code></p>
<dd> Show additional debug output. </p>
<dt><code>&#8211;delete</code></p>
<dd> Delete the database for the interface specified with <code>-i</code> or <code>&#8211;iface</code> and stop monitoring it. </p>
<dt><code>&#8211;enable, &#8211;disable</code></p>
<dd> Enable or disable updates for selected interface. Useful for interfaces that aren&#8217;t always available, like ppp0. If the interface goes down it should be disabled in order to avoid errors. Add something like <code>vnstat -r &#8211;disable -i ppp0</code> to the script that&#8217;s executed when the interface goes down and <code>vnstat &#8211;enable -i ppp0</code> to the up script. These two options aren&#8217;t needed when the daemon is used. </p>
<dt><code>&#8211;exportdb</code></p>
<dd> Instead of showing the database with a formatted output, this output will dump the whole database in a plain text based architeture independent format. The output can be imported back using the <code>&#8211;importdb</code> option and can be used for moving a database from one host to another. See the <code>&#8211;importdb</code> documentation below for an example. Using the output for scripting is possible but the outputs of <code>&#8211;xml</code> and <code>&#8211;json</code> are likely to be more suitable. The dump uses ; as field delimeter. </p>
<table>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>active;1</td>
<td>activity status
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interface;eth0</td>
<td>name for the interface
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nick;inet</td>
<td>nick (if given)
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>created;1023895272</td>
<td>creation date in Unix time
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>updated;1065467100</td>
<td>when the database was updated
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>totalrx;569605</td>
<td>all time total received MiB
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>totaltx;2023708</td>
<td>all time total transmitted MiB
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>currx;621673719</td>
<td>latest rx value in /proc
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>curtx;981730184</td>
<td>latest tx value in /proc
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>totalrxk;644</td>
<td>total rx KiB counter
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>totaltxk;494</td>
<td>total tx KiB counter
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>btime;1059414541</td>
<td>system boot time in Unix time
</td>
</tr>
</table>
<p> Then follows 30 lines like the following </p>
<p>d;0;1078696800;559;7433;68;557;1 </p>
<p> where d = days, 0 = day number in database (0 is today), 1077314401 date in Unix time, 559 = rx MiB, 7433 = tx MiB, 68 = rx KiB, 557 = tx KiB and 1 tells that vnStat has filled this value and it is in use. </p>
<table>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>m;0;1078092000;48649;139704;527;252;1</td>
<td>(x12)
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>t;0;1078351200;5979;47155;362;525;1</td>
<td>(x10)
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>h;0;1078699800;118265;516545</td>
<td>(x24)
</td>
</tr>
</table>
<p> m = months, t = top 10 and h = hours, all other fields are in the same order as in days except hours that doesn&#8217;t have a separate KiB value. For hours the forth and fifth fields have values in KiB. </p>
<dt><code>-h, &#8211;hours</code></p>
<dd> Show traffic statistics on a hourly basis for the last 24 hours. </p>
<dt><code>&#8211;importdb </code><i>file</i></p>
<dd> Import a database from <i>file</i> which was previously exported using the <code>&#8211;exportdb</code> option. This can be used to transfer a database between different architectures and hosts, as the database is architecture dependant and not compatible between different architectures. First dump the database on one host, e.g. with <code>vnstat -i ppp0 &#8211;exportdb &gt;ppp0db.txt</code> and then import the text file on a different host using <code>vnstat -i ppp0 &#8211;importdb ppp0db.txt</code> </p>
<dt><code>-i, &#8211;iface </code><i>interface</i></p>
<dd> Select one specific <i>interface</i> and apply actions to only it. For queries, it is possible to merge the information of two or more interfaces using the <i>interface1+interface2+&#8230;</i> syntax. </p>
<dt><code>&#8211;iflist</code></p>
<dd> Show list of currently available interfaces. </p>
<dt><code>&#8211;json </code><i>mode</i></p>
<dd> Show database content for selected interface or all interfaces in json format. All traffic values in the output are in KiB. An optional <i>mode</i> parameter can be used for limiting the output to only selected information. Everything is shown by default. Setting <i>mode</i> to &#8216;h&#8217; will output only hours, &#8216;d&#8217; days, &#8216;m&#8217; months and &#8216;t&#8217; the top 10. </p>
<dt><code>-l, &#8211;live </code><i>mode</i></p>
<dd> Display current transfer rate for the selected interface in real time until interrupted. Statistics will be shown after interruption if the runtime was more than 10 seconds. An optional <i>mode</i> parameter can be used to select between the displaying of packets per second (mode 0) and transfer counters (mode 1) during execution. <code>&#8211;style</code> can also be used to affect the layout of the output. </p>
<dt><code>&#8211;locale </code><i>locale</i></p>
<dd> Use <i>locale</i> instead of using the locale setting specified in the configuration file or the system default if no configuration file is available. </p>
<dt><code>&#8211;longhelp</code></p>
<dd> Show complete options list. </p>
<dt><code>-m, &#8211;months</code></p>
<dd> Show traffic statistics on a monthly basis for the last 12 months. </p>
<dt><code>&#8211;nick </code><i>nickname</i></p>
<dd> Set the selected interfaces <i>nickname</i> as an alias the will be displayed in queries. Usage of <code>-u</code> is required to save the change and the daemon may not be running during the set operation. </p>
<dt><code>&#8211;oneline</code></p>
<dd> Show traffic summary for selected interface using one line with a parseable format. The output contains 15 fields with ; used as field delimeter. The 1st field contains the version information of the output that will be changed in future versions of vnStat if the field structure changes. The following fields in order 2) interface name, 3) timestamp for today, 4) rx for today, 5) tx for today, 6) total for today, 7) average traffic rate for today, 8) timestamp for current month, 9) rx for current month, 10) tx for current month, 11) total for current month, 12) average traffic rate for today, 13) all time total rx, 14) all time total tx, 15) all time total traffic. </p>
<dt><code>-q, &#8211;query</code></p>
<dd> Force database query mode. </p>
<dt><code>-r, &#8211;reset</code></p>
<dd> Reset the internal counters in the database for the selected interface. Use this if the interface goes down and back up, otherwise that interface will get some extra traffic to its database. Not needed when the daemon is used. </p>
<dt><code>&#8211;rebuildtotal</code></p>
<dd> Reset the total traffic counters and recount those using recorded months. </p>
<dt><code>-ru, &#8211;rateunit</code></p>
<dd> Swap the configured rate unit. If rate has been configured to be shown in bytes then rate will be shown in bits if this option is present. In the same way, if rate has been configured to be shown in bits then rate will be shown in bytes when this option is present. Alternatively 0 or 1 can be given as parameter for this option in order to select between bytes (0) and bits (1) regardless of the configuration file setting. </p>
<dt><code>&#8211;savemerged</code></p>
<dd> Write the end result of a database merge to the file <i>mergeddb</i> that can then be used as a new database if renamed. Top 10 traffic days isn&#8217;t included in the merge and will start empty in the new database. The merge interface syntax is documented in <code>-i, &#8211;iface</code> option. </p>
<dt><code>-s, &#8211;short</code></p>
<dd> Use short output mode. This mode is also used if more than one database is available. </p>
<dt><code>&#8211;style </code><i>number</i></p>
<dd> Modify the content and style of outputs. Set <i>number</i> to 0 for a more narrow output, 1 for enabling bar column, 2 for same as previous but with average traffic rate visible in summary and weekly outputs and 3 for enabling average traffic rate in all outputs where it is supported. 4 disables the use of terminal control characters in <code>-l / &#8211;live</code> mode. </p>
<dt><code>&#8211;sync</code></p>
<dd> Synchronize internal counters in the database with interface counters for the selected interface. Use this if the system is rebooted but interface counters aren&#8217;t reseted. Such can occur when suspend to ram/disk is used. Not needed when the daemon is used. </p>
<dt><code>&#8211;testkernel</code></p>
<dd> Test if the kernel boot time information always stays the same like it should or if it&#8217;s shifting. </p>
<dt><code>-t, &#8211;top10</code></p>
<dd> Show all time top 10 traffic days. </p>
<dt><code>-tr </code><i>time</i></p>
<dd> Calculate how much traffic goes through the selected interface during the given <i>time</i> seconds. The <i>time</i> will be 5 seconds if a number parameter isn&#8217;t specified. </p>
<dt><code>-u, &#8211;update</code></p>
<dd> Update all enabled databases or only the one specified with <code>-i</code> parameter. Not supported when the daemon is running. </p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show current version. </p>
<dt><code>-w, &#8211;weeks</code></p>
<dd> Show traffic for 7 days, current and previous week. </p>
<dt><code>&#8211;xml </code><i>mode</i></p>
<dd> Show database content for selected interface or all interfaces in xml format. All traffic values in the output are in KiB. An optional <i>mode</i> parameter can be used for limiting the output to only selected information. Everything is shown by default. Setting <i>mode</i> to &#8216;h&#8217; will output only hours, &#8216;d&#8217; days, &#8216;m&#8217; months and &#8216;t&#8217; the top 10. </p>
<dt><code>-?, &#8211;help</code></p>
<dd> Show a command option summary. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/var/lib/vnstat/</i></p>
<dd> This directory contains all databases the program uses. Files are named according to the monitored interfaces. A backup copy of each database is kept in a file starting with a . (dot character) and otherwise named according to the original file. </p>
<dt><i>/etc/vnstat.conf</i></p>
<dd> Config file that will be used unless <i>$HOME/.vnstatrc</i> exists. See <code><a href="/docs/linux/man/5-vnstat-conf/">vnstat.conf</a></code>(5) for more information. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>vnstat</code></p>
<dd> Display traffic summary for the default interface or multiple interfaces when more than one is monitored. </p>
<dt><code>vnstat -i eth0+eth1+eth3</code></p>
<dd> Display traffic summary for a merge of interfaces eth0, eth1 and eth3. </p>
<dt><code>vnstat -i eth2 &#8211;xml</code></p>
<dd> Output all information about interface eth2 in xml format. </p>
<dt><code>vnstat &#8211;json</code></p>
<dd> Output all information of all monitored interfaces in json format. </p>
<dt><code>vnstat -u -i eth0</code></p>
<dd> Force a database update for interface eth0 or create the database if it doesn&#8217;t exist. This is usually the first command used after a fresh install if the daemon isn&#8217;t used. </p>
<dt><code>vnstat -u -i eth0 &#8211;nick local</code></p>
<dd> Give interface eth0 the nickname &quot;local&quot;. That information will be later later visible as a label when eth0 is queried. The database will also be updated when this command is executed or created if the database doesn&#8217;t exist. </p>
<dt><code>vnstat -i eth2 &#8211;delete</code></p>
<dd> Delete database of interface eth2 and stop monitoring it. </p>
</dl>
<h2>RESTRICTIONS</h2>
<p> Updates needs to be executed at least as often as it is possible for the interface to generate enough traffic to overflow the kernel interface traffic counter. Otherwise, it is possible that some traffic won&#8217;t be seen. This isn&#8217;t an issue for 64-bit kernels but at least one update every hour is always required in order to provide proper input. With 32-bit kernels, the maximum time between two updates depends on how fast the interface can transfer 4 GiB. Calculated theoretical times are:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>10 Mbit: 54 minutes</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>100 Mbit: 5 minutes</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>1000 Mbit: 30 seconds</td>
<td>
</td>
</tr>
</table>
</dl>
<p> However, for 1000 Mbit interfaces updating once every minute is usually a usable solution if faster updates can&#8217;t be used. </p>
<p> Estimated traffic values are likely to be somewhat inaccurate if daily traffic is low because only the MiB counter is used to calculate the estimate. </p>
<p> Virtual and aliased interfaces cannot be monitored because the kernel doesn&#8217;t provide traffic information for that type of interfaces. Such interfaces are usually named eth0:0, eth0:1, eth0:2 etc. where eth0 is the actual interface being aliased. </p>
<p> Using long date output formats may cause misalignment in shown columns if the length of the date exceeds the fixed size allocation. </p>
<h2>AUTHOR</h2>
<p> Teemu Toivola &lt;tst at iki dot fi&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vnstatd/">vnstatd</a></code>(1), <code><a href="/docs/linux/man/1-vnstati/">vnstati</a></code>(1), <code><a href="/docs/linux/man/5-vnstat-conf/">vnstat.conf</a></code>(5), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/7-units/">units</a></code>(7) </p>
<h2>Index</h2>
