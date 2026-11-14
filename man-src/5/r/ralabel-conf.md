---
title: "ralabel-conf(5)"
name: "ralabel-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-ralabel-conf/"
description: "ralabel.conf – ralabel resource file."
---

<p><code>ralabel.conf</code> &#8211; <code>ralabel</code> resource file.</p>
<h2>Synopsis</h2>
<p><code>ralabel.conf</code></p>
<h2>Description</h2>
<p>This configuration is a <a href="/docs/linux/man/1-ralabel/">ralabel</a>(1) configuration file. The concept is to provide a number of labeling strategies with configuration capabilities for each of the labelers. This allows the user to specify the order of the labeling, which is provided to support hierarchical labeling. Here is a valid and simple configuration file. It doesn&#8217;t do anything in particular, but it is one that is used at some sites. </p>
<h2>Supported Labeling Strategies</h2>
<h2>Addresss Based Classification</h2>
<p>Address based classifications involve building a patricia tree that we can hang labels against. The strategy is to order the address label configuration files, to develop a hierarchical label scheme.</p>
<h2>IANA IPv4 and IPv6 Address Classification Labeling</h2>
<h2>Ralabel_Iana_Address</h2>
<p>The type of IP network address can be used by many analysis programs to make decisions. While IANA standard classifications don&#8217;t change, this type of classification should be extendable to allow local sites to provide additional labeling capabilities. </p>
<pre><code>RALABEL_IANA_ADDRESS</code>=yes
<code>RALABEL_IANA_ADDRESS_FILE</code>=&quot;/usr/local/argus/iana-address-file&quot;</pre>
<h2>Addresss Based Country Code Classification</h2>
<h2>Ralabel_Arin_Country_Codes</h2>
<p>Address based country code classification leverages the feature where ra* clients cant print country codes for the IP addresses that are in a flow record. Country codes are generated from the ARIN delegated address space files. Specify the location of your DELEGATED_IP file here, or in your .rarc file (which is default). </p>
<p> Unlike the GeoIP based country code labeling, these codes can be sorted filtered and aggregated, so if you want to do that type of operations with country codes, enable this feature here. </p>
<pre><code>RALABEL_ARIN_COUNTRY_CODES</code>=yes
<code>RA_DELEGATED_IP</code>=&quot;/usr/local/argus/delegated-ipv4-latest&quot;</pre>
<h2>BIND Based Classification</h2>
<h2>Ralabel_Bind_Name</h2>
<p>BIND services provide address to name translations, and these reverse lookup strategies can provide FQDN labels, or domain labels that can be added to flow. The IP addresses that can be are synonomous and result in labeling all three IP addresses. </p>
<p> Use this strategy to provide transient semantic enhancement based on ip address values. </p>
<pre><code>RALABEL_BIND_NAME</code>=&quot;all&quot;</pre>
<h2>Port Based Classification</h2>
<h2>Ralabel_Iana_Port</h2>
<p>Port based classifications involves simple assignment of a text label to a specific port number. While IANA standard classifications are supported throught the Unix /etc/services file assignments, and the basic &quot;src port&quot; and &quot;dst port&quot; ra* filter schemes, this scheme is used to enhance/modify that labeling strategy. The text associated with a port number is placed in the metadata label field, and is searched using the regular expression searching strategies that are available to label matching. </p>
<p> Use this strategy to provide transient semantic enhancement based on port values. </p>
<pre><code>RALABEL_IANA_PORT</code>=yes
<code>RALABEL_IANA_PORT_FILE</code>=&quot;/usr/local/argus/iana-port-numbers&quot;</pre>
<h2>Flow Filter Based Classification</h2>
<p>Flow filter based classification uses the standard flow filter strategies to provide a general purpose labeling scheme. The concept is similar to racluster()&#8217;s fall through matching scheme. Fall through the list of filters, if it matches, add the label. If you want to continue through the list, once there is a match, add a &quot;cont&quot; to the end of the matching rule.</p>
<h2>Ralabel_Argus_Flow</h2>
<pre><code>RALABEL_ARGUS_FLOW</code>=yes
<code>RALABEL_ARGUS_FLOW_FILE</code>=&quot;/usr/local/argus/argus-flow-file&quot;</pre>
<h2>GeoIP Based Labeling</h2>
<p>The labeling features can use the databases provided by MaxMind using the GeoIP LGPL libraries. If your code was configured to use these libraries, then enable the features here. </p>
<p> GeoIP provides a lot of support for geo-location, configure support by enabling a feature and providing the appropriate binary data files. ASN reporting is done from a separate set of data files, obtained from MaxMind.com, and so enabling this feature is independent of the traditional city data available.</p>
<h2>Ralabel_Geoip_Asn</h2>
<p>Labeling data with Origin ASN values involves simply indicating the desire, and the filename for the database of ASN numbers. </p>
<pre><code>RALABEL_GEOIP_ASN</code>=yes
<code>RALABEL_GEOIP_ASN_FILE</code>=&quot;/usr/local/share/GeoIP/GeoIPASNum.dat&quot;</pre>
<h2>Ralabel_Geoip_City</h2>
<p>Data for city relevant data is enabled through enabling and configuring the city database support. The types of data available are:<br />
&nbsp;<wbr>&nbsp;<wbr>country_code, country_code3, country_name, region, city, postal_code,<br />
&nbsp;<wbr>&nbsp;<wbr>latitude, longitude, metro_code, area_code and continent_code.<br />
&nbsp;<wbr>&nbsp;<wbr>time_offset is also available.&nbsp;<wbr>&nbsp;<wbr> </p>
<p> The concept is that you should be able to add semantics for any IP address that is in the argus record. Support addresses are:<br />
&nbsp;<wbr>&nbsp;<wbr>saddr, daddr, inode </p>
<p> The labels provided will be tagged as:<br />
&nbsp;<wbr>&nbsp;<wbr>scity, dcity, icity </p>
<p> To configure what you want to have placed in the label, use the list of objects, in whatever order you like, as the RALABLE_GEOPIP_CITY string using these keywords:<br />
&nbsp;<wbr>&nbsp;<wbr>cco&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; country_code<br />
&nbsp;<wbr>&nbsp;<wbr>cco3&nbsp;<wbr>&nbsp;<wbr>&#8211; country_code3<br />
&nbsp;<wbr>&nbsp;<wbr>cname &#8211; country_name<br />
&nbsp;<wbr>&nbsp;<wbr>reg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; region<br />
&nbsp;<wbr>&nbsp;<wbr>city&nbsp;<wbr>&nbsp;<wbr>&#8211; city<br />
&nbsp;<wbr>&nbsp;<wbr>pcode &#8211; postal_code<br />
&nbsp;<wbr>&nbsp;<wbr>lat&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; latitude<br />
&nbsp;<wbr>&nbsp;<wbr>long&nbsp;<wbr>&nbsp;<wbr>&#8211; longitude<br />
&nbsp;<wbr>&nbsp;<wbr>metro &#8211; metro_code<br />
&nbsp;<wbr>&nbsp;<wbr>area&nbsp;<wbr>&nbsp;<wbr>&#8211; area_code<br />
&nbsp;<wbr>&nbsp;<wbr>cont&nbsp;<wbr>&nbsp;<wbr>&#8211; continent_code<br />
&nbsp;<wbr>&nbsp;<wbr>off&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; GMT time offset </p>
<p> Working examples could be:<br />
&nbsp;<wbr>&nbsp;<wbr>RALABEL_GEOIP_CITY=&quot;saddr,daddr:lat/lon&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>RALABEL_GEOIP_CITY=&quot;*:city,region,cname,lat,lon&quot;<br />
&nbsp;<wbr> </p>
<pre><code>RALABEL_GEOIP_CITY</code>=&quot;saddr,daddr,inode:lat,lon&quot;
<code>RALABEL_GEOIP_CITY_FILE</code>=&quot;/usr/local/share/GeoIP/GeoIPCity.dat&quot;</pre>
<h2>Copyright</h2>
<p>Copyright (c) 2000-2016 QoSient All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ralabel/">ralabel</a></code>(1) </p>
