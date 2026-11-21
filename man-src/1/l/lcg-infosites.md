---

title: "lcg-infosites(1)"
name: "lcg-infosites"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lcg-infosites/"
description: "lcg-infosites – list grid service information matching given criteria"
---

<h2>NAME</h2>
<p> lcg-infosites &#8211; list grid service information matching given criteria</p>
<p> <code>lcg-infosites</code> [<i>options</i>] <i>selection(s)</i> </p>
<p> <code>lcg-infosites</code> provides a user-friendly way to query the EGI/WLCG information system for services that match given criteria. The supported options and selections are detailed below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f </code><i>site_name</i></dt>
<dd> Restrict the listed service information to the given site.</dd>
<dt><code>-h | &#8211;help</code></dt>
<dd> Display a usage reminder and exit.</dd>
<dt><code>&#8211;is</code> <i>BDII_host</i>[<i>:port</i>]</dt>
<dd> Indicate the BDII to be used. By default the BDII(s) in $LCG_GFAL_INFOSYS will be tried.</dd>
<dt><code>&#8211;trust</code> <i>host</i></dt>
<dd> For the &#8216;<code>myproxy</code>&#8216; selection only list MyProxy servers that trust the given host for renewing proxies.</dd>
<dt><code>-v</code> {<i>1</i> | <i>2</i> | <i>3</i> | <i>4</i>}</dt>
<dd> Change the output verbosity for certain selections (see below).</dd>
<dt><code>-V | &#8211;version</code></dt>
<dd> Output version information and exit.</dd>
<dt><code>&#8211;vo</code> <i>VO</i></dt>
<dd> Restrict the listed service information to the given VO or VOMS attribute name. By default the VO is determined from the user&#8217;s VOMS proxy, even if it has expired. The wildcard character &#8216;*&#8217; can be used to list service information pertaining to multiple VOs or VOMS attributes.</dd></dl>
<h2>SELECTIONS</h2>
<p> For any listings of service endpoints the corresponding site names are added when the &#8216;<code>-v</code>&#8216; option is supplied with argument &#8216;<code>4</code>&#8216;.</p>
<dl>
<dt><code>all</code></dt>
<dd> Equivalent to selecting &#8216;<code>ce</code>&#8216; and &#8216;<code>se</code>&#8216;.</dd>
<dt><code>bdii_site</code></dt>
<dd> List site BDII endpoints.</dd>
<dt><code>bdii_top</code></dt>
<dd> List top BDII endpoints.</dd>
<dt><code>ce</code></dt>
<dd> If no &#8216;<code>-v</code>&#8216; option is supplied, list matching CE endpoints with their total and free CPU counts and their total, running and waiting job counts. </dd>
<p> If the &#8216;<code>-v</code>&#8216; option is supplied with argument &#8216;<code>1</code>&#8216;, list the matching CE endpoints. </p>
<p> If the &#8216;<code>-v</code>&#8216; option is supplied with argument &#8216;<code>2</code>&#8216;, list the matching GLUE SubClusters with their values for RAM, operating system name and version, and processor type. </p>
<p> If the &#8216;<code>-v</code>&#8216; option is supplied with argument &#8216;<code>3</code>&#8216;, list the matching CE endpoints with their values for RAM, operating system name and release, and processor type. A CE will appear multiple times if it is associated with multiple SubClusters. Note: the WMS currently cannot submit jobs to such a CE, unless <i>all</i> its SubClusters match the job requirements. </p>
<p> If the &#8216;<code>-v</code>&#8216; option is supplied with argument &#8216;<code>4</code>&#8216;, list the matching CE endpoints along with the corresponding site names.</p>
<dt><code>closeSE</code></dt>
<dd> For each matching CE list the matching close SEs. Close SEs that do not match the VO criteria are skipped.</dd>
<dt><code>cream</code></dt>
<dd> List the matching CREAM endpoints.</dd>
<dt><code>dli</code>, <code>dliLocal</code></dt>
<dd> List the Data Location Interface endpoints corresponding to the matching global or local LCG File Catalog endpoints (see below). The DLI is used by the WMS to resolve Logical File Names and files identified by GUIDs.</dd>
<dt><code>fts</code></dt>
<dd> List matching instances of the File Transfer Service.</dd>
<dt><code>gridice</code></dt>
<dd> List matching collector endpoints for GridICE monitoring services.</dd>
<dt><code>lb</code></dt>
<dd> List matching Logging and Bookkeeping endpoints.</dd>
<dt><code>lcg-ce</code></dt>
<dd> List the matching LCG-CE endpoints.</dd>
<dt><code>lfc</code>, <code>lfcLocal</code></dt>
<dd> List the global or local LCG File Catalog endpoints. Each VO can have only a single global LFC at most, but (also) can have multiple local LFC instances.</dd>
<dt><code>myproxy</code></dt>
<dd> List the MyProxy service endpoints. If the &#8216;<i>&#8211;trust</i>&#8216; option is specified, only those endpoints are listed that support the given host as an <i>authorized renewer</i> of proxies. This allows the user to find MyProxy servers that support e.g. a given WMS host.</dd>
<dt><code>se</code></dt>
<dd> If no &#8216;<code>-v</code>&#8216; option is supplied, list matching SE endpoints with their amounts of available and used space (deprecated legacy attributes, in kB) and their types. The type is <i>SRM</i> if the SE supports the Storage Resource Manager interface version 1.1 or 2.2, else <i>xroot</i> if it supports the <i>Xroot(d)</i> interface, else <i>gftp</i> if it supports <i>gsiftp</i> (GridFTP), else &#8216;-&#8216;. See the &#8216;<code>space</code>&#8216; selection for detailed information about SRM spaces. </dd>
<p> If the &#8216;<code>-v</code>&#8216; option is supplied with argument &#8216;<code>1</code>&#8216;, list the matching SE endpoints. </p>
<p> If the &#8216;<code>-v</code>&#8216; option is supplied with argument &#8216;<code>4</code>&#8216; (sic), list the matching SE endpoints along with the corresponding site names.</p>
<dt><code>sitenames</code></dt>
<dd> List the sites.</dd>
<dt><code>space</code></dt>
<dd> For each matching SRM space on the matching SE endpoints list the amounts of free, used and reserved space in GB for online and nearline latencies and, if defined, the tag (space token user description) identifying the space.</dd>
<dt><code>tag</code></dt>
<dd> For each matching CE list the matching software tags published by the CE.</dd>
<dt><code>vobox</code></dt>
<dd> List the matching VOBOX endpoints.</dd>
<dt><code>voms</code></dt>
<dd> List the matching VOMS endpoints.</dd>
<dt><code>voms-admin</code></dt>
<dd> List the matching VOMS-Admin endpoints.</dd>
<dt><code>voview</code></dt>
<dd> If no &#8216;<code>-v</code>&#8216; option is supplied, list matching CE endpoints with their matching VO-specific attributes: the running, waiting and total job counts, the free job slots, the estimated and worst response times, the default SE and the location of the software area. </dd>
<p> If the &#8216;<code>-v</code>&#8216; option is supplied with argument &#8216;<code>1</code>&#8216;, list the matching CE endpoints with a subset of the matching VO-specific attributes: the free job slots and the total, running and waiting job counts. This allows for easier comparison with the output for the &#8216;<code>ce</code>&#8216; selection.</p>
<dt><code>wms</code></dt>
<dd> List the matching Workload Management System endpoints.</dd></dl>
<h2>AUTHOR</h2>
<p> Versions &lt;= 2.6.9 by Patricia Mendez Lorenzo<br />
 Versions &gt;= 3.0.0 by Maarten Litmaath</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs via GGUS (<a rel="nofollow" href="http://ggus.org">http://ggus.org</a>). </p>
