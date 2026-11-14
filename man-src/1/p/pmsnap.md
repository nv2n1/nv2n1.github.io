---
title: "pmsnap(1)"
name: "pmsnap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmsnap/"
description: "pmsnap – generate performance summary snapshot images"
---

<h2>NAME</h2>
<p> <code>pmsnap</code> &#8211; generate performance summary snapshot images</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmsnap</code> [<code>-NV</code>] [<code>-C</code> <i>dir</i>] [<code>-c</code> <i>configs</i>] [<code>-n</code> <i>names</i>] [<code>-o</code> <i>dir</i>] [<code>-t</code> <i>type</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pmsnap</code> is a shell script that is normally run periodically from <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1) to generate graphic images of <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1) performance charts. These images can be in any of the supported <code>pmchart</code> formats, including <i>png</i>, <i>bmp</i>, and <i>jpeg</i>, and may be incorporated into the content offered by the local Web server. The <code>-V</code> option enables verbose tracing of the actions. By default <code>pmsnap</code> generates no output unless some error or warning condition is encountered. </p>
<p> <code>pmsnap</code> generates images according to its control file, <code>$PCP_PMSNAPCONTROL_PATH</code> (or <code>dir/control</code> if the <code>-C</code> option is specified), and uses archive logs created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) or PCP archive folios created by <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1) and <code><a href="/docs/linux/man/1-pmlogger_check/">pmlogger_check</a></code>(1). Before attempting to configure <code>pmsnap</code>, it is strongly recommended that <code>pmlogger</code> be configured according to the descriptions in <code><a href="/docs/linux/man/1-pmlogger_daily/">pmlogger_daily</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger_check/">pmlogger_check</a></code>(1) and <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> Once <code>pmlogger</code> has been configured, it is necessary to configure <code>pmsnap</code> as follows;</p>
<dl>
<dt>1.</p>
<dd> Edit the control file <code>$PCP_PMSNAPCONTROL_PATH</code>. The syntax of this file is described in the comment at the head of the file and an example is supplied for one and twelve hour &quot;Summary&quot; performance charts for the local host. Suitable arguments for <code>pmchart</code> are also described in the comment. The user should consult <code>pmchart</code> for further details. Note that when <code>pmsnap</code> is run, it globally substitutes the string <code>LOCALHOSTNAME</code> with the name of the local host in the control file.</p>
<dt>2.</p>
<dd> Test the configuration by running <center> <code>$PCP_BINADM_DIR/pmsnap</code>.<br />
 </center> Without any arguments <code>pmsnap</code> will process every non-comment line in <code>$PCP_PMSNAPCONTROL_PATH</code>. The output images will be placed in the files named in the first field of each line in the control file, with the file format appended if necessary. If these file names do not start with <code>/</code> or <code>.</code> then they are assumed relative to <i>dir</i>, as specified with the <code>-o</code> option. The default <i>dir</i> is the current directory. Note that if <code>pmlogger</code> has only been recently started (within about the last 15 minutes), snap-shot images may not be produced and no error messages will be issued &#8211; the reason is that <code>pmchart</code> can not use very short archives and hence, neither can <code>pmsnap</code>. For debugging purposes the <code>-V</code> flag should be used.</p>
<dt>3.</p>
<dd> Add an appropriate entry for <code>pmsnap</code> in the <code>root</code> user&#8217;s <code>crontab</code>. An example is supplied in <code>$PCP_VAR_DIR/config/pmlogger/crontab</code>.</p>
<dt>4.</p>
<dd> Incorporate the <code>pmsnap</code> images into the local WWW content. Usually, WWW pages use images that are relative to a particular document root, so it is often convenient to use the <code>-o</code> command line option to specify a sub-directory of the local WWW content, and then create a web page in this directory that shows the snapshot images with text and other content appropriate to the local environment.</dl>
<h2>COMMAND LINE OPTIONS</h2>
<p> <code>pmsnap</code> accepts the following command line options;</p>
<dl>
<dt><code>-C</code><i> dir</i></p>
<dd> The <code>control</code> file is located in the directory <i>dir</i> rather than in the default <code>$PCP_PMSNAPCONTROL_PATH</code> location.</p>
<dt><code>-c</code><i> config-pattern</i></p>
<dd> Only process lines in the control file which match the <i>config-pattern</i> regular expression in the <code>Config</code> column.</p>
<dt><code>-n</code><i> name-pattern</i></p>
<dd> Only process lines in the control file which match the <i>name-pattern</i> regular expression (see <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1)) in the <code>Name</code> column.</p>
<dt><code>-o</code><i> dir</i></p>
<dd> The output images having file names which do not start with <code>/</code> or <code>.</code> will be placed in a directory relative to <i>dir</i>, otherwise the output directory is relative to the current directory (i.e. the default value for <i>dir</i> is <code>./</code>). Note that <i>dir</i> must be a writable directory path and may be on an NFS or CIFS file system.</dl>
<p> The <code>-N</code> option enables a &#8220;show me&#8221; mode, where the actions are echoed, but not executed, in the style of &#8220;make -n&#8221;. Using <code>-N</code> in conjunction with <code>-V</code> maximizes the diagnostic capabilities for debugging. </p>
<p> When either <code>-n</code> or <code>-c</code> are used, <code>pmsnap</code> will only process lines in the control file which match all the supplied patterns. If no patterns are given, then all lines will be processed. These arguments allow multiple entries for <code>pmsnap</code> in <code>crontab</code> so that different performance summary images can be generated at different times or with different frequencies. </p>
<p> A sample HTML page, suitable for the Summary snapshot may be found in <code>$PCP_VAR_DIR/config/pmsnap/Summary.html</code>. </p>
<p> Although <code>pmsnap</code> attempts to flush <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3) output buffers in the relevant <code>pmlogger</code> processes before generating snap-shots images, this may fail for assorted reasons and no error message will be given. </p>
<p> <code>pmsnap</code> should not be invoked immediately after <code>pmlogger_daily</code> has rolled the logs because the new archive logs will be too short to obtain meaningful results. Note however that <code>pmsnap</code> will not report errors from <code>pmchart</code> about not being able to comply with the <code>-A</code> option on very short archives. In these cases no error will be reported and no output images will be produced.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMSNAPCONTROL_PATH</code></p>
<dd> <code>pmsnap</code> control file</p>
<dt><code>$PCP_VAR_DIR/config/pmsnap/Summary</code></p>
<dd> summary view for <code>pmchart</code></p>
<dt><code>$PCP_VAR_DIR/config/pmsnap/Summary.html</code></p>
<dd> sample HTML page for summary snapshot</p>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i><code>/Latest</code></p>
<dd> PCP archive folio for the host <i>hostname</i>, as generated by <code>pmlogger_check</code></p>
<dt><code>$PCP_VAR_DIR/config/pmlogger/crontab</code></p>
<dd> example <code>crontab</code> entry</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cron/">cron</a></code>(1), <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1), <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1), <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger_daily/">pmlogger_daily</a></code>(1), <code><a href="/docs/linux/man/1-x/">X</a></code>(1), and <code><a href="/docs/linux/man/1-xvfb/">Xvfb</a></code>(1). </p>
<h2>Index</h2>
