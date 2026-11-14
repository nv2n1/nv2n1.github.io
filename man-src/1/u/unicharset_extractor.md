---
title: "unicharset_extractor(1)"
name: "unicharset_extractor"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unicharset_extractor/"
description: "unicharset_extractor – extract unicharset from Tesseract boxfiles"
---

<h2 class="name">NAME</h2>
<p> unicharset_extractor &#8211; extract unicharset from Tesseract boxfiles </p>
<h2>SYNOPSIS</h2>
<p> <code>unicharset_extractor</code> <i>[-D dir]</i> <i>FILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Tesseract needs to know the set of possible characters it can output. To generate the unicharset data file, use the unicharset_extractor program on the same training pages bounding box files as used for clustering: </p>
<dl>
<dt>
<dd>
<pre>
unicharset_extractor fontfile_1.box fontfile_2.box ...
</pre>
</dl>
<p> The unicharset will be put into the file <i>dir/unicharset</i>, or simply <i>./unicharset</i> if no output directory is provided. </p>
<p> Tesseract also needs to have access to character properties isalpha, isdigit, isupper, islower, ispunctuation. all of this auxilury data and more is encoded in this file. (See <a href="/docs/linux/man/5-unicharset/">unicharset</a>(5)) </p>
<p> If your system supports the wctype functions, these values will be set automatically by unicharset_extractor and there is no need to edit the unicharset file. On some older systems (eg Windows 95), the unicharset file must be edited by hand to add these property description codes. </p>
<p> <code>NOTE</code> The unicharset file must be regenerated whenever inttemp, normproto and pffmtable are generated (i.e. they must all be recreated when the box file is changed) as they have to be in sync. This is made easier than in previous versions by running unicharset_extractor before mftraining and cntraining, and giving the unicharset to mftraining.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tesseract/">tesseract</a>(1), <a href="/docs/linux/man/5-unicharset/">unicharset</a>(5) </p>
<p> m[blue]<code><a rel="nofollow" href="https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract">https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract</a></code>m[]</p>
<h2>HISTORY</h2>
<p> unicharset_extractor first appeared in Tesseract 2.00.</p>
<h2>COPYING</h2>
<p> Copyright (C) 2006, Google Inc. Licensed under the Apache License, Version 2.0</p>
<h2>AUTHOR</h2>
<p> The Tesseract OCR engine was written by Ray Smith and his research groups at Hewlett Packard (1985-1995) and Google (2006-present). </p>
<h2>Index</h2>
