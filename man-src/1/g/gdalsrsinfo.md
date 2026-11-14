---
title: "gdalsrsinfo(1)"
name: "gdalsrsinfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdalsrsinfo/"
description: "gdalsrsinfo – gdalsrsinfo lists info about a given SRS in number of formats (WKT, PROJ.4, etc.)"
---

<h2 class="name">NAME</h2>
<p> gdalsrsinfo &#8211; gdalsrsinfo lists info about a given SRS in number of formats (WKT, PROJ.4, etc.) </p>
<h2>SYNOPSIS</h2>
<pre>
Usage: gdalsrsinfo [options] srs_def
srs_def may be the filename of a dataset supported by GDAL/OGR from which to extract SRS information
OR any of the usual GDAL/OGR forms (complete WKT, PROJ.4, EPSG:n or a file containing the SRS)
Options: 
   [--help-general] [-h]  Show help and exit
   [-p]                   Pretty-print where applicable (e.g. WKT)
   [-V]                   Validate SRS
   [-o out_type]          Output type { default, all, wkt_all, proj4,
                                        wkt, wkt_simple, wkt_noct, wkt_esri,
                                        mapinfo, xml }.fi
</pre>
<h2>DESCRIPTION</h2>
<p> The gdalsrsinfo utility reports information about a given SRS from one of the following: </p>
<dl>
<dt>&bull;</p>
<dd> The filename of a dataset supported by GDAL/OGR which contains SRS information</p>
<dt>&bull;</p>
<dd> Any of the usual GDAL/OGR forms (complete WKT, PROJ.4, EPSG:n or a file containing the SRS)</dl>
<p> Output types: </p>
<dl>
<dt>&bull;</p>
<dd> <code>default</code> proj4 and wkt (default option)</p>
<dt>&bull;</p>
<dd> <code>all</code> all options available</p>
<dt>&bull;</p>
<dd> <code>wkt_all</code> all wkt options available</p>
<dt>&bull;</p>
<dd> <code>proj4</code> PROJ.4 string</p>
<dt>&bull;</p>
<dd> <code>wkt</code> OGC WKT format (full)</p>
<dt>&bull;</p>
<dd> <code>wkt_simple</code> OGC WKT (simplified)</p>
<dt>&bull;</p>
<dd> <code>wkt_noct</code> OGC WKT (without OGC CT params)</p>
<dt>&bull;</p>
<dd> <code>wkt_esri</code> ESRI WKT format</p>
<dt>&bull;</p>
<dd> <code>mapinfo</code> Mapinfo style CoordSys format</p>
<dt>&bull;</p>
<dd> <code>xml</code> XML format (GML based)</dl>
<h2>EXAMPLE</h2>
<pre><code>
$ gdalsrsinfo "EPSG:4326" PROJ .4 : '+proj=longlat +datum=WGS84 +no_defs ' OGC WKT : GEOGCS["WGS 84",
                                                                                            DATUM["WGS_1984",
                                                                                                  SPHEROID["WGS 84", 6378137, 298.257223563,
                                                                                                           AUTHORITY["EPSG", "7030"]],
                                                                                                  AUTHORITY["EPSG", "6326"]],
                                                                                            PRIMEM["Greenwich", 0,
                                                                                                   AUTHORITY["EPSG", "8901"]],
                                                                                            UNIT["degree", 0.0174532925199433,
                                                                                                 AUTHORITY["EPSG", "9122"]],
                                                                                            AUTHORITY["EPSG", "4326"]]
                                                                                         .fi

                                                                                             $ gdalsrsinfo -
    o proj4 osr / data / lcc_esri.prj
</code></pre>
<pre>
$ gdalsrsinfo -o proj4 landsat.tif
PROJ.4 : '+proj=utm +zone=19 +south +datum=WGS84 +units=m +no_defs '
</pre>
<p>$ gdalsrsinfo &#8211; o wkt &#8211; p &#8220;EPSG:32722&#8221; PROJCS[&#8220;WGS 84 / UTM zone 22S&#8221;, GEOGCS[&#8220;WGS 84&#8221;, DATUM[&#8220;WGS_1984&#8221;, SPHEROID[&#8220;WGS 84&#8221;, 6378137, 298.257223563, AUTHORITY[&#8220;EPSG&#8221;, &#8220;7030&#8221;]], AUTHORITY[&#8220;EPSG&#8221;, &#8220;6326&#8221;]], PRIMEM[&#8220;Greenwich&#8221;, 0, AUTHORITY[&#8220;EPSG&#8221;, &#8220;8901&#8221;]], UNIT[&#8220;degree&#8221;, 0.0174532925199433, AUTHORITY[&#8220;EPSG&#8221;, &#8220;9122&#8221;]], AUTHORITY[&#8220;EPSG&#8221;, &#8220;4326&#8221;]], PROJECTION[&#8220;Transverse_Mercator&#8221;], PARAMETER[&#8220;latitude_of_origin&#8221;, 0], PARAMETER[&#8220;central_meridian&#8221;, -51], PARAMETER[&#8220;scale_factor&#8221;, 0.9996], PARAMETER[&#8220;false_easting&#8221;, 500000], PARAMETER[&#8220;false_northing&#8221;, 10000000], UNIT[&#8220;metre&#8221;, 1, AUTHORITY[&#8220;EPSG&#8221;, &#8220;9001&#8221;]], AXIS[&#8220;Easting&#8221;, EAST], AXIS[&#8220;Northing&#8221;, NORTH], AUTHORITY[&#8220;EPSG&#8221;, &#8220;32722&#8221;]]</p>
<pre><code>
$ gdalsrsinfo - o wkt_all "EPSG:4618" OGC WKT : GEOGCS["SAD69",
                                                       DATUM["South_American_Datum_1969",
                                                             SPHEROID["GRS 1967 Modified", 6378160, 298.25,
                                                                      AUTHORITY["EPSG", "7050"]],
                                                             TOWGS84[-57, 1, -41, 0, 0, 0, 0],
                                                             AUTHORITY["EPSG", "6618"]],
                                                       PRIMEM["Greenwich", 0,
                                                              AUTHORITY["EPSG", "8901"]],
                                                       UNIT["degree", 0.0174532925199433,
                                                            AUTHORITY["EPSG", "9122"]],
                                                       AUTHORITY["EPSG", "4618"]] OGC
                                                WKT(simple)
    : GEOGCS["SAD69",
             DATUM["South_American_Datum_1969",
                   SPHEROID["GRS 1967 Modified", 6378160, 298.25],
                   TOWGS84[-57, 1, -41, 0, 0, 0, 0]],
             PRIMEM["Greenwich", 0],
             UNIT["degree", 0.0174532925199433]] OGC WKT(no CT)
    : GEOGCS["SAD69",
             DATUM["South_American_Datum_1969",
                   SPHEROID["GRS 1967 Modified", 6378160, 298.25]],
             PRIMEM["Greenwich", 0],
             UNIT["degree", 0.0174532925199433]] ESRI WKT : GEOGCS["SAD69",
                                                                   DATUM["D_South_American_1969",
                                                                         SPHEROID["GRS_1967_Truncated", 6378160, 298.25]],
                                                                   PRIMEM["Greenwich", 0],
                                                                   UNIT["Degree", 0.017453292519943295]]
</code></pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Etienne Tourigny &lt;etourigny.dev-at-gmail-dot-com&gt; </p>
<h2>Index</h2>
