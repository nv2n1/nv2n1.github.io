---
title: "qwtsamplingthread(3)"
name: "qwtsamplingthread"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtsamplingthread/"
description: "QwtSamplingThread –"
---

<p>QwtSamplingThread &#8211; </p>
<p> A thread collecting samples at regular intervals.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_sampling_thread.h&gt; </p>
<p> Inherits QThread.</p>
<h3>Public Slots</h3>
<p>void <code>setInterval</code> (double <code>interval</code>) </p>
<p> void <code>stop</code> () </p>
<h3>Public Member Functions</h3>
<p>virtual <code>~QwtSamplingThread</code> ()<br />
 <i>Destructor. </i><br />
 double <code>interval</code> () const </p>
<p> double <code>elapsed</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>QwtSamplingThread</code> (QObject *parent=NULL)<br />
 <i>Constructor. </i><br />
 virtual void <code>run</code> () </p>
<p> virtual void <code>sample</code> (double <code>elapsed</code>)=0 </p>
<h2>Detailed Description</h2>
<p>A thread collecting samples at regular intervals. </p>
<p> Continuous signals are converted into a discrete signal by collecting samples at regular intervals. A discrete signal can be displayed by a <code>QwtPlotSeriesItem</code> on a <code>QwtPlot</code> widget. </p>
<p> <code>QwtSamplingThread</code> starts a thread calling periodically <code>sample()</code>, to collect and store ( or emit ) a single sample. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotCurve</code>, <code>QwtPlotSeriesItem</code></dl>
<h2>Member Function Documentation</h2>
<h3>double QwtSamplingThread::elapsed () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Time (in ms) since the thread was started</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QThread::start(), <code>run()</code></dl>
<h3>double QwtSamplingThread::interval () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Interval (in ms), between 2 calls of <code>sample()</code></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setInterval()</code></dl>
<h3>void QwtSamplingThread::run () [protected], [virtual]</h3>
<p>Loop collecting samples started from QThread::start() </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>stop()</code></dl>
<h3>virtual void QwtSamplingThread::sample (doubleelapsed) [protected], [pure virtual]</h3>
<p>Collect a sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>elapsed</i> Time since the thread was started in milliseconds</dl>
<h3>void QwtSamplingThread::setInterval (doubleinterval) [slot]</h3>
<p>Change the interval (in ms), when <code>sample()</code> is called. The default interval is 1000.0 ( = 1s ) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>interval()</code></dl>
<h3>void QwtSamplingThread::stop () [slot]</h3>
<p>Terminate the collecting thread </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QThread::start(), <code>run()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
