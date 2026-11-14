---
title: "grid-proxy-info(1)"
name: "grid-proxy-info"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-proxy-info/"
description: "grid-proxy-info – Display information about a proxy certificate"
---

<h2 class="name">NAME</h2>
<p> grid-proxy-info &#8211; Display information about a proxy certificate </p>
<h2>SYNOPSIS</h2>
<p> <code>grid-proxy-info</code> -help | -usage | -version </p>
<p> <code>grid-proxy-info</code> -e | -exists [-valid <i>HOURS:MINUTES</i> | -v <i>HOURS:MINUTES</i>] [-hours <i>HOURS</i> | -h <i>HOURS</i>] [-bits <i>BITS</i> | -b <i>BITS</i>] </p>
<p> <code>grid-proxy-info</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>grid-proxy-info</code> program extracts information from an X.509 proxy certificates, and optionally displays or returns an exit code based on that information. </p>
<p> The default mode of operation is to print the following facts about the current user&#8217;s default proxy: subject, issuer, identity, type, strength, path, and time left. If the command-line option <i>-exists</i> or <i>-e</i> is included in the command-line, nothing is printed unless one of the print options is specified. Instead, <code>grid-proxy-info</code> determines if a valid proxy exists and, if so, exits with the exit code 0; if a proxy does not exist or is not valid, <code>grid-proxy-info</code> exits with the exit code 1. Additional validity criteria can be added by using the <i>-valid</i>, <i>-v</i>, <i>-hours</i>, <i>-h</i>, <i>-bits</i>, or <i>-b</i> command-line options. If used, these options must occur <code>after</code> the <i>-e</i> or <i>-exists</i> command-line options. Those options are only valid if one of the <i>-e</i> or <i>-exists</i> command-line options is used.</p>
<h2>OPTIONS</h2>
<p> The complete set of command-line options to <code>grid-proxy-info</code> are: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Display the command-line options to <code>grid-proxy-info</code>.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the version number of the <code>grid-proxy-info</code> command.</dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Display verbose error messages.</dl>
<p> <code>-file </code><i>PROXYFILE</i><code>, -f </code><i>PROXYFILE</i></p>
<dl>
<dt>
<dd> Read the proxy located in the file <i>PROXYFILE</i> instead of using the default proxy.</dl>
<p> <code>-subject, -s</code></p>
<dl>
<dt>
<dd> Display the proxy certificate&#8217;s subject distinguished name.</dl>
<p> <code>-issuer, -i</code></p>
<dl>
<dt>
<dd> Display the proxy certificate issuer&#8217;s distinguished name.</dl>
<p> <code>-identity</code></p>
<dl>
<dt>
<dd> Display the proxy certificate&#8217;s identity. For non-independent proxies, the identity is the subject of the certificate which issued the first proxy in the proxy chain.</dl>
<p> <code>-type</code></p>
<dl>
<dt>
<dd> Display the type of proxy certificate. The type string includes the format (&quot;legacy&quot;, &quot;draft&quot;, or RFC 3280 compliant), identity type (&quot;impersonation&quot; or &quot;independent&quot;), and policy (&quot;limited&quot; or &quot;full&quot;). See <code><a href="/docs/linux/man/1-grid-proxy-init/">grid-proxy-init</a>(1)</code> for information about how to create different types of proxies.</dl>
<p> <code>-timeleft</code></p>
<dl>
<dt>
<dd> Display the number of seconds remaining until the proxy certificate expires.</dl>
<p> <code>-strength</code></p>
<dl>
<dt>
<dd> Display the strength (in bits) of the key associated with the proxy certificate.</dl>
<p> <code>-all</code></p>
<dl>
<dt>
<dd> Display the default information for the proxy when also using the <i>-e</i> or <i>-exists</i> command-line option.</dl>
<p> <code>-text</code></p>
<dl>
<dt>
<dd> Display the proxy certificate contents to standard output, including policy information, issuer, public key, and modulus.</dl>
<p> <code>-path</code></p>
<dl>
<dt>
<dd> Display the path to the file containing the default proxy certificate.</dl>
<p> <code>-rfc2253</code></p>
<dl>
<dt>
<dd> Display distinguished names for the subject, issuer, and identity using the string representation described in RFC 2253, instead of the legacy format.</dl>
<p> <code>-exists, -e</code></p>
<dl>
<dt>
<dd> Perform an existence and validity check for the proxy. If a valid proxy exists and matches the criteria described by other command-line options (if any), exit with 0; otherwise, exit with 1. This option must be before other validity check predicate in the command-line options. If this option is specified, the output of the default facts about the proxy is disabled. Use the <i>-all</i> option to have the information displayed as well as the exit code set.</dl>
<p> <code>-valid </code><i>HOURS:MINUTES</i><code>, -v </code><i>HOURS:MINUTES</i><code>, -hours </code><i>HOURS</i><code>, -h </code><i>HOURS</i></p>
<dl>
<dt>
<dd> Check that the proxy certificate is valid for at least <i>HOURS</i> hours and <i>MINUTES</i> minutes. If it is not, <code>grid-proxy-info</code> will exit with exit code 1.</dl>
<p> <code>-bits </code><i>BITS</i><code>, -b </code><i>BITS</i></p>
<dl>
<dt>
<dd> Check that the proxy certificate key strength is at least <i>BITS</i> bits.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>grid-proxy-info</code>: </p>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dt>
<dd> Path to the default user proxy.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grid-proxy-init/">grid-proxy-init</a>(1), <a href="/docs/linux/man/1-grid-proxy-destroy/">grid-proxy-destroy</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
