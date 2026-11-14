---
title: "pnmmercator(1)"
name: "pnmmercator"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmmercator/"
description: "pnmmercator – transform a worldmap from rectangular projection to Mercator projection and vice-versa"
---

<h2 class="name">NAME</h2>
<p> pnmmercator &#8211; transform a worldmap from rectangular projection to Mercator projection and vice-versa</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmmercator</code> [<code>-inverse</code>] [<code>-nomix</code>] [<code>-[v]verbose</code>] [<i>filename</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> The <code>pnmmercator</code> utility, converts a rectangular projection worldmap to a Mercator projection format, as used for maps.google.com and many other online maps. The map used as input for <code>pnmmercator</code> must have rows for -90 to 90 degrees latitude and columns for -180 to +180 degrees longitude. The file will typically be twice as wide as high, but this is not a requirement. The output file will be using the Mercator projection and will get double the height of the input file. </p>
<p> Maps using the Mercator projection are stretched more the closer a row is to the North or South Pole. The last few degrees (&gt; 85 or &lt; -85 degrees) are not part of a Mercator map at all because they would be stretched too much and the rows close to the edge will show banding, because they originate from the same row in the original map. </p>
<p> To overcome this, the program will by default do interpolation of pixel colors, which will eliminate the banding effect, but will cause some blurring of the output. With the -nomix option, this interpolation of colors isn&#8217;t applied. You can obtain the highest quality output by starting with an input map of high resolution, so that you can follow the <code>pnmmercator</code> transformation with a <code>pamscale</code> reduction in size. </p>
<p> This program can also convert a Mercator projection map back to a rectangular projection based. As said, the Mercator map doesn&#8217;t have information about the latitudes close to the poles. Therefore the top rows in the output image will be identical and copied from the row corresponding with latitude of 85 degrees. The same at the bottom of the map. </p>
<p> Pnmmercator doesn&#8217;t have any provision for scaling the image. You can scale by piping the output of the program through Netpbm programs such as <code>pamscale</code>. </p>
<p> You can find maps to be used as input at <code><a href="/docs/linux/man/1-flatplanet-sourceforge-net/">flatplanet.sourceforge.net</a></code>(1) </p>
<p> or uic.edu/pape . </p>
<p> The point of a Mercator projection map is that compass directions work on it. If you draw a straight line northeast from some point on the Mercator map, the line traces the course you would sail if you sailed a compass bearing of northeast from that spot. Naturally, primitive navigators appreciated that. The biggest drawback of Mercator is that areas to the north and south appear much larger than they are in real life. For example, Greenland appears to be larger than South America even though it only a ninth as large. Note that areas away from the equator are stretched north-south as well as east-west. </p>
<p> A rectangular projection is one where vertical distance is proportional to angular latitude distance of the represented area and horizontal distance is proportional to angular longitude. </p>
<h2>PARAMETERS</h2>
<p> <i>filename</i> is the name of the input file. If you don&#8217;t specify this, <code>pnmmercator</code> reads the image from standard Input. </p>
<h2>OPTIONS</h2>
<p> &lt;dl compact=&quot;compact&quot;&gt;</p>
<dl>
<dt><code>-inverse</code></p>
<dd>
<p> With this option a conversion from Mercator to degrees is applied.The output image will have half the height of the input map. </p>
<dt><code>-nomix</code></p>
<dd>
<p> Default behaviour is that color blending is applied in between two adjacent rows. If you specify the -nomix parameter there is no blending. The consequence is a banding at the top and bottom of the map. With this option, the output map will also consist of exactly the same colors as the input. </p>
<dt><code>-verbose</code> and <code>-vverbose</code></p>
<dd>
<p> This parameter outputs some additional information. If you double the &#8216;v&#8217;, it will output debug data about the lat/long degree and Mercator conversions. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1)<br />
&nbsp;<wbr>and <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-ppmglobe/">ppmglobe</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pnmmercator</code> was new in Netpbm 10.49 (December 2009). </p>
<h2>AUTHORS</h2>
<p> <i>Willem van Schaik</i> (of <code>pnmtopng</code>/<code>pngtopnm</code> fame) wrote this program in October 2009 and suggested it for inclusion in Netpbm. </p>
<h2>Index</h2>
