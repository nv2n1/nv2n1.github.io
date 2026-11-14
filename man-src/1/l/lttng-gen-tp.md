---
title: "lttng-gen-tp(1)"
name: "lttng-gen-tp"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lttng-gen-tp/"
description: "lttng-gen-tp — LTTng UST 2.x tracepoint code generator"
---

<h2 class="name">NAME</h2>
<p> lttng-gen-tp &#8212; LTTng UST 2.x tracepoint code generator</p>
<h2>SYNOPSIS</h2>
<pre>
lttng-gen-tp [OPTIONS] TEMPLATE_FILE
</pre>
<h2>DESCRIPTION</h2>
<p> The LTTng project aims at providing highly efficient tracing tools for Linux. Its tracers help in tracking down performance issues and debugging problems involving multiple concurrent processes and threads. Tracing across multiple systems is also possible. </p>
<p> The <code>lttng-gen-tp</code> tool simplifies the generation of the UST tracepoint files. It takes a simple template file and generates the necessary code to use the defined tracepoints in your application. The section TEMPLATE FILE FORMAT describes the content of the template file. </p>
<p> Currently, the tool can generate the .h, .c and .o associated with your tracepoint. The generated .h can be directly included in your application. You can let the tool generate the .o or compile the .c yourself. You can compile the .c into a .o, .a or .so at your choice and link it with your application. Refer to the UST documentation for the advantages and disadvantage of each form. To compile the resulting .c file, you need to add the options &quot;-llttng-ust -I.&quot;. </p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax with long options starting with two dashes. Below is a summary of the available options. </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Increase verbosity.</p>
<dt><code>-o, &#8211;output</code></p>
<dd> Specify the generated file. The type of the generated file depend on the file extension (.h, .c, .o). This option can be specified multiple times to generate different file type. </p>
</dl>
<p> When no output is specified the default files are generated with the same base filename as the template file. The default files are: .h, .c, .o. </p>
<h2>TEMPLATE FILE FORMAT</h2>
<p> The template file, which has the usual extension <code>.tp</code>, contains a list of TRACEPOINT_EVENT definitions and other optional definition entries like TRACEPOINT_LOGLEVEL. (See <a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3) for the complete list of available definition.) </p>
<p> You write them as you would write them in a C header file. You can add comments with <code>/* */</code>, <code>//</code> and <code>#</code>. </p>
<p> The provider name (the first field of TRACEPOINT_EVENT) must be the same for the whole file. </p>
<dl>
<dt></dl>
<h2>Example</h2>
<dd>
<dl>
<dt>
<pre>
<dd>TRACEPOINT_EVENT(
    sample_tracepoint,
    message, // Comment
    TP_ARGS(char *, text),
    /* Next are the fields */
    TP_FIELDS(
        ctf_string(message, text)
    )
)
</dl>
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<p> When the tool generates a .o file, it will look for the following environment variables </p>
<dl>
<dt>CC</p>
<dd> Specify which C compiler to use. If the variable is not specified, the tool will try &quot;cc&quot; and &quot;gcc&quot; </p>
<dt>CFLAGS</p>
<dd> Flags directly passed to the compiler</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3), <a href="/docs/linux/man/1-lttng/">lttng</a>(1) </p>
<h2>BUGS</h2>
<p> If you encounter any issues or usability problem, please report it on our mailing list &lt;lttng-dev [at] lists.lttng.org&gt; to help improve this project.</p>
<h2>CREDITS</h2>
<p> lttng-gen-tp is distributed under the GNU General Public License version 2. See the file COPYING for details. </p>
<p> A Web site is available at <a rel="nofollow" href="http://lttng.org">http://lttng.org</a> for more information on the LTTng project. </p>
<p> You can also find our git tree at <a rel="nofollow" href="http://git.lttng.org.">http://git.lttng.org.</a> </p>
<p> Mailing lists for support and development: &lt;lttng-dev [at] lists.lttng.org&gt;. </p>
<p> You can find us on IRC server irc.oftc.net (OFTC) in #lttng. </p>
<h2>AUTHORS</h2>
<p> lttng-gen-tp is written by Yannick Brosseau &lt;yannick.brosseau [at] gmail.com&gt;. </p>
<h2>Index</h2>
