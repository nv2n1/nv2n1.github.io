---
title: "pnmremap(1)"
name: "pnmremap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmremap/"
description: "pnmremap – replace colors in a PPM image with colors from another set"
---

<h2 class="name">NAME</h2>
<p> pnmremap &#8211; replace colors in a PPM image with colors from another set</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmremap</code> [<code>-floyd</code>|<code>-fs</code>|<code>-nfloyd</code>|<code>-nofs</code>] [<code>-firstisdefault</code>] [<code>-verbose</code>] [<code>-mapfile=</code><i>mapfile</i>] [<code>-missingcolor=</code><i>color</i>] [<i>pnmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> <code>pnmremap</code> replaces the colors in an input image with those from a colormap you specify. Where a color in the input is not in the colormap, you have three choices: 1) choose the closest color from the colormap; 2) choose the first color from the colormap; 3) use a color specified by a command option. (In this latter case, if the color you specify is not in your color map, the output will not necessarily contain only colors from the colormap). </p>
<p> Two reasons to do this are: 1) you want to reduce the number of colors in the input image; and 2) you need to feed the image to something that can handle only certain colors. </p>
<p> To reduce colors, you can generate the colormap with <code>ppmcolormap</code>. Example: </p>
<p> <code>ppmcolormap testimg.ppm 256 &gt;colormap.ppm</code><br />
 <code>ppmremap -map=colormap.ppm testimg.ppm </code><br />
 <code>&gt;reduced_testimg.ppm</code> </p>
<p> To limit colors to a certain set, a typical example is to create an image for posting on the World Wide Web, where different browsers know different colors. But all browsers are supposed to know the 216 &quot;web safe&quot; colors which are essentially all the colors you can represent in a PPM image with a maxval of 5. So you can do this: </p>
<p> <code>ppmcolors 5 &gt;websafe.ppm</code><br />
 <code>ppmremap -map=webafe.ppm testimg.ppm &gt;websafe_testimg.ppm</code> </p>
<p> The output image has the same type and maxval as the map file. </p>
<h2>PARAMETERS</h2>
<p> There is one parameter, which is required: The file specifcation of the input PNM file. </p>
<p> <code>OPTIONS</code></p>
<dl>
<dt><code>-floyd</code></p>
<dd> <code>-fs</code> <code>-nofloyd</code> <code>-nofs</code> These options determine whether Floyd-Steinberg dithering is done. Without Floyd-Steinberg, the selection of output color of a pixel is based on the color of only the corresponding input pixel. With Floyd-Steinberg, multiple input pixels are considered so that the average color of an area tends to stay more the same than without Floyd-Steinberg. For example, if you map an image with a black, gray, gray, and white pixel adjacent, through a map that contains only black and white, it might result in an output of black, black, white, white. Pixel-by-pixel mapping would instead map both the gray pixels to the same color. </p>
<p> <code>-fs</code> is a synomym for <code>-floyd</code>. <code>-nofs</code> is a synonym for <code>-nofloyd</code>. </p>
<p> The default is <code>-nofloyd</code>. </p>
<dt><code>-firstisdefault</code></p>
<dd> This affects what happens with a pixel in the input image whose color is not in the map file. If you specify neither <code>-firstisdefault</code> nor <code>-missingcolor</code>, <code>pnmremap</code> chooses for the output the color in the map which is closest to the color in the input. With <code>-firstisdefault</code>, <code>pnmremap</code> instead uses the first color in the colormap. </p>
<p> If you specify <code>-firstisdefault</code>, the maxval of your input must match the maxval of your colormap. </p>
<dt><code>-missingcolor=</code><i>color</i></p>
<dd> This affects what happens with a pixel in the input image whose color is not in the map file. If you specify neither <code>-firstisdefault</code> nor <code>-missingcolor</code>, <code>pnmremap</code> chooses for the output the color in the map which is closest to the color in the input. With <code>-missingcolor</code>, <code>pnmremap </code> uses <i>color</i>. <i>color</i> need not be in the colormap. </p>
<p> If you specify <code>-missingcolor</code>, the maxval of your input must match the maxval of your colormap. </p>
<dt><code>-verbose</code></p>
<dd> Display helpful messages about the mapping process. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmcolormap/">pnmcolormap</a></code>(1), <code><a href="/docs/linux/man/1-ppmcolors/">ppmcolors</a></code>(1), <code><a href="/docs/linux/man/1-pnmquant/">pnmquant</a></code>(1), <code><a href="/docs/linux/man/1-ppmquantall/">ppmquantall</a></code>(1), <code><a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a></code>(1), <code><a href="/docs/linux/man/1-ppmdither/">ppmdither</a></code>(1), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. Copyright (C) 2001 by Bryan Henderson. </p>
<h2>Index</h2>
