---
title: "qmcdesc(3)"
name: "qmcdesc"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qmcdesc/"
description: "QmcDesc – container for a metric description"
---

<p><code>QmcDesc</code> &#8211; container for a metric description</p>
<h2>C++ Synopsis</h2>
<p><code> #include &lt;QmcDesc.h&gt; </p>
<p> CC &#8230; -lqmc -lpcp </code></p>
<h2>Description</h2>
<p>A <code>QmcDesc</code> object is a container for a metric descriptor (<code>pmDesc</code>, see <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3)) and units.</p>
<h2>CONSTRUCTORS &amp; DESTRUCTOR</h2>
<dl COMPACT>
<dt><code>~QmcDesc();</code></p>
<dd>Destructor.</p>
<dt><code>QmcDesc(pmID pmid);</code></p>
<dd>Construct a container for the descriptor for <i>pmid</i>. The descriptor is obtained from the current <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) context using <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3).</dl>
<h2>Description</h2>
<dl COMPACT>
<dt><code>int status() const;</code></p>
<dd>A status less than zero indicates that the descriptor could not be obtained, the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) error is encoded in the result.</p>
<dt><code>pmID id() const;</code></p>
<dd>Return the <code>pmID</code> for this descriptor.</p>
<dt><code>pmDesc desc() const;</code></p>
<dd>Return a copy of the actual metric descriptor.</p>
<dt><code>const pmDesc *descPtr() const;</code></p>
<dd>Return a pointer to the actual descriptor to avoid using a pointer to a temporary.</dl>
<h2>Units</h2>
<dl COMPACT>
<dt><code>const QString &amp;units() const;</code></p>
<dd>The complete unit string for this descriptor.</p>
<dt><code>const QString &amp;abvUnits() const;</code></p>
<dd>The unit string using abbreviations.</p>
<dt><code>bool useScaleUnits() const;</code></p>
<dd>Returns <code>true</code> if the units have been set by a call to <code>QmcDesc::setScaleUnits</code>.</p>
<dt><code>const pmUnits &amp;scaleUnits() const;</code></p>
<dd>Return the scaling units for this descriptor.</p>
<dt><code>void setScaleUnits(const pmUnits &amp;units);</code></p>
<dd>Set the scaling units for this descriptor.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-qmc/">QMC</a></code>(3), <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) and <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>Error messages are generated using <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3) but are not flushed. It is the responsibility of the user to call <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) to output any messages. </p>
<p> Additional diagnostics may be activated by adding <code>DBG_TRACE_PMC</code> to the global <i>pmDebug</i>.</p>
