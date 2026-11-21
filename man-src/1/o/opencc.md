---
title: "opencc(1)"
name: "opencc"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opencc/"
description: "opencc – simplified-traditional chinese conversion tool"
---

<h2>NAME</h2>
<p> opencc &#8211; simplified-traditional chinese conversion tool</p>
<h2>DESCRIPTION</h2>
<p> Open Chinese Convert (OpenCC) Command Line Tool</p>
<h3>Usage:</h3>
<dl>
<dt>
</dt><dd>opencc [-i input_file] [-o output_file] [-c config_file]</dd>
<dt> <code>-i</code></dt>
<dd>Read original text from input_file.</dd>
<dt> <code>-o</code></dt>
<dd>Write converted text to output_file.</dd>
<dt> <code>-c</code></dt>
<dd>Load dictionary configuration from config_file.</dd>
<dt>
</dt><dd> Note:</dd>
<dt>
</dt><dd> Text from standard input will be read if input_file is not set and will be written to standard output if output_file is not set.</dd>
<dt>
</dt><dd> Default configuration(zhs2zht.ini) will be load if config_file is not set.</dd></dl>
<p> Open Chinese Convert (OpenCC) Command Line Tool</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) </p>
