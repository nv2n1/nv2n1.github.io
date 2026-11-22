---

title: "gvnccapture(1)"
name: "gvnccapture"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvnccapture/"
---

gvnccapture - VNC screenshot capture 

<h2>SYNOPSIS</h2>

 gvnccapture [OPTION]... [HOST][:DISPLAY] FILENAME

<h2>DESCRIPTION</h2>

 Capture a screenshot of the VNC desktop at HOST:DISPLAY saving to the image file FILENAME. If HOST is omitted it defaults to ``localhost'', if :DISPLAY is omitted, it defaults to ``:1''. FILENAME must end in a known image format extension (eg ``.png'', ``.jpeg''). Supported options are
<dl>
<dt>--help, -?
</dt><dd> Display command line help information
</dd><dt>--quiet, -q
</dt><dd> Do not display information on the console when capturing the screenshot, with the exception of any password prompt.
</dd><dt>--debug, -d
</dt><dd> Display verbose debugging information on the console</dd></dl>

<h2>EXIT STATUS</h2>

 The exit status is 0 upon successful screen capture, otherwise it is a non-zero integer

<h2>EXAMPLES</h2>

 <pre>
 # gvnccapture localhost:1 desktop.png
 Password:
 Connected to localhost:1
 Saved display to desktop.png
</pre>

<h2>AUTHORS</h2>

 Daniel P. Berrange &lt;dan [at] berrange.com&gt;

<h2>COPYRIGHT</h2>

 Copyright (C) 2010 Daniel P. Berrange &lt;dan [at] berrange.com&gt;. 

 License LGPLv2+: GNU Lesser GPL version 2 or later &lt;<a rel="nofollow" HREF="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. 

 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-vinagre/">vinagre</a></i>(1)
