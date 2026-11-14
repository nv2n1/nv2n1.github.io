---
title: "ooimpress(1)"
name: "ooimpress"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ooimpress/"
description: "libreoffice – LibreOffice office suite"
---

<h2>Name</h2>
<p> libreoffice &#8211; LibreOffice office suite </p>
<h2>SYNOPSIS</h2>
<p> <code>libreoffice</code> [<code>&#8211;accept=</code><i>accept-string</i>] [<code>&#8211;base</code>] [<code>&#8211;calc</code>] [<code>&#8211;convert-to</code> output_file_extension[:output_filter_name] [&#8211;outdir output_dir] <i>file</i>]&#8230; [<code>&#8211;display </code><i>display</i>] [<code>&#8211;draw</code>] [<code>&#8211;global</code>] [<code>&#8211;headless</code>] [<code>&#8211;help</code>|<code>-h</code>|<code>-?</code>] [<code>&#8211;impress</code>] [<code>&#8211;invisible</code>] [<code>&#8211;infilter=&quot;&lt;filter&gt;&quot;</code>] [<code>&#8211;math</code>] [<code>&#8211;minimized</code>] [<code>-n </code><i>file</i>]&#8230; [<code>&#8211;nodefault</code>] [<code>&#8211;nolockcheck</code>] [<code>&#8211;nologo</code>] [<code>&#8211;norestore</code>] [<code>-o </code><i>file</i>]&#8230; [<code>-p </code><i>file</i>&#8230;] [<code>&#8211;print-to-file [&#8211;printer-name printer_name] [&#8211;outdir output_dir] file]&#8230; [&#8211;pt </code><i>printername</i> <i>file</i>&#8230;] [<code>&#8211;show </code><i>Impress file</i>]&#8230; [<code>&#8211;unaccept=</code><i>accept-string</i>] [<code>&#8211;terminate_after_init</code>] [<code>&#8211;view </code><i>file</i>]&#8230; [<code>&#8211;web</code>] [<code>&#8211;writer</code>] [<i>file</i>&#8230;]<br />
 <code>lobase</code><br />
 <code>localc</code><br />
 <code>lodraw</code><br />
 <code>lofromtemplate</code><br />
 <code>loimpress</code><br />
 <code>lomath</code><br />
 <code>loweb</code><br />
 <code>lowriter</code> </p>
<h2>DESCRIPTION</h2>
<p> LibreOffice (LO for short) is a multi-platform office productivity suite. It was derived from OpenOffice.org 3.3 Beta on September 28, 2010. </p>
<p> <code>libreoffice</code> is a shell script that sets up the environment and passes the command line arguments to the <code>soffice.bin</code> binary. </p>
<p> Alternatively, the following helper scripts start the respective module: </p>
<p> sbase, scalc, sdraw, simpress, smath, sofficerc, swriter </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;accept=</code><i>accept-string</i></p>
<dd> Specify a UNO connect-string to create a UNO acceptor through which other programs can connect to access the API. </p>
<dt><code>&#8211;base</code></p>
<dd> Starts the wizard for a new Base document. </p>
<dt><code>&#8211;calc</code></p>
<dd> Starts with a new Calc document. </p>
<dt><code>&#8211;convert-to</code> output_file_extension[:output_filter_name] [&#8211;outdir output_dir] <i>file</i>&#8230;</p>
<dd> Batch converts files. If <i>&#8211;outdir</i> is not specified then the current working directory is used as the output directory for the converted files. It implies <i>&#8211;headless</i>. </p>
<p> Examples: </p>
<p> <code>&#8211;convert-to</code> pdf *.doc </p>
<p> Converts all .doc files to PDFs. </p>
<p> <code>&#8211;convert-to</code> pdf:writer_pdf_Export &#8211;outdir /home/user *.doc </p>
<p> Converts all .doc files to PDFs using the settings in the Writer PDF export dialog and saving them in /home/user. </p>
<dt><code>&#8211;display </code><i>display</i></p>
<dd> This option specifies the X server to use; see <code><a href="/docs/linux/man/7-x/">X</a></code>(7) </p>
<dt><code>&#8211;draw</code></p>
<dd> Starts with a new Draw document. </p>
<dt><code>&#8211;global</code></p>
<dd> Starts with a new Global document. </p>
<dt><code>&#8211;headless</code></p>
<dd> Starts in &quot;headless mode&quot;, which allows using the application without user a interface. </p>
<p> This special mode can be used when the application is controlled by external clients via the API. </p>
<p> It implies &#8211;invisible and strictly ignores any GUI environment. &#8211;quickstart does not work with this parameter. </p>
<dt><code>&#8211;help</code>|<code>-h</code>|<code>-?</code></p>
<dd> Lists LibreOffice command line parameters. </p>
<dt><code>&#8211;impress</code></p>
<dd> Starts with a new Impress document. </p>
<dt><code>&#8211;invisible</code></p>
<dd> Starts in invisible mode. </p>
<p> Neither the start-up logo nor the initial program window will be visible. LO can be controlled and documents and dialogs can be opened via the API. </p>
<p> When started with this parameter, it can only be quit using the taskmanager (Windows) or the kill command (UNIX based systems). </p>
<p> &#8211;quickstart does not work with this parameter. </p>
<dt><code>&#8211;infilter=&quot;&lt;filter&gt;&quot;</code></p>
<dd> Force an input filter type if possible. For example &#8211;infilter=&quot;Calc Office Open XML&quot; only </p>
<dt><code>&#8211;math</code></p>
<dd> Starts with a new Math document. </p>
<dt><code>&#8211;minimized</code></p>
<dd> Keeps the splash screen minimized. </p>
<dt><code>-n </code><i>template</i>&#8230;</p>
<dd> Creates the a new document from the given templates. </p>
<dt><code>&#8211;nodefault</code></p>
<dd> Starts LO without creating a new document. The next time you start LO, the welcome screen is shown. </p>
<p> It&#8217;s used together with <code>&#8211;nologo</code> by quick starters. Note that <code>&#8211;quickstart</code> has no longer been supported since OpenOffice.org 2.0.0. </p>
<dt><code>&#8211;nolockcheck</code></p>
<dd> Disables the check for remote instances using the installation. </p>
<dt><code>&#8211;nologo</code></p>
<dd> Disables the splash screen at program start. </p>
<dt><code>&#8211;norestore</code></p>
<dd> Disables restart and file recovery after a system crash. It is possible that LO will try to restore a file it keeps crashing on, if that happens <code>&#8211;norestore</code> is the only way to start LO. </p>
<dt><code>&#8211;nosplash</code></p>
<dd> Disables the splash screen at program start. </p>
<dt><code>-o </code><i>file</i>&#8230;</p>
<dd> Opens the given files for editing, even templates. </p>
<p> Without <code>-o</code> a template file would create a new document derived from that template. </p>
<dt><code>-p </code><i>file</i>&#8230;</p>
<dd> Prints the given files to the default printer and ends. The splash screen does not appear. </p>
<p> If the file name contains spaces, then it must be enclosed in quotation marks. </p>
<dt><code>&#8211;print-to-file [&#8211;printer-name printer_name] [&#8211;outdir output_dir] file&#8230;</p>
<dd> Batch print files to file. If &#8211;printer-name is not specified the default printer is used. If &#8211;outdir is not specified then the current working directory is used as the output directory for the converted files. </p>
<p> Examples: </p>
<p> &#8211;print-to-file *.doc </p>
<p> Prints all .doc files to the current working directory using the default printer. </p>
<p> &#8211;print-to-file &#8211;printer-name nasty_lowres_printer &#8211;outdir /home/user *.doc </p>
<p> Prints all .doc files to /home/user directory using the nasty_lowres_printer. </p>
<dt>&#8211;pt </code><i>printername</i> <i>file</i>&#8230;</p>
<dd> Prints the given files to the printer <i>printername</i> and ends. The splash screen does not appear. </p>
<p> If a file name contains spaces, then it must be enclosed in quotation marks. </p>
<dt><code>&#8211;quickstart &#8211;quickstart=no</p>
<dd> Starts LO with it&#8217;s quick starter. &#8211;quickstart disable the quick starter. </p>
<p> Does not work with &#8211;invisible or &#8211;headless. </p>
<dt>&#8211;show </code><i>Impress file</i>&#8230;</p>
<dd> Opens the given Impress files, starts the presentation and quits after they have finished. </p>
<dt><code>&#8211;unaccept=</code><i>accept-string</i></p>
<dd> Closes an acceptor that was created with <code>&#8211;accept</code> option. </p>
<p> Use <code>&#8211;unaccept</code>=<i>all</i> to close all open acceptors. </p>
<dt><code>&#8211;terminate_after_init</code></p>
<dd> Starts LO and terminates after it registers some UNO services. Doesn&#8217;t show the splash during startup. </p>
<dt><code>&#8211;view </code><i>file</i>&#8230;</p>
<dd> Opens the given files read-only creating a temporary copy of them at $TMPDIR. </p>
<dt><code>&#8211;web</code></p>
<dd> Starts with a new HTML document. </p>
<dt><code>&#8211;writer</code></p>
<dd> Starts with a new Writer document. </p>
</dl>
<h2>TROUBLESHOOTING PROBLEMS</h2>
<p> See <code><a rel="nofollow" href="http://wiki.documentfoundation.org/BugReport">http://wiki.documentfoundation.org/BugReport</a></code> for more details on how to report bugs in LibreOffice.</p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://www.documentfoundation.org/">http://www.documentfoundation.org/</a></code> </p>
<h2>AUTHOR</h2>
<p> This manual page was created by Rene Engelhard &lt;rene [at] debian.org&gt; for the Debian GNU/Linux Distribution, because the original package does not have one. It was updated for Novell by Petr Mladek &lt;petr.mladek [at] novell.com&gt; and adapted for LibreOffice by Philipp Weissenbacher &lt;philipp.weissenbacher [at] gmail.com&gt;. </p>
<h2>Index</h2>
