---
title: "urxvt256c-ml-background(1)"
name: "urxvt256c-ml-background"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256c-ml-background/"
---

<h2 class="name">NAME</h2>
 

 background - manage terminal background 

<h2>SYNOPSIS</h2>

 <pre>
   urxvt --background-expr 'background expression'
         --background-border
         --background-interval seconds
</pre>

<h2>QUICK AND DIRTY CHEAT SHEET</h2>

 Just load a random jpeg image and tile the background with it without scaling or anything else: 

 <pre>
   load &quot;/path/to/img.jpg&quot;
</pre> 

 The same, but use mirroring/reflection instead of tiling: 

 <pre>
   mirror load &quot;/path/to/img.jpg&quot;
</pre> 

 Load an image and scale it to exactly fill the terminal window: 

 <pre>
   scale keep { load &quot;/path/to/img.jpg&quot; }
</pre> 

 Implement pseudo-transparency by using a suitably-aligned root pixmap as window background: 

 <pre>
   rootalign root
</pre> 

 Likewise, but keep a blurred copy: 

 <pre>
   rootalign keep { blur 10, root }
</pre>

<h2>DESCRIPTION</h2>

 This extension manages the terminal background by creating a picture that is behind the text, replacing the normal background colour. 

 It does so by evaluating a Perl expression that <i>calculates</i> the image on the fly, for example, by grabbing the root background or loading a file. 

 While the full power of Perl is available, the operators have been design to be as simple as possible. 

 For example, to load an image and scale it to the window size, you would use: 

 <pre>
   urxvt --background-expr 'scale keep { load &quot;/path/to/mybg.png&quot; }'
</pre> 

 Or specified as a X resource: 

 <pre>
   URxvt.background-expr: scale keep { load &quot;/path/to/mybg.png&quot; }
</pre>

<h2>THEORY OF OPERATION</h2>

 At startup, just before the window is mapped for the first time, the expression is evaluated and must yield an image. The image is then extended as necessary to cover the whole terminal window, and is set as a background pixmap. 

 If the image contains an alpha channel, then it will be used as-is in visuals that support alpha channels (for example, for a compositing manager). In other visuals, the terminal background colour will be used to replace any transparency. 

 When the expression relies, directly or indirectly, on the window size, position, the root pixmap, or a timer, then it will be remembered. If not, then it will be removed. 

 If any of the parameters that the expression relies on changes (when the window is moved or resized, its position or size changes; when the root pixmap is replaced by another one the root background changes; or when the timer elapses), then the expression will be evaluated again. 

 For example, an expression such as <tt>&quot;scale keep { load &quot;$HOME/mybg.png&quot; }&quot;</tt> scales the image to the window size, so it relies on the window size and will be reevaluated each time it is changed, but not when it moves for example. That ensures that the picture always fills the terminal, even after its size changes.

<h3><font SIZE="-1">EXPRESSIONS</font></h3>

 Expressions are normal Perl expressions, in fact, they are Perl blocks - which means you could use multiple lines and statements: 

 <pre><code>
scale keep
{
    again 3600;
    if (localtime now)[6])
        {
            return load "$HOME/weekday.png";
        }
    else {
        return load "$HOME/sunday.png";
    }
}
</code></pre> 

 This inner expression is evaluated once per hour (and whenever the terminal window is resized). It sets <i>sunday.png</i> as background on Sundays, and <i>weekday.png</i> on all other days. 

 Fortunately, we expect that most expressions will be much simpler, with little Perl knowledge needed. 

 Basically, you always start with a function that ``generates'' an image object, such as <tt>&quot;load&quot;</tt>, which loads an image from disk, or <tt>&quot;root&quot;</tt>, which returns the root window background image: 

 <pre>
   load &quot;$HOME/mypic.png&quot;
</pre> 

 The path is usually specified as a quoted string (the exact rules can be found in the perlop manpage). The <i></i>$HOME<i></i> at the beginning of the string is expanded to the home directory. 

 Then you prepend one or more modifiers or filtering expressions, such as <tt>&quot;scale&quot;</tt>: 

 <pre>
   scale load &quot;$HOME/mypic.png&quot;
</pre> 

 Just like a mathematical expression with functions, you should read these expressions from right to left, as the <tt>&quot;load&quot;</tt> is evaluated first, and its result becomes the argument to the <tt>&quot;scale&quot;</tt> function. 

 Many operators also allow some parameters preceding the input image that modify its behaviour. For example, <tt>&quot;scale&quot;</tt> without any additional arguments scales the image to size of the terminal window. If you specify an additional argument, it uses it as a scale factor (multiply by 100 to get a percentage): 

 <pre>
   scale 2, load &quot;$HOME/mypic.png&quot;
</pre> 

 This enlarges the image by a factor of 2 (200%). As you can see, <tt>&quot;scale&quot;</tt> has now two arguments, the <tt>200</tt> and the <tt>&quot;load&quot;</tt> expression, while <tt>&quot;load&quot;</tt> only has one argument. Arguments are separated from each other by commas. 

 Scale also accepts two arguments, which are then separate factors for both horizontal and vertical dimensions. For example, this halves the image width and doubles the image height: 

 <pre>
   scale 0.5, 2, load &quot;$HOME/mypic.png&quot;
</pre> 

 <font SIZE="-1">IF</font> you try out these expressions, you might suffer from some sluggishness, because each time the terminal is resized, it loads the <font SIZE="-1">PNG</font> image again and scales it. Scaling is usually fast (and unavoidable), but loading the image can be quite time consuming. This is where <tt>&quot;keep&quot;</tt> comes in handy: 

 <pre>
   scale 0.5, 2, keep { load &quot;$HOME/mypic.png&quot; }
</pre> 

 The <tt>&quot;keep&quot;</tt> operator executes all the statements inside the braces only once, or when it thinks the outcome might change. In other cases it returns the last value computed by the brace block. 

 This means that the <tt>&quot;load&quot;</tt> is only executed once, which makes it much faster, but also means that more memory is being used, because the loaded image must be kept in memory at all times. In this expression, the trade-off is likely worth it. 

 But back to effects: Other effects than scaling are also readily available, for example, you can tile the image to fill the whole window, instead of resizing it: 

 <pre>
   tile keep { load &quot;$HOME/mypic.png&quot; }
</pre> 

 In fact, images returned by <tt>&quot;load&quot;</tt> are in <tt>&quot;tile&quot;</tt> mode by default, so the <tt>&quot;tile&quot;</tt> operator is kind of superfluous. 

 Another common effect is to mirror the image, so that the same edges touch: 

 <pre>
   mirror keep { load &quot;$HOME/mypic.png&quot; }
</pre> 

 Another common background expression is: 

 <pre>
   rootalign root
</pre> 

 This one first takes a snapshot of the screen background image, and then moves it to the upper left corner of the screen (as opposed to the upper left corner of the terminal window)- the result is pseudo-transparency: the image seems to be static while the window is moved around.

<h3><font SIZE="-1">COLOUR SPECIFICATIONS</font></h3>

 Whenever an operator expects a ``colour'', then this can be specified in one of two ways: Either as string with an X11 colour specification, such as: 

 <pre>
   &quot;red&quot;               # named colour
   &quot;#f00&quot;              # simple rgb
   &quot;[50]red&quot;           # red with 50% alpha
   &quot;TekHVC:300/50/50&quot;  # anything goes
</pre> 

 <font SIZE="-1">OR</font> as an array reference with one, three or four components: 

 
[0.5] #50 % gray, 100 % alpha[0.5, 0, 0] #dark red, no green or blur, 100 % alpha[0.5, 0, 0, 0.7] #same with explicit 70 % alpha


<h3><font SIZE="-1">CACHING AND SENSITIVITY</font></h3>

 Since some operations (such as <tt>&quot;load&quot;</tt> and <tt>&quot;blur&quot;</tt>) can take a long time, caching results can be very important for a smooth operation. Caching can also be useful to reduce memory usage, though, for example, when an image is cached by <tt>&quot;load&quot;</tt>, it could be shared by multiple terminal windows running inside urxvtd. 

 <i></i>&quot;keep { ... }&quot;<i> caching</i> 

 The most important way to cache expensive operations is to use <tt>&quot;keep { ... }&quot;</tt>. The <tt>&quot;keep&quot;</tt> operator takes a block of multiple statements enclosed by <tt>&quot;{}&quot;</tt> and keeps the return value in memory. 

 An expression can be ``sensitive'' to various external events, such as scaling or moving the window, root background changes and timers. Simply using an expression (such as <tt>&quot;scale&quot;</tt> without parameters) that depends on certain changing values (called ``variables''), or using those variables directly, will make an expression sensitive to these events - for example, using <tt>&quot;scale&quot;</tt> or <tt>&quot;TW&quot;</tt> will make the expression sensitive to the terminal size, and thus to resizing events. 

 When such an event happens, <tt>&quot;keep&quot;</tt> will automatically trigger a reevaluation of the whole expression with the new value of the expression. 

 <tt>&quot;keep&quot;</tt> is most useful for expensive operations, such as <tt>&quot;blur&quot;</tt>: 

 <pre>
   rootalign keep { blur 20, root }
</pre> 

 This makes a blurred copy of the root background once, and on subsequent calls, just root-aligns it. Since <tt>&quot;blur&quot;</tt> is usually quite slow and <tt>&quot;rootalign&quot;</tt> is quite fast, this trades extra memory (for the cached blurred pixmap) with speed (blur only needs to be redone when root changes). 

 <i></i>&quot;load&quot;<i> caching</i> 

 The <tt>&quot;load&quot;</tt> operator itself does not keep images in memory, but as long as the image is still in memory, <tt>&quot;load&quot;</tt> will use the in-memory image instead of loading it freshly from disk. 

 That means that this expression: 

 <pre>
   keep { load &quot;$HOME/path...&quot; }
</pre> 

 Not only caches the image in memory, other terminal instances that try to <tt>&quot;load&quot;</tt> it can reuse that in-memory copy.

<h2>REFERENCE</h2>

<h3><font SIZE="-1">COMMAND LINE SWITCHES</font></h3>

<dl>
<dt>--background-expr perl-expression
<dd> Specifies the Perl expression to evaluate.
<dt>--background-border
<dd> By default, the expression creates an image that fills the full window, overwriting borders and any other areas, such as the scrollbar. 

 Specifying this flag changes the behaviour, so that the image only replaces the background of the character area.
<dt>--background-interval seconds
<dd> Since some operations in the underlying XRender extension can effectively freeze your X-server for prolonged time, this extension enforces a minimum time between updates, which is normally about 0.1 seconds. 

 If you want to do updates more often, you can decrease this safety interval with this switch.</dl>

<h3><font SIZE="-1">PROVIDERS/GENERATORS</font></h3>

 These functions provide an image, by loading it from disk, grabbing it from the root screen or by simply generating it. They are used as starting points to get an image you can play with.
<dl>
<dt>load $path
<dd> Loads the image at the given <tt>$path</tt>. The image is set to plane tiling mode. 

 If the image is already in memory (e.g. because another terminal instance uses it), then the in-memory copy is returned instead.
<dt>load_uc $path
<dd> Load uncached - same as load, but does not cache the image, which means it is <i>always</i> loaded from the filesystem again, even if another copy of it is in memory at the time.
<dt>root
<dd> Returns the root window pixmap, that is, hopefully, the background image of your screen. 

 This function makes your expression root sensitive, that means it will be reevaluated when the bg image changes.
<dt>solid $colour
<dd>
<dt>solid $width, $height, $colour
<dd> Creates a new image and completely fills it with the given colour. The image is set to tiling mode. 

 If <tt>$width</tt> and <tt>$height</tt> are omitted, it creates a 1x1 image, which is useful for solid backgrounds or for use in filtering effects.
<dt>clone $img
<dd> Returns an exact copy of the image. This is useful if you want to have multiple copies of the same image to apply different effects to.
<dt>merge $img ...
<dd> Takes any number of images and merges them together, creating a single image containing them all. The tiling mode of the first image is used as the tiling mode of the resulting image. 

 This function is called automatically when an expression returns multiple images.</dl>

<h3><font SIZE="-1">TILING MODES</font></h3>

 The following operators modify the tiling mode of an image, that is, the way that pixels outside the image area are painted when the image is used.
<dl>
<dt>tile $img
<dd> Tiles the whole plane with the image and returns this new image - or in other words, it returns a copy of the image in plane tiling mode. 

 Example: load an image and tile it over the background, without resizing. The <tt>&quot;tile&quot;</tt> call is superfluous because <tt>&quot;load&quot;</tt> already defaults to tiling mode. 

 <pre>
   tile load &quot;mybg.png&quot;
</pre>
<dt>mirror $img
<dd> Similar to tile, but reflects the image each time it uses a new copy, so that top edges always touch top edges, right edges always touch right edges and so on (with normal tiling, left edges always touch right edges and top always touch bottom edges). 

 Example: load an image and mirror it over the background, avoiding sharp edges at the image borders at the expense of mirroring the image itself 

 <pre>
   mirror load &quot;mybg.png&quot;
</pre>
<dt>pad $img
<dd> Takes an image and modifies it so that all pixels outside the image area become transparent. This mode is most useful when you want to place an image over another image or the background colour while leaving all background pixels outside the image unchanged. 

 Example: load an image and display it in the upper left corner. The rest of the space is left ``empty'' (transparent or whatever your compositor does in alpha mode, else background colour). 

 <pre>
   pad load &quot;mybg.png&quot;
</pre>
<dt>extend $img
<dd> Extends the image over the whole plane, using the closest pixel in the area outside the image. This mode is mostly useful when you use more complex filtering operations and want the pixels outside the image to have the same values as the pixels near the edge. 

 Example: just for curiosity, how does this pixel extension stuff work? 

 <pre>
   extend move 50, 50, load &quot;mybg.png&quot;
</pre></dl>

<h3><font SIZE="-1">VARIABLE VALUES</font></h3>

 The following functions provide variable data such as the terminal window dimensions. They are not (Perl-) variables, they just return stuff that varies. Most of them make your expression sensitive to some events, for example using <tt>&quot;TW&quot;</tt> (terminal width) means your expression is evaluated again when the terminal is resized.
<dl>
<dt><font SIZE="-1">TX</font>
<dd>
<dt><font SIZE="-1">TY</font>
<dd> Return the X and Y coordinates of the terminal window (the terminal window is the full window by default, and the character area only when in border-respect mode). 

 Using these functions makes your expression sensitive to window moves. 

 These functions are mainly useful to align images to the root window. 

 Example: load an image and align it so it looks as if anchored to the background (that's exactly what <tt>&quot;rootalign&quot;</tt> does btw.): 

 <pre>
   move -TX, -TY, keep { load &quot;mybg.png&quot; }
</pre>
<dt><font SIZE="-1">TW</font>
<dd>
<dt><font SIZE="-1">TH</font>
<dd> Return the width (<tt>&quot;TW&quot;</tt>) and height (<tt>&quot;TH&quot;</tt>) of the terminal window (the terminal window is the full window by default, and the character area only when in border-respect mode). 

 Using these functions makes your expression sensitive to window resizes. 

 These functions are mainly useful to scale images, or to clip images to the window size to conserve memory. 

 Example: take the screen background, clip it to the window size, blur it a bit, align it to the window position and use it as background. 

 <pre>
   clip move -TX, -TY, keep { blur 5, root }
</pre>
<dt><font SIZE="-1">FOCUS</font>
<dd> Returns a boolean indicating whether the terminal window has keyboard focus, in which case it returns true. 

 Using this function makes your expression sensitive to focus changes. 

 A common use case is to fade the background image when the terminal loses focus, often together with the <tt>&quot;-fade&quot;</tt> command line option. In fact, there is a special function for just that use case: <tt>&quot;focus_fade&quot;</tt>. 

 Example: use two entirely different background images, depending on whether the window has focus. 

 <pre><code>
FOCUS ? keep{load "has_focus.jpg"} : keep
{
    load "no_focus.jpg"
}
</code></pre>
<dt>now
<dd> Returns the current time as (fractional) seconds since the epoch. 

 Using this expression does <i>not</i> make your expression sensitive to time, but the next two functions do.
<dt>again $seconds
<dd> When this function is used the expression will be reevaluated again in <tt>$seconds</tt> seconds. 

 Example: load some image and rotate it according to the time of day (as if it were the hour pointer of a clock). Update this image every minute. 

 <pre>
   again 60;
   rotate 50, 50, (now % 86400) * -72 / 8640, scale keep { load &quot;myclock.png&quot; }
</pre>
<dt>counter $seconds
<dd> Like <tt>&quot;again&quot;</tt>, but also returns an increasing counter value, starting at 0, which might be useful for some simple animation effects.</dl>

<h3><font SIZE="-1">SHAPE CHANGING OPERATORS</font></h3>

 The following operators modify the shape, size or position of the image.
<dl>
<dt>clip $img
<dd>
<dt>clip $width, $height, $img
<dd>
<dt>clip $x, $y, $width, $height, $img
<dd> Clips an image to the given rectangle. If the rectangle is outside the image area (e.g. when <tt>$x</tt> or <tt>$y</tt> are negative) or the rectangle is larger than the image, then the tiling mode defines how the extra pixels will be filled. 

 If <tt>$x</tt> and <tt>$y</tt> are missing, then <tt>0</tt> is assumed for both. 

 If <tt>$width</tt> and <tt>$height</tt> are missing, then the window size will be assumed. 

 Example: load an image, blur it, and clip it to the window size to save memory. 

 <pre>
   clip keep { blur 10, load &quot;mybg.png&quot; }
</pre>
<dt>scale $img
<dd>
<dt>scale $size_factor, $img
<dd>
<dt>scale $width_factor, $height_factor, $img
<dd> Scales the image by the given factors in horizontal (<tt>$width</tt>) and vertical (<tt>$height</tt>) direction. 

 If only one factor is given, it is used for both directions. 

 If no factors are given, scales the image to the window size without keeping aspect.
<dt>resize $width, $height, $img
<dd> Resizes the image to exactly <tt>$width</tt> times <tt>$height</tt> pixels.
<dt>fit $img
<dd>
<dt>fit $width, $height, $img
<dd> Fits the image into the given <tt>$width</tt> and <tt>$height</tt> without changing aspect, or the terminal size. That means it will be shrunk or grown until the whole image fits into the given area, possibly leaving borders.
<dt>cover $img
<dd>
<dt>cover $width, $height, $img
<dd> Similar to <tt>&quot;fit&quot;</tt>, but shrinks or grows until all of the area is covered by the image, so instead of potentially leaving borders, it will cut off image data that doesn't fit.
<dt>move $dx, $dy, $img
<dd> Moves the image by <tt>$dx</tt> pixels in the horizontal, and <tt>$dy</tt> pixels in the vertical. 

 Example: move the image right by 20 pixels and down by 30. 

 <pre>
   move 20, 30, ...
</pre>
<dt>align $xalign, $yalign, $img
<dd> Aligns the image according to a factor - <tt>0</tt> means the image is moved to the left or top edge (for <tt>$xalign</tt> or <tt>$yalign</tt>), <tt>0.5</tt> means it is exactly centered and <tt>1</tt> means it touches the right or bottom edge. 

 Example: remove any visible border around an image, center it vertically but move it to the right hand side. 

 <pre>
   align 1, 0.5, pad $img
</pre>
<dt>center $img
<dd>
<dt>center $width, $height, $img
<dd> Centers the image, i.e. the center of the image is moved to the center of the terminal window (or the box specified by <tt>$width</tt> and <tt>$height</tt> if given). 

 Example: load an image and center it. 

 <pre>
  center keep { pad load &quot;mybg.png&quot; }
</pre>
<dt>rootalign $img
<dd> Moves the image so that it appears glued to the screen as opposed to the window. This gives the illusion of a larger area behind the window. It is exactly equivalent to <tt>&quot;move -TX, -TY&quot;</tt>, that is, it moves the image to the top left of the screen. 

 Example: load a background image, put it in mirror mode and root align it. 

 <pre>
   rootalign keep { mirror load &quot;mybg.png&quot; }
</pre> 

 Example: take the screen background and align it, giving the illusion of transparency as long as the window isn't in front of other windows. 

 <pre>
   rootalign root
</pre>
<dt>rotate $center_x, $center_y, $degrees, $img
<dd> Rotates the image clockwise by <tt>$degrees</tt> degrees, around the point at <tt>$center_x</tt> and <tt>$center_y</tt> (specified as factor of image width/height). 

 Example: rotate the image by 90 degrees around its center. 

 <pre>
   rotate 0.5, 0.5, 90, keep { load &quot;$HOME/mybg.png&quot; }
</pre></dl>

<h3><font SIZE="-1">COLOUR MODIFICATIONS</font></h3>

 The following operators change the pixels of the image.
<dl>
<dt>tint $color, $img
<dd> Tints the image in the given colour. 

 Example: tint the image red. 

 <pre>
   tint &quot;red&quot;, load &quot;rgb.png&quot;
</pre> 

 Example: the same, but specify the colour by component. 

 <pre>
   tint [1, 0, 0], load &quot;rgb.png&quot;
</pre>
<dt>shade $factor, $img
<dd> Shade the image by the given factor.
<dt>contrast $factor, $img
<dd>
<dt>contrast $r, $g, $b, $img
<dd>
<dt>contrast $r, $g, $b, $a, $img
<dd> Adjusts the <i>contrast</i> of an image. 

 The first form applies a single <tt>$factor</tt> to red, green and blue, the second form applies separate factors to each colour channel, and the last form includes the alpha channel. 

 Values from 0 to 1 lower the contrast, values higher than 1 increase the contrast. 

 Due to limitations in the underlying XRender extension, lowering contrast also reduces brightness, while increasing contrast currently also increases brightness.
<dt>brightness $bias, $img
<dd>
<dt>brightness $r, $g, $b, $img
<dd>
<dt>brightness $r, $g, $b, $a, $img
<dd> Adjusts the brightness of an image. 

 The first form applies a single <tt>$bias</tt> to red, green and blue, the second form applies separate biases to each colour channel, and the last form includes the alpha channel. 

 Values less than 0 reduce brightness, while values larger than 0 increase it. Useful range is from -1 to 1 - the former results in a black, the latter in a white picture. 

 Due to idiosyncrasies in the underlying XRender extension, biases less than zero can be <i>very</i> slow. 

 You can also try the experimental(!) <tt>&quot;muladd&quot;</tt> operator.
<dt>muladd $mul, $add, $img # <font SIZE="-1">EXPERIMENTAL</font>
<dd> First multiplies the pixels by <tt>$mul</tt>, then adds <tt>$add</tt>. This can be used to implement brightness and contrast at the same time, with a wider value range than contrast and brightness operators. 

 Due to numerous bugs in XRender implementations, it can also introduce a number of visual artifacts. 

 Example: increase contrast by a factor of <tt>$c</tt> without changing image brightness too much. 

 <pre>
   muladd $c, (1 - $c) * 0.5, $img
</pre>
<dt>blur $radius, $img
<dd>
<dt>blur $radius_horz, $radius_vert, $img
<dd> Gaussian-blurs the image with (roughly) <tt>$radius</tt> pixel radius. The radii can also be specified separately. 

 Blurring is often <i>very</i> slow, at least compared or other operators. Larger blur radii are slower than smaller ones, too, so if you don't want to freeze your screen for long times, start experimenting with low values for radius (&lt;5).
<dt>focus_fade $img
<dd>
<dt>focus_fade $factor, $img
<dd>
<dt>focus_fade $factor, $color, $img
<dd> Fades the image by the given factor (and colour) when focus is lost (the same as the <tt>&quot;-fade&quot;</tt>/<tt>&quot;-fadecolor&quot;</tt> command line options, which also supply the default values for <tt>&quot;factor&quot;</tt> and <tt>$color</tt>. Unlike with <tt>&quot;-fade&quot;</tt>, the <tt>$factor</tt> is a real value, not a percentage value (that is, 0..1, not 0..100). 

 Example: do the right thing when focus fading is requested. 

 <pre>
   focus_fade load &quot;mybg.jpg&quot;;
</pre></dl>

<h3><font SIZE="-1">OTHER STUFF</font></h3>

 Anything that didn't fit any of the other categories, even after applying force and closing our eyes.
<dl>
<dt>keep { ... }
<dd> This operator takes a code block as argument, that is, one or more statements enclosed by braces. 

 The trick is that this code block is only evaluated when the outcome changes - on other calls the <tt>&quot;keep&quot;</tt> simply returns the image it computed previously (yes, it should only be used with images). Or in other words, <tt>&quot;keep&quot;</tt> <i>caches</i> the result of the code block so it doesn't need to be computed again. 

 This can be extremely useful to avoid redoing slow operations - for example, if your background expression takes the root background, blurs it and then root-aligns it it would have to blur the root background on every window move or resize. 

 Another example is <tt>&quot;load&quot;</tt>, which can be quite slow. 

 In fact, urxvt itself encloses the whole expression in some kind of <tt>&quot;keep&quot;</tt> block so it only is reevaluated as required. 

 Putting the blur into a <tt>&quot;keep&quot;</tt> block will make sure the blur is only done once, while the <tt>&quot;rootalign&quot;</tt> is still done each time the window moves. 

 <pre>
   rootalign keep { blur 10, root }
</pre> 

 This leaves the question of how to force reevaluation of the block, in case the root background changes: If expression inside the block is sensitive to some event (root background changes, window geometry changes), then it will be reevaluated automatically as needed. 

</dl>

<h2>Index</h2>



<dt><a HREF="#lbAJ">REFERENCE</a>
<dd>

</dl>
