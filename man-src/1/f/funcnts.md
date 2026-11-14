---
title: "funcnts(1)"
name: "funcnts"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funcnts/"
description: "funcnts – count photons in specified regions, with bkgd subtraction"
---

<h2>NAME</h2>
<p> <code>funcnts &#8211; count photons in specified regions, with bkgd subtraction</code></p>
<h2>SYNOPSIS</h2>
<p> funcnts [switches] &lt;source_file&gt; [source_region] [bkgd_file] [bkgd_region|bkgd_value]</p>
<h2>OPTIONS</h2>
<pre><code>
  -e "source_exposure[;bkgd_exposure]"
#source(bkgd) FITS exposure image using matching files
  -w "source_exposure[;bkgd_exposure]"
#source(bkgd) FITS exposure image using WCS transform
  -t "source_timecorr[;bkgd_timecorr]"
#source(bkgd) time correction value or header parameter name
  -g            # output using nice g format
  -G            # output using %.14g format (maximum precision)
  -i "[column;]int1;int2..." # column-based intervals
  -m            # match individual source and bkgd regions
  -p            # output in pixels, even if wcs is present
  -r            # output inner/outer radii (and angles) for annuli (and pandas)
  -s            # output summed values
  -v "scol[;bcol]" # src and bkgd value columns for tables
  -T            # output in starbase/rdb format
  -z            # output regions with zero area
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>funcnts</code> counts photons in the specified source regions and reports the results for each region. Regions are specified using the Spatial Region Filtering mechanism. Photons are also counted in the specified bkgd regions applied to the same data file or a different data file. (Alternatively, a constant background value in counts/pixel**2 can be specified.) The bkgd regions are either paired one-to-one with source regions or pooled and normalized by area, and then subtracted from the source counts in each region. Displayed results include the bkgd-subtracted counts in each region, as well as the error on the counts, the area in each region, and the surface brightness (cnts/area**2) calculated for each region. </p>
<p> The first argument to the program specifies the <font SIZE="-1">FITS</font> input image, array, or raw event file to process. If &#8220;stdin&#8221; is specified, data are read from the standard input. Use Funtools Bracket Notation to specify <font SIZE="-1">FITS</font> extensions, image sections, and filters. </p>
<p> The optional second argument is the source region descriptor. If no region is specified, the entire field is used. </p>
<p> The background arguments can take one of two forms, depending on whether a separate background file is specified. If the source file is to be used for background as well, the third argument can be either the background region, or a constant value denoting background cnts/pixel. Alternatively, the third argument can be a background data file, in which case the fourth argument is the background region. If no third argument is specified, a constant value of 0 is used (i.e., no background). </p>
<p> In summary, the following command arguments are valid: </p>
<p>[sh] funcnts sfile #counts in source file<br />
    [sh] funcnts sfile sregion #counts in source region<br />
        [sh] funcnts sfile sregion bregion #bkgd reg.is from source file<br />
            [sh] funcnts sfile sregion bvalue #bkgd reg.is constant<br />
                [sh] funcnts sfile sregion bfile bregion #bkgd reg.is from separate file</p>
<p> <font SIZE="-1">NB:</font> unlike other Funtools programs, source and background regions are specified as separate arguments on the command line, rather than being placed inside brackets as part of the source and background filenames. This is because regions in funcnts are not simply used as data filters, but also are used to calculate areas, exposure, etc. If you put the source region inside the brackets (i.e. use it simply as a filter) rather than specifying it as argument two, the program still will only count photons that pass the region filter. However, the area calculation will be performed on the whole field, since <i>field()</i> is the default source region. This rarely is the desired behavior. On the other hand, with <font SIZE="-1">FITS</font> binary tables, it often is useful to put a column filter in the filename brackets, so that only events matching the column filter are counted inside the region. </p>
<p> For example, to extract the counts within a radius of 22 pixels from the center of the <font SIZE="-1">FITS</font> binary table snr.ev and subtract the background determined from the same image within an annulus of radii 50-100 pixels: </p>
<pre>
  [sh] funcnts snr.ev &quot;circle(502,512,22)&quot; &quot;annulus(502,512,50,100)&quot;
  # source
  #   data file:        snr.ev
  #   degrees/pix:      0.00222222
  # background
  #   data file:        snr.ev
  # column units
  #   area:             arcsec**2
  #   surf_bri:         cnts/arcsec**2
  #   surf_err:         cnts/arcsec**2
</pre>
<p>#background &#8211; subtracted results<br />
reg net_counts error background berror area surf_bri surf_err&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -1 3826.403 66.465 555.597 5.972 96831.98 0.040 0.001</p>
<p>#the following source and background components were used:<br />
source region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;circle(502, 512, 22)</p>
<p>reg counts pixels&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 4382.000 1513</p>
<p>background region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;annulus(502, 512, 50, 100)</p>
<p>reg counts pixels&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -all 8656.000 23572</p>
<p> The area units for the output columns labeled &#8220;area&#8221;, &#8220;surf_bri&#8221; (surface brightness) and &#8220;surf_err&#8221; will be given either in arc-seconds (if appropriate <font SIZE="-1">WCS</font> information is in the data file header(s)) or in pixels. If the data file has <font SIZE="-1">WCS</font> info, but you do not want arc-second units, use the <code>-p</code> switch to force output in pixels. Also, regions having zero area are not normally included in the primary (background-subtracted) table, but are included in the secondary source and bkgd tables. If you want these regions to be included in the primary table, use the <code>-z</code> switch. </p>
<p> Note that a simple sed command will extract the background-subtracted results for further analysis: </p>
<p>[sh] cat funcnts.sed 1, / &#8212; &#8212; .*/ d / ^$ /, $d</p>
<pre>
  [sh] sed -f funcnts.sed funcnts.out
  1     3826.403    66.465      555.597     5.972  96831.98     0.040     0.001
</pre>
<p> If separate source and background files are specified, <code>funcnts</code> will attempt to normalize the the background area so that the background pixel size is the same as the source pixel size. This normalization can only take place if the appropriate <font SIZE="-1">WCS</font> information is contained in both files (e.g. degrees/pixel values in <font SIZE="-1">CDELT</font>). If either file does not contain the requisite size information, the normalization is not performed. In this case, it is the user&#8217;s responsibility to ensure that the pixel sizes are the same for the two files. </p>
<p> Normally, if more than one background region is specified, <code>funcnts</code> will combine them all into a single region and use this background region to produce the background-subtracted results for each source region. The <code>-m</code> (match multiple backgrounds) switch tells <code>funcnts</code> to make a one to one correspondence between background and source regions, instead of using a single combined background region. For example, the default case is to combine 2 background regions into a single region and then apply that region to each of the source regions: </p>
<pre>
  [sh] funcnts snr.ev &quot;annulus(502,512,0,22,n=2)&quot; &quot;annulus(502,512,50,100,n=2)&quot;
  # source
  #   data file:        snr.ev
  #   degrees/pix:      0.00222222
  # background
  #   data file:        snr.ev
  # column units
  #   area:             arcsec**2
  #   surf_bri:         cnts/arcsec**2
  #   surf_err:         cnts/arcsec**2
</pre>
<p>#background &#8211; subtracted results<br />
reg net_counts error background berror area surf_bri surf_err&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -1 3101.029 56.922 136.971 1.472 23872.00 0.130 0.002 2 725.375 34.121 418.625 4.500 72959.99 0.010 0.000</p>
<p>#the following source and background components were used:<br />
source region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;annulus(502, 512, 0, 22, n = 2)</p>
<p>reg counts pixels&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 3238.000 373 2 1144.000 1140</p>
<p>background region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;annulus(502, 512, 50, 100, n = 2)</p>
<p>reg counts pixels&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -all 8656.000 23572</p>
<p> Note that the basic region filter rule &#8220;each photon is counted once and no photon is counted more than once&#8221; still applies when using The <code>-m</code> to match background regions. That is, if two background regions overlap, the overlapping pixels will be counted in only one of them. In a worst-case scenario, if two background regions are the same region, the first will get all the counts and area and the second will get none. </p>
<p> Using the <code>-m</code> switch causes <code>funcnts</code> to use each of the two background regions independently with each of the two source regions: </p>
<pre>
  [sh] funcnts -m snr.ev &quot;annulus(502,512,0,22,n=2)&quot; &quot;ann(502,512,50,100,n=2)&quot;
  # source
  #   data file:        snr.ev
  #   degrees/pix:      0.00222222
  # background
  #   data file:        snr.ev
  # column units
  #   area:             arcsec**2
  #   surf_bri:         cnts/arcsec**2
  #   surf_err:         cnts/arcsec**2
</pre>
<p>#background &#8211; subtracted results<br />
reg net_counts error background berror area surf_bri surf_err&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -1 3087.015 56.954 150.985 2.395 23872.00 0.129 0.002 2 755.959 34.295 388.041 5.672 72959.99 0.010 0.000</p>
<p>#the following source and background components were used:<br />
source region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;annulus(502, 512, 0, 22, n = 2)</p>
<p>reg counts pixels&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 3238.000 373 2 1144.000 1140</p>
<p>background region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;ann(502, 512, 50, 100, n = 2)</p>
<p>reg counts pixels&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 3975.000 9820 2 4681.000 13752</p>
<p> Note that most floating point quantities are displayed using &#8220;f&#8221; format. You can change this to &#8220;g&#8221; format using the <code>-g</code> switch. This can be useful when the counts in each pixel is very small or very large. If you want maximum precision and don&#8217;t care about the columns lining up nicely, use <code>-G</code>, which outputs all floating values as %.14g. </p>
<p> When counting photons using the annulus and panda (pie and annuli) shapes, it often is useful to have access to the radii (and panda angles) for each separate region. The <code>-r</code> switch will add radii and angle columns to the output table: </p>
<pre>
  [sh] funcnts -r snr.ev &quot;annulus(502,512,0,22,n=2)&quot; &quot;ann(502,512,50,100,n=2)&quot;
  # source
  #   data file:        snr.ev
  #   degrees/pix:      0.00222222
  # background
  #   data file:        snr.ev
  # column units
  #   area:             arcsec**2
  #   surf_bri:         cnts/arcsec**2
  #   surf_err:         cnts/arcsec**2
  #   radii:            arcsecs
  #   angles:           degrees
</pre>
<p>#background &#8211; subtracted results<br />
reg net_counts error background berror area surf_bri surf_err radius1 radius2 angle1 angle2&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -1 3101.029 56.922 136.971 1.472 23872.00 0.130 0.002 0.00 88.00 NA NA 2 725.375 34.121 418.625 4.500 72959.99 0.010 0.000 88.00 176.00 NA NA</p>
<p>#the following source and background components were used:<br />
source region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;annulus(502, 512, 0, 22, n = 2)</p>
<p>reg counts pixels&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 3238.000 373 2 1144.000 1140</p>
<p>background region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;ann(502, 512, 50, 100, n = 2)</p>
<p>reg counts pixels&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -all 8656.000 23572</p>
<p> Radii are given in units of pixels or arc-seconds (depending on the presence of <font SIZE="-1">WCS</font> info), while the angle values (when present) are in degrees. These columns can be used to plot radial profiles. For example, the script <code>funcnts.plot</code> in the funtools distribution) will plot a radial profile using gnuplot (version 3.7 or above). A simplified version of this script is shown below: </p>
<pre>
  #!/bin/sh
</pre>
<p>if<br />
    [x &#8220;$1&#8221; = xgnuplot];<br />
then if[x`which gnuplot 2 &gt; / dev / null` = x];<br />
then<br />
    echo &#8220;ERROR: gnuplot not available&#8221; exit 1 fi<br />
        awk &#8216; BEGIN<br />
{<br />
    HEADER = 1;<br />
    DATA = 0;<br />
    FILES = &#8220;&#8221;;<br />
    XLABEL = &#8220;unknown&#8221;;<br />
    YLABEL = &#8220;unknown&#8221;<br />
}<br />
HEADER == 1<br />
{<br />
    if ($1 == &#8220;#&#8221; &amp;&amp; $2 == &#8220;data&#8221; &amp;&amp; $3 == &#8220;file:&#8221;) {<br />
        if (FILES != &#8220;&#8221;)<br />
            FILES = FILES &#8220;,&#8221; FILES = FILES $4<br />
    } else if ($1 == &#8220;#&#8221; &amp;&amp; $2 == &#8220;radii:&#8221;) {<br />
        XLABEL = $3<br />
    } else if ($1 == &#8220;#&#8221; &amp;&amp; $2 == &#8220;surf_bri:&#8221;) {<br />
        YLABEL = $3<br />
    } else if ($1 == &#8220;&#8212;-&#8220;) {<br />
        printf &#8220;set nokey; set title \&#8221;funcnts(%s)\&#8221;
&#8221;, FILES printf &#8220;set xlabel \&#8221; radius(%s)\&#8221;
&#8221;, XLABEL printf &#8220;set ylabel \&#8221;surf_bri(%s)\&#8221;
&#8221;, YLABEL print &#8220;plot \&#8221;-\&#8221; using 3:4:6:7:8 with boxerrorbars&#8221; HEADER = 0 DATA = 1 next<br />
    }<br />
}<br />
DATA == 1<br />
{<br />
    if (NF == 12) {<br />
        print $9, $10, ($9 + $10) / 2, $7, $8, $7 &#8211; $8, $7 + $8, $10 &#8211; $9<br />
    } else {<br />
        exit<br />
    }<br />
}<br />
&#8216; | gnuplot -persist &#8211; 1&gt;/dev/null 2&gt;&amp;1</p>
<p>elif[x &#8220;$1&#8221; = xds9];<br />
then<br />
    awk &#8216; BEGIN<br />
{<br />
    HEADER = 1;<br />
    DATA = 0;<br />
    XLABEL = &#8220;unknown&#8221;;<br />
    YLABEL = &#8220;unknown&#8221;<br />
}<br />
HEADER == 1<br />
{<br />
    if ($1 == &#8220;#&#8221; &amp;&amp; $2 == &#8220;data&#8221; &amp;&amp; $3 == &#8220;file:&#8221;) {<br />
        if (FILES != &#8220;&#8221;)<br />
            FILES = FILES &#8220;,&#8221; FILES = FILES $4<br />
    } else if ($1 == &#8220;#&#8221; &amp;&amp; $2 == &#8220;radii:&#8221;) {<br />
        XLABEL = $3<br />
    } else if ($1 == &#8220;#&#8221; &amp;&amp; $2 == &#8220;surf_bri:&#8221;) {<br />
        YLABEL = $3<br />
    } else if ($1 == &#8220;&#8212;-&#8220;) {<br />
        printf &#8220;funcnts(%s) radius(%s) surf_bri(%s) 3
&#8221;, FILES, XLABEL, YLABEL HEADER = 0 DATA = 1 next<br />
    }<br />
}<br />
DATA == 1<br />
{<br />
    if (NF == 12) {<br />
        print $9, $7, $8<br />
    } else {<br />
        exit<br />
    }<br />
}<br />
&#8216; else echo &#8220;funcnts -r &#8230; | funcnts.plot [ds9|gnuplot]&#8221; exit 1 fi</p>
<p> Thus, to run <code>funcnts</code> and plot the results using gnuplot (version 3.7 or above), use: </p>
<pre>
  funcnts -r snr.ev &quot;annulus(502,512,0,50,n=5)&quot; ...  | funcnts.plot gnuplot
</pre>
<p> The <code>-s</code> (sum) switch causes <code>funcnts</code> to produce an additional table of summed (integrated) background subtracted values, along with the default table of individual values: </p>
<pre>
  [sh] funcnts -s snr.ev &quot;annulus(502,512,0,50,n=5)&quot; &quot;annulus(502,512,50,100)&quot;
  # source
  #   data file:        snr.ev
  #   degrees/pix:      0.00222222
  # background
  #   data file:        snr.ev
  # column units
  #   area:             arcsec**2
  #   surf_bri:         cnts/arcsec**2
  #   surf_err:         cnts/arcsec**2
</pre>
<p>#summed background &#8211; subtracted results<br />
upto net_counts error background berror area surf_bri surf_err&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -1 2880.999 54.722 112.001 1.204 19520.00 0.148 0.003 2 3776.817 65.254 457.183 4.914 79679.98 0.047 0.001 3 4025.492 71.972 1031.508 11.087 179775.96 0.022 0.000 4 4185.149 80.109 1840.851 19.786 320831.94 0.013 0.000 5 4415.540 90.790 2873.460 30.885 500799.90 0.009 0.000</p>
<p>#background &#8211; subtracted results<br />
reg counts error background berror area surf_bri surf_err&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -1 2880.999 54.722 112.001 1.204 19520.00 0.148 0.003 2 895.818 35.423 345.182 3.710 60159.99 0.015 0.001 3 248.675 29.345 574.325 6.173 100095.98 0.002 0.000 4 159.657 32.321 809.343 8.699 141055.97 0.001 0.000 5 230.390 37.231 1032.610 11.099 179967.96 0.001 0.000</p>
<p>#the following source and background components were used:<br />
source region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;annulus(502, 512, 0, 50, n = 5)</p>
<p>reg counts pixels sumcnts sumpix&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 2993.000 305 2993.000 305 2 1241.000 940 4234.000 1245 3 823.000 1564 5057.000 2809 4 969.000 2204 6026.000 5013 5 1263.000 2812 7289.000 7825</p>
<p>background region(s)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;annulus(502, 512, 50, 100)</p>
<p>reg counts pixels&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -all 8656.000 23572</p>
<p> The <code>-t</code> and <code>-e</code> switches can be used to apply timing and exposure corrections, respectively, to the data. Please note that these corrections are meant to be used qualitatively, since application of more accurate correction factors is a complex and mission-dependent effort. The algorithm for applying these simple corrections is as follows: </p>
<pre>
  C =  Raw Counts in Source Region
  Ac=  Area of Source Region
  Tc=  Exposure time for Source Data
  Ec=  Average exposure in Source Region, from exposure map
</pre>
<pre>
  B=   Raw Counts in Background Region
  Ab=  Area of Background Region
  Tb=  (Exposure) time for Background Data
  Eb=  Average exposure in Background Region, from exposure map
</pre>
<p> Then, Net Counts in Source region is </p>
<pre>
  Net=  C - B * (Ac*Tc*Ec)/(Ab*Tb*Eb)
</pre>
<p> with the standard propagation of errors for the Error on Net. The net rate would then be </p>
<pre>
  Net Rate = Net/(Ac*Tc*Ec)
</pre>
<p> The average exposure in each region is calculated by summing up the pixel values in the exposure map for the given region and then dividing by the number of pixels in that region. Exposure maps often are generated at a block factor &gt; 1 (e.g., block 4 means that each exposure pixel contains 4&#215;4 pixels at full resolution) and <code>funcnts</code> will deal with the blocking automatically. Using the <code>-e</code> switch, you can supply both source and background exposure files (separated by &#8220;;&#8221;), if you have separate source and background data files. If you do not supply a background exposure file to go with a separate background data file, <code>funcnts</code> assumes that exposure already has been applied to the background data file. In addition, it assumes that the error on the pixels in the background data file is zero. </p>
<p> <font SIZE="-1">NB:</font> The <code>-e</code> switch assumes that the exposure map overlays the image file <code>exactly</code>, except for the block factor. Each pixel in the image is scaled by the block factor to access the corresponding pixel in the exposure map. If your exposure map does not line up exactly with the image, <code>do not use</code> the <code>-e</code> exposure correction. In this case, it still is possible to perform exposure correction <code>if</code> both the image and the exposure map have valid <font SIZE="-1">WCS</font> information: use the <code>-w</code> switch so that the transformation from image pixel to exposure pixel uses the <font SIZE="-1">WCS</font> information. That is, each pixel in the image region will be transformed first from image coordinates to sky coordinates, then from sky coordinates to exposure coordinates. Please note that using <code>-w</code> can increase the time required to process the exposure correction considerably. </p>
<p> A time correction can be applied to both source and background data using the <code>-t</code> switch. The value for the correction can either be a numeric constant or the name of a header parameter in the source (or background) file: </p>
<p>  [sh] funcnts -t 23.4 &#8230;            # number for source<br />
  [sh] funcnts -t &#8220;LIVETIME;23.4&#8221; &#8230; # param for source, numeric for bkgd</p>
<p> When a time correction is specified, it is applied to the net counts as well (see algorithm above), so that the units of surface brightness become cnts/area**2/sec. </p>
<p> The <code>-i</code> (interval) switch is used to run <code>funcnts</code> on multiple column-based intervals with only a single pass through the data. It is equivalent to running <code>funcnts</code> several times with a different column filter added to the source and background data each time. For each interval, the full <code>funcnts</code> output is generated, with a linefeed character (^L) inserted between each run. In addition, the output for each interval will contain the interval specification in its header. Intervals are very useful for generating X-ray hardness ratios efficiently. Of course, they are only supported when the input data are contained in a table. </p>
<p> Two formats are supported for interval specification. The most general format is semi-colon-delimited list of filters to be used as intervals: </p>
<pre>
  funcnts -i &quot;pha=1:5;pha=6:10;pha=11:15&quot; snr.ev &quot;circle(502,512,22)&quot; ...
</pre>
<p> Conceptually, this will be equivalent to running <code>funcnts</code> three times: </p>
<p>funcnts snr.ev &#8216;[pha=1:5]&#8217; &#8220;circle(502,512,22)&#8221; funcnts snr.ev &#8216;[pha=6:10]&#8217; &#8220;circle(502,512,22)&#8221; funcnts snr.ev &#8216;[pha=11:15]&#8217; &#8220;circle(502,512,22)&#8221;</p>
<p> However, using the <code>-i</code> switch will require only one pass through the data. </p>
<p> Note that complex filters can be used to specify intervals: </p>
<pre><code>
funcnts - i "pha=1:5&amp;&amp;pi=4;pha=6:10&amp;&amp;pi=5;pha=11:15&amp;&amp;pi=6" snr.ev...
</code></pre>
<p> The program simply runs the data through each filter in turn and generates three <code>funcnts</code> outputs, separated by the line-feed character. </p>
<p> In fact, although the intent is to support intervals for hardness ratios, the specified filters do not have to be intervals at all. Nor does one &#8220;interval&#8221; filter have to be related to another. For example: </p>
<pre>
  funcnts -i &quot;pha=1:5;pi=6:10;energy=11:15&quot; snr.ev &quot;circle(502,512,22)&quot; ...
</pre>
<p> is equivalent to running <code>funcnts</code> three times with unrelated filter specifications. </p>
<p> A second interval format is supported for the simple case in which a single column is used to specify multiple homogeneous intervals for that column. In this format, a column name is specified first, followed by intervals: </p>
<pre>
  funcnts -i &quot;pha;1:5;6:10;11:15&quot; snr.ev &quot;circle(502,512,22)&quot; ...
</pre>
<p> This is equivalent to the first example, but requires less typing. The <code>funcnts</code> program will simply prepend &#8220;pha=&#8221; before each of the specified intervals. (Note that this format does not contain the &#8220;=&#8221; character in the column argument.) </p>
<p> Ordinarily, when <code>funcnts</code> is run on a <font SIZE="-1">FITS</font> binary table (or a raw event table), one integral count is accumulated for each row (event) contained within a given region. The <code>-v &#8220;scol[;bcol]&#8221;</code> (value column) switch will accumulate counts using the value from the specified column for the given event. If only a single column is specified, it is used for both the source and background regions. Two separate columns, separated by a semi-colon, can be specified for source and background. The special token &#8216;$none&#8217; can be used to specify that a value column is to be used for one but not the other. For example, &#8216;pha;$none&#8217; will use the pha column for the source but use integral counts for the background, while &#8216;$none;pha&#8217; will do the converse. If the value column is of type logical, then the value used will be 1 for T and 0 for F. Value columns are used, for example, to integrate probabilities instead of integral counts. </p>
<p> If the <code>-T</code> (rdb table) switch is used, the output will conform to starbase/rdb data base format: tabs will be inserted between columns rather than spaces and line-feed will be inserted between tables. </p>
<p> Finally, note that <code>funcnts</code> is an image program, even though it can be run directly on <font SIZE="-1">FITS</font> binary tables. This means that image filtering is applied to the rows in order to ensure that the same results are obtained regardless of whether a table or the equivalent binned image is used. Because of this, however, the number of counts found using <code>funcnts</code> can differ from the number of events found using row-filter programs such as <code>fundisp</code> or <code>funtable</code> For more information about these difference, see the discussion of Region Boundaries.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
