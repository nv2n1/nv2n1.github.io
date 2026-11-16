---
title: "ptop(1)"
name: "ptop"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ptop/"
description: "ptop – The FPC Pascal configurable source beautifier."
---

<h2>NAME</h2>
<p> ptop &#8211; The FPC Pascal configurable source beautifier. </p>
<p> Origin probably Pascal-TO-Pascal. </p>
<h2>SYNOPSIS</h2>
<p> <code>ptop</code><i>[-v] [-i indent] [-b bufsize ][-c optsfile] infile outfile</i> </p>
<h2>Description</h2>
<p> <code>ptop</code> is a more or less configurable <i>source beautifier</i> for pascal sources, and specially the ones supported by FPC (which are more or less Turbo Pascal or Delphi 2.0 compatible). </p>
<p> ptop belongs to the <i>FPC utils</i> package, which currently also contains <code>ppdep</code> , <code>h2pas</code> , <code>ppudump</code> and <code>ppumove</code> . </p>
<h2>Usage</h2>
<p> <code>ptop </code> basically reformats &quot;infile&quot; and outputs the result to &quot;outfile&quot;. ituses a configuration file explained further below, and can generate a default configurationfile for you to edit. (not needed if you use the defaults) </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Writes a short description of these switches.</dd>
<dt><code>-c</code></dt>
<dd> read options from configuration file. A configuration file is not needed, ptop will revert to internal defaults then. See also -g</dd>
<dt><code>-i</code><i> ident</i></dt>
<dd> Sets the number of indent spaces used for BEGIN END; and other blocks.</dd>
<dt><code>-b</code><i> bufsize</i></dt>
<dd> Sets the buffersize to bufsize. Default 255, 0 is considered non-valid and ignored.</dd>
<dt><code>-v</code></dt>
<dd> be verbose. Currently only outputs the number of lines read/written and some error messages.</dd>
<dt><code>-g</code><i> ptop.cfg</i></dt>
<dd> Writes a default configuration file to be edited to the file <i>ptop.cfg</i> </dd>
</dl>
<p> Try to play with ptop and its configfile until you find the effect you desire. The configurability and possibilities of ptop are quite large compared to shareware source beautifier found on e.g. SIMTEL. </p>
<h2>Acknowledgements</h2>
<p> The writer of the program, Michael van Canneyt, who also helped out explaining the format of ptop.cfg. </p>
<p> Questions/corrections can be mailed to fpc-devel [at] vekoll.saturnus.vein.hu </p>
<p> Also thanks to the rest of the FPC development team. </p>
<p> The program is a modernized (OOP, Streams, Delphi extensions) version based on a program by Peter Grogono, who in turn based his program on a Pascal pretty-printer written by Ledgard, Hueras, and Singer. See SIGPLAN Notices, Vol. 12, No. 7, July 1977, pages 101-105, and PP.DOC/HLP. <code>This</code>version<code>of</code>PP<code>developed</code>under<code>Pascal/Z</code>V4.0<code>or</code>later. Very minor modifications for Turbo Pascal made by Willett Kempton March 1984 and Oct 84. Runs under 8-bit Turbo or 16-bit Turbo. Toad Hall tweak, rewrite for TP 5, 28 Nov 89 </p>
<h2>SEE ALSO</h2>
<dl>
<dt>ptop config file</dt>
<dd> <code>ptop.cfg</code>(5)</dd>
<dt>Compiler</dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1)</dd>
<dt>Other FPC utils</dt>
<dd> <code><a href="/docs/linux/man/1-ppdep/">ppdep</a></code>(1) <code><a href="/docs/linux/man/1-ppudump/">ppudump</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) <code><a href="/docs/linux/man/1-h2pas/">h2pas</a></code>(1) </dd>
</dl>
<h2>Index</h2>
