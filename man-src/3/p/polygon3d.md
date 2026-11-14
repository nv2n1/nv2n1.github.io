---
title: "polygon3d(3)"
name: "polygon3d"
section: "3"
letter: "p"
url: "/docs/linux/man/3-polygon3d/"
description: "polygon3d, polygon3d_f – Draws a 3d polygon onto the specified bitmap. Allegro game programming library."
---

<p>polygon3d, polygon3d_f &#8211; Draws a 3d polygon onto the specified bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void polygon3d(BITMAP *bmp, int type, BITMAP *texture, int vc, V3D *vtx[]);
void polygon3d_f(BITMAP *bmp, int type, BITMAP *texture, int vc, V3D_f *vtx[]);</code></pre>
<h2>Description</h2>
<p>Draw 3d polygons onto the specified bitmap, using the specified rendering mode. Unlike the regular polygon() function, these routines don&#8217;t support concave or self-intersecting shapes, and they can&#8217;t draw onto mode-X screen bitmaps (if you want to write 3d code in mode-X, draw onto a memory bitmap and then blit to the screen). The width and height of the texture bitmap must be powers of two, but can be different, eg. a 64&#215;16 texture is fine, but a 17&#215;3 one is not. The vertex count parameter (vc) should be followed by an array containing the appropriate number of pointers to vertex structures: polygon3d() uses the fixed point V3D structure, while polygon3d_f() uses the floating point V3D_f structure. These are defined as: </p>
<pre> typedef struct V3D
 {
 fixed x, y, z; - position
 fixed u, v; - texture map coordinates
 int c; - color
 } V3D;
 
 typedef struct V3D_f
 {
 float x, y, z; - position
 float u, v; - texture map coordinates
 int c; - color
 } V3D_f;</pre>
<p>How the vertex data is used depends on the rendering mode: The `x&#8217; and `y&#8217; values specify the position of the vertex in 2d screen coordinates. The `z&#8217; value is only required when doing perspective correct texture mapping, and specifies the depth of the point in 3d world coordinates. The `u&#8217; and `v&#8217; coordinates are only required when doing texture mapping, and specify a point on the texture plane to be mapped on to this vertex. The texture plane is an infinite plane with the texture bitmap tiled across it. Each vertex in the polygon has a corresponding vertex on the texture plane, and the image of the resulting polygon in the texture plane will be mapped on to the polygon on the screen. We refer to pixels in the texture plane as texels. Each texel is a block, not just a point, and whole numbers for u and v refer to the top-left corner of a texel. This has a few implications. If you want to draw a rectangular polygon and map a texture sized 32&#215;32 on to it, you would use the texture coordinates (0,0), (0,32), (32,32) and (32,0), assuming the vertices are specified in anticlockwise order. The texture will then be mapped perfectly on to the polygon. However, note that when we set u=32, the last column of texels seen on the screen is the one at u=31, and the same goes for v. This is because the coordinates refer to the top-left corner of the texels. In effect, texture coordinates at the right and bottom on the texture plane are exclusive. There is another interesting point here. If you have two polygons side by side sharing two vertices (like the two parts of folded piece of cardboard), and you want to map a texture across them seamlessly, the values of u and v on the vertices at the join will be the same for both polygons. For example, if they are both rectangular, one polygon may use (0,0), (0,32), (32,32) and (32,0), and the other may use (32,0), (32,32), (64,32), (64,0). This would create a seamless join. Of course you can specify fractional numbers for u and v to indicate a point part-way across a texel. In addition, since the texture plane is infinite, you can specify larger values than the size of the texture. This can be used to tile the texture several times across the polygon. The `c&#8217; value specifies the vertex color, and is interpreted differently by various rendering modes. Read the beginning of chapter &quot;Polygon rendering&quot; for a list of rendering types you can use with this function. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-triangle3d/">triangle3d</a></code>(3), <code><a href="/docs/linux/man/3-quad3d/">quad3d</a></code>(3), <code><a href="/docs/linux/man/3-polygon/">polygon</a></code>(3), <code><a href="/docs/linux/man/3-clip3d/">clip3d</a></code>(3), <code><a href="/docs/linux/man/3-cpu_capabilities/">cpu_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3) </p>
