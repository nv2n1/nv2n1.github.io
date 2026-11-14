---
title: "strtonum(3)"
name: "strtonum"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strtonum/"
description: "strtonum – reliably convert string value to an integer"
---

<p><code>strtonum</code> &#8211; reliably convert string value to an integer</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In limits.h In bsd/stdlib.h Ft long long Fo strtonum Fa const char *nptr Fa long long minval Fa long long maxval Fa const char **errstr Fc</p>
<h2>Description</h2>
<p>The Fn strtonum function converts the string in Fa nptr to a Vt long long value. The Fn strtonum function was designed to facilitate safe, robust programming and overcome the shortcomings of the <a href="/docs/linux/man/3-atoi/">atoi</a>(3) and <a href="/docs/linux/man/3-strtol/">strtol</a>(3) family of interfaces. </p>
<p> The string may begin with an arbitrary amount of whitespace (as determined by <a href="/docs/linux/man/3-isspace/">isspace</a>(3)) followed by a single optional `+&#8217; or `-&#8216; sign. </p>
<p> The remainder of the string is converted to a Vt long long value according to base 10. </p>
<p> The value obtained is then checked against the provided Fa minval and Fa maxval bounds. If Fa errstr is non-null, Fn strtonum stores an error string in Fa *errstr indicating the failure.</p>
<h2>Return Values</h2>
<p>The Fn strtonum function returns the result of the conversion, unless the value would exceed the provided bounds or is invalid. On error, 0 is returned, <i>errno</i> is set, and Fa errstr will point to an error message. On success, Fa *errstr will be set to <code>NULL</code> this fact can be used to differentiate a successful return of 0 from an error.</p>
<h2>Examples</h2>
<p>Using Fn strtonum correctly is meant to be simpler than the alternative functions. </p>
<blockquote>
<pre>int iterations;
const char *errstr;
iterations = strtonum(optarg, 1, 64, &amp;errstr);
if (errstr)
 errx(1, &quot;number of iterations is %s: %s&quot;, errstr, optarg);</pre>
</blockquote>
<p> The above example will guarantee that the value of iterations is between 1 and 64 (inclusive).</p>
<h2>Errors</h2>
<dt><code>Bq </code>Er ERANGE</p>
<dd>The given string was out of range.</p>
<dt><code>Bq </code>Er EINVAL</p>
<dd>The given string did not consist solely of digit characters.</p>
<dt><code>Bq </code>Er EINVAL</p>
<dd>The supplied Fa minval was larger than Fa maxval .</dl>
<p> If an error occurs, Fa errstr will be set to one of the following strings: </p>
<dt><code>too large</code></p>
<dd>The result was larger than the provided maximum value.</p>
<dt><code>too small</code></p>
<dd>The result was smaller than the provided minimum value.</p>
<dt><code>invalid</code></p>
<dd>The string did not consist solely of digit characters.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-atof/">atof</a>(3), <a href="/docs/linux/man/3-atoi/">atoi</a>(3), <a href="/docs/linux/man/3-atol/">atol</a>(3), <a href="/docs/linux/man/3-atoll/">atoll</a>(3), <a href="/docs/linux/man/3-sscanf/">sscanf</a>(3), <a href="/docs/linux/man/3-strtod/">strtod</a>(3), <a href="/docs/linux/man/3-strtol/">strtol</a>(3), <a href="/docs/linux/man/3-strtoul/">strtoul</a>(3)</p>
<h2>Standards</h2>
<p>The Fn strtonum function is a BSD extension. The existing alternatives, such as <a href="/docs/linux/man/3-atoi/">atoi</a>(3) and <a href="/docs/linux/man/3-strtol/">strtol</a>(3), are either impossible or difficult to use safely.</p>
<h2>History</h2>
<p>The Fn strtonum function first appeared in Ox 3.6 .</p>
