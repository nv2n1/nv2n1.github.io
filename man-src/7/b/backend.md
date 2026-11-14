---
title: "backend(7)"
name: "backend"
section: "7"
letter: "b"
url: "/docs/linux/man/7-backend/"
description: "backend – cups backend transmission interfaces"
---

<p>backend &#8211; cups backend transmission interfaces</p>
<h2>Synopsis</h2>
<pre><code>backend

        backend

            job

                user

                    title

                        num -
    copies

        options

            [filename

]

#include &lt;cups/cups.h&gt;

    const char *
    cupsBackendDeviceURI(char **argv);

void cupsBackendReport(const char *device_scheme,
                       const char *device_uri,
                       const char *device_make_and_model,
                       const char *device_info,
                       const char *device_id,
                       const char *device_location);

ssize_t cupsBackChannelWrite(const char *buffer,
                             size_t bytes, double timeout);

int cupsSideChannelRead(cups_sc_command_t *command,
                        cups_sc_status_t *status, char *data,
                        int *datalen, double timeout);

int cupsSideChannelWrite(cups_sc_command_t command,
                         cups_sc_status_t status, const char *data,
                         int datalen, double timeout);</code></pre>
<h2>Description</h2>
<p>Backends are a special type of <code><a href="/docs/linux/man/7-filter/">filter</a></code>(7) which is used to send print data to and discover different devices on the system. </p>
<p> Like filters, backends must be capable of reading from a filename on the command-line or from the standard input, copying the standard input to a temporary file as required by the physical interface. </p>
<p> The command name (<i>argv[0]</i>) is set to the device URI of the destination printer. Authentication information in <i>argv[0]</i> is removed, so backend developers are urged to use the <code>DEVICE_URI</code> environment variable whenever authentication information is required. The <code>cupsBackendDeviceURI</code>() function may be used to retrieve the correct device URI. </p>
<p> Back-channel data from the device should be relayed to the job filters using the <i>cupsBackChannelWrite</i> function. </p>
<p> Backends are responsible for reading side-channel requests using the <code>cupsSideChannelRead</code>() function and responding with the <code>cupsSideChannelWrite</code>() function. The <code>CUPS_SC_FD</code> constant defines the file descriptor that should be monitored for incoming requests.</p>
<h3>Device Discovery</h3>
<p>When run with no arguments, the backend should list the devices and schemes it supports or is advertising to the standard output. The output consists of zero or more lines consisting of any of the following forms: </p>
<pre> device-class scheme &quot;Unknown&quot; &quot;device-info&quot;
 device-class device-uri &quot;device-make-and-model&quot; &quot;device-info&quot;
 device-class device-uri &quot;device-make-and-model&quot; &quot;device-info&quot; &quot;device-id&quot;
 device-class device-uri &quot;device-make-and-model&quot; &quot;device-info&quot; &quot;device-id&quot; &quot;device-location&quot;</pre>
<p>The <code>cupsBackendReport</code>() function can be used to generate these lines and handle any necessary escaping of characters in the various strings. </p>
<p> The <i>device-class</i> field is one of the following values:</p>
<dl>
<dt><code>direct</code></p>
<dd>The device-uri refers to a specific direct-access device with no options, such as a parallel, USB, or SCSI device.</p>
<dt><code>file</code></p>
<dd>The device-uri refers to a file on disk.</p>
<dt><code>network</code></p>
<dd>The device-uri refers to a networked device and conforms to the general form for network URIs.</p>
<dt><code>serial</code></p>
<dd>The device-uri refers to a serial device with configurable baud rate and other options. If the device-uri contains a baud value, it represents the maximum baud rate supported by the device.</dl>
<p> The <i>scheme</i> field provides the URI scheme that is supported by the backend. Backends should use this form only when the backend supports any URI using that scheme. The <i>device-uri</i> field specifies the full URI to use when communicating with the device. </p>
<p> The <i>device-make-and-model</i> field specifies the make and model of the device, e.g. &quot;Example Foojet 2000&quot;. If the make and model is not known, you must report &quot;Unknown&quot;. </p>
<p> The <i>device-info</i> field specifies additional information about the device. Typically this includes the make and model along with the port number or network address, e.g. &quot;Example Foojet 2000 USB #1&quot;. </p>
<p> The optional <i>device-id</i> field specifies the IEEE-1284 device ID string for the device, which is used to select a matching driver. </p>
<p> The optional <i>device-location</i> field specifies the physical location of the device, which is often used to pre-populate the printer-location attribute when adding a printer.</p>
<h3>Permissions</h3>
<p>Backends without world read and execute permissions are run as the root user. Otherwise, the backend is run using an unprivileged user account, typically &quot;lp&quot;.</p>
<h2>Exit Status</h2>
<p>The following exit codes are defined for backends:</p>
<dl>
<dt><code>CUPS_BACKEND_OK</code></p>
<dd>The print file was successfully transmitted to the device or remote server.</p>
<dt><code>CUPS_BACKEND_FAILED</code></p>
<dd>The print file was not successfully transmitted to the device or remote server. The scheduler will respond to this by canceling the job, retrying the job, or stopping the queue depending on the state of the <i>printer-error-policy</i> attribute.</p>
<dt><code>CUPS_BACKEND_AUTH_REQUIRED</code></p>
<dd>The print file was not successfully transmitted because valid authentication information is required. The scheduler will respond to this by holding the job and adding the &#8216;cups-held-for-authentication&#8217; keyword to the &quot;job-reasons&quot; Job Description attribute.</p>
<dt><code>CUPS_BACKEND_HOLD</code></p>
<dd>The print file was not successfully transmitted because it cannot be printed at this time. The scheduler will respond to this by holding the job.</p>
<dt><code>CUPS_BACKEND_STOP</code></p>
<dd>The print file was not successfully transmitted because it cannot be printed at this time. The scheduler will respond to this by stopping the queue.</p>
<dt><code>CUPS_BACKEND_CANCEL</code></p>
<dd>The print file was not successfully transmitted because one or more attributes are not supported or the job was canceled at the printer. The scheduler will respond to this by canceling the job.</p>
<dt><code>CUPS_BACKEND_RETRY</code></p>
<dd>The print file was not successfully transmitted because of a temporary issue. The scheduler will retry the job at a future time &#8211; other jobs may print before this one.</p>
<dt><code>CUPS_BACKEND_RETRY_CURRENT</code></p>
<dd>The print file was not successfully transmitted because of a temporary issue. The scheduler will retry the job immediately without allowing intervening jobs.</dl>
<p> All other exit code values are reserved.</p>
<h2>Environment</h2>
<p>In addition to the environment variables listed in <code><a href="/docs/linux/man/1-cups/">cups</a></code>(1) and <code><a href="/docs/linux/man/7-filter/">filter</a></code>(7), CUPS backends can expect the following environment variable:</p>
<dl>
<dt><code>DEVICE_URI</code></p>
<dd>The device URI associated with the printer.</dl>
<h2>Files</h2>
<p><i>/etc/cups/cups-files.conf</i></p>
<h2>Notes</h2>
<p>CUPS backends are not generally designed to be run directly by the user. Aside from the device URI issue ( <i>argv[0]</i> and <code>DEVICE_URI</code> environment variable contain the device URI), CUPS backends also expect specific environment variables and file descriptors, and typically run in a user session that (on macOS) has additional restrictions that affect how it runs. Backends can also be installed with restricted permissions (0500 or 0700) that tell the scheduler to run them as the &quot;root&quot; user instead of an unprivileged user (typically &quot;lp&quot;) on the system. </p>
<p> Unless you are a developer and know what you are doing, please do not run backends directly. Instead, use the <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1) or <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1) programs to send print jobs or <code><a href="/docs/linux/man/8-lpinfo/">lpinfo</a></code>(8) to query for available printers using the backend. The one exception is the SNMP backend &#8211; see <code><a href="/docs/linux/man/8-cups-snmp/">cups-snmp</a></code>(8) for more information.</p>
<h2>Notes</h2>
<p>CUPS printer drivers and backends are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-cups/">cups</a></i>(1), <i><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></i>(5), <i><a href="/docs/linux/man/8-cups-snmp/">cups-snmp</a></i>(8), <i><a href="/docs/linux/man/8-cupsd/">cupsd</a></i>(8), <i><a href="/docs/linux/man/7-filter/">filter</a></i>(7), <i><a href="/docs/linux/man/1-lp/">lp</a></i>(1), <i><a href="/docs/linux/man/8-lpinfo/">lpinfo</a></i>(8), <i><a href="/docs/linux/man/1-lpr/">lpr</a></i>(1),<br />
 CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
