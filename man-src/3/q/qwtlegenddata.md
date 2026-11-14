---
title: "qwtlegenddata(3)"
name: "qwtlegenddata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtlegenddata/"
description: "QwtLegendData –"
---

<p>QwtLegendData &#8211; </p>
<p> Attributes of an entry on a legend.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_legend_data.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>Mode</code> { <code>ReadOnly</code>, <code>Clickable</code>, <code>Checkable</code> }<br />
 <i>Mode defining how a legend entry interacts. </i><br />
 enum <code>Role</code> { <code>ModeRole</code>, <code>TitleRole</code>, <code>IconRole</code>, <code>UserRole</code> = 32 }<br />
 <i>Identifier how to interprete a QVariant. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtLegendData</code> ()<br />
 <i>Constructor. </i><br />
 <code>~QwtLegendData</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setValues</code> (const QMap&lt; int, QVariant &gt; &amp;) </p>
<p> const QMap&lt; int, QVariant &gt; &amp; <code>values</code> () const </p>
<p> void <code>setValue</code> (int role, const QVariant &amp;) </p>
<p> QVariant <code>value</code> (int role) const </p>
<p> bool <code>hasRole</code> (int role) const </p>
<p> bool <code>isValid</code> () const </p>
<p> <code>QwtGraphic</code> <code>icon</code> () const </p>
<p> <code>QwtText</code> <code>title</code> () const </p>
<p> <code>Mode</code> <code>mode</code> () const </p>
<h2>Detailed Description</h2>
<p>Attributes of an entry on a legend. </p>
<p> <code>QwtLegendData</code> is an abstract container ( like QAbstractModel ) to exchange attributes, that are only known between to the plot item and the legend. </p>
<p> By overloading <code>QwtPlotItem::legendData()</code> any other set of attributes could be used, that can be handled by a modified ( or completely different ) implementation of a legend. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtLegend</code>, <code>QwtPlotLegendItem</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The stockchart example implements a legend as a tree with checkable items</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtLegendData::Mode</code></h3>
<p>Mode defining how a legend entry interacts. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>ReadOnly </i></p>
<dd>The legend item is not interactive, like a label.</p>
<dt><i>Clickable </i></p>
<dd>The legend item is clickable, like a push button.</p>
<dt><i>Checkable </i></p>
<dd>The legend item is checkable, like a checkable button.</dl>
<h2>Member Function Documentation</h2>
<h3>bool QwtLegendData::hasRole (introle) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>role</i> Attribute role</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the internal map has an entry for role</dl>
<h3><code>QwtGraphic</code> QwtLegendData::icon () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Value of the IconRole attribute</dl>
<h3>bool QwtLegendData::isValid () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the internal map is empty</dl>
<h3><code>QwtLegendData::Mode</code> QwtLegendData::mode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Value of the ModeRole attribute</dl>
<h3>void QwtLegendData::setValue (introle, const QVariant &amp;data)</h3>
<p>Set an attribute value </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>role</i> Attribute role<br />
 <i>data</i> Attribute value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>value()</code></dl>
<h3>void QwtLegendData::setValues (const QMap&lt; int, QVariant &gt; &amp;map)</h3>
<p>Set the legend attributes </p>
<p> <code>QwtLegendData</code> actually is a QMap&lt;int, QVariant&gt; with some convenience interfaces </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>map</i> Values</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>values()</code></dl>
<h3><code>QwtText</code> QwtLegendData::title () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Value of the TitleRole attribute</dl>
<h3>QVariant QwtLegendData::value (introle) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>role</i> Attribute role</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Attribute value for a specific role</dl>
<h3>const QMap&lt; int, QVariant &gt; &amp; QwtLegendData::values () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Legend attributes</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setValues()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
