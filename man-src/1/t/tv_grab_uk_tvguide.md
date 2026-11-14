---
title: "tv_grab_uk_tvguide(1)"
name: "tv_grab_uk_tvguide"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_uk_tvguide/"
description: "tv_grab_uk_tvguide – Grab TV listings for UK from the TV Guide UK website."
---

<h2 class="name">NAME</h2>
<p> tv_grab_uk_tvguide &#8211; Grab TV listings for UK from the TV Guide UK website. </p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> listings in <font SIZE="-1">XMLTV</font> format for many channels available in <font SIZE="-1">UK.</font> The data come from tvguide.co.uk </p>
<p> First you must run <code>tv_grab_uk_tvguide &#8211;configure</code> to choose which channels you want to receive. </p>
<p> Then running <code>tv_grab_uk_tvguide</code> with no arguments will get a listings in <font SIZE="-1">XML</font> format for the channels you chose for available days including today.</p>
<h2>OPTIONS</h2>
<p> Please see <code>tv_grab_uk_tvguide &#8211;help</code></p>
<h2>INSTALLATION</h2>
<p> The file <i>tv_grab_uk_tvguide.map.conf</i> has two purposes. Firstly you can map the channel ids used by the site into something more meaningful to your <font SIZE="-1">PVR. E</font>.g. </p>
<pre>
      map==74==BBC 1
</pre>
<p> will change &#8220;74&#8221; to &#8220;<font SIZE="-1">BBC 1&#8221;</font> in the output <font SIZE="-1">XML.</font> </p>
<p> Note: the lines are of the form &#8220;map=={channel id}=={my name}&#8221;. </p>
<p> The second purpose is to likewise translate genre names. So if your <font SIZE="-1">PVR</font> doesn&#8220;t have a category for &#8221;Science Fiction&#8220; but uses &#8221;Sci-fi&quot; instead, then you can specify </p>
<pre>
      cat==Science Fiction==Sci-fi
</pre>
<p> and the output <font SIZE="-1">XML</font> will have &#8220;Sci-fi&#8221;. </p>
<p> <font SIZE="-1">IMPORTANT:</font> the downloaded &#8220;tv_grab_uk_tvguide.map.conf&#8221; contains example lines to illustrate the format &#8211; you should edit this file to suit your own purposes!</p>
<h2>ERROR HANDLING</h2>
<p> If the grabber fails to download data for some channel on a specific day, it will print an errormessage to <font SIZE="-1">STDERR</font> and then continue with the other channels and days. The grabber will exit with a status code of 1 to indicate that the data is incomplete.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The environment variable <font SIZE="-1">HOME</font> can be set to change where configuration files are stored. All configuration is stored in <tt>$HOME</tt>/.xmltv/. On Windows, it might be necessary to set <font SIZE="-1">HOME</font> to a path without spaces in it.</p>
<h2>SUPPORTED CHANNELS</h2>
<p> For information on supported channels, see <a rel="nofollow" href="http://tvguide.co.uk/">http://tvguide.co.uk/</a></p>
<h2>XMLTV VALIDATION</h2>
<p> <code>tv_validate_grabber</code> may report an error similar to: </p>
<pre>
      &quot;Line 5 Invalid channel-id BBC 1&quot;
</pre>
<p> This is a because ValidateFile.pm insists the channel-id adheres to <font SIZE="-1">RFC2838</font> despite the xmltv.dtd only saying &#8220;preferably&#8221; not &#8220;<font SIZE="-1">SHOULD&#8221;. </font>(Having channel ids of the form &#8220;bbc1.bbc.co.uk&#8221; will be rejected by many PVRs since they require the data to match their own list.) </p>
<p> It may also report: </p>
<pre>
      &quot;tv_sort failed on the concatenated data. Probably due to overlapping data between days.&quot;
</pre>
<p> Both these errors can be ignored.</p>
<h2>DISCLAIMER</h2>
<p> The <font SIZE="-1">TV</font> Guide website&quot;s license for these data does not allow non-personal use. </p>
<p> Certainly any commercial use of listings data obtained by using this grabber will breach copyright law, but if you are just using the data for your own personal use then you are probably fine. </p>
<p> By using this grabber you aver you are using the listings data for your own personal use only and you absolve the author(s) from any liability under copyright law or otherwise.</p>
<h2>AUTHOR</h2>
<p> Geoff Westcott. This documentation and parts of the code based on various other tv_grabbers from the XMLTV-project.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5). </p>
<h2>Index</h2>
