---
title: "vnstati(1)"
name: "vnstati"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vnstati/"
description: "vnstati – png image output support for vnStat"
---

<h2>NAME</h2>
<p> vnstati &#8211; png image output support for vnStat </p>
<h2>SYNOPSIS</h2>
<p> <code>vnstati</code> [ <code>-cdhimostv?</code> ] [ <code>&#8211;altdate</code> ] [ <code>&#8211;cache</code> <i>time</i> ] [ <code>&#8211;config</code> <i>file</i> ] [ <code>&#8211;days</code> ] [ <code>&#8211;dbdir</code> <i>directory</i> ] [ <code>&#8211;headertext</code> <i>text</i> ] [ <code>&#8211;help</code> ] [ <code>&#8211;hours</code> ] [ <code>-hs</code> ] [ <code>&#8211;hsummary</code> ] [ <code>-i</code> <i>interface</i> ] [ <code>&#8211;iface</code> <i>interface</i> ] [ <code>&#8211;locale</code> <i>locale</i> ] [ <code>&#8211;months</code> ] [ <code>-ne</code> ] [ <code>-nh</code> ] [ <code>-nl</code> ] [ <code>&#8211;noedge</code> ] [ <code>&#8211;noheader</code> ] [ <code>&#8211;nolegend</code> ] [ <code>&#8211;output</code> <i>file</i> ] [ <code>-ru</code> ] [ <code>&#8211;rateunit</code> ] [ <code>&#8211;style</code> <i>number</i> ] [ <code>&#8211;summary</code> ] [ <code>&#8211;top10</code> ] [ <code>&#8211;transparent</code> ] [ <code>&#8211;version</code> ] [ <code>-vs</code> ] [ <code>&#8211;vsummary</code> ] </p>
<h2>DESCRIPTION</h2>
<p> The purpose of <code>vnstati</code> is to provide image output support for statistics collected using <code><a href="/docs/linux/man/1-vnstat/">vnstat</a></code>(1). The image file format is limited to png. All basic outputs of vnStat are supported excluding live traffic features. The image can be outputted either to a file or to standard output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;altdate</code></p>
<dd> Use alternative date and time text location. The date and time text will be moved from the upper right header section to the lower left corner. This option will have no effect if <code>-nh, &#8211;noheader</code> has been selected. </p>
<dt><code>-c, &#8211;cache </code><i>time</i></p>
<dd> Update output file only if at least <i>time</i> minutes have passed since the previous file update. This option is ignored if stdout is used as output. </p>
<dt><code>&#8211;config </code><i>file</i></p>
<dd> Use <i>file</i> as configuration file instead of using normal configuration file search functionality. </p>
<dt><code>-d, &#8211;days</code></p>
<dd> Output traffic statistics on a daily basis for the last 30 days. </p>
<dt><code>&#8211;dbdir </code><i>directory</i></p>
<dd> Use <i>directory</i> as database directory instead of using the directory specified in the configuration file or the hardcoded default if no configuration file is available. </p>
<dt><code>&#8211;headertext </code><i>text</i></p>
<dd> Show <i>text</i> in image header section instead of automatically generated interface identification. <i>text</i> is limited to 64 characters and may not get completely shown if longer than the width of the image. Use with <code>&#8211;altdate</code> if maximal space is needed. This option will have no effect if <code>-nh, &#8211;noheader</code> has been selected. </p>
<dt><code>-h, &#8211;hours</code></p>
<dd> Output traffic statistics on a hourly basis for the last 24 hours. </p>
<dt><code>-hs, &#8211;hsummary</code></p>
<dd> Output traffic summary including hourly data using a horizontal layout. </p>
<dt><code>-i, &#8211;iface </code><i>interface</i></p>
<dd> Use <i>interface</i> instead of default or configured interface. </p>
<dt><code>&#8211;locale </code><i>locale</i></p>
<dd> Use <i>locale</i> instead of using the locale setting specified in the configuration file or the system default if no configuration file is available. </p>
<dt><code>-m, &#8211;months</code></p>
<dd> Output traffic statistics on a monthly basis for the last 12 months. </p>
<dt><code>-ne, &#8211;noedge</code></p>
<dd> Remove darker edges from around the image. </p>
<dt><code>-nh, &#8211;noheader</code></p>
<dd> Remove header containing title and update time. Time of the previous update will still be visible in the lower right corner using a less visible color. </p>
<dt><code>-nl, &#8211;nolegend</code></p>
<dd> Remove legend containing rx and tx color mapping information from the image. </p>
<dt><code>-o, &#8211;output </code><i>file</i></p>
<dd> Write png image to <i>file</i> and exit. Output can be directed to stdout by giving &quot;-&quot; as filename. </p>
<dt><code>-ru, &#8211;rateunit</code></p>
<dd> Change the configured rate unit. If rate has been configured to be shown in bytes then rate will be shown in bits if this option is present. In the same way, if rate has been configured to be shown in bits then rate will be shown in bytes when this option is present. Alternatively 0 or 1 can be given as parameter for this option in order to select between bytes (0) and bits (1) regardless of the configuration file setting. </p>
<dt><code>&#8211;style </code><i>number</i></p>
<dd> Modify the content and style of outputs. Setting <i>number</i> to 3 will show average traffic rate in all outputs where it is supported. Other values will show bar graphics instead. </p>
<dt><code>-s, &#8211;summary</code></p>
<dd> Output traffic statistics summary. </p>
<dt><code>-t, &#8211;top10</code></p>
<dd> Output all time top 10 traffic days. </p>
<dt><code>&#8211;transparent</code></p>
<dd> Toggle background color transparency depending of the TransparentBg setting in the configuration file. Alternatively 0 or 1 can be given as parameter for this option in order to either disable (0) or enable (1) transparency regardless of the configuration file setting. </p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show current version. </p>
<dt><code>-vs, &#8211;vsummary</code></p>
<dd> Output traffic summary including hourly data using a vertical layout. </p>
<dt><code>-?, &#8211;help</code></p>
<dd> Show a command option summary. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/var/lib/vnstat/</i></p>
<dd> Default database directory. Files are named according to the monitored interfaces.</p>
<dt><i>/etc/vnstat.conf</i></p>
<dd> Config file that will be used unless <i>$HOME/.vnstatrc</i> exists. See <code><a href="/docs/linux/man/5-vnstat-conf/">vnstat.conf</a></code>(5) for more information.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>vnstati -s -i eth0 -o /tmp/vnstat.png</code></p>
<dd> Output traffic summary for interface eth0 to file /tmp/vnstat.png. </p>
<dt><code>vnstati -vs -i eth0+eth1+eth2 -o /tmp/vnstat.png</code></p>
<dd> Output traffic summary with hourly data under the normal summary for a merge of interfaces eth0, eth1 and eth2 to file /tmp/vnstat.png. </p>
<dt><code>vnstati -h -c 15 -o /tmp/vnstat_h.png</code></p>
<dd> Output hourly traffic statistics for default interface to file /tmp/vnstat_h.png if the file has not been updated within the last 15 minutes. </p>
<dt><code>vnstati -d -ne -nh -o &#8211;</code></p>
<dd> Output daily traffic statistics without displaying the header section and edges for default interface to standard output (stdout). </p>
<dt><code>vnstati -m &#8211;config /home/me/vnstat.cfg -i -o &#8211;</code></p>
<dd> Output monthly traffic statistics for default interface specified in configuration file /home/me/vnstat.cfg to standard output (stdout). </p>
</dl>
<h2>RESTRICTIONS</h2>
<p> Depending on the font provided by the GD library, not all characters may end up shown correctly when a UTF-8 locale is used. </p>
<p> Using long date output formats may cause misalignment in shown columns if the length of the date exceeds the fixed size allocation. </p>
<h2>AUTHOR</h2>
<p> Teemu Toivola &lt;tst at iki dot fi&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vnstat/">vnstat</a></code>(1), <code><a href="/docs/linux/man/1-vnstatd/">vnstatd</a></code>(1), <code><a href="/docs/linux/man/5-vnstat-conf/">vnstat.conf</a></code>(5), <code><a href="/docs/linux/man/7-units/">units</a></code>(7) </p>
<h2>Index</h2>
