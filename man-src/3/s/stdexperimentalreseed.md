---
title: "stdexperimentalreseed(3)"
name: "stdexperimentalreseed"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalreseed/"
description: "std::experimental::reseed – std::experimental::reseed"
---

<p>std::experimental::reseed &#8211; std::experimental::reseed</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/random&gt;<br />
void reseed(); <code>(1)</code> (library fundamentals TS v2)<br />
void reseed(std::default_random_engine::result_type value); <code>(2)</code> (library fundamentals TS v2)<br />
Reseeds the per-thread_random_number_engine and any std::uniform_int_distribution instances used by randint.<br />
1) Sets the per-thread engine to an unpredictable state.<br />
2) Seeds the per-thread engine g as if by g.seed(value). </p>
<h2>Parameters</h2>
<p>value &#8211; value of the new seed </p>
<p>Remarks </p>
<p>Subsequent calls to randint do not depend on values produced by the per-thread engine prior to calling reseed.</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generates a random integer in the specified range<br />
randint <i>(function template)</i> </p>
