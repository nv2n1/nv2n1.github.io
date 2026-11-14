---
title: "log4cppsimpleconfigurator(3)"
name: "log4cppsimpleconfigurator"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppsimpleconfigurator/"
description: "log4cpp::SimpleConfigurator –"
---

<p>log4cpp::SimpleConfigurator &#8211; </p>
<p> This class implements a simple Configurator for <code>log4cpp</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;SimpleConfigurator.hh&gt;</p>
<h3>Static Public Member Functions</h3>
<p>static void <code>configure</code> (const std::string &amp;initFileName) throw (ConfigureFailure)<br />
 <i>Configure </i><code>log4cpp</code> with the configuration in the given file.<br />
 static void <code>configure</code> (std::istream &amp;initFile) throw (ConfigureFailure)<br />
 <i>Configure </i><code>log4cpp</code> with the configuration in the given file.</p>
<h2>Detailed Description</h2>
<p>This class implements a simple Configurator for <code>log4cpp</code>. </p>
<p> It is a temporary hack with an undocumented configuration format. </p>
<p> <code>Deprecated</code></p>
<dl COMPACT>
<dd>As of version 0.3.2 <code>log4cpp</code> includes a log4j format compatible <code>PropertyConfigurator</code>, removing the need for <code>SimpleConfigurator</code>. This class will be removed in 0.4.0.</dl>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::SimpleConfigurator::configure (const std::string &amp;initFileName)<code>ConfigureFailure</code> [static]</h3>
<p>Configure <code>log4cpp</code> with the configuration in the given file. NB. The configuration file format is undocumented and may change without notice. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.2.6</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>initFileName</i> name of the configuration file</dl>
<p> <code>Exceptions:</code></p>
<dl COMPACT>
<dd><i></i><code>ConfigureFailure</code> if the method encountered a read or syntax error.</dl>
<h3>void log4cpp::SimpleConfigurator::configure (std::istream &amp;initFile)<code>ConfigureFailure</code> [static]</h3>
<p>Configure <code>log4cpp</code> with the configuration in the given file. NB. The configuration file format is undocumented and may change without notice. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.3.1</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>initFile</i> an input stream to the configuration file</dl>
<p> <code>Exceptions:</code></p>
<dl COMPACT>
<dd><i></i><code>ConfigureFailure</code> if the method encountered a read or syntax error.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
