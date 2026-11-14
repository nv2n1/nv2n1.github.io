---
title: "mgd77magref(1)"
name: "mgd77magref"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgd77magref/"
description: "mgd77magref – Evaluate the IGRF or CM4 magnetic field models"
---

<h2>NAME</h2>
<p> mgd77magref &#8211; Evaluate the IGRF or CM4 magnetic field models</p>
<h2>SYNOPSIS</h2>
<p> <code>mgd77magref</code> [ <i>inputfile</i> ] [ [<code>+a</code><i>alt</i><code>+t</code><i>date</i><code>+y</code>] ] [ <i>cm4file</i> ] [ <i>Dstfile</i> ] [ <i>f107file</i> ] [ <i>flags</i> ] [ ] [ <code>c</code>|<code>l</code><i>low/high</i> ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>mgd77magref</code> will evaluate the IGRF or the CM4 geomagnetic models at the specified locations and times.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>inputfile</i></p>
<dd> Contains the moments in space-time where we want to evaluate the magnetic reference field. The first two columns must contain longitude and latitude (however, see <code>-:</code> for latitude and longitude instead). Normally, the third and fourth columns must contain altitude (in km) and time, respectively, but if one or both of these are constant for all records they can be supplied via the <code>-A</code> option instead and are thus not expected in the input file. If no input file is given we read <i>stdin</i>. A note about the CM4 validity domain. The core field of CM4 is valid from 1960-2002.5 but the ionospheric and magnetospheric fields are computed after the <i>Dst</i> and <i>F10.7</i> coefficient files. We extended here those coefficient files up to 2006, which means that one can compute external contributions up until 2006 but the Secular Variation will be biased (non reliable). New indices files may be retrieved from from:<a href="ftp://ftp.ngdc.noaa.gov/STP/GEOMAGNETIC_DATA/INDICES/DST/">ftp://ftp.ngdc.noaa.gov/STP/GEOMAGNETIC_DATA/INDICES/DST/</a> (the <i>Dst</i> coefficients) and <i><a rel="nofollow" href="http://umbra.nascom.nasa.gov/sdb/yohkoh/ys_dbase/indices_flux_raw/Penticton_Absolute/monthly/MONTHPLT.ABS">http://umbra.nascom.nasa.gov/sdb/yohkoh/ys_dbase/indices_flux_raw/Penticton_Absolute/monthly/MONTHPLT.ABS</a></i> (The <i>F10.7</i> index file is a MONTHPLT.ABS). NOTE: since the <i>Dst</i> files in the &#8230;/DST/ directory are still only up to 2006, for GMT4.5.3 and after we extended the <i>Dst</i> until August 2009 by reformatting the data in the preliminary file Est_Ist_index_0_mean.pli, which is at <i><a href="ftp://ftp.ngdc.noaa.gov/STP/GEOMAGNETIC_DATA/INDICES/EST_IST/">ftp://ftp.ngdc.noaa.gov/STP/GEOMAGNETIC_DATA/INDICES/EST_IST/</a></i>. But since this site is now also outdated, we now get the DST indices from <i><a rel="nofollow" href="http://wdc.kugi.kyoto-u.ac.jp/dstae/index.html">http://wdc.kugi.kyoto-u.ac.jp/dstae/index.html</a></i> However, for the most recent dates those indices are &quot;Quick Look&quot; (the best are the &quot;Definitive&quot; type). Because the <i>F10.7</i> from the MONTHPLT.ABS file mentioned above are apparently no being updated, we found another place where they are, which is: <i><a href="ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/">ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/</a></i> solar-radio/noontime-flux/penticton/penticton_absolute/listings/ listing_drao_noontime-flux-absolute_monthly.txt</p>
<dt><code>-A</code>[<code>+a</code><i>alt</i><code>+t</code><i>date</i><code>+y</code>]</p>
<dd> Adjusts how the input record is interpreted. Append <code>+a</code> to set a fixed <i>altitude</i> (in km) that should apply to all data records [Default expects <i>altitude</i> to be in the 3rd column of all records]. Append <code>+t</code> to set a fixed <i>time</i> that should apply to all data records [Default expects <i>time</i> to be in the 4th column of all records]. Finally, append <code>+y</code> to indicate that all times are specified as decimal years [Default is ISO <i>date</i>T<i>colck</i> format, see <i>TIME_EPOCH</i>].</p>
<dt><code>-C</code><i>cm4file</i></p>
<dd> Specify an alternate CM4 coefficient file [umdl.CM4].</p>
<dt><code>-D</code><i>Dstfile</i></p>
<dd> Specify an alternate file with hourly means of the Dst index for CM4 [Dst_all.wdc]. Alternatively, simply specify a single index to apply for all records.</p>
<dt><code>-E</code><i>f107file</i></p>
<dd> Specify an alternate file with monthly means of absolute F10.7 solar radio flux for CM4 [F107_mon.plt]. Alternatively, simply specify a single flux to apply for all records.</p>
<dt><code>-F</code><i>flags</i></p>
<dd> Selects output items; <i>flags</i> is a string made up of one or more of these characters: </p>
<p> <code>r</code> means output all input columns before adding the items below </p>
<p> <code>t</code> means list total field (nT). </p>
<p> <code>h</code> means list horizontal field (nT). </p>
<p> <code>x</code> means list X component (nT, positive north). </p>
<p> <code>y</code> means list Y component (nT, positive east). </p>
<p> <code>z</code> means list Z component (nT, positive down). </p>
<p> <code>d</code> means list declination (deg, clockwise from north). </p>
<p> <code>i</code> means list inclination (deg, positive down). </p>
<p> Append one or more number to indicate the requested field contribution(s): </p>
<p> <code>0</code> means IGRF field (no combinations allowed) </p>
<p> <code>1</code> means CM4 Core field </p>
<p> <code>2</code> means CM4 Lithospheric field </p>
<p> <code>3</code> means CM4 Primary Magnetospheric field </p>
<p> <code>4</code> means CM4 Induced Magnetospheric field </p>
<p> <code>5</code> means CM4 Primary ionospheric field </p>
<p> <code>6</code> means CM4 Induced ionospheric field </p>
<p> <code>7</code> means CM4 Toroidal field </p>
<p> <code>9</code> means Core field from IGRF and other contributions from CM4. DO NOT USE BOTH 0 AND 9. </p>
<p> Appending several numbers (1-7) will add up the different contributions. For example <code>-Ft</code>/<code>12</code> computes the total field due to Core and Lithospheric sources. Two special cases are allowed, which mix which Core field from IGRF and other sources from CM4. <code>-Ft</code>/<code>934</code> computes Core field due to IGRF plus terms 3 and 4 from CM4 (but you can add others). <code>-Ft</code>/<code>934</code> the same as above but output the field components. The data is written out in the order they appear in <i>flags</i> [Default is <code>-Frthxyzdi</code>/<code>1</code>].</p>
<dt><code>-G</code></p>
<dd> Specifies that coordinates are geocentric [geodetic].</p>
<dt><code>-L</code></p>
<dd> Computes J field vectors from certain external sources. </p>
<p> <code>r</code> means output all input columns before adding the items below (all in Ampers/m). </p>
<p> <code>t</code> means list magnitude field. </p>
<p> <code>x</code> means list X component. </p>
<p> <code>y</code> means list Y component. </p>
<p> <code>z</code> means list Z or current function Psi. </p>
<p> Append a number to indicate the requested J contribution: </p>
<p> <code>1</code> means Induced Magnetospheric field. </p>
<p> <code>2</code> means Primary ionospheric field. </p>
<p> <code>3</code> means Induced ionospheric field. </p>
<p> <code>4</code> means Poloidal field.</p>
<dt><code>-Sc</code><i>low/high</i></p>
<dd> Limits the wavelengths of the core field contribution to the band indicated by the low and high spherical harmonic order [1/13].</p>
<dt><code>-Sl</code><i>low/high</i></p>
<dd> Limits the wavelengths of the lithosphere field contribution to the band indicated by the low and high spherical harmonic order [14/65].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 4 input columns unless <code>-A</code> is used].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is reflected by <code>-F</code>].</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit.</dl>
<h2>TIME SETTINGS</h2>
<p> If binary input files are used then absolute time are stored as time relative to the selected epoch. However, since the epoch used is not stored in the data files there can be problems decoding the correct time. The mgd77 supplement uses the Unix time system as its default; thus you should make sure that binary data files with time uses the same system (see the GMT default TIME_SYSTEM).</p>
<h2>EXAMPLES</h2>
<p> To get the CM4 Total field, Declination and Inclination due to all but lithospheric and toroidal field at a one point location and decimal time 2000.0, try </p>
<pre>
echo -28 38 0 2000.0 | gmt mgd77magref -A+y -Ftdi/13456
</pre>
<p> To do the same as above but at noon (Universal Time) of first May 2001, try </p>
<pre>
echo -28 38 0 2001-05-01T12:00:00 | gmt mgd77magref -Ftdi/13456
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>mgd77info</code>, <code>mgd77list</code>, <code>mgd77manage</code>, <code>mgd77track</code>, <code>gmt.conf</code></p>
<h2>REFERENCES</h2>
<p> Comprehensive Modeling of the Geomagnetic Field, see <i><a rel="nofollow" href="http://denali.gsfc.nasa.gov/cm/">http://denali.gsfc.nasa.gov/cm/</a></i> </p>
<p> The International Geomagnetic Reference Field (IGRF), see <i><a rel="nofollow" href="http://www.iugg.org/IAGA/iaga_pages/pubs_prods/igrf.htm">http://www.iugg.org/IAGA/iaga_pages/pubs_prods/igrf.htm</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
