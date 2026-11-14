---
title: "texconfig-sys(1)"
name: "texconfig-sys"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texconfig-sys/"
description: "texconfig – configures teTeX or TeX Live"
---

<h2>NAME</h2>
<p> texconfig &#8211; configures teTeX or TeX Live </p>
<p> texconfig-sys &#8211; configures teTeX or TeX Live system-wide</p>
<h2>SYNOPSIS</h2>
<p> <code>texconfig</code> </p>
<p> <code>texconfig</code> [<code> commands</code> &#8230;] </p>
<p> <code>texconfig-sys</code></p>
<h2>DESCRIPTION</h2>
<p> <i>texconfig</i> allows one to configure and maintain TeX in an easy and convenient manner, offering a series of dialog boxes to the user. </p>
<p> The <i>tlmgr</i> program has subsumed this function for TeX Live. This program is still supported, but the tlmgr interface is much more actively developed and tested. </p>
<p> After choosing settings or options, the appropriate files are changed automatically and the new settings are applied for the user. If needed, copies of files in <i>TEXMFDIST</i> or <i>TEXMFMAIN</i> will be made in the user&#8217;s <i>TEXMFCONFIG</i> tree. </p>
<p> <i>texconfig</i> uses either the <i><a href="/docs/linux/man/1-whiptail/">whiptail</a></i>(1) or <i><a href="/docs/linux/man/1-dialog/">dialog</a></i>(1) program to communicate with the user, so must be run in a terminal. </p>
<p> For making system-wide changes, which will apply to all users of TeX (for example, default paper size and so on), run <i>texconfig-sys</i> instead. Changed or generated files will be placed in <i>TEXMFSYSCONFIG</i>. (You may need to be root to do this.) </p>
<p> <i>texconfig</i> also offers a non-interactive batch mode which can be accessed with the following commands</p>
<h2>COMMANDS</h2>
<p> Commands that accept further options usually display available options if called without them. For example, <code>texconfig dvipdfm paper</code> will inform about valid paper settings. </p>
<p> <code></p>
<dl>
<dt>conf</p>
<dd> </code> Display the system configuration.</dl>
<dl>
<dt><code>dvipdfm paper [letter|legal|ledger|tabloid|a4|a3]</code></p>
<dd> Set up dvipdfm to use papersize PAPER by default.</p>
<dt><code>dvips add PRINTERNAME</code></p>
<dd> Create a new (empty) configuration file <i>TEXMFCONFIG/dvips/config/config.PRINTERNAME.</i> This file can later be filled with the <code>mode, offset</code> or <code>printcmd</code> options</p>
<dt><code>dvips del PRINTERNAME</code></p>
<dd> Remove <i>config.PRINTERNAME</i></p>
<dt><code>dvips mode</code></p>
<dd> List available MetaFont modes.</p>
<dt><code>dvips [-P PRINTER] mode MODE</code></p>
<dd> Change the MetaFont mode to <i>MODE</i> for <i>PRINTER</i> or for all output files <i>(config.ps),</i> if no <code>-P</code> option is given.</p>
<dt><code>dvips [-P PRINTER] offset x-OFFSET,y-OFFSET</code></p>
<dd> Set printer offset for <i>PRINTER</i> or for all output files <i>(config.ps),</i> if no <code>-P</code> option is given. Offsets must be given with units, e.g. <i>0pt,10pt</i> You can use testpage.tex from the LaTeX distribution to find these numbers.</p>
<dt><code>dvips [-P PRINTER] printcmd CMD</code></p>
<dd> Set the printing command for <i>PRINTER</i> or for all output files <i>(config.ps),</i> if no <code>-P</code> option is given. Commands might be <code>lp</code> or <code>lpr.</code> See the description of the <i>o</i> option in <code>info dvips</code> or the <i>-O</i> option in <code><a href="/docs/linux/man/1-dvips/">dvips</a>(1).</code></p>
<dt><code>faq</code></p>
<dd> Display the list of Frequently Asked Questions about <code>teTeX</code> (and their answers).</p>
<dt><code>font vardir DIR, font ro, font rw</code></p>
<dd>
<dt><code>formats</code></p>
<dd> This command allows to edit <code><a href="/docs/linux/man/5-fmtutil-cnf/">fmtutil.cnf</a>(5)</code> and (re)creates any new or changed formats afterwards.</p>
<dt><code>hyphen FORMAT</code></p>
<dd> This command allows to edit the hyphenation configuration file for formats that support this, and recreates the formats afterwards to enable the new languages. Available formats are shown when no <i>FORMAT</i> is given.</p>
<dt>
<dd> Note that for formats that use LaTeX&#8217;s <i>language.dat,</i><br />
&nbsp;<wbr>e.g. <i>(pdf)jadetex</i> and <i>latex</i> itself, this change is not persistent, since this file is a generated file. You should not use this command in these cases, read <code><a href="/docs/linux/man/1-update-language/">update-language</a>(1)</code> for alternatives.</p>
<dt><code>init [format]</code></p>
<dd> Recreate <i>format</i> or all formats if none is given, and the font information. This is the same as calling <code>fmtutil &#8211;byfmt format</code> or <code>fmtutil &#8211;all,</code> respectively, followed by <code>updmap.</code></p>
<dt><code>mode-list</code></p>
<dd> List available printer modes, together with the printers they were developed for, and their DPI resolution</p>
<dt><code>mode MODE</code></p>
<dd> Set the default printer mode in <i>/etc/texmf/web2c/mktex.cnf</i> or the respective user file in <i>$TEXMFCONFIG/web2c</i> to <code>MODE.</code></p>
<dt><code>paper [a4|letter]</code></p>
<dd> Set the default papersize for <code>dvips, dvipdfm, pdftex</code> and <code>xdvi.</code> The set is restricted because not all programs understand all sizes.</p>
<dt><code>pdftex paper [a4|letter]</code></p>
<dd> Set the default paper size for <code>pdftex.</code></p>
<dt><code>rehash</code></p>
<dd> Call <code>mktexlsr.</code></p>
<dt><code>xdvi paper PAPER</code></p>
<dd> Set the default paper size for <code>xdvi.</code> The (long) list is available with <code>texconfig xdvi paper.</code> </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> To let you change files, <code>texconfig</code> will open the editor specified in the VISUAL or EDITOR variables, or <code>sensible-editor</code> if both are unset.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-whiptail/">whiptail</a></i>(1), <i><a href="/docs/linux/man/1-dialog/">dialog</a></i>(1), <i><a href="/docs/linux/man/1-tlmgr/">tlmgr</a></i>(1), <i><a href="/docs/linux/man/1-tex/">tex</a></i>(1), <i><a href="/docs/linux/man/1-mf/">mf</a></i>(1), <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1), <i>EDITOR</i> environment variable.</p>
<h2>AUTHOR</h2>
<p> Thomas Esser </p>
<h2>Index</h2>
