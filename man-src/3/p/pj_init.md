---
title: "pj_init(3)"
name: "pj_init"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pj_init/"
description: "pj_init – initialize cartographic projection pj_init_plus – initialize cartographic projection pj_fwd – forward cartographic projection pj_inv – inverse cartographic projection pj_transform – trans..."
---

<p>pj_init &#8211; initialize cartographic projection<br />
 pj_init_plus &#8211; initialize cartographic projection<br />
 pj_fwd &#8211; forward cartographic projection<br />
 pj_inv &#8211; inverse cartographic projection<br />
 pj_transform &#8211; transform between coordinate systems<br />
 pj_free &#8211; de-initialize projection</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;proj_api.h&gt;

projPJ pj_init(int argc, char **argv)

projPJ pj_init_plus(const char *defn)

projUV pj_fwd(projUV val, projPJ proj)

projUV pj_inv(projUV val, projPJ proj)

int pj_transform(projPJ src_cs, projPJ dst_cs, long point_count,
int point_offset, double *x, double *y, double *z)

void pj_free(projPJ proj)</code></pre>
<h2>Description</h2>
<p>Procedure <code>pj_init</code> selects and initializes a cartographic projection with its argument control parameters. <code>Argc</code> is the number of elements in the array of control strings <code>argv</code> that each contain individual cartographic control keyword assignments (<tt>+</tt> <code>proj</code> arguments). The list must contain at least the <code>proj=</code><i>projection</i> and Earth&#8217;s radius or elliptical parameters. If the initialization of the projection is successful a valid address is returned otherwise a NULL value. </p>
<p> The <code>pj_init_plus</code> function operates similarly to <code>pj_init</code> but takes a single string containing the definition, with each parameter prefixed with a plus sign. For example &quot;+proj=utm +zone=11 +ellps=WGS84&quot;. </p>
<p> Once initialization is performed either forward or inverse projections can be performed with the returned value of <code>pj_init</code> used as the argument <code>proj</code>. The argument structure <code>projUV</code> values <code>u</code> and <code>v</code> contain respective longitude and latitude or x and y. Latitude and longitude are in radians. If a projection operation fails, both elements of <code>projUV</code> are set to HUGE_VAL (defined in <i>math.h</i>). </p>
<p> <code>Note:</code> all projections have a forward mode, but some do not have an inverse projection. If the projection does not have an inverse the projPJ structure element <i>inv</i> will be NULL. </p>
<p> The <code>pj_transform</code> function may be used to transform points between the two provided coordinate systems. In addition to converting between cartographic projection coordinates and geographic coordinates, this function also takes care of datum shifts if possible between the source and destination coordinate system. Unlike <code>pj_fwd</code> and <code>pj_inv</code> it is also allowable for the coordinate system definitions (<code>PJ *</code>) to be geographic coordinate systems (defined as +proj=latlong). The <code>x</code>, <code>y</code> and <code>z</code> arrays contain the input values of the points, and are replaced with the output values. The <code>point_offset</code> should indicate the spacing the of <code>x,y,z</code> arrays, normally 1. The function returns zero on success, or the error number (also in pj_errno) on failure. </p>
<p> Memory associated with the projection may be freed with <code>pj_free</code>.</p>
<h2>Example</h2>
<p>The following program reads latitude and longitude values in decimal degrees, performs Mercator projection with a Clarke 1866 ellipsoid and a 33&#176; latitude of true scale and prints the projected cartesian values in meters: </p>
<pre><tt>
#include &lt;proj_api.h&gt;
main(int argc, char **argv) {
 char *args[] = { &quot;proj=merc&quot;, &quot;ellps=clrk66&quot;, &quot;lat_ts=33&quot; };
 projUV p;
 projPJ pj;
 if (!(pj = pj_init(3, args)))
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 while (scanf(&quot;%lf %lf&quot;, &amp;p.v, &amp;p.u) == 2) {
 p.u *= DEG_TO_RAD;
 p.v *= DEG_TO_RAD;
 p = pj_fwd(p, pj);
 printf(&quot;%.2f	%.2f
&quot;, p.u, p.v);
 }
 exit(0);
} </tt>
<br></pre>
<h2>Library</h2>
<p>libproj.a &#8211; library of projections and support procedures</p>
<h2>See Also</h2>
<p><code><a rel="nofollow" href="http://proj.osgeo.org/ProjAPI,">http://proj.osgeo.org/ProjAPI,</a> <a href="//www.systutorials.com/docs/linux/man/1U-proj/">proj</a>(1U),</code><br />
 <i>Cartographic Projection Procedures for the UNIX Environment&#8212;A User&#8217;s Manual,</i> (Evenden, 1990, Open-file report 90-284).</p>
<h2>Home Page</h2>
<p><a rel="nofollow" href="http://proj.osgeo.org">http://proj.osgeo.org</a></p>
