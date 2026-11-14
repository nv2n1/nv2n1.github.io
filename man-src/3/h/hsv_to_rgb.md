---
title: "hsv_to_rgb(3)"
name: "hsv_to_rgb"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hsv_to_rgb/"
description: "hsv_to_rgb, rgb_to_hsv – Converts color values between the HSV and RGB color spaces. Allegro game programming library."
---

<h2>NAME</h2>
<p> hsv_to_rgb, rgb_to_hsv &#8211; Converts color values between the HSV and RGB color spaces. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void hsv_to_rgb(float h, float s, float v, int *r, int *g, int *b);</code> </p>
<p> <code>void rgb_to_hsv(int r, int g, int b, float *h, float *s, float *v);</code></p>
<h2>DESCRIPTION</h2>
<p> Convert color values between the HSV and RGB color spaces. The RGB values range from 0 to 255, hue is from 0 to 360, and saturation and value are from 0 to 1. Example: </p>
<pre><code>
int r, g, b;
float hue, saturation, value;
...
    /* Convert a reddish color to HSV format. */
    rgb_to_hsv(255, 0, 128, &amp;hue, &amp;saturation, &amp;value);

/* Now put our tin foil hat, and verify that. */
hsv_to_rgb(hue, saturation, value, &amp;r, &amp;g, &amp;b);
ASSERT(r == 255);
ASSERT(g == 0);
ASSERT(b == 128);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3) </p>
<h2>Index</h2>
