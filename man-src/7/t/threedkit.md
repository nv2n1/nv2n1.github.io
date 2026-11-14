---
title: "threedkit(7)"
name: "threedkit"
section: "7"
letter: "t"
url: "/docs/linux/man/7-threedkit/"
description: "threedkit – a set of functions for 3D support."
---

<p>threedkit &#8211; a set of functions for 3D support. </p>
<h2>Description</h2>
<p>The 3dkit consists mainly of the following triangle functions <code><a href="/docs/linux/man/3-gl_striangle/">gl_striangle</a></code>(3), <code><a href="/docs/linux/man/3-gl_swtriangle/">gl_swtriangle</a></code>(3), <code><a href="/docs/linux/man/3-gl_triangle/">gl_triangle</a></code>(3), <code><a href="/docs/linux/man/3-gl_trigetcolorlookup/">gl_trigetcolorlookup</a></code>(3), <code><a href="/docs/linux/man/3-gl_trisetcolorlookup/">gl_trisetcolorlookup</a></code>(3), <code><a href="/docs/linux/man/3-gl_trisetdrawpoint/">gl_trisetdrawpoint</a></code>(3), <code><a href="/docs/linux/man/3-gl_wtriangle/">gl_wtriangle</a></code>(3). Beware, these functions are not a direct part of the svgalib library. Instead their source is part of svgalib and can be found in the <i>threeDkit/</i> subdirectory of the original svgalib distribution. However, it is not installed in the system by default, s.t. it is unclear where you can find it if your svgalib was installed by some linux distribution. In case of any such problem, simply get an svgalib distribution from the net. You even don&#8217;t need to install it. Just <code>make</code> in the <i>threeDkit/</i> subdirectory. As of this writing, <i>svgalib-1.2.12.tar.gz</i> is the latest version and can be retrieved by ftp from <i>sunsite.unc.edu</i> at <i>/pub/Linux/libs/graphics</i> and <i>tsx-11.mit.edu</i> at <i>/pub/linux/sources/libs</i> which will most probably be mirrored by a site close to you. The functions are defined in the <i>tri.o</i> and <i>triangl.o</i> files (or their resp. sources) which you must link to your program. </p>
<h2>Explanation On 3Dkit.C</h2>
<p>This is main engine for 3D rendering. </p>
<p> Program flow: </p>
<dl>
<dt><code>1.</code></p>
<dd>The function called from outside of <i>3dkit.c</i> is <code>TD_drawsolid</code>. This first calculates the rotation matrix from the camera rotation angles (see below for more details). It then allocates memory for the temporary array</p>
<dt><code>emp</code></p>
<dd>for holding temporary coords in subsequently called functions. It also sorts the surfaces from furthest to closest; according to the distance of the centre grid-point of each surface from the camera. </p>
<p> It also establishes whether <code>ROTATE_OBJECT</code> option is on and zero&#8217;s the camera position if so &#8212; this is for displaying the object at the screen centre like in a 3D CAD package, as apposed to virtual reality where the object can be anywhere and the actual camera position can move. </p>
<p> In the case of <code>ROTATE_OBJECT</code> being on, although the camera position is zero, some distance has to be placed between the camera and the object (or else it would appear to be infinitely large on the screen). This is done using the variable <i>s_cam</i> which is initialized to <i>distance</i> which is set by the calling application. It then loops through each surface (ordering them in the way they were just sorted &#8212; i.e. according to <i>sortarray</i> indexing) and calls one of five graphic routines to write the 3D surface to the hardware. </p>
<dt><code>2.</code></p>
<dd>Assume that <code>TD_drawsolid</code> then calls <code>TD_drawmesh</code>. Here, each surface grid point is first <code>TD_translate</code>&#8216;d into a 2D screen point and stored in the <i>temp</i> array. There are obviously w(idth)*h(eight) points in the grid. </p>
<p> Following, each line from the 2D temp array is drawn on the screen. To draw the surface, the corner wishbone (two lines) from each grid square is drawn while advancing across and the down. After completing the scan, the furthest two edges of the surface must then be filled in, vis.:<br />
&nbsp;<wbr>_&nbsp;<wbr>_&nbsp;<wbr>_&nbsp;<wbr>_&nbsp;<wbr>_&nbsp;<wbr>_<br />
 |_|_|_|_|_|_<br />
 |_|_|_|_|_|_<br />
 |_|_|_|_|_|_<br />
 |_|_|_|_|_|_<br />
 |_|_|_|_|_|_<br />
 | | | | | | </p>
<p> To understand the object rotation, a knowledge of matrix multiplication is required. I once derived a camera rotation before I learned matrix computation. It amounted to the same thing, but was unnecessarily complicated to optimise. </p>
<dt><code>3.</code></p>
<dd><code>TD_translate</code> called from <code>TD_drawmesh</code> (and others) converts from the 3D grid point coordinate to the 2D screen coordinate using: <code>(a)</code> the three camera position coordinates, (or the single camera distance value, <i>s_cam</i>, if <code>ROTATE_OBJECT</code> is set), and <code>(b)</code> the three camera rotation angles. However, the three camera rotation angles have already been converted into a rotation matrix when <code>TD_calc_rotation_matrix</code> was called by <code>TD_draw_solid</code>. </p>
<p> To convert from a 3D coordinate to a 2D screen coordinate, the camera position (or more correctly, the position of the object from the camera) must first be added to each of the 3D grid coordinates. If the user has chosen to use 32 bit values for the discription of the surface, then these must be right shifted to the same size as the 16 bit case. </p>
<p> <i>x</i>, <i>y</i> and <i>z</i> now hold the 3D position of the object relative to the camera centre (or in these terms, the centre of the video screen <code>RIGHT ON</code> the screen). The vector <code>[</code><i>x y z</i><code>]</code> must now be multiplied by the rotation matrix. The <i>xt</i> value must also have the camera distance, <i>s_cam</i>, added to it in case the <code>ROTATE_CAMERA</code> is set (in which case <i>x_cam</i>, <i>y_cam</i> and <i>z_cam</i> (the camera position) will be zero and instead <i>s_cam</i> will have a value to provide the necessary object-camera distance). A test is also made as to whether this value is zero or negative. In the case, the point is too close to the camera, or behind the camera, and must not be drawn. </p>
<p> After the multiplication, the resulting vector <code>[</code><i>xt yt zt</i><code>]</code> has been rotated to be aligned with screen. The vector is now adjusted for perspective by dividing the <i>yt</i> and <i>zt</i> values (horizontal and vertical respectively) by the <i>xt</i> value (into the screen). Division is done by <code>muldiv64</code> because the intermediate product is larger than 32 bits. <i>xscale</i> and <i>yscale</i> are factors that scale the image to size. <i>posx</i> and <i>posy</i> is just the centre of the screen, or more precisely: </p>
<p> The exact position of the pinhole camera viewing the object. </p>
<dt><code>4.</code></p>
<dd><code>TD_calc_rotation_matrix</code> calculates the nine entries of the 3 by 3 matrix used in <code>TD_translate</code>. In order that only integer arithmetic is performed, these values are stored and used as integers. Since this matrix&#8217;s entries are always between -1 and +1, they have to be integer left shifted to give them accuracy. <code>TD_MULCONSTANT</code> scales them to sufficient bits of accuracy before they are converted to integers. </p>
<p> This also means that results (of multiplications with them) have to be scaled down by the same amount. This scaling is inherent in the final multiplication and division (<code>muldiv64</code>) done in the <code>TD_translate</code> function, so an extra division is not consumed. </p>
<p> The rotation matrix effectively rotates the vector by the Eulerian angles <i>alpha</i>, <i>beta</i> and <i>gamma</i>. These angles represent successive rotations about each of the 3D axes. You can test which angles do what by looking at the calling application. Their precise definitions are not all that important since you can get the keyboard to do the right thing with a little trial and error. </p>
</dl>
<p> Intrisics of drawing non-transparent surfaces&#8230; </p>
<p> to be continued ?!</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-vgagl/">vgagl</a></code>(7), <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/3-gl_striangle/">gl_striangle</a></code>(3), <code><a href="/docs/linux/man/3-gl_swtriangle/">gl_swtriangle</a></code>(3), <code><a href="/docs/linux/man/3-gl_triangle/">gl_triangle</a></code>(3), <code><a href="/docs/linux/man/3-gl_trigetcolorlookup/">gl_trigetcolorlookup</a></code>(3), <code><a href="/docs/linux/man/3-gl_trisetcolorlookup/">gl_trisetcolorlookup</a></code>(3), <code><a href="/docs/linux/man/3-gl_trisetdrawpoint/">gl_trisetdrawpoint</a></code>(3), <code><a href="/docs/linux/man/3-gl_wtriangle/">gl_wtriangle</a></code>(3), <code><a href="/docs/linux/man/6-plane/">plane</a></code>(6), <code><a href="/docs/linux/man/6-wrapdemo/">wrapdemo</a></code>(6). </p>
<h2>Author</h2>
<p>This manual page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The demos, the initial documentation and the whole threedkit stuff was done by Paul Sheer &lt;psheer [at] icon.co.za&gt;. </p>
<p> Paper mail:</p>
<dl>
<dd>Paul Sheer<br />
 P O BOX 890507<br />
 Lyndhurst<br />
 Johannesburg 2106<br />
 South Africa</dl>
<p> Donations (by check or postal order) will be appreciated and will encourage further development of this software. However this is strictly on a voluntary basis where this software falls under the GNU LIBRARY GENERAL PUBLIC LICENSE.</p>
