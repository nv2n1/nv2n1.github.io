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
<dt>name</p>
<dd>Print out GPT_NAME= the name of the package.</p>
<dt>version</p>
<dd>Print out version numbers as <font SIZE="-1">GPT_MAJOR_VERSION</font>, <font SIZE="-1">GPT_MINOR_VERSION</font> and <font SIZE="-1">GPT_AGE_VERSION</font> variables.</p>
<dt>build_env</p>
<dd>Print out build environment as <font SIZE="-1">GPT_CFLAGS</font>, <font SIZE="-1">GPT_INCLUDES</font>, and <font SIZE="-1">GPT_LIBS</font>.</dl>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
