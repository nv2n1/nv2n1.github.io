---
title: "arcemiestest(1)"
name: "arcemiestest"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcemiestest/"
description: "arcemiestest – perform simple operations on EMI ES service"
---

<h2 class="name">NAME</h2>
<p> arcemiestest &#8211; perform simple operations on EMI ES service</p>
<h2>DESCRIPTION</h2>
<p> The <code>arcemiestest</code> command performs simple operations on server with EMI Execution Service (ES) interface and is meant for testing interoperability of ARC EMI ES client implementation and corresponding service. Please see description of EMI ES at <code><a rel="nofollow" href="http://twiki.cern.ch/twiki/bin/view/EMI/EmiExecutionService">http://twiki.cern.ch/twiki/bin/view/EMI/EmiExecutionService</a> </code> for detailed information about functionality of the service. </p>
<h2>SYNOPSIS</h2>
<p> <code>arcemiestest command URL [arguments]</code> </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>sstat URL</code></p>
<dd> takes URL of service implementing ResourceInfo capability, retrieves service description</p>
<dt><code>submit URL filename</code></p>
<dd> takes URL of service implementing ActivityCreation capability and file containing ADL activity description, sublits activity to service</p>
<dt><code>stat URL ID</code></p>
<dd> takes URL of service implementing ActivityManagement capability and identifier of activity as returned by submit command, retireves state of activity</p>
<dt><code>info</code></p>
<dd> takes URL of service implementing ActivityManagement capability and identifier of activity as returned by submit command, retirieves extended description of the activity</p>
<dt><code>clean</code></p>
<dd> takes URL of service implementing ActivityManagement capability and identifier of activity as returned by submit command, removes the activity from the service</p>
<dt><code>kill</code></p>
<dd> takes URL of service implementing ActivityManagement capability and identifier of activity as returned by submit command, cancels execution of the activity at the service</p>
<dt><code>list</code></p>
<dd> takes URL of service implementing ActivityInfo capability, retrieves identifiers of available activities</p>
<dt><code>ivalidate</code></p>
<dd> takes URL of service implementing ResourceInfo capability, retrieves full and partial service descriptions and validates results. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>$(ARC_LOCATION)/share/arc/schema/GLUE2.xsd</code></p>
<dd> The schema of GLUE2 service description is used to validate response from service. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>X509_USER_PROXY</code></p>
<dd> The location of the user&#8217;s Grid proxy file. Shouldn&#8217;t be set unless the proxy is in a non-standard location. </p>
<dt><code>ARC_LOCATION</code></p>
<dd> The location where ARC is installed can be specified by this variable. If not specified the install location will be determined from the path to the command being executed, and if this fails a WARNING will be given stating the location which will be used. </p>
</dl>
<h2>EXAMPLE</h2>
<p> arcemiestest ivalidate <a rel="nofollow" href="https://testbed.eu-emi.eu/emies">https://testbed.eu-emi.eu/emies</a> </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arcproxy/">arcproxy</a></code>(1), <code><a href="/docs/linux/man/1-arcinfo/">arcinfo</a></code>(1), <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1), <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1) </p>
<h2>Index</h2>
