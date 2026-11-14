---
title: "tv_grab_huro(1)"
name: "tv_grab_huro"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_huro/"
description: "tv_grab_huro – Grab TV listings for Hungary or Romania."
---

<h2 class="name">NAME</h2>
<p> tv_grab_huro &#8211; Grab TV listings for Hungary or Romania. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_huro &#8211;help </p>
<p> tv_grab_huro [&#8211;config-file <font SIZE="-1">FILE</font>] &#8211;configure [&#8211;gui <font SIZE="-1">GUITYPE</font>] </p>
<p> tv_grab_huro [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;output <font SIZE="-1">FILE</font>] [&#8211;days N] [&#8211;offset N] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[&#8211;slow] [&#8211;get-full-description] [&#8211;max-desc-length <font SIZE="-1">LENGTH</font>]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[&#8211;icons | (&#8211;local-icons <font SIZE="-1">DIRECTORY</font> [&#8211;no-fetch-icons])]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[&#8211;gui <font SIZE="-1">GUITYPE</font>] [&#8211;quiet]</p>
<p> tv_grab_huro &#8211;list-channels &#8211;loc [hu | ro] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[&#8211;icons | (&#8211;local-icons <font SIZE="-1">DIRECTORY</font> [&#8211;no-fetch-icons])]</p>
<p> tv_grab_huro &#8211;capabilities </p>
<p> tv_grab_huro &#8211;version</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> listings for several channels available in Hungary or Romania. The grabber relies on parsing <font SIZE="-1">HTML</font> so it might stop working at any time. </p>
<p> First run <code>tv_grab_huro &#8211;configure</code> to choose, which channels you want to download. Then running <code>tv_grab_huro</code> with no arguments will output listings in <font SIZE="-1">XML</font> format to standard output. </p>
<p> <code>&#8211;configure</code> Prompt for which channels, and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_huro.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;gui </code><font SIZE="-1"><code>GUITYPE</code></font> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> Write to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> Grab N days. The default is eight. </p>
<p> <code>&#8211;offset N</code> Start N days in the future. The default is to start from today. </p>
<p> <code>&#8211;quiet</code> Suppress the progress messages normally written to standard error. </p>
<p> <code>&#8211;slow</code> Enables long strategy run: port.hu publishes only some (vital) information on the actual listing pages, the rest is shown in a separate popup window. If you&#8217;d like to parse the data from these popups as well, supply this flag. But consider that the grab process takes much longer when doing so, since many more web pages have to be retrieved. </p>
<p> <code>&#8211;get-full-description</code> This is quite like <code>&#8211;slow</code> but doesn&#8217;t always download data from popup window. Instead this is only requested if description in overview is truncated. </p>
<p> <code>&#8211;list-channels</code> Write output giving &lt;channel&gt; elements for every channel available (ignoring the config file), but no programmes. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt; </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;icons</code> and <code>&#8211;local-icons </code><font SIZE="-1"><code>DIRECTORY</code></font> get the <font SIZE="-1">URL</font> for channel-logos together with the channel-list. With <code>&#8211;icons</code> specified the logos(images) will be not fetched just their <font SIZE="-1">URL </font>(<a rel="nofollow" href="http://...)">http://&#8230;)</a> will be written in the output <font SIZE="-1">XML.</font> If called with <code>&#8211;local-icons</code>, the generated <font SIZE="-1">URL </font>(file://&#8230;) will point to the the local directory <font SIZE="-1">DIRECTORY</font> and all channel logos will be grabbed and saved under this place. Use <code>&#8211;no-fetch-icons</code> option to disable the icon fetching. Note: icon fetching currently works for Hungary and Romania only. </p>
<p> <code>&#8211;max-desc-length </code><font SIZE="-1"><code>LENGTH</code></font> can be used to maximize the lenght of the grabbed program long description. This can be usefull if you have a viewer program (using this xmltv output), which can not be display userfriendly the description if it is more then <font SIZE="-1">LENGTH</font> character. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>AUTHOR</h2>
<p> Attila Szekeres and Zsolt Varga. Based on tv_grab_fi by Matti Airas. Heavily patched and earlier maintained by Stefan siegl &lt;stesie [at] brokenpipe.de&gt;, reworked and now maintained by Balazs Molnar &lt;mbdev [at] freemail.hu&gt;.</p>
<h2>BUGS</h2>
<p> The data source does not include full channels information and the channels are identified by short names rather than the <font SIZE="-1">RFC2838</font> form recommended by the <font SIZE="-1">XMLTV DTD.</font> </p>
<h2>Index</h2>
