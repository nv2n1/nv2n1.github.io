---
title: "cdk_params(3)"
name: "cdk_params"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_params/"
description: "cdk_params – Cdk command-line parsing"
---

<h2>NAME</h2>
<p> cdk_params &#8211; Cdk command-line parsing</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int CDKparamNumber(
    CDK_PARAMS *params,
    int option);
int CDKparamNumber2(
    CDK_PARAMS *params,
    int option,
    int missing);
char *CDKparamString(
    CDK_PARAMS *params,
    int option);
char *CDKparamString2(
    CDK_PARAMS *params,
    int option,
    const char *missing);
void CDKparseParams(
    int argc,
    char **argv,
    CDK_PARAMS *params,
    const char *options);
int CDKparsePosition(
    char *string);
int CDKparamValue(
    CDK_PARAMS *params,
    int option,
    int missing);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> These are a set of functions used to implement the command-line utilities and demonstration programs for Cdk. Rather than set the programs&#8217; options at initialization, they construct a simple database which holds the common parameters using <code>CDKparseParams()</code>.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>CDKparamNumber</code></p>
<dd> Retrieves an integer (or boolean) option value from the parsed command-line.</p>
<dt><code>CDKparamNumber2</code></p>
<dd> Retrieves an optional integer (or boolean) value from the parsed command-line. If the command line option is not present, the <i>missing</i> value is used.</p>
<dt><code>CDKparamString</code></p>
<dd> Retrieves a string option value from the parsed command-line.</p>
<dt><code>CDKparamString2</code></p>
<dd> Retrieve an optional string option value from the parsed command-line.</p>
<dt><code>CDKparamValue</code></p>
<dd> Retrieve an integer (or boolean) option value from the parsed command-line.</p>
<dt><code>CDKparseParams</code></p>
<dd> Parse the given argc/argv command-line, with the options passed to getopt()&#8217;s 3rd parameter.</p>
<dt><code>CDKparsePosition</code></p>
<dd> Parse the string as one of CDK&#8217;s positioning keywords, or an actual position.</dl>
<h2>SEE ALSO</h2>
<p> cdk_position (3), getopt (3) </p>
<h2>Index</h2>
