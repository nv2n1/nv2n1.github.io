---
title: "gpt_extract_data(8)"
name: "gpt_extract_data"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt_extract_data/"
description: "gpt_extract_data – Print out package metadata as shell variables"
---

<p><code>gpt_extract_data</code> &#8211; Print out package metadata as shell variables</p>
<h2>Synopsis</h2>
<p>gpt_extract_data [&#8211;name &#8211;version &#8211;build_env ] pkg_data_file</p>
<h2>Description</h2>
<p><code>gpt_extract_data</code> Print out package metadata as shell variables.</p>
<h2>Options</h2>
<dl>
<dt>name</dt>
<dd>Print out GPT_NAME= the name of the package.</dd>
<dt>version</dt>
<dd>Print out version numbers as GPT_MAJOR_VERSION, GPT_MINOR_VERSION and GPT_AGE_VERSION variables.</dd>
<dt>build_env</dt>
<dd>Print out build environment as GPT_CFLAGS, GPT_INCLUDES, and GPT_LIBS.</dd></dl>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
