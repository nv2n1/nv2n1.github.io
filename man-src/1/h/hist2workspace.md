---
title: "hist2workspace(1)"
name: "hist2workspace"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hist2workspace/"
description: "hist2workspace – utility to create RooFit/RooStats workspace from histograms"
---

<h2 class="name">NAME</h2>
<p> hist2workspace &#8211; utility to create RooFit/RooStats workspace from histograms </p>
<h2>SYNOPSIS</h2>
<p> <code>hist2workspace [option] input.xml</code></p>
<h2>DESCRIPTION</h2>
<p> <code>hist2workspace</code> is a utility to create RooFit/RooStats workspace from histograms</p>
<h2>OPTIONS</h2>
<p> <code>-standard_form</code> default model, which creates an extended PDF that interpolates between RooHistFuncs. This is much faster for models with many bins and uses significantly less memory.<br />
 <code>-number_counting_form</code> this was the original model in 5.28 (without patches). It uses a Poisson for each bin of the histogram. This can become slow and memory intensive when there are many bins. </p>
<h2>Prepare working area</h2>
<p> The ROOT release ships with a script <code>prepareHistFactory</code> in the $ROOTSYS/bin directory that prepares a working area. It creates a results/, data/, and config/ directory. It also copies the HistFactorySchema.dtd and example XML files into the config/ directory. Additionally, it copies a root file into the data/ directory for use with the examples. </p>
<h2>HistFactorySchema.dtd</h2>
<p> This file is located in $ROOTSYS/etc/ specifies the XML schema. It is typically placed in the config/ directory of a working area together with the top-level XML file and the individual channel XML files. The user should not modify this file.<br />
 The HistFactorySchema.dtd is commented to specify exactly the meaning of the various options. </p>
<h2>Top-Level XML File</h2>
<p> (see for example $ROOTSYS/tutorials/histfactory/example.xml) This file is edited by the user. It specifies<br />
&nbsp;<wbr>&#8211; A top level&nbsp;<wbr>&#8216;Combination&#8217;&nbsp;<wbr>that is composed of:<br />
&nbsp;<wbr>&#8211; several&nbsp;<wbr>&#8216;Channels&#8217;, which are described in separate XML files.<br />
&nbsp;<wbr>&#8211; several&nbsp;<wbr>&#8216;Measurements&#8217;&nbsp;<wbr>(corresponding to a full fit of the model)&nbsp;<wbr>each of which specifies<br />
&#8211; a name for this measurement to be used in tables and files<br />
&#8211; what is the luminosity associated to the measurement in picobarns<br />
&#8211; which bins of the histogram should be used<br />
&#8211; what is the relative uncertainty on the luminosity<br />
&#8211; what is&nbsp;<wbr>(are)&nbsp;<wbr>the parameter(s)&nbsp;<wbr>of interest that will be measured<br />
&#8211; which parameters should be fixed/floating&nbsp;<wbr>(eg. nuisance parameters)<br />
&#8211; which type of constriants are desired<br />
&#8211; Gaussian by default<br />
&#8211; Gamma, LogNormal, and Uniform are also supported<br />
&#8211; if the tool should export the model only and skip the default fit </p>
<h2>Channel XML Files</h2>
<p> (see for example $ROOTSYS/tutorials/histfactory/example_channel.xml) This file is edited by the user. It specifies for each channel<br />
&nbsp;<wbr>&#8211; observed data<br />
&#8211; if absent the tool will use the expectation, which is useful for expected sensitivity<br />
&nbsp;<wbr>&#8211; several&nbsp;<wbr>&#8216;Samples&#8217;&nbsp;<wbr>(eg. signal, bkg1, bkg2, &#8230;), each of which has:<br />
&#8211; a name<br />
&#8211; if the sample is normalized by theory&nbsp;<wbr>(eg N&nbsp;<wbr>=&nbsp;<wbr>L*sigma)&nbsp;<wbr>or not&nbsp;<wbr>(eg. data driven)<br />
&#8211; a nominal expectation histogram<br />
&#8211; a named&nbsp;<wbr>&#8216;Normalization Factor&#8217;&nbsp;<wbr>(which can be fixed or allowed to float in a fit)<br />
&#8211; several&nbsp;<wbr>&#8216;Overall Systematics&#8217;&nbsp;<wbr>in normalization with:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; a name<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>+/- 1 sigma variations&nbsp;<wbr>(eg. 1.05 and 0.95 for a 5%&nbsp;<wbr>uncertainty)<br />
&#8211; several&nbsp;<wbr>&#8216;Histogram Systematics&#8217;&nbsp;<wbr>in shape with:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; a name&nbsp;<wbr>(which can be shared with the OverallSyst if correlated)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>+/- 1 sigma variational histograms</p>
<h2>ORIGINAL AUTHORS</h2>
<dl>
<dt>
<dd> <code>Kyle Cranmer</code> , <code>Akira Shibata</code> , and <code>Dominique Tardif</code></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA </p>
<h2>Index</h2>
