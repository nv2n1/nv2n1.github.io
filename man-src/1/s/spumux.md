---
title: "spumux(1)"
name: "spumux"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spumux/"
description: "spumux – generates and multiplexes subtitles into an existing mpeg2 program stream"
---

<h2 class="name">NAME</h2>
<p> spumux &#8211; generates and multiplexes subtitles into an existing mpeg2 program stream </p>
<h2>SYNOPSIS</h2>
<p> <code>spumux</code> [ <code>-m dvd</code> | <code>-m cvd</code> | <code>-m svcd</code> ] [ <code>-s </code><i>stream</i> ] [ <code>-v </code><i>level</i> ] [ <code>-P</code> ] [ <code>&#8211;nomux</code> ] [ <code>&#8211;nodvdauthor-data</code> ] <i>file</i> <code>&lt; </code><i>mpeg</i> <code>&gt; </code><i>mpeg-with-subtitles</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>spumux</code> encodes the subtitles and multiplexes it into the mpeg2 program stream.</p>
<dl>
<dt><code>-m </code><i>mode</i></p>
<dd> Sets the encoding for the subtitles. Can be dvd, cvd, or svcd. Default is dvd.</p>
<dt><code>-s </code><i>stream</i></p>
<dd> Sets the subtitle stream id. Default is 0.</p>
<dt><code>-v </code><i>level</i></p>
<dd> Sets the verbosity level.</p>
<dt><code>-P</code></p>
<dd> Enables a progress bar.</p>
<dt><code>&#8211;nomux</code></p>
<dd> Disables reading of an MPEG stream from standard input. Instead, the output will contain only the subpicture stream.</p>
<dt><code>&#8211;nodvdauthor-data</code></p>
<dd> Disables passing of color and button info to dvdauthor.</dl>
<p> Here&#8217;s a sample configuration file: </p>
<pre><code>
&lt;subpictures&gt;
   &lt;stream&gt;
      &lt;spu start="start-time" [ end="end-time" ] [ image="picture.png" ]
           [ highlight="picture.png" ] [ select="picture.png" ]
           [ transparent="color-spec" ] [ force="yes" ]
           [ autooutline="infer" [ outlinewidth="width" ]
             [ autoorder="rows" | autoorder="columns" ] ]
           [ xoffset="x-coord" yoffset="y-coord" ] &gt;
         &lt;button [ name="name" ] [ x0="x0" ] [ y0="y0" ] [ x1="x1" ]
                 [ y1="y1" ] [ up="name" ] [ down="name" ]
                 [ left="name" ] [ right="name" ] /&gt;
         &lt;action [ name="name" ] [ x0="x0" ] [ y0="y0" ] [ x1="x1" ]
                 [ y1="y1" ] /&gt;
      &lt;/spu&gt;
   &lt;/stream&gt;
&lt;/subpictures&gt;
</code></pre>
<p> Each subtitle image is described by an &lt;spu&gt; tag. The start and optional end attributes describe when the subtitle will be displayed on the screen, in &quot;HR:MM:SS.HU&quot;. The image attribute describes the main subtitle image, which can either be a PNG or BMP file. If your image is not a full screen image, you can use xoffset and yoffset to move the picture around. In the advent that the author is unable to use a graphics format with an alpha channel, then the transparent attribute can be used to describe which color should become fully transparent. For the valid formats for <i>color-spec</i>, see SPECIFYING COLORS below. If you want to force the display of the subtitle, regardless of whether the user has enabled subtitles or not, you can use the force tag. When you are making menus, the force tag is required. </p>
<p> The remaining attributes and tags are related to menu creation. The highlight attribute shows what all the buttons look like when they are highlighted (i.e. when you are using the arrows in the menu), and the select attribute shows what all the buttons look like when the are selected (i.e. for the 1-2 seconds after you press enter in the menu). If either of these (or the image attribute) are omitted, then spumux creates a blank (totally transparent) image. Obviously at least one tag should be specified. </p>
<p> To aid in button creation, the autooutline attribute instructs spumux to infer where the buttons are located. It does this by attempting to draw rectangles around a composition of the highlight and select images which do not intersect any opaque or semi-opaque pixels. In order to support textual buttons, the attribute outlinewidth allows you to specify the width of the rectangle which is tested. Wider rectangles won&#8217;t be able to squeeze between the letters. Finally, autoorder describes which way to order the automatically detected buttons, which is important for numerically selected buttons and for mapping buttons to button names or to the implied names. </p>
<p> The button and action tags describe the buttons (visibly selectable objects on the screen) and actions (commands that are executed as soon as the associated key is pressed on the remote). If you are using the autooutline feature, just designing buttons, are happy with the inferred button navigation, and can deal with the simplistic naming system, then you actually do not even need to specify any buttons or actions. Otherwise, read on. </p>
<p> The name attribute is used to give a button or action an easy to refer to name. By default they are numbered sequentially starting with &quot;1&quot;. The up, down, left, and right names describe which button or action should be tied to the corresponding key when the current button is highlighted, though if omitted spumux will use a reasonably intelligent algorithm to determine which buttons to move to. </p>
<p> The (x0,y0) coordinates describe the upper left hand corner inclusively, while the (x1,y1) coordinates describe the lower right hand corner EXclusively. The coordinates start at 0,0 for the upper left hand corner. Ideally, the y0 and y1 coordinates should both be even, so the button edges fully empasses two interlaced scanlines, even if there is no data in the extra scanline. Some DVD players will fill in the extra scanline if it is not specified; spumux makes an effort to ensure that will be transparent but there is no guarantee.</p>
<h2>HANDLING TEXT-BASED SUBTITLES</h2>
<p> Spumux is also able to handle text subtitles, which will be rendered to graphics by spumux. A lot of different text (must be non-graphic) formats are supported (.sub, .srt, .ssa, .smi, .rt , .txt, .aqt, .jss, .js, ass). Spumux will try to determine the format automatically. </p>
<p> If processing text-based subtitles no other streams can be defined, buttons or others need to be processed in another pass with spumux, using another xml file. </p>
<p> Following .xml file shows the available tags and their default settings. Only the textsub tag is mandatory, defaults are used if the specific tag is not specified. </p>
<pre>
&lt;subpictures [format=&quot;NTSC|PAL&quot;]&gt;
   &lt;stream&gt;
      &lt;textsub filename=&quot;demo1.srt&quot; characterset=&quot;UTF-8&quot;
         fontsize=&quot;28.0&quot; font=&quot;arial&quot; fill-color=&quot;<i>color-spec</i>&quot;
         outline-color=&quot;<i>color-spec</i>&quot; outline-thickness=&quot;3.0&quot;
         shadow-offset=&quot;0, 0&quot; shadow-color=&quot;<i>color-spec</i>&quot;
         horizontal-alignment=&quot;left&quot;  vertical-alignment=&quot;bottom&quot;
         left-margin=&quot;60&quot; right-margin=&quot;60&quot;
         top-margin=&quot;20&quot; bottom-margin=&quot;30&quot; subtitle-fps=&quot;<i>fps</i>&quot;
         movie-fps=&quot;<i>fps</i>&quot;
         movie-width=&quot;720&quot; movie-height=&quot;<i>height</i>&quot; aspect=&quot;4:3&quot;
         force=&quot;yes&quot;
      /&gt;
   &lt;/stream&gt;
&lt;/subpictures&gt;
</pre>
<p> The textsub tag defines the settings for the text to graphics rendering. </p>
<p> The filename attribute defines the path and name of the input text subtitle file, this is the only attribute that is mandatory. </p>
<p> The characterset attribute defines the characterset to be used, available charactersets can be found at <a rel="nofollow" href="http://www.gnu.org/software/libiconv.">http://www.gnu.org/software/libiconv.</a> </p>
<p> The fontsize attribute defines the size of the font in font units. The font attribute defines the font used. Spumux will match the font name using Fontconfig if available, else it will use it as a filename on linux systems and will look into the windows/fonts and subdirectory spumux of the cygwin/mingw home directory and into the execution directory for windows-based execution for the specified font. Looking for free fonts? One listing is here <a rel="nofollow" href="http://www.microsoft.com/typography/links/links.asp?type=free">http://www.microsoft.com/typography/links/links.asp?type=free</a>&amp;part=1 (this is only about fonts, not about operating systems). </p>
<p> The fill-color attribute specifies the color to be used for filling the interior of the text, while outline-color specifies the color for the outline border to draw around each character, to set it off from the video background. The outline-thickness attribute specifies the thickness of this outline. For the valid formats for <i>color-spec</i>, see SPECIFYING COLORS below. The default fill color is white and the default outline color is black. </p>
<p> The shadow-offset and shadow-color attributes specify a shadow effect to be applied to the text. The shadow-offset is specified as 2 signed integers, being the horizontal and vertical offset respectively, with positive values being to the right and down. For the valid formats for <i>color-spec</i>, see SPECIFYING COLORS below. The default shadow color is black. </p>
<p> The horizontal-alignment attribute defines the horizontal alignment of the subtitles. Options are: &quot;left&quot;, &quot;right&quot;, &quot;center&quot; and &quot;default&quot;. The &quot;default&quot; value causes spumux to use the attribute that is in the text subtitle file if the format supports such an attribute. </p>
<p> The vertical-alignment attribute defines the vertical alignment. Options are: &quot;top&quot;, &quot;center&quot; and &quot;bottom&quot;. </p>
<p> The margin attributes define the minimum blank pixel space between the border of the image and the border of the subtitle lines. </p>
<p> The subtitle-fps is needed for subtitle formats which use frame numbers rather than fractional seconds for specifying subtitle times, while the movie-fps is the frame rate of the movie onto which the subtitles are being multiplexed; if omitted, both of these default to 29.97 for NTSC and 25 for PAL. </p>
<p> Having separate subtitle-fps and movie-fps attributes make it possible for spumux to recalculate the subtitle timing if these are not the same. </p>
<p> The movie-width and movie-height attributes define the maximum size of the subtitle page, these shouldn&#8217;t be larger than the size of the video frame (720&#215;480 for NTSC, 720&#215;576 for PAL), normally they are the same. Some DVD players prefer subtitle frames that are 2 or 4 pixels smaller in height. If omitted, the default movie width is 720 and the height is 2 pixels less than the video frame height. </p>
<p> The aspect attribute lets you specify whether the video aspect ratio is 16:9 (widescreen) or 4:3. This, together with the video format, is used to adjust the rendering of the text to ensure it appears undistorted. </p>
<p> The force option allows you to force the display of the subtitle, regardless of whether the user has enabled subtitles or not.</p>
<h2>SPECIFYING COLORS</h2>
<p> Colors for image transparency and text fill and outlines can be specified in a number of ways:</p>
<dl>
<dt>&bull;</p>
<dd> As a color name, e.g. &quot;green&quot;. You can use most of the color names listed at &lt;<a rel="nofollow" href="http://www.imagemagick.org/script/color.php">http://www.imagemagick.org/script/color.php</a>&gt;.</p>
<dt>&bull;</p>
<dd> As a hexadecimal string preceded by a &quot;#&quot;, similar to HTML format, e.g. &quot;#FF8080&quot;. The number of digits must be a multiple of 3; the first group specifies the red component, the second green, and the third blue.</p>
<dt>&bull;</p>
<dd> As the name of a color space, followed by one to four component values in parentheses, e.g. &quot;hsv(120, 50%, 90%)&quot;.</dl>
<p> Valid color spaces are &quot;gray&quot; (1 component), &quot;graya&quot; (2 components), &quot;hsl&quot; (3 components), &quot;hsla&quot; (4 components), &quot;hsv&quot; (3 components), &quot;hsva&quot; (4 components), &quot;rgb&quot; (3 components) and &quot;rgba&quot; (4 components). Each component can be specified as either a percentage of the maximum value suffixed by &quot;%&quot;, or an absolute value in the range 0-360 for hues, 0-255 for everything else. For color space names ending with &quot;a&quot;, the last component is the alpha (transparency) value. </p>
<p> Note that alpha values are meaningless for the &quot;transparent&quot; attribute on the &lt;spu&gt; tag above. &lt;marc.leeman [at] gmail.com&gt; MarcLeeman2003Marc Leeman </p>
<h2>Index</h2>
