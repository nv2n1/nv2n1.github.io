---
title: "filter(7)"
name: "filter"
section: "7"
letter: "f"
url: "/docs/linux/man/7-filter/"
description: "filter – cups file conversion filter interface"
---

<p>filter &#8211; cups file conversion filter interface</p>
<h2>Synopsis</h2>
<pre><code>filter

        job

            user

                title

                    num -
    copies

        options

            [filename

]

#include &lt;cups/cups.h&gt;

    ssize_t
    cupsBackChannelRead(char *buffer, size_t bytes,
                        double timeout);

cups_sc_status_t cupsSideChannelDoRequest(cups_sc_command_t command,
                                          char *data, int *datalen,
                                          double timeout);

#include &lt;cups/ppd.h&gt;

const char *cupsGetOption(const char *name, int num_options,
                          cups_option_t *options);

int cupsMarkOptions(ppd_file_t *ppd, int num_options,
                    cups_option_t *options);

int cupsParseOptions(const char *arg, int num_options,
                     cups_option_t **options);

ppd_choice_t *ppdFindMarkedChoice(ppd_file_t *ppd, const char *keyword);

void ppdMarkDefaults(ppd_file_t *ppd);

ppd_file_t *ppdOpenFile(const char *filename);</code></pre>
<h2>Description</h2>
<p>The CUPS filter interface provides a standard method for adding support for new document types or printers to CUPS. Each filter is capable of converting from one or more input formats to another format that can either be printed directly or piped into another filter to get it to a printable format. </p>
<p> Filters <code>MUST</code> be capable of reading from a filename on the command-line or from the standard input, copying the standard input to a temporary file as required by the file format. All output <code>MUST</code> be sent to the standard output. Filters <code>MUST NOT</code> attempt to communicate directly with the printer, other processes, or other services. </p>
<p> The command name (<i>argv[0]</i>) is set to the name of the destination printer but is also available in the <code>PRINTER</code><i> environment variable. </i></p>
<h2>Options</h2>
<p>Options are passed in <i>argv[5]</i> and are encoded from the corresponding IPP attributes used when the job was submitted. Use the <code>cupsParseOptions</code>() function to load the options into a <code>cups_option_t</code> array and the <code>cupsGetOption</code>() function to get the value of a specific attribute. Be careful to look for common aliases of IPP attributes such as &quot;landscape&quot; for the IPP &quot;orientation-requested&quot; attribute. </p>
<p> Options passed on the command-line typically do not include the default choices the printer&#8217;s PPD file. Use the <code>ppdMarkDefaults</code>() and <code>cupsMarkOptions</code>() functions in the CUPS library to apply the options to the PPD defaults and map any IPP attributes to the corresponding PPD options. Use <code>ppdFindMarkedChoice</code>() to get the user-selected choice for a PPD option. For example, a filter might use the following code to determine the current value of the <code>Duplex</code> PPD option: </p>
<pre> ppd_file_t *ppd = ppdOpenFile(getenv(&quot;PPD&quot;));
 cups_option_t *options = NULL;
 int num_options = cupsParseOptions(argv[5], 0, &amp;options);
 ppdMarkDefaults(ppd);
 cupsMarkOptions(ppd, num_options, options);
 ppd_choice_t *choice = ppdFindMarkedChoice(ppd, &quot;Duplex&quot;);</pre>
<p>Raster filters should use option choices set through the raster page header, as those reflect the options in effect for a given page. Options specified on the command-line determine the default values for the entire job, which can be overridden on a per-page basis.</p>
<h2>Log Messages</h2>
<p>Messages sent to the standard error are generally stored in the printer&#8217;s &quot;printer-state-message&quot; attribute and the current <code>ErrorLog</code> file. Each line begins with a standard prefix:</p>
<dl>
<dt><code>ALERT: </code><i>message</i></p>
<dd>Sets the &quot;printer-state-message&quot; attribute and adds the specified message to the current <code>ErrorLog</code> using the &quot;alert&quot; log level.</p>
<dt><code>ATTR: </code><i>attribute=value </i>[ <i>&#8230; attribute=value</i>]</p>
<dd>Sets the named job or printer attribute(s). The following job attributes can be set: &quot;job-media-progress&quot;. The following printer attributes can be set: &quot;auth-info-required&quot;, &quot;marker-colors&quot;, &quot;marker-high-levels&quot;, &quot;marker-levels&quot;, &quot;marker-low-levels&quot;, &quot;marker-message&quot;, &quot;marker-names&quot;, &quot;marker-types&quot;, &quot;printer-alert&quot;, and &quot;printer-alert-description&quot;.</p>
<dt><code>CRIT: </code><i>message</i></p>
<dd>Sets the &quot;printer-state-message&quot; attribute and adds the specified message to the current <code>ErrorLog</code> using the &quot;critical&quot; log level.</p>
<dt><code>DEBUG: </code><i>message</i></p>
<dd>Adds the specified message to the current <code>ErrorLog</code> using the &quot;debug&quot; log level. <code>DEBUG</code> messages are never stored in the &quot;printer-state-message&quot; attribute.</p>
<dt><code>DEBUG2: </code><i>message</i></p>
<dd>Adds the specified message to the current <code>ErrorLog</code> using the &quot;debug2&quot; log level. <code>DEBUG2</code> messages are never stored in the &quot;printer-state-message&quot; attribute.</p>
<dt><code>EMERG: </code><i>message</i></p>
<dd>Sets the &quot;printer-state-message&quot; attribute and adds the specified message to the current <code>ErrorLog</code> using the &quot;emergency&quot; log level.</p>
<dt><code>ERROR:</code><i> message</i></p>
<dd>Sets the &quot;printer-state-message&quot; attribute and adds the specified message to the current <code>ErrorLog</code> using the &quot;error&quot; log level.</p>
<dt><code>INFO:</code><i> message</i></p>
<dd>Sets the &quot;printer-state-message&quot; attribute. If the current <code>LogLevel</code> is set to &quot;debug2&quot;, also adds the specified message to the current <code>ErrorLog</code> using the &quot;info&quot; log level.</p>
<dt><code>NOTICE:</code><i> message</i></p>
<dd>Sets the &quot;printer-state-message&quot; attribute and adds the specified message to the current <code>ErrorLog</code> using the &quot;notice&quot; log level.</p>
<dt><code>PAGE:</code><i> page-number #-copies</i></p>
<dd>
<dt><code>PAGE:</code><i> total #-pages</i></p>
<dd>Adds an entry to the current <code>PageLog</code>. The first form adds <i>#-copies</i> to the &quot;job-media-sheets-completed&quot; attribute. The second form sets the &quot;job-media-sheets-completed&quot; attribute to <i>#-pages</i>.</p>
<dt><code>PPD:</code><i> Keyword=Value</i> [ <i>&#8230; KeywordN=Value</i> ]</p>
<dd>Sets the named keywords in the printer&#8217;s PPD file. This is typically used to update default option keywords such as <code>DefaultPageSize</code> and the various installable options in the PPD file.</p>
<dt><code>STATE:</code><i> printer-state-reason </i>[ <i>&#8230; printer-state-reason</i> ]</p>
<dd>
<dt><code>STATE: +</code><i> printer-state-reason </i>[ <i>&#8230; printer-state-reason</i> ]</p>
<dd>
<dt><code>STATE: &#8211;</code><i> printer-state-reason </i>[ <i>&#8230; printer-state-reason</i> ]</p>
<dd>Sets, adds, or removes &quot;printer-state-reason&quot; keywords for the current queue. Typically this is used to indicate media, ink, and toner conditions on a printer.</p>
<dt><code>WARNING:</code><i> message</i></p>
<dd>Sets the &quot;printer-state-message&quot; attribute and adds the specified message to the current <code>ErrorLog</code> using the &quot;warning&quot; log level.</dl>
<h2>Environment Variables</h2>
<p>The following environment variables are defined by the CUPS server when executing the filter:</p>
<dl>
<dt><code>CHARSET</code></p>
<dd>The default text character set, typically &quot;utf-8&quot;.</p>
<dt><code>CLASS</code></p>
<dd>When a job is submitted to a printer class, contains the name of the destination printer class. Otherwise this environment variable will not be set.</p>
<dt><code>CONTENT_TYPE</code></p>
<dd>The MIME media type associated with the submitted job file, for example &quot;application/postscript&quot;.</p>
<dt><code>CUPS_CACHEDIR</code></p>
<dd>The directory where semi-persistent cache files can be found and stored.</p>
<dt><code>CUPS_DATADIR</code></p>
<dd>The directory where data files can be found.</p>
<dt><code>CUPS_FILETYPE</code></p>
<dd>The type of file being printed: &quot;job-sheet&quot; for a banner page and &quot;document&quot; for a regular print file.</p>
<dt><code>CUPS_MAX_MESSAGE</code></p>
<dd>The maximum size of a message sent to <i>stderr</i>, including any leading prefix and the trailing newline.</p>
<dt><code>CUPS_SERVERROOT</code></p>
<dd>The root directory of the server.</p>
<dt><code>FINAL_CONTENT_TYPE</code></p>
<dd>The MIME media type associated with the output destined for the printer, for example &quot;application/vnd.cups-postscript&quot;.</p>
<dt><code>LANG</code></p>
<dd>The default language locale (typically C or en).</p>
<dt><code>PATH</code></p>
<dd>The standard execution path for external programs that may be run by the filter.</p>
<dt><code>PPD</code></p>
<dd>The full pathname of the PostScript Printer Description (PPD) file for this printer.</p>
<dt><code>PRINTER</code></p>
<dd>The name of the printer.</p>
<dt><code>RIP_CACHE</code></p>
<dd>The recommended amount of memory to use for Raster Image Processors (RIPs).</p>
<dt><code>SOFTWARE</code></p>
<dd>The name and version number of the server (typically CUPS/<i>major.minor</i>).</p>
<dt><code>TZ</code></p>
<dd>The timezone of the server.</p>
<dt><code>USER</code></p>
<dd>The user executing the filter, typically &quot;lp&quot; or &quot;root&quot;; consult the <i>cups-files.conf</i> file for the current setting.</dl>
<h2>Conforming To</h2>
<p>While the filter interface is compatible with System V interface scripts, CUPS does not support System V interface scripts.</p>
<h2>Notes</h2>
<p>CUPS printer drivers and backends are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1). </p>
<p> CUPS filters are not meant to be run directly by the user. Aside from the legacy System V interface issues (<i>argv[0]</i> is the printer name), CUPS filters also expect specific environment variables and file descriptors, and typically run in a user session that (on macOS) has additional restrictions that affect how it runs. Unless you are a developer and know what you are doing, please do not run filters directly. Instead, use the <code><a href="/docs/linux/man/8-cupsfilter/">cupsfilter</a></code>(8) program to use the appropriate filters to do the conversions you need.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-backend/">backend</a></code>(7), <code><a href="/docs/linux/man/1-cups/">cups</a></code>(1), <code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/8-cupsfilter/">cupsfilter</a></code>(8),<br />
 CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
