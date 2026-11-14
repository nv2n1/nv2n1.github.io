---
title: "funinfoget(3)"
name: "funinfoget"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funinfoget/"
description: "FunInfoGet – get information from Funtools struct"
---

<h2>NAME</h2>
<p> <code>FunInfoGet &#8211; get information from Funtools struct</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<pre>
  int FunInfoGet(Fun fun, int type, char *addr, ...)
</pre>
<h2>DESCRIPTION</h2>
<p> The FunInfoGet() routine returns information culled from the Funtools structure. The first argument is the Fun handle from which information is to be retrieved. This first required argument is followed by a variable length list of pairs of arguments. Each pair consists of an integer representing the type of information to retrieve and the address where the information is to be stored. The list is terminated by a 0. The routine returns the number of get actions performed. </p>
<p> The full list of available information is described below. Please note that only a few of these will be useful to most application developers. For imaging applications, the most important types are: </p>
<p>FUN_SECT_DIM1 int           /* dim1 for section */<br />
    FUN_SECT_DIM2 int       /* dim2 for section */<br />
        FUN_SECT_BITPIX int /* bitpix for section */</p>
<p> These would be used to determine the dimensions and data type of image data retrieved using the <i>FunImageGet()</i> routine. For example: </p>
<p>/* extract and bin the data section into an image buffer */<br />
buf = FunImageGet(fun, NULL, NULL);<br />
/* get required information from funtools structure.<br />
   this should come after the FunImageGet() call, in case the call<br />
   changed sect_bitpix */<br />
FunInfoGet(fun,<br />
           FUN_SECT_BITPIX, &amp;bitpix,<br />
           FUN_SECT_DIM1, &amp;dim1,<br />
           FUN_SECT_DIM2, &amp;dim2,<br />
           0);<br />
/* loop through pixels and reset values below limit to value */<br />
for (i = 0; i &lt; dim1 * dim2; i++) {<br />
    switch (bitpix) {<br />
    case 8:<br />
        if (cbuf[i] &lt;= blimit)<br />
            cbuf[i] = bvalue;<br />
        &#8230;<br />
    }</p>
<p> It is important to bear in mind that the call to <i>FunImageGet()</i> can change the value of <font SIZE="-1">FUN_SECT_BITPIX</font> (e.g. if &#8220;bitpix=n&#8221; is passed in the param list). Therefore, a call to <i>FunInfoGet()</i> should be made <code>after</code> the call to <i>FunImageGet()</i>, in order to retrieve the updated bitpix value. See the imblank example code for more details. </p>
<p> It also can be useful to retrieve the World Coordinate System information from the Funtools structure. Funtools uses the the <font SIZE="-1">WCS</font> Library developed by Doug Mink at <font SIZE="-1">SAO</font>, which is available here. (More information about the WCSTools project in general can be found here.) The <i>FunOpen()</i> routine initializes two <font SIZE="-1">WCS</font> structures that can be used with this <font SIZE="-1">WCS</font> Library. Applications can retrieve either of these two <font SIZE="-1">WCS</font> structures using FunInfoGet(): </p>
<p>FUN_WCS struct WorldCoor *      /* wcs structure, for image coordinates*/<br />
    FUN_WCS0 struct WorldCoor * /* wcs structure, for physical coordinates */</p>
<p> The structure retrieved by <font SIZE="-1">FUN_WCS</font> is a <font SIZE="-1">WCS</font> library handle containing parameters suitable for use with image coordinates, regardless of whether the data are images or tables. For this structure, the <font SIZE="-1">WCS</font> reference point (<font SIZE="-1">CRPIX</font>) has been converted to image coordinates if the underlying file is a table (and therefore in physical coordinates). You therefore must ensure that the positions being passed to a routine like pix2wcs are in image coordinates. The <font SIZE="-1">FUN_WCS0</font> structure has not had its <font SIZE="-1">WCS</font> reference point converted to image coordinates. It therefore is useful when passing processing physical coordinates from a table. </p>
<p> Once a <font SIZE="-1">WCS</font> structure has been retrieved, it can be used as the first argument to the <font SIZE="-1">WCS</font> library routines. (If the structure is <font SIZE="-1">NULL</font>, no <font SIZE="-1">WCS</font> information was contained in the file.) The two important <font SIZE="-1">WCS</font> routines that Funtools uses are: </p>
<p>#include &lt;wcs.h&amp;gt<br />
void pix2wcs(wcs, xpix, ypix, xpos, ypos) struct WorldCoor *wcs; /* World coordinate system structure */<br />
double xpix, ypix;                                               /* x and y coordinates in pixels */<br />
double *xpos, *ypos;                                             /* RA and Dec in degrees (returned) */</p>
<p> which converts pixel coordinates to sky coordinates, and: </p>
<p>void wcs2pix(wcs, xpos, ypos, xpix, ypix, offscl) struct WorldCoor *wcs; /* World coordinate system structure */<br />
double xpos, ypos;                                                       /* World coordinates in degrees */<br />
double *xpix, *ypix;                                                     /* coordinates in pixels */<br />
int *offscl;                                                             /* 0 if within bounds, else off scale */</p>
<p> which converts sky coordinates to pixel coordinates. Again, please note that the wcs structure returned by <font SIZE="-1">FUN_WCS</font> assumes that image coordinates are passed to the pix2wcs routine, while <font SIZE="-1">FUN_WCS0</font> assumes that physical coordinates are passed. </p>
<p> Note that funtools.h file automatically includes wcs.h. An example program that utilizes these <font SIZE="-1">WCS</font> structure to call <font SIZE="-1">WCS</font> Library routines is twcs.c. </p>
<p> The following is the complete list of information that can be returned: </p>
<pre><code>
name type comment-- -- -- -- - -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -FUN_FNAME char * /* file name */
    FUN_GIO GIO                                                                                                                /* gio handle */
        FUN_HEADER FITSHead                                                                                                    /* fitsy header struct */
            FUN_TYPE int                                                                                                       /* TY_TABLE,TY_IMAGE,TY_EVENTS,TY_ARRAY */
                FUN_BITPIX int                                                                                                 /* bits/pixel in file */
                    FUN_MIN1 int                                                                                               /* tlmin of axis1 -- tables */
                        FUN_MAX1 int                                                                                           /* tlmax of axis1 -- tables */
                            FUN_MIN2 int                                                                                       /* tlmin of axis2 -- tables */
                                FUN_MAX2 int                                                                                   /* tlmax of axis2 -- tables */
                                    FUN_DIM1 int                                                                               /* dimension of axis1 */
                                        FUN_DIM2 int                                                                           /* dimension of axis2 */
                                            FUN_ENDIAN int                                                                     /* 0=little, 1=big endian */
                                                FUN_FILTER char *                                                              /* supplied filter */
                                                    FUN_IFUN FITSHead                                                          /* pointer to reference header */
                                                        FUN_IFUN0 FITSHead                                                     /* same as above, but no reset performed */
                                                            /* image information */
                                                            FUN_DTYPE int                                /* data type for images */
                                                                FUN_DLEN int                             /* length of image in bytes */
                                                                    FUN_DPAD int                         /* padding to end of extension */
                                                                        FUN_DOBLANK int                  /* was blank keyword defined? */
                                                                            FUN_BLANK int                /* value for blank */
                                                                                FUN_SCALED int           /* was bscale/bzero defined? */
                                                                                    FUN_BSCALE double    /* bscale value */
                                                                                        FUN_BZERO double /* bzero value */
                                                                                            /* table information */
                                                                                            FUN_NROWS int                /* number of rows in file (naxis2) */
                                                                                                FUN_ROWSIZE int          /* size of user row struct */
                                                                                                    FUN_BINCOLS char *   /* specified binning columns */
                                                                                                        FUN_OVERFLOW int /* overflow detected during binning? */
                                                                                                            /* array information */
                                                                                                            FUN_SKIP int /* bytes to skip in array header */
                                                                                                                /* section information */
                                                                                                                FUN_SECT_X0 int                                             /* low dim1 value of section */
                                                                                                                    FUN_SECT_X1 int                                         /* hi dim1 value of section */
                                                                                                                        FUN_SECT_Y0 int                                     /* low dim2 value of section */
                                                                                                                            FUN_SECT_Y1 int                                 /* hi dim2 value of section */
                                                                                                                                FUN_SECT_BLOCK int                          /* section block factor */
                                                                                                                                    FUN_SECT_BTYPE int                      /* 's' (sum), 'a' (average) for binning */
                                                                                                                                        FUN_SECT_DIM1 int                   /* dim1 for section */
                                                                                                                                            FUN_SECT_DIM2 int               /* dim2 for section */
                                                                                                                                                FUN_SECT_BITPIX int         /* bitpix for section */
                                                                                                                                                    FUN_SECT_DTYPE int      /* data type for section */
                                                                                                                                                        FUN_RAWBUF char *   /* pointer to raw row buffer */
                                                                                                                                                            FUN_RAWSIZE int /* byte size of raw row records */
                                                                                                                                                                /* column  information */
                                                                                                                                                                FUN_NCOL int        /* number of row columns defined */
                                                                                                                                                                    FUN_COLS FunCol /* array of row columns */
                                                                                                                                                                        /* WCS information */
                                                                                                                                                                        FUN_WCS struct WorldCoor *      /* wcs structure, converted for images*/
                                                                                                                                                                            FUN_WCS0 struct WorldCoor * /* wcs structure, not converted */
</code></pre>
<p> Row applications would not normally need any of this information. An example of how these values can be used in more complex programs is the evnext example code. In this program, the time value for each row is changed to be the value of the succeeding row. The program thus reads the time values for a batch of rows, changes the time values to be the value for the succeeding row, and then merges these changed time values back with the other columns to the output file. It then reads the next batch, etc. </p>
<p> This does not work for the last row read in each batch, since there is no succeeding row until the next batch is read. Therefore, the program saves that last row until it has read the next batch, then processes the former before starting on the new batch. In order to merge the last row successfully, the code uses <font SIZE="-1">FUN_RAWBUF</font> to save and restore the raw input data associated with each batch of rows. Clearly, this requires some information about how funtools works internally. We are happy to help you write such programs as the need arises.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
