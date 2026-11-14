---
title: "tqsl(5)"
name: "tqsl"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tqsl/"
description: "TQSL – digitally sign amateur radio contact logs"
---

<p>TQSL &#8211; digitally sign amateur radio contact logs</p>
<h2>Synopsis</h2>
<p><code>tqsl</code> -i&nbsp;<wbr>[<i>certificate-file</i>]<i></i>&#8230; </p>
<p> <code>tqsl</code> [<i>OPTIONS</i>] [<i>log-file</i>]<i></i>&#8230;</p>
<h2>Description</h2>
<p><code>TrustedQSL</code> is a file format and set of procedures that is used to send digitally signed QSL information (logs of contacts between amateur radio operators). One notable service that makes use of TrustedQSL is ARRL&#8217;s <i>Logbook of the World.</i> </p>
<p> The <code>tqsl</code> program is used to digitally sign contact log files using a digital certificate. It is also used to generate requests for digital certificates and to store the resulting received digital certificates. (Certificates used to be handled by a separate program, <code>tqslcert</code>, but all functions are now handled by tqsl). </p>
<p> This manual page briefly documents the <code>tqsl</code> program. Complete documentation is also available: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>tqsl</code>: file:///usr/share/TrustedQSL/help/tqslapp/main.htm</p>
<h2>Options</h2>
<p><code>tqsl</code> accepts these command line options: </p>
<dl>
<dt><code>-b </code><i>begin_date</i> and -e <i>end_date</i></p>
<dd>Supply a start date and end date for QSOs to be signed. If present, any QSOs before the begin date will be ignored, and any after the end date will be ignored. If either begin or end are omitted, then the corresponding limit is ignored. You should specify <i>-d</i> with this option to suppress the normal date range dialog as these options will override the user-specified dates if given.</p>
<dt><code>-d</code></p>
<dd>Suppress date-range dialog. If present, the QSO date-range dialog will not be shown for files that follow this option on the command line. </p>
<dt><code>-l </code><i>location_name</i></p>
<dd>Selects an existing station location. This location will be used for the commands that follow. If the station location doesn&#8217;t exist, <code>tqsl</code> will just exit. </p>
<dt><code>-o </code><i>output_file</i></p>
<dd>Writes the resulting signed log file to <i>output_file</i> instead of a default name based on the input <i>log-file</i> name. </p>
<dt><code>-s</code></p>
<dd>Add or edit station location. If there is a preceding -l option the specified location will be edited. If there is no preceding -l option, a new station location is being added. </p>
<dt><code>-x</code> (or) <code>-q</code></p>
<dd>Exit <code>tqsl</code>. If this argument is used it should be the last one on the command line. If this argument is not present, <code>tqsl</code> will begin normal operation after successfully processing all command-line arguments. </p>
<dt><code>-u</code></p>
<dd>Upload log file. If this argument is used, the input files will be signed then automatically uploaded to the Logbook of the World web site for processing. </p>
<dt><code>-v</code></p>
<dd>Display the version number of <code>tqsl</code> and exit. </p>
<dt><code>-i filename</code></p>
<dd>Import a certificate &#8211; either a signed response (.tq6) or a certificate stored with a private key in PKCS#12 format (.p12).</p>
<dt><code>-t filename</code></p>
<dd>Open a diagnostic trace file at startup. This file will log internal TQSL function calls for debugging purposes.</p>
<dt><code>log-files</code></p>
<dd>Any command-line parameter that is not an option or an option&#8217;s argument will be treated as the name of a log file (ADIF or Cabrillo) to be signed. The resulting signed file (.tq8) will be placed in the same directory as the log file, overwriting any existing .tq8 file of the same name. (Note: If this option is not preceded by a -l option that selects the station location to be used for signing, the Select Station Location for Signing dialog will be presented.) File names that contain spaces or other shell-special characters should be quoted in a manner suitable for the operating system and shell that&#8217;s being used. If -u is used, the signed log is not saved to disk but is instead uploaded and submitted to Logbook of the World. </p>
<p> N.B.: If the private key needed to sign a log is protected by a password, the user will be prompted to supply that password for each file being signed. </p>
</dl>
<h2>Author</h2>
<p>trustedqsl was written by &quot;American Radio Relay League, Inc.&quot; and the TrustedQSL authors. Please see the AUTHORS.txt file in the source distribution for a list of contributors. </p>
<p> This manual page was originally prepared by Kamal Mostafa &lt;kamal [at] whence.com&gt;, for the Debian project (and may be used by others).</p>
