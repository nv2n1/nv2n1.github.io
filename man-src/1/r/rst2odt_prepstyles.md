---
title: "rst2odt_prepstyles(1)"
name: "rst2odt_prepstyles"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rst2odt_prepstyles/"
description: "rst2odt_prepstyles – strip paper size specifications off of rst2odt stylesheets"
---

<h2 class="name">NAME</h2>
<p> rst2odt_prepstyles &#8211; strip paper size specifications off of rst2odt stylesheets </p>
<h2>SYNOPSIS</h2>
<p> <code>rst2odt_prepstyles</code> <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-rst2odt/">rst2odt</a></code>(1) uses a stylesheet file as a template for the ODT files it creates. The stock <code>styles.odt</code> file shipped with it comes without page dimensions. When <code>rst2odt</code> is run and detects that there no paper size is given in the stylesheet, it is automatically determined using <code><a href="/docs/linux/man/1-paperconf/">paperconf</a></code>(1). </p>
<p> When editing stylesheets with OpenOffice.org Writer (or similar programs), the resulting files always carry a page size. <code>rst2odt</code> respects this setting and ensures that documents processed with custom stylesheets look the same regardless of the host it is running on. If you want to get the original behavior, i.e. a system-dependent paper size, you can run <code>rst2odt_prepstyles</code> over your custom stylesheet. Remember to re-run the command whenever you change the file with a word processor.</p>
<h2>AUTHOR</h2>
<p> odtwriter is Copyright © 2006-2008 Dave Kuhlman &lt;<i>dkuhlman [at] rexx.com</i>&gt; </p>
<p> This manual page was written by Michael Schutte for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
