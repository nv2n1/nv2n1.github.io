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
<dt>If more than one input file specified those will be concatenated and minified together.</dt>
<dd>
</dd><dt>When you specify a config file with the <code>&#8211;config-file</code> option (see /usr/share/doc/nodejs-html-minifier/sample-cli-config-file.conf for format) you can still override some of its contents by providing individual command line options, too.</dt>
<dd>
</dd><dt>When you want to provide an array of strings for <code>&#8211;ignore-custom-comments</code> or <code>&#8211;process-scripts</code> options on the command line you must escape those such as <code>&#8211;ignore-custom-comments</code> &quot;[\&quot;string1\&quot;,\&quot;string1\&quot;]&quot;</dt>
<dd></dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Version information</dd>
<dt><code>-o</code>, <code>&#8211;output</code> FILE</dt>
<dd> Specify output file (if not specified STDOUT will be used for output)</dd>
<dt><code>-c</code>, <code>&#8211;config-file</code> FILE</dt>
<dd> Use config file</dd>
<dt><code>&#8211;remove-comments</code></dt>
<dd> Strip HTML comments</dd>
<dt><code>&#8211;remove-comments-from-cdata</code></dt>
<dd> Strip HTML comments from scripts and styles</dd>
<dt> <code>&#8211;remove-cdatasections-from-cdata</code> Remove CDATA sections from script and style elements</dt>
<dt><code>&#8211;collapse-whitespace</code></dt>
<dd>
</dd><dd>Collapse white space that contributes to text nodes in a document tree.</dd>
<dt><code>&#8211;conservative-collapse</code></dt>
<dd> Always collapse to 1 space (never remove it entirely)</dd>
<dt><code>&#8211;preserve-line-breaks</code></dt>
<dd> Always collapse to 1 line break (never remove it entirely) when whitespace between tags include a line break.</dd>
<dt><code>&#8211;collapse-boolean-attributes</code></dt>
<dd> Omit attribute values from boolean attributes</dd>
<dt><code>&#8211;remove-attribute-quotes</code></dt>
<dd> Remove quotes around attributes when possible.</dd>
<dt><code>&#8211;remove-redundant-attributes</code></dt>
<dd> Remove attributes when value matches default.</dd>
<dt><code>&#8211;use-short-doctype</code></dt>
<dd> Replaces the doctype with the short (HTML5) doctype</dd>
<dt><code>&#8211;remove-empty-attributes</code></dt>
<dd> Remove all attributes with whitespace-only values</dd>
<dt><code>&#8211;remove-optional-tags</code></dt>
<dd> Remove unrequired tags</dd>
<dt><code>&#8211;remove-empty-elements</code></dt>
<dd> Remove all elements with empty contents</dd>
<dt><code>&#8211;lint</code></dt>
<dd> Toggle linting</dd>
<dt><code>&#8211;keep-closing-slash</code></dt>
<dd> Keep the trailing slash on singleton elements</dd>
<dt><code>&#8211;case-sensitive</code></dt>
<dd> Treat attributes in case sensitive manner (useful for SVG; e.g. viewBox)</dd>
<dt><code>&#8211;minify-js</code></dt>
<dd> Minify Javascript in script elements and on* attributes (uses UglifyJS)</dd>
<dt><code>&#8211;minify-css</code></dt>
<dd> Minify CSS in style elements and style attributes (uses clean-css)</dd>
<dt><code>&#8211;minify-urls</code></dt>
<dd> Minify URLs in various attributes (uses relateurl)</dd>
<dt><code>&#8211;ignore-custom-comments</code> STRING</dt>
<dd> Array of regex&#8217;es that allow to ignore certain comments, when matched</dd>
<dt><code>&#8211;process-scripts</code> STRING</dt>
<dd> Array of strings corresponding to types of script elements to process through minifier (e.g. &quot;text/ng-template&quot;, &quot;text/x-handlebars-template&quot;, etc.)</dd>
<dt><code>&#8211;max-line-length</code> NUMBER</dt>
<dd> Max line length</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display help and usage details </dd>
</dl>
<h2>Index</h2>
