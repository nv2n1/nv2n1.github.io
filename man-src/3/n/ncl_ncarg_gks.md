---
title: "ncl_ncarg_gks(3)"
name: "ncl_ncarg_gks"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ncarg_gks/"
description: "NCAR Graphics GKS – Environment variables"
---

<p>NCAR Graphics GKS &#8211; Environment variables</p>
<h2>Synopsis</h2>
<p>A collection of environment variables allows you to control certain aspects of NCAR Graphics&#8217; GKS behaviour. <code>NCARG_GKS_OUTPUT</code> allows you to specify what file or process CGM output is directed to. <code>NCARG_GKS_PSOUTPUT</code> allows you to specify what file any PostScript output from NCAR GKS is directed to (stdout is allowed). <code>NCARG_GKS_PDFOUTPUT</code> allows you to specify what file any PDF output from NCAR GKS is directed to (stdout is allowed). <code>NCARG_GKS_GENCGM</code> allows you to request that the NCAR GKS package generate binary encoded CGM rather than NCGM (the NCAR private encoding of binary encoded CGM). Note that other NCAR Graphics utilities, such as the metafile translators, cannot read in generic CGM. <code>NCARG_GKS_BUFSIZE</code> provides you with control over how CGM output is buffered. </p>
<pre><code>NCARG_GKS_DEBUG, if set, will result in debugging information
about the GKS I/O subsystem being output to standard out.</code></pre>
<h2><code>NCARG_GKS_OUTPUT</code></h2>
<p>By default, CGM output is directed to a file called &quot;gmeta&quot;, but the environment variable <code>NCARG_GKS_OUTPUT</code> can be used to redirect output to a file with a different name or a translator process. <i>Examples</i>: setenv NCARG_GKS_OUTPUT myfile causes CGM output to be placed in &quot;myfile&quot;. setenv NCARG_GKS_OUTPUT &quot;|ctrans&quot; causes the &quot;ctrans&quot; translator to be forked and CGM output piped to it. setenv NCARG_GKS_OUTPUT &quot;|&quot; causes a default translator to be forked and CGM output to be piped to it. Note that not just any process can be used here because it is assumed that the process is invoked as &quot;translatorname -&quot; where the &quot;-&quot; indicates that the translator is to read from standard input.</p>
<h2><code>NCARG_GKS_PSOUTPUT</code></h2>
<p>By default, PostScript output is written to &quot;gmetaNN.sfx&quot; where &quot;NN&quot; is the NCAR GKS workstation ID used in the call to GOPWK to open the workstation and &quot;sfx&quot; is &quot;ps&quot;, &quot;eps&quot;, or &quot;epsi&quot; as appropriate. Setting NCARG_GKS_PSOUTPUT will override all defaults and write any PostScript output to the designated file. <i>Examples</i>: setenv NCARG_GKS_PSOUTPUT myfile causes all PostScript output to be written to &quot;myfile&quot;. setenv NCARG_GKS_PSOUTPUT stdout causes all PostScript output to be written to standard out.</p>
<h2><code>NCARG_GKS_PDFOUTPUT</code></h2>
<p>By default, PDF output is written to &quot;gmetaNN.pdf&quot; where &quot;NN&quot; is the NCAR GKS workstation ID used in the call to GOPWK to open the workstation. Setting NCARG_GKS_PDFOUTPUT will override all defaults and write any PDF output to the designated file. <i>Examples</i>: setenv NCARG_GKS_PDFOUTPUT myfile causes all PDF output to be written to &quot;myfile&quot;. setenv NCARG_GKS_PDFOUTPUT stdout causes all PDF output to be written to standard out.</p>
<h2><code>NCARG_GKS_GENCGM</code></h2>
<p>If the NCARG_GKS_GENCGM environment variable is set, GKS<br />
will strip off the NCAR wrapper and generate a binary encode CGM.<br />
As mentioned above, other NCAR Graphics utilities<br />
such as translators don&#8217;t yet support generic CGM as<br />
input. Thus, this option is useful primarily for getting CGM<br />
output into a form appropriate for use with other software<br />
packages that expect binary encoded CGM. <i>Example</i>: setenv NCARG_GKS_GENCGM</p>
<h2><code>NCARG_GKS_BUFSIZE</code></h2>
<p>If output is to a standard file, buffered I/O is used and the NCARG_GKS_BUFSIZE environment variable provides you with some flexibility in specifying buffer size. On Cray systems, the default buffer size is 1MB. All others use whatever the system default is, as specified in the file &quot;stdio.h&quot;. If the environment variable NCARG_GKS_BUFSIZE is set, it overrides the defaults. If NCARG_GKS_BUFSIZE is set to <i>N,</i> behavior is as follows: If <i>N</i> is 0: CGM output is <i>unbuffered</i>. If <i>N</i> is not 0: Buffer Size = <i>N</i> * 1024 bytes. <i>Examples</i> Let&#8217;s suppose you&#8217;re running a long multi-frame graphics job<br />
on a Cray supercomputer and you&#8217;d like to use a very large I/O buffer.<br />
The default for a Cray is 1MB but you&#8217;d like to make it 2MB. setenv NCARG_GKS_BUFSIZE 2048 Now let&#8217;s assume you&#8217;re on the same Cray computer, but you want to pipe you&#8217;re output to a translator and view the frames as they come up. A big buffer is a bad idea because your CGM might not be flushed out every frame. You can make the output unbuffered as follows: </p>
<pre>setenv NCARG_GKS_OUTPUT &quot;|ctrans&quot;
setenv NCARG_GKS_BUFSIZE 0</pre>
<p>As a final example, let&#8217;s say you&#8217;re running the big multi-frame NCAR Graphics job on a Sun, which happens to have a default buffer size of 1024 bytes (look in /usr/include/stdio.h). Specify a 1MB buffer using: setenv NCARG_GKS_BUFSIZE 1024 </p>
<h2>Caveats</h2>
<p>It&#8217;s worth saying one more time: if you output binary encoded CGM rather than NCGM (NCAR CGM), NCAR Graphics generally won&#8217;t deal with it. The one exception is that you can convert the file back to NCGM using <i>cgm2ncgm</i>.</p>
<h2>See Also</h2>
<p><code>cgm2ncgm(1NCARG),</code> <code>ncargintro(5NCARG),</code> <code>ncarg_env(5NCARG)</code></p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
