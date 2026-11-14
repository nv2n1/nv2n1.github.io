---
title: "clip3d_f(3)"
name: "clip3d_f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clip3d_f/"
description: "clip3d_f – Clips the polygon given in vtx using floating point math, Allegro game programming library."
---

<h2>NAME</h2>
<p> clip3d_f &#8211; Clips the polygon given in vtx using floating point math, Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int clip3d_f(int type, float min_z, float max_z, int vc,</code> <code>const V3D_f *vtx[], V3D_f *vout[], V3D_f *vtmp[], int out[]);</code></p>
<h2>DESCRIPTION</h2>
<p> Clips the polygon given in `vtx&#8217;. The number of vertices is `vc&#8217;, the result goes in `vout&#8217;, and `vtmp&#8217; and `out&#8217; are needed for internal purposes. The pointers in `vtx&#8217;, `vout&#8217; and `vtmp&#8217; must point to valid V3D_f structures. </p>
<p> As additional vertices may appear in the process of clipping, so the size of `vout&#8217;, `vtmp&#8217; and `out&#8217; should be at least vc * (1.5 ^ n), where `n&#8217; is the number of clipping planes (5 or 6), and `^&#8217; denotes &quot;to the power of&quot;. </p>
<p> The frustum (viewing volume) is defined by -z&lt;x&lt;z, -z&lt;y&lt;z, 0&lt;min_z&lt;z&lt;max_z. If max_z&lt;=min_z, the z&lt;max_z clipping is not done. As you can see, clipping is done in the camera space, with perspective in mind, so this routine should be called after you apply the camera matrix, but before the perspective projection. The routine will correctly interpolate u, v, and c in the vertex structure. However, no provision is made for high/truecolor GCOL.</p>
<h2>RETURN VALUE</h2>
<p> Returns the number of vertices after clipping is done. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-clip3d/">clip3d</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3) </p>
<h2>Index</h2>
