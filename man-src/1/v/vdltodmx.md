---
title: "vdltodmx(1)"
name: "vdltodmx"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vdltodmx/"
description: "vdltodmx – dmx configuration file parser and printer"
---

<h2>NAME</h2>
<p> vdltodmx &#8211; dmx configuration file parser and printer</p>
<h2>SYNOPSIS</h2>
<p> <code>vdltodmx</code> <i>infile</i> <i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> <i>vdltodmx</i> reads the input file, which should be in VDL configuration file format. After a successful parse, a file in Xdmx configuration file format is written to the output file. </p>
<p> The VDL file format is used with <i>xmovie</i>, which is available from <a rel="nofollow" href="http://www.llnl.gov/icc/lc/img/xmovie/xmovie.html">http://www.llnl.gov/icc/lc/img/xmovie/xmovie.html</a></p>
<h2>EXAMPLE</h2>
<p> Given the following VDL-format file:</p>
<dl>
<dt>
<dd>
<pre><code>
0 2
#
#
    2560 2048 Left two -
    thirds [restrict = *:2] 2 : 2.1 1280 2048 0 0 0 0 : 2.2 1280 2048 1280 0 0 0 4 1280 1024 0 0 1280 1024 0 1024 1280 1024 1280 0 1280 1024 1280 1024
#
    2560 2048 Right two -
    thirds [restrict = *:2] 2 : 2.2 1280 2048 0 0 0 0 : 2.3 1280 2048 1280 0 0 0 4 1280 1024 1280 0 1280 1024 1280 1024 1280 1024 2560 0 1280 1024 2560 1024
</code></pre>
</dl>
<p> the following DMX-format file will be produced:</p>
<dl>
<dt>
<dd>
<pre><code>
#
#
virtual "Left two-thirds" 2560x2048
{
display:
    2.1 1280x2048;
display:
    2.2 1280x2048 @1280x0;
}
#
virtual "Right two-thirds" 2560x2048
{
display:
    2.2 1280x2048;
display:
    2.3 1280x2048 @1280x0;
}
</code></pre>
</dl>
<h2>BUGS</h2>
<p> If the VDL file is not in the expected format, the program will probably dump core.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xdmx/">Xdmx</a>(1), <a href="/docs/linux/man/1-xdmxconfig/">xdmxconfig</a>(1), <a href="/docs/linux/man/3-vdl/">vdl</a>(3), <a href="/docs/linux/man/1-xmovie/">xmovie</a>(1) </p>
<h2>Index</h2>
