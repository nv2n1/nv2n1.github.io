---
title: "qos(7)"
name: "qos"
section: "7"
letter: "q"
url: "/docs/linux/man/7-qos/"
description: "qos – Quality of Service specification"
---

<p>qos &#8211; Quality of Service specification</p>
<h2>Description</h2>
<p>The <code>text2qos</code> and <code>qos2text</code> functions use the format described in this man page. Because all standard ATM tools on Linux use those functions to convert to or from the textual representation of QOS specifications, they expect them in the same format too. </p>
<p> The most fundamental parameters are the <i>traffic class</i> and the <i>AAL (ATM Adaption Layer) type</i>. If the connection is bi-directional, both directions have the same traffic class and the same AAL type. The traffic class and the AAL type are the first elements (in any order) in a QOS specification. The traffic class is the only required element. If the AAL type is omitted, the application will provide a default value. The following traffic classes are recognized:</p>
<dl>
<dt><code>ubr</code></p>
<dd>Unassigned Bit Rate</p>
<dt><code>cbr</code></p>
<dd>Constant Bit Rate</p>
<dt><code>abr</code></p>
<dd>Available Bit Rate</dl>
<p> The following AAL types are recognized:</p>
<dl>
<dt><code>aal0</code></p>
<dd>(&quot;raw ATM&quot;)</p>
<dt><code>aal5</code></p>
<dd></dl>
<p> If both, the traffic class and the AAL type are specified, they are separated by a comma. </p>
<p> If more parameters are supplied, the traffic class and AAL type must be followed by a colon. Traffic parameters can be specified independently for the transmit and the receive direction. Their parameter lists are prefixed with <code>tx:</code> and <code>rx:</code>, respectively. If both parameter lists are present, the <code>tx:</code> list must precede the <code>rx:</code> list. If a parameter is equal for both directions, it can be placed in a common parameter list (without prefix). The general format is as follows: </p>
<p> <i>class_and_aal</i><code>:</code><i>common_list</i>,tx:<i>list</i><code>,rx:</code><i>list</i> </p>
<p> Each list consists of elements specifying a parameter. Elements can appear in any order and they are separated with commas. The following elements are recognized:</p>
<dl>
<dt><code>pcr=</code><i>rate</i></p>
<dd>is a synonym for <code>max_pcr=</code><i>rate</i></p>
<dt><code>max_pcr=</code><i>rate</i></p>
<dd>The upper limit for the peak cell rate to assign. If omitted, any rate up to link speed may be chosen.</p>
<dt><code>min_pcr=</code><i>rate</i></p>
<dd>The lower limit for the peak cell rate to assign. If omitted, any rate above zero can be chosen.</p>
<dt><code>sdu=</code><i>size</i></p>
<dd>is a synonym for <code>max_sdu=</code><i>size</i></p>
<dt><code>max_sdu=</code><i>size</i></p>
<dd>The size of the largest packet that may be sent or received. If omitted, a context-dependent default value is used.</dl>
<p> Values are specified as follows:</p>
<dl>
<dt><i>rate</i></p>
<dd>The (decimal) rate, optionally followed by a unit. The unit may be prefixed with one of the multipliers <code>k</code>, <code>M</code>, or <code>G</code>, meaning 1&#8217;000, 1&#8217;000&#8217;000, or 1&#8217;000&#8217;000&#8217;000, respectively. The units <code>cps</code> (cells per second) and <code>bps</code> (bits per second) are recognized. If multiplier and unit are omitted, cells per second are assumed. Note that the rate is always converted to cells per second, so rounding errors may occur when specifying the rate in bits per second. Rates measured in bits per second are considered to be user data rates, i.e. one cell corresponds to 384 bits. The rate can be a fractional value, e.g. <code>1.3Mbps</code>. It is an error to specify only a multiplier without a unit. Link speed can be indicated by using the keyword <code>max</code> as the rate.</p>
<dt><i>size</i></p>
<dd>The (decimal) number of bytes.</dl>
<p> The <code>tx:</code> or <code>rx:</code> lists may also just contain the single element <code>none</code>, which indicates that the corresponding direction is not used. It is an error to specify <code>none</code> for both direction. </p>
<p> Note that commas must never follow colons or other commas. Also, whitespace is not allowed inside a QOS specification. QOS specifications are case-insensitive.</p>
<h2>Examples</h2>
<p>Each of the following lines contains a valid QOS specification: </p>
<pre> ubr
 ubr:pcr=100kbps
 cbr,aal0:pcr=64kbps
 CBR:max_pcr=11Mbps,min_pcr=10mbps,sdu=8192
 aal5,ubr:tx:none
 cbr:tx:pcr=30000,rx:none</pre>
<p>The following specificiations are equivalent: </p>
<pre> CBR,AAL5:PCR=48Mbps
 cbr,aal5:max_pcr=125000
 cbr,aal5:tx:pcr=125kcps,rx:pcr=125kcps</pre>
<h2>Author</h2>
<p>Werner Almesberger, EPFL LRC/ICA &lt;werner.almesberger [at] epfl.ch&gt;</p>
