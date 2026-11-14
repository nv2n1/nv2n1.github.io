---
title: "html-minifier(1)"
name: "html-minifier"
section: "1"
letter: "h"
url: "/docs/linux/man/1-html-minifier/"
description: "html-minifier – HTML minifier with lint-like capabilities"
---

<h2>NAME</h2>
<p> html-minifier &#8211; HTML minifier with lint-like capabilities</p>
<h2>SYNOPSIS</h2>
<p> html-minifier [OPTIONS] [FILE(s)]</p>
<h2>DESCRIPTION</h2>
<p> HTMLMinifier is a highly configurable, well-tested, Javascript-based HTML minifier, with lint-like capabilities.</p>
<h2>USAGE</h2>
<p> If no input file(s) specified then STDIN will be used for input.</p>
<dl>
<dt>If more than one input file specified those will be concatenated and minified together.</p>
<dd>
<dt>When you specify a config file with the <code>&#8211;config-file</code> option (see /usr/share/doc/nodejs-html-minifier/sample-cli-config-file.conf for format) you can still override some of its contents by providing individual command line options, too.</p>
<dd>
<dt>When you want to provide an array of strings for <code>&#8211;ignore-custom-comments</code> or <code>&#8211;process-scripts</code> options on the command line you must escape those such as <code>&#8211;ignore-custom-comments</code> &quot;[\&quot;string1\&quot;,\&quot;string1\&quot;]&quot;</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Version information</p>
<dt><code>-o</code>, <code>&#8211;output</code> FILE</p>
<dd> Specify output file (if not specified STDOUT will be used for output)</p>
<dt><code>-c</code>, <code>&#8211;config-file</code> FILE</p>
<dd> Use config file</p>
<dt><code>&#8211;remove-comments</code></p>
<dd> Strip HTML comments</p>
<dt><code>&#8211;remove-comments-from-cdata</code></p>
<dd> Strip HTML comments from scripts and styles</p>
<dt> <code>&#8211;remove-cdatasections-from-cdata</code> Remove CDATA sections from script and style elements</p>
<dt><code>&#8211;collapse-whitespace</code></p>
<dd>
<dd>Collapse white space that contributes to text nodes in a document tree.</p>
<dt><code>&#8211;conservative-collapse</code></p>
<dd> Always collapse to 1 space (never remove it entirely)</p>
<dt><code>&#8211;preserve-line-breaks</code></p>
<dd> Always collapse to 1 line break (never remove it entirely) when whitespace between tags include a line break.</p>
<dt><code>&#8211;collapse-boolean-attributes</code></p>
<dd> Omit attribute values from boolean attributes</p>
<dt><code>&#8211;remove-attribute-quotes</code></p>
<dd> Remove quotes around attributes when possible.</p>
<dt><code>&#8211;remove-redundant-attributes</code></p>
<dd> Remove attributes when value matches default.</p>
<dt><code>&#8211;use-short-doctype</code></p>
<dd> Replaces the doctype with the short (HTML5) doctype</p>
<dt><code>&#8211;remove-empty-attributes</code></p>
<dd> Remove all attributes with whitespace-only values</p>
<dt><code>&#8211;remove-optional-tags</code></p>
<dd> Remove unrequired tags</p>
<dt><code>&#8211;remove-empty-elements</code></p>
<dd> Remove all elements with empty contents</p>
<dt><code>&#8211;lint</code></p>
<dd> Toggle linting</p>
<dt><code>&#8211;keep-closing-slash</code></p>
<dd> Keep the trailing slash on singleton elements</p>
<dt><code>&#8211;case-sensitive</code></p>
<dd> Treat attributes in case sensitive manner (useful for SVG; e.g. viewBox)</p>
<dt><code>&#8211;minify-js</code></p>
<dd> Minify Javascript in script elements and on* attributes (uses UglifyJS)</p>
<dt><code>&#8211;minify-css</code></p>
<dd> Minify CSS in style elements and style attributes (uses clean-css)</p>
<dt><code>&#8211;minify-urls</code></p>
<dd> Minify URLs in various attributes (uses relateurl)</p>
<dt><code>&#8211;ignore-custom-comments</code> STRING</p>
<dd> Array of regex&#8217;es that allow to ignore certain comments, when matched</p>
<dt><code>&#8211;process-scripts</code> STRING</p>
<dd> Array of strings corresponding to types of script elements to process through minifier (e.g. &quot;text/ng-template&quot;, &quot;text/x-handlebars-template&quot;, etc.)</p>
<dt><code>&#8211;max-line-length</code> NUMBER</p>
<dd> Max line length</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help and usage details </p>
</dl>
<h2>Index</h2>
