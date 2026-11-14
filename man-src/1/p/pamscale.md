---
title: "pamscale(1)"
name: "pamscale"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamscale/"
description: "pamscale – scale a Netpbm image"
---

<h2 class="name">NAME</h2>
<p> pamscale &#8211; scale a Netpbm image</p>
<h2>SYNOPSIS</h2>
<pre><code>
   pamscale
      [ 
         scale_factor 
         |
         {-xyfit | -xyfill | -xysize} cols rows 
         |
         -reduce reduction_factor 
         |
         [-xsize=cols | -width=cols | -xscale=factor]
         [-ysize=rows | -height=rows | -yscale=factor]
         |
         -pixels n
      ]
      [
         [-verbose]
         [
            -nomix 
            |
            -filter=functionName [-window=functionName]
         ]
         [-linear]
   }
   [pnmfile]
</code></pre>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamscale</code> scales a Netpbm image by a specified factor, or scales individually horizontally and vertically by specified factors. </p>
<p> You can either enlarge (scale factor &gt; 1) or reduce (scale factor &lt; 1). </p>
<p> <code>pamscale</code> work on multi-image streams, scaling each one independently. But before Netpbm 10.49 (December 2009), it scales only the first image and ignores the rest of the stream. </p>
<h3>The Scale Factors</h3>
<p> The options <code>-width</code>, <code>-height</code>, <code>-xsize</code>, <code>-ysize</code>, <code>-xscale</code>, <code>-yscale</code>, <code>-xyfit</code>, <code>-xyfill</code>, <code>-reduce</code>, and <code>-pixels</code> control the amount of scaling. For backward compatibility, there is also <code>-xysize</code> and the <i>scale_factor</i> argument, but you shouldn&#8217;t use those. </p>
<p> <code>-width</code> and <code>-height</code> specify the width and height in pixels you want the resulting image to be. See below for rules when you specify one and not the other. </p>
<p> <code>-xsize</code> and <code>-ysize</code> are synonyms for <code>-width</code> and <code>-height</code>, respectively. </p>
<p> <code>-xscale</code> and <code>-yscale</code> tell the factor by which you want the width and height of the image to change from source to result (e.g. <code>-xscale 2</code> means you want to double the width; <code>-xscale .5</code> means you want to halve it). See below for rules when you specify one and not the other. </p>
<p> When you specify an absolute size or scale factor for both dimensions, <code>pamscale</code> scales each dimension independently without consideration of the aspect ratio. </p>
<p> If you specify one dimension as a pixel size and don&#8217;t specify the other dimension, <code>pamscale</code> scales the unspecified dimension to preserve the aspect ratio. </p>
<p> If you specify one dimension as a scale factor and don&#8217;t specify the other dimension, <code>pamscale</code> leaves the unspecified dimension unchanged from the input. </p>
<p> If you specify the <i>scale_factor</i> parameter instead of dimension options, that is the scale factor for both dimensions. It is equivalent to <code>-xscale=</code><i>scale_factor</i><code> -yscale=</code><i>scale_factor</i>. </p>
<p> Specifying the <code>-reduce</code> <i>reduction_factor</i> option is equivalent to specifying the <i>scale_factor </i> parameter, where <i>scale_factor</i> is the reciprocal of <i>reduction_factor</i>. </p>
<p> <code>-xyfit</code> specifies a bounding box. <code>pamscale</code> scales the input image to the largest size that fits within the box, while preserving its aspect ratio. <code>-xysize</code> is a synonym for this. Before Netpbm 10.20 (January 2004), <code>-xyfit</code> did not exist, but <code>-xysize</code> did. </p>
<p> <code>-xyfill</code> is similar, but <code>pamscale</code> scales the input image to the smallest size that completely fills the box, while preserving its aspect ratio. This option has existed since Netpbm 10.20 (January 2004). </p>
<p> <code>-pixels</code> specifies a maximum total number of output pixels. <code>pamscale</code> scales the image down to that number of pixels. If the input image is already no more than that many pixels, <code>pamscale</code> just copies it as output; <code>pamscale</code> does not scale up with <code>-pixels</code>. </p>
<p> If you enlarge by a factor of 3 or more, you should probably add a <i>pnmsmooth</i> step; otherwise, you can see the original pixels in the resulting image. </p>
<h3>Usage Notes</h3>
<p> A useful application of <code>pamscale</code> is to blur an image. Scale it down (without <code>-nomix</code>) to discard some information, then scale it back up using <code>pamstretch</code>. </p>
<p> Or scale it back up with <code>pamscale</code> and create a &#8216;pixelized&#8217; image, which is sort of a computer-age version of blurring. </p>
<h3>Transparency</h3>
<p> <code>pamscale</code> understands transparency and properly mixes pixels considering the pixels&#8217; transparency. </p>
<p> Proper mixing <i>does not</i> mean just mixing the transparency value and the color component values separately. In a PAM image, a pixel which is not opaque represents a color that contains light of the foreground color indicated explicitly in the PAM and light of a background color to be named later. But the numerical scale of a color component sample in a PAM is as if the pixel is opaque. So a pixel that is supposed to contain half-strength red light for the foreground plus some light from the background has a red color sample that says <i>full</i> red and a transparency sample that says 50% opaque. In order to mix pixels, you have to first convert the color sample values to numbers that represent amount of light directly (i.e. multiply by the opaqueness) and after mixing, convert back (divide by the opaqueness). </p>
<h3>Input And Output Image Types</h3>
<p> <code>pamscale</code> produces output of the same type (and tuple type if the type is PAM) as the input, except if the input is PBM. In that case, the output is PGM with maxval 255. The purpose of this is to allow meaningful pixel mixing. Note that there is no equivalent exception when the input is PAM. If the PAM input tuple type is BLACKANDWHITE, the PAM output tuple type is also BLACKANDWHITE, and you get no meaningful pixel mixing. </p>
<p> If you want PBM output with PBM input, use <code>pamditherbw</code> to convert <code>pamscale</code>&#8216;s output to PBM. Also consider <code>pbmreduce</code>. </p>
<p> <code>pamscale</code>&#8216;s function is essentially undefined for PAM input images that are not of tuple type RGB, GRAYSCALE, BLACKANDWHITE, or the _ALPHA variations of those. (By standard Netpbm backward compatibility, this includes PBM, PGM, and PPM images). </p>
<p> You might think it would have an obvious effect on other tuple types, but remember that the aforementioned tuple types have gamma-adjusted sample values, and <code>pamscale</code> uses that fact in its calculations. And it treats a transparency plane different from any other plane. </p>
<p> <code>pamscale</code> does not simply reject unrecognized tuple types because there&#8217;s a possibility that just by coincidence you can get useful function out of it with some other tuple type and the right combination of options (consider <code>-linear</code> in particular). </p>
<h3>Methods Of Scaling</h3>
<p> There are numerous ways to scale an image. <code>pamscale</code> implements a bunch of them; you select among them with invocation options. </p>
<p> <code>Pixel Mixing</code> </p>
<p> Pamscale&#8217;s default method is pixel mixing. To understand this, imagine the source image as composed of square tiles. Each tile is a pixel and has uniform color. The tiles are all the same size. Now take a transparent sheet the size of the target image, marked with a square grid of tiles the same size. Stretch or compress the source image to the size of the sheet and lay the sheet over the source. </p>
<p> Each cell in the overlay grid stands for a pixel of the target image. For example, if you are scaling a 100&#215;200 image up by 1.5, the source image is 100 x 200 tiles, and the transparent sheet is marked off in 150 x 300 cells. </p>
<p> Each cell covers parts of multiple tiles. To make the target image, just color in each cell with the color which is the average of the colors the cell covers &#8212; weighted by the amount of that color it covers. A cell in our example might cover 4/9 of a blue tile, 2/9 of a red tile, 2/9 of a green tile, and 1/9 of a white tile. So the target pixel would be somewhat unsaturated blue. </p>
<p> When you are scaling up or down by an integer, the results are simple. When scaling up, pixels get duplicated. When scaling down, pixels get thrown away. In either case, the colors in the target image are a subset of those in the source image. </p>
<p> When the scale factor is weirder than that, the target image can have colors that didn&#8217;t exist in the original. For example, a red pixel next to a white pixel in the source might become a red pixel, a pink pixel, and a white pixel in the target. </p>
<p> This method tends to replicate what the human eye does as it moves closer to or further away from an image. It also tends to replicate what the human eye sees, when far enough away to make the pixelization disappear, if an image is not made of pixels and simply stretches or shrinks. </p>
<p> <code>Discrete Sampling</code> </p>
<p> Discrete sampling is basically the same thing as pixel mixing except that, in the model described above, instead of averaging the colors of the tiles the cell covers, you pick the one color that covers the most area. </p>
<p> The result you see is that when you enlarge an image, pixels get duplicated and when you reduce an image, some pixels get discarded. </p>
<p> The advantage of this is that you end up with an image made from the same color palette as the original. Sometimes that&#8217;s important. </p>
<p> The disadvantage is that it distorts the picture. If you scale up by 1.5 horizontally, for example, the even numbered input pixels are doubled in the output and the odd numbered ones are copied singly. If you have a bunch of one pixel wide lines in the source, you may find that some of them stretch to 2 pixels, others remain 1 pixel when you enlarge. When you reduce, you may find that some of the lines disappear completely. </p>
<p> You select discrete sampling with <code>pamscale</code>&#8216;s <code>-nomix</code> option. </p>
<p> Actually, <code>-nomix</code> doesn&#8217;t do exactly what I described above. It does the scaling in two passes &#8211; first horizontal, then vertical. This can produce slightly different results. </p>
<p> There is one common case in which one often finds it burdensome to have <code>pamscale</code> make up colors that weren&#8217;t there originally: Where one is working with an image format such as GIF that has a limited number of possible colors per image. If you take a GIF with 256 colors, convert it to PPM, scale by .625, and convert back to GIF, you will probably find that the reduced image has way more than 256 colors, and therefore cannot be converted to GIF. One way to solve this problem is to do the reduction with discrete sampling instead of pixel mixing. Probably a better way is to do the pixel mixing, but then color quantize the result with <code>pnmquant</code> before converting to GIF. </p>
<p> When the scale factor is an integer (which means you&#8217;re scaling up), discrete sampling and pixel mixing are identical &#8212; output pixels are always just N copies of the input pixels. In this case, though, consider using <code>pamstretch</code> instead of <code>pamscale</code> to get the added pixels interpolated instead of just copied and thereby get a smoother enlargement. </p>
<p> <code>pamscale</code>&#8216;s discrete sampling is faster than pixel mixing, but <code>pamenlarge</code> is faster still. <code>pamenlarge</code> works only on integer enlargements. </p>
<p> discrete sampling (<code>-nomix</code>) was new in Netpbm 9.24 (January 2002). </p>
<p> <code>Resampling</code> </p>
<p> Resampling assumes that the source image is a discrete sampling of some original continuous image. That is, it assumes there is some non-pixelized original image and each pixel of the source image is simply the color of that image at a particular point. Those points, naturally, are the intersections of a square grid. </p>
<p> The idea of resampling is just to compute that original image, then sample it at a different frequency (a grid of a different scale). </p>
<p> The problem, of course, is that sampling necessarily throws away the information you need to rebuild the original image. So we have to make a bunch of assumptions about the makeup of the original image. </p>
<p> You tell <code>pamscale</code> to use the resampling method by specifying the <code>-filter</code> option. The value of this option is the name of a function, from the set listed below. </p>
<p> <code>To explain resampling, we are going to talk about a simple one dimensional scaling</code> &#8212; scaling a single row of grayscale pixels horizontally. If you can understand that, you can easily understand how to do a whole image: Scale each of the rows of the image, then scale each of the resulting columns. And scale each of the color component planes separately. </p>
<p> As a first step in resampling, <code>pamscale</code> converts the source image, which is a set of discrete pixel values, into a continuous step function. A step function is a function whose graph is a staircase-y thing. </p>
<p> Now, we convolve the step function with a proper scaling of the filter function that you identified with <code>-filter</code>. If you don&#8217;t know what the mathematical concept of convolution (convolving) is, you are officially lost. You cannot understand this explanation. The result of this convolution is the imaginary original continuous image we&#8217;ve been talking about. </p>
<p> Finally, we make target pixels by picking values from that function. </p>
<p> To understand what is going on, we use Fourier analysis: </p>
<p> The idea is that the only difference between our step function and the original continuous function (remember that we constructed the step function from the source image, which is itself a sampling of the original continuous function) is that the step function has a bunch of high frequency Fourier components added. If we could chop out all the higher frequency components of the step function, and know that they&#8217;re all higher than any frequency in the original function, we&#8217;d have the original function back. </p>
<p> The resampling method <i>assumes</i> that the original function was sampled at a high enough frequency to form a perfect sampling. A perfect sampling is one from which you can recover exactly the original continuous function. The Nyquist theorem says that as long as your sample rate is at least twice the highest frequency in your original function, the sampling is perfect. So we <i>assume</i> that the image is a sampling of something whose highest frequency is half the sample rate (pixel resolution) or less. Given that, our filtering does in fact recover the original continuous image from the samples (pixels). </p>
<p> To chop out all the components above a certain frequency, we just multiply the Fourier transform of the step function by a rectangle function. </p>
<p> We could find the Fourier transform of the step function, multiply it by a rectangle function, and then Fourier transform the result back, but there&#8217;s an easier way. Mathematicians tell us that multiplying in the frequency domain is equivalent to convolving in the time domain. That means multiplying the Fourier transform of F by a rectangle function R is the same as convolving F with the Fourier transform of R. It&#8217;s a lot better to take the Fourier transform of R, and build it into <code>pamscale</code> than to have <code>pamscale</code> take the Fourier transform of the input image dynamically. </p>
<p> That leaves only one question: What <i>is</i> the Fourier transform of a rectangle function? Answer: sinc. Recall from math that sinc is defined as sinc(x) = sin(PI*x)/PI*x. </p>
<p> Hence, when you specify <code>-filter=sinc</code>, you are effectively passing the step function of the source image through a low pass frequency filter and recovering a good approximation of the original continuous image. </p>
<p> <code>Refiltering</code> </p>
<p> There&#8217;s another twist: If you simply sample the reconstructed original continuous image at the new sample rate, and that new sample rate isn&#8217;t at least twice the highest frequency in the original continuous image, you won&#8217;t get a perfect sampling. In fact, you&#8217;ll get something with ugly aliasing in it. Note that this can&#8217;t be a problem when you&#8217;re scaling up (increasing the sample rate), because the fact that the old sample rate was above the Nyquist level means so is the new one. But when scaling down, it&#8217;s a problem. Obviously, you have to give up image quality when scaling down, but aliasing is not the best way to do it. It&#8217;s better just to remove high frequency components from the original continuous image before sampling, and then get a perfect sampling of that. </p>
<p> Therefore, <code>pamscale</code> filters out frequencies above half the new sample rate before picking the new samples. </p>
<p> <code>Approximations</code> </p>
<p> Unfortunately, <code>pamscale</code> doesn&#8217;t do the convolution precisely. Instead of evaluating the filter function at every point, it samples it &#8212; assumes that it doesn&#8217;t change any more often than the step function does. <code>pamscale</code> could actually do the true integration fairly easily. Since the filter functions are built into the program, the integrals of them could be too. Maybe someday it will. </p>
<p> There is one more complication with the Fourier analysis. sinc has nonzero values on out to infinity and minus infinity. That makes it hard to compute a convolution with it. So instead, there are filter functions that approximate sinc but are nonzero only within a manageable range. To get those, you multiply the sinc function by a <i>window function</i>, which you select with the <code>-window</code> option. The same holds for other filter functions that go on forever like sinc. By default, for a filter that needs a window function, the window function is the Blackman function. </p>
<p> <code>Filter Functions Besides Sinc</code> </p>
<p> The math described above works only with sinc as the filter function. <code>pamscale</code> offers many other filter functions, though. Some of these approximate sinc and are faster to compute. For most of them, I have no idea of the mathematical explanation for them, but people do find they give pleasing results. They may not be based on resampling at all, but just exploit the convolution that is coincidentally part of a resampling calculation. </p>
<p> For some filter functions, you can tell just by looking at the convolution how they vary the resampling process from the perfect one based on sinc: </p>
<p> The impulse filter assumes that the original continuous image is in fact a step function &#8212; the very one we computed as the first step in the resampling. This is mathematically equivalent to the discrete sampling method. </p>
<p> The box (rectangle) filter assumes the original image is a piecewise linear function. Its graph just looks like straight lines connecting the pixel values. This is mathematically equivalent to the pixel mixing method (but mixing brightness, not light intensity, so like <code>pamscale -linear</code>) when scaling down, and interpolation (ala <code>pamstretch</code>) when scaling up. </p>
<p> <code>Gamma</code> </p>
<p> <code>pamscale</code> assumes the underlying continuous function is a function of brightness (as opposed to light intensity), and therefore does all this math using the gamma-adjusted numbers found in a PNM or PAM image. The <code>-linear</code> option is not available with resampling (it causes <code>pamscale</code> to fail), because it wouldn&#8217;t be useful enough to justify the implementation effort. </p>
<p> Resampling (<code>-filter</code>) was new in Netpbm 10.20 (January 2004). </p>
<p> <code>The filter functions</code> </p>
<p> Here is a list of the function names you can specify for the <code>-filter</code> option. For most of them, you&#8217;re on your own to figure out just what the function is and what kind of scaling it does. These are common functions from mathematics. </p>
<dl>
<dt>point</p>
<dd> The graph of this is a single point at X=0, Y=1. </p>
<dt>box</p>
<dd> The graph of this is a rectangle sitting on the X axis and centered on the Y axis with height 1 and base 1. </p>
<dt>triangle</p>
<dd> The graph of this is an isosceles triangle sitting on the X axis and centered on the Y axis with height 1 and base 2. </p>
<dt>quadratic</p>
<dd>
<dt>cubic</p>
<dd>
<dt>catrom</p>
<dd>
<dt>mitchell</p>
<dd>
<dt>gauss</p>
<dd>
<dt>sinc</p>
<dd>
<dt>bessel</p>
<dd>
<dt>hanning</p>
<dd>
<dt>hamming</p>
<dd>
<dt>blackman</p>
<dd>
<dt>kaiser</p>
<dd>
<dt>normal</p>
<dd>
<dt>hermite</p>
<dd>
<dt>lanczos</p>
<dd> Not documented </p>
</dl>
<h3>Linear vs Gamma-adjusted</h3>
<p> The pixel mixing scaling method described above involves intensities of pixels (more precisely, it involves individual intensities of primary color components of pixels). But the PNM and PNM-equivalent PAM image formats represent intensities with gamma-adjusted numbers that are not linearly proportional to intensity. So <code>pamscale</code>, by default, performs a calculation on each sample read from its input and each sample written to its output to convert between these gamma-adjusted numbers and internal intensity-proportional numbers. </p>
<p> Sometimes you are not working with true PNM or PAM images, but rather a variation in which the sample values are in fact directly proportional to intensity. If so, use the <code>-linear</code> option to tell <code>pamscale</code> this. <code>pamscale</code> then will skip the conversions. </p>
<p> The conversion takes time. In one experiment, it increased by a factor of 10 the time required to reduce an image. And the difference between intensity-proportional values and gamma-adjusted values may be small enough that you would barely see a difference in the result if you just pretended that the gamma-adjusted values were in fact intensity-proportional. So just to save time, at the expense of some image quality, you can specify <code>-linear</code> even when you have true PPM input and expect true PPM output. </p>
<p> For the first 13 years of Netpbm&#8217;s life, until Netpbm 10.20 (January 2004), <code>pamscale</code>&#8216;s predecessor <code>pnmscale</code> always treated the PPM samples as intensity-proportional even though they were not, and drew few complaints. So using <code>-linear</code> as a lie is a reasonable thing to do if speed is important to you. But if speed is important, you also should consider the <code>-nomix</code> option and <code>pnmscalefixed</code>. </p>
<p> Another technique to consider is to convert your PNM image to the linear variation with <code>pnmgamma</code>, run <code>pamscale</code> on it and other transformations that like linear PNM, and then convert it back to true PNM with <code>pnmgamma -ungamma</code>. <code>pnmgamma</code> is often faster than <code>pamscale</code> in doing the conversion. </p>
<p> With <code>-nomix</code>, <code>-linear</code> has no effect. That&#8217;s because <code>pamscale</code> does not concern itself with the meaning of the sample values in this method; <code>pamscale</code> just copies numbers from its input to its output. </p>
<h3>Precision</h3>
<p> <code>pamscale</code> uses floating point arithmetic internally. There is a speed cost associated with this. For some images, you can get the acceptable results (in fact, sometimes identical results) faster with <code>pnmscalefixed</code>, which uses fixed point arithmetic. <code>pnmscalefixed</code> may, however, distort your image a little. See the <code>pnmscalefixed</code> user manual for a complete discussion of the difference. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmscalefixed/">pnmscalefixed</a></code>(1) , <code><a href="/docs/linux/man/1-pamstretch/">pamstretch</a></code>(1) , <code><a href="/docs/linux/man/1-pamditherbw/">pamditherbw</a></code>(1) , <code><a href="/docs/linux/man/1-pbmreduce/">pbmreduce</a></code>(1) , <code><a href="/docs/linux/man/1-pbmpscale/">pbmpscale</a></code>(1) , <code><a href="/docs/linux/man/1-pamenlarge/">pamenlarge</a></code>(1) , <code><a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a></code>(1) , <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) , <code><a href="/docs/linux/man/1-pnmgamma/">pnmgamma</a></code>(1) , <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamscale</code> was new in Netpbm 10.20 (January 2004). It was adapted from, and obsoleted, <code>pnmscale</code>. <code>pamscale</code>&#8216;s primary difference from <code>pnmscale</code> is that it handles the PAM format and uses the &quot;pam&quot; facilities of the Netpbm programming library. But it also added the resampling class of scaling method. Furthermore, it properly does its pixel mixing arithmetic (by default) using intensity-proportional values instead of the gamma-adjusted values the <code>pnmscale</code> uses. To get the old <code>pnmscale</code> arithmetic, you can specify the <code>-linear</code> option. </p>
<p> The intensity proportional stuff came out of suggestions by <i>Adam M Costello</i> in January 2004. </p>
<p> The resampling algorithms are mostly taken from code contributed by <i>Michael Reinelt</i> in December 2003. </p>
<p> The version of <code>pnmscale</code> from which <code>pamscale</code> was derived, itself evolved out of the original Pbmplus version of <code>pnmscale</code> by Jef Poskanzer (1989, 1991). But none of that original code remains. </p>
<h2>Index</h2>
