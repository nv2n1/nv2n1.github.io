---
title: "ppmtomitsu(1)"
name: "ppmtomitsu"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtomitsu/"
description: "ppmtomitsu – convert a portable pixmap to a Mitsubishi S340-10 file"
---

<h2 class="name">NAME</h2>
<p> ppmtomitsu &#8211; convert a portable pixmap to a Mitsubishi S340-10 file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtomitsu</code> [-sharpness <i>val</i>] [<code>-enlarge</code> <i>val</i>] [<code>-media</code> <i>string</i>] [<code>-copy</code> <i>val</i>] [<code>-dpi300</code>] [<code>-tiny</code>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input and converts it into a format suitable to be printed by a Mitsubishi S340-10 printer, or any other Mitsubishi color sublimation printer. </p>
<p> The Mitsubishi S340-10 Color Sublimation printer supports 24bit color. Images of the available sizes take so long to transfer that there is a fast method, employing a lookuptable, that ppmtomitsu will use if there is a maximum of 256 colors in the pixmap. ppmtomitsu will try to position your image to the center of the paper, and will rotate your image for you if xsize is larger than ysize. If your image is larger than the media allows, ppmtomitsu will quit with an error message. (We decided that the media were too expensive to have careless users produce misprints.) Once data transmission has started, the job can&#8217;t be stopped in a sane way without resetting the printer. The printer understands putting together images in the printers memory; ppmtomitsu doesn&#8217;t utilize this as pnmcat etc provide the same functionality and let you view the result on-screen, too. The S340-10 is the lowest common denominator printer; for higher resolution printers there&#8217;s the dpi300 option. The other printers also support higher values for enlarge eg, but I don&#8217;t think that&#8217;s essential enough to warrant a change in the program.</p>
<dl>
<dt><code>-sharpness</code><i> 1-4</i></p>
<dd>
&nbsp;&#8216;sharpness&#8217;&nbsp;designation. Default is to use the current sharpness.</p>
<dt><code>-enlarge</code><i> 1-3</i></p>
<dd> Enlarge by a factor; Default is 1 (no enlarge)</p>
<dt><code>-media</code><i> A, A4, AS, A4S</i></p>
<dd> Designate the media you&#8217;re using. Default is 1184 x 1350, which will fit on any media. A is 1216 x 1350, A4 is 1184 x 1452, AS is 1216 x 1650 and A4S is 1184 x 1754. A warning: If you specify a different media than the printer currently has, the printer will wait until you put in the correct media or switch it off.</p>
<dt><code>-copy</code><i> 1-9</i></p>
<dd> The number of copies to produce. Default is 1.</p>
<dt><code>-dpi300</code></p>
<dd> Double the number of allowed pixels for a S3600-30 Printer in S340-10 compatibility mode. (The S3600-30 has 300 dpi).</p>
<dt><code>-tiny</code></p>
<dd> Memory-safing, but always slow. The printer will get the data line-by-line in 24bit. It&#8217;s probably a good idea to use this if your machine starts paging a lot without this option.</dl>
<h2>REFERENCES</h2>
<p> Mitsubishi Sublimation Full Color Printer S340-10 Specifications of Parallel Interface LSP-F0232F</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ppmquant/">ppmquant</a>(1), <a href="/docs/linux/man/1-pnmscale/">pnmscale</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>BUGS</h2>
<p> We didn&#8217;t find any &#8211; yet. (Besides, they&#8217;re called features anyway :-) If you should find one, my email-adress is below.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1992, 93 by S.Petra Zeidler, MPIfR Bonn, Germany. (spz [at] specklec.mpifr-bonn.mpg.de) </p>
<h2>Index</h2>
