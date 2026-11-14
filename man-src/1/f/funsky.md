---
title: "funsky(1)"
name: "funsky"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funsky/"
description: "funsky – convert between image and sky coordinates"
---

<h2>NAME</h2>
<p> <code>funsky &#8211; convert between image and sky coordinates</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
funsky iname[ext] #RA, Dec(deg) or image pix from stdin funsky iname[ext][lname] #RA, Dec(deg) or image pix from list funsky iname[ext][col1][col2] #named cols : units from stdin funsky iname[ext][lname][col1][col2] #named cols : units from list
</code></pre>
<h2>OPTIONS</h2>
<p>&#8211; d #always use integer tlmin conversion(as ds9 does) &#8211; r #convert x, y to RA, Dec(default:convert RA, Dec to x, y) &#8211; o #include offset from the nominal target position(in arcsec) &#8211; v #display input values also(default:display output only) &#8211; T #output display in rdb format(w / header, tab delimiters)</p>
<h2>DESCRIPTION</h2>
<p> Funsky converts input sky coordinates (<font SIZE="-1">RA</font>, Dec) to image coordinates (or vice versa) using the <font SIZE="-1">WCS</font> information contained in the specified <font SIZE="-1">FITS</font> file. Several calling sequences are supported in order to make it easy to specify coordinate positions in different ways. </p>
<p> The first required argument is always the input <font SIZE="-1">FITS</font> file (or extension) containing the <font SIZE="-1">WCS</font> information in an extension header. Note that the data from this file is not used. By default, the program converts input <font SIZE="-1">RA</font> and Dec values to X and Y using this <font SIZE="-1">WCS</font> information. If the <font SIZE="-1">WCS</font> is associated with a <font SIZE="-1">FITS</font> image, then the X,Y values are image values. If the <font SIZE="-1">WCS</font> is associated with a binary table, then the X, Y values are physical values. To convert X,Y to <font SIZE="-1">RA</font> and Dec, use the <code>-r</code> (reverse) switch. </p>
<p> If no other command arguments are supplied, then the input positions are read from the standard input. Each line is assumed to contain a single coordinate position consisting of an <font SIZE="-1">RA</font> in hours (or X in pixels) followed by a Dec in degrees (or Y in pixels). The usual delimiters are supported (spaces, commas, tabs). For example: </p>
<pre>
 # read from stdin, default column names and units
 [sh] funsky snr.ev
 22.982695    58.606523   # input RA (hrs), Dec(deg)
    510.00       510.00
 22.982127    58.607634   # input
    512.00       510.50
 22.981700    58.614301   # input
    513.50       513.50
 ^D                       # end of input
</pre>
<p> If a second argument is supplied, this argument is assumed to be a file containing <font SIZE="-1">RA</font> (X) and Dec (Y) positions. The file can either be an <font SIZE="-1">ASCII</font> table or a <font SIZE="-1">FITS</font> binary table. The order of columns is unimportant, if the table has a column header. In this case, the names of the columns must be one of &#8220;<font SIZE="-1">RA</font>&#8221;, &#8220;<font SIZE="-1">DEC</font>&#8221;, or &#8220;X&#8221;, &#8220;Y&#8221; for sky to image and image to sky conversions, respectively. If the table has no header, then once again, <font SIZE="-1">RA</font> (X) is assumed to first, followed by <font SIZE="-1">DEC</font> (Y). For example: </p>
<p>#read from file, default column names and units<br />
[sh] cat hd.in<br />
    RA DEC&#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -22.982695 58.606523 22.982127 58.607634 22.981700 58.614301</p>
<pre>
  [sh] funsky snr.ev hd.in
        510.00       510.00
        512.00       510.50
        513.50       513.50
</pre>
<p> If three arguments are supplied, then the input positions again are read from the standard input. Each line is assumed to contain a single coordinate position consisting of an <font SIZE="-1">RA</font> (or X in pixels) followed by a Dec (or Y in pixels), with the usual delimiters supported. However, the second and third arguments now specify the column names and/or sky units using a colon-delimited syntax: </p>
<p>[colname] : [h | d | r]</p>
<p> If the colname is omitted, the names default to &#8220;<font SIZE="-1">RA</font>&#8221;, &#8220;<font SIZE="-1">DEC</font>&#8221;, &#8220;X&#8221;, &#8220;Y&#8221;, &#8220;<font SIZE="-1">COL1</font>&#8221;, or &#8220;<font SIZE="-1">COL2</font>&#8221; as above. If the units are omitted, the default is hours for <font SIZE="-1">RA</font> and degrees for Dec. When the -r switch is used (convert from image to sky) the units are applied to the output instead of the input. The following examples will serve to illustrate the options: </p>
<p>#read from stdin, specifying column names(def.units \<br />
                                          : hours, degrees)<br />
[sh] cat hd.in<br />
    MYRA MYDEC&#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -22.982695 58.606523 22.982127 58.607634 22.981700 58.614301</p>
<pre>
  [sh] funsky snr.ev MYRA MYDEC &lt; hd.in
        510.00       510.00
        512.00       510.50
        513.50       513.50
</pre>
<p>#read from stdin, specifying column names and units<br />
[sh] cat dd.in<br />
    MYRA MYDEC&#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -344.740432 58.606523 344.731900 58.607634 344.725500 58.614301</p>
<pre>
  [sh] funsky snr.ev MYRA:d MYDEC:d &lt; dd.in
        510.00       510.00
        512.00       510.50
        513.50       513.50
</pre>
<pre>
  # read stdin, convert image to sky, specifying output sky units
  [sh] cat im.in
        510.00       510.00
        512.00       510.50
        513.50       513.50
</pre>
<pre>
  [sh] cat im.in | funsky -r snr.ev :d :d
  344.740432    58.606523
  344.731900    58.607634
  344.725500    58.614301
</pre>
<p> Finally, four command arguments specify both and input file and column names and/or units: </p>
<p>[sh] cat dd.in<br />
    MYRA MYDEC&#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -344.740432 58.606523 344.731900 58.607634 344.725500 58.614301</p>
<pre>
  [sh] funsky snr.ev dd.in MYRA:d MYDEC:d
        510.00       510.00
        512.00       510.50
        513.50       513.50
</pre>
<pre>
  # read file, convert image to sky, specifying output sky units
  [sh] cat im.in
        510.00       510.00
        512.00       510.50
        513.50       513.50
</pre>
<pre>
  [sh] funsky -r snr.ev im.in :d :d
    344.740432    58.606523
    344.731900    58.607634
    344.725500    58.614301
</pre>
<p> By default, the output of funsky consists only of the converted coordinate position(s), one per output line. This makes parsing in shell scripts easy. Use the <code>-v</code> (verbose) switch to specify that the input coordinates should be pre-pended to each line. For example: </p>
<p>[sh] cat dd.in<br />
    MYRA MYDEC&#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; -344.740432 58.606523 344.731900 58.607634 344.725500 58.614301</p>
<pre>
  [sh] funsky snr.ev dd.in MYRA:d MYDEC:d
        510.00       510.00
        512.00       510.50
        513.50       513.50
</pre>
<pre>
  [sh] funsky -v snr.ev dd.in MYRA:d MYDEC:d
    344.740432    58.606523       510.00       510.00
    344.731900    58.607634       512.00       510.50
    344.725500    58.614301       513.50       513.50
</pre>
<p> In addition, a full starbase table can be output using the <code>-T</code> (table) switch. This switch can be used with or without the -v switch. If the -T and -v are both specified, then a descriptive header parameters are output before the table (mainly to remind you of the sky units): </p>
<p>#output table in non &#8211; verbose mode<br />
[sh] funsky &#8211; T snr.ev dd.in MYRA : d MYDEC : d<br />
                                                  X Y&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;510.00 510.00 512.00 510.50 513.50 513.50</p>
<pre>
  # output table in verbose mode
  [sh] funsky -T -v snr.ev dd.in MYRA:d MYDEC:d
  # IFILE = /Users/eric/data/snr.ev
  # ICOL1 = MYRA
  # ICOL2 = MYDEC
  # IUNITS1 = d
  # IUNITS2 = d
  # OCOL1 = X
  # OCOL2 = Y
</pre>
<pre><code>
MYRA MYDEC X Y-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --344.740432 58.606523 510.00 510.00 344.731900 58.607634 512.00 510.50 344.725500 58.614301 513.50 513.50
</code></pre>
<p> Finally, the <code>-d</code> (ds9) switch mimicks ds9&#8217;s use of integer <font SIZE="-1">TLMIN</font> and <font SIZE="-1">TLMAX</font> values for all coordinate transformations. <font SIZE="-1">FITS</font> conventions seem to call for use of floating point <font SIZE="-1">TLMIN</font> and <font SIZE="-1">TLMAX</font> when the data are floats. This convention is followed by funsky but results in a small discrepancy with ds9&#8217;s converted values for floating point data. We will remedy this conflict in the future, maybe.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
