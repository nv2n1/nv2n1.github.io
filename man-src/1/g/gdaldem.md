---
title: "gdaldem(1)"
name: "gdaldem"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdaldem/"
description: "gdaldem – gdaldem Tools to analyze and visualize DEMs. (since GDAL 1.7.0)"
---

<h2 class="name">NAME</h2>
<p> gdaldem &#8211; gdaldem Tools to analyze and visualize DEMs. (since GDAL 1.7.0) </p>
<h2>SYNOPSIS</h2>
<pre><code>
- To generate a shaded relief map from any GDAL - supported elevation raster:
                                                                          gdaldem hillshade input_dem output_hillshade
                                                                                  [-z ZFactor(default = 1)][-s scale * (default = 1)] "
                                                                                      [-az Azimuth(default = 315)][-alt Altitude(default = 45)]
                                                                                      [-alg ZevenbergenThorne][-combined]
                                                                                      [-compute_edges][-b Band(default = 1)][-of format][-co "NAME=VALUE"] *
                                                                              [-q] -
                                                                          To generate a slope map from any GDAL - supported elevation
                                                                      raster:
                                                                          gdaldem slope input_dem output_slope_map "
                                                                                  [-p use percent slope(default = degrees)][-s scale * (default = 1)]
                                                                                  [-alg ZevenbergenThorne]
                                                                                  [-compute_edges][-b Band(default = 1)][-of format][-co "NAME=VALUE"] *
                                                                              [-q] -
                                                                          To generate an aspect map from any GDAL - supported elevation raster Outputs a 32 - bit float raster with pixel values from 0 - 360 indicating
                                                                     azimuth:
                                                                         gdaldem aspect input_dem output_aspect_map "
                                                                                 [-trigonometric][-zero_for_flat]
                                                                                 [-alg ZevenbergenThorne]
                                                                                 [-compute_edges][-b Band(default = 1)][-of format][-co "NAME=VALUE"] *
                                                                             [-q] -
                                                                         To generate a color relief map from any GDAL - supported elevation raster gdaldem color - relief input_dem color_text_file output_color_relief_map[-alpha][-exact_color_entry | -nearest_color_entry][-b Band(default = 1)][-of format][-co "NAME=VALUE"] *
                                                                                                                                                                       [-q] where color_text_file contains lines of the format "elevation_value red green blue"

                                                                         - To generate a Terrain Ruggedness Index(TRI)
map from any GDAL - supported elevation raster : gdaldem TRI input_dem output_TRI_map[-compute_edges][-b Band(default = 1)][-of format][-q]

                                                 -
                                                 To generate a Topographic Position Index(TPI)
map from any GDAL - supported elevation raster : gdaldem TPI input_dem output_TPI_map[-compute_edges][-b Band(default = 1)][-of format][-q]

                                                 -
                                                 To generate a roughness map from any GDAL - supported elevation raster : gdaldem roughness input_dem output_roughness_map[-compute_edges][-b Band(default = 1)][-of format][-q] Notes : gdaldem generally assumes that x,
    y and z units are identical.If x(east - west) and y(north - south) units are identical, but z(elevation)
units are different, the scale(-s) option can be used to set the ratio of vertical units to horizontal.For LatLong projections near the equator, where units of latitude and units of longitude are similar, elevation(z) units can be converted to be compatible by using scale = 370400(if elevation is in feet) or scale = 111120(if elevation is in meters).For locations not near the equator, it would be best to reproject your grid using gdalwarp before using gdaldem..fi
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility has 7 different modes :</p>
<dl>
<dt><code>hillshade</code></p>
<dd> to generate a shaded relief map from any GDAL-supported elevation raster</p>
<dt><code>slope</code></p>
<dd> to generate a slope map from any GDAL-supported elevation raster</p>
<dt><code>aspect</code></p>
<dd> to generate an aspect map from any GDAL-supported elevation raster</p>
<dt><code>color-relief</code></p>
<dd> to generate a color relief map from any GDAL-supported elevation raster</p>
<dt><code>TRI</code></p>
<dd> to generate a map of Terrain Ruggedness Index from any GDAL-supported elevation raster</p>
<dt><code>TPI</code></p>
<dd> to generate a map of Topographic Position Index from any GDAL-supported elevation raster</p>
<dt><code>roughness</code></p>
<dd> to generate a map of roughness from any GDAL-supported elevation raster</dl>
<p> The following general options are available :</p>
<dl>
<dt><i>input_dem</i>:</p>
<dd> The input DEM raster to be processed</p>
<dt><i>output_xxx_map</i>:</p>
<dd> The output raster produced</p>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Select the output format. The default is GeoTIFF (GTiff). Use the short format name.</p>
<dt><code>-compute_edges</code>:</p>
<dd> (GDAL &gt;= 1.8.0) Do the computation at raster edges and near nodata values</p>
<dt><code>-alg</code> <i>ZevenbergenThorne</i>:</p>
<dd> (GDAL &gt;= 1.8.0) Use Zevenbergen &amp; Thorne formula, instead of Horn&#8217;s formula, to compute slope &amp; aspect. The litterature suggests Zevenbergen &amp; Thorne to be more suited to smooth landscapes, whereas Horn&#8217;s formula to perform better on rougher terrain.</p>
<dt><code>-b</code> <i>band</i>:</p>
<dd> Select an input <i>band</i> to be processed. Bands are numbered from 1.</p>
<dt><code>-co</code> <i>&#8216;NAME=VALUE&#8217;</i>:</p>
<dd> Passes a creation option to the output format driver. Multiple <code>-co</code> options may be listed. See format specific documentation for legal creation options for each format.</p>
<dt><code>-q</code>:</p>
<dd> Suppress progress monitor and other non-error output.</dl>
<p> For all algorithms, except color-relief, a nodata value in the target dataset will be emitted if at least one pixel set to the nodata value is found in the 3&#215;3 window centered around each source pixel. The consequence is that there will be a 1-pixel border around each image set with nodata value. From GDAL 1.8.0, if -compute_edges is specified, gdaldem will compute values at image edges or if a nodata value is found in the 3&#215;3 window, by interpolating missing values.</p>
<h2>Modes</h2>
<h3>hillshade</h3>
<p> This command outputs an 8-bit raster with a nice shaded relief effect. It’s very useful for visualizing the terrain. You can optionally specify the azimuth and altitude of the light source, a vertical exaggeration factor and a scaling factor to account for differences between vertical and horizontal units. </p>
<p> The value 0 is used as the output nodata value. </p>
<p> The following specific options are available :</p>
<dl>
<dt><code>-z</code> <i>zFactor</i>:</p>
<dd> vertical exaggeration used to pre-multiply the elevations</p>
<dt><code>-s</code> <i>scale</i>:</p>
<dd> ratio of vertical units to horizontal. If the horizontal unit of the source DEM is degrees (e.g Lat/Long WGS84 projection), you can use scale=111120 if the vertical units are meters (or scale=370400 if they are in feet)</p>
<dt><code>-az</code> <i>azimuth</i>:</p>
<dd> azimuth of the light, in degrees. 0 if it comes from the top of the raster, 90 from the east, &#8230; The default value, 315, should rarely be changed as it is the value generally used to generate shaded maps.</p>
<dt><code>-alt</code> <i>altitude</i>:</p>
<dd> altitude of the light, in degrees. 90 if the light comes from above the DEM, 0 if it is raking light.</p>
<dt><code>-combined</code> <i>combined shading</i>:</p>
<dd> (starting with GDAL 1.10) a combination of slope and oblique shading.</dl>
<h3>slope</h3>
<p> This command will take a DEM raster and output a 32-bit float raster with slope values. You have the option of specifying the type of slope value you want: degrees or percent slope. In cases where the horizontal units differ from the vertical units, you can also supply a scaling factor. </p>
<p> The value -9999 is used as the output nodata value. </p>
<p> The following specific options are available :</p>
<dl>
<dt><code>-p</code> :</p>
<dd> if specified, the slope will be expressed as percent slope. Otherwise, it is expressed as degrees</p>
<dt><code>-s</code> <i>scale</i>:</p>
<dd> ratio of vertical units to horizontal. If the horizontal unit of the source DEM is degrees (e.g Lat/Long WGS84 projection), you can use scale=111120 if the vertical units are meters (or scale=370400 if they are in feet)</dl>
<h3>aspect</h3>
<p> This command outputs a 32-bit float raster with values between 0° and 360° representing the azimuth that slopes are facing. The definition of the azimuth is such that : 0° means that the slope is facing the North, 90° it&#8217;s facing the East, 180° it&#8217;s facing the South and 270° it&#8217;s facing the West (provided that the top of your input raster is north oriented). The aspect value -9999 is used as the nodata value to indicate undefined aspect in flat areas with slope=0. </p>
<p> The following specifics options are available :</p>
<dl>
<dt><code>-trigonometric</code>:</p>
<dd> return trigonometric angle instead of azimuth. Thus 0° means East, 90° North, 180° West, 270° South</p>
<dt><code>-zero_for_flat</code>:</p>
<dd> return 0 for flat areas with slope=0, instead of -9999</dl>
<p> By using those 2 options, the aspect returned by gdaldem aspect should be identical to the one of GRASS r.slope.aspect. Otherwise, it&#8217;s identical to the one of Matthew Perry&#8217;s aspect.cpp utility.</p>
<h3>color-relief</h3>
<p> This command outputs a 3-band (RGB) or 4-band (RGBA) raster with values are computed from the elevation and a text-based color configuration file, containing the association between various elevation values and the corresponding wished color. By default, the colors between the given elevation values are blended smoothly and the result is a nice colorized DEM. The -exact_color_entry or -nearest_color_entry options can be used to avoid that linear interpolation for values that don&#8217;t match an index of the color configuration file. </p>
<p> The following specifics options are available :</p>
<dl>
<dt><i>color_text_file</i>:</p>
<dd> text-based color configuration file</p>
<dt><code>-alpha</code> :</p>
<dd> add an alpha channel to the output raster</p>
<dt><code>-exact_color_entry</code> :</p>
<dd> use strict matching when searching in the color configuration file. If none matching color entry is found, the &#8216;0,0,0,0&#8217; RGBA quadruplet will be used</p>
<dt><code>-nearest_color_entry</code> :</p>
<dd> use the RGBA quadruplet corresponding to the closest entry in the color configuration file.</dl>
<p> The color-relief mode is the only mode that supports VRT as output format. In that case, it will translate the color configuration file into appropriate LUT elements. Note that elevations specified as percentage will be translated as absolute values, which must be taken into account when the statistics of the source raster differ from the one that was used when building the VRT. </p>
<p> The text-based color configuration file generally contains 4 columns per line : the elevation value and the corresponding Red, Green, Blue component (between 0 and 255). The elevation value can be any floating point value, or the <i>nv</i> keyword for the nodata value.. The elevation can also be expressed as a percentage : 0% being the minimum value found in the raster, 100% the maximum value. </p>
<p> An extra column can be optionally added for the alpha component. If it is not specified, full opacity (255) is assumed. </p>
<p> Various field separators are accepted : comma, tabulation, spaces, &#8216;:&#8217;. </p>
<p> Common colors used by GRASS can also be specified by using their name, instead of the RGB triplet. The supported list is : white, black, red, green, blue, yellow, magenta, cyan, aqua, grey/gray, orange, brown, purple/violet and indigo. </p>
<p> Since GDAL 1.8.0, GMT .cpt palette files are also supported (COLOR_MODEL = RGB only). </p>
<p> Note: the syntax of the color configuration file is derived from the one supported by GRASS r.colors utility. ESRI HDR color table files (.clr) also match that syntax. The alpha component and the support of tab and comma as separators are GDAL specific extensions. </p>
<p> For example : </p>
<pre>
3500   white
2500   235:220:175
50%   190 185 135
700    240 250 150
0      50  180  50
nv     0   0   0   0 
</pre>
<h3>TRI</h3>
<p> This command outputs a single-band raster with values computed from the elevation. TRI stands for Terrain Ruggedness Index, which is defined as the mean difference between a central pixel and its surrounding cells (see Wilson et al 2007, Marine Geodesy 30:3-35). </p>
<p> The value -9999 is used as the output nodata value. </p>
<p> There are no specific options.</p>
<h3>TPI</h3>
<p> This command outputs a single-band raster with values computed from the elevation. TPI stands for Topographic Position Index, which is defined as the difference between a central pixel and the mean of its surrounding cells (see Wilson et al 2007, Marine Geodesy 30:3-35). </p>
<p> The value -9999 is used as the output nodata value. </p>
<p> There are no specific options.</p>
<h3>roughness</h3>
<p> This command outputs a single-band raster with values computed from the elevation. Roughness is the largest inter-cell difference of a central pixel and its surrounding cell, as defined in Wilson et al (2007, Marine Geodesy 30:3-35). </p>
<p> The value -9999 is used as the output nodata value. </p>
<p> There are no specific options.</p>
<h2>AUTHORS</h2>
<p> Matthew Perry perrygeo [at] gmail.com, Even Rouault even.rouault [at] mines-paris.org, Howard Butler hobu.inc [at] gmail.com, Chris Yesson chris.yesson [at] ioz.ac.uk </p>
<p> Derived from code by Michael Shapiro, Olga Waupotitsch, Marjorie Larson, Jim Westervelt : U.S. Army CERL, 1993. GRASS 4.1 Reference Manual. U.S. Army Corps of Engineers, Construction Engineering Research Laboratories, Champaign, Illinois, 1-425.</p>
<h2>See also</h2>
<p> Documentation of related GRASS utilities : </p>
<p> <a rel="nofollow" href="http://grass.osgeo.org/grass64/manuals/html64_user/r.slope.aspect.html">http://grass.osgeo.org/grass64/manuals/html64_user/r.slope.aspect.html</a> </p>
<p> <a rel="nofollow" href="http://grass.osgeo.org/grass64/manuals/html64_user/r.shaded.relief.html">http://grass.osgeo.org/grass64/manuals/html64_user/r.shaded.relief.html</a> </p>
<p> <a rel="nofollow" href="http://grass.osgeo.org/grass64/manuals/html64_user/r.colors.html">http://grass.osgeo.org/grass64/manuals/html64_user/r.colors.html</a> </p>
<h2>Index</h2>
