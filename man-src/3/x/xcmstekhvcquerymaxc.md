---
title: "xcmstekhvcquerymaxc(3)"
name: "xcmstekhvcquerymaxc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmstekhvcquerymaxc/"
description: "XcmsTekHVCQueryMaxC, XcmsTekHVCQueryMaxV, XcmsTekHVCQueryMaxVC, XcmsTekHVCQueryMaxVSamples, XcmsTekHVCQueryMinV – obtain the TekHVC coordinates"
---

<p>XcmsTekHVCQueryMaxC, XcmsTekHVCQueryMaxV, XcmsTekHVCQueryMaxVC, XcmsTekHVCQueryMaxVSamples, XcmsTekHVCQueryMinV &#8211; obtain the TekHVC coordinates </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XcmsTekHVCQueryMaxC(XcmsCCC <i>ccc</i>, XcmsFloat <i>hue</i>, XcmsFloat <i>value</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsTekHVCQueryMaxV(XcmsCCC <i>ccc</i>, XcmsFloat <i>hue</i>, XcmsFloat <i>chroma</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsTekHVCQueryMaxVC(XcmsCCC <i>ccc</i>, XcmsFloat <i>hue</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsTekHVCQueryMaxVSamples(XcmsCCC <i>ccc</i>, XcmsFloat <i>hue</i>, XcmsColor <i>colors_return[]</i>, unsigned int <i>nsamples</i>);</p>
<dd>Status XcmsTekHVCQueryMinV(XcmsCCC <i>ccc</i>, XcmsFloat <i>hue</i>, XcmsFloat <i>chroma</i>, XcmsColor *<i>color_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ccc</i></p>
<dd>Specifies the CCC. Note that the CCC&#8217;s Client White Point and White Point Adjustment procedures are ignored.</p>
<dt><i>chroma</i></p>
<dd>Specifies the chroma at which to find maximum Value (MaxV).</p>
<dt><i>colors_return</i></p>
<dd>Returns nsamples of color specifications in XcmsTekHVC such that the Chroma is the maximum attainable for the Value and Hue. The white point associated with the returned color specification is the Screen White Point. The value returned in the pixel member is undefined.</p>
<dt><i>color_return</i></p>
<dd>Returns the maximum Chroma along with the actual Hue and Value (MaxC), maximum Value along with the Hue and Chroma (MaxV), color specification in XcmsTekHVC for the maximum Chroma, the Value at which that maximum Chroma is reached and actual Hue (MaxVC) or minimum Value and the actual Hue and Chroma (MinL) at which the maximum Chroma (MaxC and MaxVC), maximum Value (MaxV), or minimum Value (MinL) was found. The white point associated with the returned color specification is the Screen White Point. The value returned in the pixel member is undefined.</p>
<dt><i>hue</i></p>
<dd>Specifies the Hue in which to find the maximum Chroma (MaxC and MaxVC), maximum Value (MaxV), the maximum Chroma/Value samples (MaxVSamples), or the minimum Value (MinL).</p>
<dt><i>nsamples</i></p>
<dd>Specifies the number of samples.</p>
<dt><i>value</i></p>
<dd>Specifies the Value in which to find the maximum Chroma (MaxC) or minimum Value (MinL).</dl>
<h2>Description</h2>
<p>The <code>XcmsTekHVCQueryMaxC</code> function, given a Hue and Value, determines the maximum Chroma in TekHVC color space displayable by the screen. It returns the maximum Chroma along with the actual Hue and Value at which the maximum Chroma was found. </p>
<p> The <code>XcmsTekHVCQueryMaxV</code> function, given a Hue and Chroma, determines the maximum Value in TekHVC color space displayable by the screen. It returns the maximum Value and the actual Hue and Chroma at which the maximum Value was found. </p>
<p> The <code>XcmsTekHVCQueryMaxVC</code> function, given a Hue, determines the maximum Chroma in TekHVC color space displayable by the screen and the Value at which that maximum Chroma is reached. It returns the maximum Chroma, the Value at which that maximum Chroma is reached, and the actual Hue for which the maximum Chroma was found. </p>
<p> The <code>XcmsTekHVCQueryMaxVSamples</code> returns nsamples of maximum Value, the Chroma at which that maximum Value is reached, and the actual Hue for which the maximum Chroma was found. These sample points may then be used to plot the maximum Value/Chroma boundary of the screen&#8217;s color gamut for the specified Hue in TekHVC color space. </p>
<p> The <code>XcmsTekHVCQueryMinV</code> function, given a Hue and Chroma, determines the minimum Value in TekHVC color space displayable by the screen. It returns the minimum Value and the actual Hue and Chroma at which the minimum Value was found.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcmscielabquerymaxc/">XcmsCIELabQueryMaxC</a>(3), <a href="/docs/linux/man/3-xcmscieluvquerymaxc/">XcmsCIELuvQueryMaxC</a>(3), <a href="/docs/linux/man/3-xcmsqueryblack/">XcmsQueryBlack</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
