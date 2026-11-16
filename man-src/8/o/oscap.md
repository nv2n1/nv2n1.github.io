---
title: "oscap(8)"
name: "oscap"
section: "8"
letter: "o"
url: "/docs/linux/man/8-oscap/"
description: "oscap – OpenSCAP command line tool"
---

<p>oscap &#8211; OpenSCAP command line tool</p>
<h2>Synopsis</h2>
<p><code>oscap</code> [<i>general-options</i>] <code>module</code> operation [<i>operation-options-and-arguments</i>] </p>
<h2>Description</h2>
<p><code>oscap</code> is Security Content Automation Protocol (SCAP) toolkit based on OpenSCAP library. It provides various functions for different SCAP specifications (modules). OpenSCAP tool claims to provide capabilities of Authenticated Configuration Scanner and Authenticated Vulnerability Scanner as defined by The National Institute of Standards and Technology. </p>
<h2>General Options</h2>
<dl>
<dt><code>-V, &#8211;version</code></dt>
<dd>Print supported SCAP specification, location of schema files, schematron files, CPE files, probes and supported OVAL objects. Displays a list of inbuilt CPE names.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Help screen. </dd>
</dl>
<h2>Modules</h2>
<dl>
<dt><code>info</code></dt>
<dd>Determine type and print information about a file.</dd>
<dt><code>xccdf</code></dt>
<dd>The eXtensible Configuration Checklist Description Format.</dd>
<dt><code>oval</code></dt>
<dd>Open Vulnerability and Assessment Language.</dd>
<dt><code>ds</code></dt>
<dd>SCAP Data Stream</dd>
<dt><code>cpe</code></dt>
<dd>Common Platform Enumeration.</dd>
<dt><code>cvss</code></dt>
<dd>Common Vulnerability Scoring System</dd>
<dt><code>cve</code></dt>
<dd>Common Vulnerabilities and Exposures </dd>
</dl>
<h2>Info Operations</h2>
<dl>
<dt>any-scap-file.xml</dt>
<dd>
</dd><dl>
<dd>This module prints information about SCAP content in a file specified on a command line. It determines SCAP content type, specification version, date of creation, date of import and so on. Info module doesn&#8217;t require any additional opperation switch. </dd>
<p> For XCCDF or Datastream files, info module prints out IDs of incorporated profiles, components, and datastreams. These IDs can be used to specify the target for evaluation. Use options &#8211;profile, &#8211;xccdf-id (or &#8211;oval-id), and &#8211;datastream-id respectively.</dl>
</dl>
<h2>Xccdf Operations</h2>
<dl>
<dt><code>eval</code> [<i>options</i>] INPUT_FILE [<i>oval-definitions-files</i>]</dt>
<dd>
</dd><dl>
<dd>Perform evaluation of XCCDF document file given as INPUT_FILE. Print result of each rule to standard output, including rule title, rule id and security identifier(CVE, CCE). Optionally you can give a source datastream as the INPUT_FILE instead of an XCCDF file (see &#8211;datastream-id). </dd>
<p> oscap returns 0 if all rules pass. If there is an error during evaluation, the return code is 1. If there is at least one rule with either fail or unknown result, oscap-scan finishes with return code 2. </p>
<p> Unless &#8211;skip-valid is used, the INPUT_FILE is validated using XSD schemas (depending on document type of INPUT_FILE) and rejected if invalid. </p>
<p> You may specify OVAL Definition files as the last parameter, XCCDF evaluation will then proceed only with those specified files. Otherwise, when <i>oval-definitions-files</i> parameter is missing, oscap tool will try to load all OVAL Definition files referenced from XCCDF automatically (search in the same path as XCCDF). </p>
<dl>
<dt><code>&#8211;profile PROFILE</code></dt>
<dd>
</dd><dl>
<dd>Select a particular profile from XCCDF document.</dd></dl>
<dt><code>&#8211;tailoring-file TAILORING_FILE</code></dt>
<dd>
</dd><dl>
<dd>Use given file for XCCDF tailoring. If both &#8211;tailoring-file and &#8211;tailoring-id are specified, &#8211;tailoring-file takes priority!</dd></dl>
<dt><code>&#8211;tailoring-id COMPONENT_ID</code></dt>
<dd>
</dd><dl>
<dd>Use component of given ID (in input source datastream) for XCCDF tailoring. If both &#8211;tailoring-file and &#8211;tailoring-id are specified, &#8211;tailoring files takes priority!</dd></dl>
<dt><code>&#8211;cpe CPE_FILE</code></dt>
<dd>
</dd><dl>
<dd>Use given CPE dictionary or language (auto-detected) for applicability checks. (Some CPE names are provided by openscap, see oscap &#8211;version for Inbuilt CPE names)</dd></dl>
<dt><code>&#8211;results FILE</code></dt>
<dd>
</dd><dl>
<dd>Write XCCDF results into FILE.</dd></dl>
<dt><code>&#8211;results-arf FILE</code></dt>
<dd>
</dd><dl>
<dd>Writes results to a given FILE in Asset Reporting Format. It is recommended to use this option instead of &#8211;results when dealing with datastreams.</dd></dl>
<dt><code>&#8211;report FILE</code></dt>
<dd>
</dd><dl>
<dd>Write HTML report into FILE. You also have to specify &#8211;results for this feature to work. Please see &#8211;oval-results to enable additional information in the report.</dd></dl>
<dt><code>&#8211;oval-results</code></dt>
<dd>
</dd><dl>
<dd>Generate OVAL Result file for each OVAL session used for evaluation. File with name &#8216;<i>original-oval-definitions-filename</i>.result.xml&#8217; will be generated for each referenced OVAL file in current working directory. This option (in conjunction with the <code>&#8211;report</code> option) also enables inclusion of additional OVAL information in the XCCDF report. To change the directory where OVAL files are generated change the CWD using the `cd` command.</dd></dl>
<dt><code>&#8211;check-engine-results</code></dt>
<dd>
</dd><dl>
<dd>After evaluation is finished, each loaded check engine plugin is asked to export its results. The export itself is plugin specific, please refer to documentation of the plugin for more details.</dd></dl>
<dt><code>&#8211;export-variables</code></dt>
<dd>
</dd><dl>
<dd>Generate OVAL Variables documents which contain external variables&#8217; values that were provided to the OVAL checking engine during evaluation. The filename format is &#8216;<i>original-oval-definitions-filename</i>&#8211;<i>session-index</i>.variables-<i>variables-index</i>.xml&#8217;.</dd></dl>
<dt><code>&#8211;datastream-id ID</code></dt>
<dd>
</dd><dl>
<dd>Uses a datastream with that particular ID from the given datastream collection. If not given the first datastream is used. Only applies if you give source datastream in place of an XCCDF file.</dd></dl>
<dt><code>&#8211;xccdf-id ID</code></dt>
<dd>
</dd><dl>
<dd>Takes component ref with given ID from checklists. This allows to select a particular XCCDF component even in cases where there are 2 XCCDFs in one datastream. If none is given, the first component from the checklists element is used.</dd></dl>
<dt><code>&#8211;benchmark-id ID</code></dt>
<dd>
</dd><dl>
<dd>Selects a component ref from any datastream that references a component with XCCDF Benchmark such that its @id attribute matches given string exactly. Please note that this is not the recommended way of selecting a component-ref. You are advised to use &#8211;xccdf-id AND/OR &#8211;datastream-id for more precision. &#8211;benchmark-id is only used when both &#8211;xccdf-id and &#8211;datastream-id are not present on the command line!</dd></dl>
<dt><code>&#8211;skip-valid</code></dt>
<dd>
</dd><dl>
<dd>Do not validate input/output files.</dd></dl>
<dt><code>&#8211;fetch-remote-resources</code></dt>
<dd>
</dd><dl>
<dd>Allow download of remote OVAL content referenced from XCCDF by check-content-ref/@href.</dd></dl>
<dt><code>&#8211;remediate</code></dt>
<dd>
</dd><dl>
<dd>Execute XCCDF remediation in the process of XCCDF evaluation. This option automatically executes content of XCCDF fix elements for failed rules, and thus this shall be avoided unless for trusted content. Use of this option is always at your own risk.</dd></dl>
<dt><code>&#8211;verbose VERBOSITY_LEVEL</code></dt>
<dd>
</dd><dl>
<dd>Turn on verbose mode at specified verbosity level. VERBOSITY_LEVEL is one of: DEVEL, INFO, WARNING, ERROR.</dd></dl>
<dt><code>&#8211;verbose-log-file FILE</code></dt>
<dd>
</dd><dl>
<dd>Set filename to write additional information.</dd></dl>
</dl>
</dl>
<dt><code>remediate</code> [<i>options</i>] INPUT_FILE [<i>oval-definitions-files</i>]</dt>
<dd>
</dd><dl>
<dd>This module provides post-scan remediation. It assumes that the INPUT_FILE is result of `oscap xccdf eval` operation. The input file must contain TestResult element. This module executes XCCDF fix elements for failed rule-result contained in the given TestResult. Use of this option is always at your own risk and it shall be avoided unless for trusted content.</dd>
<dl>
<dt><code>&#8211;result-id ID</dt>
<dd>
</dd><dl>
<dd>ID of the XCCDF TestResult element which shall be remedied. If this option is missing the last TestResult (in top-down processing) will be remedied.</dd></dl>
<dt>&#8211;skip-valid</code></dt>
<dd>
</dd><dl>
<dd>Do not validate input/output files.</dd></dl>
<dt><code>&#8211;fetch-remote-resources</code></dt>
<dd>
</dd><dl>
<dd>Allow download of remote OVAL content referenced from XCCDF by check-content-ref/@href.</dd></dl>
<dt><code>&#8211;cpe CPE_FILE</code></dt>
<dd>
</dd><dl>
<dd>Use given CPE dictionary or language (auto-detected) for applicability checks.</dd></dl>
<dt><code>&#8211;results FILE</code></dt>
<dd>
</dd><dl>
<dd>Write XCCDF results into FILE.</dd></dl>
<dt><code>&#8211;results-arf FILE</code></dt>
<dd>
</dd><dl>
<dd>Writes results to a given FILE in Asset Reporting Format. It is recommended to use this option instead of &#8211;results when dealing with datastreams.</dd></dl>
<dt><code>&#8211;report FILE</code></dt>
<dd>
</dd><dl>
<dd>Write HTML report into FILE. You also have to specify &#8211;results for this feature to work.</dd></dl>
<dt><code>&#8211;oval-results</code></dt>
<dd>
</dd><dl>
<dd>Generate OVAL Result file for each OVAL session used for evaluation. File with name &#8216;<i>original-oval-definitions-filename</i>.result.xml&#8217; will be generated for each referenced OVAL file. This option (with conjunction with the <code>&#8211;report</code> option) also enables inclusion of additional OVAL information in the XCCDF report.</dd></dl>
<dt><code>&#8211;check-engine-results</code></dt>
<dd>
</dd><dl>
<dd>After evaluation is finished, each loaded check engine plugin is asked to export its results. The export itself is plugin specific, please refer to documentation of the plugin for more details.</dd></dl>
<dt><code>&#8211;export-variables</code></dt>
<dd>
</dd><dl>
<dd>Generate OVAL Variables documents which contain external variables&#8217; values that were provided to the OVAL checking engine during evaluation. The filename format is &#8216;<i>original-oval-definitions-filename</i>&#8211;<i>session-index</i>.variables-<i>variables-index</i>.xml&#8217;.</dd></dl>
</dl>
</dl>
<dt><code>resolve</code> -o output-file xccdf-file</dt>
<dd>
</dd><dl>
<dd>Resolve an XCCDF file as described in the XCCDF specification. It will flatten inheritance hierarchy of XCCDF profiles, groups, rules, and values. Result is another XCCDF document, which will be written to <i>output-file</i>.</dd>
<dl>
<dt><code>&#8211;force</code></dt>
<dd>Force resolving XCCDF document even if it is already marked as resolved.</dd></dl>
</dl>
<dt><code>validate</code> [<i>options</i>] xccdf-file</dt>
<dd>
</dd><dl>
<dd>Validate given XCCDF file against a XML schema. Every found error is printed to the standard error. Return code is 0 if validation succeeds, 1 if validation could not be performed due to some error, 2 if the XCCDF document is not valid.</dd>
<dl>
<dt><code>&#8211;schematron</code></dt>
<dd>Turn on Schematron-based validation. It is able to find more errors and inconsistencies but is much slower. Schematron is available only for XCCDF version 1.2.</dd></dl>
</dl>
<dt><code>export-oval-variables</code> [<i>options</i>] xccdf-file [<i>oval-definitions-files</i>]</dt>
<dd>
</dd><dl>
<dd>Collect all the XCCDF values that would be used by OVAL during evaluation of a certain profile and export them as OVAL external-variables document(s). The filename format is &#8216;<i>original-oval-definitions-filename</i>&#8211;<i>session-index</i>.variables-<i>variables-index</i>.xml&#8217;. </dd>
<dl>
<dt><code>&#8211;profile PROFILE</code></dt>
<dd>
</dd><dl>
<dd>Select a particular profile from XCCDF document.</dd></dl>
<dt><code>&#8211;fetch-remote-resources</code></dt>
<dd>
</dd><dl>
<dd>Allow download of remote OVAL content referenced from XCCDF by check-content-ref/@href.</dd></dl>
<dt><code>&#8211;skip-valid</code></dt>
<dd>
</dd><dl>
<dd>Do not validate input/output files.</dd></dl>
<dt><code>&#8211;datastream-id ID</code></dt>
<dd>
</dd><dl>
<dd>Uses a datastream with that particular ID from the given datastream collection. If not given the first datastream is used. Only applies if you give source datastream in place of an XCCDF file.</dd></dl>
<dt><code>&#8211;xccdf-id ID</code></dt>
<dd>
</dd><dl>
<dd>Takes component ref with given ID from checklists. This allows to select a particular XCCDF component even in cases where there are 2 XCCDFs in one datastream.</dd></dl>
<dt><code>&#8211;cpe CPE_FILE</code></dt>
<dd>
</dd><dl>
<dd>Use given CPE dictionary or language (auto-detected) for applicability checks. The variables documents are created only for xccdf:Rules which are applicable.</dd></dl>
</dl>
</dl>
<dt><code>generate</code> [<i>options</i>] &lt;submodule&gt; [submodule-specific-options]</dt>
<dd>
</dd><dl>
<dd>Generate another document form an XCCDF file such as security guide or result report.</dd>
<dl>
<dt><code>&#8211;profile ID</code></dt>
<dd>Apply profile with given ID to the Benchmark before further processing takes place.</dd>
<dt>Available submodules:</dt>
<dd>
</dd><dt><code>guide</code> [<i>options</i>] xccdf-file</dt>
<dd>
</dd><dl>
<dd>Generate a formatted document containing a security guide from a XCCDF Benchmark. Unless the &#8211;output option is specified it will be written to the standard output. Without profile being set only groups (not rules) will be included in the output.</dd>
<dl>
<dt><code>&#8211;output FILE</code></dt>
<dd>Write the guide to this file instead of standard output.</dd>
<dt><code>&#8211;hide-profile-info</code></dt>
<dd>Information on chosen profile (e.g. rules selected by the profile) will be excluded from the document.</dd></dl>
</dl>
<dt><code>report</code> [<i>options</i>] xccdf-file</dt>
<dd>
</dd><dl>
<dd>Generate a document containing results of a XCCDF Benchmark execution. Unless the &#8211;output option is specified it will be written to the standard output. ID of the TestResult element to visualise defaults to the most recent result (according to the end-time attribute).</dd>
<dl>
<dt><code>&#8211;output FILE</code></dt>
<dd>Write the report to this file instead of standard output.</dd>
<dt><code>&#8211;result-id ID</code></dt>
<dd>ID of the XCCDF TestResult from which the report will be generated.</dd>
<dt><code>&#8211;show </code><i>what</i></dt>
<dd>Specify what result types shall be displayed in the result report. The default is to show everything except for rules with results notselected and notapplicable. The <i>what</i> part is a comma-separated list of result types to display in addition to the default. If result type is prefixed by a dash &#8216;-&#8216;, it will be excluded from the results. If <i>what</i> is prefixed by an equality sign &#8216;=&#8217;, a following list specifies exactly what rule types to include in the report. Result types are: pass, fixed, notchecked, notapplicable, notselected, informational, unknown, error, fail.</dd>
<dt><code>&#8211;oval-template </code><i>template-string</i></dt>
<dd>To use the ability to include additional information from OVAL in xccdf result file, a template which will be used to obtain OVAL result file names has to be specified. The template can be either a filename or a string containing wildcard character (percent sign &#8216;%&#8217;). Wildcard will be replaced by the original OVAL definition file name as referenced from the XCCDF file. This way it is possible to obtain OVAL information even from XCCDF documents referencing several OVAL files. To use this option with results from an XCCDF evaluation, specify <i>%.result.xml</i> as a OVAL file name template.</dd>
<dt><code>&#8211;sce-template </code><i>template-string</i></dt>
<dd>To use the ability to include additional information from SCE in XCCDF result file, a template which will be used to obtain SCE result file names has to be specified. The template can be either a filename or a string containing wildcard character (percent sign &#8216;%&#8217;). Wildcard will be replaced by the original SCE script file name as referenced from the XCCDF file. This way it is possible to obtain SCE information even from XCCDF documents referencing several SCE files. To use this option with results from an XCCDF evaluation, specify <i>%.result.xml</i> as a SCE file name template.</dd></dl>
</dl>
<dt><code>fix</code> [<i>options</i>] xccdf-file</dt>
<dd>
</dd><dl>
<dd>Generate a script that shall bring the system to a state of compliance with given XCCDF Benchmark.</dd>
<dl>
<dt><code>&#8211;output FILE</code></dt>
<dd>Write the report to this file instead of standard output.</dd>
<dt><code>&#8211;result-id </code><i>ID</i></dt>
<dd>Fixes will be generated for failed rule-results of the specified TestResult.</dd>
<dt><code>&#8211;template </code><i>ID|FILE</i></dt>
<dd>Template to be used to generate the script. If it contains a dot &#8216;.&#8217; it is interpreted as a location of a file with the template definition. Otherwise it identifies a template from standard set which currently includes: <i>bash</i> (default if no &#8211;template switch present). Brief explanation of the process of writing your own templates is in the XSL file <i>xsl/legacy-fix.xsl</i> in the openscap data directory. You can also take a look at the default template <i>xsl/legacy-fixtpl-bash.xml</i>.</dd></dl>
</dl>
<dt><code>custom</code> &#8211;stylesheet xslt-file [<i>options</i>] xccdf-file</dt>
<dd>
</dd><dl>
<dd>Generate a custom output (depending on given XSLT file) from an XCCDF file.</dd>
<dl>
<dt><code>&#8211;stylesheet </code><i>FILE</i></dt>
<dd>Specify an absolute path to a custom stylesheet to format the output.</dd>
<dt><code>&#8211;output FILE</code></dt>
<dd>&nbsp;<wbr>Write the document into file.</dd></dl>
</dl>
</dl>
</dl>
</dl>
<h2>Oval Operations</h2>
<dl>
<dt><code>eval</code> [<i>options</i>] INPUT_FILE</dt>
<dd>
</dd><dl>
<dd>Probe the system and evaluate all definitions from OVAL Definition file. Print result of each definition to standard output. The return code is 0 after a successful evaluation. On error, value 1 is returned. </dd>
<p> INPUT_FILE can be either OVAL Definition File or SCAP Source Datastream, it depends on used options. </p>
<p> Unless &#8211;skip-valid is used, the INPUT_FILE is validated using XSD schemas (depending on document type of INPUT_FILE) and rejected if invalid.</p>
<dl>
<dt><code>&#8211;id DEFINITION-ID</code></dt>
<dd>Evaluate ONLY specified OVAL Definition from OVAL Definition File.</dd>
<dt><code>&#8211;variables FILE</code></dt>
<dd>Provide external variables expected by OVAL Definition File.</dd>
<dt><code>&#8211;directives FILE</code></dt>
<dd>Use OVAL Directives content to specify desired results content.</dd>
<dt><code>&#8211;results FILE</code></dt>
<dd>Write OVAL Results into file.</dd>
<dt><code>&#8211;report FILE</code></dt>
<dd>Create human readable (HTML) report from OVAL Results.</dd>
<dt><code>&#8211;datastream-id ID</code></dt>
<dd>
</dd><dl>
<dd>Uses a datastream with that particular ID from the given datastream collection. If not given the first datastream is used. Only applies if you give source datastream in place of an OVAL file.</dd></dl>
<dt><code>&#8211;oval-id ID</code></dt>
<dd>
</dd><dl>
<dd>Takes component ref with given ID from checks. This allows to select a particular OVAL component even in cases where there are 2 OVALs in one datastream.</dd></dl>
<dt><code>&#8211;skip-valid</code></dt>
<dd>Do not validate input/output files.</dd>
<dt><code>&#8211;verbose VERBOSITY_LEVEL</code></dt>
<dd>Turn on verbose mode at specified verbosity level. VERBOSITY_LEVEL is one of: DEVEL, INFO, WARNING, ERROR.</dd>
<dt><code>&#8211;verbose-log-file FILE</code></dt>
<dd>Set filename to write additional information.</dd></dl>
</dl>
<dt><code>collect</code> [<i>options</i>] definitions-file</dt>
<dd>
</dd><dl>
<dd>Probe the system and gather system characteristics for all objects in OVAL Definition file. </dd>
<dl>
<dt><code>&#8211;id OBJECT-ID</code></dt>
<dd>Collect system characteristics ONLY for specified OVAL Object.</dd>
<dt><code>&#8211;variables FILE</code></dt>
<dd>Provide external variables expected by OVAL Definitions.</dd>
<dt><code>&#8211;syschar FILE</code></dt>
<dd>Write OVAL System Characteristic into file.</dd>
<dt><code>&#8211;skip-valid</code></dt>
<dd>Do not validate input/output files.</dd>
<dt><code>&#8211;verbose VERBOSITY_LEVEL</code></dt>
<dd>Turn on verbose mode at specified verbosity level. VERBOSITY_LEVEL is one of: DEVEL, INFO, WARNING, ERROR.</dd>
<dt><code>&#8211;verbose-log-file FILE</code></dt>
<dd>Set filename to write additional information.</dd></dl>
</dl>
<dt><code>analyse</code> [<i>options</i>] &#8211;results FILE definitions-file syschar-file</dt>
<dd>
</dd><dl>
<dd>In this mode, the oscap tool does not perform data collection on the local system, but relies upon the input file, which may have been generated on another system. The output (OVAL Results) is printed to file specified by <code>&#8211;results</code> parameter.</dd>
<dl>
<dt><code>&#8211;variables FILE</code></dt>
<dd>Provide external variables expected by OVAL Definitions.</dd>
<dt><code>&#8211;directives FILE</code></dt>
<dd>Use OVAL Directives content to specify desired results content.</dd>
<dt><code>&#8211;skip-valid</code></dt>
<dd>Do not validate input/output files.</dd>
<dt><code>&#8211;verbose VERBOSITY_LEVEL</code></dt>
<dd>Turn on verbose mode at specified verbosity level. VERBOSITY_LEVEL is one of: DEVEL, INFO, WARNING, ERROR.</dd>
<dt><code>&#8211;verbose-log-file FILE</code></dt>
<dd>Set filename to write additional information.</dd></dl>
</dl>
<dt><code>validate</code> [<i>options</i>] oval-file</dt>
<dd>
</dd><dl>
<dd>Validate given OVAL file against a XML schema. Every found error is printed to the standard error. Return code is 0 if validation succeeds, 1 if validation could not be performed due to some error, 2 if the OVAL document is not valid.</dd>
<dl>
<dt><code>&#8211;definitions</code>, <code>&#8211;variables</code>, <code>&#8211;syschar</code>, <code>&#8211;results</code> <code>&#8211;directives</code></dt>
<dd>Type of the OVAL document is automatically detected by default. If you want enforce certain document type, you can use one of these options.</dd>
<dt><code>&#8211;schematron</code></dt>
<dd>Turn on Schematron-based validation. It is able to find more errors and inconsistencies but is much slower.</dd></dl>
</dl>
<dt><code>generate</code> &lt;submodule&gt; [submodule-specific-options]</dt>
<dd>
</dd><dl>
<dd>Generate another document form an OVAL file.</dd>
<dl>
<dt>Available submodules:</dt>
<dd>
</dd><dt><code>report</code> [<i>options</i>] oval-results-file</dt>
<dd>
</dd><dl>
<dd>Generate a formatted HTML page containing visualisation of an OVAL results file. Unless the &#8211;output option is specified it will be written to the standard output.</dd>
<dl>
<dt><code>&#8211;output FILE</code></dt>
<dd>Write the report to this file instead of standard output.</dd></dl>
</dl>
</dl>
</dl>
<dt><code>list-probes</code> [<i>options</i>]</dt>
<dd>
</dd><dl>
<dd>List supported object types (i.e. probes)</dd>
<dl>
<dt><code>&#8211;static</code></dt>
<dd>List all probes defined in the internal tables.</dd>
<dt><code>&#8211;dynamic</code></dt>
<dd>List all probes supported on the current system (this is default behavior).</dd>
<dt><code>&#8211;verbose</code></dt>
<dd>Be verbose.</dd></dl>
</dl>
</dl>
<h2>Cpe Operations</h2>
<dl>
<dt><code>check</code> name</dt>
<dd>
</dd><dl>
<dd>Check whether name is in correct CPE format.</dd></dl>
</dl>
<p> <code>match</code> name dictionary.xml</p>
<dl>
<dd>Find an exact match of CPE name in the dictionary.</dd></dl>
<p> <code>validate</code> cpe-dict-file</p>
<dl>
<dd>Validate given CPE dictionary file against a XML schema. Every found error is printed to the standard error. Return code is 0 if validation succeeds, 1 if validation could not be performed due to some error, 2 if the XCCDF document is not valid. </dd>
</dl>
<h2>Cvss Operations</h2>
<dl>
<dt><code>score</code> <i>cvss_vector</i></dt>
<dd>
</dd><dl>
<dd>Calculate score from a CVSS vector. Prints base score for base CVSS vector, base and temporal score for temporal CVSS vector, base and temporal and environmental score for environmental CVSS vector.</dd></dl>
<dt><code>describe</code> <i>cvss_vector</i></dt>
<dd>
</dd><dl>
<dd>Describe individual components of a CVSS vector in a human-readable format and print partial scores.</dd></dl>
<dt><i>CVSS vector</i> consists of several slash-separated components specified as key-value pairs. Each key can be specified at most once. Valid CVSS vector has to contain at least base CVSS metrics, i.e. AV, AC, AU, C, I, and A. Following table summarizes the components and possible values (second column is metric category: B for base, T for temporal, E for environmental):</dt>
<dd>
</dd><dl>
<dd>AV:[L|A|N] B Access vector: Local, Adjacent network, Network </dd>
<p> AC:[H|M|L] B Access complexity: High, Medium, Low </p>
<p> AU:[M|S|N] B Required authentication: Multiple instances, Single instance, None </p>
<p> C:[N|P|C] B Confidentiality impact: None, Partial, Complete </p>
<p> I:[N|P|C] B Integrity impact: None, Partial, Complete </p>
<p> A:[N|P|C] B Availability impact: None, Partial, Complete </p>
<p> E:[ND|U|POC|F|H] T Exploitability: Not Defined, Unproven, Proof of Concept, Functional, High </p>
<p> RL:[ND|OF|TF|W|U] T Remediation Level: Not Defined, Official Fix, Temporary Fix, Workaround, Unavailable </p>
<p> RC:[ND|UC|UR|C] T Report Confidence: Not Defined, Unconfirmed, Uncorroborated, Confirmed </p>
<p> CDP:[ND|N|L|LM|MH|H] E Collateral Damage Potential: Not Defined, None, Low, Low-Medium, Medium-High, High </p>
<p> TD:[ND|N|L|M|H] E Target Distribution: Not Defined, None, Low, Medium, High </p>
<p> CR:[ND|L|M|H] E Confidentiality requirement: Not Defined, Low, Medium, High </p>
<p> IR:[ND|L|M|H] E Integrity requirement: Not Defined, Low, Medium, High </p>
<p> AR:[ND|L|M|H] E Availability requirement: Not Defined, Low, Medium, High</dl>
</dl>
<h2>Ds Operations</h2>
<dl>
<dt><code>sds-compose</code> [<i>options</i>] SOURCE_XCCDF TARGET_SDS</dt>
<dd>
</dd><dl>
<dd>Creates a source datastream from the XCCDF file given in SOURCE_XCCDF and stores the result in TARGET_SDS. Dependencies like OVAL files are automatically detected and bundled in target source datastream.</dd>
<dl>
<dt><code>&#8211;skip-valid</dt>
<dd>Do not validate input/output files.</dd></dl>
</dl>
<dt>sds-add</code> [<i>options</i>] NEW_COMPONENT EXISTING_SDS</dt>
<dd>
</dd><dl>
<dd>Adds given NEW_COMPONENT file to the existing source datastream (EXISTING_SDS). Component file might be OVAL, XCCDF or CPE Dictionary file. Dependencies like OVAL files are automatically detected an bundled in target source datastream.</dd>
<dl>
<dt><code>&#8211;datastream-id DATASTREAM_ID</code></dt>
<dd>Uses a datastream with that particular ID from the given datastream collection. If not given the first datastream is used.</dd>
<dt><code>&#8211;skip-valid</dt>
<dd>Do not validate input/output files.</dd></dl>
</dl>
<dt>sds-split</code> [<i>options</i>] SOURCE_DS TARGET_DIR</dt>
<dd>
</dd><dl>
<dd>Splits given source datastream into multiple files and stores all the files in TARGET_DIR.</dd>
<dl>
<dt><code>&#8211;datastream-id DATASTREAM_ID</code></dt>
<dd>Uses a datastream with that particular ID from the given datastream collection. If not given the first datastream is used.</dd>
<dt><code>&#8211;xccdf-id XCCDF_ID</code></dt>
<dd>Takes component ref with given ID from checklists. This allows to select a particular XCCDF component even in cases where there are 2 XCCDFs in one datastream.</dd>
<dt><code>&#8211;skip-valid</dt>
<dd>Do not validate input/output files.</dd></dl>
</dl>
<dt>sds-validate</code> SOURCE_DS</dt>
<dd>
</dd><dl>
<dd>Validate given source datastream file against a XML schema. Every found error is printed to the standard error. Return code is 0 if validation succeeds, 1 if validation could not be performed due to some error, 2 if the source datastream is not valid.</dd></dl>
<dt><code>rds-create</code> [<i>options</i>] SDS TARGET_ARF XCCDF_RESULTS [OVAL_RESULTS [OVAL_RESULTS ..]]</dt>
<dd>
</dd><dl>
<dd>Takes given source datastream, XCCDF and OVAL results and creates a result datastream (in Asset Reporting Format) and saves it to file given in TARGET_ARF.</dd>
<dl>
<dt><code>&#8211;skip-valid</dt>
<dd>Do not validate input/output files.</dd></dl>
</dl>
<dt>rds-split</code> [<i>options</i>] [&#8211;report-id REPORT_ID] RDS TARGET_DIR</dt>
<dd>
</dd><dl>
<dd>Takes given result datastream (also called ARF = asset reporting format) and splits given report and its respective report-request to given target directory. If no report-id is given, we assume user wants the first applicable report in top-down order in the file.</dd>
<dl>
<dt><code>&#8211;skip-valid</dt>
<dd>Do not validate input/output files.</dd></dl>
</dl>
<dt>rds-validate</code> SOURCE_RDS</dt>
<dd>
</dd><dl>
<dd>Validate given result datastream file against a XML schema. Every found error is printed to the standard error. Return code is 0 if validation succeeds, 1 if validation could not be performed due to some error, 2 if the result datastream is not valid.</dd></dl>
</dl>
<h2>Cve Operations</h2>
<dl>
<dt><code>validate</code> cve-nvd-feed.xml</dt>
<dd>
</dd><dl>
<dd>Validate given CVE data feed.</dd></dl>
<dt><code>find</code> CVE cve-nvd-feed.xml</dt>
<dd>
</dd><dl>
<dd>Find given CVE in data feed and report base score, vector string and vulnerable software list.</dd></dl>
</dl>
<h2>Exit Status</h2>
<dl>
<dt><code>Normally, the exit status is 0 when operation finished successfully and 1 otherwise. In cases when oscap performs evaluation of the system it may return 2 indicating success of the operation but incompliance of the assessed system.</dt>
<dd></dd></dl>
<p> </code></p>
<h2>Examples</h2>
<p>Evaluate XCCDF content using CPE dictionary and produce html report. In this case we use United States Government Configuration Baseline (USGCB) for Red Hat Enterprise Linux 5 Desktop. </p>
<pre><dl><dt></dt><dd>oscap xccdf eval --fetch-remote-resources --oval-results \
 --profile united_states_government_configuration_baseline \
 --report usgcb-rhel5desktop.report.html \
 --results usgcb-rhel5desktop-xccdf.xml.result.xml \
 --cpe usgcb-rhel5desktop-cpe-dictionary.xml \
 usgcb-rhel5desktop-xccdf.xml
</dd></dl></pre>
<h2>Content</h2>
<dl>
<dt><code> National Vulnerability Database</code> &#8211; <i><a rel="nofollow" href="http://web.nvd.nist.gov/view/ncp/repository">http://web.nvd.nist.gov/view/ncp/repository</a></i></dt>
<dd>
</dd><dt><code> Red Hat content repository</code> &#8211; <i><a rel="nofollow" href="http://www.redhat.com/security/data/oval/">http://www.redhat.com/security/data/oval/</a></i></dt>
<dd></dd></dl>
<h2>Reporting Bugs</h2>
<pre>Please report bugs using <a rel="nofollow" href="https://github.com/OpenSCAP/openscap/issues">https://github.com/OpenSCAP/openscap/issues</a>
Make sure you include the full output of `oscap --v` in the bug report.</pre>
<h2>Authors</h2>
<pre>Peter Vrabec &lt;pvrabec [at] redhat.com&gt;
Šimon Lukašík
Martin Preisler &lt;mpreisle [at] redhat.com&gt;</pre>
