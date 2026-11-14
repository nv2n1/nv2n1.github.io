---
title: "libppm(3)"
name: "libppm"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libppm/"
description: "libppm – functions for PPM programs"
---

<h2 class="name">NAME</h2>
<p> libppm &#8211; functions for PPM programs</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;netpbm/ppm.h&gt;</code> </p>
<p> <code>void ppm_init(</code><code>int *</code> <i>argcP</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>char&nbsp;<wbr>*</code>&nbsp;<wbr><i>argv</i><code>[]</code><code>);</code> </p>
<p> <code>pixel ** ppm_allocarray(</code> </p>
<p> <code>int </code><i>cols</i><code>,</code><code>int</code> <i>rows</i><code>);</code> </p>
<p> <code>pixel * ppm_allocrow(</code><code>int</code> <i>cols</i><code>);</code> </p>
<p> <code>void ppm_freearray(</code><code>pixel **</code> <i>pixels</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>rows</i><code>);</code> </p>
<p> <code>void ppm_freerow(</code><code>pixel *</code> <i>pixelrow</i><code>);</code> </p>
<p> <code>void ppm_readppminit(</code><code>FILE *</code> <i>fp</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int&nbsp;<wbr>*</code>&nbsp;<wbr><i>colsP</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int&nbsp;<wbr>*</code>&nbsp;<wbr><i>rowsP</i><code>,</code> </p>
<p> <code>pixval *</code> <i>maxvalP</i><code>,</code><code>int *</code> <i>formatP</i><code> );</code> </p>
<p> <code>void ppm_readppmrow(</code><code>FILE *</code><i>fp</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixel&nbsp;<wbr>*</code>&nbsp;<wbr><i>pixelrow</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int&nbsp;<wbr></code><i>cols</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval&nbsp;<wbr></code><i>maxval</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int&nbsp;<wbr></code><i>format</i><code>);</code> </p>
<p> <code>pixel ** ppm_readppm(</code><code>FILE *</code> <i>fp</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int&nbsp;<wbr>*</code>&nbsp;<wbr><i>colsP</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int&nbsp;<wbr>*</code>&nbsp;<wbr><i>rowsP</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixvalP&nbsp;<wbr>*</code>&nbsp;<wbr><i>maxvalP</i><code>);</code> </p>
<p> <code>void ppm_writeppminit(</code><code>FILE * </code><i>fp</i>,<br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>cols</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>rows</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>maxval</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>forceplain</i><code>);</code> </p>
<p> <code>void ppm_writeppmrow(</code><code>FILE *</code> <i>fp</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixel&nbsp;<wbr>*</code>&nbsp;<wbr><i>pixelrow</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>cols</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>maxval</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>forceplain</i><code>);</code> </p>
<p> <code>void ppm_writeppm(</code><code>FILE *</code> <i>fp</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixel&nbsp;<wbr>**</code>&nbsp;<wbr><i>pixels</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>cols</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>rows</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>maxval</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>forceplain</i><code>);</code> </p>
<p> <code>void ppm_writeppm(</code><code>FILE *</code> <i>fp</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixel&nbsp;<wbr>**</code>&nbsp;<wbr><i>pixels</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>cols</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>rows</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>maxval</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>forceplain</i><code>);</code> </p>
<p> <code>void ppm_nextimage(</code><code>FILE *</code> <i>file</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int&nbsp;<wbr>*&nbsp;<wbr>const</code>&nbsp;<wbr><i>eofP</i><code>);</code> </p>
<p> <code>void ppm_check(</code><code>FILE *</code> <i>file</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>const enum pm_check_type</code>&nbsp;<wbr><i>check_type</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>const int</code>&nbsp;<wbr><i>format</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>const int</code>&nbsp;<wbr><i>cols</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>const int</code>&nbsp;<wbr><i>rows</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>const int</code>&nbsp;<wbr><i>maxval</i><code>,</code> <code>enum pm_check_code * const</code> <i>retval</i><code>);</code> </p>
<p> <code>typedef &#8230; pixel;</code> </p>
<p> <code>typedef &#8230; pixval;</code> </p>
<p> <code>#define PPM_MAXMAXVAL &#8230;</code> </p>
<p> <code>#define PPM_OVERALLMAXVAL &#8230;</code> </p>
<p> <code>#define PPM_FORMAT &#8230;</code> </p>
<p> <code>#define RPPM_FORMAT &#8230;</code> </p>
<p> <code>#define PPM_TYPE PPM_FORMAT</code> </p>
<p> <code>#define</code> <code>PPM_FORMAT_TYPE(</code><i>format</i><code>)</code> <code>&#8230;</code> </p>
<p> <code>pixval PPM_GETR(pixel</code> <i>p</i><code>)</code> </p>
<p> <code>pixval PPM_GETG(pixel</code> <i>p</i><code>)</code> </p>
<p> <code>pixval PPM_GETB(pixel</code> <i>p</i><code>)</code> </p>
<p> <code>void PPM_ASSIGN(pixel</code> <i>p</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>red</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>grn</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>blu</i><code>)</code> </p>
<p> <code>int PPM_EQUAL(pixel</code> <i>p</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixel</code>&nbsp;<wbr><i>q</i><code>)</code> </p>
<p> <code>int PPM_ISGRAY(pixel</code> <i>p</i><code>)</code> </p>
<p> <code>void</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>PPM_DEPTH(pixel</code>&nbsp;<wbr><i>newp</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixel</code>&nbsp;<wbr><i>p</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>oldmaxval</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>newmaxval</i><code>)</code> </p>
<p> <code>pixel ppm_parsecolor(char *</code> <i>colorname</i><code>,</code><br />
<code>pixval</code>&nbsp;<wbr><i>maxval</i><code>)</code> </p>
<p> <code>char * ppm_colorname(pixel *</code> <i>colorP</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>pixval</code>&nbsp;<wbr><i>maxval</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>hexok</i><code>)</code> </p>
<p> <code>void ppm_readcolornamefile(</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>const char&nbsp;<wbr>*</code><i>fileName</i>,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr><code>int</code>&nbsp;<wbr><i>mustOpen</i>,<br />
&nbsp;<wbr>&nbsp;<wbr><code>colorhash_table&nbsp;<wbr>*</code>&nbsp;<wbr><i>chtP</i>,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr><code>const char&nbsp;<wbr>***</code>&nbsp;<wbr><i>colornamesP</i><br />
&nbsp;<wbr>&nbsp;<wbr><code>)</code> </p>
<h2>DESCRIPTION</h2>
<p> These library functions are part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<h3>TYPES AND CONSTANTS</h3>
<p> Each <code>pixel</code> contains three <code>pixval</code>s, each of which should contain only the values between <code>0</code> and <code>PPM_MAXMAXVAL</code>. </p>
<h3>MANIPULATING PIXELS</h3>
<p> The macros <code>PPM_GETR</code>, <code>PPM_GETG</code>, and <code>PPM_GETB</code> retrieve the red, green, or blue sample, respectively, from the given pixel. </p>
<p> The <code>PPM_ASSIGN</code> macro assigns the given values to the red, green, and blue samples of the given pixel. </p>
<p> The <code>PPM_EQUAL</code> macro tests two pixels for equality. </p>
<p> The <code>PPM_ISGRAY</code> macro tests a pixel for being gray. It returns true if and only if the color of pixel <i>p</i> is black, white, or gray. </p>
<p> The <code>PPM_DEPTH</code> macro scales the colors of pixel <i>p</i> according the old and new maxvals and assigns the new values to <i>newp</i>. It is intended to make writing ppmtowhatever easier. </p>
<p> The <code>PPM_LUMIN</code>, <code>PPM_CHROM_R</code>, and <code>PPM_CHROM_B</code> macros determine the luminance, red chrominance, and blue chrominance, respectively, of the pixel <i>p</i>. The scale of all these values is the same as the scale of the input samples (i.e. 0 to maxval for luminance, -maxval/2 to maxval/2 for chrominance). </p>
<p> Note that the macros do it by floating point multiplication. If you are computing these values over an entire image, it may be significantly faster to do it with multiplication tables instead. Compute all the possible products once up front, then for each pixel, just look up the products in the tables. </p>
<h3>INITIALIZATION</h3>
<p> <code>ppm_init()</code> is obsolete (at least since Netpbm 9.25 (March 2002)). Use <code>pm_proginit()</code> instead. </p>
<p> <code>ppm_init()</code> is identical to <code>pm_proginit</code>. </p>
<h3>MEMORY MANAGEMENT</h3>
<p> <code>ppm_allocarray()</code> allocates an array of pixels. </p>
<p> <code>ppm_allocrow()</code> allocates a row of the given number of pixels. </p>
<p> <code>ppm_freearray()</code> frees the array allocated with <code>ppm_allocarray()</code> containing the given number of rows. </p>
<p> <code>ppm_freerow()</code> frees a row of pixelss allocated with <code>ppm_allocrow()</code>. </p>
<h3>READING FILES</h3>
<p> If a function in this section is called on a PBM or PGM format file, it translates the PBM or PGM file into a PPM file on the fly and functions as if it were called on the equivalent PPM file. The <i>format</i> value returned by <code>ppm_readppminit()</code> is, however, not translated. It represents the actual format of the PBM or PGM file. </p>
<p> <code>ppm_readppminit()</code> reads the header of a PPM file, returning all the information from the header and leaving the file positioned just after the header. </p>
<p> <code>ppm_readppmrow()</code> reads a row of pixels into the <i>pixelrow</i> array. <i>format</i>, <i>cols</i>, and <i>maxval</i> are the values returned by <code>ppm_readppminit()</code>. </p>
<p> <code>ppm_readppm()</code> reads an entire PPM image into memory, returning the allocated array as its return value and returning the information from the header as <i>rows</i>, <i>cols</i>, and <i>maxval</i>. This function combines <code>ppm_readppminit()</code>, <code>ppm_allocarray()</code>, and <code>ppm_readppmrow()</code>. </p>
<h3>WRITING FILES</h3>
<p> <code>ppm_writeppminit()</code> writes the header for a PPM file and leaves it positioned just after the header. </p>
<p> <i>forceplain</i> is a logical value that tells <code>ppm_writeppminit() </code> to write a header for a plain PPM format file, as opposed to a raw PPM format file. </p>
<p> <code>ppm_writeppmrow()</code> writes the row <i>pixelrow</i> to a PPM file. For meaningful results, <i>cols</i>, <i>maxval</i>, and <i>forceplain</i> must be the same as was used with <code>ppm_writeppminit()</code>. </p>
<p> <code>ppm_writeppm()</code> write the header and all data for a PPM image. This function combines <code>ppm_writeppminit()</code> and <code>ppm_writeppmrow()</code>. </p>
<h3>MISCELLANEOUS</h3>
<p> <code>ppm_nextimage()</code> positions a PPM input file to the next image in it (so that a subsequent <code>ppm_readppminit()</code> reads its header). </p>
<p> <code>ppm_nextimage()</code> is analogous to <code>pbm_nextimage()</code>, but works on PPM, PGM, and PBM files. </p>
<p> <code>ppm_check() </code> checks for the common file integrity error where the file is the wrong size to contain all the image data. </p>
<p> <code>ppm_check() </code> is analogous to <code>pbm_check()</code>, but works on PPM, PGM, and PBM files. </p>
<h3>COLOR</h3>
<p> <code>Luminance, Chrominance (YcbCr)</code> </p>
<pre><code>

float PPM_LUMIN(pixel p);
float PPM_CHROM_B(pixel p);
float PPM_CHROM_R(pixel p);
</code></pre>
<p> <code>PPM_LUMIN</code> takes a <code>pixel</code> as an argument and returns the luminance of that pixel, with the same maxval as the pixel (e.g. if the pixel&#8217;s maxval is 255, a <code>PPM_LUMIN</code> value of 255 means fully luminant). </p>
<p> <code>PPM_CHROM_B</code> and <code>PPM_CHROM_R</code> are similar, for the red and blue chrominance values. </p>
<p>pixel ppm_color_from_ycbcr(unsigned int y,<br />
                           int cb,<br />
                           int cr);</p>
<p> <code>ppm_color_from_ycbcr()</code> converts in the other direction. Given luminance and chrominance, it returns a pixel value. </p>
<p> <code>Hue, Saturation, Value (HSV)</code> </p>
<p>struct hsv {<br />
    double h; /* hue (degrees)  0..360 */<br />
    double s; /* saturation (0-1) */<br />
    double v; /* value (0-1) */<br />
};</p>
<p>pixel ppm_color_from_hsv(struct hsv const hsv,<br />
                         pixval const maxval);</p>
<p>struct hsv<br />
ppm_hsv_from_color(pixel const color,<br />
                   pixval const maxval);</p>
<p> These convert a color between from <code>pixel</code> (RGB) form and HSV. </p>
<p>pixval<br />
ppm_saturation(pixel const p,<br />
               pixval const maxval);</p>
<p> This gives you the saturation of a color, as a pixval. (e.g. if the saturation of <i>p</i> is 50% and <i>maxval</i> is 100, <code>ppm_saturation()</code> returns 50). </p>
<p> <code>Berlin-Kay Color</code> </p>
<p> Brent Berlin and Paul Kay in 1969 did a study which identified a set of 11 basic colors people universally recognize. They are: </p>
<dl>
<dt>&bull;</p>
<dd> black</p>
<dt>&bull;</p>
<dd> gray</p>
<dt>&bull;</p>
<dd> white</p>
<dt>&bull;</p>
<dd> red</p>
<dt>&bull;</p>
<dd> orange</p>
<dt>&bull;</p>
<dd> yellow</p>
<dt>&bull;</p>
<dd> green</p>
<dt>&bull;</p>
<dd> blue</p>
<dt>&bull;</p>
<dd> violet</p>
<dt>&bull;</p>
<dd> purple</p>
<dt>&bull;</p>
<dd> brown </p>
</dl>
<p> The <code>bk_color</code> type represents a color from this set: </p>
<p>typedef enum {<br />
    BKCOLOR_BLACK = 0,<br />
    BKCOLOR_GRAY,<br />
    BKCOLOR_WHITE,<br />
    BKCOLOR_RED,<br />
    BKCOLOR_ORANGE,<br />
    BKCOLOR_YELLOW,<br />
    BKCOLOR_GREEN,<br />
    BKCOLOR_BLUE,<br />
    BKCOLOR_VIOLET,<br />
    BKCOLOR_PURPLE,<br />
    BKCOLOR_BROWN<br />
} bk_color;</p>
<p> You can use this as an index of an array, in which case you might also want macro <code>BKCOLOR_COUNT</code>, which is the number of colors in the set (11). </p>
<p> To translate between the <code>bk_color</code> type and the English names of the colors, use <code>ppm_bk_color_from_name()</code> and <code>ppm_name_from_bk_color()</code>: </p>
<pre><code>

bk_color
ppm_bk_color_from_name(const char *name);

const char *
ppm_name_from_bk_color(bk_color bkColor);
</code></pre>
<p> <code>ppm_bk_color_from_color()</code> tells you to which Berlin-Kay color a certain color is closest, by way of a fuzzy color matching algorithm: </p>
<pre>
<tt>
    bk_color
    ppm_bk_color_from_color(pixel  color,
                            pixval maxval);
</tt>
</pre>
<p> <i>maxval</i> is the maxval on which <i>color</i> is based. </p>
<p> <code>ppm_color_from_bk_color()</code> converts the opposite way: given a Berlin-Kay color, it gives the color, in <code>pixel</code> form, that best represents it. </p>
<pre>
<tt>
    pixel
    ppm_color_from_bk_color(bk_color bkColor,
                            pixval   maxval);
</tt>
</pre>
<p> <i>maxval</i> is the maxval on which the returned color is based. </p>
<p> All of the facilities in this section were new in Netpbm 10.34 (June 2006). </p>
<h3>COLOR NAMES</h3>
<p> <code>System Color Dictionary</code> </p>
<p> Netpbm uses the system&#8217;s X11 color dictionary (usually in <code>/usr/lib/X11/rgb.txt</code>). This is the same file the X Window System typically uses to associate colors with their names. </p>
<p> The color dictionary that Netpbm uses is in the file whose name is the value of the <code>RGBDEF</code> environment variable. If <code>RGBDEF</code> is not set, Netpbm defaults to the first existing file from this list: </p>
<dl>
<dt>&bull;</p>
<dd> <code>/usr/lib/X11/rgb.txt</code></p>
<dt>&bull;</p>
<dd> <code>/usr/openwinlib/rgb.txt</code></p>
<dt>&bull;</p>
<dd> <code>/usr/X11R6/lib/X11/rgb.txt</code> </p>
</dl>
<p> You can see the color names from a typical X11 color dictionary, which is probably very close to what is on your system, along with the colors, here . <code>This</code> website (1)<br />
&nbsp;<wbr>shows a bunch of other versions you could use. </p>
<p> Netpbm is packaged with a color dictionary. A standard Netpbm installation installs this file as &quot;misc/rgb.txt&quot; in the Netpbm directory. This color dictionary has colors from everywhere the Netpbm maintainer could find them, and is a superset of XFree 86&#8217;s color dictionary. </p>
<p> <code>ppm_parsecolor</code> </p>
<p> <code>ppm_parsecolor()</code> interprets a color specification and returns a pixel of the color that it indicates. The color specification is ASCII text, in one of these formats: </p>
<dl>
<dt>&bull;</p>
<dd> a name, as defined in the system color dictionary . </p>
<dt>&bull;</p>
<dd>
&nbsp;<wbr>An X11-style hexadecimal specifier: <tt>rgb:</tt><i>r</i>/<i>g</i>/<i>b</i>, where <i>r</i>, <i>g</i>, and <i>b</i> are each 1- to 4-digit hexadecimal numbers. For each, the maxval is the maximum number that can be represented in the number of hexadecimal digits given. Example: <tt>rgb:01/ff/8000</tt> specifies 1/255 red intensity, maximum green intensity, and about half blue intensity. </p>
<dt>&bull;</p>
<dd>
&nbsp;<wbr>An X11-style decimal specifier: <tt>rgbi:</tt><i>r</i>/<i>g</i>/<i>b</i>, where <i>r</i>, <i>g</i>, and <i>b</i> are floating point numbers from 0 to 1. </p>
<dt>&bull;</p>
<dd> an old-X11-style hexadecimal triple: <tt>#rgb</tt>, <tt>#rrggbb</tt>, <tt>#rrrgggbbb</tt>, or <tt>#rrrrggggbbbb</tt>. </p>
<dt>&bull;</p>
<dd> A triplet of decimal floating point numbers from 0.0 to 1.0, representing red, green, and blue intensities respectively, separated by commas. E.g. <tt>1.0,0.5,.25</tt>. This is for backwards compatibility; it was in use before MIT came up with the similar and preferred rgbi style). </p>
</dl>
<p> If the color specification does not conform to any of these formats, including the case that it is a name, but is not in the system color dictionary, <code>ppm_parsecolor()</code> <code>throws</code>an<code><a href="/docs/linux/man/1-error/">error</a></code>(1) </p>
<p> <code>ppm_colorname</code> </p>
<p> <code>ppm_colorname()</code> returns a string that describes the color of the given pixel. If a system color dictionary is available and the color appears in it, <code>ppm_colorname()</code> returns the name of the color from the file. If the color does not appear in a system color dictionary and <i>hexok</i> is true, <code>ppm_colorname()</code> returns a hexadecimal color specification triple (#rrggbb). If a system color dictionary is available but the color does not appear in it and <i>hexok</i> is false, <code>ppm_colorname()</code> returns the name of the closest matching color in the color file. Finally, if there is no system color dictionary available and <i>hexok</i> is false, <code>ppm_colorname()</code> fails and throws an error . </p>
<p> The string returned is in static libppm library storage which is overwritten by every call to <code>ppm_colorname()</code>. </p>
<p> <code>ppm_readcolornamefile</code> </p>
<p> <code>ppm_readcolornamefile()</code> reads the entire contents of the color dictionary in the file named <i>fileName</i> into data structures you can use to access it easily. </p>
<p> The function returns all the color names as an array of null-terminated strings. It mallocs the space for this array and returns its address at <i>colornamesP</i>. <code>(*colornamesP)[</code><i>i</i><code>]</code> is the address of the first character in the null-terminated string that is the name of the <i>i</i>th color in the dictionary. </p>
<p> The function also returns a <code>colorhash_table</code> (see COLOR INDEXING ) that matches all these color names up to the colors they represent. It mallocs the space for the <code>colorhash_table</code> and returns its address at <i>chtP</i>. The number that the <code>colorhash_table</code> associates with each color is the index into the color name array described above of the name of that color. </p>
<p> You may specify a null pointer for <i>fileName</i> to indicate the default color dictionary. </p>
<p> <i>mustOpen</i> is a boolean. If it is nonzero, the function fails and aborts the program if it is unable to open the specified color dictionary file. If it is zero, though, it simply treats an unopenable color dictionary as an empty one. The colorhash and color name array it returns contain no colors or names. </p>
<p> <code>ppm_readcolornamefile()</code> was new in Netpbm 10.15 (April 2003). </p>
<h3>COLOR INDEXING</h3>
<p> Sometimes in processing images, you want to associate a value with a particular color. Most often, that&#8217;s because you&#8217;re generating a color mapped graphics format. In a color mapped graphics format, the raster contains small numbers, and the file contains a color map that tells what color each of those small numbers refers to. If your image has only 256 colors, but each color takes 24 bits to describe, this can make your output file much smaller than a straightforward RGB raster would. </p>
<p> So, continuing the above example, say you have a <code>pixel</code> value for chartreuse and in your output file and you are going to represent chartreuse by the number 12. You need a data structure that allows your program quickly to find out that the number for a chartreuse <code>pixel</code> is 12. Netpbm&#8217;s color indexing data types and functions give you that. </p>
<p> <code>colorhash_table</code> is a C data type that associates an integer with each of an arbitrary number of colors. It is a hash table, so it uses far less space than an array indexed by the color&#8217;s RGB values would. </p>
<p> The problem with a <code>colorhash_table</code> is that you can only look things up in it. You can&#8217;t find out what colors are in it. So Netpbm has another data type for representing the same information, the poorly but historically named <code>colorhist_vector</code>. A <code>colorhist_vector</code> is just an array. Each entry represents a color and contains the color&#8217;s value (as a <code>pixel</code>) and the integer value associated with it. The entries are filled in starting with subscript 0 and going consecutively up for the number of colors in the histogram. </p>
<p> (The reason the name is poor is because a color histogram is only one of many things that could be represented by it). </p>
<p> <code>colorhash_table ppm_alloccolorhash()</code> </p>
<p> This creates a <code>colorhash_table</code> using dynamically allocated storage. There are no colors in it. If there is not enough storage, throws an error . </p>
<p> <code>void ppm_freecolorhash()</code> </p>
<p> This destroys a <code>ppm_freecolorhash </code> and frees all the storage associated with it. </p>
<p> <code>int ppm_addtocolorhash( colorhash_table cht, const pixel * const colorP, const int value)</code> </p>
<p> This adds the specified color to the specified <code>colorhash_table </code> and associates the specified value with it. </p>
<p> You must ensure that the color you are adding isn&#8217;t already present in the <code>colorhash_table</code>. </p>
<p> There is no way to update an entry or delete an entry from a <code>colorhash_table</code>. </p>
<p> <code>int ppm_lookupcolor( const colorhash_table cht, const pixel * const colorP )</code> </p>
<p> This looks up the specified color in the specified <code>colorhash_table</code>. It returns the integer value associated with that color. </p>
<p> If the specified color is not in the hash table, the function returns -1. (So if you assign the value -1 to a color, the return value is ambiguous). </p>
<p> <code>colorhist_vector ppm_colorhashtocolorhist( const colorhash_table cht,</code> </p>
<p> <code>const int ncolors )</code> </p>
<p> This converts a <code>colorhash_table</code> to a <code>colorhist_vector</code>. The return value is a new <code>colorhist_vector</code> which you must eventually free with <code>ppm_freecolorhist()</code>. </p>
<p> <code>ncolors</code> is the number of colors in <code>cht</code>. If it has more colors than that, <code>ppm_colorhashtocolorhist</code> does not create a <code>colorhist_vector</code> and returns NULL. </p>
<p> <code>colorhash_table ppm_colorhisttocolorhash( const colorhist_vector chv, const int ncolors ) </code> </p>
<p> This poorly named function does <i>not</i> convert from a <code>colorhist_vector</code> to a <code>colorhash_table</code>. </p>
<p> It does create a <code>colorhash_table</code> based on a <code>colorhist_vector</code> input, but the integer value for a given color in the output is not the same as the integer value for that same color in the input. <code>ppm_colorhisttocolorhash()</code> ignores the integer values in the input. In the output, the integer value for a color is the index in the input <code>colorhist_vector</code> for that color. </p>
<p> You can easily create a color map for an image by running <code>ppm_computecolorhist() </code> over the image, then <code>ppm_colorhisttocolorhash()</code> over the result. Now you can use <code>ppm_lookupcolor()</code> to find a unique color index for any pixel in the input. </p>
<p> If the same color appears twice in the input, <code>ppm_colorhisttocolorhash()</code> throws an error . </p>
<p> <code>ncolors</code> is the number of colors in <code>chv</code>. </p>
<p> The return value is a new <code>colorhash_table</code> which you must eventually free with <code>ppm_freecolorhash()</code>. </p>
<h3>COLOR HISTOGRAMS</h3>
<p> The Netpbm libraries give you functions to examine a Netpbm image and determine what colors are in it and how many pixels of each color are in it. This information is known as a color histogram. Netpbm uses its <code>colorhash_table</code> data type to represent a color histogram. </p>
<p> <code>colorhash_table ppm_computecolorhash( pixel ** const pixels, const int cols, const int rows, const int maxcolors, int* const colorsP )</code> </p>
<p> This poorly but historically named function generates a <code>colorhash_table</code> whose value for each color is the number of pixels in a specified image that have that color. (I.e. a color histogram). As a bonus, it returns the number of colors in the image. </p>
<p> (It&#8217;s poorly named because not all <code>colorhash_table</code>s are color histograms, but that&#8217;s all it generates). </p>
<p> <code>pixels</code>, <code>cols</code>, and <code>rows</code> describe the input image. </p>
<p> <code>maxcolors</code> is the maximum number of colors you want processed. If there are more colors that that in the input image, <code>ppm_computecolorhash()</code> returns NULL as its return value and stops processing as soon as it discovers this. This makes it run faster and use less memory. One use for <code>maxcolors</code> is when you just want to find out whether or not the image has more than N colors and don&#8217;t want to wait to generate a huge color table if so. If you don&#8217;t want any limit on the number of colors, specify <code>maxcolors</code>=<code>0</code>. </p>
<p> <code>ppm_computecolorhash()</code> returns the actual number of colors in the image as <code>*colorsP</code>, but only if it is less than or equal to <code>maxcolors</code>. </p>
<p> <code>colorhash_table ppm_computecolorhash2( FILE * const ifp, const int cols, const int rows, const pixval maxval, const int format,</code> </p>
<p> <code>const int maxcolors, int* const colorsP )</code> </p>
<p> This is the same as <code>ppm_computecolorhash()</code> except that instead of feeding it an array of pixels in storage, you give it an open file stream and it reads the image from the file. The file must be positioned after the header, at the raster. Upon return, the file is still open, but its position is undefined. </p>
<p> <code>maxval</code> and <code>format</code> are the values for the image (i.e. information from the file&#8217;s header). </p>
<p> <code>colorhist_vector ppm_computecolorhist( pixel ** pixels, int cols, int rows, int maxcolors, int * colorsP )</code> </p>
<p> This is like <code>ppm_computecolorhash()</code> except that it creates a <code>colorhist_vector</code> instead of a <code>colorhash_table</code>. </p>
<p> If you supply a nonzero <code>maxcolors</code> argument, that is the maximum number of colors you expect to find in the input image. If there are more colors than you say in the image, <code>ppm_computecolorhist()</code> returns a null pointer as its return value and nothing meaningful as <code>*colorsP</code>. </p>
<p> If not, the function returns the new <code>colorhist_vector </code> as its return value and the actual number of colors in the image as <code>*colorsP</code>. The returned array has space allocated for the specified number of colors regardless of how many actually exist. The extra space is at the high end of the array and is available for your use in expanding the <code>colorhist_vector</code>. </p>
<p> If you specify <code>maxcolors</code>=<code>0</code>, there is no limit on the number of colors returned and the return array has space for 5 extra colors at the high end for your use in expanding the <code>colorhist_vector</code>. </p>
<p> <code>colorhist_vector ppm_computecolorhist2( FILE * ifp, int cols, int rows, int maxcolors, pixval maxval, int format, int * colorsP )</code> </p>
<p> This is the same as <code>ppm_computecolorhist()</code> except that instead of feeding it an array of pixels in storage, you give it an open file stream and it reads the image from the file. The file must be positioned after the header, at the raster. Upon return, the file is still open, but its position is undefined. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) , <code><a href="/docs/linux/man/1-libpbm/">libpbm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Tony Hansen and Jef Poskanzer. </p>
<h2>Index</h2>
