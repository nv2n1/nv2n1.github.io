---
title: "ambiguous_words(1)"
name: "ambiguous_words"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ambiguous_words/"
description: "ambiguous_words – generate sets of words Tesseract is likely to find ambiguous"
---

<h2 class="name">NAME</h2>
<p> ambiguous_words &#8211; generate sets of words Tesseract is likely to find ambiguous </p>
<h2>SYNOPSIS</h2>
<p> <code>ambiguous_words</code> [-l lang] <i>TESSDATADIR</i> <i>WORDLIST</i> <i>AMBIGUOUSFILE</i></p>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/1-ambiguous_words/">ambiguous_words</a>(1) runs Tesseract in a special mode, and for each word in word list, produces a set of words which Tesseract thinks might be ambiguous with it. <i>TESSDATADIR</i> must be set to the absolute path of a directory containing <i>tessdata/lang.traineddata</i>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tesseract/">tesseract</a>(1)</p>
<h2>COPYING</h2>
<p> Copyright (C) 2012 Google, Inc. Licensed under the Apache License, Version 2.0</p>
<h2>AUTHOR</h2>
<p> The Tesseract OCR engine was written by Ray Smith and his research groups at Hewlett Packard (1985-1995) and Google (2006-present). </p>
<h2>Index</h2>
