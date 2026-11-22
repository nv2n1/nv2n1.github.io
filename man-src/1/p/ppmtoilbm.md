---

title: "ppmtoilbm(1)"
name: "ppmtoilbm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoilbm/"
description: "ppmtoilbm – convert a portable pixmap into an ILBM file"
---

<p> ppmtoilbm &#8211; convert a portable pixmap into an ILBM file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoilbm</code> [<code>-maxplanes</code>|<code>-mp</code> <i>N</i>] [<code>-fixplanes</code>|<code>-fp</code> <i>N</i>] [<code>-ham6</code>|<code>-ham8</code>] [<code>-dcbits</code>|<code>-dcplanes</code>r<code>g</code>b<code>]</code> [<code>-normal</code>|<code>-hamif</code>|<code>-hamforce</code>|<code>-24if</code>|<code>-24force</code>| -dcif<code>|</code>-dcforce<code>|</code>-cmaponly<code>]</code> [<code>-ecs</code>|<code>-aga</code>] [<code>-compress</code>|<code>-nocompress</code>] [<code>-cmethod</code> <i>type</i>] [<code>-map</code>ppmfile<code>]</code> [<code>-savemem</code>] [<code>ppmfile</code>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces an ILBM file as output. Supported ILBM types are:</p>
<dl>
<dt>Normal ILBMs with 1-16 planes.</dt>
<dd>
</dd><dt>Amiga HAM with 3-16 planes.</dt>
<dd>
</dd><dt>24 bit.</dt>
<dd>
</dd><dt>Color map (BMHD + CMAP chunk only, nPlanes = 0).</dt>
<dd>
</dd><dt>Unofficial direct color.</dt>
<dd> 1-16 planes for each color component.</dd>
<dt>Chunks written:</dt>
<dd> BMHD, CMAP, CAMG (only for HAM), BODY (not for colormap files) unofficial DCOL chunk for direct color ILBM</dd></dl>
<h2>OPTIONS</h2>
<p> Options marked with (*) can be prefixed with a &quot;no&quot;, e.g. &quot;-nohamif&quot;. All options can be abbreviated to their shortest unique prefix.</p>
<dl>
<dt><code>-maxplanes | -mp n</code></dt>
<dd> (default 5, minimum 1, maximum 16) Maximum planes to write in a normal ILBM. If the pixmap does not fit into &lt;n&gt; planes, ppmtoilbm writes a HAM file (if -hamif is used), a 24bit file (if -24if is used) or a direct color file (if -dcif is used) or aborts with an error.</dd>
<dt><code>-fixplanes | -fp n</code></dt>
<dd> (min 1, max 16) If a normal ILBM is written, it will have exactly &lt;n&gt; planes.</dd>
<dt><code>-hambits | -hamplanes n</code></dt>
<dd> (default 6, min 3, max 16) Select number of planes for HAM picture. The current Amiga hardware supports 6 and 8 planes, so for now you should only use this values.</dd>
<dt><code>-normal (default)</code></dt>
<dd> Turns off -hamif/-24if/-dcif, -hamforce/-24force/-dcforce and -cmaponly. Also sets compression type to byterun1.</dd>
<dt><code>-hamif (*)</code></dt>
<dd>
</dd><dt><code>-24if (*)</code></dt>
<dd>
</dd><dt><code>-dcif (*)</code></dt>
<dd> Write a HAM/24bit/direct color file if the pixmap does not fit into &lt;maxplanes&gt; planes.</dd>
<dt><code>-hamforce (*)</code></dt>
<dd>
</dd><dt><code>-24force (*)</code></dt>
<dd>
</dd><dt><code>-dcforce (*)</code></dt>
<dd> Write a HAM/24bit/direct color file.</dd>
<dt><code>-dcbits | -dcplanes r g b</code></dt>
<dd> (default 5, min 1, max 16). Select number of bits for red, green &amp; blue in a direct color ILBM.</dd>
<dt><code>-ecs (default)</code></dt>
<dd> Shortcut for: -hamplanes 6 -maxplanes 5</dd>
<dt><code>-aga</code></dt>
<dd>
</dd><dt><code>Shortcut for: -hamplanes 8 -maxplanes 8</code></dt>
<dd>
</dd><dt><code>-ham6</code></dt>
<dd>
</dd><dt><code>Shortcut for: -hamplanes 6 -hamforce</code></dt>
<dd>
</dd><dt><code>-ham8</code></dt>
<dd> Shortcut for: -hamplanes 8 -hamforce</dd>
<dt><code>-compress (*) (default)</code></dt>
<dd>
</dd><dt><code>-cmethod none|byterun1</code></dt>
<dd> Compress the BODY chunk. The default compression method is byterun1. Compression requires building the ILBM image in memory; turning compression off allows stream-writing of the image, but the resulting file will usually be 30% to 50% larger. Another alternative is the -savemem option, this will keep memory requirements for compression at a minimum, but is very slow.</dd>
<dt><code>-map ppmfile</code></dt>
<dd> Write a normal ILBM using the colors in &lt;ppmfile&gt; as the colormap. The colormap file also determines the number of planes, a -maxplanes or -fixplanes option is ignored.</dd>
<dt><code>-cmaponly</code></dt>
<dd> Write a colormap file: only BMHD and CMAP chunks, no BODY chunk, nPlanes = 0.</dd>
<dt><code>-savemem</code></dt>
<dd> See the -compress option.</dd></dl>
<h2>BUGS</h2>
<p> HAM pictures will always get a grayscale colormap; a real color selection algorithm might give better results. On the other hand, this allows row-by-row operation on HAM images, and all HAM images of the same depth (no. of planes) share a common colormap, which is useful for building HAM animations.</p>
<h2>REFERENCES</h2>
<p> Amiga ROM Kernel Reference Manual &#8211; Devices (3rd Ed.)<br/>
 Addison Wesley, ISBN 0-201-56775-X</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-ppm/">ppm</a>(5), <a href="/docs/linux/man/1-ilbmtoppm/">ilbmtoppm</a>(1)</p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1989 by Jef Poskanzer.<br/>
 Modified October 1993 by Ingo Wilken (Ingo.Wilken [at] informatik.uni-oldenburg.de) </p>
