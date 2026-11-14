---
title: "shtool-platform(1)"
name: "shtool-platform"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-platform/"
description: "shtool platform – GNU shtool Unix platform identification"
---

<h2 class="name">NAME</h2>
<p> shtool platform &#8211; GNU shtool Unix platform identification </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool platform</code> [<code>-F</code>|<code>&#8211;format</code> <i>format</i>] [<code>-S</code>|<code>&#8211;sep</code> <i>string</i>] [<code>-C</code>|<code>&#8211;conc</code> <i>string</i>] [<code>-L</code>|<code>&#8211;lower</code>] [<code>-U</code>|<code>&#8211;upper</code>] [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-c</code>|<code>&#8211;concise</code>] [<code>-n</code>|<code>&#8211;newline</code>] [<code>-d</code>|<code>&#8211;debug</code>] [<code>-t</code>|<code>&#8211;type</code> <i>type</i>] [<code>-n</code>|<code>&#8211;newline</code>] [<code>-d</code>|<code>&#8211;debug</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>shtool platform</code> is a flexible Unix platform identification program. It distinguishes a platform according to its <i>hardware architecture</i> and <i>operating system</i>. For both there is a <i>class</i>, <i>product</i> and <i>technology</i> identification. For each of those six identifications, there is a <i>verbose</i>, <i>regular</i> and <i>concise</i> version. </p>
<p> This leads to eighteen (2x3x3) available identification strings for each platform, from which usually 2 are chosen in a particular situation. This is done by assembling the platform identification string using a <i>format</i> string containing one or more identification constructs of the forms &quot;<tt>&quot;%[xx]&quot;</tt>&#8220; (verbose), &#8221;<tt>&quot;%{xx}&quot;</tt>&#8220; (regular) and &#8221;<tt>&quot;%&lt;xx&gt;&quot;</tt>&quot; (concise).</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-F</code>, <code>&#8211;format</code> <i>format</i></p>
<dd> This option controls the output formatting of this program. It is a plain-text string with the &quot;<tt>&quot;%&quot;</tt><i>xx</i>&#8220; constructs which expand to the various platform information strings. &#8221;<tt>&quot;%{&quot;</tt><i>xx</i><tt>&quot;}&quot;</tt>&#8220; is the canonical regular version of the information. &#8221;<tt>&quot;%[&quot;</tt><i>xx</i><tt>&quot;]&quot;</tt>&#8220; is the verbose version of the information. &#8221;<tt>&quot;%&lt;&quot;</tt><i>xx</i><tt>&quot;&gt;&quot;</tt>&quot; is the concise version of the information. In total, the following constructs are available for expansion: </p>
<pre><code>
% [ac] verbose hardware architecture class
    % {ac} regular hardware architecture class
    % &lt;ac&gt; concise hardware architecture class
    % [ap] verbose hardware architecture product % {ap} regular hardware architecture product % &lt;ap&gt; concise hardware architecture product % [at] verbose hardware architecture technology % {at} regular hardware architecture technology % &lt;at&gt; concise hardware architecture technology % [sc] verbose operating system class
    % {sc} regular operating system class
    % &lt;sc&gt; concise operating system class
    % [sp] verbose operating system product % {sp} regular operating system product % &lt;sp&gt; concise operating system product % [st] verbose operating system technology % {st} regular operating system technology % &lt;st&gt; concise operating system technology
</code></pre>
<p> The default <i>format</i> string is &quot;<tt>&quot;%{sp} (%{ap})&quot;</tt>&quot;, providing the regular operating system and hardware architecture product information.</p>
<dt><code>-S</code>, <code>&#8211;sep</code> <i>string</i></p>
<dd> This option sets the word <i>separation</i> string for the platform information strings. By default it is &quot;<tt>&quot; &quot;</tt>&quot; (whitespace). It is especially used for separating the operating system name and the operating system version.</p>
<dt><code>-C</code>, <code>&#8211;conc</code> <i>string</i></p>
<dd> This option sets the word <i>concatenation</i> string for the platform information strings. By default it is &quot;<tt>&quot;/&quot;</tt>&quot;. It is especially used to concatenate multiple parts in operating system name and version parts.</p>
<dt><code>-L</code>, <code>&#8211;lower</code></p>
<dd> This options enforces conversion of the output to all <i>lower</i> case.</p>
<dt><code>-U</code>, <code>&#8211;upper</code></p>
<dd> This options enforces conversion of the output to all <i>upper</i> case.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> This option enforces verbose versions of all expansion constructs in <i>format</i> string of option <code>-F</code>. It is equal to specifying all expansion constructs as &quot;<tt>&quot;%[&quot;</tt><i>xx</i><tt>&quot;]&quot;</tt>&quot;.</p>
<dt><code>-c</code>, <code>&#8211;concise</code></p>
<dd> This option enforces concise versions of all expansion constructs in <i>format</i> string of option <code>-F</code>. It is equal to specifying all expansion constructs as &quot;<tt>&quot;%&lt;&quot;</tt><i>xx</i><tt>&quot;&gt;&quot;</tt>&quot;.</p>
<dt><code>-n</code>, <code>&#8211;no-newline</code></p>
<dd> This option omits the usual trailing newline character in the output.</p>
<dt><code>-t</code>, <code>&#8211;type</code> <i>type</i></p>
<dd> This option is a meta option which internally sets options <code>-F</code>, <code>-S</code>, <code>-C</code>, <code>-L</code>, <code>-U</code>, <code>-v</code> or <code>-c</code> according to <i></i><font SIZE="-1"><i>TYPE</i></font><i></i>. It can be used to easily specify various commonly known outputs. The following <i></i><font SIZE="-1"><i>TYPE</i></font><i></i>s are available:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>binary</code></p>
<dd> Binary Package Id (OpenPKG <font SIZE="-1">RPM</font>). This is equal to &quot;<tt>&quot;-F '%&lt;ap&quot;</tt>-%&lt;sp&gt;&#8217; -L -S &#8221; -C &#8216;+&#8217;&gt;&#8220; and results in outputs like &#8221;<tt>&quot;ix86-freebsd4.9&quot;</tt>&#8220; and &#8221;<tt>&quot;ix86-debian3.0&quot;</tt>&quot;.</p>
<dt><code>build</code></p>
<dd> Build-Time Checking (OpenPKG <font SIZE="-1">RPM</font>). This is equal to &quot;<tt>&quot;-F '%&lt;at&quot;</tt>-%&lt;st&gt;&#8217; -L -S &#8221; -C &#8216;+&#8217;&gt;&#8220; and results in outputs like &#8221;<tt>&quot;i686-freebsd4.9&quot;</tt>&#8220; and &#8221;<tt>&quot;i586-linux2.4&quot;</tt>&quot;.</p>
<dt><code>gnu</code></p>
<dd> <font SIZE="-1">GNU </font><i>config.guess</i> Style Id. This is similar to <code>build</code> and is equal to &quot;<tt>&quot;-F '&quot;%&lt;at&quot;</tt>-unknown-%&lt;st&gt;&#8217; -L -S &#8221; -C &#8216;+&#8217;&gt;&#8220; and results in outputs like &#8221;<tt>&quot;i686-unknown-freebsd4.9&quot;</tt>&#8220; and &#8221;<tt>&quot;i586-unknown-linux2.4&quot;</tt>&quot;.</p>
<dt><code>web</code></p>
<dd> <font SIZE="-1">HTTP</font> Server Header Id. This is equal to &quot;<tt>&quot;-F '&quot;%&lt;sp&quot;</tt>-%&lt;ac&gt;&#8217; -S &#8216;/&#8217; -C &#8216;+&#8217;&gt;&#8220; and results in outputs like &#8221;<tt>&quot;FreeBSD/4.9-iX86&quot;</tt>&#8220; and &#8221;<tt>&quot;Debian/3.0-iX86&quot;</tt>&quot;.</p>
<dt><code>summary</code></p>
<dd> Human Readable Verbose Summary Information. This is equal to &quot;<tt>&quot;-F 'Class: %[sc] (%[ac])
Product: %[sp] (%[ap])
Technology: %[st] (%[at])' -S ' ' -C '/'&quot;</tt>&quot; and results in outputs like: </p>
<pre>
 Class:      4.4BSD (iX86)
 Product:    FreeBSD 4.9-RC (iX86)
 Technology: FreeBSD 4.9-RC (i686)
</pre>
<p> and </p>
<pre>
 Class:      LSB (iX86)
 Product:    Debian GNU/Linux 3.0 (iX86)
 Technology: GNU/Linux 2.2/2.4 (i686)
</pre>
<dt><code>all-in-one</code></p>
<dd> All-In-One Full-Table Information. This just outputs really all 2x2x3 identification strings as a table.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> This option enables some internal debugging messages.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> This option outputs the version information of <code>shtool platform</code> only.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> This option outputs the usage information of <code>shtool platform</code> only.</dl>
<h2>EXAMPLE</h2>
<p> The following real-life use cases are known:</p>
<dl>
<dt><code>OpenPKG</code> build-time decisions</p>
<dd>
<pre>
 $ platform -c -L -S &quot;&quot; -C &quot;+&quot; -F &quot;%at-%st&quot;
 $ platform -c -L -S &quot;&quot; -C &quot;+&quot; -F &quot;%ac-%sc&quot;
</pre>
<dt><code>OpenPKG</code> binary <font SIZE="-1">RPM</font> packages</p>
<dd>
<pre>
 $ platform -c -L -S &quot;&quot; -C &quot;+&quot; -F &quot;%ap-%sp&quot;
</pre>
<dt><i></i><font SIZE="-1"><i>README</i></font><i></i> files</p>
<dd>
<pre>
 $ platform -v -F &quot;%sp (%ap)&quot;
 $ platform -v -F &quot;%sc (%ac)&quot;
</pre>
<dt>Debugging</p>
<dd>
<pre>
 $ platform --type=all-in-one
</pre>
</dl>
<h2>SUPPORT</h2>
<p> <code>shtool platform</code> currently knows the following particular Unix platforms in detail: FreeBSD, NetBSD, OpenBSD, Linux, Sun Solaris, <font SIZE="-1">SCO</font> UnixWare, <font SIZE="-1">QNX</font> Neutrino, <font SIZE="-1">SGI IRIX, HP</font> HP-UX, <font SIZE="-1">HP</font> Tru64, <font SIZE="-1">IBM AIX</font> and Apple Mac <font SIZE="-1">OS X</font> Darwin. </p>
<p> All other Unix platforms are recognized through generic <i><a href="/docs/linux/man/1-uname/">uname</a></i>(1) information and so usually can be identified sufficiently, although the identification might be not as precise as possible.</p>
<h2>HISTORY</h2>
<p> <code>shtool platform</code> was implemented in September 2003 by <i>Ralf S. Engelschall</i> for use in the <font SIZE="-1"><code>OSSP</code></font> and <code>OpenPKG</code> projects. It was prompted by the need in <code>OpenPKG</code> to have both product (for <font SIZE="-1">RPM</font> filenames) and technology (for build-time decisions) identifiers for the Unix platforms, OpenPKG packages are maintained for. It was inspired by the <font SIZE="-1"><code>GNU</code></font> <i>config.guess</i> and the old <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <i>guessos</i> command. </p>
<p> The major difference to <font SIZE="-1"><code>GNU</code></font> <i>config.guess</i> is that <code>shtool platform</code> does not use a <i>vendor</i> identification (cannot be determined most of the time and is not used at all in all projects I&#8217;ve ever seen) and is a lot more flexible (class, product and technology identifications combined with verbose, regular and concise outputs). The drawback of <code>shtool platform</code> is that it (still) knows less particular platforms, although the generic platform identification is sufficient enough most of the time.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-uname/">uname</a></i>(3), <font SIZE="-1">GNU </font><i>config.guess</i>. </p>
<h2>Index</h2>
