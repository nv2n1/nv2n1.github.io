---
title: "rate(5)"
name: "rate"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rate/"
description: "/etc/isdn/rate.conf – rate and provider configuration"
---

<p>/etc/isdn/rate.conf &#8211; rate and provider configuration</p>
<h2>Description</h2>
<p>isdnlog and related programs like isdnrep or isdnrate obtain the information about telephone rates or fees from a rate-file. In addition to the general data from the rate-file it is necessary to provide information about the individual situation. This is the purpose of the configuration file rate.conf. Words below consisting of uppercase letters like <font SIZE="-1"><code>RATEFILE</code></font> refer to the so named setting in the general isdnlog configuration file <i>/etc/isdn/isdn.conf</i>.</p>
<h3>General Concepts</h3>
<p>The rate-file contains one or more providers for a country. A provider covers an offer of a telephone company. Usually there are now many telephone companies in a country and most companies offer several different price lists. A provider is identified by provider number and provider variant or sub number. The provider number, short <i>pnum</i>, is commonly used for all offers of one company. The provider variant, short <i>var</i>, is used to number these offers starting from 0. A specific provider is referenced as <i>pnum</i><code>,</code><i>var</i> or <i>pnum</i><code>_</code><i>var</i> depending on the context. <font SIZE="-1"><code>VBN</code></font> contains the shared leading digits of the carrier selection prefixes. The entire prefix for a provider is specified in the rate-file by the B: tag. In Germany the carrier selection prefix begins with 010 followed by two or three digits which make the <i>pnum</i> ranging from 10 to 199. A mapping like this is not required but common. The overall format of rate.conf is similar to the rate-file, lines starting with tags <code>P:</code>, <code>X:</code>, or <code>Q:</code> may occur in any order and quantity. (Of course, the resulting configuration should make sense.)</p>
<h3>Provider Booking</h3>
<p><code>P:</code><i>pnum</i><code>=</code><i>var</i> Mark the provider specified by <i>pnum</i> and <i>var</i> as booked or active. Only booked providers are taken into account when isdnlog computes the connection costs. Booking also tells isdnlog the provider variant to use if there are more than one. Beside computation of real connections booking also splits the providers in two groups: the booked ones that are available at the specific subscriber line at the not booked ones that are less important for price comparison. One provider in booked group is declared the default provider by setting <font SIZE="-1"><code>PRESELECTED</code></font> to its <i>pnum</i>. This provider is assumed to be used if a connection is made without a carrier selection prefix and no exceptions matching.</p>
<h3>Exceptions to Provider Selection</h3>
<pre><code>X:</code><i>number</i><code>=</code><i>pnum</i>
<code>X:</code><i>number</i><code>=</code><i>pnum</i><code>z</code><i>zone</i></pre>
<p>Connections to <i>number</i> will be assigned the booked provider with <i>pnum</i> as provider number regardless of a dialed provider selection prefix or the <font SIZE="-1"><code>PRESELECTED</code></font> setting. <i>zone</i> if present replaces the normal zone selection based on destination codes. Exceptions can also be given in the rate-file. In rate.conf exceptions may become necessary if there different preselected providers for local and distance calls for example or if preselection does not apply generally, e.g. not for connections to special numbers.</p>
<h3>Provider Skipping</h3>
<p>At least for some countries there are universal rate-files distributed with isdnlog or provided elsewhere. In this case it is desirable to keep the rate-file unmodified so that updates require no further changes beyond installing the new rate-file. If a rate-file aims to cover the telephone market in an entire nation there will be always providers in it which are not available or not suitable for a specific installation. Such providers can be disabled by not booking them but they remain present and may be displayed as overall cheapest provider or the like. Provider skipping completely ignores selected, so called skipped providers, from the rate-file. To be more precise, the effect of skipped provider could also be achieved by deleting its lines starting from its P: tag to the last line before the P: tag of the next provider from the rate-file. Providers to skip can also be configured in the parameter file of isdnlog using the syntax described below in a line starting with <code>skipProv=</code> instead of <code>Q:</code>. <code>Q:</code>[<code>!</code>|<code>~</code>]<i>list</i></p>
<dl>
<dt><i>list</i></p>
<dd>:= <i>range</i>[<code>;</code><i>list</i>]</p>
<dt><i>range</i></p>
<dd>:= (<code>*</code>|<i>prov</i>|<i>prov</i><code>&#8211;</code>|<code>&#8211;</code><i>prov</i>|<i>prov</i><code>&#8211;</code>prov)[<code>!</code>|<code>~</code>]</p>
<dt><i>prov</i></p>
<dd>:= <i>pnum</i>[<code>,</code><i>var</i>]  Skipping applies to all providers that are matched by a given <i>range.</i> If <i>var</i> is missing, all providers with <i>pnum</i> are skipped. <code>*</code> matches all providers. Booked providers are not skipped unless <code>!</code> is given at end of the <i>range</i> or in front of the entire list where it applies to whole line. The <code>~</code> can be given alternatively to <code>!.</code> Providers that match such a <i>range</i> are not skipped under any circumstances. Space can occur anywhere in the line after <code>Q:.</code> Example:<br />
 Q:*; 13,1~; 33-33,1~; 200-299!; 321-323! This skips all not booked providers except 13_1, 33_0, and 33_1. Additionally all providers with a <i>pnum</i> between 200 and 299 or 321 and 323 are skipped. </p>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/rate.conf</code></p>
<dd>This file. <font SIZE="-1"><code>RATECONF</code></font> may be used to specify an alternative rate and provider configuration file. </p>
<dt><code>/usr/share/isdn/rate-</code><i>CC</i><code>.dat</code></p>
<dd>The rate-file for your country. Replace <i>CC</i> with your two letter country code, e.g. <i>de</i> for Germany. <font SIZE="-1"><code>RATEFILE</code></font> defines the rate-file to use. </p>
</dl>
<h2>Author</h2>
<p>Tobias Becker &lt;tobiasb [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-isdnlog/">isdnlog</a></code>(8) <code><a href="/docs/linux/man/5-rate-files/">rate-files</a></code>(5) <code><a href="/docs/linux/man/5-isdn-conf/">isdn.conf</a></code>(5) </p>
