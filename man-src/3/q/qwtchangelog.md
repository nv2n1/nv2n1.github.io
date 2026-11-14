---
title: "qwtchangelog(3)"
name: "qwtchangelog"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtchangelog/"
description: "qwtchangelog – What’s new in Qwt 6.1"
---

<p>qwtchangelog &#8211; What&#8217;s new in Qwt 6.1</p>
<h2>New plot items</h2>
<dl>
<dt>&bull;</p>
<dd><code>QwtPlotBarChart</code> </p>
<p>&nbsp;<wbr>Bar chart, see&nbsp;<wbr>&#8216;examples/distrowatch&#8217;</p>
<dt>&bull;</p>
<dd><code>QwtPlotMultiBarChart</code> </p>
<p>&nbsp;<wbr>Chart of grouped bars &#8211; stacked or aligned side by side. See&nbsp;<wbr>&#8216;examples/barchart&#8217;</p>
<dt>&bull;</p>
<dd><code>QwtPlotTradingCurve</code> </p>
<p>&nbsp;<wbr>Candlestick or OHLC charts typically used to describe price movements over time. See&nbsp;<wbr>&#8216;examples/stockchart&#8217;</p>
<dt>&bull;</p>
<dd><code>QwtPlotShapeItem</code> </p>
<p>&nbsp;<wbr>A plot item to display rectangles, circles, polygons and all other type of shapes&nbsp;<wbr>(&nbsp;<wbr>built from intersections or unifications&nbsp;<wbr>), that can be expressed by a QPainterPath. See&nbsp;<wbr>&#8216;examples/itemeditor&#8217;</p>
<dt>&bull;</p>
<dd><code>QwtPlotLegendItem</code> </p>
<p>&nbsp;<wbr>A legend on the plot canvas. See&nbsp;<wbr>&#8216;examples/legends&#8217;</p>
<dt>&bull;</p>
<dd><code>QwtPlotZoneItem</code> </p>
<p>&nbsp;<wbr>A horizontal or vertical section</p>
<dt>&bull;</p>
<dd><code>QwtPlotTextLabel</code> </p>
<p>&nbsp;<wbr>In opposite to a&nbsp;<wbr><code>QwtPlotMarker</code>&nbsp;<wbr>the text is not aligned to a plot coordinate but according to the geometry of the canvas&nbsp;<wbr>(&nbsp;<wbr>f.e top/centered for a title&nbsp;<wbr>). See&nbsp;<wbr>&#8216;playground/curvetracker&#8217;.</dl>
<h2>Scales beyond linear and logarithmic transformations</h2>
<p>QwtScaleTransformation has been replaced by <code>QwtTransform</code> and its derived classes: </p>
<dl>
<dt>&bull;</p>
<dd><code>QwtTransform</code></p>
<dt>&bull;</p>
<dd><code>QwtNullTransform</code></p>
<dt>&bull;</p>
<dd><code>QwtLogTransform</code></p>
<dt>&bull;</p>
<dd><code>QwtPowerTransform</code></dl>
<p> Individual transformations ( f.e. different scaling for special sections ) can be implemented by overloading <code>QwtTransform</code> ( see playground/scaleengine ). </p>
<p> <code>QwtLinearScaleEngine</code> and <code>QwtLogScaleEngine</code> are not limited to base 10 anymore.</p>
<h3>Datetime scales</h3>
<p>A set of a new classes for displaying datetime values: </p>
<dl>
<dt>&bull;</p>
<dd><code>QwtDate</code> </p>
<p>&nbsp;<wbr>A collection of methods to convert between QDateTime and doubles</p>
<dt>&bull;</p>
<dd><code>QwtDateScaleEngine</code> </p>
<p>&nbsp;<wbr>A scale engine that aligns and finds ticks in terms of datetime units.</p>
<dt>&bull;</p>
<dd><code>QwtDateScaleDraw</code> </p>
<p>&nbsp;<wbr>A scale draw mapping values to datetime strings.</dl>
<p> Scales for Qt::UTC and Qt::LocalTime are supported.</p>
<h2>Redesign of the dial and meter widgets</h2>
<p>Many parts of the class design of the dial and meter widgets were left over from the 90s ( Qwt 0.2, Qt 1.1 ). </p>
<p> The derivation tree is simpler and more logical: </p>
<dl>
<dt>&bull;</p>
<dd><code>QwtAbstractScale</code> is a QWidget</p>
<dt>&bull;</p>
<dd><code>QwtAbstractSlider</code> is a <code>QwtAbstractScale</code>. ( for sliders without scales QAbstractSlider should be the base class )</p>
<dt>&bull;</p>
<dd><code>QwtThermo</code> is also a <code>QwtAbstractScale</code></p>
<dt>&bull;</p>
<dd><code>QwtDial</code>, <code>QwtKnob</code>, <code>QwtSlider</code> are derived from <code>QwtAbstractSlider</code></p>
<dt>&bull;</p>
<dd><code>QwtCounter</code> is derived from QWidget</dl>
<p> QwtDoubleRange has been removed. </p>
<p> All classes use the terminology known from QAbstractSlider &#8211; as far as possible. The extended <code>system for scales</code> is completely supported.</p>
<h2>Basic support for an OpenGL plot canvas</h2>
<p><code>QwtPlotGLCanvas</code> offers the option to draw plot items using an OpenGL paint engine ( QPaintEngine::OpenGL/OpenGL2 ), This is not what could be implemented with native OpenGL, but it offers hardware acceleration in environments, where the raster paint engine is the only option. ( f.e Qt4/Windows, or Qt5 on all platforms ). </p>
<p> <code>QwtPlotGLCanvas</code> is in an experimental state and is not recommended for average use cases.</p>
<h2>A new system for plot legends</h2>
<p><code>QwtLegend</code> has been decoupled from <code>QwtPlot</code> and can be replaced by application specific implementations. Plot items and the legend exchange the information using <code>QwtLegendData</code>. </p>
<p> <code>QwtPlotLegendItem</code> is a new plot item that displays a legend on the plot canvas. </p>
<p> The following examples demonstrate how to use the new system: </p>
<dl>
<dt>&bull;</p>
<dd>examples/legends </p>
<p>&nbsp;<wbr>shows how to use the new legend system</p>
<dt>&bull;</p>
<dd>examples/stockchart </p>
<p>&nbsp;<wbr>implementats a QTreeView with checkable items as legend</dl>
<h2>Off-screen paint device for vector graphics</h2>
<p><code>QwtGraphic</code> can be copied like QImage or QPixmap but is scalable like QSvgGenerator. It is implemented as a record/replay paint device like QPicture.</p>
<h2>QwtWidgetOverlay</h2>
<p><code>QwtWidgetOverlay</code> is a base class for implementing widget overlays &#8211; primarily used for use cases like graphical editors or running cursors for the plot canvas. </p>
<p> The following examples show how to use overlays: </p>
<dl>
<dt>&bull;</p>
<dd>examples/itemeditor</p>
<dt>&bull;</p>
<dd>examples/curvetracker</dl>
<p> <code>QwtPicker</code> ( -&gt; <code>QwtPlotPicker</code>, <code>QwtPlotZoomer</code> ) internally uses <code>QwtWidgetOverlay</code> now, making it easier to implement individual rubber bands.</p>
<h2>QwtSymbol</h2>
<p>New symbol types have been introduced: </p>
<dl>
<dt>&bull;</p>
<dd><code>QwtSymbol::Path</code></p>
<dt>&bull;</p>
<dd><code>QwtSymbol::Pixmap</code></p>
<dt>&bull;</p>
<dd><code>QwtSymbol::Graphic</code></p>
<dt>&bull;</p>
<dd><code>QwtSymbol::SvgDocument</code></dl>
<p> <code>QwtSymbol</code> autodetect the most performant paint strategy for a paint device what is in most situations using a QPixmap cache. </p>
<p> <code>QwtSymbol::setPinPoint()</code> allows to align the symbol individually, f.e to the position of the peak of an arrow.</p>
<h2>QwtPlotCurve</h2>
<p>Some optimizations that got lost with introducing the floating point based render code with Qwt 6.0 have been reenabled. Other specific optimizations have been added. </p>
<p> New paint attributes: </p>
<dl>
<dt>&bull;</p>
<dd><code>QwtPlotCurve::FilterPoints</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotCurve::MinimizeMemory</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotCurve::ImageBuffer</code></dl>
<p> QwtPlotCurve::CacheSymbols has been removed, as caching is implemented in <code>QwtSymbol</code> now. </p>
<p> <code>QwtPlotCurve::drawLines()</code>, <code>QwtPlotCurve::drawDots()</code>, <code>QwtPlotCurve::drawSteps()</code> and <code>QwtPlotCurve::drawSticks()</code> are virtual now.</p>
<h2>QwtPlot</h2>
<p>A footer similar to a title has been added. </p>
<p> QwtPlot::ExternalLegend is obsolete with the new <code>system for legends</code>. The signals QwtPlot::legendClicked(), QwtPlot::legendChecked() have been removed. Applications need to connect to <code>QwtLegend::clicked()</code> and <code>QwtLegend::checked()</code>. </p>
<p> To support using an OpenGL canvas <code>QwtPlot::setCanvas</code> has been added. This has 2 important implications for the application code: </p>
<dl>
<dt>&bull;</p>
<dd><code>QwtPlot::canvas()</code> returns QWidget and needs to be casted, when using methods of <code>QwtPlotCanvas</code>.</p>
<dt>&bull;</p>
<dd><code>QwtPlotCanvas</code> can be created and assigned in application code, what makes it possible to derive and overload methods.</dl>
<p> The initialization of a plot canvas with Qwt 6.1 will probably look like this: </p>
<pre>QwtPlotCanvas* canvas = new QwtPlotCanvas();
canvas-&gt;setXY( ... );
...
plot-&gt;setCanvas( canvas );</pre>
<p>To have a consistent API <code>QwtPlot::setPlotLayout()</code> has been added,</p>
<h2>Other</h2>
<h3>QwtScaleDiv</h3>
<p>The following methods have been added: </p>
<dl>
<dt>&bull;</p>
<dd><code>QwtScaleDiv::inverted()</code></p>
<dt>&bull;</p>
<dd><code>QwtScaleDiv::bounded()</code></p>
<dt>&bull;</p>
<dd><code>QwtScaleDiv::isEmpty()</code></p>
<dt>&bull;</p>
<dd><code>QwtScaleDiv::isIncreasing()</code></p>
<dt>&bull;</p>
<dd>QDebug operator</dl>
<p> The following methods have been removed: </p>
<dl>
<dt>&bull;</p>
<dd>QwtScaleDiv::isValid(), QwtScaleDiv::invalidate() </p>
<p>&nbsp;<wbr>The valid state was left over from early Qwt versions indicating a state of the autoscaler.</dl>
<h3>QwtScaleEngine</h3>
<p>The following methods have been added: </p>
<dl>
<dt>&bull;</p>
<dd><code>QwtScaleEngine::setBase()</code></p>
<dt>&bull;</p>
<dd><code>QwtScaleEngine::setTransformation()</code></dl>
<h3>QwtPlotLayout</h3>
<p>The following flags have been added: </p>
<dl>
<dt>&bull;</p>
<dd><code>QwtPlotLayout::IgnoreTitle</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotLayout::IgnoreFooter</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotLayout::setAlignCanvasToScale()</code></dl>
<h3>QwtPlotCanvas</h3>
<p>Rounded borders ( like with style sheets ) can configured using <code>QwtPlotCanvas::setBorderRadius()</code>;</p>
<h3>Other changes</h3>
<dl>
<dt>&bull;</p>
<dd><code>QwtWeedingCurveFitter</code> </p>
<p>&nbsp;<wbr><code>QwtWeedingCurveFitter::setChunkSize()</code>&nbsp;<wbr>has been added, with drastic performance improvements for huge sets of points.</p>
<dt>&bull;</p>
<dd><code>QwtPlotRenderer</code> The frame of the plot canvas can be rendered, what makes the result even closer to WYSWYG. <code>QwtPlotRenderer::exportTo()</code> has been added.</p>
<dt>&bull;</p>
<dd><code>QwtSystemClock</code> For Qt &gt;= 4.9 <code>QwtSystemClock</code> uses QElapsedTimer internally. As it doesn&#8217;t support a similar feature, QwtSystemClock::precision() has been removed.</p>
<dt>&bull;</p>
<dd>QwtPlotAbstractSeriesItem </p>
<p>&nbsp;<wbr>QwtPlotAbstractSeriesItem has been split into&nbsp;<wbr><code>QwtPlotSeriesItem</code>&nbsp;<wbr>and QwtPlotAbstractSeriesStore.</p>
<dt>&bull;</p>
<dd><code>QwtText</code> </p>
<p>&nbsp;<wbr>A metatype declaration has been added, so that&nbsp;<wbr><code>QwtText</code>&nbsp;<wbr>can be used with QVariant.</p>
<dt>&bull;</p>
<dd><code>QwtEventPattern</code>, <code>QwtPanner</code>, <code>QwtMagnifier</code> </p>
<p>&nbsp;<wbr>Forgotten Qt3 leftovers have been fixed: int -&gt;&nbsp;<wbr>Qt::KeyboardModifiers</p>
<dt>&bull;</p>
<dd>QPen Qt5/Qt4 incompatibility The default pen width for Qt5 is 1, what makes it a non cosmetic. To hide this nasty incompatibility several setPen() methods have been added the build pens with a width 0. See QPen::isCosmetic(),</p>
<dt>&bull;</p>
<dd>qwtUpperSampleIndex() </p>
<p>&nbsp;<wbr>A binary search algorithm for sorted samples</p>
<dt>&bull;</p>
<dd><code>QwtMatrixRasterData</code> <code>QwtMatrixRasterData::setValue()</code> has been added</p>
<dt>&bull;</p>
<dd><code>QwtPicker</code> QwtPicker::rubberBandWidget(), QwtPicker::trackerWidget() have been replaced by <code>QwtPicker::rubberBandOverlay()</code>, <code>QwtPicker::trackerOverlay()</code>. <code>QwtPicker::rubberBandMask()</code> has been added. QwtPicker::pickRect() has been replaced by <code>QwtPicker::pickArea()</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotItem</code> <code>QwtPlotItem::ItemInterest</code> has been added. <code>QwtPlotItem::setRenderThreadCount()</code> was shifted from <code>QwtPlotRasterItem</code>.</p>
<dt>&bull;</p>
<dd>&#8230;</dl>
<h2>Summary of the new classes</h2>
<dl>
<dt>&bull;</p>
<dd><code>QwtAbstractLegend</code></p>
<dt>&bull;</p>
<dd><code>QwtDate</code></p>
<dt>&bull;</p>
<dd><code>QwtDateScaleDraw</code></p>
<dt>&bull;</p>
<dd><code>QwtDateScaleEngine</code></p>
<dt>&bull;</p>
<dd><code>QwtGraphic</code></p>
<dt>&bull;</p>
<dd><code>QwtLegendData</code></p>
<dt>&bull;</p>
<dd><code>QwtLegendLabel</code></p>
<dt>&bull;</p>
<dd><code>QwtPainterCommand</code></p>
<dt>&bull;</p>
<dd><code>QwtPixelMatrix</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotAbstractBarChart</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotBarChart</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotMultiBarChart</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotGLCanvas</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotLegendItem</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotShapeItem</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotTextLabel</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotTradingCurve</code></p>
<dt>&bull;</p>
<dd><code>QwtPlotZoneItem</code></p>
<dt>&bull;</p>
<dd>QwtPointData</p>
<dt>&bull;</p>
<dd><code>QwtPointMapper</code></p>
<dt>&bull;</p>
<dd><code>QwtTransform</code>, <code>QwtNullTransform</code>, <code>QwtLogTransform</code>, <code>QwtPowerTransform</code></p>
<dt>&bull;</p>
<dd><code>QwtWidgetOverlay</code></dl>
