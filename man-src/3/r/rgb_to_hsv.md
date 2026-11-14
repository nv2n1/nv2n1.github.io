---
title: "rgb_to_hsv(3)"
name: "rgb_to_hsv"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rgb_to_hsv/"
description: "hsv_to_rgb, rgb_to_hsv – Converts color values between the HSV and RGB color spaces. Allegro game programming library."
---

<p>hsv_to_rgb, rgb_to_hsv &#8211; Converts color values between the HSV and RGB color spaces. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void hsv_to_rgb(float h, float s, float v, int *r, int *g, int *b);
void rgb_to_hsv(int r, int g, int b, float *h, float *s, float *v);</code></pre>
<h2>Description</h2>
<p>Convert color values between the HSV and RGB color spaces. The RGB values range from 0 to 255, hue is from 0 to 360, and saturation and value are from 0 to 1. Example: </p>
<pre><code>int r, g, b;
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
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3) </p>
