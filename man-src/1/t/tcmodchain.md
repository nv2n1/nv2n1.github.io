---
title: "tcmodchain(1)"
name: "tcmodchain"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcmodchain/"
description: "tcmodchain – Query compatibily of transcode modules chains."
---

<h2>NAME</h2>
<p> tcmodchain &#8211; Query compatibily of transcode modules chains.</p>
<h2>SYNOPSIS</h2>
<p> <code>tcmodchain</code> [ <code>-m</code> <i>path</i> ] [ <code>-C</code> ] [ <code>-L</code> ] [ <code>-d</code> <i>verbosity</i> ] [ <code>-v</code> ] module1 module2</p>
<h2>COPYRIGHT</h2>
<p> <code>tcmodchain</code> is Copyright (C) by Transcode Team</p>
<h2>DESCRIPTION</h2>
<p> <code>tcmodchain</code> allow to inspect <a href="/docs/linux/man/1-transcode/">transcode</a>(1) modules, as well as it&#8217;s companion, <a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a>(1). While <a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a>(1) focus on single modules, tcmodchain is intended to help in exploring/experimenting module interactions.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m</code> <i>path</i></p>
<dd> Look in <i>Path</i> instead of the compiled-in module path while trying to load a module.</p>
<dt><code>-C</code></p>
<dd> Enable <i>check</i> mode.<br />
 In check mode tcmodchain expects exactly two module identifiers. tcmodchain will check compatibilty between two given modules. Result will be logged out or not depending of verbosity level. Anyway, if two modules are compatible, tcmodchain will exit succesfully; otherwise, tcmodchain will exit with error.<br />
 see RETURN VALUES below.</p>
<dt><code>-L</code></p>
<dd> Enable <i>list</i> mode.<br />
 In list mode tcmodchain expects exactly two module identifiers, exactly one of which containing a wildcard. tcmodchain will inspect all avalaible installed modules matching the wildcard and will print out module names that are compatible with the other given one. if at least one compatible module is found, tcmodchain will exit succesfully; otherwise, tcmodchain will exit with error.<br />
 see RETURN VALUES below. </p>
<dt><code>-d</code> <i>verbosity</i></p>
<dd> Specify the verbosiness level to use, like transcode does. Default value is 1 (TC_INFO verbosiness).</p>
<dt><code>-v</code></p>
<dd> Print version information and exit.</dl>
<h2>MODULE IDENTIFIERS</h2>
<p> <code>tcmodchain</code> identifies modules using a <i>type:name</i> naming scheme. Currently, as in transcode 1.1.0, only <i>encode</i> and <i>multiplex</i> module <i>type</i>s are supported. <i>name</i> can refer to the name of any avalaible transcode modules, using the same rules of <a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a>(1) <i>-i</i> option. The wildcard character <i>*</i> is supported in the <i>name</i> section of module identifier. Wildcard meaning is `any of avalaible modules&#8217; and is honoured only when <i>list</i> mode (-L option) is used. Using wildcard character for <i>both</i> module identifiers will lead to an error. </p>
<h2>EXAMPLES</h2>
<p> <code>$ tcmodchain -C encode:null multiplex:null -d 1</code> </p>
<p> [encode_null.so] v0.0.3 (2005-06-05) null (fake) A/V encoder<br />
 [multiplex_null.so] v0.0.2 (2005-12-29) discard each encoded frame<br />
 [tcmodchain] encode:null | multiplex:null [OK]<br />
 [tcmodchain] module chain OK </p>
<p> <code>$ tcmodchain -L &#8216;encode:*&#8217; multiplex:null</code> </p>
<p> copy<br />
 faac<br />
 lame<br />
 lzo<br />
 null<br />
 x264<br />
 xvid </p>
<p> <code>PLEASE NOTE</code> that output of this example may vary depending of your installation.<br />
 At least <i>null</i> and <i>copy</i> modules will be showed on your output. </p>
<p> <code>$ tcmodchain -L encode:null &#8216;multiplex:*&#8217;</code> </p>
<p> avi<br />
 null<br />
 raw<br />
 y4m </p>
<h2>RETURN VALUES</h2>
<p> <code>tcmodchain</code> uses following return values: </p>
<p>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>successfull </p>
<p>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>bad parameter or command line option </p>
<p>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>error while&nbsp;<wbr>(un)loading a module </p>
<p>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>given module pair isn&#8217;t compatible </p>
<p>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>error while looking for module(s) </p>
<h2>AUTHORS</h2>
<p> <code>tcmodchain</code> was written by Francesco Romani<br />
 &lt;fromani [at] gmail.com&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) <code><a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a></code>(1) </p>
<h2>Index</h2>
