---
title: "pamperspective(1)"
name: "pamperspective"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamperspective/"
description: "pamperspective – a reverse scanline renderer for Netpbm images"
---

<h2 class="name">NAME</h2>
<p> pamperspective &#8211; a reverse scanline renderer for Netpbm images</p>
<h2>SYNOPSIS</h2>
<pre><code>
pamperspective
    [--bottom_margin = num]
    [--detail = num]
    [--frame_include = bool]
    [--height = num]
    [--include = [ x1, y1; x2, y2;... ]]
    [--input_system = spec]
    [--input_unit = spec]
    [--interpolation = spec]
    [--left_margin = num]
    [--margin = num]
    [--output_system = spec]
    [--proportion = spec]
    [--ratio = num]
    [--right_margin = num]
    [--top_margin = num]
    [--width = num]{
        {upper_left_x upper_left_y upper_right_x upper_right_y
             lower_left_x lower_left_y lower_right_x lower_right_y} |
        {
            {--upper_left_x | --ulx} = upper_left_x{--upper_left_y | --uly} = upper_left_y{--upper_right_x | --urx} = upper_right_x{--upper_right_y | --ury} = upper_right_y{--lower_left_x | --llx} = lower_left_x{--lower_left_y | --lly} = lower_left_y{--lower_right_x | --lrx} = lower_right_x{--lower_right_y | --lry} = lower_right_y}}
        [infile]
</code></pre>
<h2>OPTION USAGE</h2>
<p> Minimum unique abbreviation of option is acceptable. (But note that shortest unique prefixes might be longer in future versions of the program.) You may use single hyphens instead of double hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. All options starting with hyphens may be given in any order. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamperspective</code> reads a Netpbm image as input and produces a Netpbm image of the same format as output. </p>
<p> <code>pamperspective</code> interprets the input image as a perspective projection of another image which is in a plane oblique to that of the input image. For example, a photograph of a painting, taken at an angle. The arguments <i>upper_left_x</i> &#8230; <i>lower_right_y</i> specify a quadrilateral in the photograph that <code>pamperspective</code> assumes corresponds to a parallelogram in the painting. The output image consists of this parallelogram, sheared to a rectangle. In this way <code>pamperspective</code> undoes the effect of a raytracer or scanline renderer. </p>
<p> Note that if the input image is a projection of a solid scene, rather than a plane, the result is like a different camera angle on that scene, to the extent that the scene is shallow from the other angle. </p>
<p> The input is from <i>infile</i>, or from Standard Input, if <i>infile</i> is not specified. The output is to Standard Output. </p>
<h2>OPTIONS</h2>
<p> For options of the form <code>&#8211;name=</code><i>num</i>, You can specify the value <i>num</i> in any of the traditional ways. Additionally, you can specify it as <i>num1</i>/<i>num2</i>, where <i>num1</i> and <i>num2</i> are specified traditionally. This is useful for specifying a width/height ratio of 4/3, without having to write infinitely many digits. Where <i>num</i> is supposed to be a natural number, <code>pamperspective</code> does not allow this format. </p>
<h3>Quadrilateral specification options</h3>
<dl>
<dt><code>&#8211;upper_left_x=</code><i>num</i></p>
<dd>
<dt><code>&#8211;ulx=</code><i>num</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> This specifies the horizontal coordinate of the upper left<br />
&nbsp;<wbr>&nbsp;<wbr>vertex of the quadrilateral.&nbsp;<wbr>&nbsp;<wbr>The meaning of&nbsp;<wbr>&#8216;upper left&#8217;&nbsp;<wbr>is<br />
&nbsp;<wbr>&nbsp;<wbr>relative to the output image.&nbsp;<wbr>&nbsp;<wbr>The interpretation of&nbsp;<wbr><i>num</i><br />
&nbsp;<wbr>&nbsp;<wbr>depends on the values for&nbsp;<wbr><code>&#8211;input_system</code>&nbsp;<wbr>and<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;input_unit</code>. </p>
<dt><code>&#8211;upper_left_y=</code><i>num</i></p>
<dd>
<dt><code>&#8211;uly=</code><i>num</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> This specifies the vertical coordinate of the upper left vertex<br />
&nbsp;<wbr>&nbsp;<wbr>of the quadrilateral.&nbsp;<wbr>&nbsp;<wbr>The meaning of&nbsp;<wbr>&#8216;upper left&#8217;&nbsp;<wbr>is relative to<br />
&nbsp;<wbr>&nbsp;<wbr>the output image.&nbsp;<wbr>&nbsp;<wbr>The interpretation of&nbsp;<wbr><i>num</i>&nbsp;<wbr>depends on the<br />
&nbsp;<wbr>&nbsp;<wbr>values for&nbsp;<wbr><code>&#8211;input_system</code>&nbsp;<wbr>and&nbsp;<wbr><code>&#8211;input_unit</code>. </p>
<dt><code>&#8211;upper_right_x=</code><i>num</i></p>
<dd>
<dt><code>&#8211;urx=</code><i>num</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> This specifies the horizontal coordinate of the upper right<br />
&nbsp;<wbr>&nbsp;<wbr>vertex of the quadrilateral.&nbsp;<wbr>&nbsp;<wbr>The meaning of&nbsp;<wbr>&#8216;upper right&#8217;&nbsp;<wbr>is<br />
&nbsp;<wbr>&nbsp;<wbr>relative to the output image.&nbsp;<wbr>&nbsp;<wbr>The interpretation of&nbsp;<wbr><i>num</i><br />
&nbsp;<wbr>&nbsp;<wbr>depends on the values for&nbsp;<wbr><code>&#8211;input_system</code>&nbsp;<wbr>and<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;input_unit</code>. </p>
<dt><code>&#8211;upper_right_y=</code><i>num</i></p>
<dd>
<dt><code>&#8211;ury=</code><i>num</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> This specifies the vertical coordinate of the upper right vertex<br />
&nbsp;<wbr>&nbsp;<wbr>of the quadrilateral.&nbsp;<wbr>&nbsp;<wbr>The meaning of&nbsp;<wbr>&#8216;upper right&#8217;&nbsp;<wbr>is relative to<br />
&nbsp;<wbr>&nbsp;<wbr>the output image.&nbsp;<wbr>&nbsp;<wbr>The interpretation of&nbsp;<wbr><i>num</i>&nbsp;<wbr>depends on the<br />
&nbsp;<wbr>&nbsp;<wbr>values for&nbsp;<wbr><code>&#8211;input_system</code>&nbsp;<wbr>and&nbsp;<wbr><code>&#8211;input_unit</code>. </p>
<dt><code>&#8211;lower_left_x=</code><i>num</i></p>
<dd>
<dt><code>&#8211;llx=</code><i>num</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> This specifies the horizontal coordinate of the lower left<br />
&nbsp;<wbr>&nbsp;<wbr>vertex of the quadrilateral.&nbsp;<wbr>&nbsp;<wbr>The meaning of&nbsp;<wbr>&#8216;lower left&#8217;&nbsp;<wbr>is<br />
&nbsp;<wbr>&nbsp;<wbr>relative to the output image.&nbsp;<wbr>&nbsp;<wbr>The interpretation of&nbsp;<wbr><i>num</i><br />
&nbsp;<wbr>&nbsp;<wbr>depends on the values for&nbsp;<wbr><code>&#8211;input_system</code>&nbsp;<wbr>and<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;input_unit</code>. </p>
<dt><code>&#8211;lower_left_y=</code><i>num</i></p>
<dd>
<dt><code>&#8211;lly=</code><i>num</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> This specifies the vertical coordinate of the lower left vertex<br />
&nbsp;<wbr>&nbsp;<wbr>of the quadrilateral.&nbsp;<wbr>&nbsp;<wbr>The meaning of&nbsp;<wbr>&#8216;lower left&#8217;&nbsp;<wbr>is relative to<br />
&nbsp;<wbr>&nbsp;<wbr>the output image.&nbsp;<wbr>&nbsp;<wbr>The interpretation of&nbsp;<wbr><i>num</i>&nbsp;<wbr>depends on the<br />
&nbsp;<wbr>&nbsp;<wbr>values for&nbsp;<wbr><code>&#8211;input_system</code>&nbsp;<wbr>and&nbsp;<wbr><code>&#8211;input_unit</code>. </p>
<dt><code>&#8211;lower_right_x=</code><i>num</i></p>
<dd>
<dt><code>&#8211;lrx=</code><i>num</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> This specifies the horizontal coordinate of the lower right<br />
&nbsp;<wbr>&nbsp;<wbr>vertex of the quadrilateral.&nbsp;<wbr>&nbsp;<wbr>The meaning of&nbsp;<wbr>&#8216;lower right&#8217;&nbsp;<wbr>is<br />
&nbsp;<wbr>&nbsp;<wbr>relative to the output image.&nbsp;<wbr>&nbsp;<wbr>The interpretation of&nbsp;<wbr><i>num</i><br />
&nbsp;<wbr>&nbsp;<wbr>depends on the values for&nbsp;<wbr><code>&#8211;input_system</code>&nbsp;<wbr>and<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;input_unit</code>. </p>
<dt><code>&#8211;lower_right_y=</code><i>num</i></p>
<dd>
<dt><code>&#8211;lry=</code><i>num</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> This specifies the vertical coordinate of the lower right vertex<br />
&nbsp;<wbr>&nbsp;<wbr>of the quadrilateral.&nbsp;<wbr>&nbsp;<wbr>The meaning of&nbsp;<wbr>&#8216;lower right&#8217;&nbsp;<wbr>is relative to<br />
&nbsp;<wbr>&nbsp;<wbr>the output image.&nbsp;<wbr>&nbsp;<wbr>The interpretation of&nbsp;<wbr><i>num</i>&nbsp;<wbr>depends on the<br />
&nbsp;<wbr>&nbsp;<wbr>values for&nbsp;<wbr><code>&#8211;input_system</code>&nbsp;<wbr>and&nbsp;<wbr><code>&#8211;input_unit</code>. </p>
<dt><code>&#8211;input_system=</code><i>system</i></p>
<dd>
<dt><code>&#8211;input_unit=</code><i>unit</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> The input image consists of pixels, which are, from the point of<br />
&nbsp;<wbr>&nbsp;<wbr>view of a scanline renderer, solid squares.&nbsp;<wbr>&nbsp;<wbr>These options specify<br />
&nbsp;<wbr>&nbsp;<wbr>how the coordinates are interpreted: </p>
<dt><i>system</i>=<code>lattice</code>, <i>unit</i>=<code>image</code></p>
<dd>
<p>&nbsp;<wbr> (0,0) refers to the upper left corner of the upper left pixel<br />
&nbsp;<wbr>and&nbsp;<wbr>(1,1)&nbsp;<wbr>refers to the lower right corner of the lower right<br />
&nbsp;<wbr>pixel. </p>
<dt><i>system</i>=<code>lattice</code>, <i>unit</i>=<code>pixel</code></p>
<dd>
<p>&nbsp;<wbr> (0,0) refers to the upper left corner of the upper left pixel<br />
&nbsp;<wbr>and&nbsp;<wbr>(<i>width</i>,<i>height</i>)&nbsp;<wbr>refers to the lower right corner<br />
&nbsp;<wbr>of the lower right pixel.&nbsp;<wbr>&nbsp;<wbr>Here&nbsp;<wbr><i>width</i>&nbsp;<wbr>and&nbsp;<wbr><i>height</i>&nbsp;<wbr>are<br />
&nbsp;<wbr>the width and height of the input image. </p>
<dt><i>system</i>=<code>pixel</code>, <i>unit</i>=<code>image</code></p>
<dd>
<p>&nbsp;<wbr> (0,0) refers to the center of the upper left pixel and (1,1)<br />
&nbsp;<wbr>refers to the center of the lower right pixel. </p>
<dt><i>system</i>=<code>pixel</code>, <i>unit</i>=<code>pixel</code></p>
<dd>
<p>&nbsp;<wbr> (0,0) refers to the center of the upper left pixel and<br />
&nbsp;<wbr>(<i>width</i>-1,<i>height</i>-1)&nbsp;<wbr>refers to the center of the lower<br />
&nbsp;<wbr>right pixel.&nbsp;<wbr>&nbsp;<wbr>Here&nbsp;<wbr><i>width</i>&nbsp;<wbr>and&nbsp;<wbr><i>height</i>&nbsp;<wbr>are the width<br />
&nbsp;<wbr>and height of the input image. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The defaults are&nbsp;<wbr><code>&#8211;input_system</code>=<code>lattice</code>&nbsp;<wbr>and<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;input_unit</code>=<code>pixel</code>.&nbsp;<wbr>&nbsp;<wbr>Point-and-click front ends should<br />
&nbsp;<wbr>&nbsp;<wbr>use&nbsp;<wbr><code>&#8211;input_system</code>=<code>pixel</code>. </p>
</dl>
<h3>Frame Options</h3>
<p> By default <code>pamperspective</code> outputs exactly the above parallelogram, sheared to a rectangle. With the following options, it is possible to make <code>pamperspective</code> output a larger or smaller portion, which we call the &#8216;visible part.&#8217; We refer to the default rectangle as the &#8216;frame.&#8217; The visible part is always a rectangle the axes of which are parallel to those of the frame. </p>
<p> The frame options are additive. All the parts of the image specified by either margin options, <code>&#8211;frame_include</code>, or <code>&#8211;include</code> (or their defaults) are in the visible part. The visible part is the smallest possible rectangle that contains the parts specified those three ways. </p>
<p> The visible part must have nonzero size. That means if you specify <code>&#8211;frame_include=no</code> (overriding the default), you&#8217;ll need to specify other frame options in order to have something in the visible part. </p>
<dl>
<dt>[<code>&#8211;margin=</code><i>num</i>]</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> This specifies an area surrounding the frame that is to be<br />
&nbsp;<wbr>&nbsp;<wbr>included in the visible part.&nbsp;<wbr>&nbsp;<wbr>The units of&nbsp;<wbr><i>num</i>&nbsp;<wbr>are the width<br />
&nbsp;<wbr>&nbsp;<wbr>of the frame for the horizontal extensions and the height of the<br />
&nbsp;<wbr>&nbsp;<wbr>frame for vertical extensions. </p>
<p> For example, <code>&#8211;margin=1</code> makes the visible part 9 times as large,<br />
&nbsp;<wbr>&nbsp;<wbr>because it makes the visible part extend one frame&#8217;s worth to the left<br />
&nbsp;<wbr>&nbsp;<wbr>of the frame, one frame&#8217;s worth to the right, one frame&#8217;s worth above<br />
&nbsp;<wbr>&nbsp;<wbr>the frame, and one frame&#8217;s worth below the frame, for a total of<br />
&nbsp;<wbr>&nbsp;<wbr>3 frames&#8217;&nbsp;<wbr>worth in both dimensions. </p>
<p> A negative value has an effect only if you specify<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;frame_include=no</code>.&nbsp;<wbr>&nbsp;<wbr>The default is no margin. </p>
<p> The individual margin options below override this common margin<br />
&nbsp;<wbr>&nbsp;<wbr>setting. </p>
<dt>[<code>&#8211;top_margin=</code><i>num</i>]</p>
<dd>
<dt>[<code>&#8211;left_margin=</code><i>num</i>]</p>
<dd>
<dt>[<code>&#8211;right_margin=</code><i>num</i>]</p>
<dd>
<dt>[<code>&#8211;bottom_margin=</code><i>num</i>]</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> These are like <code>&#8211;margin</code>, but they specify only one of<br />
&nbsp;<wbr>&nbsp;<wbr>the 4 sides.&nbsp;<wbr>&nbsp;<wbr>The default value for each is the value&nbsp;<wbr>(or default)&nbsp;<wbr>of<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;margin</code>. </p>
<dt>[<code>&#8211;frame_include=</code><i>bool</i>]</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> Valid values for <i>bool</i> are: </p>
<dt><code>yes</code></p>
<dd>
<dt><code>true</code></p>
<dd>
<dt><code>on</code></p>
<dd>
<p>&nbsp;<wbr> The frame itself is in the visible part. </p>
<dt><code>no</code></p>
<dd>
<dt><code>false</code></p>
<dd>
<dt><code>off</code></p>
<dd>
<p>&nbsp;<wbr> The frame itself is not necessarily in the visible part<br />
&nbsp;<wbr>(but it could be if other options cause it to be). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The default value is&nbsp;<wbr><code>yes</code> </p>
<dt><code>&#8211;include=[</code><i>x1</i>,<i>y1</i>;<i>x2</i>,<i>y2</i>; &#8230;]</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> The visible part is made large enough such that every point<br />
&nbsp;<wbr>&nbsp;<wbr>(<i>x1</i>,<i>y1</i>),&nbsp;<wbr>(<i>x2</i>,<i>y2</i>), of the&nbsp;<wbr><i>input</i>&nbsp;<wbr>image is&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>visible.&nbsp;<wbr>&nbsp;<wbr>The meaning of&nbsp;<wbr><i>x</i>&nbsp;<wbr>and&nbsp;<wbr><i>y</i>&nbsp;<wbr>is determined by<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;input_system</code>&nbsp;<wbr>and&nbsp;<wbr><code>&#8211;input_unit</code>.&nbsp;<wbr>&nbsp;<wbr>You can specify any<br />
&nbsp;<wbr>&nbsp;<wbr>number of semicolon-delimited points, including zero. </p>
<p> If you&#8217;re supplying these options via a Unix command shell, be<br />
&nbsp;<wbr>&nbsp;<wbr>sure to use proper quoting, because semicolon&nbsp;<wbr>(<code>;</code>)&nbsp;<wbr>is usually<br />
&nbsp;<wbr>&nbsp;<wbr>a shell control character. </p>
<p>&nbsp;<wbr>&nbsp;<wbr></dl>
<p> The frame options were new in Netpbm 10.25 (October 2004). </p>
<h3>Output Size Options</h3>
<dl>
<dt><code>&#8211;width=</code><i>width</i></p>
<dd>
<dt><code>&#8211;height=</code><i>height</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> These specify the size of the output image in horizontal and<br />
&nbsp;<wbr>&nbsp;<wbr>vertical direction.&nbsp;<wbr>&nbsp;<wbr>The values are numbers of pixels, so only<br />
&nbsp;<wbr>&nbsp;<wbr>natural numbers are valid.&nbsp;<wbr>&nbsp;<wbr>These values override the default<br />
&nbsp;<wbr>&nbsp;<wbr>means to determine the output size. </p>
<dt><code>&#8211;detail=</code><i>num</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> If you do not specify <code>&#8211;width</code>, <code>pamperspective</code><br />
&nbsp;<wbr>&nbsp;<wbr>determines the width of the output image such that moving&nbsp;<wbr><i>num</i><br />
&nbsp;<wbr>&nbsp;<wbr>output pixels horizontally does not change the corresponding pixel<br />
&nbsp;<wbr>&nbsp;<wbr>coordinates of the input image by more than 1.<br />
&nbsp;<wbr>&nbsp;<wbr><code>pamperspective</code>&nbsp;<wbr>determines the height of the output image<br />
&nbsp;<wbr>&nbsp;<wbr>analogously.&nbsp;<wbr>&nbsp;<wbr>The default value is 1. </p>
<dt><code>&#8211;proportion=</code><i>prop</i></p>
<dd>
<dt><code>&#8211;ratio=</code><i>ratio</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> Valid values for <i>prop</i> are: </p>
<dt><code>free</code></p>
<dd>
<p>&nbsp;<wbr> In this case <code>&#8211;ratio</code> does not have any effect. </p>
<dt><code>fixed</code></p>
<dd> After the width and height are determined<br />
&nbsp;<wbr>according to&nbsp;<wbr><code>&#8211;detail</code>, one of both will be increased, in<br />
&nbsp;<wbr>order to obtain width/height=<i>ratio</i>. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The defaults are&nbsp;<wbr><code>&#8211;proportion</code>=<code>free</code>&nbsp;<wbr>and<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;ratio</code>=1. </p>
</dl>
<h3>Output Options</h3>
<dl>
<dt><code>&#8211;output_system=</code><i>spec</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> The output image consists of pixels, which are, from the point<br />
&nbsp;<wbr>&nbsp;<wbr>of view of a scanline renderer, solid squares.&nbsp;<wbr>&nbsp;<wbr>This option<br />
&nbsp;<wbr>&nbsp;<wbr>specifies how the four vertices of the quadrilateral correspond to<br />
&nbsp;<wbr>&nbsp;<wbr>the pixels of the output image.&nbsp;<wbr>&nbsp;<wbr>Valid values for&nbsp;<wbr><i>spec</i>&nbsp;<wbr>are: </p>
<dt><code>lattice</code></p>
<dd>
<p>&nbsp;<wbr> The upper left vertex corresponds to the upper left corner of<br />
&nbsp;<wbr>the upper left pixel and The lower right vertex corresponds to the<br />
&nbsp;<wbr>lower right corner of the lower right<br />
&nbsp;<wbr>pixel. </p>
<dt><code>pixel</code></p>
<dd>
<p>&nbsp;<wbr> The upper left vertex corresponds to the center of the upper<br />
&nbsp;<wbr>left pixel and The lower right vertex corresponds to the center of<br />
&nbsp;<wbr>the lower right pixel. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The default value is&nbsp;<wbr><code>lattice</code>.&nbsp;<wbr>&nbsp;<wbr>Point-and-click front ends<br />
&nbsp;<wbr>&nbsp;<wbr>should use&nbsp;<wbr><code>pixel</code>. </p>
<dt><code>&#8211;interpolation=</code><i>spec</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> Usually (centers of) output pixels do not exactly correspond to<br />
&nbsp;<wbr>&nbsp;<wbr>(centers of)&nbsp;<wbr>input pixels.&nbsp;<wbr>&nbsp;<wbr>This option determines how the program<br />
&nbsp;<wbr>&nbsp;<wbr>will choose the new pixels.&nbsp;<wbr>&nbsp;<wbr>Valid values for&nbsp;<wbr><i>spec</i>&nbsp;<wbr>are: </p>
<dt><code>nearest</code></p>
<dd>
<p>&nbsp;<wbr> The output pixel will be identical to the nearest input<br />
&nbsp;<wbr>pixel. </p>
<dt><code>linear</code></p>
<dd>
<p>&nbsp;<wbr> The output pixel will be a bilinear interpolation of the four<br />
&nbsp;<wbr>surrounding input pixels. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The default value is&nbsp;<wbr><code>nearest</code>. </p>
</dl>
<h2>HINTS</h2>
<p> It might be tempting always to use the options <code>&#8211;include 0,0;0,1;1,0;1,1</code> (assuming <code>&#8211;input_system=lattice</code> and <code>&#8211;input_unit=image</code>), so that no part of the input image is missing in the output. There are problems with that: </p>
<dl>
<dt>&bull;</p>
<dd> If the three dimensional plane defined by the quadrilateral has a<br />
&nbsp;<wbr>&nbsp;<wbr>visible horizon in the input image, then the above asks&nbsp;<wbr><code>pamperspective</code><br />
&nbsp;<wbr>&nbsp;<wbr>to include points that cannot ever be part of the output. </p>
<dt>&bull;</p>
<dd> If the horizon is not visible, but close to the border of the<br />
&nbsp;<wbr>&nbsp;<wbr>input image, this may result in&nbsp;<wbr><i>very</i>&nbsp;<wbr>large output<br />
&nbsp;<wbr>&nbsp;<wbr>files. Consider a picture of a road. If you ask for a point close to<br />
&nbsp;<wbr>&nbsp;<wbr>the horizon to be included, then this point is far away from the<br />
&nbsp;<wbr>&nbsp;<wbr>viewer. The output will cover many kilometers of road, while<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;detail</code>&nbsp;<wbr>perhaps makes a pixel represent a square centimeter. </p>
<p>&nbsp;<wbr>&nbsp;<wbr></dl>
<p> When working with large files <code>pamperspective</code>&#8216;s memory usage might be an issue. In order to keep it small, you should minimize each of the following: </p>
<dl>
<dt>&bull;</p>
<dd> The vertical range that the top output line consumes in the<br />
&nbsp;<wbr>&nbsp;<wbr>input image; </p>
<dt>&bull;</p>
<dd> The vertical range that the bottom output line consumes in the<br />
&nbsp;<wbr>&nbsp;<wbr>input image; </p>
<dt>&bull;</p>
<dd> The vertical range from the topmost (with respect to the<br />
&nbsp;<wbr>&nbsp;<wbr>input image)&nbsp;<wbr>quadrilateral point to the top&nbsp;<wbr>(with respect to the output&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>image)&nbsp;<wbr>output line. </p>
<p>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> For this purpose you can use <code>pamflip</code> before and/or after <code>pamperspective</code>. Example: Instead of </p>
<pre>
<code>pamperspective 10 0 100 50 0 20 95 100 infile &gt; outfile</code>
</pre>
<p> you can use </p>
<pre>
<code>pamflip -rotate90 infile | 
   pamperspective 50 0 100 5 0 90 20 100 | 
   pamflip -rotate270 &gt; outfile</code>
</pre>
<p>&nbsp;<wbr>&nbsp;<wbr></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-netpbm/">netpbm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) , <code><a href="/docs/linux/man/1-pamflip/">pamflip</a></code>(1) , <code><a href="/docs/linux/man/1-pnmrotate/">pnmrotate</a></code>(1) , <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) , <code><a href="/docs/linux/man/1-pnmshear/">pnmshear</a></code>(1) , <code><a href="/docs/linux/man/1-pnmstitch/">pnmstitch</a></code>(1) </p>
<h2>HISTORY</h2>
<p> Mark Weyer wrote <code>pamperspective</code> in March 2004. </p>
<p> It was new in Netpbm 10.22 (April 2004). </p>
<h2>AUTHOR</h2>
<p> This documentation was written by Mark Weyer. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<h2>Index</h2>
